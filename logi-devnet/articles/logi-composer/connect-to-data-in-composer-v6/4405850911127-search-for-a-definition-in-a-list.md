---
title: "Search for a Definition in a List"
id: 4405850911127
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850911127-Search-for-a-Definition-in-a-List
updated_at: 2021-09-21T01:27:04Z
---

# Search for a Definition in a List

# Search for a Definition in a List

If there are many definitions listed on the page, you may need to search for the definition you need. Use the search bar to perform the search.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747452055/connection-search-bar_576x29.png)

To search for a definition:

Select the column for the search. You can search the page for data in specific columns. For example, you can search for a specific definition author. To select a column type, select the arrows in the **All** box on the left side of the search box and select one from the drop-down menu. Select **All** to search in all columns.

On the right side of the search box, enter the characters for which you wish to search. The search returns definitions in the list that include the requested characters.

You can use complex searches. Searches are performed from left to right, with no logical preference or grouping. The following special characters are allowed in complex searches:

| Character | Use to ... |
| --- | --- |
| **&** or **;** | Conditionally AND items in the search string. |
| **|** | Conditionally OR items in the search string. |

The following keywords can also be used in complex searches and map to columns in the list. So, some keywords don't work on some lists because the column is not available for that list.

| Keyword | Use to identify a search for ... |
| --- | --- |
| author | The name of an author in the Author column. |
| connection | The name of a connection definition in the Connection column. |
| name | The name of the definition in the Name column. |
| type | The type of the definition in the Type column. |

For example, on the Connections page, the following search string would search for connection definitions with names that include the characters `impala` and that were created by user `sarah`:

```
name:impala & author:sarah
```

If a connection definition in the list does not meet both of these criteria, it is not returned by the search.
