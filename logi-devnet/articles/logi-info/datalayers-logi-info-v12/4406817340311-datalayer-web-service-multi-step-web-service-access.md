---
title: "DataLayer.Web Service - Multi-Step Web Service Access"
id: 4406817340311
section: "Datalayers - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817340311-DataLayer-Web-Service-Multi-Step-Web-Service-Access
updated_at: 2022-04-06T06:05:28Z
---

# DataLayer.Web Service - Multi-Step Web Service Access

# DataLayer.Web Service - Multi-Step Web Service Access

Some web services require **multiple** interaction steps before they will return a result. For example, you may first need to tell the web service your security credentials, then tell it what data category you need, then tell it what format to put the results in, and then request the actual data. A single **DataLayer.Web Service** element is not designed for this kind of multi-step "conversation" with a web service. So how can this be accomplished?

One approach is to use *multiple* DataLayer.Web Service elements, one for each part of the conversation. In your report, just add multiple DataLayer.Web Service elements, one for each part of the conversation, and they will execute one after another.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563372567/dlwebsvc_10.png)

In the example shown above, multiple DataLayer.Web Service elements are used, with each calling a different web service method, to complete the multi-step conversation required by the web service. The last one sends the query and the data is retrieved and available using standard @Data tokens.

Another approach is to write a **plug-in** to handle the multi-step conversation. When used with[DataLayer.Plugin](https://devnet.logianalytics.com/hc/en-us/articles/4406816911767-DataLayer-Plugin), the plug-in would issue the sequential web service method calls and place the resulting data into the datalayer for use in the report. DevNet members, after login, can see an example of this type of plug-in in action in our [Web Service
with Complex Header](https://devnet.logianalytics.com/hc/en-us/articles/360047205234-Web-Service-with-Complex-Header) sample plug-in.

For more information, our [Web Service Sample Application](https://devnet.logianalytics.com/hc/en-us/articles/360049630754-Web-Services-Sample-Application) demonstrates the use of DataLayer.Web Service.
