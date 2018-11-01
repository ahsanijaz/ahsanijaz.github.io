---
layout: post
title: Monte Calro simulation using low level TensorFlow (Part I)
date: "01/11/2018"
---

Monte Carlo methods are computational algorithms relying on repeated random sampling to solve a variety of optimization, integration and sampling problems. More often than not, one stumbles across an intractable integral only solvable through numericel integration. The field of Physics and Mathematics also rely heavily on Monte Carlo Simulations. Moreover, these simulations provide random amount of error, reduciable by expanding computational resources. Thus, an error budget can be provided based on the resources.
In machine learning, some methods are quite difficult to solve and approximate answers is all that we can get. Therefore, at times, it is needed to use Monte Carlo approximations over deterministic methods. In this post, I'll attempt at solving some simple integrations by using Monte Carlo simulations. Future posts will expand on this to discuss Importance Sampling and Markov Chain Monte Carlo Methods.

## Monte Carlo Simulation using low-level TensorFlow

In this post, I'd use low level TensorFlow framework to solve simple integration problems. Hopefully, by the end of this post, you'd develop an understanding of how these simulations are used to solve complex problems. Let's start simple and follow the logic between different portions of the program.


```python
import tensorflow as tf
```

### Defining problem
As an example problem, let's find the solution of the following equation:

$$ \int_{0}^{2}{x^{2}}dx $$

This can easily be integrated to obtain:

$$ \tfrac{x^{3}}{3}\big|_0^2 = 2.667 $$

Now if want to solve it using Monte Carlo simulation, we have to generate random samples within some bounded region and see how many of those fall within our region of interest i.e. lie under the line drawn by $$y= x^2$$. 

### Generating samples in TensorFlow
In other words, we have to generate random uniform numbers with x-coordinate between 0 and 2 (since integration is from 0 to 2) and y-coordinate from 0 to 4 (as the $$x^2$$ function gives the y value of 4 at x = 2). To ease understanding, I'll execute the TensorFlow code in Eager mode and wrap it around a function in the end. Here, I draw 10000 samples from uniform distribution in TensorFlow as follows:


```python
tf.enable_eager_execution()
x = tf.random_uniform((10000,1),0,2)
y = tf.random_uniform((10000,1),0,4)
```

### Finding region of interest
Once we have our random samples drawn from uniform distribution, we have to find the number of (x,y) samples that fall within $$x^2$$ function. This can easily be done as:


```python
sample_in_region = y<x**2
```

Finally, we can find the total count of these samples as:


```python
count = tf.reduce_sum(tf.cast(sample_in_region,tf.float32))
print(count)
```

    tf.Tensor(3282.0, shape=(), dtype=float32)


### Computing the area
Now, in the example above, we know that the total samples we have generated are 10,000 where as those lying under the $$x^2$$ function are given in the variable _count_. The range in which uniform samples were drawn has the area of 8 ( x-range * y-range = (2-0)*(4-0) = 8).
Therefore, the ratio of area of function and range is equal to the ratio of _count_ and total samples. This is given as:

$$\frac{\textit{area}}{\textit{range_area}} = \frac{count}{\textit{n_of_samples}}$$

Programmatically, the area can be computed as:


```python
area = count/10000*8
print(area)
```

    tf.Tensor(2.6256, shape=(), dtype=float32)


As you can see, the area is approximately equal to the one computed deterministically.

## Using TensorFlow session:

What follows is the vanilla TensorFlow mode of carrying these computations along with some code refactoring.


```python
def compute_integral(n_samples):
    x = tf.random_uniform((n_samples,1),0,2)
    y = tf.random_uniform((n_samples,1),0,4)
    c_in_region = y<x**2
    count = tf.reduce_sum(tf.cast(c_in_region,tf.int16))
    return count*8/n_samples
```


```python
with tf.Session() as sess:
    result = sess.run(compute_integral(10000))
    print(result)
```

    2.6599998

