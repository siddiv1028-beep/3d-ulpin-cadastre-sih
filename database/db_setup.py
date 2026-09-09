import sqlite3
import os
import pandas as pd

def initialize_db():
    db_path = os.path.join(os.path.dirname(__file__), 'spatial_records.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Drop existing table if structure changed
    cursor.execute('DROP TABLE IF EXISTS property_parcels')

    # Create the enhanced 3D property table with Pan-India cadastral fields
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
        zone TEXT
    )
    ''')

    # Comprehensive Pan-India Cadastral Dataset (clean Python integers)
    sample_data = [
        # --- Navi Mumbai & Mumbai MMR (Maharashtra: State Code 27) ---
        (101, 'Seawoods Grand Central', 'Navi Mumbai', 'Maharashtra', 27, 21, 101, 50, 'Commercial', 19.0216, 73.0181, 0, 120, 'L&T Realty & Seawoods Corp', 'Verified 3D Cadastre', 850.0, 'Commercial Core'),
        (102, 'Grand Central Subsurface Concourse', 'Navi Mumbai', 'Maharashtra', 27, 21, 101, 50, 'Underground Parking', 19.0216, 73.0181, -15, 15, 'CIDCO Urban Infra', 'Subsurface Title Active', 180.0, 'Transit Subsurface'),
        (103, 'Palm Beach Residency Pinnacle', 'Navi Mumbai', 'Maharashtra', 27, 21, 101, 52, 'Apartment', 19.0245, 73.0115, 0, 85, 'Palm Beach Residents Welfare', 'Verified 3D Cadastre', 320.0, 'Residential High-Density'),
        (104, 'Seawoods Urban Transit Terminal', 'Navi Mumbai', 'Maharashtra', 27, 21, 101, 51, 'Transit', 19.0180, 73.0190, 0, 35, 'Indian Railways / CIDCO', 'Public Utility Asset', 420.0, 'Multimodal Hub'),
        (105, 'BKC Diamond Tower', 'Mumbai', 'Maharashtra', 27, 22, 104, 12, 'Commercial', 19.0657, 72.8688, 0, 160, 'MMRDA & Global Diamond Bourse', 'Verified 3D Cadastre', 2400.0, 'Special Financial Zone'),
        (106, 'BKC Metro-3 Underground Vault', 'Mumbai', 'Maharashtra', 27, 22, 104, 12, 'Subsurface Utility', 19.0665, 72.8695, -24, 24, 'MMRCL Underground Corridor', 'Critical Infrastructure', 680.0, 'Subsurface Transit'),
        (107, 'Worli Sea-Facing Super-Tower', 'Mumbai', 'Maharashtra', 27, 22, 108, 5, 'Apartment', 19.0178, 72.8172, 0, 240, 'Lodha Luxury Holdings', 'Verified 3D Cadastre', 1850.0, 'Coastal Residential'),

        # --- New Delhi & NCR (Delhi: State Code 07, Haryana: 06) ---
        (201, 'Connaught Outer Circle Tower', 'New Delhi', 'Delhi', 7, 1, 101, 10, 'Commercial', 28.6328, 77.2197, 0, 75, 'NDMC Heritage & Commercial', 'Heritage Buffer 3D', 950.0, 'Central Business Dist'),
        (202, 'Rajiv Chowk Subsurface Metro Terminal', 'New Delhi', 'Delhi', 7, 1, 101, 10, 'Subsurface Utility', 28.6328, 77.2197, -18, 18, 'DMRC Underground Network', 'Subsurface Multi-Level', 780.0, 'Transit Interchange'),
        (203, 'Aerocity Horizon Gateway', 'New Delhi', 'Delhi', 7, 2, 105, 18, 'Commercial', 28.5524, 77.1215, 0, 65, 'DIAL Aerocity Developers', 'Verified 3D Cadastre', 1400.0, 'Aviation Commercial'),
        (204, 'Cyber City Epitome Horizon', 'Gurugram', 'Haryana', 6, 18, 102, 44, 'Commercial', 28.4952, 77.0895, 0, 140, 'DLF CyberCity Holdings', 'Verified 3D Cadastre', 2100.0, 'IT & Cyber Park'),

        # --- Bengaluru (Karnataka: State Code 29) ---
        (301, 'Manyata Embassy High-Tech Park', 'Bengaluru', 'Karnataka', 29, 20, 201, 15, 'Commercial', 13.0489, 77.6200, 0, 110, 'Embassy REIT Infrastructure', 'Verified 3D Cadastre', 1750.0, 'IT Corridor'),
        (302, 'Cubbon Park Underground Metro Junction', 'Bengaluru', 'Karnataka', 29, 20, 201, 11, 'Subsurface Utility', 12.9815, 77.5950, -21, 21, 'BMRCL Namma Metro Underground', 'Critical Infrastructure', 540.0, 'Transit Subsurface'),
        (303, 'UB City Pinnacle Sky Suites', 'Bengaluru', 'Karnataka', 29, 20, 201, 8, 'Apartment', 12.9719, 77.5958, 0, 128, 'UBHL Luxury Living', 'Verified 3D Cadastre', 1200.0, 'Commercial Mixed-Use'),
        (304, 'Whitefield Tech Park Nexus', 'Bengaluru', 'Karnataka', 29, 20, 203, 32, 'Commercial', 12.9860, 77.7320, 0, 95, 'Prestige Estates Projects', 'Verified 3D Cadastre', 920.0, 'Tech SEZ Zone'),

        # --- GIFT City (Gujarat: State Code 24) ---
        (401, 'GIFT Diamond Tower Pinnacle', 'GIFT City', 'Gujarat', 24, 7, 101, 1, 'Commercial', 23.1610, 72.6840, 0, 180, 'GIFT City Authority & FinTech SPV', 'Verified 3D Cadastre', 2800.0, 'International FinTech SEZ'),
        (402, 'GIFT Subsurface Utility Tunnel (TUM)', 'GIFT City', 'Gujarat', 24, 7, 101, 1, 'Subsurface Utility', 23.1620, 72.6850, -16, 16, 'GIFT Urban Infrastructure Ltd', 'Subsurface Automated Utility', 890.0, 'Utility Corridors'),
        (403, 'GIFT Aspire Smart Residential', 'GIFT City', 'Gujarat', 24, 7, 101, 3, 'Apartment', 23.1590, 72.6820, 0, 105, 'GIFT Housing Development', 'Verified 3D Cadastre', 470.0, 'Smart Residential'),

        # --- Hyderabad (Telangana: State Code 36) ---
        (501, 'HITEC Cyber Towers Skyrise', 'Hyderabad', 'Telangana', 36, 12, 101, 2, 'Commercial', 17.4504, 78.3808, 0, 135, 'Telangana State Ind. Infra Corp', 'Verified 3D Cadastre', 1600.0, 'Cyberabad Tech Zone'),
        (502, 'Cyberabad Subsurface Data Vault', 'Hyderabad', 'Telangana', 36, 12, 101, 2, 'Subsurface Utility', 17.4490, 78.3795, -20, 20, 'National Cloud & Data Grid', 'High-Security Subsurface', 620.0, 'Digital Infrastructure'),
        (503, 'Durgam Cheruvu Mixed Urban Hub', 'Hyderabad', 'Telangana', 36, 12, 102, 14, 'Transit', 17.4330, 78.3870, 0, 45, 'Hyderabad Metro Rail & HMDA', 'Verified 3D Cadastre', 390.0, 'Waterfront Commercial'),

        # --- Chennai (Tamil Nadu: State Code 33) ---
        (601, 'TIDEL Park IT Expressway Tower', 'Chennai', 'Tamil Nadu', 33, 2, 104, 21, 'Commercial', 12.9892, 80.2486, 0, 85, 'TIDEL Park Ltd (TIDCO)', 'Verified 3D Cadastre', 980.0, 'OMR IT Corridor'),
        (602, 'Chennai Central Underground Transit Hub', 'Chennai', 'Tamil Nadu', 33, 2, 101, 5, 'Subsurface Utility', 13.0827, 80.2755, -22, 22, 'CMRL Underground Metro', 'Subsurface Title Active', 720.0, 'Transit Interchange'),

        # --- Kolkata (West Bengal: State Code 19) ---
        (701, 'New Town EcoSpace Tech Centre', 'Kolkata', 'West Bengal', 19, 11, 103, 19, 'Commercial', 22.5855, 88.4680, 0, 92, 'Bengal Ambuja Housing Ltd', 'Verified 3D Cadastre', 810.0, 'New Town IT Hub'),
        (702, 'Hooghly Underwater Subsurface Corridor', 'Kolkata', 'West Bengal', 19, 11, 101, 1, 'Subsurface Utility', 22.5820, 88.3510, -32, 32, 'KMRCL Underwater Metro', 'Underwater Engineering Marvel', 1150.0, 'Sub-riverine Transit')
    ]

    cursor.executemany('''
    INSERT INTO property_parcels 
    (property_id, name, city, state, state_code, dist_code, sub_dist_code, village_code, type, lat, lon, base_elevation, total_height, owner, status, valuation_cr, zone) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
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