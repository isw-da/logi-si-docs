---
title: "Search and Filter Lists"
id: 34932690388621
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932690388621-Search-and-Filter-Lists
updated_at: 2026-05-26T22:10:19Z
---

# Search and Filter Lists

# Search and Filter Lists

If there are many items included in your work area, you may need to search and filter for what you need.

You can use the search bar to perform a search, and a filter to filter all items or your search results, using built in filters or content tags.

## Use The Search Field

You can search many of the columns in your list to find what you need. Select **All** to search all searchable columns, or select an option available from the drop-down menu, such as **Author**, **Name**, or **Type**. Some work areas also allow you to search the text of a **Description** associated with an item.

**Note:** 
The columns you can search vary by work area.

Enter some characters into the search field. Logi Composer hides items that don't match your partial search criteria. Narrow the results further by entering a complete search term or character string, or by performing a more complex search.

To perform a complex search, you can include the following special characters in the Search field:

**Note:** 
Searches are performed from left to right, with no logical preference or grouping.

| Character | Use to ... |
| --- | --- |
| **&** or **:** | Conditionally AND items in the search string. |
| **|** | Conditionally OR items in the search string. |

Optionally, use these column keywords in complex searches and map to columns in the list.

**Note:** 
A column keyword is not searchable in a list that does not contain that column. For example, dashboards do not include a **Type** column.

| Keyword | Use to identify a search for ... |
| --- | --- |
| author | The name of an author in the Author column. |
| connection | The name of a connection in the Connection column (outside of the Connections work area). |
| name | The name of an item in the Name column. |
| type | The type of an item in the Type column. |
| description | Items with specific words in the Description. |

For example, in the Connections work area, the following search string would search for connections with names that include the characters `impala` and that were created by user `linda`:

name:impala & author:linda

If no connections in the list meet both of these criteria, a message is returned indicating that no items match the current search.

## Filter Lists or Results

You can search for specific items using the search field, and narrow your returned results by selecting a content filter at the top of your work area. These filters are available in the Sources work area, the Visual Gallery, and the Library.

| Filter | Description |
| --- | --- |
| **All** | Removes any filters for the list and displays all items of this type you can access within your Composer environment. |
|  | Displays only items that you have marked as favorites. |
|  | Displays only items that you created and saved. Visuals created and saved by other users are hidden. |
|  | Displays only items that other users shared with you. See [Grant Permissions for a Visual](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933273320845-Grant-Permissions-for-a-Visual). |

## Filter Lists and Search Results Using Tags

After you've added tags to one or more sources, visuals, or dashboards , you can filter your view of these items by selecting one or more tags (or select items that do not have a tag, specifically).

**Filter your items using tags**

1. Navigate to the work area you want to filter or search and filter (Sources, Visual Gallery, Library ).
2. Optionally, enter a search term in the **Search** field to find items in your list that match that search query.
3. Select the filter icon for the **Tags** column header to open a drop-down selection list.
4. Select one or more tags in the list by selecting (checking) the checkbox. The list changes to reflect items that included your selected tags criteria.
5. Select any portion of the work area to hide the drop-down selection list and view your results.
6. Clear the **Search** field and the filtered tags to return your entire list of items to the work area, or simply refresh the page.

### Tags Drop-Down Selection List Options

The tags shown in your list are determined by the available tags in your environment. Tags are shared among sources, Visual Gallery visuals, and dashboards . For example, if the sources in your instance only have two associated tags, while visuals and dashboards have a broader range of associated tags, you'll see all available tags in the drop-down selection list.

Two options you can use to filter are not tags. They are listed at the top of the drop-down selection list: **Select All (*n*)** and **[NONE]**.

* **Select All (*n*)**: Use Select All to quickly select or deselect all tags in the list by filling or clearing the checkbox.
* **[NONE]**: Use NONE to return all items in the list that do not have associated tags.

  + If you select NONE while any or all tags are selected, those selections are cleared, and only items with no tags are shown.
  + If you select any other tag while NONE is selected, the NONE checkbox is cleared, and only items with selected tags are shown.
