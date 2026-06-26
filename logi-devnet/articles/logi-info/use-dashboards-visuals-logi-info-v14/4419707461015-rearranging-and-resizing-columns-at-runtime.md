---
title: "Rearranging and Resizing Columns at Runtime"
id: 4419707461015
section: "Use Dashboards & Visuals - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707461015-Rearranging-and-Resizing-Columns-at-Runtime
updated_at: 2023-02-01T03:08:02Z
---

# Rearranging and Resizing Columns at Runtime

# Rearranging and Resizing Columns at Runtime

If a Data Table element's **Draggable****Columns** attribute is set to *True*, users can rearrange its columns at runtime:

![](https://devnet.logianalytics.com/hc/article_attachments/7522801645079/dtcols_07_602x193.png)

When this feature is enabled, as shown above, users can click on the left side of the column header and drag the column right or left to a new position. If columns can be dragged they'll display a special icon in their headers, as shown above, which isn't visible until the cursor is hovered over it. The new column arrangement can now be stored in bookmarks and "remembered".

![](https://devnet.logianalytics.com/hc/article_attachments/7522843313303/dtcols_08.png)

The Data Table element's **Resizable Columns** attribute allows users to drag an icon in the column header, shown above, at runtime to increase or decrease the column width.

The default value for both of these attributes is *False*.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) Column dragging and resizing functions can't be used when the Data Table includes optional special rows, such as Header rows or Summary rows, that include columns that span multiple Data Table columns.
