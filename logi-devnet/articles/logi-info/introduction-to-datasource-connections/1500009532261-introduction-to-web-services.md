---
title: "Introduction to Web Services"
id: 1500009532261
section: "Introduction to Datasource Connections"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009532261-Introduction-to-Web-Services
updated_at: 2021-06-17T01:58:44Z
---

# Introduction to Web Services

# Introduction to Web Services

This topic provides an overview of **web services** and their use with Logi applications.

* About Web Services
* [Connectivity](#Connectivity)
* [Working with Data](#Data)

## About Web Services

A **Web Service** is defined by the W3C as "a software system designed to support interoperable machine-to-machine interaction over a network". Web services are frequently just **Web APIs** that can be accessed over a network, such as the Internet, and executed on a remote system hosting the requested services.

In common usage, "web service" refers to clients and servers that communicate using **XML** messages, following the **SOAP** or **REST** protocol standards. Logi Analytics products use XML as their underlying technology and are therefore well-suited to work with web services.

Logi Studio makes it easy to work with web services by doing some of the required legwork for you. For example, there is often a machine-readable description of the operations offered by a web service written in the Web Services Description Language (WSDL) and Studio's wizards can read this remote file and then present developers with choices of methods and their parameters.

Web services often require that commercial users pay for the use of their service. At a minimum, an account will likely have to be established in order to access a web service.

## Connectivity

In a Logi application, the same basic technique that's used for connecting to a database is used for connecting to a web service. A connection element, either **Connection.Web Service** or **Connection.REST**, is placed in the \_Settings definition and provides connectivity. Connection.Web Service has a child element, **Connector Property Parameters**, which can be used handle
special authentication and proxy settings for the SOAP service.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif) For developers connecting to their *own* web service using Connection.Web Service, note that the WSDL document specified in this connection element's required WSDL URL attribute must be "valid", meaning that it can contain no errors that would cause it to fail to compile. A document that's readable but that will not compile is invalid and will cause the connection to fail.

Once defined, this connection is then referenced in other report definitions that wish to use the web service. The process is quick and easy.

## Working with Data

Similarly, the same basic technique that's used to retrieve data from a database is used to retrieve data from a web service. A special datalayer element, either **DataLayer.Web Service** or **DataLayer.REST**, is placed in the report definition and, using the connection mentioned earlier, receives the data retrieved from the web service. DataLayer.Web Service has special child elements that are used to call, and pass parameters to, the methods exposed by the SOAP web service.

Both datalayer elements expect to receive XML data beginning with the relevant nodes. However, this may not always be the case: results may have additional parent nodes before the data. To deal with this, both datalayer elements have an **XPath** attribute where XPath queries can be entered for the purpose of selecting the desired data nodes for the datalayer.

Once data from the web service has been retrieved into a datalayer, then all of the usual Logi data handling (filtering, aggregating, etc.) and presentation elements can be applied to it.

For more information and examples of how to use the appropriate elements, see [DataLayer.Web Service](https://devnet.logianalytics.com/hc/en-us/articles/1500009514802-DataLayer-Web-Service) and [DataLayer.REST](https://devnet.logianalytics.com/hc/en-us/articles/1500009514722-DataLayer-REST).
