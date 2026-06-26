---
title: "Listening to Other Query Events"
id: 34932700136717
section: "Composer 25 Developer Tools"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932700136717-Listening-to-Other-Query-Events
updated_at: 2026-05-26T22:06:20Z
---

# Listening to Other Query Events

# Listening to Other Query Events

Chart developers may need to apply particular logic to their charts whenever a query event is triggered. Handler functions can be defined to override the following list of query methods:

* `controller.onStart`: Called as soon as the query execution begins.
* `controller.onNoDataFound`: Called when no data is available for the given query.
* `controller.onNotDirtyData`: Called as soon as all of the data is received.
* `controller.onStreamError`: Called when the query execution returns an error from the server.
