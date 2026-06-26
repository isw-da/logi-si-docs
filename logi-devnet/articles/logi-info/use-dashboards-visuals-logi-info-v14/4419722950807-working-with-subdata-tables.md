---
title: "Working with SubData Tables"
id: 4419722950807
section: "Use Dashboards & Visuals - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722950807-Working-with-SubData-Tables
updated_at: 2022-07-17T01:47:34Z
---

# Working with SubData Tables

# Working with SubData Tables

As mentioned earlier, another method of presenting hierarchical data is
to use a subData Table beneath a Data Table Column or More Info Row
element, see [Data Table Rows](https://devnet.logianalytics.com/hc/en-us/articles/4419707464855-Data-Table-Rows).
*We don't generally recommend this approach, although the necessary
elements remain in Logi Info for backward compatibility*.

SubData Tables receive data from the **Subdata Layer** element, which
uses a standard datalayer to retrieve data and then relates its columns to
those of the parent Data Table's datalayer.

![](https://devnet.logianalytics.com/hc/article_attachments/5163479892119/criticalicon.png)
Most developers find it easier to use a subreport that includes a
regular Data Table, rather than a subData Table. One advantage to this
approach is that a subreport, which is a separate report definition, can
be independently developed and tested, and then embedded in a parent
report using the SubReport element. This technique works well with the
More Info Row element and does not require hierarchical data. More
information is available in
[SubReports](https://devnet.logianalytics.com/hc/en-us/articles/4419708006551-SubReports) .

![](https://devnet.logianalytics.com/hc/article_attachments/5163513099927/hierarchdata_17.png)

The example definition shown above employs two More Info Row elements and
two SubData Table elements to create a hierarchy of data from the previous
examples. In this case, the detail data may not always be visible in the
report and may require the user to do some clicking to make it visible.

For information about using SubData Tables, see
[SubData Tables](https://devnet.logianalytics.com/hc/en-us/articles/4419715627159-SubData-Tables).
