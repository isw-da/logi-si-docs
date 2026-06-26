---
title: "Manage the Jira Connector"
id: 34932766172941
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932766172941-Manage-the-Jira-Connector
updated_at: 2026-05-26T22:06:41Z
---

# Manage the Jira Connector

# Manage the Jira Connector

The Composer Jira connector lets you access the data available in Jira. Obtain the connector server following this process: [Obtain Additional Connector Servers](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932693640717-Obtain-Additional-Connector-Servers)

After setting up the connector, create data sources that specify the necessary connection information and identify the data you want to use. See [Manage Data Sources](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932941009037-Manage-Data-Sources) for more information. After you set up your data sources, create [dashboards](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932763355021-Create-Dashboards) and [visuals](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933273224589-Create-and-Add-Visuals-to-the-Visual-Gallery) from from the data in these data sources. See [Create Dashboards](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932763355021-Create-Dashboards).

* [Composer Feature Support](#feature)
* [Connect to Jira](#Connect)
* [Optimize Performance](#Optimize)
* [Custom SQL Optimization](#Custom)
* [Custom Fields](#Custom2)
* [Retrieving and Calculating Story Points](#Retrievi)

## Composer Feature Support

Connector support for specific  [features](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932704861453-Connector-Feature-Support) is shown in the following table.

**Key:** **Y** - Supported; **N** - Not Supported; N/A - not applicable

| Feature | Supported? |
| --- | --- |
| [Admin-Defined Functions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932796673933-Admin-Defined-Functions) | **N** |
| [Box Plots](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933208692493-Box-Plots) | **Y** |
| [Custom SQL Queries](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932704947213-Custom-SQL-Queries) | **Y** |
| [Derived Fields (Row-Level Expressions)](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932839148813-Maintain-Derived-Fields) | **Y** |
| [Distinct Counts](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932867905037-Distinct-Counts) | **Y** |
| [Fast Distinct Values](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932715069197-Fast-Distinct-Values) | **N** |
| [Group By Multiple Fields](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932715164173-Group-By-Multiple-Fields) | **Y** |
| [Group By Time](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932690999309-Group-By-Time) | **Y** |
| [Group By UNIX Time](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932730700429-Group-By-UNIX-Time) | **Y** |
| [Histogram Floating Point Values](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932708132109-Histogram-Floating-Point-Values) | **Y** |
| [Histograms](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933212496141-Bars-Histograms) | **Y** |
| [Kerberos Authentication](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933139627149-Configure-Kerberos-Single-Sign-On-SSO-Settings) | **N** |
| [Last Value](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932730888205-Last-Value) | **N** |
| [Live Mode and Playback](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933163012621-Live-Mode-and-Historical-Playback) | **Y** |
| [Multivalued Fields](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932715662093-Multivalued-Fields) | **N** |
| [Nested Fields](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932861225357-Support-of-Nested-Data-Structures-in-Composer) | **N** |
| [Partitions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932715778445-Partitions) | **N** |
| [Pushdown Joins for Fusion Data Sources](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932963077133-Optimize-Joins) | **N** |
| [Schemas](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932691729805-Schemas) | **Y** |
| [Text Search](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932739827853-Text-Search) | **N** |
| [TLS](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932692004749-TLS) | **N** |
| [User Delegation](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932742695053-Enable-User-Delegation) | **N** |
| [Wildcard Filters](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932977272717-Apply-Wildcard-Filters-to-a-Visual-Filter-Snippet-or-Dashboard) | **Y** |
| [Wildcard Filters, Case-Insensitive Mode](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932723779981-Wildcard-Case-Insensitive-Filters) | **Y** |
| [Wildcard Filters, Case-Sensitive Mode](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932692417677-Wildcard-Case-Sensitive-Filters) | **Y** |

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

Large Jira boards and projects can affect the connector's performance. To minimize this impact, you can create your data source using a [custom SQL query](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932891763981-Source-Creation-Tab) and pushdown filters. To optimize the query, you can:

* Include pushdown filters
* Design queries to filter on columns for which folding is supported
* Limit your query using a `WHERE` clause and `TOP` for columns that don't support pushdown filters
* Narrow your data retrieval by filtering your data by epic, project, issue creation date, or completion date
* Speed your initial load time by defining a small time range on the [Global Settings tab](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932890843277-Global-Settings-Tab#Time)

Example:

SELECT S.Sprint\_name, S.Sprint\_startDate, S.Sprint\_endDate, S.Sprint\_state, I.Issues\_fields\_project\_name, I.Issues\_fields\_project\_key, I.Issues\_fields\_status\_name, I.Issues\_key
FROM Agile\_Board\_Sprint S
JOIN Extra.Agile\_Board\_Issue I ON S.Sprint\_id = I.Issues\_fields\_sprint\_id
WHERE S.Sprint\_startDate > 'YYY-MM-DD' AND I.Issues\_fields\_project\_key = 'MY\_PROJECT\_KEY'

### Raw Data Cache

You can reduce the number of queries Composer makes to the source and speed up data query execution by enabling raw data caching. When enabled, an **Entity Data Cache** toggle is added to the Source Creation work area. Enable and define a caching schedule. Contact [Technical Support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932980712461-Contact-Technical-Support) for assistance enabling this feature.

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
