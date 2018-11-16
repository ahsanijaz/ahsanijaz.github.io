---
layout: post
title: A less trodden road to data science 
date: "01/11/2018"
tags: [Workshops, Data Science]
image: /img/scream.jpg
---

Internet is replete with posts on 'how to become a data scientist'. Unfortunately, I'm also adding a post on this topic. The breadth of knowledge expected of a practicing data scientist can be quite daunting. However, one can limit the depth in some of these skills. 
Here, I'd put together the bare minimum resources that a data scientist should go through. I'll attempt to provide the resources needed to sharpen each of the needed skill sets and how to approach the learning path. There is minimum set of skills that is needed before one qualifies as a practicing data scientist. Data Scientist role has morphed into a concoction of skill sets. 

What follows is a catalog of resources divided under different skill sets. 


# Mathematical Background
There is no way around it! You need strong mathematics to be a data scientist. I usually start the interview process by asking the candidates to draw equations of commonly used functions ($$\exp(-x)$$, $$\cos(kx)$$, $$sin(kx)$$ $$\log_{k}(x),...$$. Why is this needed? Once you start on the machine learning journey, You can't go around without sigmoid functions, trend analysis, radial basis kernels and estimators using log scale. Therefore, it is important to familiarize yourself with geometry of these functions:
* [An intuition of exponential functions](http://setosa.io/ev/exponentiation/)
* [sin and cos functions](http://setosa.io/ev/sine-and-cosine/) 
* [Common mathematical functions](https://www.mathsisfun.com/sets/functions-common.html)
* [Activation functions in deep learning](https://www.learnopencv.com/understanding-activation-functions-in-deep-learning/)

## Calculus review
Since, most of the machine learning models require a geometric interpretation, I'd recommend to create a geometric interpretation of mathematical concepts as well. Here, the suggested resources are provided since the explanations are provided within a geometric framework. In the links that follow, explanations are provided that help in visualizing the derivatives; critical points and using these to plot lines. You'd see that this interpretation will help you to create a deeper appreciation of optimization algorithms like **gradient descent, RMSprop and stochastic gradient descent**.
* [The Shape Of A Graph](http://tutorial.math.lamar.edu/Classes/CalcI/ShapeofGraphPtI.aspx)
* [The Shape Of A Graph (Part 2)](http://tutorial.math.lamar.edu/Classes/CalcI/ShapeofGraphPtII.aspx)
Also, don't forget to review the chain rule:
* [Chain Rule](http://tutorial.math.lamar.edu/Classes/CalcIII/ChainRule.aspx)

What follows is an article of using integrals to compute areas. I find this interpretation important when working on **Monte Carlo simulations**. 
* [Area between curves](http://tutorial.math.lamar.edu/Classes/CalcI/AreaBetweenCurves.aspx)
* [Volumes using integration](http://tutorial.math.lamar.edu/Classes/CalcIII/TripleIntegrals.aspx)
Here is another article that discusses integration as area and can more easily be related to **dot product** (mother of all machine learning and feature engineering).
* [Integration as area](http://tutorial.math.lamar.edu/Classes/CalcI/AreaProblem.aspx)
Finally, it is important to understand the interplay of integration and probability distributions.
* [Probability density function](http://tutorial.math.lamar.edu/Classes/CalcII/Probability.aspx)

If it is easier for you to follow videos instead of reading, here's the link to some exceptional visually explained lectures on Calculus: [Cal lectures](https://www.youtube.com/watch?v=WUvTyaaNkzM&list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr). 

## Linear Algebra
Linear algebra is the core of feature engineering; basis selection; dimensionality reduction; matrix factorization; spectral clustering; deep learning and generalized linear models to name some. Almost all the algorithms have a linear algebra interpretation to them. Therefore, it is the back bone of Machine learning and you can't do without knowing it well.
I haven't found a resource better than Gilbert Strang's [lecture series](https://www.youtube.com/watch?v=ZK3O402wf1c&list=PL49CF3715CB9EF31D) on linear algebra. It can be arduous to follow through all of them, but do if you can. If you just want the essentials for Machine Learning from the complete course, take the following of his lectures:
* [Lec 6: Column space and null space](https://www.youtube.com/watch?v=8o5Cmfpeo6g)
* [Lec 9: Independence, basis and Dimension](https://www.youtube.com/watch?v=yjBerM5jWsc)
* [Lec 14: Orthogonal vectors](https://www.youtube.com/watch?v=YzZUIYRCE38)
* [Lec 15: Projection into subspaces](https://www.youtube.com/watch?v=Y_Ac6KiQ1t0)
* [Lec 16: Projection matrices and least squares](https://www.youtube.com/watch?v=osh80YCg_GM)
* [Lec 21: Eigenvalues and Eigenvector](https://www.youtube.com/watch?v=lXNXrLcoerU)
* [Lec 29: Singular Value Decomposition](https://www.youtube.com/watch?v=Nx0lRBaXoz4)
* [Lec 31: Change of basis](https://www.youtube.com/watch?v=vGkn-3NFGck)

The mathematical background provided by Ian Goodgellow is quite thorough although somewhat dry. It is a good review nevertheless, so referring it over here.
[Ian Goodfellow](https://www.deeplearningbook.org/contents/linear_algebra.html)
In case you are taking the selected lectures only, do go through this small series of linear algebra lectures. It is one of the best visualization explanation lecture series that I've come across.
[3blue1brown Linear Algebra Lecture](https://www.youtube.com/watch?v=fNk_zzaMoSs&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)

Finally, these are some beautiful javascript visualizations to understand EigenValues, Eigen vectors, PCA and least squares.

* [Eigenvectors and eigenvalues](http://setosa.io/ev/eigenvectors-and-eigenvalues/)
* [Principal Component Analysis](http://setosa.io/ev/principal-component-analysis/)
* [Least Squares Regression](http://setosa.io/ev/ordinary-least-squares-regression/)


## Probability and Statistics
Read the first two parts of [Larry Wasserman's All of Statistics](https://www.ic.unicamp.br/~wainer/cursos/1s2013/ml/livro.pdf). In addition to that, do look through the following articles:
* [Conditional Probability](http://setosa.io/conditional/)
* [Monty Hall Problem](http://blog.vctr.me/monty-hall/)
* [Markov Chains](http://setosa.io/blog/2014/07/26/markov-chains/index.html)
* [Central limit theorem](http://blog.vctr.me/posts/central-limit-theorem.html)

# Programming

# Data Engineering


# Big Data Paradigm


# Machine Learning
* [Machine learning specialization](https://www.coursera.org/specializations/machine-learning)

# Deep Learning


## Frameworks

# Books

