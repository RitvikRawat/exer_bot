from scipy import misc
import numpy as np
import sys

for img_no in range(1,94):

	f = misc.imread('/home/robot/Desktop/data_modification/folder/%d_cr.png' % img_no)

	depthlist = []

	for i in range(400):
		for j in range(525):
			depthlist.append( f[i][j] )

	depthlist.sort()

	max_val = depthlist[ int(400*525*0.75) ]

	for i in range(400):
		for j in range(525):
			if ( f[i][j] >= max_val ):
				f[i][j] = max_val
			f[i][j] = int( (f[i][j] * 254) / max_val )

	print img_no , max_val

	misc.imsave('/home/robot/Desktop/data_modification/folder2/%d_cr_sc.png' % img_no, f)
