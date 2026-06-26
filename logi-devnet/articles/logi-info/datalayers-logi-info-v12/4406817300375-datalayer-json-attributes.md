---
title: "DataLayer.JSON - Attributes"
id: 4406817300375
section: "Datalayers - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817300375-DataLayer-JSON-Attributes
updated_at: 2022-04-06T06:05:16Z
---

# DataLayer.JSON - Attributes

# DataLayer.JSON - Attributes

The DataLayer.JSON element has the following attributes:

| Attribute | Description |
| --- | --- |
| Json File/URL | (Required) Specifies the identifier of the JSON data file. You may enter either a file system location or the URL for a location on the web. By default, the server will look in the \_SupportFiles folder and, if the file is located there, then only the file name and extension are needed in this attribute. If it's located elsewhere in the file system, a fully-qualified path and file name is required, such as: D:\Projects\Accounting\Data\MyData.js If a URL is used to retrieve a file from a web server, it must be fully-formed, such as: http://myserver/mydata.js |
| Connection ID | Specifies the element ID of a Connection element defined in the \_Settings definition. If a value is specified here, then Json File / URL attribute value is appended to the Connection element's Url Host attribute value (does not apply to Connection.Logi Application Service). |
| Http Method | Specifies the verb to be sent with a REST request. Options include: *DELETE*, *GET*, *POST*, and *PUT,* or can be a custom verb. The default value is *GET*. |
| ID | Specifies an optional element ID. Recommended for easier identification when debugging. |
| Maximum Rows | Specifies the maximum number of data rows to be retrieved. |
| XPath | Specifies a standard XPath string that will be used to select a set of matching nodes. All of the matching nodes are then used to generate the resulting datalayer. Tokens may be used in this attribute value. |
