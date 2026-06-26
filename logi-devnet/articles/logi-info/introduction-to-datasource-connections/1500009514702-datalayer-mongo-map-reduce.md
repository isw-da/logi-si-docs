---
title: "DataLayer.Mongo Map Reduce"
id: 1500009514702
section: "Introduction to Datasource Connections"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009514702-DataLayer-Mongo-Map-Reduce
updated_at: 2021-06-17T01:58:12Z
---

# DataLayer.Mongo Map Reduce

# DataLayer.Mongo Map Reduce

**MongoDB** is a cross-platform, document-oriented database system, classified as a "NoSQL" database. Rather than using a traditional table-based, relational DB structure, it uses a collection of JSON-like documents with variable schemas. The **DataLayer.Mongo Map Reduce** element runs a Mongo Map Reduce command designed to return one or more documents.

* Attributes
* [Work with DataLayer.Mongo Map Reduce](#Working)

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771450519/plusicon.gif) General information about MongoDB can be found at the [official website](http://www.mongodb.com/).

## Attributes

The DataLayer.Mongo Map Reduce element has the following attributes:

| Attribute | Description |
| --- | --- |
| Connection ID | (Required) Specifies the ID of a Connection.MongoDB element in the application's \_Settings definition. *This element is discussed in more detail in the next section.* |
| ID | (Required) A unique element ID. |
| Map Function | (Required) In MongoDB, map-reduce operations use custom JavaScript functions to *map*, or associate, values to a key. This attribute specifies that function. For example:  function() { emit(this.cust\_id, this.price); }; |
| Mongo Collection | (Required) Specifies the name of the document collection to open. Note that the collection name is case-sensitive! |
| Reduce Function | (Required) If the Map Function produces a key with multiple values mapped to it, the custom JavaScript function specified here *reduces*, or aggregates, the values for the key to a single object. For example:  function(keyCustId, valuesPrices) {    return Array.sum(valuesPrices); } |
| Finalize Function | The output of the Reduce Function may pass through a *finalize* function. specified here, to further condense or process the results of the aggregation. For example:  function (key, reducedVal) {    reducedVal.avg = reducedVal.qty/reducedVal.count;    return reducedVal; } |
| Maximum Rows | Specifies a the maximum number of data rows to retrieve. If left blank, then all records that satisfy the request will be retrieved (up to a maximum of 16MB). |
| Mongo Query Document | Specifies a Mongo "find" document to identify one or more documents. Examples:  Find all documents with "type" equal to "snacks". { type: "snacks" }   Find all documents with "type" equal to "food" or "snacks" { type: { $in: [ 'food', 'snacks' ] } }  To vary the document content based on user or other input, use tokens, such as @Request, inside the document. |

## Work with DataLayer.Mongo Map Reduce

The Mongo map-reduce operation is used to condense large volumes of data into useful aggregated results, and this element incorporates that functionality into its data retrieval process.

In many respects, DataLayer.Mongo Map Reduce functions exactly as other datalayer elements do and, once retrieved, its data can be filtered and conditioned using appropriate child elements. Like other datalayers, it works with a specific Connection element, **Connection.MongoDB**, to connect to the datasource.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771861911/dlmongomap_01.png)

As shown above, the **Connection.MongoDB** element is added to the **\_Settings** definition, beneath the Connections element. Attributes are set appropriately for the MongoDB datasource. Note that the attributes have changed in v11.2.040+.

A **Mongo Params** element is available for use beneath Connection.MongoDB to supply additional options when connecting to the MongoDB database. Examples of additional parameters include "connectTimeoutMS" and "maxPoolSize". Refer to the [MongoDB connection options documentation](http://docs.mongodb.org/manual/reference/connection-string/#connections-connection-options) for a the complete list of options.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778696855/dlmongomap_02.png)

Next, in the report definition, a **DataLayer.Mongo Map Reduce** element is added as a child element of a data table or another data container element. Its attributes are set so that it accesses the desired MongoDB connection and data collection.

MongoDB results are often hierarchical and may consist of multiple levels of parent-child relationships. In order to work with Logi elements, the data often must be "tabularized" and this can be done by using the Flattener element. For more information, see [The Flattener](https://devnet.logianalytics.com/hc/en-us/articles/1500009515102-The-Flattener).

The datalayer **reads** and **caches** the data from the datasource. You can add standard **child elements** beneath the datalayer to affect its contents, including:

* **Filtering**: Sort, group, or restrict the data
* **Extending**: Add virtual columns to the datalayer that contain aggregated, calculated, or totaled data values
* **Securing**: Limit access to the data using Logi security
* **Linking**: Make the results reusable elsewhere in your report definitions

The use of many of these elements is described in separate DevNet documents.

Data read into the datalayer is cached in XML format in memory and/or on the web server's file system. The latter is discussed in [The Logi Server Engine](https://devnet.logianalytics.com/hc/en-us/articles/1500009515722-The-Logi-Server-Engine) and may be of interest to developers working with extremely large datasets or large numbers of concurrent users.

The data read with the datalayer is available using **@Data****tokens**, in the format @Data.*ColumnName*~. The spelling of the column name is **case-sensitive**. The data is only available within the **scope** of the **parent** element of the datalayer, not throughout the entire report definition. The **DataLayer.Linked** element can be used to make the data reusable in another datalayer outside this scope.

The data retrieved into the datalayer can be viewed by turning on the **Debugging Link** in your \_Settings definition (**General** element) and using the resulting link at the bottom of your report page to view the **Debugger Trace** page. A link on the Debug page will display the retrieved data.
