#This program is used to resize all scanned document to 300dpi 

from PIL import Image
import tempfile
from glob import glob
img_mask = "Processed image/extended dataset/Medical Prescriptions/*.jpg"
img_names = glob(img_mask)
# print(img_names)

count = 1
for img in img_names:
	im = Image.open(img)
	length_x, width_y = im.size
	# print(length_x,width_y)

	factor = min(1,float(1024.0/length_x))
	size = int(factor*length_x), int(factor*width_y)
	im_resized = im.resize(size,Image.ANTIALIAS)
# temp_file = tempfile.NamedTemporaryFile(delete=False,   suffix='.png')
# temp_filename = temp_file
	im_resized.save("Processed image/extended dataset/Resized image with 300 DPI/Medical Prescription_%s.jpg"%count, dpi=(500, 500))
	count += 1
	print(im_resized.size)

