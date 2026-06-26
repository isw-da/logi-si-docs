---
title: "Working with the Tabs Element"
id: 4419723270295
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723270295-Working-with-the-Tabs-Element
updated_at: 2022-07-17T02:22:59Z
---

# Working with the Tabs Element

# Working with the Tabs Element

The **Tabs** element is the parent element for one of more Tab Panels elements. The attributes of the Tabs element are:

| Attribute | Description |
| --- | --- |
| ID | (Required) Specifies a unique element identifier. |
| Active Tab Background Color | Specifies the background color for the active tab panel. Enter a color by name, decimal RGB value, or hex RGB value. Prefix hex values with the pound sign, such as #112233. |
| Border Color | Specifies the color of the border lines for all tab panels. If border lines are not desired, you may select "Transparent". Enter a color by name, decimal RGB value, or hex RGB value. Prefix hex values with the pound sign, such as #112233. |
| Default Tab | Specifies the ID of the Tab Panel that will be initially selected when the report is displayed. *See the paragraph below concerning how to maintain the tab selection between page refreshes.* |
| Height Height Scale | Specifies a fixed height for the tab panels. Leaving this value blank will cause the panels to dynamically resize themselves based on their content. The adjacent **Height Scale** attribute specifies whether this value is in to be applied in pixels or as a percentage. |
| Inactive Tab Background Color | Specifies the background color for inactive tab panels. Enter a color by name, decimal RGB value, or hex RGB value. Prefix hex values with the pound sign, such as #112233. |
| Security Right ID | Controls access to this element using Logi Security. Provide the ID of a Right defined in the application's \_settings definition and only users that have a Role referenced in the Right will be able to see the element. Multiple Right IDs, separated by commas, may be entered. |
| Tab Location | Specifies location of the tabs that the user clicks to switch between tab panels. Options include: *Top*, *Bottom*, *Left*, and *Right*. The default value is: *Top*. |
| Tabbing Style | Specifies when tab panel *content* will be refreshed and rendered. Possible values are: *Static* - (default value) The content of all tabs is retrieved and rendered when Tabs element is displayed. When the user selects a hidden tab, the tab panel's content is already at the browser and the selected tab and content are displayed immediately *Ajax* - The contents of tabs other than the default tab are *not* retrieved and rendered until each tab is selected. When the user selects a tab, an AJAX request is sent to the server to get its panel's contents. This can help reduce rendering time when there are many tabs, especially if those panels contain datalayers. If a tab is re-selected after other tabs have been selected, the panel is simply redisplayed without going back again to the server for content. *RefreshPage* - Unselected tab panel contents are not processed by the server until the user selects their tab. When selected, the panel page is always re-submitted and therefore displayed with refreshed content. As with the previous mode, this can help reduce rendering time when there are many tabs, especially if their panels contain datalayers. |
| Width Width Scale | Specifies the fixed width of the tab panels. Leaving this value blank will cause the panels to dynamically resize themselves based on their content. The adjacent **Width Scale** attribute specifies whether this value is in to be applied in pixels or as a percentage. |

## Maintaining the Tab Selection Between Page Refreshes

It may be desirable to maintain the current tab selection when the page is refreshed. For example, if a Data Table is displayed in a tab panel and its records can be sorted by clicking column headers, the current tab should remain selected after a column header is clicked, the table is resorted, and the page is refreshed.

When a page with tabs is submitted using Action elements, the ID of the currently selected Tab Panel is automatically sent out as the value of a **request variable**. The request variable name is set to the ID of the Tabs element. Referring to the example definition shown earlier in this topic and assuming that the Sales tab was selected, this request variable would be sent when the page is submitted: tabsReports = pnlSales.

![](https://devnet.logianalytics.com/hc/article_attachments/7522761580439/tabpanels_05.png)

So, by setting the **Default Tab** attribute of the Tabs element to the request variable token, as shown above, the current tab will be maintained when the page is refreshed.

## Refreshing or Navigating to a Specific Tab

If you'd like to refresh your page, or navigate to it from another page, and ensure that a specific tab will be selected after it loads, it's easy to do.

First, set the Tabs element's **Default Tab** attribute to a Request token. In the previous example, this value was set to @Request.tabsReports~.

Then, in the URL used to call the report, include this query string parameter: &*<Tabs Element ID>* = *<Tab Panel Element ID>*

To do this when refreshing your report page or navigating to it from another Logi definition using Action.Report, assuming the element IDs from the previous example, use a **Link Parameters** element to add a request parameter with the name *tabsReports* and a value of *pnlOrders* to select the Orders tab.

To do this when navigating from an non-Logi HTML page or using Action.Link, the URL would be something like:

http://myLogiApp/rdPage.aspx?rdReport=ReportWithTabs&tabsReports=pnlOrders
