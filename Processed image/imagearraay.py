import cv2
import numpy as np
import tempfile
from glob import glob
from PIL import Image
import numpy as np
img_mask = "*.jpg"
img_names = glob(img_mask)
im_array = []
count = 1
for img in img_names:
	im = cv2.imread(img)
	im_array = np.array(im)
	im_array = im_array[:,:,0]
	width_y = im_array[0].shape
	length_x = im_array[1].shape
	print(width_y,length_x)
	# im_array = im_array.reshape(width_y[0]*length_x[0],1)

	# print(im_array.shape)
	# width_y, length_x = im[:2]
	# im_array.append([length_x,width_y])
	# im_array = np.array(im)
	# im_array = im_array.reshape(12000,1)
# print(im_array)
