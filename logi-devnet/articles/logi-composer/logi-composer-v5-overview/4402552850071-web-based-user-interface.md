---
title: "Web-Based User Interface"
id: 4402552850071
section: "Logi Composer v5 Overview"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402552850071-Web-Based-User-Interface
updated_at: 2021-09-15T02:22:05Z
---

# Web-Based User Interface

# Web-Based User Interface

Composer provides a single, unified web-based user interface (the Composer UI) for administrators, dashboard developers, analysts and casual users alike. The web application is compatible with modern browsers that support the HTML5 standard for web applications and WebSocket communication protocol.

Because it supports the HTML5 standard, the user interface responsively adjusts to a tablet form factor without loss of functionality. The application will function on a smartphone, however due to the smaller form factor, such devices don't lend themselves well to the out-of-the-box exploratory experience for which Composer was developed. Custom mobile apps can be developed using mobile frameworks such as Ionic or React Native and the Composer JavaScript SDK.

The web browser (or any client application using the Composer JavaScript APIs) is responsible for establishing a two-way WebSocket communication channel between itself and the Composer query engine. The web browser is responsible for keeping the WebSocket connection alive and automatically reconnecting to the query engine when network problems occur.

Messages transmit over WebSockets using the lightweight JSON (JavaScript object notation) file format. There are several message types used by Composer.

| Message Type | Description |
| --- | --- |
| Query messages | Define the query request. Requests can be raw data requests or single or multidimensional data requests that include filters, sorts, and limits. |
| Data messages | Contain the results of a query execution. |
| Metadata messages | Contain information about the query status (progress, error, time window). |
| Control messages | Define control events, such as pause or play. |

The Composer web application delivers unique functionality to the end-user, such as:

* Data Sharpening™ to stream predictive results when working with very large data sets
* Smart loading of visuals and dashboards. Smart loading improves the performance for loading visuals on a dashboard.
* A time bar to simplify time-based analysis
* Data DVR to rewind, play, and fast forward data streams
* Live mode to visualize near real-time data streams
* Highly configurable visuals and dashboards that includes filtering and sorting the data in near real-time
* Search box and facets to maximize performance when connecting to search-enabled data platforms such as Apache Solr and Elasticsearch.

The web application pulls all of these technologies and features together in a “non-blocking” data exploration experience.

There are two ways to understand the non-blocking UI. One is that data loads independently in each visual, so viewing the entire dashboard is not slowed down by the longest running query. The second is that at the same time that data rolls in, users can filter, sort, drill down, reformat, change visual styles, and otherwise manipulate visuals. The ability to interact with visuals while data loads is significant because it is what enables users to engage in speed-of-thought analysis against massive and live data sources. When a user switches direction to explore different data, Composer efficiently cancels previously running queries to conserve computing and network resources.

The value of the Composer non-blocking user experience should not be underestimated. Because many studies suggest that the human attention span for most tasks is less than 10 seconds, it’s important that your users are not stuck staring at a blank screen or a waiting hourglass. True data exploration only happens when users can rapidly and freely decide to explore where the data leads.
