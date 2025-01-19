def convert_depth_to_distance(depth_value, depth_scale):
    # Convert depth value to distance in meters
    distance = depth_value * depth_scale
    return distance

def convert_distance_to_feet(distance_value):
    # Convert distance value from meters to feet
    distance_feet = distance_value * 3.28084
    return distance_feet
