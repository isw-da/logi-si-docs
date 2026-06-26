---
title: "Web Service Interactions"
id: 4419715443735
section: "Use Logi Studio/SSRM - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715443735-Web-Service-Interactions
updated_at: 2022-07-17T01:39:47Z
---

# Web Service Interactions

# Web Service Interactions

The **Procedure.REST** element can be used to interact with a REST-style web service from within a process task. Typically, this would be to send a request that invokes an HTTP PUT or DELETE method, but GET and POST are also supported.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599319/criticalicon.png) If you're trying to communicate with a web service that requires the **TLS 1.1** or 1.2 protocol, you will need to use Logi Info v12.2-SP4 or later (earlier versions only support TLS 1.0). In addition, Info Java applications must use Oracle JDK 1.8 or OpenJDK 8 to make the protocol work.

The Procedure.REST element has attributes that are similar to those of DataLayer.REST:

| Attribute | Description |
| --- | --- |
| ID | (Required) Specifies a unique element ID. |
| Accept Type | Specifies the type of data expected to be received from a REST request. Options include *application/json* and *application/xml* (the default). |
| Connection ID | Specifies the ID of a **Connection.REST** element defined in the \_Settings definition. |
| Http Method | Specifies the verb to be sent with a REST request. Standard options include: *DELETE*, *GET*, *POST*, and *PUT,* and you can also enter custom verbs, like *PATCH*, if necessary. The default value is *GET*. |
| ID | Specifies a unique element ID. You'll need to provide this if you want to use tokens to get a returned code or description. |
| Remove Namespace | Specifies whether the namespace and schema information that some data sources will add to the retrieved data is removed. The default value is *False*. |
| Url Path | Specifies the portion of the URL that will be appended to the end of the URL specified in the Connection.REST element's Url Host attribute and may need to begin with a "/". For example,  Connection.RESTUrl Host = http://local.yahooapis.com Procedure.RESTUrl Path = /MapsService/V1/geocode?appid=YD... etc.  producing this complete URL to request the web service method: http://local.yahooapis.com/MapsService/V1/geocode?appid=YD... etc. |

You can reference the web service's response code and description with these Procedure tokens:

+ @Procedure.*yourProcedureID*.rdHttpResponseCode~
+ @Procedure.*yourProcedureID*.rdHttpResponseDescription~
+ @Procedure.idof Restprocess.rdhttpResponseBodyContent~

Procedure.REST can also use the **Http Body** child element, which has two attributes:

* **Content Type,** which sets the content type in the request header and defaults to *application/x-www-form-urlencoded*.
* **Http Body Content**, which is the request body data, entered as an XML or JSON document or as a URL-encoded set of name/value pairs.

If you want to encode name/value pairs in the request body data to
avoid possible issues with invalid characters, ensure that the Http Body
element's Content Type attribute is blank or set to *application/x-www-form-urlencoded* and use the **Http Body Params** element to define the pairs. Tokens may be used in Http Body Param values.
