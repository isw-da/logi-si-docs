---
title: "Create a New Report Definition"
id: 4406817270423
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817270423-Create-a-New-Report-Definition
updated_at: 2022-04-06T06:05:04Z
---

# Create a New Report Definition

# Create a New Report Definition

This topic demonstrates how to create a new report definition in Logi Studio.

1. Begin by launching **Logi Studio**, using its desktop icon or Start![](https://devnet.logianalytics.com/hc/article_attachments/4417583616279/menuarrowrt.png)All Programs![](https://devnet.logianalytics.com/hc/article_attachments/4417583616279/menuarrowrt.png)Logi Info![](https://devnet.logianalytics.com/hc/article_attachments/4417583616279/menuarrowrt.png)Studio.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575778967/datatableman_01.png)

2. In Logi Studio, close the Getting Started dialog box and re-open the **HelloWorld** application from the Welcome Panel, as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584035095/datatableman_02.png)

3. Click the **New File** menu item, and select *Report* from its drop-down list of options, as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563395991/datatableman_03.png)
Studio will add a new report definition, named "newReport" in the Application Panel, and put it into rename mode. Just start typing a new name - such as "**MyDataTable2**" - and press Enter to rename it.

If something happens, like you click elsewhere, and it exits rename mode, just select the newReport definition and press F2, or right-click and select *Rename*, to rename it.  

You probably noticed that the new definition was opened in the Workspace editor. It contains five key elements by default:

* The **Root** element of the report. Its ID is the report definition name, in this example, "MyDataTable2", and
* A **Body** element, a container for displaying the main report content (tables, charts, controls, etc.)

Any report that displays data in a table also requires five more types of elements, which we'll work with next:

* A **Connection** to the database or other data source*.*
* A **Data Table** element, which defines the data presentation (rows and columns).
* A **DataLayer** element, to retrieve and cache the data.
* One or more **Data Table Column** elements, to organize the data.
* A **Label** element in each column to format and display the actual data.

  
Your next step is to create a connection to your database server.
