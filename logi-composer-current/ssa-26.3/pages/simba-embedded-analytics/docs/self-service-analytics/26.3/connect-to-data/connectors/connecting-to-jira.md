> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage the Jira Connector

The Self-Service Analytics Jira connector lets you access the data available in Jira. Obtain the connector server following this process: [Obtain Additional Connector Servers](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connectors-ov#obtain-additional-connector-servers).

After setting up the connector, create data sources that specify the necessary connection information and identify the data you want to use. See [Create and Manage Data Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview) for more information. After you set up your data sources, create [dashboards](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-manage#create-dashboards), [self service reports](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/ssr-manage), and [visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-add-dash#create-and-add-visuals-to-the-visual-gallery) from the data in these data sources.

* [Feature Support](#feature-support)
* [Connect to Jira](#connect-to-jira)
* [Optimize Performance](#optimize-performance)
* [Custom SQL Optimization](#custom-sql-optimization)
* [Custom Fields](#custom-fields)
* [Retrieving and Calculating Story Points](#retrieving-and-calculating-story-points)

<h3 id="feature-support">
  Feature Support
</h3>

Connector support for specific [features](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support) is shown in the following table.

**Key:** **Y** - Supported; **N** - Not Supported; N/A - not applicable

| Feature | Supported? |
| - | - |
| [Admin-Defined Functions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/admin-fx-ov) | **N** |
| [Box Plots](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/scatter-plot#box-plots) | **Y** |
| [Custom SQL Queries](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#custom-sql-queries-2) | **Y** |
| [Derived Fields (Row-Level Expressions)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/derived-fields) | **Y** |
| [Distinct Counts](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#distinct-counts) | **Y** |
| [Fast Distinct Values](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#fast-distinct-values) | **N** |
| [Group By Multiple Fields](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#group-by-multiple-fields) | **Y** |
| [Group By Time](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#group-by-time) | **Y** |
| [Group By UNIX Time](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#group-by-unix-time) | **Y** |
| [Histogram Floating Point Values](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#histogram-floating-point-values) | **Y** |
| [Histograms](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/bar-standard#bars-histograms) | **Y** |
| [Kerberos Authentication](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/kerberos-sso) | **N** |
| [Last Value](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#last-value) | **N** |
| [Live Mode and Playback](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/time-bar#live-mode-and-historical-playback) | **Y** |
| [Multivalued Fields](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#multivalued-fields-2) | **N** |
| [Nested Fields](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/nested-data-structures) | **N** |
| [Partitions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#partitions) | **N** |
| [Pushdown Joins for Fusion Data Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-fusion-overview#optimize-joins) | **N** |
| [Schemas](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#schemas-2) | **Y** |
| [Text Search](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#text-search) | **N** |
| [TLS](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#tls) | **N** |
| [User Delegation](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connectors-ov#enable-user-delegation) | **N** |
| [Wildcard Filters](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters-attr#apply-wildcard-filters-to-a-visual-filter-snippet-or-dashboard) | **Y** |
| [Wildcard Filters, Case-Insensitive Mode](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#wildcard-case-insensitive-filters) | **Y** |
| [Wildcard Filters, Case-Sensitive Mode](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#wildcard-case-sensitive-filters) | **Y** |

<h3 id="connect-to-jira">
  Connect to Jira
</h3>

To connect Self-Service Analytics to your Jira instance, provided the JDBC url, a Jira user name, and password or API token.

| Input Field | Description |
| - | - |
| JDBC Url | jdbc:jira://;Host=*host\_name\_or\_your\_server*;Auth\_Type=Basic Authentication |
| User Name | Jira user name |
| Password | Jira user password or API token generated for the Atlassian account. |

Configure your Jira rate limit using Atlassian's guidelines to minimize rate limit errors and prevent performance issues. Rate limit are configured per user, per project; add a test user account with no rate limit to test your projects. See [https://developer.atlassian.com/cloud/jira/platform/rate-limiting/](https://developer.atlassian.com/cloud/jira/platform/rate-limiting/).

<h3 id="optimize-performance">
  Optimize Performance
</h3>

The Jira connector and Simba JDBC driver use schema tables to map your data to a compatible JDBC format you can use when creating your sources. Learn more here: [Schema Tables](https://documentation.insightsoftware.com/simba-jira-jdbc-reference-guide/content/reference/schema-intro-jdbc.htm).

<h4 id="custom-sql-optimization">
  Custom SQL Optimization
</h4>

Large Jira boards and projects can affect the connector's performance. To minimize this impact, you can create your data source using a [custom SQL query](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-source-creation-tab) and pushdown filters. To optimize the query, you can:

* Include pushdown filters
* Design queries to filter on columns for which folding is supported
* Limit your query using a `WHERE` clause and `TOP` for columns that do not support pushdown filters
* Narrow your data retrieval by filtering your data by epic, project, issue creation date, or completion date
* Speed your initial load time by defining a small time range on the [Global Settings tab](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-global-settings-tab#time-bar-settings)

Example:

```
SELECT S.Sprint_name, S.Sprint_startDate, S.Sprint_endDate, S.Sprint_state, I.Issues_fields_project_name, I.Issues_fields_project_key, I.Issues_fields_status_name, I.Issues_key
FROM Agile_Board_Sprint S
JOIN Extra.Agile_Board_Issue I ON S.Sprint_id = I.Issues_fields_sprint_id
WHERE S.Sprint_startDate > 'YYY-MM-DD' AND I.Issues_fields_project_key = 'MY_PROJECT_KEY'
```

#### Raw Data Cache

You can reduce the number of queries Self-Service Analytics makes to the source and speed up data query execution by enabling raw data caching. When enabled, an **Entity Data Cache** toggle is added to the Source Creation work area. Enable and define a caching schedule. Contact [Technical Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support) for assistance enabling this feature.

<h4 id="custom-fields">
  Custom Fields
</h4>

See [Api\_Field](https://documentation.insightsoftware.com/simba-jira-jdbc-reference-guide/content/reference/jir/schema-jdbc/platform_api_field.htm) for custom fields mappings. The field `custom_name` is type `SQL_VARCHAR(1024)` and is often represented in JSON format. Use the `SUBSTRING()` function to extract fields from the JSON.

Example:

```
SELECT Fields_Issue_Type_Name, SUBSTRING(customfield_13218, 89, 5) AS Team, SUBSTRING(customfield_11200, 105, 1) AS Severity, Fields_Status_Name AS Status, SUBSTRING(customfield_12618, 105, 8) AS Defect_Origin, Fields_Created, customfield_10100 AS Story_points
FROM Extra.Api_Issue E
WHERE Fields_Project_Key = 'MY_PROJECT_KEY' AND Fields_Issue_Type_Name = 'Story'
```

<h4 id="retrieving-and-calculating-story-points">
  Retrieving and Calculating Story Points
</h4>

Jira stores time estimation and story points. The story points are a custom field mapping, see [Api\_Field](https://documentation.insightsoftware.com/simba-jira-jdbc-reference-guide/content/reference/jir/schema-jdbc/platform_api_field.htm). Use this information to build custom metrics and return commonly used calculations.

* Committed story points: `SUM(story_points)`
* Completed story points: `SUM(story_points) WHERE fields_status_name = 'Done'`
* Percent completed: `(SUM(story_points) WHERE fields_status_name = 'Done') / (SUM(story_points))`

Example:

```
SELECT Issues_fields_project_name, Issues_fields_sprint_name, Issues_fields_sprint_startDate, Issues_fields_sprint_endDate, Issues_fields_sprint_self, Issues_fields_sprint_state, Issues_key, Issues_fields_status_name, customfield_10100 AS story_points
FROM Extra.Agile_Board_Issue
WHERE Issues_fields_project_key = 'MY_PROJECT_KEY' AND Issues_fields_sprint_name !=NULL
```
