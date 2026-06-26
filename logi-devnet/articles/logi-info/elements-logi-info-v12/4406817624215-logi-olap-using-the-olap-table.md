---
title: "Logi OLAP - Using the OLAP Table"
id: 4406817624215
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817624215-Logi-OLAP-Using-the-OLAP-Table
updated_at: 2022-04-06T06:07:16Z
---

# Logi OLAP - Using the OLAP Table

# Logi OLAP - Using the OLAP Table

The **OLAP Table** element displays OLAP data in a data table, without
any of the built-in user input controls for filtering and drilling down
into the data found in the OLAP Grid. This element is useful if you just
want to display data or you prefer to add your own user input elements.
Like the OLAP Grid, the OLAP Table gets its data from a
**DataLayer.MDX** element, and an **MDX Query** element can be used
with the datalayer to automatically generate the query.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575616279/getstartolap_33.png)

Or, if you prefer, instead of using the MDX Query element, you can enter
your own query in the datalayer's **MDX Source** attribute, as shown
above. This attribute is only functional when used with an OLAP Table and
is ignored when the datalayer is used with the OLAP Grid.
The OLAP Table elements has all of the attributes of a Data Table and also
includes the **Level Indent** and **OLAP Cell Colors** attributes
from the OLAP Grid.
There are no Data Table Column child elements needed when using the OLAP
Table; it includes an "auto columns" functionality and
automatically shows all columns in the datalayer.
