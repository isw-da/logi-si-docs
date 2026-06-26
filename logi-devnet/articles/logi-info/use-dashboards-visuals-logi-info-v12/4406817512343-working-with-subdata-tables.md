---
title: "Working with Subdata Tables"
id: 4406817512343
section: "Use Dashboards & Visuals - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817512343-Working-with-Subdata-Tables
updated_at: 2022-04-06T06:06:32Z
---

# Working with Subdata Tables

# Working with Subdata Tables

As mentioned earlier, another method of presenting hierarchical data is
to use a subdata table beneath a Data Table Column or More Info Row
element, see [Data Table Rows](https://devnet.logianalytics.com/hc/en-us/articles/4406822236823-Data-Table-Rows).
*We don't generally recommend this approach, although the necessary
elements remain in Logi Info for backward compatibility*.

Subdata tables receive data from the **Subdata Layer** element, which
uses a standard datalayer to retrieve data and then relates its columns to
those of the parent data table's datalayer.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png)
Most developers find it easier to use a subreport that includes a
regular data table, rather than a subdata table. One advantage to this
approach is that a subreport, which is a separate report definition, can
be independently developed and tested, and then embedded in a parent
report using the SubReport element. This technique works well with the
More Info Row element and does not require hierarchical data. More
information is available in
[SubReports](https://devnet.logianalytics.com/hc/en-us/articles/4406822672663-SubReports).

![](https://devnet.logianalytics.com/hc/article_attachments/4417563255703/hierarchdata_17.png)

The example definition shown above employs two More Info Row elements and
two Subdata Table elements to create a hierarchy of data from the previous
examples. In this case, the detail data may not always be visible in the
report and may require the user to do some clicking to make it visible.

For information about using subdata tables, see
[Subdata Tables](https://devnet.logianalytics.com/hc/en-us/articles/4406818149143-Subdata-Tables).
