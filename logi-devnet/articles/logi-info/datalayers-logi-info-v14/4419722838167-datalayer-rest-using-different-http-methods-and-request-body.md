---
title: "DataLayer.REST - Using Different HTTP Methods and Request Body Data"
id: 4419722838167
section: "Datalayers - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722838167-DataLayer-REST-Using-Different-HTTP-Methods-and-Request-Body-Data
updated_at: 2022-07-17T01:53:02Z
---

# DataLayer.REST - Using Different HTTP Methods and Request Body Data

# DataLayer.REST - Using Different HTTP Methods and Request Body Data

If the web service requires you to use a different HTTP method, such as *POST* instead of *GET*, you can select it from the option list in the datalayer's **Http Method** attribute. Some web services may want you to use a custom method that's not in the option list, like *PATCH*, and in that case you can just type it right into the attribute value.

In addition, some web services expect that request parameters be available in the "Request Body". DataLayer.REST has a child element that facilitates the passing of information in the request body for this purpose and the datalayer's Http Method must
be set to *POST*
in order to use it.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699653783/dlrest_04.png)

The **Http Body** element, shown above, has two attributes:

* **Content Type,** which sets the content type in the request header and defaults to *application/x-www-form-urlencoded* for this datalayer.
* **Http Body Content**, which is the request body data, entered as an XML or JSON document or as a URL-encoded set of name/value pairs.

If you want to encode name/value pairs in the request body data to avoid possible issues with invalid characters, ensure that the Http Body element's Content Type attribute is blank or set to *application/x-www-form-urlencoded* and use the **Http Body Params** element to define the pairs. Tokens may be used in Http Body Param values.  
For more information, our [Web Service Sample Application](https://devnet.logianalytics.com/hc/en-us/articles/360049630754-Web-Services-Sample-Application) (under the "Advanced" category) demonstrates the use of DataLayer.REST.
