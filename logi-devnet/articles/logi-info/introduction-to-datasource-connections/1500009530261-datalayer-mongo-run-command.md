---
title: "DataLayer.Mongo Run Command"
id: 1500009530261
section: "Introduction to Datasource Connections"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009530261-DataLayer-Mongo-Run-Command
updated_at: 2021-06-17T01:58:12Z
---

# DataLayer.Mongo Run Command

**MongoDB** is a cross-platform, document-oriented database system, classified as a "NoSQL" database. Rather than using a traditional table-based, relational DB structure, it uses a collection of JSON-like documents with variable schemas. The **DataLayer.Mongo Run Command** element runs a Mongo command designed to return one or more documents.

* Attributes
* [Work with DataLayer.Mongo Run Command](#Working)

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771450519/plusicon.gif) General information about MongoDB can be found at the [official website](http://www.mongodb.com/).

## Attributes

The DataLayer.Mongo Run Command element has the following attributes:

| Attribute | Description |
| --- | --- |
| Connection ID | (Required) Specifies the ID of a Connection.MongoDB element in the application's \_Settings definition. *This element is discussed in more detail in the next section.* |
| Mongo Run Command | (Required) Specifies a MongoDB command document. To vary the document content based on user or other input, use tokens, such as @Request, inside the document. |
| ID | A unique element ID. |
| Maximum Rows | Specifies a the maximum number of data rows to retrieve. If left blank, then all records that satisfy the request will be retrieved (up to a maximum of 16MB). |
| Preserve Hierarchy | Specifies whether or not to process the data to create traditional rows and columns. Set to *True* (the default value) to leave the data as it is, or *False* to process it. |

## Work with DataLayer.Mongo Run Command

DataLayer.Mongo Run Command runs a Mongo command designed to return one or more
documents and is suitable for running aggregations with the Aggregation
Pipeline, a simpler alternative to using map-reduce operations. Mongo Run Command has a result set size limit of 16MB.

In many respects, DataLayer.Mongo Run Command functions exactly as other datalayer elements do and, once retrieved, its data can be filtered and conditioned using appropriate child elements. Like other datalayers, it works with a specific Connection element, **Connection.MongoDB**, to connect to the datasource.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771861527/dlmongorun_01.png)

As shown above, the **Connection.MongoDB** element is added to the **\_Settings** definition, beneath the Connections element. Attributes are set appropriately for the MongoDB datasource. Note that the attributes have changed in v11.2.040+.

A **Mongo Params** element is available for use beneath Connection.MongoDB to supply additional options when connecting to the MongoDB database. Examples of additional parameters include "connectTimeoutMS" and "maxPoolSize". Refer to the [MongoDB connection options documentation](http://docs.mongodb.org/manual/reference/connection-string/#connections-connection-options) for a the complete list of options.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778696471/dlmongorun_02.png)

Next, in the report definition, a **DataLayer.Mongo Run Command** element is added as a child element of a data table or another data container element. Its attributes are set so that it issues the desired MongoDB database command. This operation has a result size limit of 16MB.

MongoDB results are often hierarchical and may consist of multiple levels of parent-child relationships. In order to work with Logi elements, the data often must be "tabularized" and this can be done by using the Flattener element. For more information, see [The Flattener](https://devnet.logianalytics.com/hc/en-us/articles/1500009515102-The-Flattener).

The datalayer **reads** and **caches** the data from the datasource. You can add standard **child elements** beneath the datalayer to affect its contents, including:

* **Filtering**: Sort, group, or restrict the data
* **Extending**: Add virtual columns to the datalayer that contain aggregated, calculated, or totaled data values
* **Securing**: Limit access to the data using Logi security
* **Linking**: Make the results reusable elsewhere in your report definitions

The use of many of these elements is described in separate DevNet documents.

Data read into the datalayer is cached in XML format in memory and/or on the web server's file system. The latter is discussed in [The Logi Server Engine](https://devnet.logianalytics.com/hc/en-us/articles/1500009515722-The-Logi-Server-Engine) and may be of interest to developers working with extremely large datasets or large numbers of concurrent users.

The data read with the datalayer is available using **@Data****tokens**, in the format @Data.*ColumnName*~. The spelling of the column name is **case-sensitive**. The data is only available within the **scope** of the **parent** element of the datalayer, not throughout the entire report definition. The **DataLayer.Linked** element can be used to make the data reusable in another datalayer outside this scope.

The data retrieved into the datalayer can be viewed by turning on the **Debugging Link** in your \_Settings definition (**General** element) and using the resulting link at the bottom of your report page to view the **Debugger Trace** page. A link on the Debug page will display the retrieved data.
