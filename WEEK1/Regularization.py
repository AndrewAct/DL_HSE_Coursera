#Overfitting and generalization 
#Training set and holdout set


#Small holdout set:
#The training set is representative 
#The holdout set is of high variance

#Large holdout set:
#The training set is not so representative 
#The variance of large holdout set is of low variance but biased

#Crossvalidtion 
#With a n-fold cross validation set
#n times of training are required 

#Weight penalty
#Lreg(w) = L(w) + lambda* R(w)
#L(w): loss function 
#R(w): regularizer
#lambda: regularizaation strength 
#Cannot be optimized for simple linear gradient models

##Common method up to now (this module) is penalizing large weight 

##Quizzes##
#Overfitting is a situation where a model gives lower quality for new data compared to quality on a training sample
#Large model weights can indicate that model is overfitted


#It is sensitive to the particular split of the sample into training and test parts
#It can give biased quality estimates for small samples

##Stochastic gradient descent##
#When dealing with large sample sets 
#We can store our sample on the hard drive, 
#Then read one example at a time and do an update using just this example.

##Momentum 
#ht = åht-1 + ßt*gt
#Tend to move in the same direction as previous did 

##nesterov-momentum
##AdaGrad

