import cv2
import numpy as np

print("hello");
img_path = "inimg.JPG"
segmentation_mask_img = "seg_img.JPG"
img = cv2.imread(img_path)
seg_mask = cv2.imread(segmentation_mask_img)

alpha_binary = np.sum(seg_mask, axis=-1) > 0
alpha = np.uint8(alpha_binary * 255)

black_to_alpha = np.dstack((img, alpha))
cv2.imwrite('black_to_alpha11.png', black_to_alpha)
