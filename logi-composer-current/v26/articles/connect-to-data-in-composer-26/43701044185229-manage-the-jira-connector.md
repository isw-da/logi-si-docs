---
title: "Manage the Jira Connector"
id: 43701044185229
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701044185229-Manage-the-Jira-Connector
updated_at: 2026-05-29T14:07:47Z
---

# Manage the Jira Connector

# Manage the Jira Connector

The Composer Jira connector lets you access the data available in Jira. Obtain the connector server following this process: [Obtain Additional Connector Servers](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701024898061-Obtain-Additional-Connector-Servers)

After setting up the connector, create data sources that specify the necessary connection information and identify the data you want to use. See [Manage Data Sources](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701068934669-Manage-Data-Sources) for more information. After you set up your data sources, create [dashboards](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701076467981-Create-Dashboards) and [visuals](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701179894541-Create-and-Add-Visuals-to-the-Visual-Gallery) from from the data in these data sources. See [Create Dashboards](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701076467981-Create-Dashboards).

* [Feature Support](#feature)
* [Connect to Jira](#Connect)
* [Optimize Performance](#Optimize)
* [Custom SQL Optimization](#Custom)
* [Custom Fields](#Custom2)
* [Retrieving and Calculating Story Points](#Retrievi)

## Feature Support

Connector support for specific  [features](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700992759565-Connector-Feature-Support) is shown in the following table.

**Key:** **Y** - Supported; **N** - Not Supported; N/A - not applicable

| Feature | Supported? |
| --- | --- |
| [Admin-Defined Functions](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701029797901-Admin-Defined-Functions) | **N** |
| [Box Plots](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701211727885-Box-Plots) | **Y** |
| [Custom SQL Queries](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701041493645-Custom-SQL-Queries) | **Y** |
| [Derived Fields (Row-Level Expressions)](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701078705933-Maintain-Derived-Fields) | **Y** |
| [Distinct Counts](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701030916365-Distinct-Counts) | **Y** |
| [Fast Distinct Values](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701008284941-Fast-Distinct-Values) | **N** |
| [Group By Multiple Fields](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701054799373-Group-By-Multiple-Fields) | **Y** |
| [Group By Time](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701054819213-Group-By-Time) | **Y** |
| [Group By UNIX Time](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701041642381-Group-By-UNIX-Time) | **Y** |
| [Histogram Floating Point Values](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701041703437-Histogram-Floating-Point-Values) | **Y** |
| [Histograms](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701211617293-Bars-Histograms) | **Y** |
| [Kerberos Authentication](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701208766477-Configure-Kerberos-Single-Sign-On-SSO-Settings) | **N** |
| [Last Value](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701008456845-Last-Value) | **N** |
| [Live Mode and Playback](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701210493837-Live-Mode-and-Historical-Playback) | **Y** |
| [Multivalued Fields](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700993039117-Multivalued-Fields) | **N** |
| [Nested Fields](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701068575501-Support-of-Nested-Data-Structures-in-Composer) | **N** |
| [Partitions](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701024301709-Partitions) | **N** |
| [Pushdown Joins for Fusion Data Sources](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701134208269-Optimize-Joins) | **N** |
| [Schemas](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701038566797-Schemas) | **Y** |
| [Text Search](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701041900045-Text-Search) | **N** |
| [TLS](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700993160717-TLS) | **N** |
| [User Delegation](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701039382541-Enable-User-Delegation) | **N** |
| [Wildcard Filters](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701071787533-Apply-Wildcard-Filters-to-a-Visual-Filter-Snippet-or-Dashboard) | **Y** |
| [Wildcard Filters, Case-Insensitive Mode](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701038723341-Wildcard-Case-Insensitive-Filters) | **Y** |
| [Wildcard Filters, Case-Sensitive Mode](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700993286669-Wildcard-Case-Sensitive-Filters) | **Y** |

## Connect to Jira

To connect Composer to your Jira instance, provided the JDBC url, a Jira user name, and password or API token.

| Input Field | Description |
| --- | --- |
| JDBC Url | jdbc:jira://;Host=*host\_name\_or\_your\_server*;Auth\_Type=Basic Authentication |
| User Name | Jira user name |
| Password | Jira user password or API token generated for the Atlassian account. |

Configure your Jira rate limit using Atlassian's guidelines to minimize rate limit errors and prevent performance issues. Rate limit are configured per user, per project; add a test user account with no rate limit to test your projects. See <https://developer.atlassian.com/cloud/jira/platform/rate-limiting/>.

## Optimize Performance

The Jira connector and Simba JDBC driver use schema tables to map your data to a compatible JDBC format you can use when creating your sources. Learn more here: [Schema Tables](https://documentation.insightsoftware.com/simba-jira-jdbc-reference-guide/content/reference/schema-intro-jdbc.htm).

### Custom SQL Optimization

Large Jira boards and projects can affect the connector's performance. To minimize this impact, you can create your data source using a [custom SQL query](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701080568205-Source-Creation-Tab) and pushdown filters. To optimize the query, you can:

* Include pushdown filters
* Design queries to filter on columns for which folding is supported
* Limit your query using a `WHERE` clause and `TOP` for columns that don't support pushdown filters
* Narrow your data retrieval by filtering your data by epic, project, issue creation date, or completion date
* Speed your initial load time by defining a small time range on the [Global Settings tab](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701085233549-Global-Settings-Tab#Time)

Example:

SELECT S.Sprint\_name, S.Sprint\_startDate, S.Sprint\_endDate, S.Sprint\_state, I.Issues\_fields\_project\_name, I.Issues\_fields\_project\_key, I.Issues\_fields\_status\_name, I.Issues\_key
FROM Agile\_Board\_Sprint S
JOIN Extra.Agile\_Board\_Issue I ON S.Sprint\_id = I.Issues\_fields\_sprint\_id
WHERE S.Sprint\_startDate > 'YYY-MM-DD' AND I.Issues\_fields\_project\_key = 'MY\_PROJECT\_KEY'

### Raw Data Cache

You can reduce the number of queries Composer makes to the source and speed up data query execution by enabling raw data caching. When enabled, an **Entity Data Cache** toggle is added to the Source Creation work area. Enable and define a caching schedule. Contact [Technical Support](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072313613-Contact-Technical-Support) for assistance enabling this feature.

### Custom Fields

See [Api\_Field](https://documentation.insightsoftware.com/simba-jira-jdbc-reference-guide/content/reference/jir/schema-jdbc/platform_api_field.htm) for custom fields mappings. The field `custom_name` is type `SQL_VARCHAR(1024)` and is often represented in JSON format. Use the `SUBSTRING()` function to extract fields from the JSON.

Example:

SELECT Fields\_Issue\_Type\_Name, SUBSTRING(customfield\_13218, 89, 5) AS Team, SUBSTRING(customfield\_11200, 105, 1) AS Severity, Fields\_Status\_Name AS Status, SUBSTRING(customfield\_12618, 105, 8) AS Defect\_Origin, Fields\_Created, customfield\_10100 AS Story\_points
FROM Extra.Api\_Issue E
WHERE Fields\_Project\_Key = 'MY\_PROJECT\_KEY' AND Fields\_Issue\_Type\_Name = 'Story'

### Retrieving and Calculating Story Points

Jira stores time estimation and story points. The story points are a custom field mapping, see [Api\_Field](https://documentation.insightsoftware.com/simba-jira-jdbc-reference-guide/content/reference/jir/schema-jdbc/platform_api_field.htm). Use this information to build custom metrics and return commonly used calculations.

* Committed story points: `SUM(story_points)`
* Completed story points: `SUM(story_points) WHERE fields_status_name = 'Done'`
* Percent completed: `(SUM(story_points) WHERE fields_status_name = 'Done') / (SUM(story_points))`

Example:

SELECT Issues\_fields\_project\_name, Issues\_fields\_sprint\_name, Issues\_fields\_sprint\_startDate, Issues\_fields\_sprint\_endDate, Issues\_fields\_sprint\_self, Issues\_fields\_sprint\_state, Issues\_key, Issues\_fields\_status\_name, customfield\_10100 AS story\_points
FROM Extra.Agile\_Board\_Issue
WHERE Issues\_fields\_project\_key = 'MY\_PROJECT\_KEY' AND Issues\_fields\_sprint\_name !=NULL
