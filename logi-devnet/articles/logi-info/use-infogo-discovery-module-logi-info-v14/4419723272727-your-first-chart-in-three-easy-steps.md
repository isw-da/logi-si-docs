---
title: "Your First Chart in Three Easy Steps"
id: 4419723272727
section: "Use InfoGo/Discovery Module - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723272727-Your-First-Chart-in-Three-Easy-Steps
updated_at: 2022-07-17T01:30:53Z
---

# Your First Chart in Three Easy Steps

# Your First Chart in Three Easy Steps

Let's make your first visualization, a bar chart, so you can see how easy
it is to do. In this, and the following examples, we'll use data from the
Northwind database but you can use any data with similar data types to
follow along.

In this example, we'll create a chart that shows the sum of freight
charges by county. Run your application and access the Thinkspace.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699974551/dm30_usingts_02_409x425.png)

Step 1. After the Thinkspace loads, select the **Bars** chart from the
visualizations menu on the left of the page, as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714954903/dm30_usingts_03_630x426.png)

Step 2. Two blue "drop zones" will appear, as shown above. In
the Data Table, click the Country column "pill", drag it to the
Label drop zone, and drop it there. We call the line that appears when you
drag a pill the "Blue Dot Connector".

![](https://devnet.logianalytics.com/hc/article_attachments/4419707154967/dm30_usingts_04_657x426.png)

Step 3. Repeat the process by dragging the Freight column pill into the
Data drop zone, as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699974807/dm30_usingts_05_670x346.png)

A chart will be instantly generated, as shown above. You've just learned
the Thinkspace's most important technique: dragging and dropping pills.
That *was* easy, wasn't it?

![](https://devnet.logianalytics.com/hc/article_attachments/4419699975063/dm30_usingts_06_682x329.png)

However, it can be *even easier*. We can combine all three steps into
*one*! Let's start over: click the red trash canicon in the
upper-right corner to remove the chart. Now, just drag the Data Table's
Country column pill and drop it onto the Freight column pill, as shown
above. The same chart will be rendered.

Here's what happened: The Thinkspace automatically "recommended"
the Bars chart as the best fit for the data. The column pill that you
dragged the Blue Dot Connector *from* (Country) was identified as the
Y-axis or Label values, and the pill you *dropped it on* (Freight)
was identified as the X-axis or Data values. The chart was then rendered.
Notice that the pills for each column also appear next to the chart in the
appropriate axis zones.
