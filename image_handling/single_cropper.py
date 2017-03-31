from scipy import misc
import numpy as np
import sys

# face = misc.face()
# misc.imsave('face.png', face)

image_to_open = str(sys.argv[1])
image_to_save = str(sys.argv[2])

print image_to_open

f = misc.imread(image_to_open)
print type(f)      
print f.shape, f.dtype

cropped_image = np.zeros((400,525),dtype=f.dtype)

for i in range(540):
	for j in range(960):
		if( (i > 75) and (i <= 475) and (j > 200) and (j <= 725) ):
			cropped_image[i - 76][j - 201] = f[i][j]

misc.imsave(image_to_save, cropped_image)

import matplotlib.pyplot as plt
plt.imshow(cropped_image)
plt.show()