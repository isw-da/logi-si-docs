---
title: "Use the Context Menu"
id: 34933236349453
section: "Use Dashboards and Visuals in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933236349453-Use-the-Context-Menu
updated_at: 2026-05-26T22:09:06Z
---

# Use the Context Menu

# Use the Context Menu

Users can use the context menu on all visuals to view more information about specific data points in visuals. This menu provides streamlined options for working with data.

To access the context menu, select any data point in the visual, grouped or ungrouped, to explore or drill down into that data element.

![use the context menu to drill deeper into text for any available data element](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46166986370317 "Context Menu in a bar chart")

Define how to embed the context menu in your Composer instance by specifying default options for right and left mouse selection. If needed, you can also add custom controls to the context menu for embedded visuals. See [Control How Users Interact With a Visual](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933282294029-Control-How-Users-Interact-With-a-Visual).

The following options are available in the context menu:

* [Details](#Details)
* [Create Alert](#Alert)
* [Filter](#Filter)
* [Keyset](#Keyset)
* [Trend](#Trend)
* [Zoom](#Zoom)
* [Link](#Link)
* [Actions](#Actions)
* [Remove](#Remove)
* [Settings](#Settings)

## Details

To display additional information about specific data elements, select **Details**. The details for the element are displayed in a table.

![view the details that make up this element](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167014784781 "Data Details work area")

The table header contains the following:

1. Attribute whose details you have selected to view
2. Metric
3. Volume metric
4. Time attribute and the selected time interval on the time bar
5. Data source

Select **Export Raw Data** to export your data set to a CSV file. If the **Table** visual style is enabled for your data source, you can select
**Open in Table** to view your information.

You can also view the information in a pop-out window over your visual. Select the collapse icon to minimize the window.

## Create Alert

Use **Create Alert** to create an alert for this visual and data element. See [Create an Alert Definition](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932664892685-Create-an-Alert-Definition) .

## Filter

Use **Filter** to filter other visuals in the dashboard that are subscribed to same-source or cross-source links by the data point you have selected. For more information, see [Apply a Filter to Dashboard Visuals Using the Context Menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932953236237-Apply-a-Filter-to-Dashboard-Visuals-Using-the-Context-Menu).

The context menu can be used to apply cross-visual filters to all visuals in a dashboard. If a visual subscribes to a link field, a context menu filter for the field from a different visual in the same dashboard will also be applied to the first visual. For example, if Visuals A and B are both subscribed to a link for field Z, and you use the context menu to apply a filter for field Z on Visual B, the filter will also be applied to Visual A. For information about controlling the publish and subscribe link settings for a visual, see [Control How Cross-Visual Filters Interact in a Dashboard](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933107422477-Control-How-Cross-Visual-Filters-Interact-in-a-Dashboard).

**Note:** 
Unlike row-level filters, cross-visual filters are not saved with the visual.

In addition, **Filter** is only available in the context menu when the visual publishes a link for the field it is also using for its visual grouping. It is *not* available if the published cross-visual links for the visual are muted. See [Mute a Published Link](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933081445773-Mute-a-Published-Link).

## Keyset

Use **Keyset** to create a keyset from the selected data point. See [Create a Keyset](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933047131789-Create-a-Keyset).

## Trend

Use **Trend** to view trends for a selected data point. **Trend** is not available for: Line and Bars Trend, Line Trend: Attribute Values, and Line Trend: Multiple Metrics.

## Zoom

Use **Zoom** to zoom into the selected data point and filter the data for that data point by another filter attribute in the data source. When you select **Zoom**, a menu appears from which you select the second filter attribute.

For example, if you wanted to see the real time sales for every city in Florida, select Florida in the bar chart to bring up the context menu, select **Zoom**, and then select the City attribute from the resulting menu. The result set in the bar chart might look like this:

![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167010581133 "Zoomed in data element")

## Link

Use **Link** to quickly access a dashboard that has been linked to this visual. **Link** is only available if a dashboard link has been defined for a visual. See [Link a Dashboard](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932833747469-Link-a-Dashboard).

## Actions

Use **Actions** to invoke an action. If this menu option does not appear on the context menu, an action template is either not defined or is not enabled for the data source used by the visual.

The invoked action:

* Creates a query definition based on the filters applied to the visual and on the data and limit specifications in the associated action template.
* Sends the query definition to your application. Your application can use the Composer API to run the query and display or use the data that it collects.

**Note:** 
You must be logged in as an administrator or as a user with the **Invoke Actions** [privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference).

To invoke an action, see [Invoke an Action](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932653492621-Invoke-an-Action).

## Remove

Select **Remove** to exclude the selected data element from your visual.

## Settings

Select **Settings** to open the [visual sidebar menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933295031181-Use-the-Visual-Sidebar-Menu).
