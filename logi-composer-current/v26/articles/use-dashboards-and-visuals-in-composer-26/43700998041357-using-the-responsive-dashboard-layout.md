---
title: "Using the Responsive Dashboard Layout"
id: 43700998041357
section: "Use Dashboards and Visuals in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700998041357-Using-the-Responsive-Dashboard-Layout
updated_at: 2026-05-29T14:11:17Z
---

# Using the Responsive Dashboard Layout

# Using the Responsive Dashboard Layout

Composer's dashboard layout is responsive, building on a grid format that presents your dashboards to Users with Viewer access a flexible, mobile-friendly layout on a variety of screen sizes. Composer rebuilds the dashboard layout on smaller screen sizes for any widget wider than 250 pixels. Preview the dashboard in [View mode](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701014828173-Use-Dashboard-View-Mode).

**Edit mode:**

![make changes to your dashboard in edit mode](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242665410701 "Dashboard in Edit Mode")

**View mode:**

![view your responsive dashboard layout](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242692861069 "Dashboard in View Mode")

When you add widgets in [Edit mode](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701014828173-Use-Dashboard-View-Mode), Composer groups the widgets in rows and columns. These rows include up to four widgets side by side in a single row. When you add a fifth widget to a dashboard that includes four widgets in a row, Composer starts a new row with the new widget.

If you move, resize, or reposition widgets, then add a new one, Composer will add any new widgets to the first row that contains fewer than three widgets.

## Manage Your Dashboard Layout

Select the Dashboard Layout icon (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242697068301)) to open the Dashboard Layout work area. Here you can enable and disable locking mode, the responsive layout, and manage the minimum widget widths and heights.

| Dashboard Layout Option | Description / Actions |
| --- | --- |
| Locking Mode | Enable and disable the toggle to control widget locking in this dashboard. See [Lock and Unlock Widget Positions](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701029061261-Lock-and-Unlock-Widget-Positions). |
| Responsive Layout | Enable and disable the toggle to control responsive layout for this dashboard. |
| Min widget width | By default, the width is 250 pixels. Set from 1 to 250 pixels. When the dashboard is in View mode, widgets are resized to no smaller than the defined size, based on browser window size. |
| Min widget height | By default, the height is 50 pixels. Set from 1 to 250 pixels. When the dashboard is in View mode, widgets are resized to no smaller than the defined size, based on browser window size. |

**Note:** 
Use the property `supressResponsiveLayout` to control if the responsive layout is enabled or disabled. By default, this is set to `false`, enabling responsive layout. In embedded environments, set to `true` to suppress responsive layout.
