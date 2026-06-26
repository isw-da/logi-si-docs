---
title: "Data Fusion Table Structures"
id: 4405851074199
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851074199-Data-Fusion-Table-Structures
updated_at: 2021-09-21T01:28:42Z
---

# Data Fusion Table Structures

# Data Fusion Table Structures

The following table structures are used when data is fused using Composer's data fusion. For examples of these used in data fusion, see [*Data Fusion Use Cases*](https://devnet.logianalytics.com/hc/en-us/articles/4405851075095-Data-Fusion-Use-Cases).

## Lookup Table

A lookup table contains description fields that describe dimensional data. For example, a lookup table may contain information about sellers that includes the seller's username, first name, last name and contact information. But this table may not contain pertinent sales data linked to the seller. This table may need to be joined with a [fact table](#Fact) to provide more insightful information. The following is an example of a lookup table.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747414039/table-lookup.png)

## Fact Table

A fact table stores measurements, metrics and other analytical information. A fact table typically contains two types of columns:

* Fact columns that contain the measures to analyze
* Dimensional keys to analyze the facts using different attribute contexts.

For example, analyzing quantities sold (fact) and price of tickets (fact) by event would be one context. Another context might be to analyze the same facts by seller. Fact tables may be missing the descriptions needed for categorizing and analyzing the data. Combining fact tables with [lookup tables](#Lookup) may be necessary to conduct proper data analysis.

The following figure illustrates a sample fact table containing sales information that includes the identifiers for each sales transaction along with the related event (and other information).

![](https://devnet.logianalytics.com/hc/article_attachments/4406743789719/table-fact.png)

## Star Schema

A star schema consists of one or more fact tables with references to dimension tables. Dimension tables store descriptions for key identifiers in the fact table as well as parent attributes that can allow aggregation of metric data to higher levels. This type of table structure is useful for rolling up and analyzing metric data using various dimensional attributes. The following figure depicts a sample star schema.

![](https://devnet.logianalytics.com/hc/article_attachments/4406743790103/use-case-star-schema_425x324.png)

## Snowflake Schema

A snowflake schema consists of one or more fact tables that have references to multiple dimension tables which in turn may connect to additional dimension tables. The logical arrangement of tables in a multidimensional database when displayed in a diagram resembles a snowflake shape. Like a star schema, dimension tables store descriptions for key identifiers in the fact table as well as parent attributes that can allow aggregation of metric data to higher levels. However, the difference is that the dimension table themselves may connect to additional dimension tables providing further information. The following figure depicts a sample snowflake schema.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747414295/concept-snowflake_465x291.png)
