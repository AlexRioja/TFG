import numpy as np
from cv2 import cv2 as cv
import utils
"""The edge pixels above the upper limit are considered in an edge map and edge 
pixels below the threshold are discarded. So what about the pixels inbetween upper 
and lower threshold?
They are considered only if they are connected to pixels in upper threshold. 
Thus we get a clean edge map.
"""

# Read image
gray_image = cv.imread('assets/test_images/2.jpg', 0)
#Filter helps de-noise dense edges areas
gray_filtered = cv.bilateralFilter(gray_image, 7, 50, 50)
# Apply Canny algorithm(image, lowLimit, upperLimit)
edges = cv.Canny(gray_image, 60, 120)
edges_high_thresh = cv.Canny(gray_image, 150, 320)
edges_f = cv.Canny(gray_filtered, 60, 120)
edges_high_thresh_f = cv.Canny(gray_filtered, 150, 320)
# Show results
utils.plot_results(gray_image, gray_filtered, edges, edges_high_thresh,edges_f,edges_high_thresh_f)
