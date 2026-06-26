---
title: "DataLayer.XML - Attributes"
id: 4419707508759
section: "Datalayers - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707508759-DataLayer-XML-Attributes
updated_at: 2022-07-17T01:52:34Z
---

# DataLayer.XML - Attributes

# DataLayer.XML - Attributes

The **DataLayer.XML** element has the following attributes:

| Attribute | Description |
| --- | --- |
| XML File / URL | (Required) Specifies the identifier of the XML data file. You may enter either a file system location or the URL for a location on the web. By default, the server will look in the \_SupportFiles folder and, if the file is located there, then only the file name and extension are needed in this attribute. If it's located elsewhere in the file system, a fully-qualified path and file name is required, such as: D:\Projects\Accounting\Data\MyData.xml If a URL is used to retrieve a file from a web server, it must be fully-formed, such as: http://myserver/mydata.xml |
| Connection ID | Specifies the element ID of a Connection element defined in the \_Settings definition. If a value is specified here, then XML File attribute value isappended to the Connection element's Url Host attribute value. |
| Http Method | Specifies the verb to be sent with a REST request. Options include: *DELETE*, *GET*, *POST*, and *PUT,* or can be a custom verb.The default value is *GET*. |
| ID | Specifies an optional element ID. Recommended for easier identification when debugging. |
| Maximum Rows | Specifies the maximum number of data rows to be retrieved. |
| Remove Namespace | Specifies whether the namespace and schema information that some XML data sources will add to the retrieved data is removed. The default value is *False*. |
| XPath | Specifies a standard XPath string that will be used to select a set of matching nodes. All of the matching nodes are then used to generate the resulting datalayer. Tokens may be used in this attribute value. |
