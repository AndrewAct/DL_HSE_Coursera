#11/29/2019
#Placeholder
X = tf.placeholder(tf.float32, (None, 10))

#Variable 
w = tf.get_variable("w", shape = (10, 20), dtype = tf.float32)
w = tf.Variable(tf.random_uniform((10,20)), name = "w")

#Constant 

#Matrix product 
x = tf.placeholder(tf.float32, (None, 10))
w = tf.Variable(tf.random_unifor((10, 20)), name = "w")
z = x@w

#COmputational graph
#Tensorflow creates default graph after importing

#You can also create your own one 
#Using tf.get_default_graph().get_operations()

#Create a session 
s = tf.InteractiveSession()

#Defining a graph 
a = tf.constant(5.0)
b = tf.constant(6.0)
c = a*b

#Running a graph 
print(c)
print(s.run(c))

##    Example    ##
#Definition 
tf.reset_default_graph()
a = tf.constant(np.ones((2,2), dtype = np.float32))
b = tf.Variable(tf.ones((2,2)))
c = a@b

#Running attempt 
s = tf.InteractiveSession()
s.run(c)
#This is a bad display

#Running properly 
s.run(tf.gloabal_variables_initializer())
s.run(c)


#### First TensorFlow Framework ####
#Optimizer in TensorFlow 
import numpy as np 
import tensorflow as tf 

tf.reset_default_graph()
x = tf.get_variable("x", shape = (), dtype = tf.float32)
f = x**2

#If minimize the value of x
optimizer = tf.train.GradientDescentOptimizer(0.1)
step = optimizer.minimize(f, var_list = [x])


#Yu could do better with TensorBoard
tf.summary.scalar('curr_x', x)
tf.summary.scalar('curr_x', f)
summaries = tf.summary.merge_all()

#Log the summaries
s = tf.InteractiveSession()
summary_writer = tf.summary.FileWriter("logs/1", s.graph)

s.run(tf.global_variables_initializer)

for i in range(10):
    _, curr_summaries = s.run([step, summaries])
    summary_writer.add_summary(curr_summaries, i)
    summary_writer.flush()

#Solve a linear regression 
##Gradient descent 
s =tf.InteractiveSession()
s.run(tf.global_variables_initializer())

for i in range(300):
    _, curr_loss, curr_weights = s.run(
        [step, loss, weights], feed_dict = {features:x, target: y}
    )
    if i%50 == 0:
        saver.save(s, "logs/2/model.ckpt", global_step = i)
        print(curr_loss)