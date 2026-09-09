# 🏙️ Bhu-Aadhaar 3D: Pan-India 3D Cadastral System
### ISO 19152 Compliant Next-Generation 3D Spatial Cadastre, Subsurface Collision Engine & Vertical Land Registry Portal

**Author / Lead:** Parijat Sharma  
**Event:** Smart India Hackathon 2026 (SIH 2026)  
**Tech Stack:** Python, Streamlit, PyDeck (Deck.gl), SQLite, ReportLab

---

## 📌 1. Executive Summary & Problem Statement[cite: 3]
Modern Indian urban centers (e.g., Mumbai MMR, Delhi NCR, Bengaluru, GIFT City) have evolved rapidly into dense, vertically stacked superstructures featuring multi-level subterranean basements, underground metro lines, and dense utility corridors[cite: 3]. However, existing land administration systems across India (under DILRMP and Bhu-Naksha) remain fundamentally two-dimensional (2D), treating land parcels purely as flat polygons (Latitude, Longitude)[cite: 3]. 

This creates severe architectural mismatches and systemic risks:
* **Airspace & Floor Ownership Ambiguity:** In a 40-storey high-rise, dozens of distinct owners share the exact same 2D footprint, which traditional cadastres cannot legally demarcate[cite: 3].
* **Catastrophic Subsurface Encroachments:** Deep private foundations and underground parking lots often collide with or breach the safety buffers of underground metro tunnels, gas conduits, water mains, and optic fiber networks[cite: 3].
* **Title Disputes & Double Mortgaging:** The absence of a unique, immutable vertical parcel identifier allows fraudulent sales or overlapping conveyance of individual floor units[cite: 3].

**The Solution:** Bhu-Aadhaar 3D provides an ISO 19152 compliant 3D cadastral platform featuring real-time volumetric floor slicing, automated 3D subsurface collision detection, a 14-digit + vertical ULPIN standard, cryptographic title certificate issuance with QR verification, and role-based workflows[cite: 3].

---

## 🏗️ 2. System Architecture & End-to-End Pipeline[cite: 3]
The project is structured around a modular, decoupled architecture consisting of core mathematical engines, a relational spatial SQLite database, an interactive Deck.gl GIS visualization layer, and role-based operational modules[cite: 3]:

| Component | Module Path | Primary Responsibility & Algorithms |
| :--- | :--- | :--- |
| **Spatial Math Engine** | `core/spatial_math.py` | Segments total height and base elevation into discrete volumetric floor blocks for both superstructures and negative subterranean basements[cite: 3]. |
| **3D ULPIN Engine** | `core/ulpin_logic.py` | Generates 14-digit LGD-compliant base ULPIN + 3-char vertical suffix (e.g., `-004` for floor 4, `-U02` for basement 2) with instant bidirectional parsing[cite: 3]. |
| **Collision & Clash Engine** | `core/collision_engine.py` | Performs Haversine surface proximity calculation and 1D vertical overlap checks to identify critical collisions and buffer violations[cite: 3]. |
| **Digital Certificate Engine** | `core/certificate_generator.py` | Computes immutable SHA-256 title hashes, generates QR code payloads, and builds downloadable official PDF certificates[cite: 3]. |
| **PyDeck 3D Map Studio** | `frontend/map_engine.py` | Renders 3D extruded `ColumnLayer` columns and ground `ScatterplotLayer` footprints with theme-adaptive basemaps[cite: 3]. |
| **UI Components & Theming** | `frontend/ui_components.py` | Injects modern glassmorphic styling, Light/Dark mode switcher, KPI metrics rows, and dossier cards[cite: 3]. |
| **Database Storage** | `database/spatial_records.db` | Relational SQLite storage for property IDs, LGD geography, 3D coordinates, zones, owners, and valuations[cite: 3]. |

---

## 🧮 3. Deep Dive: Mathematical & Algorithmic Engines[cite: 3]

### 3.1 Volumetric 3D Parcel Slicing (`core/spatial_math.py`)[cite: 3]
Standard land surveys record flat physical footprints[cite: 3]. Our spatial segmentation algorithm accepts building base elevation ($Z_{base}$), total height ($H$), and floor height ($h = 3\text{m}$ default) to generate precise 3D vertical intervals[cite: 3]:
* **Superstructure (Above Ground, $Z_{base} \ge 0$):** For floor index $f \in [0, N-1]$, the interval is $[Z_{base} + f \cdot h, \; Z_{base} + (f+1) \cdot h]$[cite: 3]. The floor number is designated as $f+1$[cite: 3].
* **Subsurface (Basements, $Z_{base} < 0$):** Extends downwards below the surface datum $[-(f \cdot h), \; -((f+1) \cdot h)]$[cite: 3]. The floor number is recorded as $-(f+1)$ to denote subterranean depth[cite: 3].

### 3.2 14-Digit Bhu-Aadhaar + 3D Vertical ULPIN Standard (`core/ulpin_logic.py`)[cite: 3]
India's Ministry of Rural Development specifies a 14-digit Unique Land Parcel Identification Number (ULPIN) derived from Local Government Directory (LGD) codes: `SS-DD-SSS-VVV-PPPP` (State, District, Sub-District, Village/Ward, Plot ID)[cite: 3].
* **3D ISO 19152 Cadastral Extension:** We append a hyphenated 3-character vertical suffix: `-FFF` for above-ground floors (e.g., `-004` for Level 4) and `-UXX` for underground basements (e.g., `-U02` for Basement 2)[cite: 3]. 
* **Bidirectional Decoder:** Instantly unpacks raw ULPIN inputs, validates length/integrity, extracts geographic jurisdiction, and flies the camera directly to the parcel[cite: 3].

### 3.3 Subsurface 3D Clash & Encroachment Detection (`core/collision_engine.py`)[cite: 3]
To prevent catastrophic strikes between deep foundations and municipal utility corridors, the engine computes geodesic proximity and vertical intersection[cite: 3]:
* **Horizontal Ground Distance:** Uses the Haversine equation over Earth radius $R = 6,371,000\text{m}$[cite: 3]:
  $$a = \sin^2\left(\frac{\Delta \phi}{2}\right) + \cos(\phi_1)\cos(\phi_2)\sin^2\left(\frac{\Delta \lambda}{2}\right), \quad D = 2R \cdot \arctan2\left(\sqrt{a}, \sqrt{1-a}\right)$$[cite: 3]
* **Vertical Interval Overlap ($\Delta Z$):**
  $$\Delta Z = \min(Z_{top1}, Z_{top2}) - \max(Z_{base1}, Z_{base2})$$[cite: 3]
* **Severity Classification:** If $D \le 2 \times R_{footprint}$ and $\Delta Z > 0$, it is flagged as a **CRITICAL COLLISION** (Direct 3D Encroachment)[cite: 3]. If $D \le 2 \times R_{footprint} + S_{buffer}$ and $\Delta Z > -10\text{m}$, it is flagged as a **SAFETY BUFFER VIOLATION**[cite: 3].

### 3.4 Cryptographic SHA-256 Title Certificate & QR Engine (`core/certificate_generator.py`)[cite: 3]
Generates an immutable cryptographic fingerprint sealing the vertical airspace parcel: `SHA-256 (ULPIN | Owner | Lat | Lon | Z_Range | Valuation)`[cite: 3]. This generates a scannable JSON QR payload that any citizen or bank official can scan with a standard smartphone camera to verify title legitimacy on-site[cite: 3].

---

## 👥 4. Role-Based Operational Workflows[cite: 3]
The platform provides tailored operational personas with 1-click switching to address diverse stakeholders[cite: 3]:

* **🏠 Citizen / Homebuyer Mode:** Designed for citizens, flat buyers, and banks[cite: 3]. Features instant title verification, RERA status checks, unit/floor level dropdowns with height bounds, live 3D Bhu-Aadhaar certificate card previews, and 1-click official PDF title certificate downloads[cite: 3].
* **📐 Government GIS Surveyor Mode:** Designed for municipal engineers, GIS officers, and urban planners[cite: 3]. Computes 3D spatial metrics (Gross Volume $\text{m}^3$, Built-up area $\text{m}^2$, FSI/FAR), runs automated subsurface 3D clash audits, renders vertical architectural cross-section stacks, and handles 3D parcel coordinate ingestion into SQLite[cite: 3].
* **🏛️ Sub-Registrar Mode:** Designed for revenue officers, land registrars, and legal authorities[cite: 3]. Simulates individual vertical airspace deed registrations, calculates 6% state stamp duty based on cadastral value, records immutable ownership conveyance in SQLite, and logs audit trails for pan-India transactions[cite: 3].

---

## 🚀 5. Getting Started & Installation[cite: 3]

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/3d-ulpin-cadastre-sih.git](https://github.com/YOUR_USERNAME/3d-ulpin-cadastre-sih.git)
   cd 3d-ulpin-cadastre-sih


1. Install Dependencies:  
   pip install -r requirements.txt
2. Initialize the Spatial Database:
   python database/db_setup.py
4. Launch the Streamlit Application:
   streamlit run main.py
