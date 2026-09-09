-- 3D Cadastral Property Parcels with Vertical & Subsurface Attributes
CREATE TABLE IF NOT EXISTS property_parcels (
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
);
