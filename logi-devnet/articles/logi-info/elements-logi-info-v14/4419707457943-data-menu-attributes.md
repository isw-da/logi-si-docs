---
title: "Data Menu Attributes"
id: 4419707457943
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707457943-Data-Menu-Attributes
updated_at: 2022-07-17T01:54:50Z
---

# Data Menu Attributes

# Data Menu Attributes

The Data Menu element has the following unique attributes:

| Attribute | Description |
| --- | --- |
| Caption Column | (Required) The name of the column in the datalayer whose values will be displayed as the menu items. |
| Action ID Column | The name of the column in the datalayer whose values are the ID of a child Action element that will be executed when the menu item is tapped. This is used for menu items that call another report definition, a URL, etc., not for navigating to sub-menus. |
| Image Column | The name of the column in the datalayer whose values are the names of image files. These images are displayed to the left of the menu item. If the image file is stored in the \_SupportFiles folder, no file path is required. Relative file paths may be used. Example: *abcnews.png* |
| Sub Menu ID Column | The name of the column in the datalayer whose values are the names of the sub-menus, if any, that each menu item *resides in*. Used in data rows for sub-menus only. |
| Target Sub Menu ID Column | The name of the column in the datalayer whose values are the names of the sub-menus to *navigate to* when each menu item is tapped. Used only when sub-menus exist. |

When working a hierarchy of sub-menus with **DataLayer.Static**, it is possible to construct and use **Static Data Rows** that do not necessarily all have the same number of columns. Different data rows contain data for different purposes and the Logi Server Engine won't object if columns exist in one row but don't exist in another row where they serve no purpose.

Obviously, if you use a database to provide your menu data, then all rows returned by a query will have the same number of columns. In that case, you'll need to ensure that the query returns *all* of the columns needed for *all* purposes.
