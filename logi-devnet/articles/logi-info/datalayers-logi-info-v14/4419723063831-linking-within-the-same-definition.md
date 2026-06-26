---
title: "Linking Within the Same Definition"
id: 4419723063831
section: "Datalayers - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723063831-Linking-Within-the-Same-Definition
updated_at: 2023-02-16T16:01:58Z
---

# Linking Within the Same Definition

# Linking Within the Same Definition

When we have a need to re-use the data from the datalayer, we can do so using the **DataLayer.Linked** element:

![](https://devnet.logianalytics.com/hc/article_attachments/5163511414807/dllinked_04.png)

1. As shown above, in the same definition, a Data Table has been added and we'd like to use it to present some of the same data retrieved earlier for the selection list.
2. A **DataLayer.Linked** element has been added beneath the Data Table.
3. Its **Link ID** attribute has been set to the ID of the Data Layer Link element we used earlier. This makes the data retrieved earlier available for use in the table.
4. Linked data can subsequently be manipulated using standard elements, such as the Sort Filter.

That's all there is to it. Multiple DataLayer.Linked elements can be used in a definition; because each one represents the original data, sorts and filters applied to one will not affect the data in another.

This technique is especially useful when presenting the same data in *different ways* in a single report; for example, by using a table and a chart of some kind. Logi charts can use DataLayer.Linked as their datalayer and re-use the data retrieved for the table.

![](https://devnet.logianalytics.com/hc/article_attachments/5163469731607/noteicon.png) Due to order-of-operations differences, datalayers that have the [Handle Quotes Inside Tokens](https://clm.logianalytics.com/rdPage.aspx?rdReport=ElementRefDetail&itemID=999&iName=HandleQuotesInTokens&iType=Attribute&iLabel=Handle+Quotes+Inside+Tokens&lnkpg=0&dnView=G-I&dnSelect=Attribute) attribute set to *True* will not process quotes as expected
when used underneath Chart
Canvas elements. In this scenario, we recommend that you use the datalayer under Local Data and link it, using the techniques described in this topic, to a datalayer for the chart.

![](https://devnet.logianalytics.com/hc/article_attachments/5163479892119/criticalicon.png) A datalayer used to retrieve data for a chart *cannot* be linked later in the definition for use with a Data Table. This is because the data retrieved into a datalayer for a chart is processed somewhat differently than data retrieved for a table. However, the reverse usage, a datalayer beneath a Data Table linked to a datalayer beneath a chart later in the definition is okay.
Some developers, faced
with this
restriction, prefer to use a **Local Data** element to retrieve the data, then link its datalayer to both a chart and Data Table later in the definition.
