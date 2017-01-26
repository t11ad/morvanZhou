import tensorflow as tf

import tensorflow.examples.tutorials.mnist \
        import input_data

mnist = input_data.read_data_sets('MNIST_data', \
        one_hot=True)


def add_layer(inputs, in_size, out_size, \
        activation_function=None,):
    #add one more layer and return the output of 
    #this layer

    Weights = tf.Variable(tf.random_normal([in_size, \
            out_size]))

    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1,)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases

    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b,)
    return outputs

# define placeholders for inputs to network
xs = tf.placeholder(tf.float32, [None, 784]) #28*28 = 784
xs = tf.placeholder(tf.float32, [None, 10]) 

# add output layer
prediction = add_layer(xs, 784, 10, \
        activation_function=tf.nn.softmax)

# the error between prediction and real data

cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys* \
    tf.log(prediction), reduction_indices=[1])) # loss

train_step =
tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

sess = tf.Session()

#important step
sess.run(tf.initialize_all_variables())

for i in range(1000)
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={xs: batch_xs, \
            ys: batch_ys})
    if i % 50 == 0
        print(compute_accuracy(mnist.test.images, \
                mnist.test.labels))



