---
title       : Information retrieval 
subtitle    : 
author      : Ahsan Ijaz
job         : 
# logo        : ebryx-logo.png
framework   : io2012        # {io2012, html5slides, shower, dzslides, ...}
highlighter : highlight.js  # {highlight.js, prettify, highlight}
hitheme     : tomorrow   # 
# url:
  # lib: ../../libraries
  # assets: /home/ahsan/Personal/Workshop Machine learning/Workshop1 
widgets     : [mathjax]            # {mathjax, quiz, bootstrap}
mode        : selfcontained # {standalone, draft}
embed : TRUE
---




## Information retreival: Applications 

<img class="center" src= irApps.png height = 400>

---

## Document retrieval

- Currently reading an article

<img class="center" src= articleRead.png  height=400>

---

## Document retrieval

- Currently reading an article
- Goal: Want to find an article similar to that one

<img class="center" src= articleRead.png  height=400>

---

## Document retrieval

> - How do we measure similarity?
> - How do we search over articles?

---

## Retrieval as nearest neighbor search

- Organize all articles by similarity of text

<img class="center" src= query1ar.png  height=400>

---

### Compute distances with all other articles

- Organize all articles by similarity of text

<img class="center" src= computeDistance.png  height=400>

---

### Retrieve 'nearest neighbor'

- Organize all articles by similarity of text

<img class="center" src= nn.png  height=400>

---

### Retrieve set of nearest neighbors

- Organize all articles by similarity of text

<img class="center" src= setNN.png  height=400>

---

### Elements of NN search

- Item (e.g., doc) representation $x_q$ 
- Measure of distance between items :
$$ \xi = \textit{distance}(x_i, x_q) $$ 


---

## Document representation

---

### Word count document representation

Bag of words model
- Igonore order of words
- Count # of instances of each word in vocabulary

<img class="center" src= repDoc.png  height=300>

Sample sentence with matrix: 


---

### Issues with word counts - Rare words

- Common words in doc: "the", "player", "field",...
- Dominate rare words like: "cricket", "Shane Watson"

<img class="center" src= repDoc.png  height=300>

---

### TF-IDF document representation 

- Emphasizes important words

     - Appears frequently in document (common locally)
     - Term frequency = Word Count

- Appears rarely in corpus (rare globally)

$$ \textit{Inverse doc frequency} = \log\frac{\textit{#docs}}{1 + \textit{#docs using the word}} $$

> - <center> tf*idf </center>

---

## IDF function

<div class="rimage center"><img src="fig/unnamed-chunk-1-1.png" title="plot of chunk unnamed-chunk-1" alt="plot of chunk unnamed-chunk-1" class="plot" /></div>

---


## Distance metrics

Notion of closeness?

- Euclidean distance:

$$ \textit{distance}(x_i,x_q) =  |x_i - x_q| $$

---


### Weighting different features

- Some features might be more important than others
- Weighing features in distance metrics

<img class="center" src= impFeatures.png  height=200>

---

### Scaled euclidean distance

- Weight on each feature
- Setting weights as zero or one is same as feature selection

$$ \textit{distance}(x_i,x_q) = \sqrt{(a_1(x_i[1]-x_q[1])^2+\ldots+a_d(x_i[d]-x_q[d])^2))} $$

---


### Inner product similarity

<img class="center" src= cos1.png  height=400>

---

### Inner product similarity

<img class="center" src= cos2.png  height=400>

---


### Cosine similarity (Normalized inner product)

$$ \frac{\mathbf{x}_i^{T}\mathbf{x}_q}{\|x_i\|\|x_q\|}  $$

---

### Unnormalized case

<img class="center" src= normalizeDouble.png  height=400>

---


### Normalized case

<img class="center" src= normalizedCase.png  height=400>

---

### Undesired case of normalization

<img class="center" src= undersiredNormalize.png height=400>
