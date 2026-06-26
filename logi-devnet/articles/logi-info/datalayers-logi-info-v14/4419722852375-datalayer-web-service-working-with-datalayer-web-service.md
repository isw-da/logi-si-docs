---
title: "DataLayer.Web Service - Working with DataLayer.Web Service"
id: 4419722852375
section: "Datalayers - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722852375-DataLayer-Web-Service-Working-with-DataLayer-Web-Service
updated_at: 2022-07-17T01:52:20Z
---

# DataLayer.Web Service - Working with DataLayer.Web Service

# DataLayer.Web Service - Working with DataLayer.Web Service

A web service can expose one or more of its **methods** so that they can be called by developers from an application. Web service methods return XML as either a *dataset* *object* or serialized *string* type. In both cases, the XML data may require special formatting for use within Logi reporting products. Logi Studio includes an **XslTransform** element which can be quite useful for converting XML in a datalayer into a format the Logi engine understands.

The information needed to configure the values of the Logi elements used with a web service can be found in the web service's **WSDL** document.

The following example illustrates how to use the **DataLayer.Web Service** element and its child elements:

![](https://devnet.logianalytics.com/hc/article_attachments/4419699667223/dlwebsvc_01.png)

1. Add a **DataLayer.Web Service** element to the definition, as shown above, and configure its attributes per the attribute table in [DataLayer.Web Service - Attributes](https://devnet.logianalytics.com/hc/en-us/articles/4419707511831-DataLayer-Web-Service-Attributes).
2. Add a **Web Service Method** element beneath the datalayer, and give it a unique ID.
3. Set its **Method Name** attribute value to the name of the web service method that is to be called.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699667479/dlwebsvc_02.png)

4. As shown above, add one or more **Method Input Parameter** elements beneath the Web Service Method element, based on the number of parameters you must pass to the web service method.   
     
   If you're developing a **.NET** Logi application, these elements *must* be in the **order** that the parameters are expected by the web service.  
    If you're developing a **Java** Logi application, the element ID attribute *must* be set to the **name** of the corresponding parameter.  
    Consult the WSDL document to confirm correct parameter order and names.

5. Set each parameter's **Data Type** attribute value to the correct data type.
6. Set each parameter's **Value** attribute to the value (hard-coded or as a token) that you want to pass to the method.

Now when you run your report, the data from the web service should be retrieved into the datalayer.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699667735/dlwebsvc_03.png)

When working with web services and Data Tables, you may not be sure what the column names of the returned data will be; this is a perfect time to use the **Add data columns** wizard found in Studio. Right-click the datalayer element, then select the options shown above in the pop-up menus. The wizard will interrogate the web service and insert the elements needed to display your Data Table columns.

## Working with Complex Data Types

Some web services may require you to send data, such as a user name and password, to them using complex data types. These requirements should be handled by writing a plug-in, as our DataLayer.Web Service element is not capable of creating complex structures for transmission to a web service.

You can see an example of this type of plug-in in action in our [Web Service with Complex Header](https://devnet.logianalytics.com/hc/en-us/articles/360047205234-Web-Service-with-Complex-Header) sample plug-in.
