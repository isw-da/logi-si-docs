---
title: "Analysis Grid - Filtering Rows"
id: 4406822101271
section: "Use Dashboards & Visuals - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822101271-Analysis-Grid-Filtering-Rows
updated_at: 2022-04-06T06:03:17Z
---

# Analysis Grid - Filtering Rows

# Analysis Grid - Filtering Rows

Click the **Filter** tab or button to use the feature that lets you remove table rows that don't meet your criteria:

![](https://devnet.logianalytics.com/hc/article_attachments/4417584182679/usingag_12.png)

Here's how to use this feature:

1. Select the **Filter Column** containing the values to be compared.  
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417591969431/usingag_12a.png)  
   As shown above, you'll see that the options are grouped and color-coded to make it
   easier for you to identify them. If you created any Formula columns,
   they'll be in there, too.
2. Set the filtering criteria by selecting a **Comparison** operator from the list.   
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417575410199/__new12.8.png) Comparison operators include = , <, >, < =, > =, *Not =*, *Starts With*, *Not Start With*, *Contains*, *Not Contains*, Like, Not Like. If the Filter Column is a date, then *Date Range* is available and some other options are not. The *Starts With* and *Contains* operators are useful for finding values at the beginning or within text data. The *Not Contains* and *Does Not Start With* operators work in the opposite
   manner.   
     
    Comparison operators *In List* and *Not In List* allow comparison against a comma-separated list of values you enter in the Value text box.  
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417575435927/notev12.7base.png)When using *In List* or *Not In List* comparisons in filters, multiple values can be entered, separated by commas. However, the values themselves may *include* commas, causing incorrect comparisons.  
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417584183703/usingag_32.png)  
   To address this, values for these types of filters are now represented in the controls by visual "pills" that enclose the complete value, as shown above. The filter uses the complete string within the pill during its comparison operation.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417575907479/usingag_33.png)  
   Pills with included commas are created by entering the first part of the value and pressing comma. This creates a blue pill as shown above. Then place your cursor *inside* the pill and type the rest of the value. Press tab to exit the pill and repeat the process for the next value, if desired.  
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417575435927/notev12.7base.png)The Filter feature is usually used to compare column data and a value you enter, but you can also directly compare the values in two data columns:  
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417591969815/usingag_34.png)  
   To do this, first select a Filter Column, as shown above, and a supported Comparison operator (= < > <= >= Not=). Then select the second column from the list displayed when you click the **[]** button, or enter the column name within square brackets.  
     
   Depending on the comparison chosen, additional input controls may be displayed, for example, for date ranges. Or you may see a browse button that lets you select values for comparison from a pop-up list of choices.

3. Enter a comparison **Value**. Wildcard characters (\*, %) are *not* allowed in these values. Click **Add**. Rows that don't meet these criteria will be removed from the table.
4. As filters are created, they're added to the filter list. Use the adjacent **Replace** button and **Remove** (Trashcan) icon to manage the list.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584184343/usingag_13.png)

If you add multiple filters, only rows that meet *all* the conditions will be retained (an "And" situation). Clicking the *And* link in the Filters list, shown above, changes it to an *Or* link, so rows that meet *any*
of the conditions will be retained. A set of four arrow icons will also
appear by the trash can icon. These can be used to re-order the
precedence of the filters or to group them together in various
arrangements using parentheses.

![](https://devnet.logianalytics.com/hc/article_attachments/4417591970071/usingag_13a.png)

Once filters are configured, you can use the gear icon to collapse the Filter configuration area, as shown above. Check boxes and filter descriptions will remain visible in the area. Uncheck a check box to disable a filter. If you click the description text, simple controls will appear, allowing you to change the filter value.

## Filtering by Dates

If the Filter Column selected is a **date****type** column, the interface presents different value controls:

![](https://devnet.logianalytics.com/hc/article_attachments/4417584184599/usingag_14.png)

![](https://devnet.logianalytics.com/hc/article_attachments/4417575410199/__new12.8.png)You may choose to filter on a **Specific Date** and either type it in or select it from a pop-up calendar. Or, you can filter using a **Sliding Date** value and select from a long list of relative dates (*Last Week End, Last Month Start*, *90 Days Ago*, *Current Hour, Last Hour,* etc.)

![](https://devnet.logianalytics.com/hc/article_attachments/4417575908375/usingag_15.png)

If the Comparison option *Range* is chosen, as shown above, different value controls for Starting and Ending dates are displayed. These can be used in a variety of combinations.

Click the **Filter** tab or button to hide the panel.
