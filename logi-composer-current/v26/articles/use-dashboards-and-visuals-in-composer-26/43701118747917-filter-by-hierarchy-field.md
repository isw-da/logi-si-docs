---
title: "Filter by Hierarchy Field"
id: 43701118747917
section: "Use Dashboards and Visuals in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701118747917-Filter-by-Hierarchy-Field
updated_at: 2026-05-29T14:10:52Z
---

# Filter by Hierarchy Field

# Filter by Hierarchy Field

You can filter your data by the values in a hierarchy field. The source used by the visual, visuals, dashboard (when only one source is in use) or associated filter snippet must be set up to include a hierarchy field. See [Hierarchical Fields and Structures](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701084425613-Hierarchical-Fields-and-Structures).

## Filter in a Visual or Dashboard

1. Select the filter icon on the [visual](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701118671885-Apply-a-Row-Level-Filter-to-a-Visual-or-Filter-Snippet) or [dashboard](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701108132365-Apply-a-Row-Level-Filter-to-a-Dashboard) to access the appropriate filter sidebar.

   * To access the filter sidebar, select its filter icon ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243250328461) or select **Settings** from the Show More [menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701184743565-Use-the-Visual-Menu)![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243234011917) and then select the filter icon ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243234012685) on the [sidebar menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701215106445-Use-the-Visual-Sidebar-Menu).
   * To access the dashboard filter sidebar, select its filter icon ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243250328461). The dashboard-level filter icon is available only when all the visuals are from the same data source.

   The Filters sidebar opens, showing currently applied filters, if any.
2. Select **Add Filter**. An Add Filter work area opens to the Row tab, and includes Group and Saved tabs.
3. On the Row tab, select an available hierarchy field to use to filter your data. A Select Values work area opens.
4. Select a filter **Operator** for your data.

   1. When you select **Include**, you can individually select hierarchical values in the filter to be included. This allows exclusion of specific descendent data from a parent as needed.
   2. When you select **Equals or Descendents of**, you can select groups of data quickly and easily; select a top level node and all of its descendents are included by default.
5. Select one or more nodes to filter your data. At least one filter value is required.

   * Use the **Search** box to find specific nodes.
   * Select the node indicators to expand and collapse nodes, or select and deselect **Expand All** to expand and collapse all nodes.
6. After you've defined your filter specifics, select **Continue**.

   * If you create the filter at the dashboard level, it is applied to all the visuals and filter snippets in the dashboard.
   * Otherwise, it is applied only to the selected (active) visual or filter snippet. After confirming your changes, select **Apply.**

## Create a Filter Snippet - Hierarchy Data Type

1. Create a [new filter snippet](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701071841933-Add-Filter-Snippets-to-a-Dashboard).
2. Define the **Data Settings** to use a Data Type of **Hierarchy**.
3. Select an **Operator** for your data.

   1. When you select **Include**, you and your users can individually select hierarchical values in the filter to be included. This allows exclusion of specific descendent data from a parent as needed.
   2. When you select **Equals or Descendents of**, you and your users can select groups of data quickly and easily; select a top level node and all of its descendents are included by default.
4. Select an available **Source**. Any visuals in this dashboard that use this source can be affected by this filter snippet.
5. Select an available **Value Column**, then select **Apply**.
6. Your filter snippet updates, allowing users to filter data for widgets you connect to this filter snippet.

After you've connected the filter snippet to widgets, users can filter data in the filter snippet. They can:

* Use the **Search** box to find specific nodes.
* Select and deselect **Expand All** to expand and collapse all nodes.
* Select the node indicators to expand and collapse individual nodes and their descendents.

## Additional Hierarchy Filters in a Filter Snippet

When you create a [new filter snippet](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701071841933-Add-Filter-Snippets-to-a-Dashboard), you define the initial data type, operator, data source, and value column to use in [Data Settings](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701104142221-Use-The-Filter-Snippet-Sidebar-Menu#Data "Data settings"). You can add additional filters, including nested filters, as needed.

1. Open your existing filter snippet.
2. Select the Filters option from the [Filter Snippet sidebar](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701104142221-Use-The-Filter-Snippet-Sidebar-Menu#Filters "Filter Snippet sidebar").
3. Select **Add Filter**. An Add Filter work area opens to the Row tab, and includes Group and Saved tabs.
4. Select or create a field to filter from available options on the Row or Group tab.

   * Select an existing available field from [Attribute](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701133345293-Set-an-Attribute-Filter), [Number](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701133427085-Set-a-Numeric-Field-Filter), [Time](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701087681293-Set-a-Time-Field-Filter), or [Hierarchy](#) and define appropriate options to use.
   * Alternatively, elect the add icon to add a [derived field](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701095677581-Derived-Field-Editor) or [custom metric](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701082580237-Custom-Metrics-Editor), and define appropriate options to use.
5. After you have defined the filter specifics, select **Continue**. After confirming your changes, select **Apply**.

**Note:** Optionally, nest multiple filters for more targeted filtering results. Select Nest Filters, then link multiple filters using `AND` and `OR` filtering.
