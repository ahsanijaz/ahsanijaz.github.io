---
title       : MapReduce and RDBMS
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



## Distributed File system

> - For very large files (TBs, PBs)
> - Each file is partioned into <color style="color:blue;"> chunks (64MB) </color>
> - Each chunk is replicated several times ($ > 3 $) 
> - Implementations - <color style="color:blue;"> Hadoop file system (HDFS- open source), Google distributed File system (GFS- proprietary) </color> 

---

## Implementation

> - One master node
> - Master partitions file into <color style="color:blue;"> M splits </color> by key
> - Master assigns <color style="color:green;"> workers </color> to the <color style="color:blue;"> M map tasks </color> and keep track of their progress.
> - Workers write output into local disks with <color style="color:blue;"> R regions. </color>
> - Master assigns workers to <color style="color:blue;"> R reduced tasks. </color>
> - Reduce workers read regions from the map worker's local disk.

---

## MapReduce Complete cycle

<img class="center" src= mr.png height=450>

---


## Large-scale Data Processing

> - Many tasks process big data.
> - Want to use hundreds or thousands of CPUs
    - Parallel databases exist - Expensive! Difficult to set up.
> - MapReduce is a lightweight framework, providing:
    - Automatic parallelization and distribution
    - Fault-tolerance
    - I/O scheduling
    - Status and monitoring

---

## Design space for Big data

<img class="center" src= dspace.png height=450>

---


## Parallel query processing

> - Distributed Query (Microsoft SQL server)
     - Rewrite the query as a union of subqueries
     - Workers communicate through standard interfaces 
     - Same as MR, BUT all results are sent back to head node
> - Parallel Query
     - Each operator is implemented with a parallel query
     - Same as MR


---


## Distributed Query


```r
CREATE VIEW SALES AS
SELECT * from janSales
UNION ALL
SELECT * from febSales
UNION ALL
SELECT * from marchSales
UNION ALL
```

---

## Parallel Query

<img class="center" src= parallelQuery.png height=450>

---

## TeraData Example 

```r
SELECT *
    FROM Orders o, Lines i
WHERE o.item = i.item
AND o.date = today()
```

---

## TeraData Example

<img class="center" src= tera1.png height=450>

---

## TeraData Example

<img class="center" src= tera2.png height=450>

---

## MapReduce Extensions

> - Pig 
    - Relational algebra over Hadoop
> - Hive
    - SQL over hadoop
> - Impala
    - SQL over HDFS; builds on HIVE code

---

## MapReduce vs RDBMS

### RDBMS

- Declarative query language (Pig, HIVE)
- Schemas (HIVE)
- Logical data independence
- Indexing (Hbase)
- Algebraic optimization (Pig, HIVE)
- Caching Views
- ACID/Transactions

### MapReduce

- High Scalability ( $>$ 1000 Nodes)
- Fault tolerance

---

## Hadoop vs. RDBMS

- Comparison of 3 systems
  - Hadoop
  - Vertica (column oriented)
  - Oracle  (row oriented)
- Qualitative
  - Programming model, ease of setup, features
- Quantitative
  - Data loading, different types of queries

---

## Grep Task

- Find 3-byte pattern in 100 byte record
  - 1 match per 10,000 records
- Data set:
  - 10 byte unique key, 90 byte value
  - 1TB spread across 25, 50 or 100 nodes
  - 10 billion records
  

---


## Grep task loading results

<img class="center" src= saveHadoop.png height=450>

---

## Grep Task

<img class="center" src= grepExec.png height=450>

---


## Selection and filter task

<img class="center" src= selectFilter.png height=450>

---

## Aggregate tasks

<img class="center" src= aggregate.png height=450>



