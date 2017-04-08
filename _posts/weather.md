---
title: Mining Severe weather conditions from the U.S. National Oceanic and Atmospheric
  Administration’s (NOAA) storm Database
author: "Ahsan Ijaz"
date: "24/01/2015"
output: pdf_document
---
## Synopsis
In this assignment, we look at the data of U.S. National Oceanic and Atmospheric Administration's storm database to see which of the hazards cause the most property damage and is cause most fatalites. Some exploratory analysis is done with plots used to answer the questions. According to analysis, the most hazardous event for human life is Tornados followed by excessive heat and flash floods whereas floods cause the most property and crop damage followed by hurricane, tornado and storm surge.

## Data Processing

Loading required libraries for analysis:

```r
library(dplyr)
```

```
## 
## Attaching package: 'dplyr'
```

```
## The following objects are masked from 'package:stats':
## 
##     filter, lag
```

```
## The following objects are masked from 'package:base':
## 
##     intersect, setdiff, setequal, union
```

```r
library(ggplot2)
library(reshape2)
```


Reading the data as a data frame:


```r
NOAAdata <- read.csv("/home/ahsan/Downloads/repdata_data_StormData.csv")
```

```
## Warning in file(file, "rt"): cannot open file '/home/ahsan/Downloads/
## repdata_data_StormData.csv': No such file or directory
```

```
## Error in file(file, "rt"): cannot open the connection
```
To answer our questions, we look at the data to see which columns are relavant for our analysis:

```r
str(NOAAdata)
```

```
## Error in str(NOAAdata): object 'NOAAdata' not found
```
Fromn the documentation, we can see that the study can be limited using columns EVTYPE, PROPDMG, PROPDMGEXP, FATALITIES,INJURIES, CROPDMG, CROPDMGEXP. So subsetting the data:


```r
NOAAdata.rel <- NOAAdata[,c("EVTYPE", "PROPDMG", "PROPDMGEXP", "FATALITIES","INJURIES", "CROPDMG", "CROPDMGEXP")]
```

```
## Error in eval(expr, envir, enclos): object 'NOAAdata' not found
```

Now we would like to see which event type causes most property and crop damage. The levels in PROPDMGEXP and CROPDMGEXP are given as:

```r
levels(NOAAdata.rel$PROPDMGEXP)
```

```
## Error in levels(NOAAdata.rel$PROPDMGEXP): object 'NOAAdata.rel' not found
```

```r
levels(NOAAdata.rel$CROPDMGEXP)
```

```
## Error in levels(NOAAdata.rel$CROPDMGEXP): object 'NOAAdata.rel' not found
```
The documentation doesn't specify anything about levels "-","+","0-8" so they would be removed from the analysis. Since some levels contain either small or capital, for consistency, all the levels of these two columns are changed into capital letters. This is done as follows:


```r
NOAAdata.rel$CROPDMGEXP <- as.factor(toupper(NOAAdata.rel$CROPDMGEXP))
```

```
## Error in toupper(NOAAdata.rel$CROPDMGEXP): object 'NOAAdata.rel' not found
```

```r
NOAAdata.rel$PROPDMGEXP <- as.factor(toupper(NOAAdata.rel$PROPDMGEXP))
```

```
## Error in toupper(NOAAdata.rel$PROPDMGEXP): object 'NOAAdata.rel' not found
```

```r
NOAAdata.rel$CROPDMG[as.character(NOAAdata.rel$CROPDMGEXP) %in% c("0","1","2","3","4","5","6","7","8","-"," ","?")] <- 0
```

```
## Error in NOAAdata.rel$CROPDMG[as.character(NOAAdata.rel$CROPDMGEXP) %in% : object 'NOAAdata.rel' not found
```

```r
NOAAdata.rel$PROPDMG[as.character(NOAAdata.rel$PROPDMGEXP) %in% c("0","1","2","3","4","5","6","7","8","-"," ","?")] <- 0
```

```
## Error in NOAAdata.rel$PROPDMG[as.character(NOAAdata.rel$PROPDMGEXP) %in% : object 'NOAAdata.rel' not found
```

As per documentation, H will be translated as hundred, K as thousand, M as million and B as billion in the PROPDMGEXP and CROPDMGEXP to be multiplied with relevant variables. 


```r
NOAAdata.rel$PROPDMG[NOAAdata.rel$PROPDMGEXP == "B"] <- NOAAdata.rel$PROPDMG[NOAAdata.rel$PROPDMGEXP == "B"]*10^9
```

```
## Error in eval(expr, envir, enclos): object 'NOAAdata.rel' not found
```

```r
NOAAdata.rel$PROPDMG[NOAAdata.rel$PROPDMGEXP == "M"] <- NOAAdata.rel$PROPDMG[NOAAdata.rel$PROPDMGEXP == "M"]*10^6
```

```
## Error in eval(expr, envir, enclos): object 'NOAAdata.rel' not found
```

```r
NOAAdata.rel$PROPDMG[NOAAdata.rel$PROPDMGEXP == "K"] <- NOAAdata.rel$PROPDMG[NOAAdata.rel$PROPDMGEXP == "K"]*1000
```

```
## Error in eval(expr, envir, enclos): object 'NOAAdata.rel' not found
```

```r
NOAAdata.rel$PROPDMG[NOAAdata.rel$PROPDMGEXP == "H"] <- NOAAdata.rel$PROPDMG[NOAAdata.rel$PROPDMGEXP == "H"]*100
```

```
## Error in eval(expr, envir, enclos): object 'NOAAdata.rel' not found
```

```r
NOAAdata.rel$CROPDMG[NOAAdata.rel$CROPDMGEXP == "B"] <- NOAAdata.rel$CROPDMG[NOAAdata.rel$CROPDMGEXP == "B"]*10^9
```

```
## Error in eval(expr, envir, enclos): object 'NOAAdata.rel' not found
```

```r
NOAAdata.rel$CROPDMG[NOAAdata.rel$CROPDMGEXP == "M"] <- NOAAdata.rel$CROPDMG[NOAAdata.rel$CROPDMGEXP == "M"]*10^6
```

```
## Error in eval(expr, envir, enclos): object 'NOAAdata.rel' not found
```

```r
NOAAdata.rel$CROPDMG[NOAAdata.rel$CROPDMGEXP == "K"] <- NOAAdata.rel$CROPDMG[NOAAdata.rel$CROPDMGEXP == "K"]*1000
```

```
## Error in eval(expr, envir, enclos): object 'NOAAdata.rel' not found
```

```r
NOAAdata.rel$CROPDMG[NOAAdata.rel$CROPDMGEXP == "H"] <- NOAAdata.rel$CROPDMG[NOAAdata.rel$CROPDMGEXP == "H"]*100
```

```
## Error in eval(expr, envir, enclos): object 'NOAAdata.rel' not found
```

Here we are grouping data in formats that can be used to plot the final results:

```r
NOAAdata.rel.arranged <- NOAAdata.rel %>% 
  group_by(EVTYPE) %>%
  summarise(Fatalities = sum(FATALITIES),
            Injuries = sum(INJURIES),TotalDamage = sum(CROPDMG)+ sum(PROPDMG))
```

```
## Error in eval(expr, envir, enclos): object 'NOAAdata.rel' not found
```

```r
noaaFatal <- NOAAdata.rel.arranged %>%
  select(Fatalities,EVTYPE,Injuries) %>%
  arrange(desc(Fatalities))
```

```
## Error in eval(expr, envir, enclos): object 'NOAAdata.rel.arranged' not found
```

```r
noaaFatal<- head(noaaFatal)
```

```
## Error in head(noaaFatal): object 'noaaFatal' not found
```

```r
noaaFatal <- melt(noaaFatal,id.vars = c("EVTYPE"))
```

```
## Error in melt(noaaFatal, id.vars = c("EVTYPE")): object 'noaaFatal' not found
```

```r
noaaFatal$variable<-as.factor(noaaFatal$variable)
```

```
## Error in is.factor(x): object 'noaaFatal' not found
```

```r
noaaDamages <- NOAAdata.rel.arranged %>%
  select(TotalDamage,EVTYPE) %>%
  arrange(desc(TotalDamage))
```

```
## Error in eval(expr, envir, enclos): object 'NOAAdata.rel.arranged' not found
```

```r
noaaDamages <- head(noaaDamages)
```

```
## Error in head(noaaDamages): object 'noaaDamages' not found
```

## Results

The highest fatalities and injuries caused by disasters is shown in figure below:

```r
ggplot(noaaFatal,aes(x = EVTYPE,y = value,fill=EVTYPE))+geom_bar(stat="identity") + facet_grid(.~variable) + xlab("Event Type") + ylab("") + ggtitle("Highest Fatalities and Injuries caused by Disaster") + coord_flip()
```

```
## Error in ggplot(noaaFatal, aes(x = EVTYPE, y = value, fill = EVTYPE)): object 'noaaFatal' not found
```

The highest property damage caused by disasters is shown in figure below:

```r
ggplot(noaaDamages,aes(x = EVTYPE,y = TotalDamage,fill=EVTYPE))+geom_bar(stat="identity") + xlab("Event Type") + ylab("") + ggtitle("Highest total property and crop damage caused by Disaster") + coord_flip()
```

```
## Error in ggplot(noaaDamages, aes(x = EVTYPE, y = TotalDamage, fill = EVTYPE)): object 'noaaDamages' not found
```
