---
title: "Link Datalayers"
id: 1500009530221
section: "Introduction to Datasource Connections"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009530221-Link-Datalayers
updated_at: 2022-03-03T08:57:54Z
---

# Link Datalayers

# Link Datalayers

Datalayers **retrieve** and **cache** data, and it's often useful to avoid additional datasource queries by allowing one datalayer to **share** data that's already been cached by another. This topic discusses the technique of **linking datalayers** for this purpose.

* Making a DataLayer Link Available
* [Linking Within the Same Definition](#SameDef)
* [Linking Across Different Definitions](#DifferentDefs)

Developers are always looking for ways to **improve performance**, particularly where database queries are concerned. Developers of Logi applications can improve performance by eliminating **multiple queries** of the same data, through use of a feature that allows data retrieved into one datalayer to be saved and **reused** elsewhere within the application.

Two elements are used in this process: the first one, **Data Layer Link**, identifies the data to be saved and made available; and the second one, **DataLayer.Linked**, provides a way to access and reuse that data.

## Making a DataLayer Link Available

The following example illustrates how to make the data in a datalayer reusable:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771862935/dllinked_01.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778698519/dllinked_01a.gif)

1. As shown above, the example definition contains an **Input Select List** and **DataLayer.SQL** elements. The datalayer uses a regular SQL query to retrieve data from the database to present as options in the selection list.
2. Beneath the datalayer, a **Data Layer Link** element has been added. The effect of the element is to "save" a copy of the data for future use. **Important:** it must be given a *unique* ID.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778698775/dllinked_03.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771863191/dllinked_03a.gif)

Note that, if you use elements to filter, condition, etc. the data in the datalayer, then the *position* of the Data Layer Link in the element tree is significant. For example, above left, the **raw data**, as it was retrieved from the database, will be available for reuse. But, above right, only the **conditioned** and **sorted****data** will be available.  
  
![](https://logianalytics.zendesk.com/hc/article_attachments/4402771863447/dllinked_03b.gif)

You can even use *multiple* Data Layer Link elements beneath a datalayer. In the example above, *both* the raw and the conditioned/sorted data would be available for re-use.

The data in the datalayer is now available for reuse, saving us one or more queries later in our application.

## Linking Within the Same Definition

Now, when we have a need to reuse the data from the datalayer, we can do so using the **DataLayer.Linked** element:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771863703/dllinked_02.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771863959/dllinked_02a.gif)

1. As shown above, in the same definition, a **Data Table** has been added and we'd like to use it to present some of the same data retrieved earlier for the selection list.
2. A **DataLayer.Linked** element has been added beneath the Data Table.
3. Its **Link ID** attribute has been set to the ID of the Data Layer Link element. This makes the data retrieved earlier available for use in the table. It can even be manipulated using standard elements, such as the Sort and Condition Filters.

That's all there is to it. **Multiple** DataLayer.Linked elements can be used in a definition; because each one represents the original data, sorts and filters applied to one will not affect the data in another.

This technique is especially useful when presenting the same data in **different ways** in a single report; for example, by using a **table** and a **chart** of some kind. Logi charts can use DataLayer.Linked as their datalayer and reuse the data retrieved for the table.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771462807/stopicon.gif)   A datalayer used beneath a chart *cannot* be linked later in the definition to a table; this is because the data retrieved into a datalayer beneath a chart is processed somewhat differently than data retrieved for a table. However, the reverse usage, a datalayer beneath a table linked to a datalayer beneath a chart later in the definition is okay. Some developers, faced
with this
situation, prefer to use a LocalData element to retrieve the data, then link its datalayer to both a chart and table later in the definition.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif)   Prior to v11.0.727, you could not use a **DataLayer Link** element beneath DataLayer.XOLAP Query used with an OLAP Grid. This arrangement was not allowed and caused a "pipeline processing" error. In v11.0.727+, the link is allowed.

## Linking Across Different Definitions

As we've seen above, data can be reused by linking datalayers within the same definition. They can also be reused in the same manner **across different definitions**. This is done by making the definition that wants to reuse the data a "target" of the definition that originally retrieves the data. The target report then includes a DataLayer.Linked element.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778699031/DLLinked_04.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771864215/DLLinked_04a.gif)

1. As shown above, the "parent" definition has been modified to include **Label**, **Action.Report**, and **Target.Report** elements. This makes the label text become a link to the next report.
2. To make the reusable data available in the next ("child") report, the Target.Report element's **Link Data Layers** attribute has been set to *True*.
3. In the child report definition ("MyDetailReport"), a **DataLayer.Linked** element is used in the same manner shown in the previous section in order to access the reusable data.

This cross-definition linking is also available in **Target.Export Word**, **Target.Export Excel**, and **Target.Template**.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif) If you're considering opening your child report in a new window, keep in mind that linked data is only available in the *same session*. For example, if you specify "New Window" in your Target element's **Frame ID** attribute and run the parent report inside Studio's Preview window, the linked datalayer won't be found. This happens because the new window opened for the child report will
be outside
of Studio and will start its own new session.

However, under most default browser
configurations, when you run the parent report in a browser window, the new window for the child report will be opened in new *tab*, which uses the same session, and the linked datalayer will be found. But, if your browser is configured to open a new *window* for each new URL and that causes a new session to be started, then the linked datalayer will not be found by the child report.

The ability to link datalayers within and across definitions is a **powerful feature** in Logi applications and a **good technique** for developers who want to reduce the number of datasource queries they need to issue.
