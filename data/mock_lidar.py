"""
Mock Drone LiDAR & Point Cloud Synthesizer for AI Floor Slicing.
"""

import random
from typing import List

def generate_synthetic_building_lidar(
    ground_z: float = 0.0,
    num_floors: int = 8,
    storey_height: float = 3.2,
    num_basements: int = 2,
    basement_height: float = 3.0,
    slab_thickness: float = 0.25,
    points_per_slab: int = 400,
    points_per_wall: int = 180,
    noise_std: float = 0.04
) -> List[float]:
    """Synthesizes Z elevation values of a scanned multi-storey building."""
    z_points = []
    
    # Ground terrain
    for _ in range(700):
        z_points.append(random.gauss(ground_z, 0.08))
        
    # Underground basements
    for b in range(num_basements, 0, -1):
        slab_z = ground_z - (b * basement_height)
        for _ in range(int(points_per_slab * 0.7)):
            z_points.append(random.gauss(slab_z, noise_std))
        for _ in range(points_per_wall // 2):
            z_points.append(random.uniform(slab_z, slab_z + basement_height))
            
    # Superstructure floors
    for f in range(num_floors + 1):
        slab_z = ground_z + (f * storey_height)
        for _ in range(points_per_slab):
            z_points.append(random.gauss(slab_z, noise_std))
        if f < num_floors:
            for _ in range(points_per_wall):
                z_points.append(random.uniform(slab_z + slab_thickness, slab_z + storey_height - slab_thickness))
                
    # Rooftop parapet
    roof_z = ground_z + ((num_floors + 1) * storey_height)
    for _ in range(points_per_slab // 2):
        z_points.append(random.gauss(roof_z, noise_std))
        
    return z_points
