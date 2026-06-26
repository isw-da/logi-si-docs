---
title: "Analysis Grid - Filtering Rows "
id: 4419707291927
section: "Use Dashboards & Visuals - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707291927-Analysis-Grid-Filtering-Rows
updated_at: 2022-10-12T17:10:21Z
---

# Analysis Grid - Filtering Rows 

# Analysis Grid - Filtering Rows

Click the **Filter** tab to use the feature that lets you remove table rows that don't meet your criteria:

![](https://devnet.logianalytics.com/hc/article_attachments/7522864015511/usingag_12.png)

Here's how to use this feature:

1. Select the **Filter Column** containing the values to be compared.  
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/7522880731287/usingag_12a.png)  
   As shown above, you'll see that the options are grouped and color-coded to make it easier for you to identify them. If you created any Formula columns, they'll be in there, too.
2. Set the filtering criteria by selecting a **Comparison** operator from the list.   
     
   Comparison operators include = , <, >, < =, > =, *Not =*, *Starts With*, *Not Start With*, *Contains*, *Not Contains*, Like, Not Like. If the Filter Column is a date, then *Date Range* is available and some other options are not. The *Starts With* and *Contains* operators are useful for finding values at the beginning or within text data. The *Not Contains* and *Does Not Start With* operators work in the opposite manner.   
     
   Comparison operators *In List* and *Not In List* allow comparison against a comma-separated list of values you enter in the Value text box.  
     
   When using *In List* or *Not In List* comparisons in filters, multiple values can be entered, separated by commas. However, the values themselves may *include* commas, causing incorrect comparisons.  
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/7522849904407/usingag_32.png)  
   To address this, values for these types of filters are now represented in the controls by visual "pills" that enclose the complete value, as shown above. The filter uses the complete string within the pill during its comparison operation.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/7522833642647/usingag_33.png)  
   Pills with included commas are created by entering the first part of the value and pressing comma. This creates a blue pill as shown above. Then place your cursor *inside* the pill and type the rest of the value. Press tab to exit the pill and repeat the process for the next value, if desired.  
     
   The Filter feature is usually used to compare column data and a value you enter, but you can also directly compare the values in two data columns:  
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/7522849931671/usingag_34.png)  
   To do this, first select a Filter Column, as shown above, and a supported Comparison operator (= < > <= >= Not=). Then select the second column from the list displayed when you click the **[]** button, or enter the column name within square brackets.  
     
   Depending on the comparison chosen, additional input controls may be displayed, for example, for date ranges. Or you may see a browse button that lets you select values for comparison from a pop-up list of choices.

3. Enter a comparison **Value**. Wildcard characters (\*, %) are *not* allowed in these values. Click **Add**. Rows that don't meet these criteria will be removed from the table.
4. As filters are created, they're added to the filter list. Use the adjacent **Replace** button and **Remove** (trash can ) icon to manage the list.

![](https://devnet.logianalytics.com/hc/article_attachments/7522818868247/usingag_13.png)

If you add multiple filters, only rows that meet *all* the conditions will be retained (an "And" situation). Clicking the *And* link in the Filters list, shown above, changes it to an *Or* link, so rows that meet *any* of the conditions will be retained. A set of four arrow icons will also appear by the trash can icon. These can be used to re-order the precedence of the filters or to group them together in various arrangements using parentheses.

![](https://devnet.logianalytics.com/hc/article_attachments/7522833666839/usingag_13a.png)

Once filters are configured, you can use the gear icon to collapse the Filter configuration area, as shown above. Check boxes and filter descriptions will remain visible in the area. Uncheck a check box to disable a filter. If you click the description text, simple controls will appear, allowing you to change the filter value.

## Filtering by Dates

If the Filter Column selected is a **date****type** column, the interface presents different value controls:

![](https://devnet.logianalytics.com/hc/article_attachments/7522833673111/usingag_14.png)

You may choose to filter on a **Specific Date** and either type it in or select it from a pop-up calendar. Or, you can filter using a **Sliding Date** value and select from a long list of relative dates (*Last Week End, Last Month Start*, *90 Days Ago*, *Current Hour, Last Hour,* etc.)

![](https://devnet.logianalytics.com/hc/article_attachments/7522880783511/usingag_15.png)

If the Comparison option *Range* is chosen, as shown above, different value controls for Starting and Ending dates are displayed. These can be used in a variety of combinations.

![](https://devnet.logianalytics.com/hc/article_attachments/7522745474327/_newplus.jpg) New for 14.2 Selecting the **Customize...** button, or choosing **Customize...** from the drop-down menu allows you to customize the time frame for your analysis. This option is only available for use with date/time-type data when Sliding Date is selected.

![](https://devnet.logianalytics.com/hc/article_attachments/7522774742039/screen_shot_2022-03-30_at_10.08.12_am_839x637.png)

Upon selecting Customize... additional fields generate, with default values, where you can manipulate the data:

![](https://devnet.logianalytics.com/hc/article_attachments/7522752050839/screen_shot_2022-03-30_at_10.06.02_am_1244x382.png)

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) Usually *Start* and *End* is a range. You may need to change your Comparison value.

If you choose any value other than *Hour* in the drop-down list, the value *On* will be added to the Start/End drop-down list. The time picker only displays when Start, End, or On is chosen.

![](https://devnet.logianalytics.com/hc/article_attachments/7522752067863/screen_shot_2022-03-30_at_10.19.45_am_1248x384.png)

Specify a time by selecting the time picker:

![](https://devnet.logianalytics.com/hc/article_attachments/7522756583447/screen_shot_2022-03-30_at_10.21.19_am_1094x292.png)![](https://devnet.logianalytics.com/hc/article_attachments/7522752093335/time_picker.png)

To apply the filter, select **Replace** and **OK**:

![](https://devnet.logianalytics.com/hc/article_attachments/7522788118679/replace.png)

The filtered results reflect the sliding date and specified time.

Click the **Filter** tab or button to hide the panel.

## Filter by Aggregate

You can now apply filters on aggregates in your Analysis Grid. This feature is only supported on the following database versions:

* MySQL > = 8
* SQLServer > = 2005
* Oracle > = 9
* PostegreSQL > = 8

In the example below we grouped the columns Reorder Level and Discontinued. Then, we applied an aggregate of *Count* on the Product Id column, *Discount* on the Supplier Id column, and *Average* on the Unit Price column:

![](https://devnet.logianalytics.com/hc/article_attachments/7522805711767/1_1206x734.png)

Narrow down the results of an aggregated column by applying a filter on the aggregate. In this example, we want to apply an aggregate filter that distinguishes any Count over 10.

1. To access the new feature, select the **Aggregate** tab and then select the **filter** icon:

![](https://devnet.logianalytics.com/hc/article_attachments/7522759452567/select_filter_icon_692x526.jpg)

The Aggregate Filter dialog box appears.

1. Select the **Filter Column** drop-down:

![](https://devnet.logianalytics.com/hc/article_attachments/7522849978775/aggregate_filter.jpg)

1. After you select the desired Filter Column, add a Comparison and enter a Value.
2. Then, select **Add**.

![](https://devnet.logianalytics.com/hc/article_attachments/7522820036887/select_add_aggregate_filter.jpg)

Now, our Analysis Grid displays Count values over 10 for the Product Id column:

![](https://devnet.logianalytics.com/hc/article_attachments/7522759471895/2_1228x849.png)

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) Repeat these steps to add aggregate filters to additional columns.

Currently, the relationship between the two filters is *And*. Select **And** to change the relationship to Or.

![](https://devnet.logianalytics.com/hc/article_attachments/7522818891543/and_or_condition.jpg)

You can temporarily disable one (or both) of these filters by selecting the **gear** icon next to the Filer Column and selecting the corresponding check box:

![](https://devnet.logianalytics.com/hc/article_attachments/7522864096023/disable_aggregate_filter_491x203.jpg)

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) You can also apply filters on the aggregates created through formula and it will populate as an option in the Filter Column drop-down menu. Below is an example of the CountCustomer formula we created using an aggregate:

![](https://devnet.logianalytics.com/hc/article_attachments/7522880854423/countcustomer_column_formula.png)

Once you select Add, the new formula will populate the Filter Column drop-down menu:

![](https://devnet.logianalytics.com/hc/article_attachments/7522864157847/count_customer.png)

For more information about adding aggregate formulas, see [Analysis Grid - Adding Formula Columns](https://devnet.logianalytics.com/hc/en-us/articles/4419715058455-Analysis-Grid-Adding-Formula-Columns).

### Recalculate Based on Filter

The Recalculate based on Filter check box is useful if you want to reset the column's overall aggregate value.

![](https://devnet.logianalytics.com/hc/article_attachments/7522833752599/recaclulate_based_on_filter.jpg)

In this example, the Product Id column has an aggregate of Count that still reflects the overall Count (77) prior to adding the aggregate filter:

![](https://devnet.logianalytics.com/hc/article_attachments/7522818974487/overall_count_508x604.jpg)

After selecting the **Recalculate based on filter** check box, the new Count is 28:

![](https://devnet.logianalytics.com/hc/article_attachments/7522833772311/overall_count_after.jpg)
