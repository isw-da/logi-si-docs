---
title: "Elasticsearch Data Source Configuration Notes"
id: 43700994953869
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700994953869-Elasticsearch-Data-Source-Configuration-Notes
updated_at: 2026-05-29T14:11:28Z
---

# Elasticsearch Data Source Configuration Notes

# Elasticsearch Data Source Configuration Notes

When setting up an Elasticsearch [data source configuration](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701068934669-Manage-Data-Sources), select the indices and aliases to be queried, and select the fields to be handled. You can do this in three steps:

1. Select indices and aliases to be queried on the Source Creation tab.
2. Select indices **Manually** or **Automatically**.

   * If you want to get the data only from specific indices, select the **Manually** option and choose the corresponding indices from the list **Select Indices**.
   * The **Automatically** option is more flexible. It lets you set the pattern by which the indices will be selected automatically.

     For this option, you can select one of the pattern types. Note that when no indices match the pattern while querying, your visuals are returned empty.

     + **Native** - specify the pattern for index names. Use an asterisk (\*) to replace one character or a set of characters.

       For example, you want to get all the indices whose name starts with ***log*** and ends with ***16***. In this case, specify the following pattern:

       log\*16
     + **Time Based** - set the time pattern to get the matching indices. [Check the supported date and time patterns](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701078376461-Convert-Attributes-to-Time-Fields-in-Data-Source-Field-Specifications).

       For example, the time pattern YYYY-MM will return all the indices, whose name will match the pattern in the following examples. Note that if the Index Name includes text with the time and date pattern, you need to enclose the text portion in brackets [ ]:

       **Examples:**

       | Index Name | Pattern |
       | --- | --- |
       | 2022-01 | YYYY-MM |
       | 2022-3 | YYYY-Q |
       | 10:23:11 | HH:MM:SS |
       | logstash-2022-06-14 | [logstash-]YYYY-MM-DD |

       **Note:** 
       The fields for indexes are not refreshed. If new fields are added to your data source, they are added to Composer only after you select the
       **Manual Refresh** (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243329907597)) button on the **Cache** tab of the [data source](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701068934669-Manage-Data-Sources). If there are some changes in the existing fields (for example, if a field has been removed) they won't be applied.

   **Note:** 
   Filtering by type is not supported.

When you connect to your Elasticsearch data source, the additional service field
**type** is added.
The
**type** field
contains all the selected Elasticsearch types you can visualize as attributes on your visuals.
