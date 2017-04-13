import numpy as np
import tensorflow as tf

# read data from CSV format
feature_data = np.genfromtxt("all.csv", delimiter=',',usecols=range(1,210001))
label_data = np.genfromtxt("all.csv", delimiter=',',usecols=(0))



print feature_data[0].shape
print label_data.shape
# print feature_data[97][50000]
# print label_data[0]

# x has the input training vector
x = tf.placeholder(tf.float32, [210000])

# model
W = tf.Variable(tf.zeros([210000, 3]))
b = tf.Variable(tf.zeros([1,3]))

# model output
y = tf.matmul(tf.expand_dims(x,0), W) + b

# label of the image
y_ = tf.placeholder(tf.float32, [1,3])

# loss defined
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))

# optimiser used is gradient descent
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

sess = tf.InteractiveSession()
tf.global_variables_initializer().run()

no_of_runs = 1000000
print "_____________________________________________"
print no_of_runs

# train the model
for i in range(1,no_of_runs):
	
	index = i % 279
	if (index == 0):
		index = 1

	if(label_data[index] == 1):
		hard_code_label = [[1,0,0]]
	elif(label_data[index] == 2):
		hard_code_label = [[0,1,0]]
	elif(label_data[index] == 3):
		hard_code_label = [[0,0,1]]

	sess.run(train_step, feed_dict={x: feature_data[index] , y_: hard_code_label})

# load test data
test_data = np.genfromtxt("test.csv", delimiter=',',usecols=range(1,210001))
test_label = np.genfromtxt("test.csv", delimiter=',',usecols=(0))


#n testing the model
for i in range(9):

	if(test_label[i] == 1):
		test_coded = [[1,0,0]]
	elif(test_label[i] == 2):
		test_coded = [[0,1,0]]
	elif(test_label[i] == 3):
		test_coded = [[0,0,1]]
	
	print(sess.run(y, feed_dict={x: test_data[i] , y_: test_coded}))