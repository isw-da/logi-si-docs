---
title: "Get Started with the Composer Application Framework"
id: 34932674790029
section: "Composer 25 Developer Tools"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932674790029-Get-Started-with-the-Composer-Application-Framework
updated_at: 2026-05-26T22:10:22Z
---

# Get Started with the Composer Application Framework

# Get Started with the Composer Application Framework

Composer's application framework provides you with the tools you need to query data or embed visuals from Composer in your own application. If you want to use Composer visuals or data in your own custom application, then read on. You might be looking for information about creating your own custom charts, see
[Maintain Custom Charts Using the Custom Chart CLI](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932777064845-Maintain-Custom-Charts-Using-the-Custom-Chart-CLI).

**Note:** insightsoftware recommends using [Trusted Access](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933153713037-Trusted-Access) for all embed-related workflows.

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

https://<yourserver>/composer/sdk/zoomdata-client.js

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

### Typical Workflow to Query Data

This workflow creates a query and then queries data from it. This workflow is useful if you already have visuals in your application and you need to supply them with data from Composer. It's also useful if you just want the data.

1. Create a Composer client. Steps to create a client are found in [Use a Data Query](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932657243149-Use-a-Data-Query).
2. [Create a Composer query.](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932657243149-Use-a-Data-Query#Configuring)
3. [Run the Composer query.](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932657243149-Use-a-Data-Query#Running)
4. [Gather and use the queried data.](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932657243149-Use-a-Data-Query#Finding)

To help you get going, you might want to [fiddle with an example](https://jsfiddle.net/user/Zoomdata/fiddles/) or [download it from GitHub](https://github.com/Zoomdata/SDK20-ApplicationFW-samples).

## Next Steps

It might be that you only need to embed a visual or use data from Composer in your own application. Consider the information at the following links:

* [Use a Data Query](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932657243149-Use-a-Data-Query)
* [Composer REST API Overview](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932682480781-Composer-REST-API-Overview)
* [Maintain Custom Charts Using the Custom Chart CLI](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932777064845-Maintain-Custom-Charts-Using-the-Custom-Chart-CLI)
* [Trusted Access](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933153713037-Trusted-Access)
