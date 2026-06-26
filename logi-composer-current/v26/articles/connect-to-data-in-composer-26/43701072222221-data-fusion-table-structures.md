---
title: "Data Fusion Table Structures"
id: 43701072222221
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072222221-Data-Fusion-Table-Structures
updated_at: 2026-05-29T14:10:43Z
---

# Data Fusion Table Structures

# Data Fusion Table Structures

The following table structures are used when data is fused using Composer's data fusion feature. For examples of these used in data fusion, see [Data Fusion Use Cases](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701104692237-Data-Fusion-Use-Cases).

**Note:** 
You can flag one or both entities used in creating a join for a fused data source as a dimensional entity. See [Create a Fusion Source](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072201741-Create-a-Fusion-Source).

## Lookup Table

A lookup table contains description fields that describe dimensional data. For example, a lookup table may contain information about sellers that includes the seller's username, first name, last name and contact information. But this table may not contain pertinent sales data linked to the seller. This table may need to be joined with a [fact table](#Fact) to provide more insightful information. The following is an example of a lookup table.

![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242466346893)

## Fact Table

A fact table stores measurements, metrics and other analytical information. A fact table typically contains two types of columns:

* Fact columns that contain the measures to analyze
* Dimensional keys to analyze the facts using different attribute contexts.

For example, analyzing quantities sold (fact) and price of tickets (fact) by event would be one context. Another context might be to analyze the same facts by seller. Fact tables may be missing the descriptions needed for categorizing and analyzing the data. Combining fact tables with [lookup tables](#Lookup) may be necessary to conduct proper data analysis.

The following figure illustrates a sample fact table containing sales information that includes the identifiers for each sales transaction along with the related event (and other information).

![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242494677773)

## Star Schema

A star schema consists of one or more fact tables with references to dimension tables. Dimension tables store descriptions for key identifiers in the fact table as well as parent attributes that can allow aggregation of metric data to higher levels. This type of table structure is useful for rolling up and analyzing metric data using various dimensional attributes. The following figure depicts a sample star schema.

![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242466632845)

## Snowflake Schema

A snowflake schema consists of one or more fact tables that have references to multiple dimension tables which in turn may connect to additional dimension tables. The logical arrangement of tables in a multidimensional database when displayed in a diagram resembles a snowflake shape. Like a star schema, dimension tables store descriptions for key identifiers in the fact table as well as parent attributes that can allow aggregation of metric data to higher levels. However, the difference is that the dimension table themselves may connect to additional dimension tables providing further information. The following figure depicts a sample snowflake schema.

![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242466868877)
