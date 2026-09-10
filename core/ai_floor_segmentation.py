"""
AI/ML Module: Point Cloud Vertical Profiling & Automated Floor Segmentation.
Uses vertical point density histograms and signal peak detection to detect floor slabs
and calculate exact vertical storey bounds from drone photogrammetry and LiDAR point clouds.
"""

from typing import List, Dict, Any, Tuple
import math

def compute_z_histogram(
    points_z: List[float],
    bin_size: float = 0.1,
    min_z: float = None,
    max_z: float = None
) -> Tuple[List[float], List[int]]:
    """
    Computes vertical elevation histogram from 3D point cloud Z coordinates.
    Returns bin centers and point frequencies.
    """
    if not points_z:
        return [], []
        
    z_min = min(points_z) if min_z is None else min_z
    z_max = max(points_z) if max_z is None else max_z
    
    num_bins = max(1, int(math.ceil((z_max - z_min) / bin_size)))
    bins = [0] * num_bins
    bin_centers = [round(z_min + (i + 0.5) * bin_size, 3) for i in range(num_bins)]
    
    for z in points_z:
        if z_min <= z <= z_max:
            idx = min(num_bins - 1, max(0, int((z - z_min) / bin_size)))
            bins[idx] += 1
            
    return bin_centers, bins

def smooth_signal(signal: List[int], window_size: int = 5) -> List[float]:
    """Applies moving average filter to smooth point cloud noise."""
    if len(signal) < window_size:
        return [float(x) for x in signal]
        
    smoothed = []
    half = window_size // 2
    for i in range(len(signal)):
        start = max(0, i - half)
        end = min(len(signal), i + half + 1)
        sub = signal[start:end]
        smoothed.append(sum(sub) / len(sub))
    return smoothed

def detect_slab_peaks(
    bin_centers: List[float],
    frequencies: List[float],
    min_floor_height: float = 2.6,
    prominence_ratio: float = 0.25
) -> List[Dict[str, Any]]:
    """
    Detects structural floor slabs via local maxima in the vertical density profile.
    Slabs exhibit high point density due to horizontal ceiling/floor reflectances.
    """
    if not frequencies or len(frequencies) < 3:
        return []
        
    max_freq = max(frequencies)
    threshold = max_freq * prominence_ratio
    peaks = []
    
    for i in range(1, len(frequencies) - 1):
        if frequencies[i] > threshold:
            if frequencies[i] >= frequencies[i - 1] and frequencies[i] >= frequencies[i + 1]:
                z_val = bin_centers[i]
                # Enforce minimum floor-to-floor height separation
                if not peaks or (z_val - peaks[-1]["z_elevation"]) >= min_floor_height:
                    peaks.append({
                        "index": len(peaks),
                        "z_elevation": round(z_val, 2),
                        "density_score": round(frequencies[i], 1)
                    })
                    
    return peaks

def segment_building_floors(
    lidar_points_z: List[float],
    ground_elevation_msl: float = 0.0,
    bin_size: float = 0.1
) -> Dict[str, Any]:
    """
    End-to-end automated floor segmentation pipeline.
    Identifies basement levels, ground floor, residential/commercial storeys, and rooftop terrace.
    """
    bin_centers, raw_freq = compute_z_histogram(lidar_points_z, bin_size=bin_size)
    smoothed_freq = smooth_signal(raw_freq, window_size=5)
    detected_peaks = detect_slab_peaks(bin_centers, smoothed_freq, min_floor_height=2.7)
    
    # Structure detected slabs into formal vertical cadastre floor units
    floors = []
    for i in range(len(detected_peaks) - 1):
        slab_bottom = detected_peaks[i]["z_elevation"]
        slab_top = detected_peaks[i + 1]["z_elevation"]
        mid_z = (slab_bottom + slab_top) / 2.0
        
        # Determine code based on relationship to ground
        if slab_top <= ground_elevation_msl + 0.5:
            # Subsurface basement
            b_idx = max(1, int(round((ground_elevation_msl - mid_z) / 3.0)))
            level_code = f"B{b_idx:02d}"
            level_type = "Subterranean Basement"
            stratum = "SUB"
        elif slab_bottom <= ground_elevation_msl + 0.5:
            level_code = "G00"
            level_type = "Ground / Stilt Level"
            stratum = "BLD"
        else:
            f_idx = int(round((slab_bottom - ground_elevation_msl) / 3.2)) + 1
            level_code = f"F{f_idx:02d}"
            level_type = f"Storey Floor {f_idx}"
            stratum = "BLD"
            
        floors.append({
            "floor_id": f"FL_{level_code}",
            "level_code": level_code,
            "level_type": level_type,
            "stratum": stratum,
            "elevation_min_m": slab_bottom,
            "elevation_max_m": slab_top,
            "storey_height_m": round(slab_top - slab_bottom, 2),
            "slab_detection_confidence": round(min(0.99, detected_peaks[i]["density_score"] / 200.0), 3)
        })
        
    return {
        "status": "SUCCESS",
        "ground_elevation_msl": ground_elevation_msl,
        "total_floors_detected": len(floors),
        "detected_slabs_count": len(detected_peaks),
        "floors": floors,
        "histogram": {
            "bin_centers": bin_centers[::2],  # downsample for payload efficiency
            "frequencies": [round(f, 1) for f in smoothed_freq[::2]]
        }
    }
