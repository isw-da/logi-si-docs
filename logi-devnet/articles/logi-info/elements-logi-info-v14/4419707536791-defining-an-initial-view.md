---
title: "Defining an Initial View"
id: 4419707536791
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707536791-Defining-an-Initial-View
updated_at: 2022-07-17T01:51:13Z
---

# Defining an Initial View

# Defining an Initial View

If you were to run the example XOLAP definition shown in [Configuring the Data Cube](https://devnet.logianalytics.com/hc/en-us/articles/4419707535895-Configuring-the-Data-Cube) you would notice that, while we define all the dimensions and measures, when the Dimension Grid is first displayed, no data is actually shown.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714738455/xolapwork_14.png)

The example above shows what a user typically first sees: no data and an instruction to selection a Dimension. What if you want the Dimension Grid to show data right away? Well, we have an element for that.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699693719/xolapwork_20.png)

A special datalayer, **DataLayer.XOLAP Query**, shown above, is used for this purpose. This element, and its child elements, allows you to retrieve the data, identify default Dimensions and Measures, and present the user with visible data the first time the report runs.
