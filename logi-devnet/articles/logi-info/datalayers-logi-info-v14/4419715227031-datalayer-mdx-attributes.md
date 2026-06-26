---
title: "DataLayer.MDX - Attributes"
id: 4419715227031
section: "Datalayers - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715227031-DataLayer-MDX-Attributes
updated_at: 2022-07-17T01:53:12Z
---

# DataLayer.MDX - Attributes

# DataLayer.MDX - Attributes

The **DataLayer.MDX** element has the following attributes:

| Attribute | Description |
| --- | --- |
| Connection ID | (Required) Specifies a connection to a data source, which has been defined in the \_Settings definition. |
| ID | (Required) A unique element name. |
| Handle Quotes Inside Tokens | Enables special token processing, allowing use of token values that contain single quotes. When set to *True*, the single quotes in the values of any tokens in the MDX Source attribute will be "doubled" so that they work within aSQL statement. The default for value is *False*. |
| MDX Source | Specifies an optional developer-coded MDX command to be sent to the OLAP server. Only applicable when used with an OLAP Table parent element; OLAP Gridsmust use the **MDX Query** element instead. The Browse button for this attribute can be used to launch the **MDX Query Builder** tool. |
