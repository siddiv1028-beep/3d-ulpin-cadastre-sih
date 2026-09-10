import streamlit as st
from core.certificate_generator import generate_qr_code_image, generate_title_hash
from data.blueprints_and_imagery import get_property_blueprint

def inject_custom_theme(theme="dark"):
    """
    Injects a curated modern GIS dashboard design system supporting both Dark and Light modes.
    Ensures seamless glassmorphic styling, high contrast typography, crisp metric cards,
    and responsive interactive controls.
    """
    is_light = theme == "light"
    
    if is_light:
        theme_css = """
        /* Light Theme Design System */
        .stApp {
            background-color: #f8fafc !important;
            background: radial-gradient(circle at 50% 0%, #ffffff 0%, #f8fafc 85%) !important;
            color: #0f172a !important;
        }

        html, body, [class*="css"] {
            font-family: 'Plus Jakarta Sans', sans-serif;
            color: #0f172a;
        }

        p, span, label, div {
            color: #1e293b;
        }

        h1, h2, h3, h4, h5, h6 {
            color: #0f172a !important;
        }

        /* Minimalist Modern Metric Cards - Light */
        div[data-testid="stMetric"] {
            background: #ffffff !important;
            border: 1px solid #e2e8f0 !important;
            border-radius: 12px !important;
            padding: 14px 18px !important;
            box-shadow: 0 4px 16px rgba(15, 23, 42, 0.05) !important;
            transition: all 0.25s ease !important;
        }

        div[data-testid="stMetric"]:hover {
            border-color: rgba(2, 132, 199, 0.4) !important;
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 25px rgba(2, 132, 199, 0.12) !important;
        }

        div[data-testid="stMetricLabel"] p {
            font-size: 0.78rem !important;
            font-weight: 700 !important;
            text-transform: uppercase !important;
            letter-spacing: 0.08em !important;
            color: #64748b !important;
            margin-bottom: 4px !important;
        }

        div[data-testid="stMetricValue"] {
            font-size: 1.55rem !important;
            font-weight: 800 !important;
            color: #0284c7 !important;
            font-family: 'JetBrains Mono', monospace !important;
        }

        /* Selectboxes & Multiselects - Light */
        div[data-baseweb="select"] {
            border-radius: 10px;
        }
        
        div[data-baseweb="select"] > div {
            background-color: #ffffff !important;
            border-color: #cbd5e1 !important;
            border-radius: 10px !important;
            color: #0f172a !important;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05) !important;
        }

        div[data-baseweb="select"] * {
            color: #0f172a !important;
        }

        div[data-baseweb="popover"] div {
            background-color: #ffffff !important;
            color: #0f172a !important;
        }

        /* Inputs & Textareas - Light */
        div[data-baseweb="input"] {
            background-color: #ffffff !important;
            border-color: #cbd5e1 !important;
            border-radius: 10px !important;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05) !important;
        }

        input[data-testid="stTextInput"], input[data-testid="stNumberInput"] {
            color: #0f172a !important;
            background-color: #ffffff !important;
        }

        input::placeholder {
            color: #94a3b8 !important;
        }

        /* Expander - Light */
        .streamlit-expanderHeader {
            background-color: #ffffff !important;
            border-radius: 10px !important;
            border: 1px solid #e2e8f0 !important;
            font-weight: 600 !important;
            color: #0f172a !important;
            box-shadow: 0 2px 8px rgba(15, 23, 42, 0.03) !important;
        }

        .streamlit-expanderContent {
            background-color: #ffffff !important;
            border: 1px solid #e2e8f0 !important;
            border-top: none !important;
            border-radius: 0 0 10px 10px !important;
        }

        /* Tabs styling - Light */
        button[data-baseweb="tab"] {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-weight: 600 !important;
            font-size: 0.88rem !important;
            color: #64748b !important;
        }

        button[data-baseweb="tab"][aria-selected="true"] {
            color: #0284c7 !important;
            border-bottom-color: #0284c7 !important;
        }

        /* Radio buttons - Light */
        div[data-testid="stRadio"] label span {
            color: #1e293b !important;
            font-weight: 600 !important;
        }

        div[data-testid="stRadio"] [data-testid="stMarkdownContainer"] p {
            color: #1e293b !important;
        }

        /* Checkbox & Toggle - Light */
        div[data-testid="stCheckbox"] label span, div[data-testid="stToggle"] label span {
            color: #1e293b !important;
            font-weight: 600 !important;
        }

        /* Dataframe / Table - Light */
        div[data-testid="stDataFrame"] {
            background-color: #ffffff !important;
            border: 1px solid #e2e8f0 !important;
            border-radius: 8px !important;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04) !important;
        }

        /* Theme Toggle Button - Light */
        .st-key-theme_toggle_btn button {
            background: linear-gradient(135deg, #ffffff 0%, #f1f5f9 100%) !important;
            border: 1px solid #cbd5e1 !important;
            color: #0f172a !important;
            border-radius: 12px !important;
            font-weight: 700 !important;
            font-size: 0.82rem !important;
            height: 44px !important;
            transition: all 0.25s ease !important;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06) !important;
        }

        .st-key-theme_toggle_btn button:hover {
            background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%) !important;
            border-color: #0284c7 !important;
            color: #0284c7 !important;
            transform: translateY(-1px) !important;
            box-shadow: 0 4px 14px rgba(2, 132, 199, 0.18) !important;
        }

        /* Custom Scrollbars - Light */
        ::-webkit-scrollbar-track {
            background: #f1f5f9;
        }
        ::-webkit-scrollbar-thumb {
            background: #cbd5e1;
            border-radius: 3px;
        }
        """
    else:
        theme_css = """
        /* Dark Theme Design System */
        .stApp {
            background-color: #0b0f19 !important;
            background: radial-gradient(circle at 50% 0%, #111827 0%, #0b0f19 80%) !important;
            color: #e2e8f0 !important;
        }

        html, body, [class*="css"] {
            font-family: 'Plus Jakarta Sans', sans-serif;
            color: #e2e8f0;
        }

        p, span, label, div {
            color: #cbd5e1;
        }

        h1, h2, h3, h4, h5, h6 {
            color: #f8fafc !important;
        }

        /* Minimalist Modern Metric Cards - Dark */
        div[data-testid="stMetric"] {
            background: linear-gradient(135deg, rgba(30, 41, 59, 0.7) 0%, rgba(15, 23, 42, 0.8) 100%) !important;
            border: 1px solid rgba(255, 255, 255, 0.08) !important;
            border-radius: 12px !important;
            padding: 14px 18px !important;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25) !important;
            transition: all 0.25s ease !important;
        }

        div[data-testid="stMetric"]:hover {
            border-color: rgba(6, 182, 212, 0.4) !important;
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 25px rgba(6, 182, 212, 0.15) !important;
        }

        div[data-testid="stMetricLabel"] p {
            font-size: 0.78rem !important;
            font-weight: 600 !important;
            text-transform: uppercase !important;
            letter-spacing: 0.08em !important;
            color: #94a3b8 !important;
            margin-bottom: 4px !important;
        }

        div[data-testid="stMetricValue"] {
            font-size: 1.55rem !important;
            font-weight: 800 !important;
            color: #38bdf8 !important;
            font-family: 'JetBrains Mono', monospace !important;
        }

        /* Selectboxes & Multiselects - Dark */
        div[data-baseweb="select"] {
            border-radius: 10px;
        }
        
        div[data-baseweb="select"] > div {
            background-color: #1e293b !important;
            border-color: rgba(255, 255, 255, 0.1) !important;
            border-radius: 10px !important;
            color: #f1f5f9 !important;
        }

        /* Expander - Dark */
        .streamlit-expanderHeader {
            background-color: #1e293b !important;
            border-radius: 10px !important;
            border: 1px solid rgba(255, 255, 255, 0.06) !important;
            font-weight: 600 !important;
            color: #e2e8f0 !important;
        }

        .streamlit-expanderContent {
            background-color: rgba(15, 23, 42, 0.6) !important;
            border: 1px solid rgba(255, 255, 255, 0.06) !important;
            border-top: none !important;
            border-radius: 0 0 10px 10px !important;
        }

        /* Tabs styling - Dark */
        button[data-baseweb="tab"] {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-weight: 600 !important;
            font-size: 0.88rem !important;
            color: #94a3b8 !important;
        }

        button[data-baseweb="tab"][aria-selected="true"] {
            color: #38bdf8 !important;
            border-bottom-color: #38bdf8 !important;
        }

        /* Radio buttons - Dark */
        div[data-testid="stRadio"] label span {
            color: #e2e8f0 !important;
            font-weight: 500 !important;
        }

        div[data-testid="stRadio"] [data-testid="stMarkdownContainer"] p {
            color: #cbd5e1 !important;
        }

        /* Checkbox & Toggle - Dark */
        div[data-testid="stCheckbox"] label span, div[data-testid="stToggle"] label span {
            color: #e2e8f0 !important;
            font-weight: 500 !important;
        }

        /* Theme Toggle Button - Dark */
        .st-key-theme_toggle_btn button {
            background: linear-gradient(135deg, rgba(30, 41, 59, 0.85) 0%, rgba(15, 23, 42, 0.95) 100%) !important;
            border: 1px solid rgba(255, 255, 255, 0.15) !important;
            color: #f1f5f9 !important;
            border-radius: 12px !important;
            font-weight: 700 !important;
            font-size: 0.82rem !important;
            height: 44px !important;
            transition: all 0.25s ease !important;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25) !important;
        }

        .st-key-theme_toggle_btn button:hover {
            background: linear-gradient(135deg, #1e293b 0%, #334155 100%) !important;
            border-color: #38bdf8 !important;
            color: #38bdf8 !important;
            transform: translateY(-1px) !important;
            box-shadow: 0 6px 18px rgba(56, 189, 248, 0.25) !important;
        }

        /* Custom Scrollbars - Dark */
        ::-webkit-scrollbar-track {
            background: #0f172a;
        }
        ::-webkit-scrollbar-thumb {
            background: #334155;
            border-radius: 3px;
        }
        """

    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

        .block-container {{
            padding-top: 1.2rem;
            padding-bottom: 2rem;
            max-width: 96%;
        }}

        header[data-testid="stHeader"] {{
            display: none;
        }}

        /* Buttons Styling (Shared) */
        button[kind="primary"] {{
            background: linear-gradient(135deg, #0284c7 0%, #2563eb 100%) !important;
            border: none !important;
            color: #ffffff !important;
            font-weight: 600 !important;
            border-radius: 10px !important;
            padding: 0.55rem 1.2rem !important;
            transition: all 0.2s ease !important;
            box-shadow: 0 4px 15px rgba(37, 99, 235, 0.35) !important;
        }}

        button[kind="primary"]:hover {{
            background: linear-gradient(135deg, #0ea5e9 0%, #3b82f6 100%) !important;
            box-shadow: 0 6px 20px rgba(14, 165, 233, 0.5) !important;
            transform: translateY(-1px);
        }}

        /* Custom Scrollbars */
        ::-webkit-scrollbar {{
            width: 6px;
            height: 6px;
        }}

        {theme_css}
        </style>
    """, unsafe_allow_html=True)

def render_header(theme="dark"):
    """
    Renders the minimalistic national portal navbar with integrated Light/Dark mode switch.
    """
    is_light = theme == "light"
    nav_bg = "rgba(255, 255, 255, 0.9)" if is_light else "rgba(15, 23, 42, 0.7)"
    nav_border = "rgba(226, 232, 240, 0.95)" if is_light else "rgba(255, 255, 255, 0.08)"
    nav_shadow = "0 4px 20px rgba(15, 23, 42, 0.05)" if is_light else "0 4px 20px rgba(0, 0, 0, 0.3)"
    title_col = "#0f172a" if is_light else "#ffffff"
    sub_col = "#64748b" if is_light else "#94a3b8"
    sync_bg = "rgba(16, 185, 129, 0.12)" if is_light else "rgba(16, 185, 129, 0.1)"
    sync_border = "rgba(16, 185, 129, 0.35)" if is_light else "rgba(16, 185, 129, 0.25)"
    sync_text = "#059669" if is_light else "#34d399"

    c_brand, c_controls = st.columns([0.75, 0.25], gap="medium")
    
    with c_brand:
        st.markdown(f"""
            <div style="display: flex; align-items: center; gap: 14px; padding: 10px 16px; background: {nav_bg}; border: 1px solid {nav_border}; border-radius: 14px; box-shadow: {nav_shadow}; backdrop-filter: blur(12px); min-height: 64px;">
                <div style="width: 40px; height: 40px; background: linear-gradient(135deg, #38bdf8, #6366f1); border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 22px; box-shadow: 0 4px 12px rgba(56,189,248,0.3); flex-shrink: 0;">
                    🇮🇳
                </div>
                <div>
                    <div style="display: flex; align-items: center; gap: 8px; flex-wrap: wrap;">
                        <span style="font-size: 1.15rem; font-weight: 800; letter-spacing: -0.01em; color: {title_col};">BHU-AADHAAR 3D</span>
                        <span style="background: rgba(6, 182, 212, 0.15); color: {'#0284c7' if is_light else '#22d3ee'}; font-size: 0.68rem; font-weight: 700; padding: 2px 8px; border-radius: 6px; border: 1px solid rgba(6, 182, 212, 0.3);">ENTERPRISE CADASTRE</span>
                        <span style="background: rgba(168, 85, 247, 0.15); color: {'#7e22ce' if is_light else '#c084fc'}; font-size: 0.68rem; font-weight: 700; padding: 2px 8px; border-radius: 6px; border: 1px solid rgba(168, 85, 247, 0.3);">SIH 2026</span>
                    </div>
                    <div style="font-size: 0.76rem; color: {sub_col}; font-weight: 400; margin-top: 2px;">
                        National 3D Spatial Cadastre, Subsurface Clash Detection & Vertical ULPIN Engine &bull; DILRMP / NIC
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
    with c_controls:
        c_sync, c_btn = st.columns([0.48, 0.52], gap="small")
        with c_sync:
            st.markdown(f"""
                <div style="display: flex; align-items: center; justify-content: center; gap: 6px; background: {sync_bg}; border: 1px solid {sync_border}; padding: 10px 8px; border-radius: 12px; font-size: 0.72rem; color: {sync_text}; font-weight: 700; height: 44px; margin-top: 10px; box-shadow: {nav_shadow};">
                    <span style="width: 7px; height: 7px; background: #10b981; border-radius: 50%; display: inline-block; box-shadow: 0 0 8px #10b981; flex-shrink: 0;"></span>
                    <span>Sync: ACTIVE</span>
                </div>
            """, unsafe_allow_html=True)
        with c_btn:
            btn_label = "☀️ Light Mode" if theme == "dark" else "🌙 Dark Mode"
            btn_help = f"Currently active: {theme.capitalize()} Mode. Click to switch to {'Light' if theme == 'dark' else 'Dark'} Mode."
            st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
            if st.button(btn_label, key="theme_toggle_btn", help=btn_help, use_container_width=True):
                new_theme = "light" if theme == "dark" else "dark"
                st.session_state["theme"] = new_theme
                st.rerun()

def render_kpi_bar(df, theme="dark"):
    """Renders high-level summary KPIs with robust fallback."""
    total_parcels = len(df)
    subsurface_count = len(df[df['base_elevation'] < 0]) if 'base_elevation' in df.columns else 0
    cities_count = df['city'].nunique() if 'city' in df.columns else 1
    total_val = df['valuation_cr'].sum() if 'valuation_cr' in df.columns else 0

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("Total 3D Parcels", f"{total_parcels:,}")
    with c2:
        st.metric("Pan-India Metro Hubs", f"{cities_count} Metros")
    with c3:
        st.metric("Subsurface Assets", f"{subsurface_count} Nodes")
    with c4:
        st.metric("Cadastral Valuation", f"₹{total_val:,.0f} Cr")

def render_property_spec_card(prop, theme="dark"):
    """Renders a sleek property specification dossier card with robust field access and theme support."""
    is_light = theme == "light"
    base_elev = prop.get('base_elevation', 0)
    is_underground = base_elev < 0
    type_badge_color = "#f43f5e" if is_underground else ("#0284c7" if is_light else "#38bdf8")
    city = prop.get('city', 'Unknown')
    state = prop.get('state', 'India')
    name = prop.get('name', f"Parcel #{prop.get('property_id')}")
    prop_type = prop.get('type', 'Standard')
    owner = prop.get('owner', 'Government / Private')
    zone = prop.get('zone', 'Urban Commercial')
    lat = prop.get('lat', 0.0)
    lon = prop.get('lon', 0.0)
    val = prop.get('valuation_cr', 0.0)
    
    card_bg = "#ffffff" if is_light else "rgba(30, 41, 59, 0.4)"
    card_border = "#e2e8f0" if is_light else "rgba(255, 255, 255, 0.08)"
    card_shadow = "0 4px 15px rgba(15, 23, 42, 0.04)" if is_light else "none"
    title_col = "#0f172a" if is_light else "#f8fafc"
    sub_col = "#64748b" if is_light else "#94a3b8"
    grid_bg = "#f8fafc" if is_light else "rgba(15, 23, 42, 0.6)"
    grid_border = "#e2e8f0" if is_light else "rgba(255, 255, 255, 0.04)"
    label_col = "#64748b"
    val_col = "#1e293b" if is_light else "#cbd5e1"
    badge_bg = f"{type_badge_color}18" if is_light else "rgba(255,255,255,0.05)"
    gps_col = "#0284c7" if is_light else "#38bdf8"
    gps_bg = "#e0f2fe" if is_light else "rgba(0,0,0,0.2)"
    val_badge_col = "#059669" if is_light else "#34d399"
    
    st.markdown(f"""
        <div style="background: {card_bg}; border: 1px solid {card_border}; border-radius: 12px; padding: 16px; margin-bottom: 16px; box-shadow: {card_shadow};">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px;">
                <div>
                    <div style="font-size: 0.72rem; text-transform: uppercase; color: {sub_col}; font-weight: 700; letter-spacing: 0.05em;">
                        PARCEL #{prop['property_id']} &bull; {str(city).upper()}, {str(state).upper()}
                    </div>
                    <div style="font-size: 1.15rem; font-weight: 700; color: {title_col}; margin-top: 2px;">
                        {name}
                    </div>
                </div>
                <span style="background: {badge_bg}; color: {type_badge_color}; border: 1px solid {type_badge_color}44; font-size: 0.72rem; font-weight: 700; padding: 3px 10px; border-radius: 6px;">
                    {prop_type}
                </span>
            </div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; font-size: 0.8rem; background: {grid_bg}; padding: 10px; border-radius: 8px; border: 1px solid {grid_border};">
                <div><span style="color: {label_col};">Owner:</span> <b style="color: {val_col};">{owner}</b></div>
                <div><span style="color: {label_col};">Zone:</span> <b style="color: {val_col};">{zone}</b></div>
                <div><span style="color: {label_col};">GPS Coordinates:</span> <code style="color: {gps_col}; font-size: 0.75rem; background: {gps_bg}; padding: 2px 4px; border-radius: 4px;">{lat:.4f}, {lon:.4f}</code></div>
                <div><span style="color: {label_col};">Cadastral Valuation:</span> <b style="color: {val_badge_col};">₹{val:.1f} Cr</b></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Real Architectural Blueprint & Real Photographic Imagery Section
    bp = get_property_blueprint(prop.get('property_id', 101))
    with st.expander(f"📐 Real Architectural Blueprint & Site Imagery &bull; #{prop.get('property_id')}", expanded=False):
        t_bp, t_img, t_spec = st.tabs(["📐 CAD Blueprint (SVG)", "📸 Authentic Reference Imagery", "🏗️ Structural Specs"])
        with t_bp:
            st.markdown(f"<div style='font-size: 0.8rem; font-weight: 700; color: #38bdf8; margin-bottom: 6px;'>{bp.get('title', 'Architectural Blueprint')}</div>", unsafe_allow_html=True)
            st.markdown(bp.get('blueprint_svg', ''), unsafe_allow_html=True)
            dims = bp.get('dimensions', {})
            st.markdown(f"""
                <div style='display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 6px; margin-top: 8px; font-size: 0.75rem; background: rgba(15,23,42,0.6); padding: 8px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.06);'>
                    <div><span style='color: #94a3b8;'>Length:</span> <b>{dims.get('length_m', 80)}m</b></div>
                    <div><span style='color: #94a3b8;'>Width:</span> <b>{dims.get('width_m', 60)}m</b></div>
                    <div><span style='color: #94a3b8;'>Height:</span> <b>{dims.get('height_m', 100)}m</b></div>
                </div>
            """, unsafe_allow_html=True)
        with t_img:
            st.markdown(f"""
                <div style='border-radius: 8px; overflow: hidden; border: 1px solid rgba(255,255,255,0.1);'>
                    <img src='{bp.get("photo_url")}' style='width: 100%; height: 190px; object-fit: cover; display: block;' />
                    <div style='padding: 8px 10px; background: rgba(15,23,42,0.85); font-size: 0.75rem; color: #cbd5e1;'>
                        <b>{bp.get("photo_caption")}</b>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        with t_spec:
            st.markdown(f"""
                <div style='font-size: 0.78rem; line-height: 1.8; color: #cbd5e1; background: rgba(15,23,42,0.5); padding: 10px; border-radius: 8px;'>
                    <div><span style='color: #94a3b8;'>Principal Architect:</span> <b>{bp.get('architect', 'Municipal Master Architect')}</b></div>
                    <div><span style='color: #94a3b8;'>Structural Engineer:</span> <b>{bp.get('engineer', 'National Civil Engineering Board')}</b></div>
                    <div><span style='color: #94a3b8;'>Year Built:</span> <b>{bp.get('year_built', 2018)}</b></div>
                    <div><span style='color: #94a3b8;'>Structural System:</span> <b>{bp.get('structural_system', 'Reinforced Concrete Framework')}</b></div>
                    <div><span style='color: #94a3b8;'>FSI / FAR Consumed:</span> <b>{bp.get('fsi_far', '3.50')}</b></div>
                    <div><span style='color: #94a3b8;'>RERA / Sanction ID:</span> <code style='color: #38bdf8;'>{bp.get('rera_id', 'RERA-CAD-2026')}</code></div>
                </div>
            """, unsafe_allow_html=True)

def render_vertical_stack(floors, prop_data, theme="dark"):
    """
    Renders an interactive cross-section diagram of the building's
    vertical parcel stack showing above-ground and subterranean levels.
    """
    is_light = theme == "light"
    section_title_col = "#64748b" if is_light else "#94a3b8"
    
    st.markdown(f"""
        <div style="font-size: 0.8rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em; color: {section_title_col}; margin-bottom: 8px;">
            Vertical Architectural Cross-Section
        </div>
    """, unsafe_allow_html=True)

    sorted_floors = sorted(floors, key=lambda x: x['z_end'], reverse=True)
    
    html_blocks = []
    for f in sorted_floors:
        floor_num = f['floor_number']
        z_start = f['z_start']
        z_end = f['z_end']
        
        if floor_num < 0:
            if is_light:
                bg = "linear-gradient(90deg, rgba(239, 68, 68, 0.08) 0%, rgba(245, 158, 11, 0.05) 100%)"
                border_col = "rgba(239, 68, 68, 0.25)"
                badge_col = "#dc2626"
                text_col = "#0f172a"
                z_bg = "#f1f5f9"
                z_text = "#475569"
            else:
                bg = "linear-gradient(90deg, rgba(239, 68, 68, 0.15) 0%, rgba(245, 158, 11, 0.1) 100%)"
                border_col = "rgba(239, 68, 68, 0.3)"
                badge_col = "#f87171"
                text_col = "#f1f5f9"
                z_bg = "rgba(0,0,0,0.3)"
                z_text = "#94a3b8"
            default_title = f"Basement {abs(floor_num):02d} (Subsurface)"
            z_badge = f"{z_end}m to {z_start}m"
        else:
            if is_light:
                bg = "linear-gradient(90deg, rgba(2, 132, 199, 0.08) 0%, rgba(59, 130, 246, 0.05) 100%)"
                border_col = "rgba(2, 132, 199, 0.25)"
                badge_col = "#0284c7"
                text_col = "#0f172a"
                z_bg = "#f1f5f9"
                z_text = "#475569"
            else:
                bg = "linear-gradient(90deg, rgba(6, 182, 212, 0.12) 0%, rgba(59, 130, 246, 0.08) 100%)"
                border_col = "rgba(6, 182, 212, 0.25)"
                badge_col = "#38bdf8"
                text_col = "#f1f5f9"
                z_bg = "rgba(0,0,0,0.3)"
                z_text = "#94a3b8"
            default_title = f"Level {floor_num:02d} (Superstructure)"
            z_badge = f"+{z_start}m to +{z_end}m"

        lvl_code = f.get('level_code', f"#{abs(floor_num):02d}")
        flr_title = f.get('floor_name', default_title)
        use_cat = f.get('use_category', '')
            
        block = f"""
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 6px 12px; background: {bg}; border: 1px solid {border_col}; border-radius: 6px; margin-bottom: 4px; font-size: 0.78rem;">
                <div style="display: flex; align-items: center; gap: 8px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; max-width: 68%;">
                    <span style="font-weight: 700; color: {badge_col}; font-family: 'JetBrains Mono', monospace; flex-shrink: 0;">{lvl_code}</span>
                    <span style="color: {text_col}; font-weight: 600; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;" title="{flr_title}">{flr_title}</span>
                </div>
                <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: {z_text}; background: {z_bg}; padding: 2px 6px; border-radius: 4px; flex-shrink: 0;">
                    {z_badge}
                </div>
            </div>
        """
        html_blocks.append(block)

    stack_container = f"""
        <div style="max-height: 220px; overflow-y: auto; padding-right: 4px; margin-bottom: 14px;">
            {''.join(html_blocks)}
        </div>
    """
    st.markdown(stack_container, unsafe_allow_html=True)

def render_clash_report_ui(conflicts, theme="dark"):
    """
    Renders the 3D collision & spatial encroachment detection findings with theme support.
    """
    is_light = theme == "light"
    if not conflicts:
        bg = "rgba(16, 185, 129, 0.08)" if is_light else "rgba(16, 185, 129, 0.12)"
        border = "rgba(16, 185, 129, 0.25)" if is_light else "rgba(16, 185, 129, 0.3)"
        title_col = "#059669" if is_light else "#34d399"
        sub_col = "#475569" if is_light else "#94a3b8"
        st.markdown(f"""
            <div style="display: flex; align-items: center; gap: 10px; background: {bg}; border: 1px solid {border}; padding: 12px 16px; border-radius: 10px; margin-bottom: 12px;">
                <span style="font-size: 1.2rem;">✅</span>
                <div>
                    <div style="font-weight: 700; color: {title_col}; font-size: 0.88rem;">No 3D Encroachments Detected</div>
                    <div style="font-size: 0.76rem; color: {sub_col};">All subsurface foundations and utility safety buffers comply with municipal spatial regulations.</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        return

    warning_header_col = "#dc2626" if is_light else "#f87171"
    st.markdown(f"""
        <div style="margin-bottom: 10px; font-size: 0.82rem; font-weight: 700; color: {warning_header_col}; text-transform: uppercase; letter-spacing: 0.05em;">
            ⚠️ Identified {len(conflicts)} Spatial Conflicts / Buffer Violations
        </div>
    """, unsafe_allow_html=True)

    for c in conflicts:
        is_crit = c['severity'] == "CRITICAL_COLLISION"
        if is_light:
            bg_col = "rgba(239, 68, 68, 0.08)" if is_crit else "rgba(245, 158, 11, 0.08)"
            border_col = "rgba(239, 68, 68, 0.25)" if is_crit else "rgba(245, 158, 11, 0.25)"
            badge_text_col = "#dc2626" if is_crit else "#d97706"
            dist_col = "#475569"
            asset_col = "#0f172a"
            desc_col = "#64748b"
        else:
            bg_col = "rgba(239, 68, 68, 0.12)" if is_crit else "rgba(245, 158, 11, 0.12)"
            border_col = "rgba(239, 68, 68, 0.35)" if is_crit else "rgba(245, 158, 11, 0.35)"
            badge_text_col = "#f87171" if is_crit else "#fbbf24"
            dist_col = "#cbd5e1"
            asset_col = "#f1f5f9"
            desc_col = "#94a3b8"

        st.markdown(f"""
            <div style="background: {bg_col}; border: 1px solid {border_col}; border-radius: 10px; padding: 12px; margin-bottom: 8px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                    <span style="font-size: 0.8rem; font-weight: 800; color: {badge_text_col};">{c['badge']}</span>
                    <span style="font-size: 0.72rem; color: {dist_col}; font-family: monospace;">Dist: {c['distance_m']}m &bull; Z-Overlap: {c['overlap_z_m']}m</span>
                </div>
                <div style="font-size: 0.82rem; color: {asset_col}; margin-bottom: 4px;">
                    Conflicting Asset: <b>{c['conflicting_name']}</b> (#{c['conflicting_id']}) - <i>{c['conflicting_type']}</i>
                </div>
                <div style="font-size: 0.76rem; color: {desc_col};">
                    {c['description']}
                </div>
            </div>
        """, unsafe_allow_html=True)

def render_bhu_aadhaar_card_preview(prop, floor_dict, ulpin_str, theme="dark"):
    """
    Renders a live digital certificate card preview with scannable QR code and theme support.
    """
    is_light = theme == "light"
    z_range = f"{floor_dict['z_start']}m to {floor_dict['z_end']}m"
    effective_owner = floor_dict.get('owner') or prop.get('owner', 'Government Cadastral Registry')
    sha_hash = generate_title_hash(
        ulpin_str,
        effective_owner,
        prop['lat'],
        prop['lon'],
        z_range,
        prop.get('valuation_cr', 0)
    )

    qr_payload = {
        "ulpin": ulpin_str,
        "owner": effective_owner,
        "plot": int(prop['property_id']),
        "level": floor_dict['floor_number'],
        "z_range": z_range,
        "sha": sha_hash[:16]
    }
    qr_bytes = generate_qr_code_image(qr_payload)

    if is_light:
        card_bg = "linear-gradient(135deg, #ffffff 0%, #f0f9ff 100%)"
        card_border = "rgba(2, 132, 199, 0.35)"
        card_shadow = "0 6px 20px rgba(2, 132, 199, 0.1)"
        border_div = "rgba(226, 232, 240, 0.9)"
        title_header_col = "#0284c7"
        status_bg = "rgba(16, 185, 129, 0.12)"
        status_text = "#059669"
        ulpin_col = "#0f172a"
        text_col = "#334155"
        label_col = "#64748b"
        hash_bg = "#f1f5f9"
        hash_text = "#475569"
    else:
        card_bg = "linear-gradient(135deg, rgba(15, 23, 42, 0.85) 0%, rgba(30, 41, 59, 0.7) 100%)"
        card_border = "rgba(6, 182, 212, 0.4)"
        card_shadow = "0 4px 20px rgba(6, 182, 212, 0.15)"
        border_div = "rgba(255, 255, 255, 0.08)"
        title_header_col = "#38bdf8"
        status_bg = "rgba(16, 185, 129, 0.15)"
        status_text = "#34d399"
        ulpin_col = "#ffffff"
        text_col = "#cbd5e1"
        label_col = "#64748b"
        hash_bg = "rgba(0,0,0,0.3)"
        hash_text = "#94a3b8"

    c_card, c_qr = st.columns([3.2, 1.3], gap="medium")
    with c_card:
        st.markdown(f"""
            <div style="background: {card_bg}; border: 1px solid {card_border}; border-radius: 12px; padding: 14px; box-shadow: {card_shadow};">
                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid {border_div}; padding-bottom: 8px; margin-bottom: 10px;">
                    <div style="font-size: 0.72rem; text-transform: uppercase; color: {title_header_col}; font-weight: 800; letter-spacing: 0.06em;">
                        BHU-AADHAAR SPATIAL TITLE CERTIFICATE
                    </div>
                    <span style="font-size: 0.68rem; background: {status_bg}; color: {status_text}; padding: 2px 8px; border-radius: 4px; font-weight: 700;">
                        DIGITALLY VERIFIED
                    </span>
                </div>
                <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.05rem; font-weight: 800; color: {ulpin_col}; margin-bottom: 8px;">
                    {ulpin_str}
                </div>
                <div style="font-size: 0.78rem; color: {text_col}; display: grid; grid-template-columns: 1fr 1fr; gap: 6px; margin-bottom: 8px;">
                    <div><span style="color: {label_col};">Title Holder:</span> <b>{effective_owner}</b></div>
                    <div><span style="color: {label_col};">Vertical Span:</span> <b>{z_range}</b></div>
                    <div style="grid-column: span 2;"><span style="color: {label_col};">Unit Designation:</span> <b style="color: {title_header_col};">{floor_dict.get('floor_name', f"Level {floor_dict.get('floor_number')}")}</b></div>
                    <div><span style="color: {label_col};">Complex:</span> <b>{prop['name']}</b></div>
                    <div><span style="color: {label_col};">Jurisdiction:</span> <b>{prop['city']}, {prop['state']}</b></div>
                </div>
                <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.65rem; color: {hash_text}; background: {hash_bg}; padding: 4px 8px; border-radius: 4px; overflow-x: hidden; text-overflow: ellipsis; white-space: nowrap;">
                    SHA-256: {sha_hash}
                </div>
            </div>
        """, unsafe_allow_html=True)
    with c_qr:
        st.image(qr_bytes, caption="Scan to Verify 3D Title", width=140)
