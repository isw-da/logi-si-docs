---
title: "DataLayer.Web Service"
id: 1500009514802
section: "Introduction to Datasource Connections"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009514802-DataLayer-Web-Service
updated_at: 2021-06-17T01:58:14Z
---

# DataLayer.Web Service

# DataLayer.Web Service

The **DataLayer.Web Service** element gives developers the ability to retrieve information from a SOAP **web service**. Web services can return either an XML *dataset* *object* or a *string*. The Logi server engine generates an XML rowset from the returned data and developers can use tokens to retrieve records from each column.

* Attributes
* [Working with DataLayer.Web Service](#sec1)
* [Using Studio's DataLayer Wizard](#Wizard)
* [Multi-Step Web Service Access](#MultStep)

We also offer [DataLayer.REST](https://devnet.logianalytics.com/hc/en-us/articles/1500009514722-DataLayer-REST) for use with web services that use a RESTful protocol.

## Attributes

The DataLayer.Web Service element has the following attributes:

| Attribute | Description |
| --- | --- |
| Connection ID | (Required) The ID of a **Connection.Web Service** element defined in the \_Settings definition. If this value is left blank, the datalayer will use the **first** connection in the \_Settings definition. For clarity, developers are advised to enter an ID here in all cases. |
| ID | (Required through v10.1.46) A unique element ID. |
| XPath | Specifies a standard XPath string that will be used to select a set of matching nodes. All of the matching nodes are then used to generate the resulting datalayer. If an XPath is defined, it will be processed *before* any user defined XSL file. |

**Note:** The **Connection.Web Service** element sets the parameters required to link the application to a web service; user account credentials are specified in its attributes.

## Working with DataLayer.Web Service

A web service can expose one or more of its **methods** so that they can be called by developers from an application. Web service methods return XML as either a *dataset* *object* or serialized *string* type. In both cases, the XML data may require special formatting for use within Logi reporting products. Logi Studio includes an **XslTransform** element which can be quite useful for converting XML in a datalayer into a format the Logi engine understands.

The information needed to configure the values of the Logi elements used with a web service can be found in the web service's WSDL document.

The following example illustrates how to use the **DataLayer.Web Service** element and its child elements:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771848855/dlwebsvc_01.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778685975/dlwebsvc_01a.png)

1. Add a **DataLayer.Web Service** element to the definition, as shown above, and configure its attributes per the attribute table in the previous section.
2. Add a **Web Service Method** element beneath the datalayer, and give it a unique ID.
3. Set its **Method Name** attribute value to the name of the web service method that is to be called.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771849111/dlwebsvc_02.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771849367/dlwebsvc_02a.png)

4. As shown above, add one or more **Method Input Parameter** elements beneath the Web Service Method element, based on the number of parameters you must pass to the web service method.   
     
   If working with our **.NET** products, these elements *must* be in the **order** that the parameters are expected by the web service.  
    If working with our **Java** products, the element ID attribute *must* be set to the **name** of the corresponding parameter.  
    Consult the WSDL document to confirm correct parameter order and names.

5. Set each parameter's **Data Type** attribute value to the correct data type.
6. Set each parameter's **Value** attribute to the value (hard-coded or as a token) that you want to pass to the method.

Now when you run your report, the data from the web service should be retrieved into the datalayer.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778686359/dlwebsvc_02b.png)

When working with web services and data tables, you may not be sure what the column names of the returned data will be; this is a perfect time to use the **Add data columns** wizard found in Studio. Right-click the datalayer element, then select the options shown above in the pop-up menus. The wizard will interrogate the web service and insert the elements needed to display your data table columns.

### Working with Complex Data Types

Some web services may require you to send data, such as a user name and password, to them using complex data types. These requirements should be handled by writing a plug-in, as our DataLayer.Web Service element is not capable of creating complex structures for transmission to a web service.

You can see an example of this type of plug-in in action in our [Web Service with Complex Header](https://devnet.logianalytics.com/rdPage.aspx?rdReport=Samples&tabsSamples=tabPlugins) sample plug-in.

## Using Studio's DataLayer Wizard

Beginning in v10.0.299, Studio includes a wizard that can assist you in configuring DataLayer.Web Service. The wizard assumes that you have already added an appropriate database **Connection** element in the \_Settings definition and configured it.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771849623/dlwebsvc_04.png)

As shown above, the wizard can be started by selecting and then right-clicking the parent element under which you want to add the datalayer, and using the context menus to select "Add a Web Service DataLayer". The wizard will open; use it as follows:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771849879/dlwebsvc_05.png)

1. Select the ID of the Connection element from the drop-down list of available connections. Click **Next** to continue.  
     
   ![](https://logianalytics.zendesk.com/hc/article_attachments/4402778686615/dlwebsvc_06.png)
2. Select the desired web service method from the drop-down list of available methods that the wizard retrieved from the service. If an error occurs here, then the wizard was not able to connect to the web service and you should examine your Connection element attributes to ensure that they are correct. Click **Next** to continue.  
     
   ![](https://logianalytics.zendesk.com/hc/article_attachments/4402778686871/dlwebsvc_07.png)
3. Click **Finish** to close the wizard.  
     
     
   ![](https://logianalytics.zendesk.com/hc/article_attachments/4402771850135/dlwebsvc_08.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778687127/dlwebsvc_08a.png)
4. The wizard has inserted the datalayer and configured its attributes, as shown above, and has inserted and configured any required **Web Service Method** and **Method Input Parameter** elements. You will need to manually provide the input parameter values, either directly or using tokens.

## Multi-Step Web Service Access

Some web services require **multiple** interaction steps before they will return a result. For example, you may first need to tell the web service your security credentials, then tell it what data category you need, then tell it what format to put the results in, and then request the actual data. A single **DataLayer.Web Service** element is not designed for this kind of multi-step "conversation" with a web service. So how can this be accomplished?

One approach is to use *multiple* DataLayer.Web Service elements, one for each part of the conversation. In your report, just add multiple DataLayer.Web Service elements, one for each part of the conversation, and they will execute one after another.

In the example shown above, multiple DataLayer.Web Service elements are used, with each calling a different web service method, to complete the multi-step conversation required by the web service. The last one sends the query and the data is retrieved and available using standard @Data tokens.

Another approach is to write a **plug-in** to handle the multi-step conversation. When used with [DataLayer.Plugin](https://devnet.logianalytics.com/hc/en-us/articles/1500009530281-DataLayer-Plugin), the plug-in would issue the sequential web service method calls and place the resulting data into the datalayer for use in the report. DevNet members, after login, can see an example of this type of plug-in in action in our [Web Service
with Complex Header](https://devnet.logiAnalytics.com/rdPage.aspx?rdReport=Samples&tabsSamples=tabPlugins) sample plug-in.

For more information, our [Web Service Sample Application](https://devnet.logianalytics.com/rdPage.aspx?rdReport=Samples&tabsSamples=pnlApps) demonstrates the use of DataLayer.Web Service.

keyword: webservice
