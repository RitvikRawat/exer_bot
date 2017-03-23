import numpy as np
from PIL import Image

data = open('firstlog.txt').read()
#out = open('output.txt','wb')
data_list = data.split()

maximum = 0
for i in range(len(data_list)):
	data_list[i] = float(data_list[i])
	# data_list[i] = int(data_list[i])
	if(data_list[i] >= maximum):
		maximum = data_list[i]

# print maximum
# print len(data_list)

for i in range(len(data_list)):
	data_list[i] = ( data_list[i] / maximum ) * 254
	data_list[i] = int(data_list[i])

array = np.zeros( (512,424,3) , dtype = np.uint8 )

for i in range(len(data_list)):
	row_index = i / 424
	column_index = i % 424
	#print i , data_list[i]
	array[row_index][column_index][0] = data_list[i]
	array[row_index][column_index][1] = data_list[i]
	array[row_index][column_index][2] = data_list[i]
	# print row_index , column_index

img = Image.fromarray( array , 'RGB' )
img.save( 'my.png' )
img.show()