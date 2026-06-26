---
title: "Data Sharpening Prerequisites"
id: 43701095182477
section: "Manipulate Data In The Composer 26 Data Store"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701095182477-Data-Sharpening-Prerequisites
updated_at: 2026-05-29T14:08:13Z
---

# Data Sharpening Prerequisites

# Data Sharpening Prerequisites

Before you use Data Sharpening, verify that your data source configuration has enabled it. See [Enable Data Sharpening and Configure Its Defaults](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701078143885-Enable-Data-Sharpening-and-Configure-Its-Defaults).

Before Composer can perform Data Sharpening with a data source, a "playable" time field is required. Composer attempts to automatically detect this playable field from your data source when it is defined. To determine what makes a time attribute "playable," refer to the table below. In addition, an appropriate time attribute must be specified in your data source's global default settings on the Visuals page of the data source configuration. The granularity of this time field is referred to as the *driving time field granularity* (DTFG) and plays an important role in determining whether and how Data Sharpening is executed (see [When Data Sharpening Occurs](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701048625037-When-Data-Sharpening-Occurs)). See [Enable Data Sharpening and Configure Its Defaults](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701078143885-Enable-Data-Sharpening-and-Configure-Its-Defaults) to learn how to enable Data Sharpening for your connected data sources.

Data Sharpening setup differs slightly depending on the data source. Although a playable time field is required for sharpening to occur, the time field requirement is based on the data source. The table below lists the time field requirements for different data stores supported in Composer.

| Data Store | Time Field Requirement |
| --- | --- |
| Amazon Redshift | Sort Key (only the first sort key is selected) |
| Cloudera Impala, Hive | Partitioned time field (The time field that is partitioned needs to be configured from the "Fields" page. A single partitioned column is needed for Data Sharpening to work in Impala or Hive sources.) |
| Search-based sources  (Cloudera Search, Elasticsearch, Apache Solr) | Indexed time field\*. Composer automatically detects for indices. |
| SQL-based sources  (MySQL, Oracle, PostgreSQL, SQL Server) | Indexed time field\*. Composer automatically detects for indices. |
| **Note:**  The indexed time field should already be set in the data source, so no additional configuration is needed in Composer. | |
