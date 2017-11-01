import tensorflow as tf

constant_1 = tf.constant(1, dtype="float32")
constant_2 = tf.constant(2, dtype="float32")
sum = tf.add(constant_1, constant_2)
product = tf.multiply(constant_1, constant_2)


#create session
session = tf.Session()

#print constants
print(session.run([constant_1, constant_2]))

#print sum
print(session.run(sum))

#print product
print(session.run(product))

session.close()
