---
title: "Composer Elasticsearch Connector Feature Support"
id: 43701010430477
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701010430477-Composer-Elasticsearch-Connector-Feature-Support
updated_at: 2026-05-29T14:07:43Z
---

# Composer Elasticsearch Connector Feature Support

# Composer Elasticsearch Connector Feature Support

Connector support for specific  [features](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700992759565-Connector-Feature-Support) is shown in the following table.

**Key:** **Y** - Supported; **N** - Not Supported; N/A - not applicable

| Feature | Supported? | | | Notes |
| --- | --- | --- | --- | --- |
| [Admin-Defined Functions](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701029797901-Admin-Defined-Functions) | **N** | | |  |
| [Box Plots](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701211727885-Box-Plots) | **Y** | | |  |
| [Custom SQL Queries](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701041493645-Custom-SQL-Queries) | **Y** | | | If you need to access a BigQuery partition, explicitly include an alias for the built in partition column in your select clause, such as `select *, _PARTITIONTIME as pt from projectId.datasetId.tableId`. |
| [Derived Fields (Row-Level Expressions)](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701078705933-Maintain-Derived-Fields) | **Y** | | |  |
| [Distinct Counts](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701030916365-Distinct-Counts) | **Y** | | |  |
| [Fast Distinct Values](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701008284941-Fast-Distinct-Values) | **Y** | | |  |
| [Group By Multiple Fields](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701054799373-Group-By-Multiple-Fields) | **Y** | | |  |
| [Group By Time](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701054819213-Group-By-Time) | **Y** | | |  |
| [Group By UNIX Time](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701041642381-Group-By-UNIX-Time) | **N** | | |  |
| [Histogram Floating Point Values](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701041703437-Histogram-Floating-Point-Values) | **Y** | | |  |
| [Histograms](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701211617293-Bars-Histograms) | **Y** | | |  |
| [Kerberos Authentication](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701208766477-Configure-Kerberos-Single-Sign-On-SSO-Settings) | **N** | | |  |
| [Last Value](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701008456845-Last-Value) | **Y** | | |  |
| [Live Mode and Playback](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701210493837-Live-Mode-and-Historical-Playback) | **Y** | | |  |
| [Multivalued Fields](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700993039117-Multivalued-Fields) | **Y** | | |  |
| [Nested Fields](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701068575501-Support-of-Nested-Data-Structures-in-Composer) | **Y** | | |  |
| [Partitions](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701024301709-Partitions) | N/A | | |  |
| [Pushdown Joins for Fusion Data Sources](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701134208269-Optimize-Joins) | **N** | | |  |
| [Schemas](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701038566797-Schemas) | N/A | | |  |
| [Text Search](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701041900045-Text-Search) | **Y** | | | You can sort keyword searches by Best Match and Most Recent (when you select a preferred time field from the source). Filter your search results by selecting fields in the Filter modal. Select **Clear All** to clear filtered search results. |
| [TLS](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700993160717-TLS) | **Y** | | |  |
| [User Delegation](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701039382541-Enable-User-Delegation) | **N** | | |  |
| [Wildcard Filters](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701071787533-Apply-Wildcard-Filters-to-a-Visual-Filter-Snippet-or-Dashboard) | **Y** | | |  |
| [Wildcard Filters, Case-Insensitive Mode](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701038723341-Wildcard-Case-Insensitive-Filters) | **N** | | | Case-sensitivity cannot be enforced. Consequently, neither case-sensitive or case-insensitive wildcard filters are supported. |
| [Wildcard Filters, Case-Sensitive Mode](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700993286669-Wildcard-Case-Sensitive-Filters) | **N** | | | Case-sensitivity cannot be enforced. Consequently, neither case-sensitive or case-insensitive wildcard filters are supported. |
