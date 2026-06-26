---
title: "Data Fusion Use Cases"
id: 4405851075095
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851075095-Data-Fusion-Use-Cases
updated_at: 2021-09-21T01:28:43Z
---

# Data Fusion Use Cases

# Data Fusion Use Cases

Composer supports the following data fusion use cases:

* Looking up descriptions from lookup tables
* Aggregating data using dimensional tables in a star or snowflake schema
* Joining multiple fact tables on common keys

We’ll explore each use case in greater detail and then demonstrate how you can combine these different scenarios together to build unique data fusion data sets for your research and analysis.

## Fact-to-Lookup Table Use Case

The lookup description is the simplest use case since it is joining a fact table to a lookup table using a common identity key. In this scenario, the description from a lookup table can be visualized along with metrics information from a fact table. The following diagram illustrates an example of a join between the event (lookup table) and the price paid. The common field between the two disparate tables is **event\_id**.

![](https://devnet.logianalytics.com/hc/article_attachments/4406743788055/use-case-lookup-description_384x173.png)

The resulting fused data includes the attributes from the lookup table and the metrics from the fact table. Any additional group-by attributes that are available from the lookup table are displayed as well.

## Star Schema Table Use Case

A star schema table extends the capability of the lookup description use case to dimensional tables that contain attribute descriptions and higher level group-by attributes than on fact table. The fact table can be joined to several dimensional tables using common ID keys (limited to one key per join). This allows you to visualize the fused data set using group-bys and filtering on dimensional attributes sourced from the dimension table in conjunction with metrics from the fact table.

For example, the following diagram illustrates a star schema table. The Sales table is the fused data set resulting from the following disparate data sources: seller details from the Sellers data source, event information from the Events data source, and listing details from the List data source.

  

![](https://devnet.logianalytics.com/hc/article_attachments/4406743789207/table-star-schema_435x288.png)

## Multiple Fact Table Use Case

Composer supports the capability to join different fact tables together. Similar to the lookup description use case, multiple fact tables are joined using a common key. As a result, metrics from different tables can be displayed on the same visual with common keys as the Group By keys. The following diagram shows two disparate fact tables being joined under the common attribute - **seller\_id**.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747413783/table-multiple-facts_488x166.png)

If a join is attempted between tables that have a one-to-many or many-to-many relationship, the table metrics will be duplicated.

## Combination Use Case

You can also fuse data using a combination of these use cases. For example, you can create a lookup to fact to lookup join (as shown in the diagram below) to explore the sellers, their ticket sales and event information all on one visual. In this example, seller information is located in a lookup table, sales data is housed in a fact table, and event details are stored in a lookup table. The common keys connecting these data sets are **user\_id**, **seller\_id**, and **event\_id**.

![](https://devnet.logianalytics.com/hc/article_attachments/4406743789463/combo-use-case_576x308.png)
