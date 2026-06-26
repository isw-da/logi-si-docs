---
title: "Defining an Initial View"
id: 4406822298135
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822298135-Defining-an-Initial-View
updated_at: 2022-04-06T06:05:44Z
---

# Defining an Initial View

# Defining an Initial View

If you were to run the example XOLAP definition shown in [Configuring the Data Cube](https://devnet.logianalytics.com/hc/en-us/articles/4406817378711-Configuring-the-Data-Cube) you would notice that, while we define all the dimensions and measures, when the Dimension Grid is first displayed, no data is actually shown.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563327255/xolapwork_14.png)

The example above shows what a user typically first sees: no data and an instruction to selection a Dimension. What if you want the Dimension Grid to show data right away? Well, we have an element for that.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563327383/xolapwork_20.png)

A special datalayer, **DataLayer.XOLAP Query**, shown above, is used for this purpose. This element, and its child elements, allows you to retrieve the data, identify default Dimensions and Measures, and present the user with visible data the first time the report runs.
