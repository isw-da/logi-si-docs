---
title: "DataLayer.JSON - Using Different HTTP Methods and Request Body Data"
id: 4406822258071
section: "Datalayers - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822258071-DataLayer-JSON-Using-Different-HTTP-Methods-and-Request-Body-Data
updated_at: 2022-04-06T06:05:17Z
---

# DataLayer.JSON - Using Different HTTP Methods and Request Body Data

# DataLayer.JSON - Using Different HTTP Methods and Request Body Data

If the web service requires you to use a different HTTP method, such as *POST* instead of *GET*, you can select it from the option list in the datalayer's **Http Method** attribute. Some web services may want you to use a custom method that's not in the option list, like *PATCH*, and in that case you can just type it right into the attribute value.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563388695/dljson_05.png)

The **Http Body** element, shown above, has two attributes:

* **Content Type,** which sets the content type in the request header and defaults to *application/json* for this datalayer.
* **Http Body Content**, which is the request body data, entered as an XML or JSON document or as a URL-encoded set of name/value pairs.

If you want to encode name/value pairs in the request body data to avoid possible issues with invalid characters, set the Http Body element's Content Type attribute to *application/x-www-form-urlencoded* and use the **Http Body Params** element to define the pairs. Tokens may be used in Http Body Param values.
