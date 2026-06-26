---
title: "Creating Dynamic Connections"
id: 4419723039767
section: "Connect to Data - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723039767-Creating-Dynamic-Connections
updated_at: 2022-07-17T01:43:20Z
---

# Creating Dynamic Connections

# Creating Dynamic Connections

You may want to create *dynamic* connections, which connect to a datasource based on external criteria. Connection elements make this possible by accepting tokens in their attributes.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706963223/introconn5_10.png)

In the example above, left, tokens are used for the required attributes of the **Connection.SQL Server** element. Another approach is to assign a complete connection string to a Session variable and use its token in the **Connection String** attribute, as shown above right. A value in that attribute will cause the "required" attributes to be ignored.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699829271/introconn5_11.png)

Or you can enter the literal connection string text into that attribute, as shown above, and tokenize parts of it, like this:

Server=@Session.DBServer~;Database=@Session.DBName~;User Id=@Function.UserID~;Password=@Session.DBPassword~;

There are a variety of techniques available for setting the token values prior to the processing of the \_Settings definition. For example, the Startup Process element, when included in \_Settings, can be used to call a Process task that assigns the Session variables needed. This task will run *before* the Connection elements are processed.
For more information, see [The \_Settings Definition](https://devnet.logianalytics.com/hc/en-us/articles/4419723151767-The-Settings-Definition).

![](https://devnet.logianalytics.com/hc/article_attachments/4419706964375/introconn5_12.png)

The example shown above is simplistic but shows you how to use a Process task to set Session variables, which can be used later as tokens in the Connection element's attributes.
If you're unable to use the Startup Process element for some reason, you can still make the Process task run by calling it directly, rather than calling the default report definition:

http://yourServer/yourLogiApp/rdProcess.aspx?rdProcess=yourProcessDefinition&rdTaskID=taskStartUp
