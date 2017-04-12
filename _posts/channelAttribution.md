---
layout: post
title: Cross Channel Attribution (Part I)
date: "19/10/2016"
bigimg: 
---

With the advent of data driven and measurement-focused marketing, cross channel attribution has become a hot topic. Briefly, it is used to assign proportional credit to each marketing touch point be it offline or digital that leads to a desired customer action. Therefore, attribution analytics can help the brands to optimize their media and marketing spending while measuring the impact produced by each marketing channel. 
When understood correctly, it provides clear and accurate insights about marketing influence on customers across channels. With this system in place, a marketing budget can be made to create an optimal mix of customer interactions. In short, with cross-channel attribution, marketers can do more with less because they understand their customers better.
Trouble is, that brands routinely underestimate the intricacies involved in creating advanced, enterprise-scale, near real time analytics. In my personal interactions, most of the major brands do not even have a closed loop system about customer interactions and sale points with marketing efforts. Even to get some antiquated methods to work like 'first click', appropriate data measuring tools need to be in place. The first step, therefore is informing the brands how to gather data. Once that is done, and the correct technology stack, the power of attribution and data driven marketing produces game changing results. 
In this post, I'd discuss some antiquated attribution methods along with the state of art, enterprise-scale, big data, attribution systems. Even if a marketing company or brand decides to choose an old attribution method, I hope that this post will provide some understanding, interpretations and pitfalls for using that system.


## Channel attribution 

Let's start with an example data set, where we have five channels: Social Network, Organic search, Referrals, Paid searches and Direct link. Using these five channels, we'd discuss various attribution models.


### First Click Attribution




### Last Click Attribution

```
## Warning: Ignoring unknown aesthetics: ymax
```

![plot of chunk unnamed-chunk-2](/figure/source/channelAttribution/unnamed-chunk-2-1.png)

### Last non-direct click attribution


```
## Warning: Ignoring unknown aesthetics: ymax
```

![plot of chunk unnamed-chunk-3](/figure/source/channelAttribution/unnamed-chunk-3-1.png)

### Linear attribution


```
## Warning: Ignoring unknown aesthetics: ymax
```

![plot of chunk unnamed-chunk-4](/figure/source/channelAttribution/unnamed-chunk-4-1.png)

### Time decay attribution


```
## Warning: Ignoring unknown aesthetics: ymax
```

![plot of chunk unnamed-chunk-5](/figure/source/channelAttribution/unnamed-chunk-5-1.png)

### Markov chain based attribution


```
## Package:  markovchain
## Version:  0.6.6
## Date:     2017-01-22
## BugReport: http://github.com/spedygiorgio/markovchain/issues
```

```
## Loading required package: eha
```

```
## Loading required package: survival
```

```
## Loading required package: statmod
```

```
## Loading required package: KMsurv
```

![plot of chunk unnamed-chunk-6](/figure/source/channelAttribution/unnamed-chunk-6-1.png)

### Survival Model

![plot of chunk unnamed-chunk-7](/figure/source/channelAttribution/unnamed-chunk-7-1.png)

### Comparison of other models

![plot of chunk unnamed-chunk-8](/figure/source/channelAttribution/unnamed-chunk-8-1.png)

Comparison of other models
========================================================
- Attribution to touch-points

![plot of chunk unnamed-chunk-9](/figure/source/channelAttribution/unnamed-chunk-9-1.png)
