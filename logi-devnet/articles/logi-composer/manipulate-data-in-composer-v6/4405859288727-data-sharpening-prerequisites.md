---
title: "Data Sharpening Prerequisites"
id: 4405859288727
section: "Manipulate Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859288727-Data-Sharpening-Prerequisites
updated_at: 2021-09-21T01:27:59Z
---

# Data Sharpening Prerequisites

# Data Sharpening Prerequisites

Before you use Data Sharpening, verify that your data source configuration has enabled it. See [*Enable Data Sharpening and Configure Its Defaults*](https://devnet.logianalytics.com/hc/en-us/articles/4405851007127-Enable-Data-Sharpening-and-Configure-Its-Defaults).

Before Composer can perform Data Sharpening with a data source, a "playable" time field is required. Composer attempts to automatically detect this playable field from your data source when it is defined. To determine what makes a time attribute "playable," refer to the table below. In addition, an appropriate time attribute must be specified in your data source's global default settings on the Visuals page of the data source configuration. The granularity of this time field is referred to as the *driving time field granularity* (DTFG) and plays an important role in determining whether and how Data Sharpening is executed (see [*When Data Sharpening Occurs*](https://devnet.logianalytics.com/hc/en-us/articles/4405851008919-When-Data-Sharpening-Occurs)). See [*Enable Data Sharpening and Configure Its Defaults*](https://devnet.logianalytics.com/hc/en-us/articles/4405851007127-Enable-Data-Sharpening-and-Configure-Its-Defaults) to learn how to enable Data Sharpening for your connected data sources.

Data Sharpening setup differs slightly depending on the data source. Although a playable time field is required for sharpening to occur, the time field requirement is based on the data source. The table below lists the time field requirements for different data stores supported in Composer.

| Data Store | Time Field Requirement |
| --- | --- |
| Amazon Redshift | Sort Key (only the first sort key is selected) |
| Cloudera Impala, Hive | Partitioned time field (The time field that is partitioned needs to be configured from the "Fields" page. A single partitioned column is needed for Data Sharpening to work in Impala or Hive sources.) |
| Search-based sources  (Cloudera Search, Elasticsearch, Apache Solr) | Indexed time field\*. Composer automatically detects for indices. |
| SQL-based sources  (MySQL, Oracle, PostgreSQL, SQL Server) | Indexed time field\*. Composer automatically detects for indices. |
| \* The indexed time field should already be set in the data source, so no additional configuration is needed in Composer. | |
