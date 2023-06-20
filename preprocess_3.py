#this program is used to convert the watermark free document into binary image using inv binary thresolding
import cv2
import numpy as np
from matplotlib import pyplot as plt
import tempfile
from glob import glob

img_mask = "Processed image/extended dataset/Removed Watermark/*.jpg"
img_names = glob(img_mask)
count = 1
for im in img_names:

	img = cv2.imread(im,0)
# ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
	# ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)

	blur = cv2.GaussianBlur(img,(5,5),0)

# find normalized_histogram, and its cumulative distribution function
	hist = cv2.calcHist([blur],[0],None,[256],[0,256])
	hist_norm = hist.ravel()/hist.max()
	Q = hist_norm.cumsum()

	bins = np.arange(256)

	fn_min = np.inf
	thresh = -1

	for i in range(1,256):
		p1,p2 = np.hsplit(hist_norm,[i]) # probabilities
		q1,q2 = Q[i],Q[255]-Q[i] # cum sum of classes
		print(q1,q2)
		b1,b2 = np.hsplit(bins,[i]) # weights

	# finding means and variances
		m1,m2 = np.sum(p1*b1)/q1, np.sum(p2*b2)/q2
		v1,v2 = np.sum(((b1-m1)**2)*p1)/q1,np.sum(((b2-m2)**2)*p2)/q2

	# calculates the minimization function
		fn = v1*q1 + v2*q2
		if fn < fn_min:
			fn_min = fn
			thresh = i

# find otsu's threshold value with OpenCV function
	ret, otsu = cv2.threshold(blur,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
	# print thresh,ret



	# cv2.imwrite("Processed image/Medical Prescriptions/Binary Img/Medical Prescription_%s.jpg"%count, thresh1)
	cv2.imwrite("Processed image/extended dataset/Binary Img/Medical Prescription_%s.jpg"%count, otsu)

	count += 1
	# th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
	# thresh2.save("Processed image/Medical Prescriptions/Binary Img/Medical Prescription_%s.jpg"%count)

# ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
# ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
# ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

# titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV','Adaptive Gaussian Thresholding']
	# titles = ['Original Image','BINARY_INV']
	# images = [img, thresh1]
# images = [img, thresh1, thresh2, thresh3, thresh4, thresh5, th3]

	# for i in range(2):
	#     plt.subplot(1,2,i+1),plt.imshow(images[i],'gray')
	#     plt.title(titles[i])
	#     plt.xticks([]),plt.yticks([])

	# plt.show()