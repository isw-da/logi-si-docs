---
title: "DataLayer.Web Service - Attributes"
id: 4406822273943
section: "Datalayers - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822273943-DataLayer-Web-Service-Attributes
updated_at: 2022-04-06T06:05:30Z
---

# DataLayer.Web Service - Attributes

# DataLayer.Web Service - Attributes

The DataLayer.Web Service element has the following attributes:

| Attribute | Description |
| --- | --- |
| Connection ID | (Required) The ID of a **Connection.Web Service** element defined in the \_Settings definition. If this value is left blank, the datalayer will use the *first* connection in the \_Settings definition. For clarity, developers are advised to enter an ID here in all cases. |
| ID | An optional unique element ID. Recommended for easier identification when debugging. |
| XPath | Specifies a standard XPath string that will be used to select a set of matching nodes. All of the matching nodes are then used to generate the resulting datalayer. If an XPath is defined, it will be processed *before* any user defined XSL file. Tokens may be used in this attribute value. |

The **Connection.Web Service** element sets the parameters required to link the application to a web service; user account credentials are specified in its attributes.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) If you're trying to communicate with a web service that requires the **TLS 1.1** or 1.2 protocol, you will need to use Logi Info v12.2-SP4 or later (earlier versions only support TLS 1.0). In addition, Info Java applications must use Oracle JDK 1.8 or OpenJDK 8 to make the protocol work.
