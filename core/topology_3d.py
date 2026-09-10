"""
AI/ML Module: Volumetric 3D Parcel Delineation & Intelligent Cadastral Topology Validation.
Performs 3D intersection volume clash detection, parent setback boundary containment,
watertightness checks, and underground utility clearance verification.
"""

from typing import List, Dict, Any, Tuple
import math

def calculate_polygon_area_2d(coords: List[List[float]]) -> float:
    """Computes 2D planar polygon area via the Shoelace formula."""
    if len(coords) < 3:
        return 0.0
    n = len(coords)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += coords[i][0] * coords[j][1]
        area -= coords[j][0] * coords[i][1]
    return abs(area) / 2.0

def calculate_polygon_centroid_2d(coords: List[List[float]]) -> Tuple[float, float]:
    """Computes 2D centroid of polygon."""
    if len(coords) < 3:
        if coords:
            return coords[0][0], coords[0][1]
        return 0.0, 0.0
    n = len(coords)
    area = 0.0
    cx = 0.0
    cy = 0.0
    for i in range(n):
        j = (i + 1) % n
        factor = (coords[i][0] * coords[j][1] - coords[j][0] * coords[i][1])
        area += factor
        cx += (coords[i][0] + coords[j][0]) * factor
        cy += (coords[i][1] + coords[j][1]) * factor
    area *= 0.5
    if abs(area) < 1e-6:
        return coords[0][0], coords[0][1]
    cx /= (6.0 * area)
    cy /= (6.0 * area)
    return cx, cy

def delineate_volumetric_parcel(
    unit_id: str,
    footprint_coords: List[List[float]],
    z_min: float,
    z_max: float,
    stratum_type: str = "BLD"
) -> Dict[str, Any]:
    """
    Constructs a 3D volumetric spatial unit (prismatic polyhedral B-Rep).
    """
    area_2d = calculate_polygon_area_2d(footprint_coords)
    cx_2d, cy_2d = calculate_polygon_centroid_2d(footprint_coords)
    cz_3d = (z_min + z_max) / 2.0
    
    height = z_max - z_min
    volume_3d = area_2d * height
    
    xs = [pt[0] for pt in footprint_coords]
    ys = [pt[1] for pt in footprint_coords]
    
    bbox = {
        "min_x": min(xs) if xs else 0.0,
        "min_y": min(ys) if ys else 0.0,
        "min_z": z_min,
        "max_x": max(xs) if xs else 0.0,
        "max_y": max(ys) if ys else 0.0,
        "max_z": z_max
    }
    
    return {
        "unit_id": unit_id,
        "stratum_type": stratum_type,
        "centroid": {"x": round(cx_2d, 3), "y": round(cy_2d, 3), "z": round(cz_3d, 2)},
        "bbox": bbox,
        "elevation_min_m": round(z_min, 2),
        "elevation_max_m": round(z_max, 2),
        "height_m": round(height, 2),
        "gross_floor_area_sqm": round(area_2d, 2),
        "enclosed_volume_cum": round(volume_3d, 2),
        "footprint": footprint_coords
    }

def check_bbox_overlap_3d(b1: Dict[str, float], b2: Dict[str, float]) -> bool:
    """Fast axis-aligned bounding box (AABB) intersection test in 3D."""
    if b1["max_x"] < b2["min_x"] or b1["min_x"] > b2["max_x"]:
        return False
    if b1["max_y"] < b2["min_y"] or b1["min_y"] > b2["max_y"]:
        return False
    if b1["max_z"] < b2["min_z"] or b1["min_z"] > b2["max_z"]:
        return False
    return True

def calculate_aabb_intersection_volume(b1: Dict[str, float], b2: Dict[str, float]) -> float:
    """Computes the 3D intersection volume between two AABBs."""
    dx = max(0.0, min(b1["max_x"], b2["max_x"]) - max(b1["min_x"], b2["min_x"]))
    dy = max(0.0, min(b1["max_y"], b2["max_y"]) - max(b1["min_y"], b2["min_y"]))
    dz = max(0.0, min(b1["max_z"], b2["max_z"]) - max(b1["min_z"], b2["min_z"]))
    return dx * dy * dz

def is_point_inside_polygon(x: float, y: float, poly: List[List[float]]) -> bool:
    """Ray casting algorithm for 2D point-in-polygon containment."""
    inside = False
    n = len(poly)
    if n < 3:
        return False
    p1x, p1y = poly[0]
    for i in range(n + 1):
        p2x, p2y = poly[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside

def check_parent_containment(unit_footprint: List[List[float]], parent_parcel_boundary: List[List[float]]) -> Tuple[bool, float]:
    """
    Verifies that all vertices of the 3D unit's footprint lie inside the parent surface parcel boundary.
    Returns (is_contained, violation_ratio).
    """
    if not parent_parcel_boundary or not unit_footprint:
        return True, 0.0
        
    violations = 0
    total = len(unit_footprint)
    for pt in unit_footprint:
        if not is_point_inside_polygon(pt[0], pt[1], parent_parcel_boundary):
            violations += 1
            
    is_contained = (violations == 0)
    violation_ratio = round(violations / total, 3) if total > 0 else 0.0
    return is_contained, violation_ratio

def validate_cadastral_topology(
    parcels: List[Dict[str, Any]],
    parent_surface_boundary: List[List[float]] = None
) -> Dict[str, Any]:
    """
    Comprehensive 3D Topology Audit across all cadastral parcels:
    1. Volumetric clash detection between adjacent private units
    2. Encroachment of building units over surface parcel setback lines
    3. Collision / buffer infringement between underground utilities and foundations
    4. Watertightness and geometric degeneracy checks
    """
    clashes = []
    setback_violations = []
    clashing_ids = set()
    
    num_parcels = len(parcels)
    for i in range(num_parcels):
        p1 = parcels[i]
        b1 = p1.get("bbox")
        id1 = p1.get("ulpin_3d") or p1.get("spatial_unit_id")
        
        # Check watertightness
        if p1.get("elevation_max_m", 0) <= p1.get("elevation_min_m", 0):
            clashes.append({
                "type": "GEOMETRIC_DEGENERACY",
                "severity": "CRITICAL",
                "parcel_a": id1,
                "parcel_b": None,
                "description": f"Parcel {id1} has non-positive vertical thickness (Z_max <= Z_min)."
            })
            clashing_ids.add(id1)
            
        # Parent setback boundary containment check
        if parent_surface_boundary and p1.get("stratum_type") in ["BLD", "SUB", "AIR"]:
            footprint = p1.get("footprint_polygon", [])
            is_contained, ratio = check_parent_containment(footprint, parent_surface_boundary)
            if not is_contained:
                violation_record = {
                    "type": "SURFACE_SETBACK_ENCROACHMENT",
                    "severity": "HIGH",
                    "parcel_id": id1,
                    "unit_name": p1.get("unit_designation", id1),
                    "stratum": p1.get("stratum_type"),
                    "violation_ratio": ratio,
                    "description": f"Parcel {id1} extends outside legal surface parcel boundary by {ratio*100:.1f}%."
                }
                setback_violations.append(violation_record)
                clashing_ids.add(id1)

        # Pairwise clash checks
        for j in range(i + 1, num_parcels):
            p2 = parcels[j]
            b2 = p2.get("bbox")
            id2 = p2.get("ulpin_3d") or p2.get("spatial_unit_id")
            
            # Skip SUR vs BLD/SUB base test
            if (p1.get("stratum_type") == "SUR" and p2.get("stratum_type") != "SUR") or \
               (p2.get("stratum_type") == "SUR" and p1.get("stratum_type") != "SUR"):
                continue
                
            if b1 and b2 and check_bbox_overlap_3d(b1, b2):
                overlap_vol = calculate_aabb_intersection_volume(b1, b2)
                if overlap_vol > 0.25:
                    clash_type = "VOLUMETRIC_UNIT_CLASH"
                    severity = "CRITICAL"
                    
                    if p1.get("stratum_type") == "UTL" or p2.get("stratum_type") == "UTL":
                        clash_type = "UTILITY_EASEMENT_INFRINGEMENT"
                        severity = "HIGH"
                    elif p1.get("stratum_type") == "AIR" or p2.get("stratum_type") == "AIR":
                        clash_type = "AIR_RIGHTS_INTERFERENCE"
                        severity = "HIGH"
                        
                    clashes.append({
                        "type": clash_type,
                        "severity": severity,
                        "parcel_a": id1,
                        "parcel_b": id2,
                        "unit_a": p1.get("unit_designation", id1),
                        "unit_b": p2.get("unit_designation", id2),
                        "overlap_volume_cum": round(overlap_vol, 2),
                        "description": (
                            f"3D clash between {p1.get('unit_designation')} and {p2.get('unit_designation')} "
                            f"with {round(overlap_vol, 2)} m³ disputed volume."
                        )
                    })
                    clashing_ids.add(id1)
                    clashing_ids.add(id2)
                    
    total_audited = len(parcels)
    valid_count = total_audited - len(clashing_ids)
    
    return {
        "overall_status": "CONFLATED_ISSUES_FOUND" if (clashes or setback_violations) else "VERIFIED_WATERTIGHT",
        "total_parcels_audited": total_audited,
        "valid_parcels_count": valid_count,
        "clashing_parcels_count": len(clashing_ids),
        "clashes": clashes,
        "setback_violations": setback_violations,
        "clashing_ids": list(clashing_ids)
    }
