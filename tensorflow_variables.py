import tensorflow as tf

#define and print variable_1's properties
variable_1 = tf.Variable([1,2], "variable_1")
print(variable_1)

#define and print variable_2's properties
variable_2 = tf.Variable([2,3], "variable_2")
print(variable_2)

#define add operation
sum = tf.add(variable_1, variable_2)

#define variable_3 which will hold the result of the add operation
variable_3 = tf.Variable([-1,-1], "variable_3")

#init a global variable initializer
init_variables = tf.global_variables_initializer()

#create a session to manipulate nodes
with tf.Session() as session:
    session.run(init_variables)
    print("variable 1: ", session.run(variable_1))
    print("variable 2: ", session.run(variable_2))
    print("variable 3: ", session.run(variable_3))
    # assign sum to variable 3
    variable_3 = tf.assign(variable_3, sum)
    print("variable 3: ", session.run(variable_3))
