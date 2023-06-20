#this program is used to remove watermarks from the resized document
import cv2
import numpy as np
import tempfile
from glob import glob


img_mask = "Processed image/extended dataset/Resized image with 300 DPI/*.jpg"
img_names = glob(img_mask)
count = 1
for im in img_names:
	img = cv2.imread(im)
	# print(img)
	alpha = 2.0
	beta = -160

	new = alpha * img + beta
	new = np.clip(new, 0, 255).astype(np.uint8)

	cv2.imwrite("Processed image/extended dataset/Removed Watermark/Medical Prescription_%s.jpg"%count, new)
	count += 1
	# print(new)