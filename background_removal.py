import cv2
import numpy as np

def perform_background_removal(color_frame, aligned_depth_frame, depth_image_bg, depth_scale, clipping_distance):
    depth_image = np.asanyarray(aligned_depth_frame.get_data())
    depth_image_3d = np.dstack((depth_image, depth_image, depth_image))
    clipping_distance_in_pixels = clipping_distance * depth_scale

    # Perform background removal based on depth differences
    depth_diff = np.abs(depth_image_3d.astype(float) - depth_image_bg.astype(float))
    background_mask = np.where(depth_diff < clipping_distance_in_pixels, 0, 255).astype(np.uint8)
    background_removed = cv2.bitwise_and(color_frame, color_frame, mask=background_mask)

    # Return the background-removed color image
    return background_removed
