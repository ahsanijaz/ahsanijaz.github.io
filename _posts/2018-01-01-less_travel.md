---
layout: post
title: A less trodden road to data science (Part I) 
date: "04/09/2018"
tags: [Workshops, Data Science]
image: /img/scream.jpg
---

Internet is replete with posts on 'how to become a data scientist'. Unfortunately, I'm also adding a post on this topic. The breadth of knowledge expected of a practicing data scientist can be quite daunting. However, one can limit the depth in some of these skills. 
Here, I'd put together the bare minimum resources that a data scientist should go through. I'll attempt to provide the resources needed to sharpen each of the needed skill sets and how to approach the learning path. 
Data Scientist role has morphed into a concoction of skill sets. What follows is a catalog of resources divided under different skill sets. 

# Mathematical Background
There is no way around it! You need strong mathematics to be a data scientist. I usually start the interview process by asking the candidates to draw equations of commonly used functions ($$\exp(-x)$$, $$\cos(kx)$$, $$sin(kx)$$ $$\log_{k}(x),...$$). Why is this needed? Once you start on the machine learning journey, you can't go around without sigmoid functions, trend analysis, radial basis kernels and estimators using log scale. Therefore, it is important to familiarize yourself with geometry of these functions:

* [An intuition of exponential functions](http://setosa.io/ev/exponentiation/){:target="_blank"}
* [sin and cos functions](http://setosa.io/ev/sine-and-cosine/){:target="_blank"}
* [Common mathematical functions](https://www.mathsisfun.com/sets/functions-common.html){:target="_blank"}
* [Activation functions in deep learning](https://www.learnopencv.com/understanding-activation-functions-in-deep-learning/){:target="_blank"}

## Calculus review
Since, most of the machine learning models require a geometric interpretation, I'd recommend to create a geometric intuition of mathematical concepts as well. Here, the suggested resources are provided since the explanations are provided within a geometric framework. In the links that follow, explanations are provided that help in visualizing the derivatives; critical points and using these to plot lines. You'd see that this interpretation will help you to create a deeper appreciation of optimization algorithms like **gradient descent, RMSprop and stochastic gradient descent**:

* [The Shape Of A Graph](http://tutorial.math.lamar.edu/Classes/CalcI/ShapeofGraphPtI.aspx){:target="_blank"}
* [The Shape Of A Graph (Part 2)](http://tutorial.math.lamar.edu/Classes/CalcI/ShapeofGraphPtII.aspx){:target="_blank"}.

Also, don't forget to review the chain rule needed for back propagation algorithms:

* [Chain Rule](http://tutorial.math.lamar.edu/Classes/CalcIII/ChainRule.aspx){:target="_blank"}.

What follows is an article of using integrals to compute areas. I find this interpretation important when working on **Monte Carlo simulations**: 

* [Area between curves](http://tutorial.math.lamar.edu/Classes/CalcI/AreaBetweenCurves.aspx){:target="_blank"}
* [Volumes using integration](http://tutorial.math.lamar.edu/Classes/CalcIII/TripleIntegrals.aspx){:target="_blank"}.

Here is another article that discusses integration as area and can more easily be related to **dot product** (mother of all machine learning and feature engineering).

* [Integration as area](http://tutorial.math.lamar.edu/Classes/CalcI/AreaProblem.aspx){:target="_blank"}

Finally, it is important to understand the interplay of integration and probability distributions:

* [Probability density function](http://tutorial.math.lamar.edu/Classes/CalcII/Probability.aspx){:target="_blank"}

If it is easier for you to follow videos instead of reading, here's the link to some exceptional visually explained lectures on Calculus: [Cal lectures](https://www.youtube.com/watch?v=WUvTyaaNkzM&list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr){:target="_blank"}. 

## Linear Algebra
Linear algebra is the core of feature engineering; basis selection; dimensionality reduction; matrix factorization; spectral clustering; deep learning and generalized linear models to name some. Almost all the algorithms have a linear algebra interpretation to them. Therefore, it is the backbone of Machine learning.
I haven't found a better resource than Gilbert Strang's [lecture series](https://www.youtube.com/watch?v=ZK3O402wf1c&list=PL49CF3715CB9EF31D){:target="_blank"} on linear algebra. It can be arduous to follow through all of them, but it will be highly rewarding if you do. If you just want the essentials for Machine Learning from the complete course, take the following of his lectures:

* [Lec 6: Column space and null space](https://www.youtube.com/watch?v=8o5Cmfpeo6g){:target="_blank"}
* [Lec 9: Independence, basis and Dimension](https://www.youtube.com/watch?v=yjBerM5jWsc){:target="_blank"}
* [Lec 14: Orthogonal vectors](https://www.youtube.com/watch?v=YzZUIYRCE38){:target="_blank"}
* [Lec 15: Projection into subspaces](https://www.youtube.com/watch?v=Y_Ac6KiQ1t0){:target="_blank"}
* [Lec 16: Projection matrices and least squares](https://www.youtube.com/watch?v=osh80YCg_GM){:target="_blank"}
* [Lec 21: Eigenvalues and Eigenvector](https://www.youtube.com/watch?v=lXNXrLcoerU){:target="_blank"}
* [Lec 29: Singular Value Decomposition](https://www.youtube.com/watch?v=Nx0lRBaXoz4){:target="_blank"}
* [Lec 31: Change of basis](https://www.youtube.com/watch?v=vGkn-3NFGck){:target="_blank"}

The [mathematical background](https://www.deeplearningbook.org/contents/linear_algebra.html){:target="_blank"} provided by Ian Goodfellow is quite thorough although somewhat dry. It is a good review nevertheless, so referring it over here. In case you are taking the selected lectures only, do go through this small series of [linear algebra lectures](https://www.youtube.com/watch?v=fNk_zzaMoSs&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab){:target="_blank"} before embarking on the selected lectures. It is one of the best visualization explanation lecture series that I've come across.

Finally, these are some beautiful javascript visualizations to understand eigenvalues, eigenvectors, PCA and least squares.

* [Eigenvectors and eigenvalues](http://setosa.io/ev/eigenvectors-and-eigenvalues/){:target="_blank"}
* [Principal Component Analysis](http://setosa.io/ev/principal-component-analysis/){:target="_blank"}
* [Least Squares Regression](http://setosa.io/ev/ordinary-least-squares-regression/){:target="_blank"}

## Probability and Statistics
Read the first two parts of [Larry Wasserman's All of Statistics](https://www.ic.unicamp.br/~wainer/cursos/1s2013/ml/livro.pdf){:target="_blank"} (you can skip Chapter 5,6, 12 and 13). In addition to that, do look through the following articles:

* [Conditional Probability](http://setosa.io/conditional/){:target="_blank"}
* [Monty Hall Problem](http://blog.vctr.me/monty-hall/){:target="_blank"}
* [Markov Chains](http://setosa.io/blog/2014/07/26/markov-chains/index.html){:target="_blank"}
* [Central limit theorem](http://blog.vctr.me/posts/central-limit-theorem.html){:target="_blank"}

# Programming

The usual candidates for Data Science programming languages are Python, R and Scala. As this post is directed towards industry folks, my recommendation would be to go with Python as your primary language. Python is already used by many organizations and is a complete production ready programming language. Integration is also easier as it has good support of Web Frameworks and the larger engineering environment. Furthermore, TensorFlow provides a rich environment for production ready machine learning deployments and it has good high level API support of Python. PyTorch (albeit a bit behind in terms of production grade pipelines) is also written in Python. Also, if you'd look into Cloud Deployment solutions (AWS and GCP), Python support is far more than that of R (except for Azure). 

You might use R in the following cases:

* You have small data sets and need to make beautiful visualizations.
* You are working on a cutting edge statistical problem; As statistics research community works heavily on R, it is easier to find R packages of recent papers as compared to that of Python implementations.
* You are working purely on a research problem; in my experience, it is faster to write a machine learning pipeline and prototyping using R as compared to Python.

A final note on Statistical packages; I've started working on TensorFlow and especially [Edward2](https://medium.com/tensorflow/introducing-tensorflow-probability-dca4c304e245){:target="_blank"} programming language for statistical computation. You can write Bayesian models, MCMC problems, variational approximation methods and trainable distributions. 
There are numerous online resources available for learning Python. I'd suggest to develop of thorough understanding of data structures and algorithms in Python instead of diving directly into the world of 'dataframes' and 'scikit-learn'.
[This]((https://runestone.academy/runestone/static/pythonds/index.html){:target="_blank"}) free online book provides a great resource and is replete with excellent examples on data structures and algorithms. I'd suggest to do the first seven chapters with all the sample problems: [Problem solving with algorithms and data structures](https://runestone.academy/runestone/static/pythonds/index.html){:target="_blank"}.

Finally, I cannot stress enough to consistently sharpen your programming skills through practice. [LeetCode](https://leetcode.com){:target="_blank"} and [Coding games](https://www.codingame.com/start){:target="_blank"} are great platforms that provide interesting programming problems and games to solve; so get in a habit of solving these programming problems. 

# Data Engineering
This might be a digression from pure data science. At best, you'd need a high level knowledge of data engineering pipelines so that it is easier for you to integrate your work with real time, big data systems in a secure manner. There is no alternate to real world experience; but to get the basic knowledge on data engineering, I'd suggest to take one of these data engineering certifications and follow the course work needed for that. Preparing for any one of these will give you significant understanding of the state of art technologies and infrastructure needed for data engineering pipelines. 

* [Google Cloud Certified Data Engineer](https://cloud.google.com/certification/data-engineer){:target="_blank"}
* [AWS Certified Big Data – Specialty](https://aws.amazon.com/certification/certified-big-data-specialty/){:target="_blank"}
* [CCP Data Engineer](https://www.cloudera.com/more/training/certification/ccp-data-engineer.html){:target="_blank"}

I'd recommend the CCP certification if most of your work is on-premise systems. Otherwise, both AWS and GCP certifications are equally challenging and rewarding. Once certified, you'd know how to build and maintain databases; analyze data to enable machine learning; and most importantly, design for reliability, security and compliance. 

### Google Cloud Certified Data Engineer

As I've only done the GCP certification, what follows are some useful resources for it. Start off with the five course [Data Engineering specialization](https://www.coursera.org/specializations/gcp-data-machine-learning){:target="_blank"} on Coursera. There is no need to give it too much time; play around with Qwiklab links that you find personally interesting. Other than that, the key takeaway should be learning about all the major GCP components for Data Engineering. 

* [Data lifecycle on GCP](https://cloud.google.com/solutions/data-lifecycle-cloud-platform){:target="_blank"}
* [Transferring Big DataSets to cloud Platform](https://cloud.google.com/solutions/transferring-big-data-sets-to-gcp){:target="_blank"}
* [BigQuery Basics](https://cloud.google.com/solutions/bigquery-data-warehouse){:target="_blank"}
* [BigQuery Cost optimization](https://cloud.google.com/bigquery/docs/best-practices-costs){:target="_blank"}
* [BigQuery Performance](https://cloud.google.com/bigquery/docs/best-practices-performance-overview){:target="_blank"}
* [BigQuery Storage](https://cloud.google.com/bigquery/docs/best-practices-storage){:target="_blank"}
* [BigQuery access control](https://cloud.google.com/bigquery/docs/access-control){:target="_blank"}
* [BigQuery nested and repeated columns](https://cloud.google.com/bigquery/docs/nested-repeated){:target="_blank"}
* [BigQuery streaming inserts](https://cloud.google.com/blog/products/gcp/life-of-a-bigquery-streaming-insert){:target="_blank"}
* [Authorized Views in BigQuery](https://cloud.google.com/bigquery/docs/share-access-views){:target="_blank"}
* [Query plan explanation](https://cloud.google.com/bigquery/query-plan-explanation){:target="_blank"}
* [Handling sensitive Data for machine learning](https://cloud.google.com/solutions/sensitive-data-and-ml-datasets){:target="_blank"}
* [Why Quizlet choose GCP](https://quizlet.com/blog/whats-the-best-cloud-probably-gcp/){:target="_blank"}
* [Large Scale Ingestion](https://cloud.google.com/solutions/architecture/optimized-large-scale-analytics-ingestion){:target="_blank"}
* [Financial Time Series analysis](https://cloud.google.com/solutions/correlating-time-series-dataflow){:target="_blank"}
* [Real Time Processing IOT](https://cloud.google.com/solutions/architecture/real-time-stream-processing-iot){:target="_blank"}
* [Processing Logs at Scale using DataFlow](https://cloud.google.com/solutions/processing-logs-at-scale-using-dataflow){:target="_blank"}
* [Transitioning from Data Warehousing in Teradata to GCP Big Data Services](https://cloud.google.com/solutions/teradata-to-gcp){:target="_blank"}
* [Financial Time Series on GCP](https://cloud.google.com/solutions/time-series/bigquery-financial-forex){:target="_blank"}
* [Encryption at rest](https://cloud.google.com/security/encryption-at-rest/){:target="_blank"}
* [Encryption in transit](https://cloud.google.com/security/encryption-in-transit/){:target="_blank"}
* [Best Practices for datastore](https://cloud.google.com/datastore/docs/best-practices){:target="_blank"}
* [Cloud DataFlow Use Cases](https://cloud.google.com/blog/big-data/2017/06/guide-to-common-cloud-dataflow-use-case-patterns-part-1){:target="_blank"}
* [Cloud Dataflow use cases part 2](https://cloud.google.com/blog/big-data/2017/08/guide-to-common-cloud-dataflow-use-case-patterns-part-2){:target="_blank"}
* [12 Myths regarding BigQuery](https://cloud.google.com/blog/big-data/2017/12/busting-12-myths-about-bigquery){:target="_blank"}
* [Bigtable overview](https://cloud.google.com/bigtable/docs/overview){:target="_blank"}
* [Bigtable schema design](https://cloud.google.com/bigtable/docs/schema-design){:target="_blank"}
* [Bigtable performance optimization](https://cloud.google.com/bigtable/docs/performance){:target="_blank"}
* [Bigtable time series schema design](https://cloud.google.com/bigtable/docs/schema-design-time-series){:target="_blank"}
* [Bigtable performance](https://cloud.google.com/bigtable/docs/performance){:target="_blank"}
* [Choosing between SSD and HDD for Bigtable](https://cloud.google.com/bigtable/docs/choosing-ssd-hdd){:target="_blank"}
* [Apache beam programming guide](https://beam.apache.org/documentation/programming-guide/){:target="_blank"}
* [Streaming 101](https://www.oreilly.com/ideas/the-world-beyond-batch-streaming-101){:target="_blank"}
* [Steaming 102](https://www.oreilly.com/ideas/the-world-beyond-batch-streaming-102){:target="_blank"}
* [Using cloud dataprep and cloud ml in a unified timeline](https://cloud.google.com/blog/big-data/2017/11/google-cloud-provides-a-unified-streamlined-way-to-execute-your-ml-strategy){:target="_blank"}
* [Spotify's Event delivery](https://labs.spotify.com/2016/02/25/spotifys-event-delivery-the-road-to-the-cloud-part-i/){:target="_blank"}
* [Data Science on the Google Cloud Platform](http://shop.oreilly.com/product/0636920057628.do){:target="_blank"}

### Big Data Paradigm
I've suggested one of the data engineering certification since most of the components used by one of the cloud providers have equivalent services offered by other cloud providers. What follows is a table providing the mapping of these services:

|Data Engineering Product|AWS|GCP|Azure|On-premise
|---|:---:|:---:|:---:|:---:|
|Object Storage|Amazon Simple Storage Service|Cloud Storage|Azure Blob Storage|HDFS|
|Block Storage|Amazon Elastic Block Store|Persistent Disk|Disk Storage|Hard disks|
|File Storage|Amazon Elastic File System|Cloud Filestore|Azure File Storage|HDFS|
|RDBMS|Amazon Relational Database Service, Amazon Aurora|Cloud SQL, Cloud Spanner|SQL Database|PostgreSQL|
|Reduced-availability Storage|Amazon S3 Standard-Infrequent Access, Amazon S3 One Zone-Infrequent Access|Cloud Storage Nearline|Azure Cool Blob Storage|HDFS|
|Archival Storage|Amazon Glacier|Cloud Storage Coldline|Azure Archive Blob Storage|HDFS|
|NoSQL: Key-value|Amazon DynamoDB|Cloud Datastore, Cloud Bigtable|Table Storage|HBase/Cassandra|
|NoSQL: Indexed|Amazon SimpleDB|Cloud Datastore|Cosmos DB|MongoDB|
|Batch Data Processing|Amazon Elastic MapReduce, AWS Batch|Cloud Dataproc, Cloud Dataflow|HDInsight, Batch|Hadoop/Spark|
|Stream Data Processing|Amazon Kinesis|Cloud Dataflow|Stream Analytics|Apache Beam/Spark stream|
|Stream Data Ingest|Amazon Kinesis|Cloud Pub/Sub|Event Hubs, Service Bus|Kafka|
|Analytics|Amazon Redshift, Amazon Athena|BigQuery|Data Lake Analytics, Data Lake Store|Kudu/GreenPlum|
|Workflow Orchestration|Amazon Data Pipeline, AWS Glue|Cloud Composer||Apache AirFlow|
|Monitoring|Amazon CloudWatch|StackDriver Monitoring|Application Insights|Elastic Search/Solr|
|Fully Managed ML|Amazon SageMaker|Cloud Machine Learning Engine|ML Studio|KubeFlow/Seldon.io|

In addition to this, I'd suggest to take the first course of the specialization [Data Science at Scale](https://www.coursera.org/specializations/data-science){:target="_blank"} to get a cursory understanding of Hadoop, Spark and big data design space. 

# Machine Learning
For machine learning, I'll highly recommend taking the Machine learning specialization at Coursera. It is a four course specialization that touches on all the important topics. The first course will give an overview of ML techniques and use cases. The second course will have you  implement regression, gradient descent, modifying it for ridge and lasso, feature selection and introduction to kernel regression. The third course will have implementation exercises on logistic regression, maximum likelihood, regularization, decision trees, boosting and scaling. While implementing these methods, you'd get to know quite a lot about different optimization techniques and machine learning scalability. The final course of the specialization will start from topics of information retrieval and what similarity metrics are suitable depending on use cases. It will follow with implementation details on KD-trees and locality sensitive hashing. Next section will address K-means, K-means++ and its implementation using MapReduce. This will be followed with Gaussian mixture models and expectation maximization techniques. The next week will cover Latent Dirichlet Allocation model and Gibbs Sampling. The final week will cover hierarchical clustering. Just as previous courses, you'll have to implement all of these algorithms. This is not an easy specialization and will require considerable time and attention to complete but it stands out as one of the best machine learning specialization out there. The link is given below:

* [Machine learning specialization](https://www.coursera.org/specializations/machine-learning){:target="_blank"}

On parallel to this specialization, you can read ["An introduction to statistical learning with applications in R"](https://www-bcf.usc.edu/~gareth/ISL/ISLR%20First%20Printing.pdf){:target="_blank"}. Please read it thoroughly as it is an easy to read book that covers machine learning from a statistical perspective and covers a few topics not covered in ML specialization (confidence intervals in Regression; splines; SVM; QDA and linear discriminant analysis; resampling methods and Random Forests to name a few). As it is an introductory book, it is imperative to know each and every concept discussed in this. The good part is, it won't take more than a week to finish this book.

# Deep Learning
If you want to get a decent introduction to deep learning, [Deep Learning specialization](https://www.coursera.org/specializations/deep-learning){:target="_blank"} by Andrew Ng is the best resource out there. The exercises are provided so that you get to implement the key components of Deep Learning models (the code snippets are quite simple and the comments almost provide the needed code so it will be quite easy to complete these exercises). The second and third course of the specialization covers practical issues as well: including hyperparameter tuning; weight initialization; faster optimization algorithms; gradient checking; vanishing and exploding gradients and batch normalization. Once you've completed this specialization, I'd highly recommend taking [Advanced Machine Learning with TensorFlow on Google Cloud Platform Specialization](https://www.coursera.org/specializations/advanced-machine-learning-tensorflow-gcp){:target="_blank"}. This specialization covers the practical aspects of Machine learning quite well including machine learning Devops. It also covers aspects of hybrid deployments (Kubeflow); adaptable machine learning; use of managed services; TPU/GPU/CPU. If you just want the essential out of this specialization that generalizes to more than just the GCP, take the second course: [Production Machine Learning Systems](https://www.coursera.org/learn/gcp-production-ml-systems){:target="_blank"}. I've found that this specialization has provided better advice on practical aspects of deep learning as compared to Andrew Ng's Deep learning specialization. 


## Machine learning frameworks
For industry and production ready systems, go with TensorFlow if you are programming in Python; [H2o](https://www.h2o.ai){:target="_blank"} if you are working in R. [TensorFlow](http://tensorflow.org){:target="_blank"}, is by far, the best machine learning framework to go into production; whether you are doing cloud or on-premise deployment. Its portability means that the models can be deployed on any operating system and computing device. Whenever you are judging a machine learning platform, you need to mindful about the following watchpoints:

1. Does it provide capability of fast prototyping?
2. Does the framework provide model check pointing?
3. Can it handle out of memory datasets?
4. Does it provide a good method for monitoring training and validation errors during train sessions?
5. Can it provide distributed training?
6. Does it provide a method for hyperparameter tuning?
7. Does it provide a framework for serving predictions from a trained model?

TensorFlow resolves all of these watch points and is therefore, the most production ready machine learning framework in market.
