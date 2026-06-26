---
title: "Repeat Elements"
id: 4419723219991
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723219991-Repeat-Elements
updated_at: 2022-07-17T01:34:53Z
---

# Repeat Elements

# Repeat Elements

The **Repeat Elements** element allows data-driven replication of elements, making Logi report definitions dynamic and able to automatically accommodate data schema changes.

The following topics discuss the use of the Repeat Elements element:

* [Example: Building a Comma-Separated String of Values](https://devnet.logianalytics.com/hc/en-us/articles/4419707893143-Repeat-Elements-Example-Building-a-Comma-Separated-String-of-Values#CSV)
* [Example: Dynamic Data Table Columns](https://devnet.logianalytics.com/hc/en-us/articles/4419707894935-Repeat-Elements-Example-Dynamic-Data-Table-Columns#DTColumns)
* [Example: Dynamic Tables with Nested Repeat Elements](https://devnet.logianalytics.com/hc/en-us/articles/4419715529239-Repeat-Elements-Example-Dynamic-Tables-with-Nested-Repeat-Elements#Nested)
* [Example: Dynamic Analysis Grid Columns](https://devnet.logianalytics.com/hc/en-us/articles/4419707894039-Repeat-Elements-Example-Dynamic-Analysis-Grid-Columns#AGColumns)

## About the Repeat Elements Element

It's not unusual for Logi developers to encounter situations in which there's an uncertainty about the data they're working with. That uncertainty makes it hard to know, during development, how many Logi elements are necessary to present the data in a report definition. This may be due to a changing database schema, or to expanding data, or other reasons.

For example, imagine a scenario in which you're creating a monthly report that displays a table for each project proposal your company receives during the month. However, the number of proposals varies widely each month. How can you create a report with a Data Table for each project if you don't know how many of them there will be (short of editing the definition each month, which is hardly efficient)?

Another example is a situation in which you want to significantly *reduce* the *number* of elements in, and shorten, a report definition, just to make it easier to work with.

The **Repeat Elements** element is the right tool for these and similar jobs! It's associated with a datalayer and iterates through each row, telling the Logi Server Engine at runtime to create a complete set of its child elements for each row.

![](https://devnet.logianalytics.com/hc/article_attachments/4419707113623/repeatele_01_601x192.png)

In the definition example above, left, a **Repeat Elements** element is used. It has its own datalayer and two other child elements: a **Label** and a **New Line**. All of the child elements, except the datalayer, will be replicated - one set of child elements for *each* datalayer row - by the Logi Server Engine at runtime. The result is shown above, right.

A special token, @Repeat, is used to represent the data. In the example above, the **Caption** of the Label element is configured as:

Category: @Repeat.CategoryName~

As usual, the second part of the token is the name of a column in the datalayer.

Yes, you could have just as easily gotten the same result using a regular Data Table. However, the value of the Repeat Elements element will become more obvious as we go along. The Repeat Elements element can be used *anywhere* in a report definition, and it can take almost every other element as a child element (except as noted below), so you have a lot of flexibility in using it. In the following sections, you'll see examples of a variety of use-cases for this element.

### Some Token & Element Restrictions

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599319/criticalicon.png) Repeat Elements are one of the very *first* things processed when a page goes through the Logi Server Engine and, therefore, some elements and values that are processed *later* are not available for use with Repeat Elements, including:

* @Local tokens
* @Session tokens for variables that are set in the definition using the **Set Session Variables** element
* @Request tokens for variables that are set in the definition using the **Default Request Parameters** element
* Do not use **DataLayer.Linked** to provide data to Repeat Elements
* Do not include Repeat Elements in a **Shared Element**; it will not be processed
