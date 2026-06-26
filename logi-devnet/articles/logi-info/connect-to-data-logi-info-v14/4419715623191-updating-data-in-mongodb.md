---
title: "Updating Data in MongoDB"
id: 4419715623191
section: "Connect to Data - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715623191-Updating-Data-in-MongoDB
updated_at: 2022-07-17T01:26:38Z
---

# Updating Data in MongoDB

# Updating Data in MongoDB

Updating existing data in MongoDB is accomplished using a Process Task and the **Procedure.Mongo Update** element.

![](https://devnet.logianalytics.com/hc/article_attachments/4419715005591/workmongodb_05.png)

In the example above, a Process Task has been defined that includes a Procedure.Mongo Update element and its attributes have been set to update data into the "animals" collection. Note the use of a @Request token in the update document.

The Procedure.Mongo Update element's attributes include:

| Attribute | Description |
| --- | --- |
| Connection ID | (Required) Specifies the ID of a Connection.MongoDB element in the application's \_Settings definition. |
| ID | (Required) A unique element ID. |
| Mongo Collection | (Required) Specifies the name of the document collection to open. This value is *case-sensitive*. |
| Mongo Query Document | Specifies a Mongo "find" document to identify one or more documents. Examples:  Find all documents with "type" equal to "snacks". { type: "snacks" }   Find all documents with "type" equal to "food" or "snacks" { type: { $in: [ 'food', 'snacks' ] } }  To vary the document content based on user or other input, use tokens, such as @Request, inside the document. |
| Mongo Update Document | (Required) Specifies the new document to be updated, or possibly inserted into to the collection. To update selected attributes, instead of replacing the entire document, use the Mongo "$set" operator. To vary the document content based on user or other input, use tokens, such as @Request, inside the document. |
| Mongo Write Concern | Specifies whether the procedure should wait for acknowledgement of the write operation.  The default value is *Acknowledged*, meaning wait for acknowledgement. |
| Multiple Documents | Specifies whether this command should affect multiple documents. The default value is *False*. |
| Upsert | Specifies whether this update command should be performed as an "Upsert". When the key already exists, the item is updated, otherwise a new item is inserted. The default value is *False*. |

After an update procedure runs, you can use the special token @Procedure.*myProcMongoUpdateID*.DocumentsAffected~ to report the number of
documents actually updated or inserted by an update operation.
