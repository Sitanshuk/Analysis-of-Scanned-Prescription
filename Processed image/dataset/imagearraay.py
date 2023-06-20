import cv2
import numpy as np
import tempfile
from glob import glob
from PIL import Image
import numpy as np
import pandas as pd
img_mask = "*.jpg"
img_names = glob(img_mask)
im_array = []
count = 0
x = []
# print(img_names)
for img in img_names:
	im = cv2.imread(img)
	im_array = np.array(im)
	im_array = im_array[:,:,0]
	(h, w) = im_array.shape[:2]
	im_array = im_array.reshape(w*h,1)
	x.append(im_array)

budecort = np.ones(38)
dery = np.ones(30)
dery = dery*2
dolo = np.ones(64)
dolo = dolo*3
duo = np.ones(50)
duo = duo*4
neg = np.ones(249)
neg = neg*5
nor = np.ones(76)
nor = nor*6
pan = np.ones(65)
pan = pan*7

label = np.concatenate((budecort,dery,dolo,duo,neg,nor,pan))
dataset = list(zip(x,label))
dataset = pd.DataFrame(dataset)
print(dataset.head)




	# print(im_array.shape)
	# count += 1

# print(count)
