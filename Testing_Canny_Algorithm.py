import numpy as np
from cv2 import cv2 as cv
import utils

"""The edge pixels above the upper limit are considered in an edge map and edge 
pixels below the threshold are discarded. So what about the pixels inbetween upper 
and lower threshold?
They are considered only if they are connected to pixels in upper threshold. 
Thus we get a clean edge map.
"""

"""
1.- First try with manual parameters
"""
# Read image
gray_image = cv.imread('assets/1.jpg', 0)
#Filter helps de-noise dense edges areas
gray_filtered = cv.bilateralFilter(gray_image, 7, 50, 50)
# Apply Canny algorithm(image, lowLimit, upperLimit)
edges = cv.Canny(gray_image, 60, 120)
edges_high_thresh = cv.Canny(gray_image, 150, 320)
edges_f = cv.Canny(gray_filtered, 60, 120)
edges_high_thresh_f = cv.Canny(gray_filtered, 150, 320)
# Show results
utils.plot_results(gray_image, gray_filtered, edges, edges_high_thresh,edges_f,edges_high_thresh_f)

"""
2.-Automatic parameters (from pyimagesearch-automatic canny)
"""
def auto_canny(image, sigma=0.33):
    """[summary]

    Args:
        image ([type]): [description]
        sigma (float, optional): Lower value->tighter threshold. Defaults to 0.33.

    Returns:
        [type]: [description]
    """
    # compute the median of the single channel pixel intensities
    v = np.median(image)
    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv.Canny(image, lower, upper)
    # return the edged image
    return edged


# load the image, convert it to grayscale, and blur it slightly
image = cv.imread('assets/1.jpg')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
blurred = cv.GaussianBlur(gray, (3, 3), 0)
# apply Canny edge detection using a wide threshold, tight
# threshold, and automatically determined threshold
wide = cv.Canny(blurred, 10, 200)
tight = cv.Canny(blurred, 225, 250)
auto = auto_canny(blurred)
# show the images
cv.namedWindow("Original",cv.WINDOW_NORMAL)
cv.imshow("Original", image)
cv.namedWindow("Edges",cv.WINDOW_NORMAL)
cv.imshow("Edges", np.hstack([wide, tight, auto]))
cv.waitKey(0)
