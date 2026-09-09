import os
import sys
import sqlite3
import pandas as pd
import streamlit as st

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.spatial_math import segment_building
from core.ulpin_logic import generate_ulpin, decode_ulpin
from core.collision_engine import check_parcel_conflicts, run_national_audit
from core.certificate_generator import generate_bhu_aadhaar_pdf
from frontend.map_engine import render_3d_map, CITY_VIEWPORTS, MAP_STYLES
from frontend.ui_components import (
    inject_custom_theme, 
    render_header, 
    render_kpi_bar, 
    render_property_spec_card, 
    render_vertical_stack,
    render_clash_report_ui,
    render_bhu_aadhaar_card_preview
)

# Page configuration
st.set_page_config(
    layout="wide", 
    page_title="Bhu-Aadhaar 3D | Pan-India Cadastral System", 
    page_icon="🏙️",
    initial_sidebar_state="collapsed"
)

# Initialize theme state (default: dark)
if "theme" not in st.session_state:
    st.session_state["theme"] = "dark"

current_theme = st.session_state["theme"]

# Invalidate any stale Streamlit data caches
st.cache_data.clear()

# Apply curated modern design system (Light / Dark)
inject_custom_theme(theme=current_theme)

# Top Portal Header with Light/Dark Switch Button
render_header(theme=current_theme)

def load_data():
    db_path = os.path.join(os.path.dirname(__file__), 'database', 'spatial_records.db')
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * FROM property_parcels", conn)
    conn.close()
    
    if 'city' not in df.columns:
        from database.db_setup import initialize_db
        initialize_db()
        conn = sqlite3.connect(db_path)
        df = pd.read_sql_query("SELECT * FROM property_parcels", conn)
        conn.close()
        
    return df

try:
    df = load_data()
except Exception as e:
    st.error(f"Database error: {e}. Please run `python database/db_setup.py`.")
    st.stop()

# National Summary KPI Row
render_kpi_bar(df, theme=current_theme)

st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)

# -------------------------------------------------------------
# GLOBAL 3D ULPIN SEARCH & INSTANT DECODER BAR
# -------------------------------------------------------------
with st.container():
    c_search, c_btn = st.columns([4, 1], gap="small")
    with c_search:
        search_query = st.text_input(
            "🔍 Global 3D ULPIN / Title Verification Search:",
            placeholder="Search by 14-digit ULPIN (e.g. 27211010500101-004) or Property Name (e.g. Seawoods, Cyber Towers, GIFT)...",
            label_visibility="collapsed"
        )
    with c_btn:
        search_clicked = st.button("🔎 Verify & Locate", use_container_width=True)

searched_prop_id = None
searched_floor_target = None

if search_query.strip():
    clean_q = search_query.strip()
    
    # Check if query matches 14-digit ULPIN format
    if ("-" in clean_q or len(clean_q) == 14) and any(c.isdigit() for c in clean_q):
        decoded = decode_ulpin(clean_q)
        if decoded["valid"]:
            searched_prop_id = decoded["plot_id"]
            searched_floor_target = decoded["floor_number"]
            
            if current_theme == "light":
                banner_bg = "rgba(2, 132, 199, 0.08)"
                banner_border = "rgba(2, 132, 199, 0.3)"
                title_c = "#0284c7"
                code_bg = "#e2e8f0"
                code_c = "#0f172a"
                badge_bg = "rgba(168, 85, 247, 0.12)"
                badge_c = "#7e22ce"
            else:
                banner_bg = "rgba(6, 182, 212, 0.12)"
                banner_border = "rgba(6, 182, 212, 0.3)"
                title_c = "#38bdf8"
                code_bg = "rgba(0,0,0,0.3)"
                code_c = "#ffffff"
                badge_bg = "rgba(168, 85, 247, 0.2)"
                badge_c = "#c084fc"

            st.markdown(f"""
                <div style="background: {banner_bg}; border: 1px solid {banner_border}; border-radius: 8px; padding: 8px 14px; margin-bottom: 12px; display: flex; align-items: center; justify-content: space-between; font-size: 0.8rem;">
                    <div>
                        <span style="font-weight: 700; color: {title_c};">Parsed Bhu-Aadhaar ULPIN:</span>
                        <code style="color: {code_c}; background: {code_bg}; padding: 2px 6px; border-radius: 4px;">{decoded['raw_ulpin']}</code>
                        &bull; State: <b>{decoded['state_name']}</b> (LGD {decoded['state_code']}) &bull; Plot: <b>#{decoded['plot_id']}</b>
                    </div>
                    <span style="background: {badge_bg}; color: {badge_c}; padding: 2px 8px; border-radius: 4px; font-weight: 700;">
                        {decoded['floor_description']}
                    </span>
                </div>
            """, unsafe_allow_html=True)
    else:
        # Search by name or city
        matched = df[df['name'].str.contains(clean_q, case=False, na=False) | df['city'].str.contains(clean_q, case=False, na=False)]
        if not matched.empty:
            searched_prop_id = matched.iloc[0]['property_id']
            st.success(f"Matched Cadastral Record: #{searched_prop_id} - {matched.iloc[0]['name']} ({matched.iloc[0]['city']})")
        else:
            st.warning(f"No cadastral record matched query: '{clean_q}'")

st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)

# -------------------------------------------------------------
# ROLE-BASED NAVIGATION SYSTEM (SIH 2026 Core Workflow)
# -------------------------------------------------------------
selected_role = st.radio(
    "Select Operating Persona:",
    options=[
        "🏠 Citizen / Homebuyer Mode",
        "📐 Government GIS Surveyor Mode",
        "🏛️ Sub-Registrar (Revenue Officer) Mode"
    ],
    horizontal=True,
    label_visibility="collapsed"
)

st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

# -------------------------------------------------------------
# GEOGRAPHIC VIEWPORT & BASEMAP CONTROLS
# -------------------------------------------------------------
c_reg, c_mode, c_thm = st.columns([2.5, 1.2, 1.3], gap="medium")
with c_reg:
    region_options = list(CITY_VIEWPORTS.keys())
    selected_region = st.selectbox(
        "📍 Geographic Viewport:",
        options=region_options,
        index=0,
        help="Navigate 3D map across national scale down to metro hubs."
    )
with c_mode:
    filter_parcels_by_region = st.toggle(
        "Filter data to active region",
        value=False,
        help="If disabled, shows all Pan-India parcels simultaneously."
    )
with c_thm:
    map_style_options = list(MAP_STYLES.keys())
    # Smart default basemap based on active theme
    default_basemap = "Minimalist Light" if current_theme == "light" else "Dark Matter (Default)"
    if "basemap_aesthetic" not in st.session_state:
        st.session_state["basemap_aesthetic"] = default_basemap
    
    # Check if session state value is valid in options
    if st.session_state["basemap_aesthetic"] in map_style_options:
        default_index = map_style_options.index(st.session_state["basemap_aesthetic"])
    else:
        default_index = 0

    selected_theme = st.selectbox(
        "🗺️ Basemap Aesthetic:",
        options=map_style_options,
        index=default_index,
        key="basemap_select_box"
    )
    st.session_state["basemap_aesthetic"] = selected_theme

# Filter Dataset based on region preference
if filter_parcels_by_region and selected_region != "🇮🇳 Pan-India (Subcontinent)":
    target_city = selected_region.split(" ")[0]
    if 'city' in df.columns:
        display_df = df[df['city'].str.contains(target_city, case=False, na=False) | df['name'].str.contains(target_city, case=False, na=False)]
    else:
        display_df = df.copy()
    if display_df.empty:
        display_df = df.copy()
else:
    display_df = df.copy()

# -------------------------------------------------------------
# MAIN WORKSPACE: 3D MAP ON LEFT, ROLE-BASED PANEL ON RIGHT
# -------------------------------------------------------------
col_map, col_panel = st.columns([2.6, 1.4], gap="large")

with col_map:
    # Filter Bar directly above map
    f1, f2, f3 = st.columns([2.2, 1.2, 0.8])
    with f1:
        all_types = sorted(df['type'].unique().tolist())
        selected_types = st.multiselect(
            "Layer Categories:",
            options=all_types,
            default=all_types,
            label_visibility="collapsed"
        )
    with f2:
        show_underground = st.toggle("Subsurface Infrastructure", value=True)
    with f3:
        active_count_color = "#64748b" if current_theme == "light" else "#94a3b8"
        st.markdown(
            f"<div style='text-align: right; padding-top: 6px; font-size: 0.8rem; color: {active_count_color}; font-weight: 600; font-family: monospace;'>Active: {len(display_df)}</div>",
            unsafe_allow_html=True
        )

    # Apply filters
    filtered_map_df = display_df[display_df['type'].isin(selected_types)]
    if not show_underground:
        filtered_map_df = filtered_map_df[filtered_map_df['base_elevation'] >= 0]

    map_placeholder = st.empty()

    # Minimalist Map Legend
    leg_bg = "#ffffff" if current_theme == "light" else "rgba(15, 23, 42, 0.5)"
    leg_border = "#e2e8f0" if current_theme == "light" else "rgba(255, 255, 255, 0.06)"
    leg_shadow = "0 2px 8px rgba(15, 23, 42, 0.04)" if current_theme == "light" else "none"
    leg_text = "#334155" if current_theme == "light" else "#cbd5e1"

    st.markdown(f"""
        <div style="display: flex; gap: 16px; flex-wrap: wrap; align-items: center; justify-content: center; background: {leg_bg}; border: 1px solid {leg_border}; padding: 8px 16px; border-radius: 10px; margin-top: 8px; font-size: 0.76rem; box-shadow: {leg_shadow};">
            <div style="display: flex; align-items: center; gap: 6px;"><span style="width: 10px; height: 10px; border-radius: 2px; background: #00d4ff;"></span> <span style="color: {leg_text};">Commercial</span></div>
            <div style="display: flex; align-items: center; gap: 6px;"><span style="width: 10px; height: 10px; border-radius: 2px; background: #a855f7;"></span> <span style="color: {leg_text};">Residential</span></div>
            <div style="display: flex; align-items: center; gap: 6px;"><span style="width: 10px; height: 10px; border-radius: 2px; background: #fb923c;"></span> <span style="color: {leg_text};">Underground Parking</span></div>
            <div style="display: flex; align-items: center; gap: 6px;"><span style="width: 10px; height: 10px; border-radius: 2px; background: #10b981;"></span> <span style="color: {leg_text};">Transit Hub</span></div>
            <div style="display: flex; align-items: center; gap: 6px;"><span style="width: 10px; height: 10px; border-radius: 2px; background: #f43f5e;"></span> <span style="color: {leg_text};">Subsurface Utility</span></div>
        </div>
    """, unsafe_allow_html=True)

with col_panel:
    parcel_options = filtered_map_df['property_id'].tolist() if not filtered_map_df.empty else df['property_id'].tolist()
    
    def format_parcel_option(pid):
        matching = df[df['property_id'] == pid]
        if matching.empty:
            return f"#{pid}"
        row = matching.iloc[0]
        name = row.get('name', f"Parcel #{pid}")
        city = row.get('city', 'India')
        return f"#{pid} - {name} ({city})"

    default_index = 0
    if searched_prop_id and searched_prop_id in parcel_options:
        default_index = parcel_options.index(searched_prop_id)

    selected_prop_id = st.selectbox(
        "Select Target Parcel to Analyze:",
        options=parcel_options,
        index=default_index,
        format_func=format_parcel_option,
        label_visibility="collapsed"
    )

    prop_data = df[df["property_id"] == selected_prop_id].iloc[0]

    # Focus Camera Option (Auto-checked if searched directly)
    focus_camera = st.checkbox("🎯 Lock 3D Camera to Selected Parcel", value=(searched_prop_id is not None))
    custom_center = {"lat": prop_data["lat"], "lon": prop_data["lon"]} if focus_camera else None

    # Render Dossier Card
    render_property_spec_card(prop_data, theme=current_theme)

    # Slicing floors
    floors = segment_building(prop_data["total_height"], prop_data["base_elevation"])
    
    # Determine default selected floor
    floor_opts = [f['floor_number'] for f in floors]
    default_f_idx = 0
    if searched_floor_target and searched_floor_target in floor_opts:
        default_f_idx = floor_opts.index(searched_floor_target)

    # -------------------------------------------------------------
    # PERSONA 1: CITIZEN / HOMEBUYER MODE
    # -------------------------------------------------------------
    if "Citizen" in selected_role:
        cit_bg = "#ffffff" if current_theme == "light" else "rgba(15, 23, 42, 0.6)"
        cit_border = "#e2e8f0" if current_theme == "light" else "rgba(255, 255, 255, 0.06)"
        cit_shadow = "0 2px 10px rgba(15, 23, 42, 0.04)" if current_theme == "light" else "none"
        cit_title = "#0284c7" if current_theme == "light" else "#38bdf8"
        cit_text = "#334155" if current_theme == "light" else "#cbd5e1"
        cit_green = "#059669" if current_theme == "light" else "#34d399"

        st.markdown(f"""
            <div style="background: {cit_bg}; border: 1px solid {cit_border}; border-radius: 10px; padding: 12px; margin-bottom: 12px; box-shadow: {cit_shadow};">
                <div style="font-size: 0.84rem; font-weight: 700; color: {cit_title}; margin-bottom: 6px;">
                    🛡️ Official Title & Encumbrance Verification
                </div>
                <div style="font-size: 0.76rem; color: {cit_text}; line-height: 1.5;">
                    &bull; <b>RERA Status:</b> <span style="color: {cit_green};">Approved & Active</span><br/>
                    &bull; <b>Encumbrance / Mortgage:</b> <span style="color: {cit_green};">NIL (Clear Freehold Title)</span><br/>
                    &bull; <b>Building Height Sanction:</b> Compliant with Municipal Bye-Laws
                </div>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("<b>Select Your Unit / Floor Level:</b>", unsafe_allow_html=True)
        selected_floor_num = st.selectbox(
            "Floor Level:",
            options=floor_opts,
            index=default_f_idx,
            format_func=lambda n: f"Basement {abs(n):02d} (Subsurface)" if n < 0 else f"Floor {n:02d} (Superstructure)",
            label_visibility="collapsed"
        )
        selected_floor_dict = next(f for f in floors if f['floor_number'] == selected_floor_num)

        active_ulpin = generate_ulpin(
            int(prop_data.get("state_code", 27)),
            int(prop_data.get("dist_code", 21)),
            int(prop_data.get("sub_dist_code", 101)),
            int(prop_data.get("village_code", 50)),
            int(selected_prop_id),
            selected_floor_num
        )

        # Digital Bhu-Aadhaar Certificate Preview
        render_bhu_aadhaar_card_preview(prop_data, selected_floor_dict, active_ulpin, theme=current_theme)

        st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)

        # 1-Click PDF Certificate Download
        pdf_bytes = generate_bhu_aadhaar_pdf(prop_data, selected_floor_dict, active_ulpin)
        st.download_button(
            label="📜 Download Official 3D Bhu-Aadhaar Certificate (PDF)",
            data=pdf_bytes,
            file_name=f"3D_Bhu_Aadhaar_Certificate_{active_ulpin}.pdf",
            mime="application/pdf",
            type="primary",
            use_container_width=True
        )

    # -------------------------------------------------------------
    # PERSONA 2: GOVERNMENT GIS SURVEYOR MODE
    # -------------------------------------------------------------
    elif "Surveyor" in selected_role:
        st.markdown("""
            <div style="font-size: 0.88rem; font-weight: 700; color: #fb923c; margin-bottom: 6px;">
                📐 3D Spatial Metrics & FAR Analysis
            </div>
        """, unsafe_allow_html=True)

        ground_area = 1200.0 # Approximate default parcel footprint m2
        built_up_area = ground_area * len(floors)
        total_vol = ground_area * float(prop_data['total_height'])
        fsi = built_up_area / ground_area

        s1, s2, s3 = st.columns(3)
        s1.metric("Gross Volume", f"{total_vol:,.0f} m³")
        s2.metric("Built-up Area", f"{built_up_area:,.0f} m²")
        s3.metric("Computed FSI", f"{fsi:.1f}")

        st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)

        # 3D Clash & Encroachment Detection Tool
        st.markdown("""
            <div style="font-size: 0.88rem; font-weight: 700; color: #f43f5e; margin-bottom: 6px;">
                ⚠️ Subsurface 3D Clash & Buffer Audit
            </div>
        """, unsafe_allow_html=True)

        conflicts = check_parcel_conflicts(prop_data, df, safety_buffer=25.0)
        render_clash_report_ui(conflicts, theme=current_theme)

        st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)

        # Architectural cross-section visualizer
        render_vertical_stack(floors, prop_data, theme=current_theme)

        # Ingest New Parcel Expander
        with st.expander("➕ Ingest New 3D Parcel Coordinates", expanded=False):
            with st.form("new_parcel_form"):
                new_name = st.text_input("Parcel / Building Name:")
                new_city = st.selectbox("City:", ["Navi Mumbai", "Mumbai", "New Delhi", "Bengaluru", "GIFT City", "Hyderabad", "Chennai", "Kolkata"])
                new_type = st.selectbox("Type:", ["Commercial", "Apartment", "Underground Parking", "Transit", "Subsurface Utility"])
                n_col1, n_col2 = st.columns(2)
                with n_col1:
                    new_lat = st.number_input("Latitude:", value=float(prop_data['lat']), format="%.5f")
                    new_height = st.number_input("Height (m):", value=45.0, min_value=3.0)
                with n_col2:
                    new_lon = st.number_input("Longitude:", value=float(prop_data['lon']), format="%.5f")
                    new_base_elev = st.number_input("Base Elevation (m):", value=0.0)
                new_owner = st.text_input("Owner / Agency:", value="Urban Development Authority")
                
                submitted = st.form_submit_button("💾 Commit 3D Parcel to SQLite Database", type="primary")
                if submitted and new_name.strip():
                    db_path = os.path.join(os.path.dirname(__file__), 'database', 'spatial_records.db')
                    conn = sqlite3.connect(db_path)
                    cur = conn.cursor()
                    max_id = cur.execute("SELECT MAX(property_id) FROM property_parcels").fetchone()[0] or 100
                    new_id = max_id + 1
                    cur.execute("""
                        INSERT INTO property_parcels 
                        (property_id, name, city, state, state_code, dist_code, sub_dist_code, village_code, type, lat, lon, base_elevation, total_height, owner, status, valuation_cr, zone)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (new_id, new_name, new_city, prop_data['state'], int(prop_data['state_code']), int(prop_data['dist_code']), 101, 50, new_type, new_lat, new_lon, new_base_elev, new_height, new_owner, 'Verified 3D Cadastre', 250.0, 'Commercial Core'))
                    conn.commit()
                    conn.close()
                    st.success(f"Successfully ingested 3D Parcel #{new_id}: {new_name}!")
                    st.rerun()

    # -------------------------------------------------------------
    # PERSONA 3: SUB-REGISTRAR (REVENUE OFFICER) MODE
    # -------------------------------------------------------------
    elif "Sub-Registrar" in selected_role:
        st.markdown("""
            <div style="font-size: 0.88rem; font-weight: 700; color: #a855f7; margin-bottom: 6px;">
                🏛️ Vertical Title Transfer & Deed Registration
            </div>
        """, unsafe_allow_html=True)
        sub_desc_col = "#64748b" if current_theme == "light" else "#94a3b8"
        st.markdown(f"""
            <div style="font-size: 0.76rem; color: {sub_desc_col}; margin-bottom: 10px;">
                Legally transfer individual vertical airspace titles with immutable cryptographic deed records.
            </div>
        """, unsafe_allow_html=True)

        target_floor_to_transfer = st.selectbox(
            "Select Floor Unit to Convey:",
            options=floor_opts,
            index=default_f_idx,
            format_func=lambda n: f"Basement {abs(n):02d} (Subsurface)" if n < 0 else f"Floor {n:02d} (Superstructure)"
        )
        
        t_col1, t_col2 = st.columns(2)
        with t_col1:
            st.caption("Current Grantor (Seller):")
            st.code(prop_data['owner'])
        with t_col2:
            buyer_name = st.text_input("Grantee (New Buyer):", placeholder="e.g. Parijat Sharma / Reliance Infra")

        stamp_duty = (prop_data.get('valuation_cr', 0) * 0.06) # 6% standard state stamp duty
        stamp_bg = "rgba(168, 85, 247, 0.08)" if current_theme == "light" else "rgba(168, 85, 247, 0.1)"
        stamp_border = "rgba(168, 85, 247, 0.2)" if current_theme == "light" else "rgba(168, 85, 247, 0.25)"
        stamp_duty_col = "#7e22ce" if current_theme == "light" else "#c084fc"
        stamp_paid_col = "#059669" if current_theme == "light" else "#34d399"

        st.markdown(f"""
            <div style="background: {stamp_bg}; border: 1px solid {stamp_border}; border-radius: 8px; padding: 8px 12px; margin-bottom: 12px; font-size: 0.78rem;">
                Estimated State Stamp Duty (6%): <b style="color: {stamp_duty_col};">₹ {stamp_duty:.2f} Crores</b> &bull; Registration Fee: <b style="color: {stamp_paid_col};">PAID</b>
            </div>
        """, unsafe_allow_html=True)

        if st.button("✍️ Execute Digital Vertical Deed Transfer", type="primary", use_container_width=True):
            if not buyer_name.strip():
                st.error("Please enter the name of the new buyer / grantee.")
            else:
                db_path = os.path.join(os.path.dirname(__file__), 'database', 'spatial_records.db')
                conn = sqlite3.connect(db_path)
                cur = conn.cursor()
                cur.execute("UPDATE property_parcels SET owner = ? WHERE property_id = ?", (buyer_name.strip(), int(selected_prop_id)))
                conn.commit()
                conn.close()
                st.success(f"Vertical Title for Parcel #{selected_prop_id} successfully conveyed to {buyer_name}!")
                st.rerun()

        # Architectural cross-section visualizer
        render_vertical_stack(floors, prop_data, theme=current_theme)

# Render the 3D Map in the map column placeholder with exact active parameters
with col_map:
    deck = render_3d_map(
        filtered_map_df,
        selected_region=selected_region,
        custom_center=custom_center,
        map_theme=selected_theme
    )
    map_placeholder.pydeck_chart(deck, use_container_width=True)

# -------------------------------------------------------------
# BOTTOM DRAWER: MASTER CADASTRAL DATABASE & NATIONAL AUDIT
# -------------------------------------------------------------
st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
with st.expander("🗄️ National 3D Cadastral Registry & All-India Clash Audit", expanded=False):
    t1, t2, t3 = st.tabs([
        "📋 Tabular Cadastre Register", 
        "⚠️ Pan-India Encroachment Audit", 
        "📊 Spatial Analytics"
    ])
    
    with t1:
        cols_to_show = [c for c in [
            'property_id', 'name', 'city', 'state', 'type', 'total_height', 
            'base_elevation', 'valuation_cr', 'owner', 'status'
        ] if c in df.columns]
        st.dataframe(
            df[cols_to_show],
            use_container_width=True,
            hide_index=True
        )
        
    with t2:
        st.caption("Automated spatial audit of subterranean safety corridors across all Indian metros:")
        all_national_clashes = run_national_audit(df, safety_buffer=20.0)
        render_clash_report_ui(all_national_clashes, theme=current_theme)

    with t3:
        c_chart1, c_chart2 = st.columns(2)
        with c_chart1:
            st.caption("Distribution of 3D Cadastre Assets by Category")
            type_counts = df['type'].value_counts()
            st.bar_chart(type_counts)
        with c_chart2:
            st.caption("Asset Valuation by Metro Region (₹ Crores)")
            if 'city' in df.columns and 'valuation_cr' in df.columns:
                city_vals = df.groupby('city')['valuation_cr'].sum()
                st.bar_chart(city_vals)