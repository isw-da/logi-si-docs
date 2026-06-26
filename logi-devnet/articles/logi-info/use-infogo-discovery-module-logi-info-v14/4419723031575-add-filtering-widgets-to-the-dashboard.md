---
title: "Add Filtering Widgets to the Dashboard"
id: 4419723031575
section: "Use InfoGo/Discovery Module - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723031575-Add-Filtering-Widgets-to-the-Dashboard
updated_at: 2022-07-17T01:43:48Z
---

# Add Filtering Widgets to the Dashboard

# Add Filtering Widgets to the Dashboard

The Dashboard editing tool includes several built-in filtering widgets and they can be added to a Dashboard and configured to filter one or more visualization widgets. To add filtering widgets to a Dashboard, open the built-in widgets panel and find one of widgets you want to use.

![](https://devnet.logianalytics.com/hc/article_attachments/5163525179159/introsuperwidgets_20.png)

In the example shown above, the **List Filter Widget** is being dragged onto a drop zone in the Dashboard.

![](https://devnet.logianalytics.com/hc/article_attachments/5163472646679/introsuperwidgets_21_530x224.png)

The widget will expand in place and can be moved, resized, and deleted just like other widgets. Click its gear icon to open its settings panel:

![](https://devnet.logianalytics.com/hc/article_attachments/5163525186199/introsuperwidgets_22_309x355.png)

Configuration options will vary by filter widget type, but the example above is typical. The options above include:

1. **Caption** - Specifies the caption that will appear for this widget.
2. **Selection Type** - Specifies whether the filtering values will be appear in a simple list, filling the panel, or a drop-down list.
3. **Selection Mode** - Specifies whether multiple filtering values can be selected, and whether a search feature is available.
4. **Select Data** - Specifies the Dataview whose data will be filtered.
5. **Display Column** - Specifies the data column that will supply text shown in the selection list.
6. **Value Column** - Specifies the data column that will be targeted by the filtering.
7. **Include "No Selection"** - Specifies if the list will include a "blank" entry and, if so, what its text will be.

Click **Apply** to save the filter configuration.
Once the filter has been configured, a new icon for connecting the filter to visualization widgets will appear at the top:

![](https://devnet.logianalytics.com/hc/article_attachments/5163472661655/introsuperwidgets_23_452x343.png)

Click the Link icon, circled above, to open the **Filter Parameter Settings** panel, which is where you select the visualization widgets that will be filtered. Use the ![](https://devnet.logianalytics.com/hc/article_attachments/5163525212951/plusminusarizona.png) icons to add and remove target widgets. The list of target widgets only includes those that have been created using the same Dataview as the one specified for this filter. Click **Done** when ready.

![](https://devnet.logianalytics.com/hc/article_attachments/5163472663447/introsuperwidgets_23a_490x206.png)

A faster way to select target widgets is to use the Blue Dot Connecter, as shown above, to make the connections. The visualization widgets available for filtering (those using the same Dataview) will temporarily turn pink as you start to drag the Blue Dot. Once connections have been made, the Link icon will turn red.

![](https://devnet.logianalytics.com/hc/article_attachments/5163512284055/introsuperwidgets_24_486x347.png)

As you select Category filter values, they're applied to *all* of the visualization widgets linked to the filter, as shown above.
