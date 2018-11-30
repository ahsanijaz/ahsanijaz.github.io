---
layout: post
title: Mining weather conditions
date: "04/03/2017"
---


number of input features
gpu/cpu configuration
training data

impossible to correctly guess the correct hyperparameters-iterative process of finding a good choice of network.

How efficient you can cycle:

Train/validation set/Test sets
dev test just big enough-not whole 20% of data
same is the case with test case (10k might be enough with 1mil examples)
Traditional ratios with small data sets
Distribution should be the same (getting data from different sources)

bias/variance tradeoff 

if train error << dev error (over-fitting) (high variance)
Bayes set- look at train/dev set to see if high variance or high bias
 
L1 and L2 regularization

regularization parameter - using cross validation/validation set

Frobenius norm of a matrix

Drop out regularization:

Separate optimization and over-fitting-decouple these

l2 over early stopping to decouple-but need to set hyperparameter


NORMALIZE THE INPUTS:

use same mean and sd


Initialization: speed up convergence
Increase the odds of gd converging to lower training error
Vanishing/exploding gradients

Deep learning flexible enough to cause over-fitting

really iterative process

works on big data-slow 

stochastic-loose speed up by vectorization
batch descent- too big
so something in between for value of batch size (64,128,256,512,1024)

minibatch in CPU/GPU memory - hyperparameter


shear number of hyperparameters (adam, b1, b2, epsilon, number of layers, hidden units; learning rate decay;
learning rate; mini batch size)
Learning rate- most important
Momentum term (0.8-0.99) 0.9
3) #hidden units
3) mini batch size
4) layers-learning rate decay

Don't use grid search for hyperparameters;
- choose at random: difficult to know in advance which one is more important 
- coarse to fine sampling scheme
-
Picking hyperparameters at random:

uniformly random on layers or hidden units

-but with alpha maybe 0.0001 to 1: less resources at smaller scale-search on log scale (uniformly between 

r = -3*np.random.rand() -> 
alpha = 10^r <- 10-4 ... 10-0

beta = 0.9 to 0.999 (0.9 last 10 values, averaging over last 1000 values). (1 - beta) do on the log scale.
1-beta = 10^r r belongs to -3, -1 (log scale)

when beta is close to 1, sensitivity changes with small changes- b 0.9 ->0.9005 (no diff) 0.999 ->9.9995 huge difference. (last 1000 to last 2000 examples).

babysitting the model-dev set error decrease
training many models at the same time
Batch normalization:

slight regularization effect 
bigger minibatch size-less regularization effect due to noise

filter size; padding; stride; number of filters;
max pooling hyperparameters: filter size (2,2)shrinking by two ,(3,2; stride; max or average pooling;padding = 0
look at literature and use similar hyperparameters

It helps us keep more of the information at the border of an image. Without padding, very few values at the next layer would be affected by pixels as the edges of an image
It allows you to use a CONV layer without necessarily shrinking the height and width of the volumes. This is important for building deeper networks, since otherwise the height/width would shrink as you go to deeper layers.



open source-freeze-depending on data freeze layers-use as initialization-use the same network if you are working on the same kind of problem. (always do unless too big data+computational budget)
