from scipy import misc
import sys
import matplotlib.pyplot as plt

image_to_open = str( sys.argv[1] )
image_to_save = str( sys.argv[2] )

f = misc.imread( image_to_open )

depth_list = []

for i in range(400):
	for j in range(525):
		depth_list.append( f[i][j] )

depth_list.sort()

max_val = depth_list[ int(400*525*0.75) ]

print max_val

for i in range(400):
	for j in range(525):
		if ( f[i][j] >= max_val ):
			f[i][j] = max_val
		f[i][j] = int( (f[i][j] * 254) / max_val )

misc.imsave( image_to_save, f )
plt.imshow( f )
plt.show()