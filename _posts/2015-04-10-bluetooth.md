---
layout: post
title: "Estimating number of people by using bluetooth"
bigimg: /img/peopleCount.png
tags: [confidence intervals, extrapolation]
---

As a thought experiment, I was working on the detection of number of people using Bluetooth visibility. Briefly, I was collecting data on my cellphone by counting the number of visible bluetooth devices while hanging out in some Cafes around Palo Alto. I was also counting the actual number of people in those shops. Thus, a simple extrapolation using these two numbers would provide an extrapolation factor. Assuming that the number of bluetooth devices follow a gaussian distribution, we can provide confidence interval of our extrapolation by looking at the standard deviation of data obtained. In this post, I'm generating psuedo-data to provide such estimates. In the next post, I'll work and show the actual results obtained through real data around Palo Alto. 
The sections that follow look into the confidence intervals by assuming that a certain proportion of population has there bluetooth devices turned on. With that, we provide the observed total number of people and use mean and standard deviations of a binomial distribution. With increasing percentage, our confidence of estimates will increase and margin of error reduce. 


## Bluetooth usage = 10% 



<!-- Table generated in R 3.3.1 by googleVis 0.6.2 package -->
<!-- Sat Apr  8 22:30:50 2017 -->


<!-- jsHeader -->
<script type="text/javascript">
 
// jsData 
function gvisDataTableID71a35f616f3a () {
var data = new google.visualization.DataTable();
var datajson =
[
 [
2,
20,
7,
33
],
[
3,
30,
14,
46
],
[
4,
40,
21,
59
],
[
5,
50,
29,
71
] 
];
data.addColumn('number','devicesFound');
data.addColumn('number','estimateOfPeople');
data.addColumn('number','lowerLimit');
data.addColumn('number','upperLimit');
data.addRows(datajson);
return(data);
}
 
// jsDrawChart
function drawChartTableID71a35f616f3a() {
var data = gvisDataTableID71a35f616f3a();
var options = {};
options["allowHtml"] = true;

    var chart = new google.visualization.Table(
    document.getElementById('TableID71a35f616f3a')
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
callbacks.push(drawChartTableID71a35f616f3a);
})();
function displayChartTableID71a35f616f3a() {
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
<script type="text/javascript" src="https://www.google.com/jsapi?callback=displayChartTableID71a35f616f3a"></script>
 
<!-- divChart -->
  
<div id="TableID71a35f616f3a" 
  style="width: 500; height: automatic;">
</div>

## Bluetooth usage = 20% 



<!-- Table generated in R 3.3.1 by googleVis 0.6.2 package -->
<!-- Sat Apr  8 22:30:50 2017 -->


<!-- jsHeader -->
<script type="text/javascript">
 
// jsData 
function gvisDataTableID71a3fba048f () {
var data = new google.visualization.DataTable();
var datajson =
[
 [
4,
20,
11,
29
],
[
6,
30,
19,
41
],
[
8,
40,
27,
53
],
[
10,
50,
36,
64
] 
];
data.addColumn('number','devicesFound');
data.addColumn('number','estimateOfPeople');
data.addColumn('number','lowerLimit');
data.addColumn('number','upperLimit');
data.addRows(datajson);
return(data);
}
 
// jsDrawChart
function drawChartTableID71a3fba048f() {
var data = gvisDataTableID71a3fba048f();
var options = {};
options["allowHtml"] = true;

    var chart = new google.visualization.Table(
    document.getElementById('TableID71a3fba048f')
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
callbacks.push(drawChartTableID71a3fba048f);
})();
function displayChartTableID71a3fba048f() {
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
<script type="text/javascript" src="https://www.google.com/jsapi?callback=displayChartTableID71a3fba048f"></script>
 
<!-- divChart -->
  
<div id="TableID71a3fba048f" 
  style="width: 500; height: automatic;">
</div>

## Bluetooth usage = 30% 



<!-- Table generated in R 3.3.1 by googleVis 0.6.2 package -->
<!-- Sat Apr  8 22:30:50 2017 -->


<!-- jsHeader -->
<script type="text/javascript">
 
// jsData 
function gvisDataTableID71a348743b47 () {
var data = new google.visualization.DataTable();
var datajson =
[
 [
6,
20,
13,
27
],
[
9,
30,
22,
38
],
[
12,
40,
30,
50
],
[
15,
50,
39,
61
] 
];
data.addColumn('number','devicesFound');
data.addColumn('number','estimateOfPeople');
data.addColumn('number','lowerLimit');
data.addColumn('number','upperLimit');
data.addRows(datajson);
return(data);
}
 
// jsDrawChart
function drawChartTableID71a348743b47() {
var data = gvisDataTableID71a348743b47();
var options = {};
options["allowHtml"] = true;

    var chart = new google.visualization.Table(
    document.getElementById('TableID71a348743b47')
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
callbacks.push(drawChartTableID71a348743b47);
})();
function displayChartTableID71a348743b47() {
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
<script type="text/javascript" src="https://www.google.com/jsapi?callback=displayChartTableID71a348743b47"></script>
 
<!-- divChart -->
  
<div id="TableID71a348743b47" 
  style="width: 500; height: automatic;">
</div>

## Bluetooth usage = 40% 



<!-- Table generated in R 3.3.1 by googleVis 0.6.2 package -->
<!-- Sat Apr  8 22:30:50 2017 -->


<!-- jsHeader -->
<script type="text/javascript">
 
// jsData 
function gvisDataTableID71a36112b405 () {
var data = new google.visualization.DataTable();
var datajson =
[
 [
8,
20,
15,
25
],
[
12,
30,
23,
37
],
[
16,
40,
32,
48
],
[
20,
50,
41,
59
] 
];
data.addColumn('number','devicesFound');
data.addColumn('number','estimateOfPeople');
data.addColumn('number','lowerLimit');
data.addColumn('number','upperLimit');
data.addRows(datajson);
return(data);
}
 
// jsDrawChart
function drawChartTableID71a36112b405() {
var data = gvisDataTableID71a36112b405();
var options = {};
options["allowHtml"] = true;

    var chart = new google.visualization.Table(
    document.getElementById('TableID71a36112b405')
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
callbacks.push(drawChartTableID71a36112b405);
})();
function displayChartTableID71a36112b405() {
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
<script type="text/javascript" src="https://www.google.com/jsapi?callback=displayChartTableID71a36112b405"></script>
 
<!-- divChart -->
  
<div id="TableID71a36112b405" 
  style="width: 500; height: automatic;">
</div>

## Bluetooth usage = 50% 



<!-- Table generated in R 3.3.1 by googleVis 0.6.2 package -->
<!-- Sat Apr  8 22:30:50 2017 -->


<!-- jsHeader -->
<script type="text/javascript">
 
// jsData 
function gvisDataTableID71a332f64407 () {
var data = new google.visualization.DataTable();
var datajson =
[
 [
10,
20,
16,
24
],
[
15,
30,
25,
35
],
[
20,
40,
34,
46
],
[
25,
50,
43,
57
] 
];
data.addColumn('number','devicesFound');
data.addColumn('number','estimateOfPeople');
data.addColumn('number','lowerLimit');
data.addColumn('number','upperLimit');
data.addRows(datajson);
return(data);
}
 
// jsDrawChart
function drawChartTableID71a332f64407() {
var data = gvisDataTableID71a332f64407();
var options = {};
options["allowHtml"] = true;

    var chart = new google.visualization.Table(
    document.getElementById('TableID71a332f64407')
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
callbacks.push(drawChartTableID71a332f64407);
})();
function displayChartTableID71a332f64407() {
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
<script type="text/javascript" src="https://www.google.com/jsapi?callback=displayChartTableID71a332f64407"></script>
 
<!-- divChart -->
  
<div id="TableID71a332f64407" 
  style="width: 500; height: automatic;">
</div>
