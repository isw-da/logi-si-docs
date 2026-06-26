---
title: "Filtering Dashboard Data"
id: 4406817243543
section: "Use Dashboards & Visuals - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817243543-Filtering-Dashboard-Data
updated_at: 2022-04-06T06:04:54Z
---

# Filtering Dashboard Data

# Filtering Dashboard Data

Dashboards can be configured with special features that allow you to *filter* the data used in dashboard panels, individually and globally.

## Filtering Individual Panels

If filtering has been enabled, clicking the panel's "gear" icon will display a pop-up menu that has a *Filter* option.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563417623/usingdash_12.png)

This option will open the **Panel Filter** panel, as shown above. The controls displayed in it will depend on the view mode, *Simple* or *Design*, configured by your application developer.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575796503/usingdash_13.png)

In Design view, you can define and combine filters, using the controls shown above. Adding, changing, or removing filters will immediately filter the data in the dashboard panel accordingly.

## Adding a Global Filter

You can also add a "global" filter, one that affects the data used in *multiple* dashboard panels at once. This type of filter functionality is automatically available when multiple dashboard panels have been configured for filtering.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563418007/usingdash_14.png)

The example dashboard shown above has two panels, each of which has been configured for filtering and whose visualizations use data from the ShipCountry column.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575797399/usingdash_15.png)

You can create a global filter by clicking the gear icon for the dashboard tab, as shown above, and selecting the *Add Global Filters* pop-up menu option.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584056983/usingdash_16.png)

The **Global Filter** panel will be displayed, as shown above. The controls displayed in it will depend on the configured view mode and have been explainedearlier. Once a filter has been created, dashboard panels with visualizations whose data includes the filter'sdata columns will be filtered; those that do not include the filter'scolumns will not be filtered.

Filter descriptions, circled above, will be added to each filtered panel and can be clicked to re-open the Global Filter panel.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584057111/usingdash_17.png)

A global filter description will also appear at the top of the tab and can be used as a link to re-open the Global Filter panel. In addition, when you hover your mouse cursor over this description, the panels affected by the filter will be highlighted, as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575799191/usingdash_16a.png)

When the Simple view mode is used, filters can be disabled by unchecking their check box. This causes the global filter description to be removed, but a filter icon, circled above, remains as an indicator that a global filter is defined and available for use. Clicking the icon will re-open the Global Filter panel.

## Global Filtering using Chart Data Points

If your application has been configured to allow it, you can also create a global filter in a dashboard by selecting data points in a chart:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575799319/usingdash_18.png)

Once again, we have an example with two dashboard panels, one with a chart and one with a table, shown above. When you click a bar in the chart, a global filter is created automatically and three other things happen:

1. A Filter Description appears at the top of the dashboard tab. This can be clicked to edit the global filter.
2. The color of the selected chart bar changes to indicate it's included in a filter.
3. The data for the table in the second panel is filtered.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) This is different from the previous global filtering example because the chart that was clicked is *not* filtered.

Clicking the same chart bar a second time will cancel the filter related to that data. Clicking another bar will add additional criteria to the global filter.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584057239/usingdash_19.png)

Clicking the Filter Description at the top of the dashboard tab will cause the automatically-generated Global Filter panel to be displayed. As before, the controls displayed in it will depend on the view mode, Simple or Design, configured by your application developer (only Simple mode is shown above).

![](https://devnet.logianalytics.com/hc/article_attachments/4417563419031/usingdash_20.png)

For chart types that support it, you can also create a global filter by dragging the cursor to select a range of values, as shown in the Line chart above. This will create a global filter that includes the selected range of values.
