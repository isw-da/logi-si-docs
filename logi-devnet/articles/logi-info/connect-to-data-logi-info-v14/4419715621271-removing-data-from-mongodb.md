---
title: "Removing Data from MongoDB"
id: 4419715621271
section: "Connect to Data - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715621271-Removing-Data-from-MongoDB
updated_at: 2022-07-17T01:26:42Z
---

# Removing Data from MongoDB

# Removing Data from MongoDB

Removing existing data from a MongoDB is accomplished using a Process Task and the **Procedure.Mongo Remove** element.

![](https://devnet.logianalytics.com/hc/article_attachments/4419700022551/workmongodb_06.png)

In the example above, a Process Task has been defined that includes a Procedure.Mongo Remove element and its attributes have been set to delete any documents in the "Products" collection that include a UnitPrice equal to the value of a @Request token.

The Procedure.Mongo Remove element's attributes include:

| Attribute | Description |
| --- | --- |
| Connection ID | (Required) Specifies the ID of a Connection.MongoDB element in the application's \_Settings definition. |
| ID | (Required) A unique element ID. |
| Mongo Collection | (Required) Specifies the name of the document collection to open. This value is *case-sensitive*. |
| Mongo Query Document | Specifies a Mongo "find" document to identify one or more documents. Examples:  Find all documents with "type" equal to "snacks". { type: "snacks" }   Find all documents with "type" equal to "food" or "snacks" { type: { $in: [ 'food', 'snacks' ] } }  To vary the document content based on user or other input, use tokens, such as @Request, inside the document. |
| Mongo Write Concern | Specifies whether the procedure should wait for acknowledgement of the write operation.  The default value is *Acknowledged*, meaning wait for acknowledgement. |
| Multiple Documents | Specifies whether this command should affect multiple documents. The default value is *False*. |

After a remove procedure runs, you can use the special token @Procedure.*myProcMongoRemoveID*.DocumentsAffected~ to report the number of documents actually removed by the operation.
