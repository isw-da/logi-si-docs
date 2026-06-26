---
title: "Elasticsearch Data Source Configuration Notes"
id: 4405850944279
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850944279-Elasticsearch-Data-Source-Configuration-Notes
updated_at: 2021-09-21T01:27:22Z
---

# Elasticsearch Data Source Configuration Notes

# Elasticsearch Data Source Configuration Notes

When setting up an Elasticsearch [data source configuration](https://devnet.logianalytics.com/hc/en-us/articles/4405851027479-Manage-Data-Source-Configurations), consider the following notes for the Indices tab.

You select the indices and types to be queried, and select the fields to be handled. You can do this in three steps:

1. Select indices and aliases to be queried.
2. You can select indices **Manually** or **Automatically**.

   * If you want to get the data only from specific indices, select the **Manually** option and choose the corresponding indices from the list below.
   * The **Automatically** option is more flexible. It lets you set the pattern by which the indices will be selected automatically.

     For this option, you can select one of the pattern types. Note that when no indices match the pattern while querying, your visuals are returned empty.

     + **Native** - specify the pattern for index names. Use an asterisk (\*) to replace one character or a set of characters.

       For example, you want to get all the indices whose name starts with ***log*** and ends with ***16***. In this case, specify the following pattern:

       ```
       log*16
       ```
     + **Time-Based** - set the time pattern to get the matching indices. [Check the supported date and time patterns](https://devnet.logianalytics.com/hc/en-us/articles/4405851010711-Supported-Date-and-Time-Formats).

       For example, the time pattern YYYY-MM will return all the indices, whose name will match the pattern in the following examples. Note that if the Index Name includes text with the time and date pattern, you need to enclose the text portion in brackets [ ]:

       **Examples:**

       | Index Name | Pattern |
       | --- | --- |
       | 2016-01 | YYYY-MM |
       | 2016-3 | YYYY-Q |
       | 10:23:11 | HH:MM:SS |
       | logstash-2016-06-14 | [logstash-]YYYY-MM-DD |

       ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) The fields for indexes will not be refreshed. If new fields are added to your data source, they are added to Composer only after you select the
       **Refresh Fields** button on the **Fields** tab of the [data source configuration](https://devnet.logianalytics.com/hc/en-us/articles/4405851027479-Manage-Data-Source-Configurations). If there are some changes in the existing fields (for example, if a field has been removed) they won't be applied.
3. Optionally, configure filtering by type. If you need to filter by type, select the **Enable Filter By Type** checkbox. The type by which filtering will occur is shown. Select **Edit** to alter the filter by type by selecting one from a list of types available for the selected index

   If the **Enable Filter By Type** checkbox is cleared, all the types that refer to the selected indices are selected.

   If some fields have different data types in types, you are not able to use them for grouping, filters, and so on. However, the option is still available for raw export.

When you connect to your Elasticsearch data source, the additional service field
**\_type** is added.
The
**\_type** field
contains all the selected Elasticsearch types you can visualize as attributes on your visuals.
