---
layout: post
title: "Normalization of location data through different channels"
date: "16/08/2015"
bigimg: /img/locDat.jpg
tags: [geospatial analysis, data normalization]

---



In an exploration of some data on open street maps (OSM), FourSquare, and analysis of the same places on ground showed some
discrepancies between addresses, names and actual location.  In other words, the same place had different names at different data sources and hence a need for normalization is required. 

### Summarize metrics:

Here, I'm listing down the collected data from our sources:




<!-- Table generated in R 3.3.1 by googleVis 0.6.2 package -->
<!-- Tue Apr 18 17:33:58 2017 -->


<!-- jsHeader -->
<script type="text/javascript">
 
// jsData 
function gvisDataTableID18d91b852d81 () {
var data = new google.visualization.DataTable();
var datajson =
[
 [
"4Square",
19184,
19184,
19184,
17847,
11989
],
[
"Open Street Map",
836489,
0,
12448,
10650,
0
] 
];
data.addColumn('string','place_data_source');
data.addColumn('number','totalEntries');
data.addColumn('number','withAddress');
data.addColumn('number','withName');
data.addColumn('number','withUniqueNames');
data.addColumn('number','withRatings');
data.addRows(datajson);
return(data);
}
 
// jsDrawChart
function drawChartTableID18d91b852d81() {
var data = gvisDataTableID18d91b852d81();
var options = {};
options["allowHtml"] = true;
options["page"] = "enable";

    var chart = new google.visualization.Table(
    document.getElementById('TableID18d91b852d81')
    );
    chart.draw(data,options);
    

}
  
 
// jsDisplayChart
(function() {
var pkgs = window.__gvisPackages = window.__gvisPackages || [];
var callbacks = window.__gvisCallbacks = window.__gvisCallbacks || [];
var chartid = "table";
  
// Manually see if chartid is in pkgs (not all browsers support Array.indexOf)
var i, newPackage = true;
for (i = 0; newPackage && i < pkgs.length; i++) {
if (pkgs[i] === chartid)
newPackage = false;
}
if (newPackage)
  pkgs.push(chartid);
  
// Add the drawChart function to the global list of callbacks
callbacks.push(drawChartTableID18d91b852d81);
})();
function displayChartTableID18d91b852d81() {
  var pkgs = window.__gvisPackages = window.__gvisPackages || [];
  var callbacks = window.__gvisCallbacks = window.__gvisCallbacks || [];
  window.clearTimeout(window.__gvisLoad);
  // The timeout is set to 100 because otherwise the container div we are
  // targeting might not be part of the document yet
  window.__gvisLoad = setTimeout(function() {
  var pkgCount = pkgs.length;
  google.load("visualization", "1", { packages:pkgs, callback: function() {
  if (pkgCount != pkgs.length) {
  // Race condition where another setTimeout call snuck in after us; if
  // that call added a package, we must not shift its callback
  return;
}
while (callbacks.length > 0)
callbacks.shift()();
} });
}, 100);
}
 
// jsFooter
</script>
 
<!-- jsChart -->  
<script type="text/javascript" src="https://www.google.com/jsapi?callback=displayChartTableID18d91b852d81"></script>
 
<!-- divChart -->
  
<div id="TableID18d91b852d81" 
  style="width: 500; height: automatic;">
</div>

### Technique Used:

We use three features for merging the data.

1. Location
2. Name Matching
3. Address Matching

A brief summary of utilizing information in each of these fields, along with important chunks of code is explained as follows:

#### Location:

As a first step, we loop over FourSquare location entries to fetch all data within 200 meters of our current fourSquare entry. This is acheived using a query similar to:


```r
query2<- paste0("SELECT *,
ST_Distance(ST_GeomFromText('POINT(",placeFourData$long[i],
" ",placeFourData$lat[i],")',4326),
 place_geometry) as Dist,
 st_asText(st_geometryn(place_geometry,1)) as geom
 from place where
ST_DWithin(ST_GeomFromText('POINT(",placeFourData$long[i],
" ",placeFourData$lat[i],")',4326),place_geometry,",d,")
ORDER BY ST_Distance(ST_GeomFromText('POINT(",placeFourData$long[i],
" ",placeFourData$lat[i],")',4326), place_geometry);")
```

where _d_ is distance in radians, and _placeFourData$long[i]_ , _placeFourData$lat[i]_ is the longitude and lattitude of current fourSquare location. The "order by" statement returns the location closest to our point of interest on top. The distance is also stored in a variable "dist" for further use. A confidence interval depending on the least euclidean

#### Name Matching:

Names in FourSquare are taken as the base for name matching. Each name entry of fourSquare and nearest location places is tokenized, part of speech tagging is done and conjunctions and determiners are removed for comparison part. Optimal string alignment, with a maximum distance of two is used to match each string of name in FourSquare with name in OSM data. A confidence level is calculated by dividing the number of votes recieved by each name in OSM data divided by the length of strings in OSM data. Example of function coded is shown as follows:


```r
FourSquareName <- "The Rose & Crown Pub"
OSMName <- c("Santa Clara County",
             "NA","East Palo Alto",
             "Rose and Crown","Thaiphoon",
             "The Goldsmith") 
print(nameMatch2(FourSquareName,OSMName))
```

```
##        FourSquareName1            osmName combVotes  probName
## 1 The Rose & Crown Pub Santa Clara County         0 0.0000000
## 2 The Rose & Crown Pub                 NA         0 0.0000000
## 3 The Rose & Crown Pub     East Palo Alto         0 0.0000000
## 4 The Rose & Crown Pub     Rose and Crown         2 0.6666667
## 5 The Rose & Crown Pub          Thaiphoon         0 0.0000000
## 6 The Rose & Crown Pub      The Goldsmith         0 0.0000000
```


#### Address Matching:

The third and final metric used for matching FourSquare data with OSM data is looking at the address. The OSM data that contains addresses have there first field as the house number. So, we only take that into account when matching. Since, we are only matching with places that are closely located, therefore we are on the same street with high probability. A psuedo example of this function in action is shown as follows:


```r
OSMAddresses <- c("NA","NA","547 CA,
 United States","NA","NA","543 CA, United States",
 "541 CA, United States",
 "215 CA, United States",
 "538 Ramona Street, CA, United States")
fourSquareAddress <- "547 Emerson St"
addressMatch(fourSquareAddress,OSMAddresses)
```

```
##      FourAddress                      AddressRawMatch probMatch
## 1 547 Emerson St                                   NA 0.0000000
## 2 547 Emerson St                                   NA 0.0000000
## 3 547 Emerson St              547 CA,\n United States 1.0000000
## 4 547 Emerson St                                   NA 0.0000000
## 5 547 Emerson St                                   NA 0.0000000
## 6 547 Emerson St                543 CA, United States 0.3333333
## 7 547 Emerson St                541 CA, United States 0.0000000
## 8 547 Emerson St                215 CA, United States 0.0000000
## 9 547 Emerson St 538 Ramona Street, CA, United States 0.0000000
```



