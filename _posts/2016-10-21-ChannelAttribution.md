---
layout: post
title: Cross Channel Attribution (Part II)
date: "19/10/2016"
bigimg: /img/ca1.jpg
tags: [marketing models, Markov models, survival regression, financial engineering]
---



In the [previous post](https://ahsanijaz.github.io/2016-10-19-channelAttribution/), we looked at some basic models that are used for channel attribution. As discussed earlier, more refined models are required for objective budget allocation. Here, we'll look at two recent methods that take into account the complete conversion chains. We'd also discuss about A/B lift, and how these models should be understood to create a hybrid decision model. 

## Markov chain based attribution

A Markov chain tells you the probability of going from one state to another. Taking the weather example, say you can have three different weather conditions: cloudy, sunny and rainy. There will be some probability of transitioning from a cloudy day to a rainy day. Similarly, there will be some probability of having a sunny day followed with another sunny day. Therefore, we get a transitional probability matrix. So, a markov chain tells you about the possible states and probability of hopping from one state to another. I'd highly recommend the following [tutorial](http://setosa.io/ev/markov-chains/) with excellent visualizations on Markov chains to understand them better. 
In comparison to multichannel heuristic based models, Markov chain provides an objective, robust and transparent way of attributing marketing budget. Instead of condensing user journeys to one click and omitting any additional marketing contacts, or as is the case with more complex models based on predefined weights by the advertisers, markov based models consider the complete chain objectively.
For attribution modeling, the ad factor used in this case is Removal Effect; it is calculated for each channel $$ s_i $$ and is the
change in probability of reaching the conversion state from the starting state when the channel $$ s_i $$ is removed. All the incoming edges of the state $$ s_i $$ that is removed are redirected to the absorbing state (NULL state or no conversion). 
Because it requires no preliminary assumptions about channels or decision processes,
this framework is highly versatile. The only prerequisite for building graphical models is the
availability of historical, individual-level tracking data. This framework can evaluate various
conversion types, including sales, sign-ups, or leads, and easily integrate new online
marketing channels. Analyses can also be run on different aggregation levels, such that users can
analyze not only channels but also advertising campaigns or even different creatives.


![plot of chunk unnamed-chunk-1](/figure/source/2016-10-21-ChannelAttribution/unnamed-chunk-1-1.png)

### Survival Model

- Use time to conversion from each touch-point
- Medians time required to convert starting from each touch-point 

![plot of chunk unnamed-chunk-2](/figure/source/2016-10-21-ChannelAttribution/unnamed-chunk-2-1.png)


### Comparison of other models

- Attribution to conversions to different channels by using all the models

![plot of chunk unnamed-chunk-3](/figure/source/2016-10-21-ChannelAttribution/unnamed-chunk-3-1.png)

### Comparison of other models

- Attribution to touch-points


```
## Error: Insufficient values in manual scale. 5 needed but only 1 provided.
```

![plot of chunk unnamed-chunk-4](/figure/source/2016-10-21-ChannelAttribution/unnamed-chunk-4-1.png)

