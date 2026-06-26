---
title: "Set a Numeric Field Filter"
id: 43701133427085
section: "Use Dashboards and Visuals in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701133427085-Set-a-Numeric-Field-Filter
updated_at: 2026-05-29T14:10:51Z
---

# Set a Numeric Field Filter

# Set a Numeric Field Filter

You can filter visual data by the values in a numeric field.

## Set a Filter in a Visual or Dashboard

1. Select the filter icon on the [visual](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701118671885-Apply-a-Row-Level-Filter-to-a-Visual-or-Filter-Snippet) or [dashboard](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701108132365-Apply-a-Row-Level-Filter-to-a-Dashboard) to access the appropriate filter sidebar.

   * To access the filter sidebar, select its filter icon ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243233974669) or select **Settings** from the Show More [menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701184743565-Use-the-Visual-Menu) (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243250290189)) and then select the filter ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243250290829) on the [sidebar menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701215106445-Use-the-Visual-Sidebar-Menu).
   * To access the dashboard filter sidebar, select its filter icon ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243250291725). The dashboard-level filter icon is available only when all the visuals are from the same data source.

   The Filters sidebar opens, showing currently applied filters, if any.
2. Select **Add Filter**. An Add Filter work area opens to the Row tab, and includes Group and Saved tabs.
3. Select the Row tab. If the style of your visual is an arc gauge, KPI chart, table (raw data), histogram, or map markers chart, the Group tab is available, but you cannot create a group filter because all filters for these visual styles are row-level filters. If you are using the dashboard filters sidebar, the Group tab is not available.

   The Saved tab shows saved filters that you can apply to a dashboard, visual, or filter snippet. See [Maintain Saved Filters](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701104098061-Maintain-Saved-Filters).
4. On the Row tab, select the numeric field you want to use from the list of available number fields. A Select Values work area opens that you can use to select values and define this filter's specifics. See the table below for available options.

   | Tab | Description |
   | --- | --- |
   | Range | Select a relational comparison operator in the **Operator** selection box. Data is included in the visual when the data in the filter field meets the condition set by the relational operator and the numeric values you specify. Valid numeric operators are described in [Operators](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701114195085-Operators).  The Range tab initially shows the full range of values available. It provides an **Operator** selection box and **From** and **To** boxes for you to use to select the range of values. Use the arrows in the **From** and **To** boxes to increase and decrease the maximum and minimum values. |
   | Keyset | The Keyset tab allows you to select a keyset to apply as the filter (see [Use Keysets](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701105959565-Use-Keysets)). |

   **Note:** You can also select the add icon ![add icon](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243250292237 "add icon") to access the [Derived Field Editor](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701095677581-Derived-Field-Editor) or the [Custom Metrics Editor](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701082580237-Custom-Metrics-Editor) to create or modify derived fields and custom metrics to be used as filters. See [Access the Derived Field Editor from the Filters Sidebar](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701066934285-Access-the-Derived-Field-Editor-from-the-Filters-Sidebar) and [Access the Custom Metrics Editor from the Filters Sidebar](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701015326349-Access-the-Custom-Metrics-Editor-from-the-Filters-Sidebar).
5. After you have defined the filter specifics, select **Continue**. After confirming your changes, select **Apply**.

   * Filters you create at the dashboard level are applied to all the visuals in the dashboard that use that source.
   * Filters you create at the visual level apply only to the selected (active) visual.

**Note:** Optionally, nest multiple filters for more targeted filtering results. Select **Nest Filters**, then link multiple filters using `AND` and `OR` filtering.

## Additional Numeric Field Filters in a Filter Snippet

When you create a [new filter snippet](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701071841933-Add-Filter-Snippets-to-a-Dashboard), you define the initial data type, operator, data source, and value column to use in [Data Settings](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701104142221-Use-The-Filter-Snippet-Sidebar-Menu#Data "Data settings"). You can add additional filters, including nested filters, as needed.

1. Open your existing filter snippet.
2. Select the Filters option from the [Filter Snippet sidebar](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701104142221-Use-The-Filter-Snippet-Sidebar-Menu#Filters "Filter Snippet sidebar").
3. Select **Add Filter**. An Add Filter work area opens to the Row tab, and includes Group and Saved tabs.
4. Select or create a field to filter from available options on the Row or Group tab.

   * Select an existing available field from [Attribute](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701133345293-Set-an-Attribute-Filter), [Number](#), [Time](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701087681293-Set-a-Time-Field-Filter), or [Hierarchy](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701118747917-Filter-by-Hierarchy-Field) and define appropriate options to use.
   * Alternatively, elect the add icon to add a [derived field](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701095677581-Derived-Field-Editor) or [custom metric](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701082580237-Custom-Metrics-Editor), and define appropriate options to use.
5. After you have defined the filter specifics, select **Continue**. After confirming your changes, select **Apply**.

**Note:** Optionally, nest multiple filters for more targeted filtering results. Select Nest Filters, then link multiple filters using `AND` and `OR` filtering.
