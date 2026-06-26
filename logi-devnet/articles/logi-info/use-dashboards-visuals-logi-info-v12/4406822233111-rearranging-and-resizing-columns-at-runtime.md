---
title: "Rearranging and Resizing Columns at Runtime"
id: 4406822233111
section: "Use Dashboards & Visuals - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822233111-Rearranging-and-Resizing-Columns-at-Runtime
updated_at: 2022-04-06T06:05:01Z
---

# Rearranging and Resizing Columns at Runtime

# Rearranging and Resizing Columns at Runtime

If a Data Table element's **Draggable****Columns** attribute is set to *True*, users can rearrange its columns at runtime:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563403927/dtcols_07_602x193.png)

When this feature is enabled, as shown above, users can click on the left side of the column header and drag the column right or left to a new position. If columns can be dragged they'll display a special icon in their headers, as shown above, which isn't visible until the cursor is hovered over it.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575786007/dtcols_08.png)

The Data Table element's **Resizable Columns** attribute allows users to drag an icon in the column header, shown above, at runtime to increase or decrease the column width.

The new column arrangement or width is "remembered" for the duration of the current session. The default value for both of these attributes is *False*.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png)Column dragging and resizing functions can't be used when the data table includes optional special rows, such as Header rows or Summary rows, that include columns that span multiple data table columns.
