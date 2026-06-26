---
title: "Data Fusion Join Rules"
id: 4405851073175
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851073175-Data-Fusion-Join-Rules
updated_at: 2021-09-21T01:28:44Z
---

# Data Fusion Join Rules

# Data Fusion Join Rules

Data fusion joins are key to the success of your attempts to fuse data. So they must adhere to the rules described in this section.

You can explicitly specify the [type of join](https://www.w3schools.com/sql/sql_join.asp) that occurs for fusion: [inner join](https://www.w3schools.com/sql/sql_join_inner.asp), [left outer join](https://www.w3schools.com/sql/sql_join_left.asp), or [full outer join](https://www.w3schools.com/sql/sql_join_full.asp). [Right outer joins](https://www.w3schools.com/sql/sql_join_right.asp) are not supported. The join type can be selected for each pair of mapped fields in a join condition.

The following diagram depicts the relationship between the data sources included in a Fusion data source and the join definitions and join conditions (mappings) defined in a Fusion data source.

![](https://devnet.logianalytics.com/hc/article_attachments/4406743793431/fusion-joins_436x304.png)

The following rules must be adhered to for data fusion joins:

1. Joins are processed in the order in which they are specified in the UI. This affects the resulting data and the performance of the join.
2. Only a single join definition is allowed between two data sources. The join definition can contain multiple join conditions (mappings), previously called *forms*. Each mapping must contain exactly two fields. The fields used in the mapping must be of the same type and should contain the same kind of data.

   If there are more than two data sources in a Fusion data source definition, a single join definition can be specified for each unique combination of the included data sources. For example, if you have four data sources in your Fusion data source definition (sources A, B, C, and D), you can specify six join definitions, one each for these source combinations: A+B, A+C, A+D, B+C, B+D, and C+D.
3. Every data source in a Fusion data source must be connected to at least one other data source in the fused source. The data sources in a Fusion data source must be interconnected in some way.

   For example, if you have four data sources (A, B, C, and D) in your Fusion data source definition, you cannot define only a join between sources A and B and a second join between sources C and D. In addition, all the sources must be connected in some way to one of the others. So the following join sequence would be correct because every data source is included: A+B, B+D, D+C. However, the following join sequence would be incorrect because source C is entirely omitted: A+B, A+D, B+D.
4. Each subsequent join in the Fusion data source configuration must use a source from one of the previously defined joins.

   For example, if you have four data sources (A, B, C, and D) in your Fusion data source definition, if a join between sources A and B is the first join defined, the second join defined for the fused source must include either source A or source B and one of the other sources (C or D). So the following join sequence would be correct: A+B, B+D, D+C. However, the following join sequence would be incorrect because source C and D are introduced before they have been linked to either source A or source B: A+B, D+C, B+D.
5. The data in mapped time fields must have the same granularity. Composer assumes that the granularity of a time field correctly matches the granularity of its data. For example, if one time field contains data in days and another time field contains data in seconds, they cannot be joined. The only way to join these two time fields would be to modify the granularity of the underlying data in the data store.
6. When [data source permissions](https://devnet.logianalytics.com/hc/en-us/articles/4405859328535-About-Data-Source-Permissions) are granted to a fused data source, read permission is automatically granted to all the data sources in the fused data source. Appropriate warning messages are provided when adding permission for a fused data source and when removing permissions for one of the sources in the fused source.
7. Fused data sources respect the row security filters and permissions established for the underlying data sources joined in the fused data source.
