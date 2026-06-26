---
title: "Use the Upload API"
id: 4405859140247
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859140247-Use-the-Upload-API
updated_at: 2021-09-21T01:26:44Z
---

# Use the Upload API

# Use the Upload API

You can use the Composer Upload API to dynamically upload and stream your data in real-time. Uploaded data can be in CSV or JSON XML formats. Setting up and configuring an Upload API connector has two parts:

* [*Set Up the Upload API Data Source*](#Setting)
* [*Work with the Upload API*](#Working)

See [*Manage Connectors and Connector Servers*](https://devnet.logianalytics.com/hc/en-us/articles/4405859186199-Manage-Connectors-and-Connector-Servers) for general instructions on enabling the Upload API connector.

After the connector has been set up, you can create data source configurations that specify the necessary connection information and identify the data you want to use. See [*Manage Data Source Configurations*](https://devnet.logianalytics.com/hc/en-us/articles/4405851027479-Manage-Data-Source-Configurations) for more information. After data sources are configured, they can be used to create dashboards and visuals from your data. See [*Create Dashboards*](https://devnet.logianalytics.com/hc/en-us/articles/4405859261207-Create-Dashboards).

## Composer Feature Support

Upload API support for specific [Composer features](https://devnet.logianalytics.com/hc/en-us/articles/4405859170583-Connector-Feature-Support) is shown in the following table.

**Key:** **Y** - Supported; **N** - Not Supported; N/A - not applicable

| Feature | Supported? | |
| --- | --- | --- |
| [Admin-Defined Functions](https://devnet.logianalytics.com/hc/en-us/articles/4405850995991-Admin-Defined-Functions) | **Y** | |
| [Box Plots](https://devnet.logianalytics.com/hc/en-us/articles/4405859517207-Box-Plots) | **Y** | |
| [Custom SQL Queries](https://devnet.logianalytics.com/hc/en-us/articles/4405859171735-Custom-SQL-Queries) | **N** | |
| [Derived Fields (Row-Level Expressions)](https://devnet.logianalytics.com/hc/en-us/articles/4405859299479-Maintain-Derived-Fields) | **Y** | |
| [Distinct Counts](https://devnet.logianalytics.com/hc/en-us/articles/4405859300503-Enable-Distinct-Counts) | **Y** | |
| [Fast Distinct Values](https://devnet.logianalytics.com/hc/en-us/articles/4405850912279-Fast-Distinct-Values) | N/A | |
| [Group By Multiple Fields](https://devnet.logianalytics.com/hc/en-us/articles/4405850913303-Group-By-Multiple-Fields) | **Y** | |
| [Group By Time](https://devnet.logianalytics.com/hc/en-us/articles/4405850914199-Group-By-Time) | **Y** | |
| [Group By UNIX Time](https://devnet.logianalytics.com/hc/en-us/articles/4405850915095-Group-By-UNIX-Time) | **Y** | |
| [Histogram Floating Point Values](https://devnet.logianalytics.com/hc/en-us/articles/4405850915991-Histogram-Floating-Point-Values) | **Y** | |
| [Histograms](https://devnet.logianalytics.com/hc/en-us/articles/4405859514775-Bars-Histograms) | **Y** | |
| [Kerberos Authentication](https://devnet.logianalytics.com/hc/en-us/articles/4405859461271-Configure-Kerberos-Single-Sign-On-SSO-Settings) | **N** | |
| [Last Value](https://devnet.logianalytics.com/hc/en-us/articles/4405859174295-Last-Value) | **Y** | |
| [Live Mode and Playback](https://devnet.logianalytics.com/hc/en-us/articles/4405851191447-Live-Mode-and-Historical-Playback) | **Y** | |
| [Multivalued Fields](https://devnet.logianalytics.com/hc/en-us/articles/4405859175319-Multivalued-Fields) | N/A | |
| [Nested Fields](https://devnet.logianalytics.com/hc/en-us/articles/4405851022871-Support-of-Nested-Data-Structures-in-Composer) | N/A | |
| [Partitions](https://devnet.logianalytics.com/hc/en-us/articles/4405859176343-Partitions) | **N** | |
| [Pushdown Joins for Fusion Data Sources](https://devnet.logianalytics.com/hc/en-us/articles/4405859358487-Optimize-Joins) | **Y** | |
| [Schemas](https://devnet.logianalytics.com/hc/en-us/articles/4405859177367-Schemas) | **Y** | |
| [Text Search](https://devnet.logianalytics.com/hc/en-us/articles/4405859178391-Text-Search) | N/A | |
| [TLS](https://devnet.logianalytics.com/hc/en-us/articles/4405859179671-TLS) | **Y** | |
| [User Delegation](https://devnet.logianalytics.com/hc/en-us/articles/4405859193111-Enable-User-Delegation) | **N** | |
| [Wild Card Filters](https://devnet.logianalytics.com/hc/en-us/articles/4405851071383-Apply-Wild-Card-Filters-to-a-Visual-or-Dashboard) | **Y** | |
| [Wild Card Filters, Case-Insensitive Mode](https://devnet.logianalytics.com/hc/en-us/articles/4405851071383-Apply-Wild-Card-Filters-to-a-Visual-or-Dashboard) | **Y** | |
| [Wild Card Filters, Case-Sensitive Mode](https://devnet.logianalytics.com/hc/en-us/articles/4405851071383-Apply-Wild-Card-Filters-to-a-Visual-or-Dashboard) | **Y** | |

## Set Up the Upload API Data Source

1. Log into Composer as an administrator.
2. Select **Sources**.
3. Select **Upload API**.
4. Specify the name of your source and add a description (if desired).
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743911191/next-btn_40x24.png).
6. On the Sampling page, enter your sample data. The supported formats are CSV or JSON. You can also upload sample data from a file.
7. Select **Preview** to view your data.
8. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743911191/next-btn_40x24.png).
9. On the [*Fields Tab*](https://devnet.logianalytics.com/hc/en-us/articles/4405851026455-Fields-Tab), edit the data shown for the source. For more information and steps, see [*Manage Data Source Configurations*](https://devnet.logianalytics.com/hc/en-us/articles/4405851027479-Manage-Data-Source-Configurations).
10. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743911191/next-btn_40x24.png).
11. On the Refresh page, set the refresh rates or your data. If you want to schedule a refresh of all your data, select **Schedule** and then selecting an option. If you only want certain fields within your data to be refreshed, select Configuration.
12. Use the sample cURL calls to clear previously stored data or add additional data to the source. The example cURL calls can be found on the API Endpoints page.
13. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406747455383/save-next-btn_81x25.png).
14. On the Visuals page, you can:

    * Edit Global Default Settings.
    * Select the **Standard** and, if available, **Custom** visual styles to be used with the data source.
    * Set default parameters (group, sub-group, colors, sorting, and so on) for each visual style.
15. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743931799/finish-btn_46x24.png) to save your changes. After your data connection has been established, it is listed under **My Data Sources**.

## Work with the Upload API

There are two operations that can be performed using the Upload API: appending additional data and clearing previously uploaded data. The data source wizard offers convenient example cURL requests but the APIs can be leveraged from your preferred development platform.

Remember to modify the example cURL requests to include your own Composer credentials, replacing the placeholders for username and password.

```
curl -v --user <username>:<password> <YourServer>
```

### Example: Append Data

In the following example, the Upload API accepts an array of JSON objects. Note that the object field types must match those used to create the Upload API source originally. For example, if the value of the
***price***
field is a number, you can not upload new rows in which the value of the
***price***
field is a string.

```
curl -v --user <username>:<password> 'https://<Your_Composer_Server>/ composer/api/upload/<YourDataSourceId>' -X POST -H "Content-Type: application/vnd.composer.v2+json" -d '[{"price":100.5,"venue_id":"V678","venue_name": "Pizza Barn"}]' --insecure
```

### Example: Clear Previously Uploaded Data

In the example below, the Upload API will clear all previously uploaded data from the data source with the ID of `<YourDataSourceId>`.

```
curl -v --user <username>:<password> 'https://<Your_Composer_Server>/ api/upload/<YourDataSourceId>' -X DELETE --insecure
```
