import tensorflow.compat.v1 as tf

tf.disable_v2_behavior()

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
c = a + b
print('c = ', c)

with tf.Session() as sess:
    result = sess.run(c, {a: 2., b: 3.})
print('result = ', result)