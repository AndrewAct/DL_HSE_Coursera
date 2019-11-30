## Multilayer Perception ##
#Decision function: d(x) = w0 + w1x1 + w2x2
#Agorithm; a(x) = sign(d(x))

## Logistic regression ##
#Decision function: d(x) = w0 + w1x1 + w2x2
#Algorithm: a(x) = œ(d(x))
#Recall Sigmoid function 

## Neuron ##

##Chain Rule##
##Chain rule of a function

##Backprogation##
#Apply chain rule efficiently
#Example 
def forward_pass(inputs):
    return 1./(1+np.exp(-inputs))

#Backward pass
def backward_pass(nputs, incoming_gradient):
    sigmoid = 1./(1+np.exp(-inputs))
    return sigmoid*(1- sigmoid)*incoming_gradient