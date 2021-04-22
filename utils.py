from matplotlib import pyplot as plt


def plot_results(gray_image, gray_filtered, edges, edges_high_thresh,
                 edges_filtered, edges_high_thresh_filtered):
    plt.subplot(231), plt.imshow(gray_image, cmap='gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(232), plt.imshow(edges, cmap='gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(233), plt.imshow(edges_high_thresh, cmap='gray')
    plt.title('Edge Image High Threshold'), plt.xticks([]), plt.yticks([])

    plt.subplot(234), plt.imshow(gray_filtered, cmap='gray')
    plt.title('Filtered Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(235), plt.imshow(edges_filtered, cmap='gray')
    plt.title('Edge Image Filtered'), plt.xticks([]), plt.yticks([])
    plt.subplot(236), plt.imshow(edges_high_thresh_filtered, cmap='gray')
    plt.title('Edge Image High Threshold Filtered'), plt.xticks([]), plt.yticks([])
    plt.show()
