---
title: "Events and Objects"
id: 4419707737111
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707737111-Events-and-Objects
updated_at: 2022-07-17T02:06:59Z
---

# Events and Objects

# Events and Objects

The API provides the following events and objects:

## Y

This object is an underlying Logi application script object, automatically
created. It's used in your code to identify the next two events.

## rdCreate

This event fires *before* the Google Map object is created. It has
three properties:

* **id** - Gets the ID of the Google Map object about to be created.
* **mapOptions** - Sets the Google Map's MapOptions object properties,
  ranging from background color to zoom control options. A complete list
  of these is available from Google on their
  [specifications page](https://developers.google.com/maps/documentation/javascript/3.exp/reference#MapOptions).
* **container** - Gets the ID of the internal Division created as a
  container for the Google Map object.

The mapOptions property is the most useful as it allows you to configure
the map in a variety of ways before it's created:

var mapDiv = Y.one('#gmap');  
 mapDiv.on('rdCreate', function(e) {  
 e.mapOptions["scrollwheel"] = false;  
 });
The example code shown above refers to a Google Map element with an
element ID of "gmap". The code configures the map to disable the
mouse scroll wheel (used to zoom in and out) when it's created.

## rdCreated

This event fires *after* the Google Map object is created. It has
four properties:

* **map** - Gets a reference to the newly-created Google Map object.
* **id** - Gets the ID of the newly-created Google Map object.
* **mapOptions** - Gets the Google Map's MapOptions object properties,
  ranging from background color to zoom control options. A complete list
  of these is available from Google on their
  [specifications page](https://developers.google.com/maps/documentation/javascript/3.exp/reference#MapOptions).
* **container** - Gets the ID of the internal division created as a
  container for the Google Map object.

This event and its properties allow you to customize the map after it's
been created:

var mapDiv = Y.one('#gmap');  
 mapDiv.on('rdCreated', function(e) {  
 var latLng = new google.maps.LatLng(38.924622,
-77.216779);  
 var marker = new google.maps.Marker({  
 position: latLng,  
 map: e.map  
 });  
 });
The example code shown above refers to a Google Map element with an
element ID of "gmap". It adds a Map Marker at a specific
location (Logi World HQ) after the map is created, using the
**LatLng** and **Marker** classes from the Google Map API.

var latLng = new
google.maps.LatLng(@Request.LatHQ~, @Request.LngHQ~);  
Of course, the code can be made dynamic through the use of tokens, as
shown above.

## rdGetMapObject()

This Logi function returns a reference to the specified Google Map object
and can be used to customize an existing Google Map based on events
related to the Logi page, such as a user-initiated mouse click. Imagine a
button or link on a page, with Action.JavaScript as its child with this
code:

var myMap = rdGetGMapObject('gmap');  
 var randomNumber = Math.random();  
 var latLng = new google.maps.LatLng(38.924622 + randomNumber, -77.216779 -
randomNumber);  
 var marker = new google.maps.Marker({  
 position: latLng,  
 map: myMap  
 });
The example code shown above refers to a Google Map element with an
element ID of "gmap". It adds a Map Marker at a random location,
using the **LatLng** and **Marker** classes from the Google Map API,
when the button or link is clicked.
