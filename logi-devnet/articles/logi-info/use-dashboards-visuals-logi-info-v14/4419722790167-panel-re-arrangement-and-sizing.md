---
title: "Panel Re-Arrangement and Sizing"
id: 4419722790167
section: "Use Dashboards & Visuals - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722790167-Panel-Re-Arrangement-and-Sizing
updated_at: 2022-07-17T02:24:43Z
---

# Panel Re-Arrangement and Sizing

# Panel Re-Arrangement and Sizing

A Dashboard or tab's layout usually consists of one or more *columns* and, if the Dashboard is configured to be adjustable, you can drag-and-drop the panels into the columns and the arrangement of your choice.

![](https://devnet.logianalytics.com/hc/article_attachments/7522830458519/usingdash_09a.png)

If the Dashboard is adjustable, then by using the Dashboard or tab's gear icon and Settings menu, you can change the number of columns in a tab or Dashboard, as shown above.

Adjustable layouts let you use the "splitter bar", described below, to adjust column widths. In this case, when the layout dialog box shown above appears, you're only asked to specify the *number of panel columns* you want.

![](https://devnet.logianalytics.com/hc/article_attachments/7522826802327/usingdash_09.png)

You can drag a panel to a new location by clicking on its caption bar, as shown above (note the cursor change). As the panel is dragged into a different column or position, a yellow "drop zone" indicator appears to help snap the panel into its new location.

In a columnar layout, panels will automatically resize based on the width of the column they're dropped into, and the column's width is determined by the *widest panel* it contains. If the contents of a panel are widened, then the panel and its column will widen, too.

*This is a change from panel behavior in previous versions!* In a columnar layout, panels will automatically resize based on the width of the column they're dropped into. Column width is a *fixed width*, determined by the layout chosen and screen width. Panel content will be automatically scaled up to the maximum width that fits in the panel. In support of this change, charts in panels
in columnar layouts no longer have horizontal resizing handles.

## Using the Splitter Bar

You can change the widths of layout columns (and therefore panels) in Dashboards that are configured to be adjustable by using the "splitter" bar:

![](https://devnet.logianalytics.com/hc/article_attachments/7522843421847/usingdash_09b.png)

Hover your mouse cursor over the vertical space between two Dashboard panels, as shown above, and a gray splitter bar will appear and the cursor will change, as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/7522846099607/usingdash_09c.png)

Drag the bar right or left to the adjust panel widths, then drop the bar at the desired location. Visualization widths will automatically adjust to match the change in panel widths.

## Using Free-form Layout

Depending on your application's configuration, a "Free-form Layout" option may also available. If it's enabled, you can resize and rearrange Dashboard panels without regard to any predetermined columns:

![](https://devnet.logianalytics.com/hc/article_attachments/7522826821143/usingdash_10.png)

In Free-form layout, shown above, any widths and placements can be achieved. When the mouse cursor hovers over a panel, "resizing handles" appear at its sides and bottom and these can be dragged to resize the panel. Internal panel scroll bars will automatically appear if the panel is made too small for its contents.

Panel side resizing handles no longer appear; use the splitter bar, described earlier, to change panel width instead.

Given that you may be able to customize a Dashboard, it's
useful to be able to save those customizations and re-use them in a future session. Your developer may have enabled an automatic "bookmark" mechanism for this, or there may be a link you have to click to save your settings.

## Bookmark Undo and Redo

![](https://devnet.logianalytics.com/hc/article_attachments/7522826824983/usingdash_11.png)

If the automatic bookmark mechanism is in use, **Undo** and **Redo** icons will appear beside the Dashboard tabs, as shown above. You can click these to undo and redo actions you've taken.
