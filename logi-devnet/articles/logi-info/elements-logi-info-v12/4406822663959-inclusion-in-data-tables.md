---
title: "Inclusion in Data Tables"
id: 4406822663959
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822663959-Inclusion-in-Data-Tables
updated_at: 2022-04-06T06:10:31Z
---

# Inclusion in Data Tables

# Inclusion in Data Tables

Some applications display data in a Data Table and include **user input** elements in each row of the table. A common example is a "Delete" check box for every record.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575411991/workingui_12.png)  

This can be done in Logi applications, but generally requires use of a Process Task to process the input values. DevNet offers a [sample application](http://sampleapps.logianalytics.com/SampleProcessUpdateTable/rdPage.aspx?rdReport=MultipleRows) that shows you the coding techniques for doing this.
In addition, this technique is *not recommended* when hierarchical data is being used. The complex data relationships involved make it impossible to uniquely identify the associated user input elements. This prohibition applies to obvious hierarchical representations, such as the **Data Table**, and also to elements like the **Data Tree**, which use hierarchical grouping internally to create their parent-child data representations.
