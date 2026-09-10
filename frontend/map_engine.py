import pydeck as pdk
import pandas as pd

# Curated High-Tech Neon Palette for 3D Cadastral Visualization
COLOR_PALETTE = {
    'Commercial': [0, 212, 255, 230],          # Neon Cyan
    'Apartment': [168, 85, 247, 230],          # Electric Violet
    'Underground Parking': [251, 146, 60, 240],# Glowing Amber
    'Transit': [16, 185, 129, 230],            # Cyber Emerald
    'Subsurface Utility': [244, 63, 94, 240],  # Rose / Magma Red
}

import json
import base64

# Satellite & Hybrid raster styles for MapLibre / Deck.gl
_ESRI_SATELLITE_SPEC = {
    "version": 8,
    "sources": {
        "satellite": {
            "type": "raster",
            "tiles": ["https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}"],
            "tileSize": 256,
            "maxzoom": 19
        }
    },
    "layers": [
        {"id": "satellite-layer", "type": "raster", "source": "satellite", "minzoom": 0, "maxzoom": 22}
    ]
}

_HYBRID_SATELLITE_SPEC = {
    "version": 8,
    "sources": {
        "satellite": {
            "type": "raster",
            "tiles": ["https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}"],
            "tileSize": 256,
            "maxzoom": 19
        },
        "labels": {
            "type": "raster",
            "tiles": ["https://basemaps.cartocdn.com/rastertiles/voyager_only_labels/{z}/{x}/{y}.png"],
            "tileSize": 256,
            "maxzoom": 19
        }
    },
    "layers": [
        {"id": "satellite-layer", "type": "raster", "source": "satellite", "minzoom": 0, "maxzoom": 22},
        {"id": "labels-layer", "type": "raster", "source": "labels", "minzoom": 0, "maxzoom": 22}
    ]
}

_SATELLITE_URI = "data:application/json;base64," + base64.b64encode(json.dumps(_ESRI_SATELLITE_SPEC).encode()).decode()
_HYBRID_URI = "data:application/json;base64," + base64.b64encode(json.dumps(_HYBRID_SATELLITE_SPEC).encode()).decode()

MAP_STYLES = {
    "🗺️ Google Maps Style (Streets & POIs)": "https://basemaps.cartocdn.com/gl/voyager-gl-style/style.json",
    "🛰️ Google Maps Hybrid (Satellite + Labels)": _HYBRID_URI,
    "🛰️ Pure Satellite (High-Res)": _SATELLITE_URI,
    "🌌 Dark Matter (Default)": "https://basemaps.cartocdn.com/gl/dark-matter-gl-style/style.json",
    "☀️ Minimalist Light": "https://basemaps.cartocdn.com/gl/positron-gl-style/style.json",
    # Backward compatibility
    "🛰️ Satellite View (High-Res)": _SATELLITE_URI,
    "🛰️ Hybrid Satellite (Labels & Roads)": _HYBRID_URI,
    "🧭 Voyager Detailed": "https://basemaps.cartocdn.com/gl/voyager-gl-style/style.json"
}

# Authentic Google Maps Location Names & Badges for Cadastral Parcels
GMAPS_PARCEL_NAMES = {
    101: "🚉 Seawoods Grand Central Station & Mall",
    102: "🅿️ Seawoods Concourse Subsurface Vault",
    103: "🏢 Palm Beach Residency, Sector 54",
    104: "🚊 Seawoods Urban Railway Terminal",
    105: "💎 Bharat Diamond Bourse, BKC",
    106: "🚇 BKC Underground Metro Station (Line 3)",
    107: "🏙️ Lodha World One, Worli Sea Face",
    201: "🏛️ Connaught Place (Outer Circle), CP",
    202: "🚇 Rajiv Chowk Metro Interchange (Yellow & Blue Line)",
    203: "✈️ Aerocity Gateway, IGI Airport",
    204: "🏢 DLF Cyber City Building 10 (The Epitome)",
    301: "💻 Manyata Embassy Business Park, Hebbal",
    302: "🚇 Cubbon Park Metro Station, Central",
    303: "🛍️ UB City & Kingfisher Towers",
    304: "🏢 Prestige Tech Park, Whitefield",
    401: "💎 GIFT Diamond Tower, Gandhinagar",
    402: "⚡ GIFT Subsurface Utility Tunnel (TUM)",
    403: "🏢 GIFT Aspire Smart Residences",
    501: "🌐 HITEC Cyber Towers, Madhapur",
    502: "🛡️ Cyberabad Subsurface Data Vault",
    503: "🌉 Durgam Cheruvu Cable Bridge Hub",
    601: "💻 TIDEL Park, OMR IT Expressway",
    602: "🚇 Puratchi Thalaivar Dr. MGR Central Metro",
    701: "🌿 New Town EcoSpace Business Park",
    702: "🌊 Hooghly Underwater Metro Corridor, Howrah"
}

# Authentic Google Maps Real-World Surrounding Points of Interest (POIs)
GMAPS_SURROUNDING_POIS = [
    # Gurugram Cyber City Corridor
    {"name": "Cyber Hub Dining & Social", "category": "Dining & Retail", "icon": "🍽️", "lat": 28.4945, "lon": 77.0886, "city": "Gurugram", "color": [245, 158, 11, 230]},
    {"name": "IndusInd Bank Cyber City Metro", "category": "Rapid Metro", "icon": "🚇", "lat": 28.4975, "lon": 77.0910, "city": "Gurugram", "color": [2, 132, 199, 230]},
    {"name": "DLF Gateway Tower (The Ship)", "category": "Corporate Landmark", "icon": "🏢", "lat": 28.4990, "lon": 77.0925, "city": "Gurugram", "color": [14, 165, 233, 230]},
    {"name": "Belvedere Towers Rapid Metro", "category": "Rapid Metro", "icon": "🚇", "lat": 28.4910, "lon": 77.0860, "city": "Gurugram", "color": [2, 132, 199, 230]},
    {"name": "Ambience Mall NH-48", "category": "Shopping Mall", "icon": "🛍️", "lat": 28.5040, "lon": 77.0965, "city": "Gurugram", "color": [236, 72, 153, 230]},

    # Mumbai Worli & BKC Corridor
    {"name": "Worli Sea Face Promenade", "category": "Public Promenade", "icon": "🌊", "lat": 19.0135, "lon": 72.8150, "city": "Mumbai", "color": [56, 189, 248, 230]},
    {"name": "Bandra-Worli Sea Link Bridge", "category": "Expressway Bridge", "icon": "🌉", "lat": 19.0250, "lon": 72.8180, "city": "Mumbai", "color": [14, 165, 233, 230]},
    {"name": "Jio World Centre & Convention Centre", "category": "Convention Hub", "icon": "🏛️", "lat": 19.0635, "lon": 72.8670, "city": "Mumbai", "color": [168, 85, 247, 230]},
    {"name": "US Consulate General Mumbai", "category": "Diplomatic", "icon": "🏛️", "lat": 19.0685, "lon": 72.8660, "city": "Mumbai", "color": [100, 116, 139, 230]},
    {"name": "BKC City Park", "category": "Botanical Park", "icon": "🌿", "lat": 19.0680, "lon": 72.8710, "city": "Mumbai", "color": [34, 197, 94, 230]},

    # Navi Mumbai Seawoods & Belapur
    {"name": "Nexus Grand Central Mall", "category": "Shopping Mall", "icon": "🛍️", "lat": 19.0210, "lon": 73.0175, "city": "Navi Mumbai", "color": [236, 72, 153, 230]},
    {"name": "Jewel of Navi Mumbai Lake", "category": "Public Waterfront", "icon": "🏞️", "lat": 19.0290, "lon": 73.0150, "city": "Navi Mumbai", "color": [56, 189, 248, 230]},
    {"name": "Nerul Balaji Temple", "category": "Heritage Landmark", "icon": "🛕", "lat": 19.0350, "lon": 73.0210, "city": "Navi Mumbai", "color": [245, 158, 11, 230]},
    {"name": "Seawoods Darave Railway Station", "category": "Suburban Rail", "icon": "🚉", "lat": 19.0185, "lon": 73.0185, "city": "Navi Mumbai", "color": [2, 132, 199, 230]},

    # New Delhi Connaught Place & CBD
    {"name": "Central Park (Connaught Place)", "category": "Public Plaza", "icon": "🌿", "lat": 28.6328, "lon": 77.2197, "city": "New Delhi", "color": [34, 197, 94, 230]},
    {"name": "Palika Bazaar Underground Market", "category": "Underground Market", "icon": "🛍️", "lat": 28.6315, "lon": 77.2185, "city": "New Delhi", "color": [245, 158, 11, 230]},
    {"name": "Barakhamba Road Metro Station", "category": "Blue Line Metro", "icon": "🚇", "lat": 28.6300, "lon": 77.2270, "city": "New Delhi", "color": [2, 132, 199, 230]},
    {"name": "Shivaji Stadium Airport Express", "category": "Airport Express", "icon": "🚄", "lat": 28.6285, "lon": 77.2130, "city": "New Delhi", "color": [249, 115, 22, 230]},
    {"name": "Janpath Tibetan Market", "category": "Shopping Street", "icon": "🛍️", "lat": 28.6265, "lon": 77.2190, "city": "New Delhi", "color": [236, 72, 153, 230]},

    # Bengaluru CBD & Whitefield
    {"name": "Cubbon Park Botanical Reserve", "category": "Botanical Park", "icon": "🌳", "lat": 12.9760, "lon": 77.5925, "city": "Bengaluru", "color": [34, 197, 94, 230]},
    {"name": "Vidhana Soudha Capitol Complex", "category": "State Secretariat", "icon": "🏛️", "lat": 12.9795, "lon": 77.5910, "city": "Bengaluru", "color": [168, 85, 247, 230]},
    {"name": "M. Chinnaswamy Cricket Stadium", "category": "Sports Arena", "icon": "🏏", "lat": 12.9785, "lon": 77.5995, "city": "Bengaluru", "color": [239, 68, 68, 230]},
    {"name": "MG Road Boulevard & Metro", "category": "Metro Station", "icon": "🚇", "lat": 12.9750, "lon": 77.6080, "city": "Bengaluru", "color": [2, 132, 199, 230]},
    {"name": "ITPL Main Gate, Whitefield", "category": "Tech Park Hub", "icon": "💻", "lat": 12.9870, "lon": 77.7340, "city": "Bengaluru", "color": [14, 165, 233, 230]},

    # Hyderabad HITEC City & Madhapur
    {"name": "Inorbit Mall Cyberabad", "category": "Shopping Mall", "icon": "🛍️", "lat": 17.4355, "lon": 78.3850, "city": "Hyderabad", "color": [236, 72, 153, 230]},
    {"name": "IKEA Hyderabad Store", "category": "Retail Hub", "icon": "🏬", "lat": 17.4410, "lon": 78.3760, "city": "Hyderabad", "color": [245, 158, 11, 230]},
    {"name": "Raidurg Metro Terminal", "category": "Blue Line Metro", "icon": "🚇", "lat": 17.4400, "lon": 78.3780, "city": "Hyderabad", "color": [2, 132, 199, 230]},
    {"name": "Mindspace IT Park Campus", "category": "Technology SEZ", "icon": "💻", "lat": 17.4430, "lon": 78.3820, "city": "Hyderabad", "color": [14, 165, 233, 230]},

    # GIFT City Gandhinagar
    {"name": "IFSCA Headquarters Building", "category": "Financial Authority", "icon": "🏛️", "lat": 23.1630, "lon": 72.6830, "city": "GIFT City", "color": [168, 85, 247, 230]},
    {"name": "GIFT City Club & Grand O7", "category": "Hospitality & Club", "icon": "🏨", "lat": 23.1580, "lon": 72.6860, "city": "GIFT City", "color": [245, 158, 11, 230]},
    {"name": "Sabarmati Riverfront Promenade", "category": "Waterfront Walkway", "icon": "🌊", "lat": 23.1670, "lon": 72.6780, "city": "GIFT City", "color": [56, 189, 248, 230]},

    # Kolkata Central & Rajarhat
    {"name": "Howrah Railway Station Terminal", "category": "Major Rail Terminal", "icon": "🚉", "lat": 22.5835, "lon": 88.3425, "city": "Kolkata", "color": [2, 132, 199, 230]},
    {"name": "Howrah Bridge (Rabindra Setu)", "category": "Iconic Cantilever Bridge", "icon": "🌉", "lat": 22.5850, "lon": 88.3470, "city": "Kolkata", "color": [14, 165, 233, 230]},
    {"name": "Mahakaran Metro Station", "category": "East-West Metro", "icon": "🚇", "lat": 22.5720, "lon": 88.3510, "city": "Kolkata", "color": [2, 132, 199, 230]},
    {"name": "Biswa Bangla Gate, New Town", "category": "Iconic Ring Monument", "icon": "⭕", "lat": 22.5875, "lon": 88.4695, "city": "Kolkata", "color": [249, 115, 22, 230]},

    # Chennai OMR & Central
    {"name": "TIDEL Park MRTS Railway Station", "category": "Transit Station", "icon": "🚉", "lat": 12.9880, "lon": 80.2470, "city": "Chennai", "color": [2, 132, 199, 230]},
    {"name": "Thiruvanmiyur Beach Promenade", "category": "Beach & Promenade", "icon": "🏖️", "lat": 12.9820, "lon": 80.2600, "city": "Chennai", "color": [56, 189, 248, 230]},
    {"name": "Puratchi Thalaivar Dr. MGR Central Station", "category": "Heritage Railway Terminal", "icon": "🏛️", "lat": 13.0825, "lon": 80.2750, "city": "Chennai", "color": [2, 132, 199, 230]},
    {"name": "Ripon Building (Greater Chennai Corp)", "category": "Municipal Headquarters", "icon": "🏛️", "lat": 13.0835, "lon": 80.2740, "city": "Chennai", "color": [168, 85, 247, 230]}
]

CITY_VIEWPORTS = {
    "🇮🇳 Pan-India (National Cadastre)": {"lat": 22.5000, "lon": 79.5000, "zoom": 4.3, "pitch": 35, "bearing": 0, "radius": 22000, "scale": 1800},
    "🇮🇳 Pan-India (Subcontinent)": {"lat": 22.5000, "lon": 79.5000, "zoom": 4.3, "pitch": 35, "bearing": 0, "radius": 22000, "scale": 1800},
    "Gurugram (NCR - Cyber City & Golf Course Corridor)": {"lat": 28.4952, "lon": 77.0895, "zoom": 15.2, "pitch": 62, "bearing": 30, "radius": 75, "scale": 1},
    "Navi Mumbai (MMR - Belapur & Seawoods TOD)": {"lat": 19.0216, "lon": 73.0181, "zoom": 15.3, "pitch": 62, "bearing": 32, "radius": 70, "scale": 1},
    "Mumbai (MMR - Worli Sea Face & BKC Financial Centre)": {"lat": 19.0400, "lon": 72.8400, "zoom": 13.0, "pitch": 60, "bearing": 25, "radius": 130, "scale": 1},
    "New Delhi (NCT - Lutyens & Central Business District)": {"lat": 28.6328, "lon": 77.2197, "zoom": 14.5, "pitch": 58, "bearing": 20, "radius": 110, "scale": 1},
    "Bengaluru Urban (BBMP - IT Corridor, Whitefield & CBD)": {"lat": 12.9780, "lon": 77.6100, "zoom": 13.0, "pitch": 60, "bearing": 30, "radius": 140, "scale": 1},
    "GIFT City (Gandhinagar / Ahmedabad IFSC)": {"lat": 23.1610, "lon": 72.6840, "zoom": 15.6, "pitch": 64, "bearing": 40, "radius": 65, "scale": 1},
    "Hyderabad (GHMC - Cyberabad & HITEC City)": {"lat": 17.4480, "lon": 78.3800, "zoom": 14.2, "pitch": 60, "bearing": 30, "radius": 110, "scale": 1},
    "Chennai (GCC - OMR IT Expressway & Central)": {"lat": 13.0200, "lon": 80.2600, "zoom": 13.2, "pitch": 58, "bearing": 20, "radius": 130, "scale": 1},
    "Kolkata (KMC - New Town IT Hub & Underwater Metro)": {"lat": 22.5830, "lon": 88.4000, "zoom": 13.2, "pitch": 58, "bearing": 20, "radius": 130, "scale": 1},
}

def render_3d_map(df, selected_region="🇮🇳 Pan-India (National Cadastre)", custom_center=None, map_theme="Dark Matter (Default)", show_labels=True):
    """
    Renders an interactive, futuristic 3D Cadastral Deck.gl map.
    Supports pan-India continent scale down to micro-parcel vertical footprints.
    Integrates Google Maps style landmark names, POIs, and high-contrast labels.
    """
    if df.empty:
        # Fallback empty view centered on India
        view_state = pdk.ViewState(latitude=22.5, longitude=79.5, zoom=4.3, pitch=30)
        return pdk.Deck(layers=[], initial_view_state=view_state)

    map_df = df.copy()

    # Determine colors
    map_df['color'] = map_df['type'].apply(lambda x: COLOR_PALETTE.get(x, [148, 163, 184, 220]))
    
    # Authentic Google Maps landmark name mapping
    map_df['gmaps_name'] = map_df['property_id'].apply(
        lambda pid: GMAPS_PARCEL_NAMES.get(int(pid), map_df.loc[map_df['property_id'] == pid, 'name'].values[0] if not map_df.loc[map_df['property_id'] == pid, 'name'].empty else "Cadastral Landmark")
    )

    # Tooltip label formatting
    map_df['elevation_label'] = map_df.apply(
        lambda r: f"Subsurface: {r['base_elevation']}m to {r['base_elevation'] + r['total_height']}m" 
        if r['base_elevation'] < 0 
        else f"Surface to +{r['total_height']}m",
        axis=1
    )
    map_df['archetype_display'] = map_df['archetype'].apply(
        lambda a: str(a).replace('_', ' ').title() if pd.notna(a) and str(a) != 'None' else 'Parametric Modern'
    ) if 'archetype' in map_df.columns else 'Parametric Modern'

    # Determine camera view state & scale
    pan_india_default = CITY_VIEWPORTS.get("🇮🇳 Pan-India (National Cadastre)") or CITY_VIEWPORTS.get("🇮🇳 Pan-India (Subcontinent)") or list(CITY_VIEWPORTS.values())[0]
    preset = CITY_VIEWPORTS.get(selected_region, pan_india_default)
    
    if custom_center:
        # Focusing on a specific selected property
        view_lat = custom_center['lat']
        view_lon = custom_center['lon']
        zoom = 16.2
        pitch = 65
        bearing = 35
        radius = 55
        elevation_scale = 1
    elif selected_region.startswith("🇮🇳") or "Pan-India" in selected_region:
        view_lat = preset["lat"]
        view_lon = preset["lon"]
        zoom = preset["zoom"]
        pitch = preset["pitch"]
        bearing = preset["bearing"]
        radius = preset["radius"]
        elevation_scale = preset["scale"]
    else:
        # Specific city selected
        view_lat = preset["lat"]
        view_lon = preset["lon"]
        zoom = preset["zoom"]
        pitch = preset["pitch"]
        bearing = preset["bearing"]
        radius = preset["radius"]
        elevation_scale = 1

    view_state = pdk.ViewState(
        latitude=view_lat,
        longitude=view_lon,
        zoom=zoom,
        pitch=pitch,
        bearing=bearing
    )

    layers = []

    # 1. Main 3D Cadastral Extrusion Layer
    column_layer = pdk.Layer(
        'ColumnLayer',
        data=map_df,
        get_position='[lon, lat]',
        get_elevation='total_height',
        elevation_scale=elevation_scale,
        radius=radius,
        get_fill_color='color',
        pickable=True,
        extruded=True,
        auto_highlight=True,
    )
    layers.append(column_layer)

    # 2. Add halo / ground footprint ring for subsurface & iconic parcels
    scatter_layer = pdk.Layer(
        'ScatterplotLayer',
        data=map_df,
        get_position='[lon, lat]',
        get_radius=radius * 1.35,
        get_fill_color=[255, 255, 255, 40],
        get_line_color='color',
        line_width_min_pixels=2,
        stroked=True,
        filled=True,
        pickable=False
    )
    layers.append(scatter_layer)

    # 3. Google Maps Style Text Labels for Cadastral Parcels
    is_daylight = "Light" in map_theme or "Google Maps Style" in map_theme or "Voyager" in map_theme
    text_color = [15, 23, 42, 255] if is_daylight else [255, 255, 255, 255]
    text_bg = [255, 255, 255, 235] if is_daylight else [15, 23, 42, 220]
    border_col = [2, 132, 199, 255]

    if show_labels:
        parcel_text_layer = pdk.Layer(
            'TextLayer',
            id='gmaps-parcel-labels',
            data=map_df,
            get_position=['lon', 'lat'],
            get_text='gmaps_name',
            get_color=text_color,
            get_size=12,
            get_alignment_baseline='bottom',
            get_text_anchor='middle',
            get_pixel_offset=[0, -22],
            background=True,
            get_background_color=text_bg,
            get_border_color=border_col,
            get_border_width=1.5,
            font_family="'Inter', 'Segoe UI', Roboto, sans-serif",
            font_weight=700,
            pickable=True
        )
        layers.append(parcel_text_layer)

        # 4. Surrounding Real-World Google Maps Points of Interest (POIs)
        if selected_region.startswith("🇮🇳") or "Pan-India" in selected_region:
            matched_pois = [p for i, p in enumerate(GMAPS_SURROUNDING_POIS) if i % 3 == 0]
        else:
            city_toks = ["Gurugram", "Navi Mumbai", "Mumbai", "New Delhi", "Bengaluru", "GIFT City", "Hyderabad", "Chennai", "Kolkata"]
            matched_tok = next((tok for tok in city_toks if tok.lower() in selected_region.lower()), selected_region)
            matched_pois = [p for p in GMAPS_SURROUNDING_POIS if p['city'].lower() in matched_tok.lower() or matched_tok.lower() in p['city'].lower()]
            if not matched_pois:
                matched_pois = GMAPS_SURROUNDING_POIS[:6]

        if matched_pois:
            poi_df = pd.DataFrame(matched_pois)
            poi_df['display_label'] = poi_df['icon'] + " " + poi_df['name']

            poi_pin_layer = pdk.Layer(
                'ScatterplotLayer',
                id='gmaps-poi-pins',
                data=poi_df,
                get_position=['lon', 'lat'],
                get_radius=22,
                get_fill_color='color',
                get_line_color=[255, 255, 255, 240],
                line_width_min_pixels=1.5,
                stroked=True,
                filled=True,
                pickable=True
            )
            layers.append(poi_pin_layer)

            poi_text_layer = pdk.Layer(
                'TextLayer',
                id='gmaps-poi-labels',
                data=poi_df,
                get_position=['lon', 'lat'],
                get_text='display_label',
                get_color=[30, 41, 59, 255] if is_daylight else [241, 245, 249, 255],
                get_size=11,
                get_alignment_baseline='top',
                get_text_anchor='middle',
                get_pixel_offset=[0, 10],
                background=True,
                get_background_color=[241, 245, 249, 225] if is_daylight else [30, 41, 59, 210],
                get_border_color=[100, 116, 139, 180],
                get_border_width=1,
                font_family="'Inter', 'Segoe UI', Roboto, sans-serif",
                font_weight=600,
                pickable=True
            )
            layers.append(poi_text_layer)

    # Add Satellite raster tile layers if satellite mode is selected
    if "Satellite" in map_theme:
        sat_tile_layer = pdk.Layer(
            "TileLayer",
            id="esri-satellite-basemap",
            data="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
            min_zoom=0,
            max_zoom=19,
            tile_size=256
        )
        layers.insert(0, sat_tile_layer)
        if "Hybrid" in map_theme or "Labels" in map_theme:
            label_tile_layer = pdk.Layer(
                "TileLayer",
                id="carto-labels-overlay",
                data="https://basemaps.cartocdn.com/rastertiles/voyager_only_labels/{z}/{x}/{y}.png",
                min_zoom=0,
                max_zoom=19,
                tile_size=256
            )
            layers.append(label_tile_layer)

    # Informative & Minimalist Glassmorphism Tooltip
    tooltip_html = """
    <div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; min-width: 220px; padding: 4px 6px;">
        <div style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.08em; color: #38bdf8; font-weight: 700; margin-bottom: 2px;">
            📍 {gmaps_name}
        </div>
        <div style="font-size: 11px; color: #94a3b8; font-weight: 600; margin-bottom: 4px;">
            {city}, {state} &bull; Survey ID: #{property_id}
        </div>
        <div style="font-size: 11px; margin-bottom: 3px; color: #cbd5e1;">
            <span style="color: #64748b;">Type:</span> <b>{type}</b> &bull; <span style="color: #38bdf8;">{archetype_display}</span>
        </div>
        <div style="font-size: 11px; margin-bottom: 3px; color: #cbd5e1;">
            <span style="color: #64748b;">Vertical Span:</span> <b>{total_height}m</b> ({elevation_label})
        </div>
        <div style="font-size: 11px; margin-bottom: 3px; color: #cbd5e1;">
            <span style="color: #64748b;">Titleholder:</span> {owner}
        </div>
        <div style="font-size: 11px; margin-top: 5px; padding-top: 4px; border-top: 1px solid rgba(255,255,255,0.1); color: #38bdf8;">
            <b>₹{valuation_cr} Cr</b> &bull; <span style="color: #10b981;">{status}</span>
        </div>
    </div>
    """

    # Resolve map style with fuzzy fallback
    map_style_url = MAP_STYLES.get(map_theme)
    if not map_style_url:
        for k, v in MAP_STYLES.items():
            if map_theme.lower() in k.lower():
                map_style_url = v
                break
    if not map_style_url:
        map_style_url = MAP_STYLES["🌌 Dark Matter (Default)"]

    return pdk.Deck(
        layers=layers,
        initial_view_state=view_state,
        tooltip={
            "html": tooltip_html,
            "style": {
                "backgroundColor": "rgba(15, 23, 42, 0.94)",
                "backdropFilter": "blur(8px)",
                "color": "#ffffff",
                "border": "1px solid rgba(255, 255, 255, 0.12)",
                "borderRadius": "10px",
                "boxShadow": "0 12px 30px rgba(0, 0, 0, 0.5)",
                "padding": "10px 14px"
            }
        },
        map_style=map_style_url,
        height=680
    )