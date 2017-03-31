from scipy import misc
# face = misc.face()
# misc.imsave('face.png', face)

f = misc.imread('t1.png')
print type(f)      
print f.shape, f.dtype

lin_arr = []

for i in range(540):
	for j in range(960):
		lin_arr.append( f[i][j] )

lin_arr.sort()

max_jump = 0
flag = 0

for i in range( len(lin_arr)/2 , len(lin_arr) - 1 ):
	if( (- ( lin_arr[i] - lin_arr[i+1] )) > max_jump ):
		max_jump = - ( lin_arr[i] - lin_arr[i+1] )
		flag = i

print "max_jump is :", max_jump
print "from ",lin_arr[flag]," to ",lin_arr[flag+1]

threshold = ( lin_arr[flag] + lin_arr[flag + 1] ) / 2

print "Threshold is : ",threshold

for i in range(540):
	for j in range(960):
		if( f[i][j] > threshold ):
			f[i][j] = 0

misc.imsave('test_plot.png', f)

import matplotlib.pyplot as plt
plt.imshow(f)
plt.show()