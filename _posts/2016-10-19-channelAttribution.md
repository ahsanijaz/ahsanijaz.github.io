---
layout: post
title: Cross Channel Attribution (Part I)
date: "19/10/2016"
bigimg: /img/ca1.jpg
tags: [data driven marketing, financial engineering]
---



With the advent of data driven and measurement-focused marketing, cross channel attribution has become a hot topic. Briefly, it is used to assign proportional credit to each marketing touch point be it offline or digital that leads to a desired customer action. Therefore, attribution analytics can help the brands to optimize their media and marketing spending while measuring the impact produced by each marketing channel. 
When understood correctly, it provides clear and accurate insights about marketing influence on customers across channels. With this system in place, a marketing budget can be made to create an optimal mix of customer interactions. In short, with cross-channel attribution, marketers can do more with less because they understand their customers better.
Trouble is, that brands routinely underestimate the intricacies involved in creating advanced, enterprise-scale, near real time analytics. In my personal interactions, most of the major brands do not even have a closed loop system about customer interactions and sale points with marketing efforts. Even to get some antiquated methods to work like 'first click', appropriate data measuring tools need to be in place. The first step, therefore is informing the brands how to gather data. Once that is done, and the correct technology stack, the power of attribution and data driven marketing produces game changing results. 
In this post, I'd discuss some antiquated attribution methods along with the state of art, enterprise-scale, big data, attribution systems. Even if a marketing company or brand decides to choose an old attribution method, I hope that this post will provide some understanding, interpretations and pitfalls for using that system.


## Simple multi-channel attribution models

Let's start with an example data set, where we have five channels: Social Network, Organic search, Referrals, Paid searches and Direct link. Using these five channels, we'd discuss various attribution models. 


### First Click Attribution

Some of these models are down right ridiculous. Starting off with frist click attribution. Usually, the customers interact with various channels before conversion (buying something, making transaction). Say, you might see and advertisment on Television, google it up and click on an add offering a deal, and from there ending up buying the product. This 'chain' was started from a TV commercial; in the case of first click attribution, all the credit goes to this first channel. That is first click attribution. Please note that the figure below only depicts that all credit goes to the first channel, and is not representative of how the budget suggestion would look like through first click attribution.

![plot of chunk unnamed-chunk-1](/figure/source/2016-10-19-channelAttribution/unnamed-chunk-1-1.png)

### Last Click Attribution
One of the standard attribution models provided by all web analytics tools. Another ridiculous model, but you need to know of it since it keeps on showing in marketing reports. Like the previous model, instead of giving credit to all the channels involved, it delivers all the credit to the last channel. Ideally, a method should be used to provide contribution to each channel in the conversion process.

![plot of chunk unnamed-chunk-2](/figure/source/2016-10-19-channelAttribution/unnamed-chunk-2-1.png)

### Last non-direct click attribution
The choice of Google analytics is the last non-direct click attribution. That means that anything before direct contact and conversion will get the credit. There is some sound logic behind it. In case of digital market, you'd normally not remember the website and reach that place either through Google search, social media link or some advertisement. Thus, it does not make sense to attribute the conversion to your website where the conversion takes place. In terms of traditional marketing, it won't make sense to provide marketing credit to a local shop making the sale rather than the advertisement that drove the customer towards that sale. 
Although, better than last and first click attribution methods, it still doesn't provide credit to all the channels involved in conversion.

![plot of chunk unnamed-chunk-3](/figure/source/2016-10-19-channelAttribution/unnamed-chunk-3-1.png)

### Linear attribution
Linear attribution gives equal credit to all the channels involved in conversion. This is definitely an improvement over the previous three methods. But, the way these attributions are provided are quite arbitrary. In statistical terms, we have no logical reason to hold a uniform prior over the time from interaction with first channel to conversion.

![plot of chunk unnamed-chunk-4](/figure/source/2016-10-19-channelAttribution/unnamed-chunk-4-1.png)

### Time decay attribution
Definitely an improvement on the linear attribution model, it provides higher weight to channels close to sale as compared to earlier ones. If you need a simple, common sense based method for attribution modeling, choose the time decay attribution method. 

![plot of chunk unnamed-chunk-5](/figure/source/2016-10-19-channelAttribution/unnamed-chunk-5-1.png)

The methods discussed so far are heuristic based and not data driven. In the [next post](https://ahsanijaz.github.io/2016-10-19-ChannelAttribution/), we'll look into two state-of-art methods for attribution modeling that can be scaled at enterprise level. 
