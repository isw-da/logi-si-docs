---
title: "Repeat Elements"
id: 4406817974295
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817974295-Repeat-Elements
updated_at: 2022-04-06T06:09:21Z
---

# Repeat Elements

# Repeat Elements

The **Repeat Elements** element allows data-driven replication of elements, making Logi report definitions dynamic and able to automatically accommodate data schema changes.

The following topics discuss the use of the Repeat Elements element:

* [Example: Building a Comma-Separated String of Values](https://devnet.logianalytics.com/hc/en-us/articles/4406817970967-Repeat-Element-Example-Building-a-Comma-Separated-String-of-Values#CSV)
* [Example: Dynamic Data Table Columns](https://devnet.logianalytics.com/hc/en-us/articles/4406822568087-Repeat-Element-Example-Dynamic-Data-Table-Columns#DTColumns)
* [Example: Dynamic Tables with Nested Repeat Elements](https://devnet.logianalytics.com/hc/en-us/articles/4406817973271-Repeat-Element-Example-Dynamic-Tables-with-Nested-Repeat-Elements#Nested)
* [Example: Dynamic Analysis Grid Columns](https://devnet.logianalytics.com/hc/en-us/articles/4406817971991-Repeat-Element-Example-Dynamic-Analysis-Grid-Columns#AGColumns)

## About the Repeat Elements Element

It's not unusual for Logi developers to encounter situations in which there's an uncertainty about the data they're working with. That uncertainty makes it hard to know, during development, how many Logi elements are necessary to present the data in a report definition. This may be due to a changing database schema, or to expanding data, or other reasons.

For example, imagine a scenario in which you're creating a monthly report that displays a table for each project proposal your company receives during the month. However, the number of proposals varies widely each month. How can you create a report with a Data Table for each project if you don't know how many of them there will be (short of editing the definition each month, which is hardly efficient)?

Another example is a situation in which you want to significantly *reduce* the *number* of elements in, and shorten, a report definition, just to make it easier to work with.

The **Repeat Elements** element is the right tool for these and similar jobs! It's associated with a datalayer and iterates through each row, telling the Logi Server Engine at runtime to create a complete set of its child elements for each row.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583685015/repeatele_01_601x192.png)

In the definition example above, left, a **Repeat Elements** element is used. It has its own datalayer and two other child elements: a **Label** and a **New Line**. All of the child elements, except the datalayer, will be replicated - one set of child elements for *each* datalayer row - by the Logi Server Engine at runtime. The result is shown above, right.

A special token, @Repeat, is used to represent the data. In the example above, the **Caption** of the Label element is configured as:

Category: @Repeat.CategoryName~

As usual, the second part of the token is the name of a column in the datalayer.

Yes, you could have just as easily gotten the same result using a regular Data Table. However, the value of the Repeat Elements element will become more obvious as we go along. The Repeat Elements element can be used *anywhere* in a report definition, and it can take almost every other element as a child element (except as noted below), so you have a lot of flexibility in using it. In the following sections, you'll see examples of a variety of use-cases for this element.

### Some Token & Element Restrictions

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) Repeat Elements are one of the very *first* things processed when a page goes through the Logi Server Engine and, therefore, some elements and values that are processed *later* are not available for use with Repeat Elements, including:

* @Local tokens
* @Session tokens for variables that are set in the definition using the **Set Session Variables** element
* @Request tokens for variables that are set in the definition using the **Default Request Parameters** element
* Do not use **DataLayer.Linked** to provide data to Repeat Elements
* Do not include Repeat Elements in a **Shared Element**; it will not be processed
