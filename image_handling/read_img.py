from scipy import misc
import sys
# face = misc.face()
# misc.imsave('face.png', face)

image_to_open = str(sys.argv[1])
image_to_save = str(sys.argv[2])

print image_to_open

# f = misc.imread('0000_depth.png')
f = misc.imread(image_to_open)
print type(f)      
print f.shape, f.dtype

misc.imsave(image_to_save, f)

import matplotlib.pyplot as plt
plt.imshow(f)
plt.show()