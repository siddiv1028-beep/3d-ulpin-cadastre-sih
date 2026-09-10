"""
Automated Verification Suite for Merged 3D Cadastre & AI Slicing Features in 3D-ULPIN-Cadastre-SIH.
"""

import unittest
from core.ai_floor_segmentation import segment_building_floors, detect_slab_peaks, compute_z_histogram
from core.topology_3d import validate_cadastral_topology, calculate_aabb_intersection_volume, check_parent_containment
from core.ulpin_enhanced import generate_enhanced_3d_ulpin, decode_enhanced_3d_ulpin, calculate_checksum_mod36, verify_checksum_mod36
from data.mock_lidar import generate_synthetic_building_lidar

class TestMergedCadastreFeatures(unittest.TestCase):

    def test_enhanced_3d_ulpin_checksum(self):
        ulpin, chk = generate_enhanced_3d_ulpin("MH27", "27211010500101", "BLD", "F04", "A402")
        self.assertTrue(ulpin.startswith("MH27-27211010500101-BLD-F04-A402-"))
        self.assertEqual(len(chk), 1)
        
        # Test decoding
        dec = decode_enhanced_3d_ulpin(ulpin)
        self.assertTrue(dec["is_valid"])
        self.assertTrue(dec["checksum_valid"])
        self.assertEqual(dec["stratum_code"], "BLD")

    def test_ai_floor_segmentation_pipeline(self):
        pts = generate_synthetic_building_lidar(ground_z=0.0, num_floors=5, storey_height=3.2, num_basements=1)
        res = segment_building_floors(pts, ground_elevation_msl=0.0)
        self.assertEqual(res["status"], "SUCCESS")
        self.assertGreaterEqual(res["total_floors_detected"], 5)
        codes = [f["level_code"] for f in res["floors"]]
        self.assertIn("G00", codes)

    def test_3d_topology_clash_detection(self):
        parcels = [
            {
                "spatial_unit_id": "U1",
                "unit_designation": "Flat 101",
                "stratum_type": "BLD",
                "elevation_min_m": 0, "elevation_max_m": 3.5,
                "bbox": {"min_x": 0, "min_y": 0, "min_z": 0, "max_x": 10, "max_y": 10, "max_z": 3.5},
                "footprint_polygon": [[0,0],[10,0],[10,10],[0,10]]
            },
            {
                "spatial_unit_id": "U2",
                "unit_designation": "Flat 102 (Clashing)",
                "stratum_type": "BLD",
                "elevation_min_m": 0, "elevation_max_m": 3.5,
                "bbox": {"min_x": 8, "min_y": 0, "min_z": 0, "max_x": 18, "max_y": 10, "max_z": 3.5},
                "footprint_polygon": [[8,0],[18,0],[18,10],[8,10]]
            }
        ]
        audit = validate_cadastral_topology(parcels)
        self.assertEqual(audit["clashing_parcels_count"], 2)
        self.assertEqual(len(audit["clashes"]), 1)
        self.assertEqual(audit["clashes"][0]["type"], "VOLUMETRIC_UNIT_CLASH")
        # Overlap: dx=2, dy=10, dz=3.5 -> vol = 70.0 m³
        self.assertAlmostEqual(audit["clashes"][0]["overlap_volume_cum"], 70.0)

    def test_setback_violation(self):
        parent_boundary = [[0, 0], [20, 0], [20, 20], [0, 20]]
        violating_unit = [[15, 5], [25, 5], [25, 15], [15, 15]] # extends to x=25 beyond 20
        is_contained, ratio = check_parent_containment(violating_unit, parent_boundary)
        self.assertFalse(is_contained)
        self.assertGreater(ratio, 0.0)

if __name__ == "__main__":
    unittest.main()
