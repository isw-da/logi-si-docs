---
title: "Analysis Grid - Creating Custom Aggregations"
id: 4419715062807
section: "Use Dashboards & Visuals - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715062807-Analysis-Grid-Creating-Custom-Aggregations
updated_at: 2022-07-17T02:25:21Z
---

# Analysis Grid - Creating Custom Aggregations

# Analysis Grid - Creating Custom Aggregations

In addition to the standard aggregations, you can create custom aggregations and save them to use again in the future. There are two different types of custom aggregates you can create in the Analysis Grid: column-specific and data type-specific.

## Column-Specific Custom Aggregations

For this example, we want to determine the *Average Item Cost*. Using the data provided in the table below, you'll notice we need to incorporate a Tax Rate. This additional data component indicates that we cannot find the average by simply using a standard Sum or Average aggregation. Instead, we're going to create a Custom Aggregation to calculate the Average Item Cost.

![](https://devnet.logianalytics.com/hc/article_attachments/7522856155927/data_table_607x541.png)

To calculate this number, we need to first add a formula for Tax Amount (Order Amount \* Tax Rate). Additionally, we need a formula that calculates the Average Item Cost (Order Amount/Item Count). These formulas will automatically display in your Data Table as additional columns. For more information about creating formulas in your Analysis Grid, see [Analysis Grid - Adding Formula Columns](https://devnet.logianalytics.com/hc/en-us/articles/4419715058455-Analysis-Grid-Adding-Formula-Columns).

![](https://devnet.logianalytics.com/hc/article_attachments/7522774430103/noteicon.jpg) If you're going to aggregate a Formula column (created by executing a calculation), the "order of operations" may be important. For example, should the Analysis Grid do the calculation first, then apply the aggregation, or apply the aggregation and then do the calculation? The choice can result in completely different results.

Once you've created your formulas, follow the steps below to create a custom aggregate:

1. Select the **gear** icon to access the Aggregation feature:

![](https://devnet.logianalytics.com/hc/article_attachments/7522856162455/select_gear_icon.png)

Info displays the Table configuration options.

1. Select the **Aggregate** tab.
2. To add a Custom aggregation, select the **Data Column** to be aggregated from the column list.
3. Then, select **Aggregate Function** > **Custom**. Info displays the Add a custom aggregation for (name of Data Column) pop-up window:

![](https://devnet.logianalytics.com/hc/article_attachments/7522880978455/custom_aggregation_popup.png)

1. Type a name for the Custom Aggregation.
2. Customize the formula by utilizing the drop-down arrows to select a **Column**, **Formula**, and **Operator**.
3. Select **Add**. Logi Info displays your custom aggregation in the Data Table and adds your new custom Aggregate Function to the drop-down list for future use:

![](https://devnet.logianalytics.com/hc/article_attachments/7522819039895/custom_agg_in_dropdown.png)

1. You can turn the custom aggregation on/off by selecting the **column header** > **Aggregations** > **Remove** (Custom Agg):

![](https://devnet.logianalytics.com/hc/article_attachments/7522856186135/turn_off_agg_367x375.png)

1. To edit your Custom Aggregation, select the **Aggregation hyperlink** in the Aggregates section:

![](https://devnet.logianalytics.com/hc/article_attachments/7522850161047/aggregate_hyperlink.png)

Info displays the Add a custom aggregation pop-up window.

1. Manage the list of custom aggregates by selecting the adjacent **Replace** button or **trash can** icon.

## Data Type-Specific Custom Aggregation

The other type of custom aggregate you can create in your Analysis Grid are applied to a specific data type(s).

1. Begin by selecting the **gear** icon to access the Aggregation feature:

![](https://devnet.logianalytics.com/hc/article_attachments/7522856162455/select_gear_icon.png)

Info displays the Table configuration options.

1. Select the **Aggregate** tab.
2. Select **All** from the Data Column drop-down list.
3. Then, select **Aggregate Function** > **(Custom)**. Logi Info displays the Add a custom aggregation for the selected data type (s) pop-up window:

![](https://devnet.logianalytics.com/hc/article_attachments/7522881048343/select_custom.png)

1. Type a name for the Custom Aggregation.
2. Customize the formula by entering your formula, or, utilize the drop-down arrows to select a **Column**, **Formula**, and **Operator**. Data type-specific Custom Aggregates use a @CurrentColumn token as a column reference and replace the column on which it's applied, as shown below. Reminder that you cannot apply a sum or count aggregate on a variable character field or text column.
3. Select the **All** Data Type check box, or select individual data type(s) to apply the custom aggregate:

![](https://devnet.logianalytics.com/hc/article_attachments/7522856241815/select_data_types.png)

![](https://devnet.logianalytics.com/hc/article_attachments/7522774430103/noteicon.jpg) You must select at least one check box to create the aggregate. Selecting all ensures that the custom aggregate is applied to all of the columns.

1. Select **Create**. Info displays your custom aggregation in the Data Table and adds your new custom Aggregate Function to the drop-down list for future use.
2. You can turn the custom aggregation on/off by selecting the **column header** > **Aggregations** > **Remove** (Custom Agg).
3. To edit your Custom Aggregation, select the Aggregation hyperlink in the Aggregates section:

![](https://devnet.logianalytics.com/hc/article_attachments/7522819104663/select_aggregate_hyperlink_711x459.png)

Info displays the Add a custom aggregation pop-up window.

11. Manage the list of custom aggregates by selecting the adjacent **Replace** button or **trash can** icon.
