---
title: "Get Started with the Composer Application Framework"
id: 4405850877335
section: "Composer v6 Developer Tools"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850877335-Get-Started-with-the-Composer-Application-Framework
updated_at: 2021-09-21T01:26:43Z
---

# Get Started with the Composer Application Framework

# Get Started with the Composer Application Framework

Composer's application framework provides you with the tools you need to query data or embed visuals from Composer in your own application. If you want to use Composer visuals or data in your own custom application, then read on. You might be looking for information about creating your own custom charts, see
[*Maintain Custom Charts Using the Custom Chart CLI*](https://devnet.logianalytics.com/hc/en-us/articles/4405859247127-Maintain-Custom-Charts-Using-the-Custom-Chart-CLI).

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg)Logi Analytics recommends using [Trusted Access](https://devnet.logianalytics.com/hc/en-us/articles/4405851181463-Trusted-Access) for all embed-related workflows.

## Uses of the Application Framework

|  |  |
| --- | --- |
|  | **You can use a query to get data from Composer and use it in your own applications.**  You might want to go this route if:   * You just need the data. * You already have a visual built into your application and you want to keep it, but need data for it. |
|  | **You can embed a Composer visual in your application and use your query to supply it with data.**  You might want to go this route if:   * You already have a data query set up. * You need to use the same query for more than one visual or for visuals and other purposes. |
|  | **You can embed a Composer visual and give it the information it needs to create its own query.**  You might want to go this route if you really just need one visual based on its own query. |

## Dependencies

The application framework depends upon jQuery. Composer recommends that you link jQuery v1.8 or later.

## Accessing the Application Framework

Composer's application framework is provided by linking the
`zoomdata-client.js`
file in your web application. You can find `zoomdata-client.js` on your installation at

```
https://<yourserver>/composer/sdk/zoomdata-client.js
```

replacing
`<yourserver>`
with the URL for your server.

Best practice: Use the `zoomdata-client.js` file found on the Composer installation that will be supplying your data and visuals. There is not usually a problem using different versions, but following this guidance avoids such issues and may help Composer support your work.

Linking the zoomdata-client.js file into your web application gives you access to the
`ZoomdataSDK`
object. The main purpose of the ZoomdataSDK object is to create a Composer
client
for your application. Typically, one Composer client is enough, but if you need to access multiple Composer servers, you'll need one client for each one.

## Typical Workflows

There is a lot of flexibility with the Composer application framework, but some steps must precede others. When steps must be kept in a particular order, the Composer application framework uses promises to do so. Below is an example of the most common workflow.

### Typical Workflow to Embed a Visual

This workflow creates a query independent of the visual and then uses that query to supply the visual with data. The advantage to this workflow is that the independent visual can easily be used for additional purposes such as other calculations or supplying the same data to other visuals.

1. Create a Composer client. Steps to create a client are found in [*Use a Data Query*](https://devnet.logianalytics.com/hc/en-us/articles/4405850882839-Use-a-Data-Query).
2. [Create a Composer query](https://devnet.logianalytics.com/hc/en-us/articles/4405850882839-Use-a-Data-Query).
3. [Visualize a Composer visual using data from the query](https://devnet.logianalytics.com/hc/en-us/articles/4405850883735-Embed-a-Visual-in-Your-Web-Page).

To help you get going, you might want to [fiddle with an example](https://jsfiddle.net/user/Zoomdata/fiddles/) or [download it from GitHub](https://github.com/Zoomdata/SDK20-ApplicationFW-samples).

### Typical Workflow to Query Data

This workflow creates a query and then queries data from it. This workflow is useful if you already have visuals in your application and you need to supply them with data from Composer. It's also useful if you just want the data.

1. Create a Composer client. Steps to create a client are found in [*Use a Data Query*](https://devnet.logianalytics.com/hc/en-us/articles/4405850882839-Use-a-Data-Query).
2. [Create a Composer query.](https://devnet.logianalytics.com/hc/en-us/articles/4405850882839-Use-a-Data-Query#Configuring)
3. [Run the Composer query.](https://devnet.logianalytics.com/hc/en-us/articles/4405850882839-Use-a-Data-Query#Running)
4. [Gather and use the queried data.](https://devnet.logianalytics.com/hc/en-us/articles/4405850882839-Use-a-Data-Query#Finding)

To help you get going, you might want to [fiddle with an example](https://jsfiddle.net/user/Zoomdata/fiddles/) or [download it from GitHub](https://github.com/Zoomdata/SDK20-ApplicationFW-samples).

## Next Steps

It might be that you only need to embed a visual or use data from Composer in your own application. Consider the information at the following links:

* [*Embed a Visual in Your Web Page*](https://devnet.logianalytics.com/hc/en-us/articles/4405850883735-Embed-a-Visual-in-Your-Web-Page)
* [*Use a Data Query*](https://devnet.logianalytics.com/hc/en-us/articles/4405850882839-Use-a-Data-Query)
* [*Composer REST API Overview*](https://devnet.logianalytics.com/hc/en-us/articles/4405850881943-Composer-REST-API-Overview)
* [*Maintain Custom Charts Using the Custom Chart CLI*](https://devnet.logianalytics.com/hc/en-us/articles/4405859247127-Maintain-Custom-Charts-Using-the-Custom-Chart-CLI)
* [*Implement OAuth 2.0 with Composer*](https://devnet.logianalytics.com/hc/en-us/articles/4405851172503-Implement-OAuth-2-0-with-Composer)
