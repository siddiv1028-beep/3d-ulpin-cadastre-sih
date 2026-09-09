import math
import pandas as pd

def calculate_ground_distance(lat1, lon1, lat2, lon2):
    """
    Computes accurate surface distance in meters between two coordinates 
    using the Haversine formula.
    """
    R = 6371000.0  # Earth's radius in meters
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = (math.sin(delta_phi / 2.0) ** 2 +
         math.cos(phi1) * math.cos(phi2) * (math.sin(delta_lambda / 2.0) ** 2))
    c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))
    return R * c

def check_parcel_conflicts(target_prop, all_props_df, default_radius=35.0, safety_buffer=20.0):
    """
    Performs volumetric 3D intersection and proximity buffer analysis 
    between a target parcel and surrounding urban infrastructure.
    """
    target_id = target_prop['property_id']
    t_lat = target_prop['lat']
    t_lon = target_prop['lon']
    t_z_min = float(target_prop['base_elevation'])
    t_z_max = t_z_min + float(target_prop['total_height'])

    conflicts = []

    for _, other in all_props_df.iterrows():
        if other['property_id'] == target_id:
            continue

        # Proximity check
        dist = calculate_ground_distance(t_lat, t_lon, other['lat'], other['lon'])
        
        # We only check parcels within 500m of interest
        if dist > 500.0:
            continue

        o_z_min = float(other['base_elevation'])
        o_z_max = o_z_min + float(other['total_height'])

        # Calculate vertical overlap
        overlap_z = min(t_z_max, o_z_max) - max(t_z_min, o_z_min)
        has_z_overlap = overlap_z > 0

        # Physical footprint thresholds
        footprint_combined = default_radius * 2
        buffer_threshold = footprint_combined + safety_buffer

        if dist <= footprint_combined and has_z_overlap:
            severity = "CRITICAL_COLLISION"
            badge = "🔴 Direct 3D Encroachment"
            desc = (f"Direct volumetric intersection! Parcel #{target_id} and #{other['property_id']} "
                    f"physically overlap by {overlap_z:.1f}m vertically.")
        elif dist <= buffer_threshold and (has_z_overlap or abs(overlap_z) < 10.0):
            severity = "BUFFER_VIOLATION"
            badge = "🟡 Safety Buffer Violation"
            desc = (f"Separation distance is only {dist:.1f}m (Required: >{buffer_threshold:.1f}m). "
                    f"Structural or vibration monitoring required.")
        else:
            continue

        conflicts.append({
            "target_id": target_id,
            "target_name": target_prop['name'],
            "conflicting_id": other['property_id'],
            "conflicting_name": other['name'],
            "conflicting_type": other['type'],
            "conflicting_owner": other['owner'],
            "distance_m": round(dist, 1),
            "overlap_z_m": round(max(0, overlap_z), 1),
            "severity": severity,
            "badge": badge,
            "description": desc
        })

    return conflicts

def run_national_audit(df, safety_buffer=20.0):
    """
    Audits the entire national database for subterranean & vertical boundary conflicts.
    """
    all_conflicts = []
    seen_pairs = set()

    for idx, prop in df.iterrows():
        conflicts = check_parcel_conflicts(prop, df, safety_buffer=safety_buffer)
        for c in conflicts:
            pair = tuple(sorted([c['target_id'], c['conflicting_id']]))
            if pair not in seen_pairs:
                seen_pairs.add(pair)
                all_conflicts.append(c)

    return all_conflicts
