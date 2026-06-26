---
title: "Logi Google Map API"
id: 4406822446999
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822446999-Logi-Google-Map-API
updated_at: 2022-04-06T06:07:47Z
---

# Logi Google Map API

# Logi Google Map API

The Logi Info **Google Map** element allows developers to include the
geo-mapping features of the Google Maps web service in their reports and
provides an opportunity to combine it with their own data to produce
hybrid maps. A JavaScript-based API is available, providing developers
with an opportunity to handle low-level events and customize their maps.

The following topics discuss the Logi Google Map API:

* [Events and Objects](https://devnet.logianalytics.com/hc/en-us/articles/4406817714327-Events-and-Objects#Objects)
* [Example Definition](https://devnet.logianalytics.com/hc/en-us/articles/4406822446103-Example-Definition#Definition)

## About the Logi Google Map API

The Logi Google Map API is a JavaScript-based API that lets you handle
Google Map-related events and objects. It depends on other JavaScript
objects that are automatically created by the standard Logi Engine code.
These objects are clearly identified in the example provided.
The Logi Google Map API extends Logi's Google Map element, letting
developer dynamically configure map features and markers. It's based on
the
[Google Maps JavaScript API v3](https://developers.google.com/maps/documentation/javascript/).
The Logi Google Map API is contained in
rdTemplate\rdGoogleMap\rdGmap.js, which is automatically included in your Logi application when you use
the Google Map element. You *do not* need to include this script file
independently.

You can include the JavaScript code you write that uses Logi Google Map
API calls using the standard elements for that purpose, such as
**Include Script** or **Include Script File**. If you use the
latter, it must be a child of the Body or Report Footer elements, not the
Report (root) or Report Header elements.
