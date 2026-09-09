# Indian State Census / LGD Codes Mapping
STATE_LGD_MAP = {
    7: "Delhi",
    6: "Haryana",
    19: "West Bengal",
    24: "Gujarat",
    27: "Maharashtra",
    29: "Karnataka",
    33: "Tamil Nadu",
    36: "Telangana"
}

def generate_ulpin(state, dist, sub_dist, village, plot, floor=0):
    """
    Generates a 14-digit base ULPIN + a 3-character vertical/floor extension.
    Handles surface, elevated, and subsurface/underground parcels.
    Standard: SS-DD-SSS-VVV-PPPP-FFF
    """
    base_ulpin = f"{state:02d}{dist:02d}{sub_dist:03d}{village:03d}{plot:04d}"
    
    # Add a Z-axis identifier
    if floor > 0:
        floor_ext = f"{floor:03d}"       # e.g., 001 for Floor 1
    elif floor < 0:
        floor_ext = f"U{abs(floor):02d}" # e.g., U01 for Basement 1
    else:
        floor_ext = "000"                # Surface level
        
    return f"{base_ulpin}-{floor_ext}"


def decode_ulpin(ulpin_str):
    """
    Decodes a standard 14-digit or 18-character 3D ULPIN string into spatial components.
    Example: '27211010500101-004' or '27211010500101'
    """
    clean_str = ulpin_str.strip().replace(" ", "").upper()
    
    parts = clean_str.split("-")
    base_code = parts[0]
    floor_suffix = parts[1] if len(parts) > 1 else "000"
    
    if len(base_code) != 14 or not base_code.isdigit():
        return {
            "valid": False,
            "error": "Base ULPIN must be exactly 14 digits (Bhu-Aadhaar standard)."
        }
    
    state_code = int(base_code[0:2])
    dist_code = int(base_code[2:4])
    sub_dist_code = int(base_code[4:7])
    village_code = int(base_code[7:10])
    plot_id = int(base_code[10:14])
    
    # Parse floor / Z-dimension
    if floor_suffix.startswith("U"):
        try:
            floor_num = -int(floor_suffix[1:])
            floor_desc = f"Subsurface Level {abs(floor_num)} (Basement)"
            vertical_type = "Subsurface Parcel"
        except ValueError:
            floor_num = 0
            floor_desc = "Unknown Subsurface"
            vertical_type = "Subsurface"
    elif floor_suffix.isdigit():
        floor_num = int(floor_suffix)
        if floor_num == 0:
            floor_desc = "Ground / Surface Level (0m)"
            vertical_type = "Surface Parcel"
        else:
            floor_desc = f"Superstructure Floor {floor_num}"
            vertical_type = "Elevated Unit"
    else:
        floor_num = 0
        floor_desc = "Standard Level"
        vertical_type = "Standard"

    state_name = STATE_LGD_MAP.get(state_code, f"State Code {state_code}")

    return {
        "valid": True,
        "raw_ulpin": clean_str,
        "base_ulpin": base_code,
        "floor_suffix": floor_suffix,
        "state_code": state_code,
        "state_name": state_name,
        "dist_code": dist_code,
        "sub_dist_code": sub_dist_code,
        "village_code": village_code,
        "plot_id": plot_id,
        "floor_number": floor_num,
        "floor_description": floor_desc,
        "vertical_type": vertical_type
    }