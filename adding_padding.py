from PIL import Image
import tempfile
from glob import glob
import cv2
import matplotlib.pyplot as plt
img_mask = "Processed image/Medical Prescriptions/Detected text trial/negative/Resized image with 300 DPI/*.jpg"
img_names = glob(img_mask)
count = 1
for img in img_names:
	im = cv2.imread(img)
	width_y, length_x = im.shape[:2]
	# (H, W) = image.shape[:2]
	padd = 60 - width_y
	if padd > 0:
		im_resized = cv2.copyMakeBorder(im,int(padd/2),int(padd/2),0,0,cv2.BORDER_CONSTANT,value=(0,0,0))	
	else:
		im_resized = im[int(abs(padd/2)):width_y - int(abs(padd/2)),:]
	if length_x < 200:
		padd = 200 - length_x
		im_resized = cv2.copyMakeBorder(im_resized,0,0,int(padd/2),int(padd/2),cv2.BORDER_CONSTANT,value=(0,0,0))
	cv2.imwrite("Processed image/Medical Prescriptions/Detected text trial/negative/Resized image with 300 DPI/padded/negative%s.jpg"%count, im_resized)
	count += 1
	# print(im_resized.size)