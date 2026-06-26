---
title: "DataLayer.JSON - Using It with REST Web Services"
id: 4419707490967
section: "Datalayers - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707490967-DataLayer-JSON-Using-It-with-REST-Web-Services
updated_at: 2022-07-17T01:53:22Z
---

# DataLayer.JSON - Using It with REST Web Services

# DataLayer.JSON - Using It with REST Web Services

DataLayer.JSON is able to retrieve data from REST-style web services and the simplest approach is to configure its **Json File/URL** attribute with a complete URL. If the web service requires nothing else, the data will be retrieved using the default HTTP GET method.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714718359/dljson_03.png)

For more flexibility, you can instead use a **Connection.REST** element to define the first part of the URL:

![](https://devnet.logianalytics.com/hc/article_attachments/4419699651607/dljson_04.png)

Using a value in the datalayer's **Connection ID** attribute causes its Json File/URL value to be appended to the Connection element's **URL Host** attribute value, as shown above. This can be useful if your application uses multiple datalayers to connect to the same web service.
If you prefer, you can leave the Json File/URL value blank and add a **Link Parameters** element beneath the datalayer. Its name/value pairs will then be appended to the Connection ID's URL Host value, preceded by a "?".
