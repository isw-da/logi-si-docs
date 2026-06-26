---
title: "InfoGo - Filtering Rows"
id: 4419723209879
section: "Use InfoGo/Discovery Module - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723209879-InfoGo-Filtering-Rows
updated_at: 2022-07-17T02:23:19Z
---

# InfoGo - Filtering Rows

# InfoGo - Filtering Rows

Click the **Filter** tab or button to use the feature that lets you *remove* InfoGo table rows that don't meet your criteria.

![](https://devnet.logianalytics.com/hc/article_attachments/7522751898135/usinginfogo125_15.png)

Here's how to use this feature:

1. Select the **Filter Column** containing the values to be compared:  
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/7522774623639/usinginfogo125_16.png)  
   A shown above, you'll see that the options are grouped and color-coded to make it easier for you to identify them. If you created any Formula columns, they'll be in there, too.
2. Set the filtering criteria by selecting a **Comparison** operator from the list.   
     
   Comparison operators include = , <, >, < =, > =, *Not =*, *Starts With*, *Not Start With*, *Contains*, *Not Contains*, Like, Not Like. If the Filter Column is a date, then *Date Range* is available and some other options are not. The *Starts With* and *Contains* operators are useful for finding values at the beginning or within data and will work with both text and numeric data. The *Not Contains* and *Does Not Start With* operators work in the opposite
   manner. Comparison operators *In List* and *Not In List* allow comparison against a comma-separated list of values you enter in the Value text box.  
     
   Comparison operators *In List* and *Not In List* allow comparison against a comma-separated list of values you enter in the Value text box.  
     
   When using *In List* or *Not In List* comparisons in filters, multiple values can be entered, separated by commas. However, the values themselves may *include* commas, causing incorrect comparisons.  
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/7522756440727/usinginfogo125_98.png)  
   To address this, values for these types of filters are now represented in the controls by visual "pills" that enclose the complete value, as shown above. The filter uses the complete string within the pill during its comparison operation.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/7522782923159/usinginfogo125_99.png)  
   Pills with included commas are created by entering the first part of the value and pressing comma. This creates a blue pill as shown above. Then place your cursor *inside* the pill and type the rest of the value. Press tab to exit the pill and repeat the process for the next value, if desired.  
     
   The Filter feature is usually used to compare column data and a value you enter, but you can also directly compare the values in two data columns:  
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/7522782933527/usinginfogo125_100.png)  
   To do this, first select a Filter Column, as shown above, and a supported Comparison operator (= < > <= >= Not=). Then select the second column from the list displayed when you click the **[]** button, or enter the column name within square brackets.  
     
   Depending on the comparison chosen, additional input controls may be displayed, for example, for date ranges. Or you may see a browse button that lets you select values for comparison from a pop-up list of choices.
3. Enter a comparison **Value.** Wildcard characters (\*, %) are *not* allowed in these values. Click **Add**. Rows that don't meet these criteria will be removed from the table.
4. As filters are created, they're added to the filter list. Use the adjacent **Replace** button and **Remove** icon to manage the list.

![](https://devnet.logianalytics.com/hc/article_attachments/7522766337303/usinginfogo125_17.png)

If you add multiple filters, initially rows that meet *all* the conditions will be retained (an "And" situation). Clicking the *And* button in the Filters list, shown above, changes it to an *Or* button, so rows that meet *any* of the conditions will be retained. A set of four icons will also appear by the Remove icon. These can be used to re-order the precedence of the filters or to group them together in various arrangements using parentheses.

![](https://devnet.logianalytics.com/hc/article_attachments/7522766348951/usinginfogo125_18.png)

Once filters are configured, you can use the gear icon to collapse the
Filter configuration area, as shown above. check boxes and filter
descriptions will remain visible in the area. Uncheck a check box to
disable a filter. If you click the description text, simple controls
will appear, allowing you to change the filter value.

## Filtering by Dates

If the Filter Column selected is a **date****type** column, the interface presents different value controls:

![](https://devnet.logianalytics.com/hc/article_attachments/7522788040599/usinginfogo125_19.png)

You may choose to filter on a **Specific Date** and Time and either type it in or select it from a pop-up calendar. Or, as shown above, right, you can filter using a **Sliding Date** value and select from a long list of relative dates (*Last Week End, Last Month Start*, *90 Days Ago*, Current Hour, Last Hour, etc.)

![](https://devnet.logianalytics.com/hc/article_attachments/7522756518679/usinginfogo125_20.png)

If the Comparison option *Date Range* is chosen, as shown above,
different value controls for Starting and Ending dates, which can be
used in a variety of combinations are displayed.

You can also use a combination of specific and sliding date comparisons.

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

When done, click the **Filter** tab to hide the panel.
