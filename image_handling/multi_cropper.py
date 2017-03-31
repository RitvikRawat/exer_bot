from scipy import misc
import numpy as np
import sys

# face = misc.face()
# misc.imsave('face.png', face)

for img_no in range(1,99):
	print img_no

	f = misc.imread('/home/robot/Desktop/crop_trial/folder/%d.png' % img_no)
	# print type(f)      
	# print f.shape, f.dtype

	cropped_image = np.zeros((400,525),dtype=f.dtype)

	for i in range(540):
		for j in range(960):
			if( (i > 75) and (i <= 475) and (j > 200) and (j <= 725) ):
				cropped_image[i - 76][j - 201] = f[i][j]

	misc.imsave('/home/robot/Desktop/crop_trial/folder2/%d_cr.png' % img_no, cropped_image)

# import matplotlib.pyplot as plt
# plt.imshow(cropped_image)
# plt.show()