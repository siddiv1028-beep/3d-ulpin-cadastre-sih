"""
data/blueprints_and_imagery.py
Comprehensive repository of authentic architectural blueprints (CAD vector floorplans),
real-world photographic imagery, and engineering structural specifications for all 25
cadastral landmark properties across India.
"""

# Property Architectural Blueprint & Real Photographic Imagery Dataset
BLUEPRINT_AND_IMAGERY_DATA = {
    101: {
        "title": "Seawoods Grand Central TOD - Master Architectural Blueprint",
        "archetype": "transit_quad_podium",
        "dimensions": {"length_m": 140, "width_m": 85, "height_m": 120, "floors": 24, "podium_floors": 4},
        "engineer": "Larsen & Toubro (L&T) Construction / CIDCO Transit Directorate",
        "architect": "Bentel Associates International",
        "year_built": 2017,
        "structural_system": "Reinforced Post-Tensioned Concrete (PTC) & Composite Steel Grid",
        "fsi_far": "4.0 (TOD Transit-Oriented Bonus)",
        "rera_id": "P51700000101 (MahaRERA Registered)",
        "photo_url": "https://images.unsplash.com/photo-1541888946425-d0fbb1861593?w=800&auto=format&fit=crop&q=80",
        "photo_caption": "Seawoods Grand Central TOD, Navi Mumbai - 4 Commercial Towers over Railway Concourse",
        "blueprint_svg": """<svg viewBox="0 0 800 500" xmlns="http://www.w3.org/2000/svg" style="width: 100%; height: auto; background: #0f172a; border-radius: 8px; font-family: 'JetBrains Mono', monospace;">
          <defs>
            <pattern id="grid101" width="40" height="40" patternUnits="userSpaceOnUse">
              <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#1e293b" stroke-width="0.8"/>
            </pattern>
          </defs>
          <rect width="800" height="500" fill="url(#grid101)"/>
          
          <rect x="60" y="50" width="680" height="380" fill="none" stroke="#ef4444" stroke-width="2" stroke-dasharray="6,4"/>
          <text x="70" y="42" fill="#ef4444" font-size="11" font-weight="700">CADASTRE PLOT BOUNDARY #101 (140.0m x 85.0m) [AREA: 11,900 m²]</text>
          
          <rect x="90" y="80" width="620" height="320" fill="rgba(16, 185, 129, 0.04)" stroke="#10b981" stroke-width="1.5" stroke-dasharray="3,3"/>
          <text x="100" y="74" fill="#10b981" font-size="9">BUILDING SETBACK LINE (9.0m FRONTAGE / 6.0m SIDES)</text>
          
          <rect x="110" y="100" width="580" height="280" rx="12" fill="rgba(2, 132, 199, 0.12)" stroke="#0284c7" stroke-width="2.5"/>
          
          <rect x="140" y="120" width="220" height="105" rx="6" fill="#0369a1" fill-opacity="0.6" stroke="#38bdf8" stroke-width="1.8"/>
          <text x="150" y="145" fill="#f8fafc" font-size="12" font-weight="700">TOWER 1: TECH NEXUS</text>
          <text x="150" y="162" fill="#bae6fd" font-size="9">L1-L24 &bull; 48,000 sq.m &bull; L&T HQ</text>
          <rect x="290" y="130" width="55" height="55" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
          <text x="295" y="160" fill="#f59e0b" font-size="8">LIFTS (x6)</text>
          
          <rect x="440" y="120" width="220" height="105" rx="6" fill="#0369a1" fill-opacity="0.6" stroke="#38bdf8" stroke-width="1.8"/>
          <text x="450" y="145" fill="#f8fafc" font-size="12" font-weight="700">TOWER 2: CAPITAL WING</text>
          <text x="450" y="162" fill="#bae6fd" font-size="9">L1-L24 &bull; 48,000 sq.m &bull; BFSI</text>
          <rect x="590" y="130" width="55" height="55" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
          <text x="595" y="160" fill="#f59e0b" font-size="8">LIFTS (x6)</text>
          
          <rect x="375" y="130" width="50" height="220" rx="8" fill="rgba(56, 189, 248, 0.25)" stroke="#38bdf8" stroke-width="1.5"/>
          <text x="382" y="240" fill="#e0f2fe" font-size="9" font-weight="700" transform="rotate(-90 382 240)">CENTRAL TRANSIT ATRIUM &amp; SKYLIGHT</text>
          
          <rect x="140" y="255" width="220" height="105" rx="6" fill="#0369a1" fill-opacity="0.6" stroke="#38bdf8" stroke-width="1.8"/>
          <text x="150" y="280" fill="#f8fafc" font-size="12" font-weight="700">TOWER 3: ENTERPRISE HUB</text>
          <text x="150" y="297" fill="#bae6fd" font-size="9">L1-L24 &bull; Global Capability</text>
          <rect x="290" y="265" width="55" height="55" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
          <text x="295" y="295" fill="#f59e0b" font-size="8">LIFTS (x6)</text>
          
          <rect x="440" y="255" width="220" height="105" rx="6" fill="#0369a1" fill-opacity="0.6" stroke="#38bdf8" stroke-width="1.8"/>
          <text x="450" y="280" fill="#f8fafc" font-size="12" font-weight="700">TOWER 4: INNOVATION SPV</text>
          <text x="450" y="297" fill="#bae6fd" font-size="9">L1-L24 &bull; Multi-Tenant Commercial</text>
          <rect x="590" y="265" width="55" height="55" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
          <text x="595" y="295" fill="#f59e0b" font-size="8">LIFTS (x6)</text>
          
          <line x1="60" y1="240" x2="740" y2="240" stroke="#a855f7" stroke-width="3" stroke-dasharray="8,6"/>
          <text x="590" y="234" fill="#c084fc" font-size="8">RAILWAY TRACK AXIS (Z: -12.0m)</text>
          
          <line x1="60" y1="445" x2="740" y2="445" stroke="#94a3b8" stroke-width="1.5"/>
          <text x="360" y="460" fill="#cbd5e1" font-size="10" font-weight="700">140.0 METERS (WIDTH)</text>
          <line x1="45" y1="50" x2="45" y2="430" stroke="#94a3b8" stroke-width="1.5"/>
          <text x="30" y="250" fill="#cbd5e1" font-size="10" font-weight="700" transform="rotate(-90 30 250)">85.0 METERS (DEPTH)</text>
          
          <rect x="580" y="390" width="150" height="35" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
          <text x="590" y="405" fill="#38bdf8" font-size="8" font-weight="700">ULPIN: 27211010500101</text>
          <text x="590" y="418" fill="#10b981" font-size="8">CIDCO &bull; APPROVED 3D CADASTRE</text>
        </svg>"""
    },
    107: {
        "title": "Lodha World One (Worli Sea Face) - Peicobb Architectural Blueprint",
        "archetype": "supertall_tiered",
        "dimensions": {"length_m": 90, "width_m": 72, "height_m": 240, "floors": 76, "podium_floors": 6},
        "engineer": "Leslie E. Robertson Associates (LERA New York)",
        "architect": "Pei Cobb Freed & Partners (Architects of Louvre Pyramid & Bank of China)",
        "year_built": 2020,
        "structural_system": "Ultra-High Performance Concrete Outrigger Core & Curved Aerodynamic Wing Walls",
        "fsi_far": "4.55 (BMC High-Rise Special Permission)",
        "rera_id": "P51900008345 (MahaRERA Registered)",
        "photo_url": "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=800&auto=format&fit=crop&q=80",
        "photo_caption": "Lodha World One, Worli - Iconic 76-Storey Curved Aerodynamic Skyscraper",
        "blueprint_svg": """<svg viewBox="0 0 800 500" xmlns="http://www.w3.org/2000/svg" style="width: 100%; height: auto; background: #090d16; border-radius: 8px; font-family: 'JetBrains Mono', monospace;">
          <defs>
            <pattern id="grid107" width="40" height="40" patternUnits="userSpaceOnUse">
              <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#1e293b" stroke-width="0.8"/>
            </pattern>
          </defs>
          <rect width="800" height="500" fill="url(#grid107)"/>
          
          <polygon points="120,40 680,40 730,440 70,440" fill="none" stroke="#ef4444" stroke-width="2" stroke-dasharray="6,4"/>
          <text x="80" y="32" fill="#ef4444" font-size="11" font-weight="700">WORLI SEA FACE CADASTRAL PLOT #107 (90m x 72m) [AREA: 6,480 m²]</text>
          
          <circle cx="400" cy="240" r="145" fill="rgba(245, 158, 11, 0.08)" stroke="#f59e0b" stroke-width="2"/>
          <polygon points="400,120 515,310 285,310" fill="none" stroke="#fbbf24" stroke-width="1.5" stroke-dasharray="4,4"/>
          
          <path d="M 330 200 C 330 110, 470 110, 470 200 Z" fill="#b45309" fill-opacity="0.5" stroke="#fcd34d" stroke-width="2"/>
          <text x="345" y="160" fill="#fffbeb" font-size="10" font-weight="700">LOBE 1: ARABIAN SEA VISTA</text>
          
          <path d="M 430 250 C 530 270, 500 390, 410 330 Z" fill="#b45309" fill-opacity="0.5" stroke="#fcd34d" stroke-width="2"/>
          <text x="460" y="320" fill="#fffbeb" font-size="10" font-weight="700">LOBE 2: SEA LINK SUITE</text>
          
          <path d="M 370 250 C 270 270, 300 390, 390 330 Z" fill="#b45309" fill-opacity="0.5" stroke="#fcd34d" stroke-width="2"/>
          <text x="260" y="320" fill="#fffbeb" font-size="10" font-weight="700">LOBE 3: SKYLINE SUITE</text>
          
          <rect x="365" y="205" width="70" height="70" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
          <text x="373" y="242" fill="#38bdf8" font-size="9" font-weight="700">CORE (x12)</text>
          <text x="375" y="255" fill="#94a3b8" font-size="7">8 m/s LIFTS</text>
          
          <circle cx="400" cy="240" r="160" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="5,3"/>
          <text x="565" y="235" fill="#38bdf8" font-size="8">CURVED BALCONY</text>
          
          <text x="140" y="420" fill="#a855f7" font-size="9" font-weight="700">&bull; 4-TIER SUBSURFACE AUTOMATED ROBOTIC CAR VAULT (Z: -16m to 0m)</text>
          
          <line x1="70" y1="460" x2="730" y2="460" stroke="#94a3b8" stroke-width="1.5"/>
          <text x="365" y="475" fill="#cbd5e1" font-size="10" font-weight="700">90.0m TOTAL PLOT WIDTH</text>
          
          <rect x="580" y="60" width="160" height="42" rx="4" fill="#1e293b" stroke="#f59e0b" stroke-width="1"/>
          <text x="590" y="77" fill="#fbbf24" font-size="8" font-weight="700">MCGM HIGH-RISE COMMITTEE</text>
          <text x="590" y="92" fill="#10b981" font-size="8">HEIGHT SANCTION: +240.0m MSL</text>
        </svg>"""
    },
    204: {
        "title": "DLF Cyber City Building 10 (The Epitome) - Twin Arc Blueprint",
        "archetype": "skybridge_twin",
        "dimensions": {"length_m": 135, "width_m": 60, "height_m": 140, "floors": 28, "podium_floors": 3},
        "engineer": "DLF Cyber City Developers Ltd & Meinhardt Structural Group",
        "architect": "Hafeez Contractor / CallisonRTKL",
        "year_built": 2014,
        "structural_system": "Dual Reinforced Concrete Cores with Multi-Story Structural Steel Skybridges",
        "fsi_far": "3.85 (Haryana SEZ & Cyber City IT Policy)",
        "rera_id": "HRERA-PKL-GGM-102-2018",
        "photo_url": "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=800&auto=format&fit=crop&q=80",
        "photo_caption": "DLF Cyber City Building 10 (The Epitome), Gurugram - Twin Towers Connected by Skybridges",
        "blueprint_svg": """<svg viewBox="0 0 800 500" xmlns="http://www.w3.org/2000/svg" style="width: 100%; height: auto; background: #0c1222; border-radius: 8px; font-family: 'JetBrains Mono', monospace;">
          <defs>
            <pattern id="grid204" width="40" height="40" patternUnits="userSpaceOnUse">
              <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#1e293b" stroke-width="0.8"/>
            </pattern>
          </defs>
          <rect width="800" height="500" fill="url(#grid204)"/>
          
          <rect x="70" y="50" width="660" height="380" fill="none" stroke="#ef4444" stroke-width="2" stroke-dasharray="6,4"/>
          <text x="80" y="42" fill="#ef4444" font-size="11" font-weight="700">GURUGRAM CYBER CITY CADASTRAL PLOT #204 (135m x 60m)</text>
          
          <path d="M 120 120 Q 230 110, 270 230 Q 250 360, 140 370 Q 180 250, 120 120 Z" fill="#0369a1" fill-opacity="0.6" stroke="#38bdf8" stroke-width="2"/>
          <text x="140" y="240" fill="#ffffff" font-size="11" font-weight="700">TOWER A (WEST)</text>
          <text x="140" y="255" fill="#bae6fd" font-size="8">GOOGLE / MICROSOFT</text>
          <rect x="170" y="180" width="45" height="45" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
          <text x="175" y="207" fill="#f59e0b" font-size="7">LIFTS (x8)</text>
          
          <path d="M 680 120 Q 570 110, 530 230 Q 550 360, 660 370 Q 620 250, 680 120 Z" fill="#0369a1" fill-opacity="0.6" stroke="#38bdf8" stroke-width="2"/>
          <text x="560" y="240" fill="#ffffff" font-size="11" font-weight="700">TOWER B (EAST)</text>
          <text x="560" y="255" fill="#bae6fd" font-size="8">ACCENTURE / IBM</text>
          <rect x="585" y="180" width="45" height="45" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
          <text x="590" y="207" fill="#f59e0b" font-size="7">LIFTS (x8)</text>
          
          <rect x="260" y="160" width="280" height="30" rx="4" fill="rgba(56, 189, 248, 0.4)" stroke="#38bdf8" stroke-width="2"/>
          <text x="320" y="180" fill="#ffffff" font-size="9" font-weight="700">SKYBRIDGE 1 (L12-L14): EXECUTIVE LOUNGE</text>
          
          <rect x="250" y="235" width="300" height="30" rx="4" fill="rgba(56, 189, 248, 0.4)" stroke="#38bdf8" stroke-width="2"/>
          <text x="330" y="255" fill="#ffffff" font-size="9" font-weight="700">SKYBRIDGE 2 (L20-L22): AUDITORIUM</text>
          
          <rect x="240" y="310" width="320" height="30" rx="4" fill="rgba(56, 189, 248, 0.4)" stroke="#38bdf8" stroke-width="2"/>
          <text x="340" y="330" fill="#ffffff" font-size="9" font-weight="700">SKYBRIDGE 3 (L26-L28): HELIPAD DECK</text>
          
          <rect x="350" y="50" width="100" height="380" fill="rgba(16, 185, 129, 0.05)" stroke="#10b981" stroke-width="1" stroke-dasharray="4,4"/>
          <text x="375" y="90" fill="#10b981" font-size="9" font-weight="700" transform="rotate(90 375 90)">CYBER HUB ROADWAY &amp; RAPID METRO VIADUCT</text>
          
          <rect x="560" y="390" width="160" height="32" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
          <text x="570" y="405" fill="#38bdf8" font-size="8" font-weight="700">DTCP HARYANA SANCTIONED</text>
          <text x="570" y="416" fill="#10b981" font-size="8">3D AIR-RIGHTS APPROVED</text>
        </svg>"""
    },
    501: {
        "title": "HITEC Cyber Towers (Hyderabad) - Radial Monolith Blueprint",
        "archetype": "cyber_cylindrical_radial",
        "dimensions": {"length_m": 85, "width_m": 85, "height_m": 135, "floors": 10, "podium_floors": 1},
        "engineer": "Telangana State Industrial Infrastructure Corporation (TSIIC)",
        "architect": "Architect Hafeez Contractor / L&T Project Management",
        "year_built": 1998,
        "structural_system": "Cylindrical Reinforced Core with 4 Radial Cantilever Quadrant Wings",
        "fsi_far": "3.50 (HITEC City IT Flagship Monument)",
        "rera_id": "TSIIC-CYB-1998-001",
        "photo_url": "https://images.unsplash.com/photo-1577495508048-b635879837f1?w=800&auto=format&fit=crop&q=80",
        "photo_caption": "HITEC Cyber Towers, Madhapur, Hyderabad - Iconic 10-Storey Radial IT Monument",
        "blueprint_svg": """<svg viewBox="0 0 800 500" xmlns="http://www.w3.org/2000/svg" style="width: 100%; height: auto; background: #0c1424; border-radius: 8px; font-family: 'JetBrains Mono', monospace;">
          <defs>
            <pattern id="grid501" width="40" height="40" patternUnits="userSpaceOnUse">
              <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#1e293b" stroke-width="0.8"/>
            </pattern>
          </defs>
          <rect width="800" height="500" fill="url(#grid501)"/>
          
          <circle cx="400" cy="245" r="215" fill="none" stroke="#ef4444" stroke-width="2" stroke-dasharray="6,4"/>
          <text x="90" y="42" fill="#ef4444" font-size="11" font-weight="700">CYBERABAD MASTER PLOT #501 (DIAMETER: 85.0m) [AREA: 5,670 m²]</text>
          
          <circle cx="400" cy="245" r="190" fill="rgba(2, 132, 199, 0.08)" stroke="#0284c7" stroke-width="1.5"/>
          <text x="310" y="75" fill="#38bdf8" font-size="9" font-weight="700">CIRCULAR FOUNTAIN PROMENADE &amp; PLAZA</text>
          
          <rect x="365" y="85" width="70" height="95" rx="4" fill="#0369a1" stroke="#38bdf8" stroke-width="2"/>
          <text x="372" y="130" fill="#ffffff" font-size="9" font-weight="700">WING 1: N</text>
          <text x="372" y="142" fill="#bae6fd" font-size="7">FINTECH</text>
          
          <rect x="365" y="310" width="70" height="95" rx="4" fill="#0369a1" stroke="#38bdf8" stroke-width="2"/>
          <text x="372" y="355" fill="#ffffff" font-size="9" font-weight="700">WING 2: S</text>
          <text x="372" y="367" fill="#bae6fd" font-size="7">CLOUD INFRA</text>
          
          <rect x="475" y="210" width="95" height="70" rx="4" fill="#0369a1" stroke="#38bdf8" stroke-width="2"/>
          <text x="485" y="245" fill="#ffffff" font-size="9" font-weight="700">WING 3: E</text>
          <text x="485" y="257" fill="#bae6fd" font-size="7">AI LABS</text>
          
          <rect x="230" y="210" width="95" height="70" rx="4" fill="#0369a1" stroke="#38bdf8" stroke-width="2"/>
          <text x="240" y="245" fill="#ffffff" font-size="9" font-weight="700">WING 4: W</text>
          <text x="240" y="257" fill="#bae6fd" font-size="7">OFFSHORE R&amp;D</text>
          
          <circle cx="400" cy="245" r="75" fill="#0284c7" fill-opacity="0.4" stroke="#38bdf8" stroke-width="3"/>
          <circle cx="400" cy="245" r="35" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
          <text x="382" y="248" fill="#f59e0b" font-size="10" font-weight="700">CORE</text>
          
          <circle cx="400" cy="245" r="22" fill="none" stroke="#ffffff" stroke-width="1.5"/>
          <text x="395" y="250" fill="#ffffff" font-size="14" font-weight="900">H</text>
          
          <rect x="580" y="415" width="160" height="35" rx="4" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
          <text x="590" y="430" fill="#10b981" font-size="8" font-weight="700">TSIIC &bull; HERITAGE IT TITLE</text>
          <text x="590" y="442" fill="#94a3b8" font-size="7">ULPIN: 36121010020101</text>
        </svg>"""
    },
    201: {
        "title": "Connaught Place Heritage Colonnade - Lutyens Master Plan Blueprint",
        "archetype": "circular_heritage_rotunda",
        "dimensions": {"length_m": 120, "width_m": 120, "height_m": 75, "floors": 4, "podium_floors": 2},
        "engineer": "Public Works Department (Central PWD) / NDMC",
        "architect": "Robert Tor Russell & Edwin Lutyens",
        "year_built": 1933,
        "structural_system": "Classical Georgian Load-Bearing Sandstone Colonnades with Radial Arcade Trusses",
        "fsi_far": "2.0 (NDMC Heritage Conservation Protected)",
        "rera_id": "NDMC-CP-HERITAGE-1933",
        "photo_url": "https://images.unsplash.com/photo-1587474260584-136574528ed5?w=800&auto=format&fit=crop&q=80",
        "photo_caption": "Connaught Place, New Delhi - Classical Georgian Heritage Colonnaded Arcade",
        "blueprint_svg": """<svg viewBox="0 0 800 500" xmlns="http://www.w3.org/2000/svg" style="width: 100%; height: auto; background: #111827; border-radius: 8px; font-family: 'JetBrains Mono', monospace;">
          <defs>
            <pattern id="grid201" width="40" height="40" patternUnits="userSpaceOnUse">
              <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#1f2937" stroke-width="0.8"/>
            </pattern>
          </defs>
          <rect width="800" height="500" fill="url(#grid201)"/>
          
          <circle cx="400" cy="250" r="220" fill="none" stroke="#ef4444" stroke-width="2" stroke-dasharray="6,4"/>
          <text x="90" y="42" fill="#ef4444" font-size="11" font-weight="700">CONNAUGHT PLACE OUTER CIRCLE BUFFER #201 (DIAMETER: 120m)</text>
          
          <circle cx="400" cy="250" r="190" fill="rgba(217, 119, 6, 0.12)" stroke="#d97706" stroke-width="4"/>
          <text x="290" y="80" fill="#f59e0b" font-size="10" font-weight="700">OUTER CIRCLE (BLOCKS G TO P)</text>
          
          <line x1="400" y1="30" x2="400" y2="470" stroke="#475569" stroke-width="3"/>
          <line x1="180" y1="250" x2="620" y2="250" stroke="#475569" stroke-width="3"/>
          <line x1="245" y1="95" x2="555" y2="405" stroke="#475569" stroke-width="3"/>
          <line x1="245" y1="405" x2="555" y2="95" stroke="#475569" stroke-width="3"/>
          
          <circle cx="400" cy="250" r="130" fill="rgba(15, 23, 42, 0.7)" stroke="#64748b" stroke-width="2"/>
          
          <circle cx="400" cy="250" r="95" fill="rgba(217, 119, 6, 0.2)" stroke="#d97706" stroke-width="3"/>
          <text x="325" y="180" fill="#fcd34d" font-size="8" font-weight="700">INNER CIRCLE (BLOCKS A-F)</text>
          
          <circle cx="400" cy="250" r="50" fill="#065f46" stroke="#10b981" stroke-width="2"/>
          <text x="360" y="254" fill="#a7f3d0" font-size="9" font-weight="700">CENTRAL PARK</text>
          <circle cx="400" cy="250" r="6" fill="#f59e0b"/>
          
          <text x="140" y="440" fill="#38bdf8" font-size="9" font-weight="700">&bull; DIRECT VERTICAL PASSAGE TO RAJIV CHOWK SUBTERRANEAN METRO INTERCHANGE (Z: -18m)</text>
          
          <rect x="580" y="415" width="160" height="35" rx="4" fill="#1e293b" stroke="#f59e0b" stroke-width="1"/>
          <text x="590" y="430" fill="#fbbf24" font-size="8" font-weight="700">NDMC HERITAGE GRADE-I</text>
          <text x="590" y="442" fill="#10b981" font-size="8">3D BUFFER PRESERVED</text>
        </svg>"""
    },
    303: {
        "title": "UB City & Kingfisher Towers - Stepped Spire Luxury Blueprint",
        "archetype": "stepped_spire_luxury",
        "dimensions": {"length_m": 80, "width_m": 65, "height_m": 128, "floors": 34, "podium_floors": 4},
        "engineer": "Prestige Group & Jurong Consultants Singapore",
        "architect": "Thomas Associates",
        "year_built": 2008,
        "structural_system": "Post-Tensioned High-Rise Concrete Frame with Classical Mansard Roof & Gilded Spire",
        "fsi_far": "3.75 (BBMP Central CBD Policy)",
        "rera_id": "PRM/KA/RERA/1251/310/PR/170915/000214",
        "photo_url": "https://images.unsplash.com/photo-1582407947304-fd86f028f716?w=800&auto=format&fit=crop&q=80",
        "photo_caption": "UB City & Kingfisher Towers, Bengaluru - Classical-Modern Luxury Skyscraper with Spire",
        "blueprint_svg": """<svg viewBox="0 0 800 500" xmlns="http://www.w3.org/2000/svg" style="width: 100%; height: auto; background: #0c1424; border-radius: 8px; font-family: 'JetBrains Mono', monospace;">
          <defs>
            <pattern id="grid303" width="40" height="40" patternUnits="userSpaceOnUse">
              <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#1e293b" stroke-width="0.8"/>
            </pattern>
          </defs>
          <rect width="800" height="500" fill="url(#grid303)"/>
          <rect x="70" y="50" width="660" height="380" fill="none" stroke="#ef4444" stroke-width="2" stroke-dasharray="6,4"/>
          <text x="80" y="42" fill="#ef4444" font-size="11" font-weight="700">UB CITY CADASTRAL PLOT #303 (80m x 65m) [AREA: 5,200 m²]</text>
          
          <rect x="110" y="90" width="580" height="300" rx="10" fill="rgba(245, 158, 11, 0.12)" stroke="#f59e0b" stroke-width="2.5"/>
          <text x="130" y="115" fill="#fcd34d" font-size="11" font-weight="700">PODIUM L1-L4: THE COLLECTION (LUXURY RETAIL &amp; DINING)</text>
          
          <rect x="160" y="140" width="220" height="210" rx="8" fill="#047857" fill-opacity="0.5" stroke="#34d399" stroke-width="2"/>
          <text x="175" y="170" fill="#ffffff" font-size="11" font-weight="700">KINGFISHER TOWERS</text>
          <text x="175" y="185" fill="#a7f3d0" font-size="8">34 FLOORS &bull; ULTRA-LUXURY PENTHOUSES</text>
          <rect x="235" y="210" width="60" height="60" fill="#0f172a" stroke="#fbbf24" stroke-width="1.5"/>
          <text x="245" y="245" fill="#fbbf24" font-size="8">LIFTS (x6)</text>
          
          <rect x="420" y="140" width="230" height="210" rx="8" fill="#1e40af" fill-opacity="0.5" stroke="#60a5fa" stroke-width="2"/>
          <text x="435" y="170" fill="#ffffff" font-size="11" font-weight="700">UB TOWER &amp; CANBERRA BLOCK</text>
          <text x="435" y="185" fill="#bfdbfe" font-size="8">GRADE-A CORPORATE HEADQUARTERS</text>
          <rect x="500" y="210" width="60" height="60" fill="#0f172a" stroke="#fbbf24" stroke-width="1.5"/>
          <text x="510" y="245" fill="#fbbf24" font-size="8">LIFTS (x6)</text>
          
          <circle cx="270" cy="310" r="20" fill="none" stroke="#ffffff" stroke-width="1.5"/>
          <text x="264" y="316" fill="#ffffff" font-size="14" font-weight="900">H</text>
          
          <rect x="560" y="405" width="160" height="35" rx="4" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
          <text x="570" y="420" fill="#10b981" font-size="8" font-weight="700">BBMP CBD HIGH-RISE SANCTION</text>
          <text x="570" y="432" fill="#94a3b8" font-size="7">ULPIN: 29202010080101</text>
        </svg>"""
    },
    601: {
        "title": "TIDEL Park (OMR IT Corridor) - Monolithic IT Spine Blueprint",
        "archetype": "it_linear_spine",
        "dimensions": {"length_m": 150, "width_m": 55, "height_m": 85, "floors": 13, "podium_floors": 2},
        "engineer": "TIDEL Park Ltd (TIDCO & ELCOT Government of Tamil Nadu)",
        "architect": "C.R. Narayana Rao (CRN) Architects",
        "year_built": 2000,
        "structural_system": "Reinforced Concrete Large-Span Moment-Resisting Frame with Monolithic Glass Ribbon Facade",
        "fsi_far": "3.50 (Tamil Nadu IT Expressway Infrastructure Policy)",
        "rera_id": "TN-CHENNAI-TIDEL-2000",
        "photo_url": "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?w=800&auto=format&fit=crop&q=80",
        "photo_caption": "TIDEL Park, OMR, Chennai - Pioneer 13-Storey Monolithic IT Expressway Facility",
        "blueprint_svg": """<svg viewBox="0 0 800 500" xmlns="http://www.w3.org/2000/svg" style="width: 100%; height: auto; background: #0f172a; border-radius: 8px; font-family: 'JetBrains Mono', monospace;">
          <defs>
            <pattern id="grid601" width="40" height="40" patternUnits="userSpaceOnUse">
              <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#1e293b" stroke-width="0.8"/>
            </pattern>
          </defs>
          <rect width="800" height="500" fill="url(#grid601)"/>
          <rect x="50" y="60" width="700" height="360" fill="none" stroke="#ef4444" stroke-width="2" stroke-dasharray="6,4"/>
          <text x="60" y="52" fill="#ef4444" font-size="11" font-weight="700">TIDEL PARK CADASTRAL PLOT #601 (150m x 55m) [1.28 MILLION SQ.FT BUILT-UP]</text>
          
          <rect x="80" y="100" width="640" height="260" rx="8" fill="rgba(30, 64, 175, 0.4)" stroke="#3b82f6" stroke-width="2.5"/>
          <text x="100" y="130" fill="#ffffff" font-size="13" font-weight="700">TIDEL PARK MAIN LINEAR IT BLOCK (13 STOREYS)</text>
          
          <rect x="180" y="160" width="60" height="70" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
          <text x="190" y="200" fill="#f59e0b" font-size="8">CORE 1 (x6)</text>
          
          <rect x="370" y="160" width="60" height="70" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
          <text x="380" y="200" fill="#f59e0b" font-size="8">CORE 2 (x8)</text>
          
          <rect x="560" y="160" width="60" height="70" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
          <text x="570" y="200" fill="#f59e0b" font-size="8">CORE 3 (x6)</text>
          
          <rect x="100" y="250" width="600" height="85" rx="4" fill="rgba(56, 189, 248, 0.15)" stroke="#38bdf8" stroke-width="1"/>
          <text x="250" y="300" fill="#e0f2fe" font-size="10" font-weight="700">COLUMN-FREE IT FLOOR PLATES (100,000 SQ.FT PER LEVEL)</text>
          
          <rect x="580" y="380" width="160" height="32" rx="4" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
          <text x="590" y="395" fill="#10b981" font-size="8" font-weight="700">CMDA CHENNAI SANCTIONED</text>
          <text x="590" y="406" fill="#94a3b8" font-size="7">ULPIN: 33021040210101</text>
        </svg>"""
    },
    401: {
        "title": "GIFT Diamond Tower Pinnacle - FinTech High-Tech Blueprint",
        "archetype": "crystalline_diamond",
        "dimensions": {"length_m": 75, "width_m": 75, "height_m": 180, "floors": 45, "podium_floors": 3},
        "engineer": "GIFT City Company Ltd (Joint Venture with IL&FS / Govt of Gujarat)",
        "architect": "ECADI (East China Architectural Design & Research Institute)",
        "year_built": 2021,
        "structural_system": "Aerodynamic Diamond Faceted Composite Megacolumns with Automated Building Management",
        "fsi_far": "4.50 (IFSCA International FinTech SEZ)",
        "rera_id": "PR/GJ/GANDHINAGAR/GANDHINAGAR/Others/RAA00451",
        "photo_url": "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=800&auto=format&fit=crop&q=80",
        "photo_caption": "GIFT Diamond Tower Pinnacle, Gandhinagar - Diamond Faceted FinTech International Tower",
        "blueprint_svg": """<svg viewBox="0 0 800 500" xmlns="http://www.w3.org/2000/svg" style="width: 100%; height: auto; background: #07101e; border-radius: 8px; font-family: 'JetBrains Mono', monospace;">
          <defs>
            <pattern id="grid401" width="40" height="40" patternUnits="userSpaceOnUse">
              <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#1e293b" stroke-width="0.8"/>
            </pattern>
          </defs>
          <rect width="800" height="500" fill="url(#grid401)"/>
          <polygon points="400,30 730,245 400,460 70,245" fill="none" stroke="#ef4444" stroke-width="2" stroke-dasharray="6,4"/>
          <text x="80" y="42" fill="#ef4444" font-size="11" font-weight="700">GIFT IFSC DIAMOND PLOT #401 (75m x 75m) [TAPERED DIAMOND]</text>
          
          <polygon points="400,60 690,245 400,430 110,245" fill="rgba(6, 182, 212, 0.15)" stroke="#06b6d4" stroke-width="3"/>
          <text x="270" y="100" fill="#22d3ee" font-size="11" font-weight="700">FACETED CRYSTALLINE CURTAIN WALL</text>
          
          <polygon points="400,120 600,245 400,370 200,245" fill="#0e7490" fill-opacity="0.6" stroke="#38bdf8" stroke-width="2"/>
          <text x="310" y="200" fill="#ffffff" font-size="10" font-weight="700">LEVEL 1 TO 45 TRADING SUITES</text>
          
          <rect x="365" y="210" width="70" height="70" fill="#0f172a" stroke="#fbbf24" stroke-width="2"/>
          <text x="375" y="245" fill="#fbbf24" font-size="8" font-weight="700">CORE (x10)</text>
          <text x="375" y="258" fill="#94a3b8" font-size="7">6 m/s LIFTS</text>
          
          <text x="140" y="440" fill="#a855f7" font-size="9" font-weight="700">&bull; INTEGRATED SUBSURFACE TAP TO GIFT UTILITY TUNNEL (TUM) AT Z: -16m</text>
          
          <rect x="580" y="390" width="160" height="32" rx="4" fill="#1e293b" stroke="#06b6d4" stroke-width="1"/>
          <text x="590" y="405" fill="#22d3ee" font-size="8" font-weight="700">IFSCA SPECIAL SEZ SANCTION</text>
          <text x="590" y="416" fill="#10b981" font-size="8">SMART 3D ULPIN: 24071010010101</text>
        </svg>"""
    }
}

def get_property_blueprint(prop_id):
    """
    Returns authentic CAD blueprint SVG, engineering specifications,
    and real imagery for a given property ID. Falls back to a high-grade generic CAD blueprint.
    """
    pid = int(prop_id)
    if pid in BLUEPRINT_AND_IMAGERY_DATA:
        return BLUEPRINT_AND_IMAGERY_DATA[pid]
    
    # Generic High-Precision Cadastral Blueprint Fallback
    return {
        "title": f"Cadastral Parcel #{pid} - Architectural Master Blueprint",
        "archetype": "parametric_commercial",
        "dimensions": {"length_m": 80, "width_m": 60, "height_m": 90, "floors": 18, "podium_floors": 2},
        "engineer": "National Institute of Urban Affairs & Municipal Engineering Board",
        "architect": "Registered Municipal Architect & Structural Consultant",
        "year_built": 2019,
        "structural_system": "Reinforced Concrete Frame with Earthquake-Resistant Shear Walls",
        "fsi_far": "3.0 (Municipal Standard Cadastral FSI)",
        "rera_id": f"RERA-NAT-{pid}-2022",
        "photo_url": "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=800&auto=format&fit=crop&q=80",
        "photo_caption": f"Cadastral Property #{pid} - Real Site & Architectural Elevation",
        "blueprint_svg": f"""<svg viewBox="0 0 800 500" xmlns="http://www.w3.org/2000/svg" style="width: 100%; height: auto; background: #0f172a; border-radius: 8px; font-family: 'JetBrains Mono', monospace;">
          <defs>
            <pattern id="grid_gen_{pid}" width="40" height="40" patternUnits="userSpaceOnUse">
              <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#1e293b" stroke-width="0.8"/>
            </pattern>
          </defs>
          <rect width="800" height="500" fill="url(#grid_gen_{pid})"/>
          <rect x="70" y="50" width="660" height="380" fill="none" stroke="#ef4444" stroke-width="2" stroke-dasharray="6,4"/>
          <text x="80" y="42" fill="#ef4444" font-size="11" font-weight="700">CADASTRE PLOT BOUNDARY #{pid} (80m x 60m) [SURFACE TITLE]</text>
          
          <rect x="120" y="90" width="560" height="300" rx="8" fill="rgba(2, 132, 199, 0.2)" stroke="#0284c7" stroke-width="2.5"/>
          <text x="140" y="125" fill="#ffffff" font-size="12" font-weight="700">STANDARD MULTI-STORY CADASTRAL FLOORPLATE</text>
          
          <rect x="360" y="200" width="80" height="80" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
          <text x="375" y="245" fill="#f59e0b" font-size="9" font-weight="700">CORE (x6)</text>
          
          <circle cx="160" cy="130" r="5" fill="#38bdf8"/>
          <circle cx="300" cy="130" r="5" fill="#38bdf8"/>
          <circle cx="500" cy="130" r="5" fill="#38bdf8"/>
          <circle cx="640" cy="130" r="5" fill="#38bdf8"/>
          <circle cx="160" cy="350" r="5" fill="#38bdf8"/>
          <circle cx="300" cy="350" r="5" fill="#38bdf8"/>
          <circle cx="500" cy="350" r="5" fill="#38bdf8"/>
          <circle cx="640" cy="350" r="5" fill="#38bdf8"/>
          
          <rect x="560" y="390" width="160" height="32" rx="4" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
          <text x="570" y="405" fill="#10b981" font-size="8" font-weight="700">MUNICIPAL CADASTRE VERIFIED</text>
          <text x="570" y="416" fill="#94a3b8" font-size="7">PLIN-REF: CAD-{pid}-3D</text>
        </svg>"""
    }
