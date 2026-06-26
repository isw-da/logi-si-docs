---
title: "DataLayer.Definition List - Example Usage: With an Input Select List"
id: 4406817293847
section: "Datalayers - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817293847-DataLayer-Definition-List-Example-Usage-With-an-Input-Select-List
updated_at: 2022-04-06T06:05:13Z
---

# DataLayer.Definition List - Example Usage: With an Input Select List

# DataLayer.Definition List - Example Usage: With an Input Select List

In the following example, you'll see how to use DataLayer.Definition List with an **Input Select List** element, so that users can select report definitions to see at runtime.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584028823/dldeflist_01.png)

Start by adding an **Input Select List** element to your report definition and setting its attributes as shown above. Referring to the table of returned columns from [DataLayer.Definition List - Working with DataLayer.Definition List](https://devnet.logianalytics.com/hc/en-us/articles/4406817294999-DataLayer-Definition-List-Working-with-DataLayer-Definition-List), use "DefinitionName" for the Caption Column and Value Column attribute values.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563389975/dldeflist_02.png)

Next, add a **DataLayer.Definition List** element beneath the input element, as shown above. You only want to present users with a choice of *report* definitions, so set the Definition List Folder attribute to *\_Reports*. Without this, they'd also see Process, Widget, and all other definitions.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563390103/dldeflist_03.png)

When you preview the report, you see that your list is populated, but there's a problem: the list includes many report definitions in subfolders that you don't want users to see. To fix this, filter the datalayer:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575774231/dldeflist_04.png)

As shown above, add a **Compare Filter** beneath the datalayer. Set its attributes to keep only definitions that have an underscore in their names.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563390359/dldeflist_05.png)

Now when we preview the definition again, we see that the list includes the desired set of definitions.
