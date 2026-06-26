---
title: "Set an Attribute Filter"
id: 34932939064717
section: "Use Dashboards and Visuals in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932939064717-Set-an-Attribute-Filter
updated_at: 2026-05-26T22:09:32Z
---

# Set an Attribute Filter

# Set an Attribute Filter

You can filter data by the values in an attribute field.

## Set a Filter in a Visual or Dashboard

1. Select the filter icon on the [visual](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932931145741-Apply-a-Row-Level-Filter-to-a-Visual-or-Filter-Snippet) or [dashboard](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932922987533-Apply-a-Row-Level-Filter-to-a-Dashboard) to access the appropriate filter sidebar.

   * To access the filter sidebar, select its filter icon ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167886334221) or select **Settings** from the Show More [menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933290868621-Use-the-Visual-Menu) (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167886335117)) and then select the filter ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167886337549) on the [sidebar menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933295031181-Use-the-Visual-Sidebar-Menu).
   * To access the dashboard filter sidebar, select its filter icon ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167886334221). The dashboard-level filter icon is available only when all the visuals are from the same data source.

   The Filters sidebar opens, showing currently applied filters, if any.
2. Select **Add Filter**. An Add Filter work area opens to the Row tab, and includes Group and Saved tabs.
3. Select the Row tab. If the style of your visual is an arc gauge, KPI chart, table (raw data), histogram, or map markers chart, the Group tab is available, but you cannot create a group filter because all filters for these visual styles are row-level filters. If you are using the dashboard filters sidebar, the Group tab is not available.

   The Saved tab shows saved filters that you can apply to a dashboard or visual. See [Maintain Saved Filters](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932976956941-Maintain-Saved-Filters).
4. On the Row tab, select the filter attribute you want to use from the list of available attributes. A Select Values work area opens that you can use to select values and define this filter's specifics. See the table below for available options.

   | Tab | Description |
   | --- | --- |
   | Value | The Value tab allows you to select:  * A filter operator (**Include** or **Exclude**, depending on whether you want to include or exclude the value from the data). * An optional custom value. To create and select a custom value, enter the value in the **Customize** field and select **Add**. Your custom field is added and selected in the list of possible values. To remove the custom value, uncheck it in the list of possible values. It is removed from the filter and from the list of possible values for the filter. * One or more values from the list of available values for the attribute you selected. To select all values, select **Select All**. Use the search bar to quickly find a value. You can type the name of the value in the Search bar (or characters in the value name) to limit the list of values. A maximum of 1000 values are listed. If no values are listed or if you cannot find your value, type the exact name of the value (as stored in your data) into the Search bar and select the add icon add icon to select it. This will force your instance to use this value when sending the query to the data store.  See [Apply Row-Level Filters](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932930630157-Apply-Row-Level-Filters). |
   | Wildcard | The Wildcard tab allows you to specify a wildcard filter for the attribute. See [Apply Wildcard Filters to a Visual, Filter Snippet, or Dashboard](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932977272717-Apply-Wildcard-Filters-to-a-Visual-Filter-Snippet-or-Dashboard). |
   | Keyset | The Keyset tab allows you to select a keyset filter for the attribute. See [Use Keysets](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933047406605-Use-Keysets) for instructions on using keysets in a filter. |

   **Note:** You can also select the add icon ![add icon](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167876107533 "add icon") to access the [Derived Field Editor](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932882620813-Derived-Field-Editor) or the [Custom Metrics Editor](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932820475405-Custom-Metrics-Editor) to create or modify derived fields and custom metrics to be used as filters. See [Access the Derived Field Editor from the Filters Sidebar](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932881853581-Access-the-Derived-Field-Editor-from-the-Filters-Sidebar) and [Access the Custom Metrics Editor from the Filters Sidebar](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932813600525-Access-the-Custom-Metrics-Editor-from-the-Filters-Sidebar).
5. After you have defined the filter specifics, select **Continue**. After confirming your changes, select **Apply**.

   * Filters you create at the dashboard level are applied to all the visuals in the dashboard that use that source.
   * Filters you create at the visual level apply only to the selected (active) visual.

**Note:** Optionally, nest multiple filters for more targeted filtering results. Select **Nest Filters**, then link multiple filters using `AND` and `OR` filtering.

## Additional Attribute Filters in a Filter Snippet

When you create a [new filter snippet](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933003207309-Add-Filter-Snippets-to-a-Dashboard), you define the initial data type, operator, data source, and value column to use in [Data Settings](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932987838349-Use-The-Filter-Snippet-Sidebar-Menu#Data "Data settings"). You can add additional filters, including nested filters, as needed.

1. Open your existing filter snippet.
2. Select the Filters option from the [Filter Snippet sidebar](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932987838349-Use-The-Filter-Snippet-Sidebar-Menu#Filters "Filter Snippet sidebar").
3. Select **Add Filter**. An Add Filter work area opens to the Row tab, and includes Group and Saved tabs.
4. Select or create a field to filter from available options on the Row or Group tab.

   * Select an existing available field from [Attribute](#), [Number](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932957895565-Set-a-Numeric-Field-Filter), [Time](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932958685197-Set-a-Time-Field-Filter), or [Hierarchy](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932931841549-Filter-by-Hierarchy-Field) and define appropriate options to use.
   * Alternatively, elect the add icon to add a [derived field](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932882620813-Derived-Field-Editor) or [custom metric](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932820475405-Custom-Metrics-Editor), and define appropriate options to use.
5. After you have defined the filter specifics, select **Continue**. After confirming your changes, select **Apply**.

**Note:** Optionally, nest multiple filters for more targeted filtering results. Select Nest Filters, then link multiple filters using `AND` and `OR` filtering.
