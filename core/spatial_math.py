def segment_building(total_height, base_elevation=0, floor_height=3):
    """
    Slices a property into individual floors/parcels, handling both 
    above-ground and underground properties.
    """
    num_floors = int(total_height // floor_height)
    floors = []
    
    for f in range(num_floors):
        if base_elevation < 0:
            # For underground, we count downwards from 0 (Basement 1, Basement 2...)
            z_start = - (f * floor_height)
            z_end = - ((f + 1) * floor_height)
            floors.append({
                'floor_number': -(f + 1),  # Negative signifies underground
                'z_start': z_start,
                'z_end': z_end
            })
        else:
            # Above ground
            z_start = base_elevation + (f * floor_height)
            z_end = base_elevation + ((f + 1) * floor_height)
            floors.append({
                'floor_number': f + 1,
                'z_start': z_start,
                'z_end': z_end
            })
            
    return floors