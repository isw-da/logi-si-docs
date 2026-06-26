---
title: "Retrieving Data from MongoDB"
id: 4419715622295
section: "Connect to Data - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715622295-Retrieving-Data-from-MongoDB
updated_at: 2022-07-17T01:26:41Z
---

# Retrieving Data from MongoDB

# Retrieving Data from MongoDB

Special datalayer elements are used to retrieve data from the MongoDB system and their attributes can be used to form a "query" so that specific data is returned. In some cases, the data retrieved is limited to 16MB.

The available datalayers include the following (click the link for more information and examples):

| Element | Description |
| --- | --- |
| [DataLayer.Mongo Find](https://devnet.logianalytics.com/hc/en-us/articles/4419707246615-DataLayer-Mongo-Find) | Retrieves documents from a MongoDB collection using the MongoDB Find API. |
| [DataLayer.Mongo Map Reduce](https://devnet.logianalytics.com/hc/en-us/articles/4419700058135-DataLayer-Mongo-Map-Reduce) | Runs a MongoDB map-reduce operation to return one or more documents. |
| [DataLayer.Mongo Run Command](https://devnet.logianalytics.com/hc/en-us/articles/4419707247639-DataLayer-Mongo-Run-Command) | Runs a MongoDB command, suitable for use with the Aggregation Pipeline, a simpler alternative to using map-reduce operations, to return one or more documents. |

MongoDB results are often hierarchical and may consist of multiple levels of parent-child relationships. In order to work with Logi elements, the data often must be "tabularized" and this can be done by using [The Flattener](https://devnet.logianalytics.com/hc/en-us/articles/4419722921623-The-Flattener) element.

In many respects, these datalayers function exactly as other datalayer elements do and, once retrieved, the data can be filtered and conditioned using all the usual datalayer child elements.
