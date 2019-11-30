#Regression Classification 
#y carries regression task 
#Can be used in salary prediction 
#Movie rating 
#y performs classification task
#Object recognition
#Topic classification
#y = w*x + b (simplified version)
#w: coefficient (slope)
#b: bias (intercept0)

#Loss function
#Features of an example
#Mean squred value 
#Can be understood as: 
#Predicted value minus true value, then square 
#And then divided by the amount of sampls (l)


#Linear Model for classification 
#Binary 

#Multiclassification model 
#With the "max" argument, find the nth number is the largest 

#Iverson bracket
#Classification loss

#Class classification
#Softmax function 
#The probability distribution 
#Example
logits = [2.0, 1.0, 0.1]
import numpy as np
exps = [np.exp(i) for i in logits]

#Cross entropy
#One of the most popular
#H(p,q) = ∑p(x)*log[q(x)]

#Gradient descent 
#Linear classification and cross entropy

#Gradient vector 
#Fastest rate of decrease in the direction of gradient vector (if it is negative)
#check whether the value of loss function is very close to the value from previous iteration 
#or that the norm of gradient vector is close to zero.