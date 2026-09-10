import sqlite3
import os
import pandas as pd

def initialize_db():
    db_path = os.path.join(os.path.dirname(__file__), 'spatial_records.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Drop existing table if structure changed
    cursor.execute('DROP TABLE IF EXISTS property_parcels')

    # Create the enhanced 3D property table with Pan-India cadastral fields & architectural metadata
    cursor.execute('''
    CREATE TABLE property_parcels (
        property_id INTEGER PRIMARY KEY,
        name TEXT,
        city TEXT,
        state TEXT,
        state_code INTEGER,
        dist_code INTEGER,
        sub_dist_code INTEGER,
        village_code INTEGER,
        type TEXT,
        lat REAL,
        lon REAL,
        base_elevation REAL,
        total_height REAL,
        owner TEXT,
        status TEXT,
        valuation_cr REAL,
        zone TEXT,
        archetype TEXT,
        facade_theme TEXT,
        roof_feature TEXT,
        subsurface_infra TEXT
    )
    ''')

    # Comprehensive Pan-India Cadastral Dataset with Realistic Architectural Digital Twin Metadata
    sample_data = [
        # --- Navi Mumbai & Mumbai MMR (Maharashtra: State Code 27) ---
        (101, 'Seawoods Grand Central TOD', 'Navi Mumbai', 'Maharashtra', 27, 21, 101, 50, 'Commercial', 19.0216, 73.0181, 0, 120, 'L&T Realty & Seawoods Corp', 'Verified 3D Cadastre', 850.0, 'Navi Mumbai (MMR / CIDCO Seawoods TOD)', 'transit_quad_podium', 'azure_glass', 'helipad_skywalk', 'metro_rail_transit'),
        (102, 'Grand Central Subsurface Concourse', 'Navi Mumbai', 'Maharashtra', 27, 21, 101, 50, 'Underground Parking', 19.0216, 73.0181, -15, 15, 'CIDCO Urban Infrastructure Authority', 'Subsurface Title Active', 180.0, 'Navi Mumbai (MMR / CIDCO Urban Infra)', 'subterranean_multilevel_cavern', 'concrete_vault', 'street_plaza', 'multi_tier_parking'),
        (103, 'Palm Beach Residency Pinnacle', 'Navi Mumbai', 'Maharashtra', 27, 21, 101, 52, 'Apartment', 19.0245, 73.0115, 0, 85, 'Palm Beach Residents Welfare Association', 'Verified 3D Cadastre', 320.0, 'Navi Mumbai (MMR / Palm Beach Corridor)', 'coastal_residential_tower', 'emerald_terrace', 'sky_garden', 'basement_parking'),
        (104, 'Seawoods Urban Transit Terminal', 'Navi Mumbai', 'Maharashtra', 27, 21, 101, 51, 'Transit', 19.0180, 73.0190, 0, 35, 'Central Railway / CIDCO', 'Public Utility Asset', 420.0, 'Navi Mumbai (MMR / Central Railway Node)', 'transit_canopy_terminal', 'aerodynamic_mesh', 'tensile_canopy', 'underground_pedestrian_concourse'),
        (105, 'BKC Diamond Tower', 'Mumbai', 'Maharashtra', 27, 22, 104, 12, 'Commercial', 19.0657, 72.8688, 0, 160, 'MMRDA & Bharat Diamond Bourse', 'Verified 3D Cadastre', 2400.0, 'Mumbai (MMR / MMRDA BKC Financial Dist)', 'crystalline_diamond', 'diamond_crystal_blue', 'observation_crown', 'bkc_metro3_vault'),
        (106, 'BKC Metro-3 Underground Vault', 'Mumbai', 'Maharashtra', 27, 22, 104, 12, 'Subsurface Utility', 19.0665, 72.8695, -24, 24, 'MMRCL Underground Metro Corridor', 'Critical Infrastructure', 680.0, 'Mumbai (MMR / MMRCL Metro-3 Colaba-SEEPZ)', 'subterranean_multilevel_cavern', 'subterranean_granite', 'surface_roadway', 'metro3_double_bore'),
        (107, 'Lodha World One (Worli Sea Face)', 'Mumbai', 'Maharashtra', 27, 22, 108, 5, 'Apartment', 19.0178, 72.8172, 0, 240, 'Lodha Luxury Holdings & World One SPV', 'Verified 3D Cadastre', 1850.0, 'Mumbai (MMR / BMC Worli Sea Face)', 'supertall_tiered', 'champagne_gold_glass', 'illuminated_crown_spire', 'four_tier_valet_vault'),

        # --- New Delhi & NCR (Delhi: State Code 07, Haryana: 06) ---
        (201, 'Connaught Outer Circle Heritage Colonnade', 'New Delhi', 'Delhi', 7, 1, 101, 10, 'Commercial', 28.6328, 77.2197, 0, 75, 'New Delhi Municipal Council (NDMC)', 'Heritage Buffer 3D', 950.0, 'New Delhi (NCT / NDMC Connaught Place)', 'circular_heritage_rotunda', 'terracotta_sandstone', 'rotunda_dome', 'subterranean_utility_link'),
        (202, 'Rajiv Chowk Subsurface Metro Terminal', 'New Delhi', 'Delhi', 7, 1, 101, 10, 'Subsurface Utility', 28.6328, 77.2197, -18, 18, 'Delhi Metro Rail Corp (DMRC)', 'Subsurface Multi-Level', 780.0, 'New Delhi (NCT / DMRC Rajiv Chowk Hub)', 'subterranean_multilevel_cavern', 'granite_concourse', 'central_park_rotunda', 'dual_level_metro_interchange'),
        (203, 'Aerocity Horizon Gateway', 'New Delhi', 'Delhi', 7, 2, 105, 18, 'Commercial', 28.5524, 77.1215, 0, 65, 'Delhi International Airport Ltd (DIAL)', 'Verified 3D Cadastre', 1400.0, 'New Delhi (NCT / DIAL Aerocity Gateway)', 'aerocity_curvilinear_atrium', 'silver_metallic_louver', 'aviation_beacons', 'airport_express_link'),
        (204, 'DLF Cyber City Building 10 (The Epitome)', 'Gurugram', 'Haryana', 6, 18, 102, 44, 'Commercial', 28.4952, 77.0895, 0, 140, 'DLF CyberCity Holdings & Co-Tenants', 'Verified 3D Cadastre', 2100.0, 'Gurugram (NCR / MCG Cyber City Zone)', 'skybridge_twin', 'cyber_steel_blue', 'telecom_masts', 'rapid_metro_viaduct'),

        # --- Bengaluru (Karnataka: State Code 29) ---
        (301, 'Manyata Embassy High-Tech Park', 'Bengaluru', 'Karnataka', 29, 20, 201, 15, 'Commercial', 13.0489, 77.6200, 0, 110, 'Embassy REIT Infrastructure', 'Verified 3D Cadastre', 1750.0, 'Bengaluru Urban (BBMP / Hebbal IT Corridor)', 'tech_park_interconnected_blocks', 'forest_green_solar', 'solar_pv_canopy', 'data_infrastructure_vault'),
        (302, 'Cubbon Park Underground Metro Junction', 'Bengaluru', 'Karnataka', 29, 20, 201, 11, 'Subsurface Utility', 12.9815, 77.5950, -21, 21, 'BMRCL Namma Metro Underground', 'Critical Infrastructure', 540.0, 'Bengaluru Urban (BBMP / BMRCL Central Junction)', 'subterranean_multilevel_cavern', 'heritage_stone_portal', 'botanical_ground', 'deep_shield_tunnel'),
        (303, 'UB City & Kingfisher Towers', 'Bengaluru', 'Karnataka', 29, 20, 201, 8, 'Apartment', 12.9719, 77.5958, 0, 128, 'UBHL & Prestige Luxury Living', 'Verified 3D Cadastre', 1200.0, 'Bengaluru Urban (BBMP / CBD Vittal Mallya Road)', 'stepped_spire_luxury', 'emerald_classical_glass', 'soaring_gilded_spire', 'luxury_concierge_parking'),
        (304, 'Whitefield Tech Park Nexus', 'Bengaluru', 'Karnataka', 29, 20, 203, 32, 'Commercial', 12.9860, 77.7320, 0, 95, 'Prestige Estates Projects', 'Verified 3D Cadastre', 920.0, 'Bengaluru Urban (BBMP / Whitefield IT Corridor)', 'geometric_modular_tech', 'cobalt_modular_grid', 'chill_plant_deck', 'fiber_optic_vault'),

        # --- GIFT City (Gujarat: State Code 24) ---
        (401, 'GIFT Diamond Tower Pinnacle', 'GIFT City', 'Gujarat', 24, 7, 101, 1, 'Commercial', 23.1610, 72.6840, 0, 180, 'GIFT City Authority & FinTech SPV', 'Verified 3D Cadastre', 2800.0, 'GIFT City (Gandhinagar / IFSCA Special SEZ)', 'crystalline_diamond', 'fintech_cyan_facets', 'helipad_sky_lounge', 'gift_tum_tunnel'),
        (402, 'GIFT Subsurface Utility Tunnel (TUM)', 'GIFT City', 'Gujarat', 24, 7, 101, 1, 'Subsurface Utility', 23.1620, 72.6850, -16, 16, 'GIFT Urban Infrastructure Ltd', 'Subsurface Automated Utility', 890.0, 'GIFT City (Gandhinagar / Automated TUM Trench)', 'utility_tunnel_trench', 'industrial_concrete', 'smart_boulevard', 'cooling_waste_power_trays'),
        (403, 'GIFT Aspire Smart Residential', 'GIFT City', 'Gujarat', 24, 7, 101, 3, 'Apartment', 23.1590, 72.6820, 0, 105, 'GIFT Housing Development Authority', 'Verified 3D Cadastre', 470.0, 'GIFT City (Gandhinagar / Smart Residential Enclave)', 'smart_modular_residential', 'biophilic_green_facade', 'rooftop_hydroponics', 'automated_car_stacker'),

        # --- Hyderabad (Telangana: State Code 36) ---
        (501, 'HITEC Cyber Towers (Cyberabad)', 'Hyderabad', 'Telangana', 36, 12, 101, 2, 'Commercial', 17.4504, 78.3808, 0, 135, 'Telangana State Ind. Infra Corp (TSIIC)', 'Verified 3D Cadastre', 1600.0, 'Hyderabad (GHMC / Cyberabad HITEC City)', 'cyber_cylindrical_radial', 'hyderabad_granite_azure', 'central_helipad_h', 'data_grid_bunker'),
        (502, 'Cyberabad Subsurface Data Vault', 'Hyderabad', 'Telangana', 36, 12, 101, 2, 'Subsurface Utility', 17.4490, 78.3795, -20, 20, 'National Cloud & Data Grid SPV', 'High-Security Subsurface', 620.0, 'Hyderabad (GHMC / Cyberabad Data Infrastructure)', 'subterranean_bunker_vault', 'blast_reinforced_walls', 'surface_substation', 'tier4_server_chambers'),
        (503, 'Durgam Cheruvu Mixed Urban Hub', 'Hyderabad', 'Telangana', 36, 12, 102, 14, 'Transit', 17.4330, 78.3870, 0, 45, 'Hyderabad Metro Rail & HMDA', 'Verified 3D Cadastre', 390.0, 'Hyderabad (GHMC / HMDA Durgam Cheruvu Hub)', 'cable_stayed_transit_hub', 'cable_stay_composite', 'cable_pylons', 'cable_anchorage_vault'),

        # --- Chennai (Tamil Nadu: State Code 33) ---
        (601, 'TIDEL Park (OMR IT Expressway)', 'Chennai', 'Tamil Nadu', 33, 2, 104, 21, 'Commercial', 12.9892, 80.2486, 0, 85, 'TIDEL Park Ltd (TIDCO)', 'Verified 3D Cadastre', 980.0, 'Chennai (GCC / OMR IT Expressway Corridor)', 'it_linear_spine', 'monolithic_slate_glass', 'long_span_cooling_rigs', 'expressway_storm_reservoir'),
        (602, 'Chennai Central Underground Transit Hub', 'Chennai', 'Tamil Nadu', 33, 2, 101, 5, 'Subsurface Utility', 13.0827, 80.2755, -22, 22, 'CMRL Underground Metro', 'Subsurface Title Active', 720.0, 'Chennai (GCC / CMRL Central Interchange)', 'subterranean_multilevel_cavern', 'heritage_red_portal', 'historic_railway_square', 'triple_tier_metro_concourse'),

        # --- Kolkata (West Bengal: State Code 19) ---
        (701, 'New Town EcoSpace Tech Centre', 'Kolkata', 'West Bengal', 19, 11, 103, 19, 'Commercial', 22.5855, 88.4680, 0, 92, 'Bengal Ambuja Housing Ltd', 'Verified 3D Cadastre', 810.0, 'Kolkata (WBHIDCO / New Town Rajarhat IT Hub)', 'green_terrace_commercial', 'eco_bamboo_glass', 'hanging_gardens', 'rainwater_harvesting_aquifer'),
        (702, 'Hooghly Underwater Subsurface Corridor', 'Kolkata', 'West Bengal', 19, 11, 101, 1, 'Subsurface Utility', 22.5820, 88.3510, -32, 32, 'KMRCL Underwater Metro', 'Underwater Engineering Marvel', 1150.0, 'Kolkata (KMC / KMRCL Underwater Hooghly Line)', 'underwater_subaqueous_tunnel', 'subaqueous_shield_rings', 'hooghly_riverbed', 'twin_underwater_train_tubes')
    ]

    cursor.executemany('''
    INSERT INTO property_parcels 
    (property_id, name, city, state, state_code, dist_code, sub_dist_code, village_code, type, lat, lon, base_elevation, total_height, owner, status, valuation_cr, zone, archetype, facade_theme, roof_feature, subsurface_infra) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', sample_data)

    conn.commit()

    # Also update CSV for file-based fallback/interoperability
    df = pd.read_sql_query("SELECT * FROM property_parcels", conn)
    csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'mock_city_data.csv')
    df.to_csv(csv_path, index=False)

    conn.close()
    print(f"Database initialized successfully at {db_path} with {len(sample_data)} Pan-India parcels!")

if __name__ == '__main__':
    initialize_db()