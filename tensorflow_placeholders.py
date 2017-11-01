import tensorflow as tf
import numpy as np

#define placeholder
placeholder_1 = tf.placeholder(tf.float32, shape=(1024,1024), name="placeholder_1")
product = tf.matmul(placeholder_1, placeholder_1)

with tf.Session() as session:
    tensor = np.random.rand(1024,1024)
    print(session.run(product, feed_dict = {placeholder_1: tensor}))
