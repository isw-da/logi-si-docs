---
title: "Time Period Columns Advanced Usage Example"
id: 4406822608151
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822608151-Time-Period-Columns-Advanced-Usage-Example
updated_at: 2022-04-06T06:09:51Z
---

# Time Period Columns Advanced Usage Example

# Time Period Columns Advanced Usage Example

Time Period Columns can be really useful in providing **data** for use by **other** elements. The following example of a Crosstab Table uses them to provide data for the necessary sorting and crosstab filters.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562989975/timeperiod_07.png)

In the example definition above, a **Crosstab Table** has been added and its datalayer's SQL query returns data including a column named OrderDate. Two **Time Period Column** elements have been added which create new columns in the datalayer based on OrderDate. The example above shows one of these ("OrderDay") set to derive the day of the week, a number, from OrderDate.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575463319/timeperiod_08.png)

The datalayer's **Sort Filter** element can now use the new OrderDay column as its sort column, as shown above. This ensures the data for the report will be sorted in day-of-the-week order.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562990615/timeperiod_09.png)

The datalayer's **Crosstab Filter** element is configured, as shown above, to use the new OrderDayName column as its crosstab column. This ensures the crosstab columns will be arranged one per day of the week.  
![](https://devnet.logianalytics.com/hc/article_attachments/4417575463703/timeperiod_10.png)

For the sake of brevity, the additional elements used to display the crosstab data are not shown here, but the first few rows of the resulting table are shown above.
In conclusion, the **Time Period Column** element can create derived columns in a datalayer that are immediately available for use in other elements for purposes such as filtering and grouping.
