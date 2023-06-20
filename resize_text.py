from PIL import Image
import tempfile
from glob import glob
import cv2
import matplotlib.image as img
img_mask = "Processed image/Medical Prescriptions/Detected text trial/negative/*.jpg"
img_names = glob(img_mask)
count = 1
for img in img_names:
	im = Image.open(img)
	length_x, width_y = im.size
	factor = min(1,float(200/length_x))
	size = int(factor*length_x), int(factor*width_y)
	im_resized = im.resize(size,Image.ANTIALIAS)	
	im_resized.save("Processed image/Medical Prescriptions/Detected text trial/negative/Resized image with 300 DPI/negative%s.jpg"%count, dpi=(500, 500))
	count += 1
	print(im_resized.size)