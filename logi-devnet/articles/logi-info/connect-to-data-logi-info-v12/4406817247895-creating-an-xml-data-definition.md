---
title: "Creating an XML Data Definition"
id: 4406817247895
section: "Connect to Data - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817247895-Creating-an-XML-Data-Definition
updated_at: 2022-04-06T06:04:55Z
---

# Creating an XML Data Definition

# Creating an XML Data Definition

![](https://devnet.logianalytics.com/hc/article_attachments/4417575435927/notev12.7base.png)An XML Data definition uses a small subset of the standard Logi Info elements, most of them related to data retrieval and manipulation.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584054295/usingdatadefs_16.png)

The first element that needs to be added in any XML Data definition is an **XML Data** element. It runs a datalayer, inserts the results into an XML document, and streams it.

Its optional attributes are:

| Attribute | Description |
| --- | --- |
| Attributes as Elements | Specifies the format of the data values. The values are normally expressed as attributes in XML, but may be represented instead as elements with text nodes. When this attribute is set to *True*, values are contained in elements. For example:  If *False* (the default) is specified, the output will look like:  <Root>  <Order OrderID="12345" Freight="1.12" /> <Root>  If *True* is specified, the output will look like:  <Root>  <Order>  <OrderID>12345</ID  <Freight>1.12</Freight>  </Order> <Root> |
| Data Row ElementName | Specifies the name for XML elements which represent each of the data rows. The default is the Xml Data element's ID attribute. |
| Document Element Name | Specifies the name of the output XML's root element. The default is the Xml Data element's ID attribute. |
| ID | A unique element ID. |
