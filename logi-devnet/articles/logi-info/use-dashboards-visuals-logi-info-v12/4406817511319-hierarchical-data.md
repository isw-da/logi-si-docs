---
title: "Hierarchical Data"
id: 4406817511319
section: "Use Dashboards & Visuals - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817511319-Hierarchical-Data
updated_at: 2022-04-06T06:06:33Z
---

# Hierarchical Data

# Hierarchical Data

Data in **hierarchical****groups** presents a special challenge
for the Logi developer and this topic introduces several different
techniques for presenting it using data tables.

The following topics discuss Hierarchical Data:

* [Using Group Header and Group Summary Rows](https://devnet.logianalytics.com/hc/en-us/articles/4406817510295-Using-Group-Header-and-Group-Summary-Rows#Rows)
* [Creating a Hierarchical Data Table with Indented Groups](https://devnet.logianalytics.com/hc/en-us/articles/4406817507991-Creating-a-Hierarchical-Data-Table-with-Indented-Groups#DataTable)
* [Creating Hierarchies by Hiding Duplicate Values](https://devnet.logianalytics.com/hc/en-us/articles/4406817507991-Creating-a-Hierarchical-Data-Table-with-Indented-Groups#DupValues)
* [Working with Subdata Tables](https://devnet.logianalytics.com/hc/en-us/articles/4406817512343-Working-with-Subdata-Tables#SubTable)

See the
[Data Grouping Sample](https://sampleapps.logianalytics.com/LambdaExV2/rdPage.aspx?rdReport=DataTable.TableGroups) DevNet for an example related to
this subject.

## About Hierarchical Data

Hierarchical data is data that is grouped into a tree-like structure, with
repeating parent/child relationships:

![](https://devnet.logianalytics.com/hc/article_attachments/4417583905943/hierarchdata_01.png)

For example, the data shown above is in a hierarchy, grouped first by
**Customer**, then by **Order**, with Order Item details. In the
business intelligence reporting world, this is a very common approach to
presenting data and segments the data visually in a way that makes it easy
to understand.

The challenge with HTML-based reports, such as Logi applications, is to
manage the screen real estate effectively when working with hierarchical
data and there are several approaches to doing this. Depending on the
number of columns to be displayed, a straight forward data table can be
used. If that isn't practical, then it may be better to embed a data table
(either as a "subdata" table or an embedded subreport) within a
table to more easily manage the columns; this is discussed in [Subdata Tables](https://devnet.logianalytics.com/hc/en-us/articles/4406818149143-Subdata-Tables). And, finally, placing a subdata table or an embedded
subreportwithin a More Info Row may help to reduce visual clutter, see [Working with "More Info Rows"](https://devnet.logianalytics.com/hc/en-us/articles/4406817267991-Working-with-More-Info-Rows-). The following examples build on the
first approach, which uses a regular data table.

## Restriction when using Input Elements

Some applications display data in a Data Table and include
Input
elements in each row of the table. A common example is a
"Delete" check box for every record. This can be done in Logi
applications, but is *not recommended* when hierarchical data is
being used. The complex data relationships involved make it impossible to
uniquely identify the associated Input elements.

This prohibition applies to obvious hierarchical representations, such as
the Data Table, but also to elements like the Data Tree, which use
hierarchical grouping internally to create their parent-child data
representations.
