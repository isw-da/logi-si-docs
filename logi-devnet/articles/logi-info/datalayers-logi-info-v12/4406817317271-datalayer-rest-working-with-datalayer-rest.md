---
title: "DataLayer.REST - Working with DataLayer.REST"
id: 4406817317271
section: "Datalayers - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817317271-DataLayer-REST-Working-with-DataLayer-REST
updated_at: 2022-10-28T13:55:28Z
---

# DataLayer.REST - Working with DataLayer.REST

# DataLayer.REST - Working with DataLayer.REST

A web service can expose one or more of its methods so that they can be called from an application, resulting in data being returned, as a JSON or XML document in a serialized string.

The web service's Web Application Description Language (WADL) document identifies the available methods. This is the REST equivalent of the SOAP-based web service's WSDL document and provide information about the service's methods, requirements, and data.

DataLayer.REST can be used with one or more child **XslTransform** elements, which use XSL files to transform the data *before* it's loaded into the datalayer. This allows the adjustment of data if it has a schema that cannot be understood by the Logi Server engine.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) Data may be returned in a hierarchical format, with parent-child relationships, such as JSON data. This data won't be fully available as standard datalayer XML and will create difficulties for further processing and analysis. [The Flattener](https://devnet.logianalytics.com/hc/en-us/articles/4406817464343-The-Flattener) child element can be used to process this hierarchical data into
the standard tabular set of rows and columns normally found in a datalayer.
The following example shows DataLayer.REST in use:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575770007/dlrest_01.png)

As shown above, a **DataLayer.REST** element has been added beneath a data table. Its **Connection ID** and **Url Path** attributes have been set appropriately. Remember that its Url Path value will be appended to the Connection.REST element's Url Host value.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563384727/dlrest_02.png)

As shown above, one or more **XslTransform** elements can be added beneath the datalayer for each XSL transform to be applied to the data *before* it is retrieved into the datalayer. If a complete file path is not provided for the transform file, the engine will assume that the XSL file is in the \_SupportFiles folder.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584023959/dlrest_03.png)

You may not have access to the web service's WADL file and, therefore, may not know the names of the data columns. In this case, Studio's **Add data columns** can be a tremendous help. Right-click the data table element, then select the options shown above in the pop-up menus. The wizard will interrogate the web service and insert the elements needed to display your data table columns.
