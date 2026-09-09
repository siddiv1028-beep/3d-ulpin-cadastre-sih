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

MAP_STYLES = {
    "Dark Matter (Default)": "https://basemaps.cartocdn.com/gl/dark-matter-gl-style/style.json",
    "Minimalist Light": "https://basemaps.cartocdn.com/gl/positron-gl-style/style.json",
    "Voyager Detailed": "https://basemaps.cartocdn.com/gl/voyager-gl-style/style.json"
}

CITY_VIEWPORTS = {
    "🇮🇳 Pan-India (Subcontinent)": {"lat": 22.5000, "lon": 79.5000, "zoom": 4.3, "pitch": 35, "bearing": 0, "radius": 22000, "scale": 1800},
    "Navi Mumbai": {"lat": 19.0216, "lon": 73.0181, "zoom": 15.3, "pitch": 62, "bearing": 32, "radius": 70, "scale": 1},
    "Mumbai MMR": {"lat": 19.0500, "lon": 72.8500, "zoom": 12.8, "pitch": 60, "bearing": 25, "radius": 140, "scale": 1},
    "New Delhi & NCR": {"lat": 28.5800, "lon": 77.1600, "zoom": 12.2, "pitch": 58, "bearing": 20, "radius": 160, "scale": 1},
    "Bengaluru": {"lat": 12.9800, "lon": 77.6300, "zoom": 12.5, "pitch": 60, "bearing": 30, "radius": 150, "scale": 1},
    "GIFT City": {"lat": 23.1610, "lon": 72.6840, "zoom": 15.6, "pitch": 64, "bearing": 40, "radius": 65, "scale": 1},
    "Hyderabad": {"lat": 17.4450, "lon": 78.3800, "zoom": 13.8, "pitch": 60, "bearing": 30, "radius": 120, "scale": 1},
    "Chennai": {"lat": 13.0400, "lon": 80.2600, "zoom": 13.0, "pitch": 58, "bearing": 20, "radius": 140, "scale": 1},
    "Kolkata": {"lat": 22.5800, "lon": 88.4100, "zoom": 13.0, "pitch": 58, "bearing": 20, "radius": 140, "scale": 1},
}

def render_3d_map(df, selected_region="🇮🇳 Pan-India (Subcontinent)", custom_center=None, map_theme="Dark Matter (Default)"):
    """
    Renders an interactive, futuristic 3D Cadastral Deck.gl map.
    Supports pan-India continent scale down to micro-parcel vertical footprints.
    """
    if df.empty:
        # Fallback empty view centered on India
        view_state = pdk.ViewState(latitude=22.5, longitude=79.5, zoom=4.3, pitch=30)
        return pdk.Deck(layers=[], initial_view_state=view_state)

    map_df = df.copy()

    # Determine colors
    map_df['color'] = map_df['type'].apply(lambda x: COLOR_PALETTE.get(x, [148, 163, 184, 220]))
    
    # Tooltip label formatting
    map_df['elevation_label'] = map_df.apply(
        lambda r: f"Subsurface: {r['base_elevation']}m to {r['base_elevation'] + r['total_height']}m" 
        if r['base_elevation'] < 0 
        else f"Surface to +{r['total_height']}m",
        axis=1
    )

    # Determine camera view state & scale
    preset = CITY_VIEWPORTS.get(selected_region, CITY_VIEWPORTS["🇮🇳 Pan-India (Subcontinent)"])
    
    if custom_center:
        # Focusing on a specific selected property
        view_lat = custom_center['lat']
        view_lon = custom_center['lon']
        zoom = 16.2
        pitch = 65
        bearing = 35
        radius = 55
        elevation_scale = 1
    elif selected_region == "🇮🇳 Pan-India (Subcontinent)":
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

    # Informative & Minimalist Glassmorphism Tooltip
    tooltip_html = """
    <div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; min-width: 200px; padding: 4px 6px;">
        <div style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.08em; color: #94a3b8; font-weight: 600; margin-bottom: 2px;">
            {city}, {state} &bull; ID: #{property_id}
        </div>
        <div style="font-size: 14px; font-weight: 700; color: #ffffff; margin-bottom: 6px;">
            {name}
        </div>
        <div style="font-size: 11px; margin-bottom: 3px; color: #cbd5e1;">
            <span style="color: #64748b;">Type:</span> <b>{type}</b>
        </div>
        <div style="font-size: 11px; margin-bottom: 3px; color: #cbd5e1;">
            <span style="color: #64748b;">Vertical Span:</span> <b>{total_height}m</b> ({elevation_label})
        </div>
        <div style="font-size: 11px; margin-bottom: 3px; color: #cbd5e1;">
            <span style="color: #64748b;">Owner:</span> {owner}
        </div>
        <div style="font-size: 11px; margin-top: 5px; padding-top: 4px; border-top: 1px solid rgba(255,255,255,0.1); color: #38bdf8;">
            <b>₹{valuation_cr} Cr</b> &bull; <span style="color: #10b981;">{status}</span>
        </div>
    </div>
    """

    map_style_url = MAP_STYLES.get(map_theme, MAP_STYLES["Dark Matter (Default)"])

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