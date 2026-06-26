---
title: "Inserting Data into MongoDB"
id: 4419715620375
section: "Connect to Data - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715620375-Inserting-Data-into-MongoDB
updated_at: 2022-07-17T01:26:45Z
---

# Inserting Data into MongoDB

# Inserting Data into MongoDB

Inserting data into MongoDB is accomplished using a Process Task and the **Procedure.Mongo Insert** element.

![](https://devnet.logianalytics.com/hc/article_attachments/4419700020759/workmongodb_03.png)

In the example above, a Process Task has been defined that includes a Procedure.Mongo Insert element and its attributes have been set to insert data into the "zips" collection.

The Procedure.Mongo Insert element's attributes include:

| Attribute | Description |
| --- | --- |
| Connection ID | (Required) Specifies the ID of a Connection.MongoDB element in the application's \_Settings definition. |
| ID | (Required) A unique element ID. |
| Mongo Collection | (Required) Specifies the name of the document collection to open. This value is *case-sensitive*. |
| Mongo Insert Document | (Required) Specifies the new document to be inserted to the collection. To vary the document content based on user or other input, use tokens, such as @Request, inside the document. |
| Mongo Write Concern | Specifies whether the procedure should wait for acknowledgement of the write operation.  The default value is *Acknowledged*, meaning wait for acknowledgement. |

No results are returned when the insert operation runs; however, an error that can be handled with the **If Error** element will be thrown if it fails.
Let's examine a more complicated example:

![](https://devnet.logianalytics.com/hc/article_attachments/4419700021015/workmongodb_04.png)

In the process task shown above, data is being read from a SQL database and inserted into a MongoDB collection. First, **Procedure.Run Datalayer Rows** and its datalayer query the SQL database. Then, for each datalayer row, Procedure.Mongo Insert is run. Two **Procedure.If** elements are used to determine if the SQL data's "ShippedDate" column is null or not, in order to run different insert elements with slightly different Mongo Insert Documents for each case.

Note how the @Data tokens from the SQL query data are used in the Mongo Insert Document.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599319/criticalicon.png) The **Procedure.Mongo Update** element can perform an "Upsert", inserting a new document if one doesn't exist to be updated; see [Updating Data in MongoDB](https://devnet.logianalytics.com/hc/en-us/articles/4419715623191-Updating-Data-in-MongoDB).
