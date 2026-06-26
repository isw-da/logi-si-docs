---
title: "Running MongoDB Commands"
id: 4406818135703
section: "Connect to Data - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406818135703-Running-MongoDB-Commands
updated_at: 2022-04-06T06:10:23Z
---

# Running MongoDB Commands

# Running MongoDB Commands

You can issue MongoDB Commands using a Process Task and the **Procedure.Mongo Run Command** element.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562949399/workmongodb_07.png)

In the example above, a Process Task has been defined that includes a Procedure.Mongo Run Command element and its attributes have been set to run the MongoDB "isMaster" command.

The Procedure.Mongo Run Command element's attributes include:

| Attribute | Description |
| --- | --- |
| Connection ID | (Required) Specifies the ID of a Connection.MongoDB element in the application's \_Settings definition. |
| ID | (Required) A unique element ID. |
| Mongo Run Command | Specifies a MongoDB command. Refer to the [MongoDB Database Command documentation](http://docs.mongodb.org/manual/reference/command/) for a the complete list of commands. |

No results are returned when the command runs; however, an error that can be handled with the **If Error** element will be thrown if it fails.
