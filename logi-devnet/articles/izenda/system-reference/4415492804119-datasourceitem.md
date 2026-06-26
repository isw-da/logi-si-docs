---
title: "DataSourceItem"
id: 4415492804119
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415492804119-DataSourceItem
updated_at: 2021-12-10T03:08:40Z
---

# DataSourceItem

# DataSourceItem

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **id**  string (GUID) |  | The id of item |  |
| **name**  string |  | The name of the item |  |
| **childNodes**  array of objects |  | An array of [DataSourceItem](#) objects |  |
| **parentId**  string (GUID) |  | The id of the parent item |  |
| **checked**  boolean |  | Wether this item is checked or not |  |
| **isLeafItem**  boolean |  | Whether this item is leaf item or not |  |
| **expand**  boolean |  | Whether this item is expanded or not |  |
| **interacted**  boolean |  | Whether this item is interacted by user or not |  |

Inherited fields:

# HierarchyItem

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **fullPath**  string |  | The full path |  |
| **isChecked**  boolean |  | Whether this instance is checked or not |  |
| **isLastPage**  boolean |  | Whether children in this node contain last element or not |  |
| **numOfChilds**  integer |  | Total child nodes |  |
| **numOfCheckedChilds**  integer |  | Total slected child nodes |  |
| **indeterminate**  boolean |  | Whether this node is inderterminate or not |  |
