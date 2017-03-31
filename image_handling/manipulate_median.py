from scipy import misc
# face = misc.face()
# misc.imsave('face.png', face)

f = misc.imread('t1.png')
print type(f)      
print f.shape, f.dtype

min_val = 2000

# for i in range(540):
# 	for j in range(960):
# 		if( ( f[i][j] > 1500 ) & ( f[i][j] <= min_val ) ):
# 			min_val = f[i][j]

# print min_val

# for i in range(540):
# 	for j in range(960):
# 		f[i][j] = f[i][j] - min_val

lin_arr = []

for i in range(540):
	for j in range(960):
		lin_arr.append( f[i][j] )

lin_arr.sort()

threshold = lin_arr[ ( 540 * 960 ) / 2 ]

print "Threshold is : ",threshold

for i in range(540):
	for j in range(960):
		if( f[i][j] > threshold ):
			f[i][j] = 0

misc.imsave('test_plot.png', f)

import matplotlib.pyplot as plt
plt.imshow(f)
plt.show()