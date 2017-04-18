---
layout: post
title: Cross Channel Attribution (Part II)
date: "19/10/2016"
bigimg: /img/ca1.jpg
tags: [data driven marketing, financial engineering]
---




## Markov chain based attribution

- Transitional probalities by using markov model 
- Check the effect of removal of each touch point
- Attribute touch points according to the lift 

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

