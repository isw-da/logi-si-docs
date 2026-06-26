---
title: "DataLayer.REST - Attributes"
id: 4419722835223
section: "Datalayers - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722835223-DataLayer-REST-Attributes
updated_at: 2022-07-17T02:08:14Z
---

# DataLayer.REST - Attributes

# DataLayer.REST - Attributes

The DataLayer.REST element has the following attributes:

| Attribute | Description |
| --- | --- |
| Connection ID | (Required) Specifies the ID of a **Connection.REST** element defined in the \_Settings definition. |
| Url Path | (Required) Specifies the portion of the URL that will be appended to the end of the URL specified in the Connection.REST element's Url Host attribute and may need to begin with a "/". For example, Connection.RESTUrl Host = http://local.yahooapis.com DataLayer.RESTUrl Path = /MapsService/V1/geocode?appid=YD... etc. producing this complete URL to request the web service method: http://local.yahooapis.com/MapsService/V1/geocode?appid=YD... etc. |
| Accept Type | Specifies the type of data expected to be received from a REST request. Options include *application/json* and *application/xml* (the default). |
| Http Method | Specifies the verb to be sent with a REST request. Options include: *DELETE*, *GET*, *POST*, and *PUT,* orcan bea custom verb.The default value is *GET*. |
| ID | Specifies an optional element ID. Recommended for easier identification when debugging. |
| New for 14.1 Maximum Rows | Specifies the maximum number of data rows to be retrieved. |
| Remove Namespace | Specifies whether the namespace and schema information that some data sources will add to the retrieved data is removed. The default value is *False*. |
| XPath | Specifies a standard XPath string that will be used to select a set of matching nodes. All of the matching nodes are then used to generate the resulting datalayer. Tokens may be used in this attribute value. |
