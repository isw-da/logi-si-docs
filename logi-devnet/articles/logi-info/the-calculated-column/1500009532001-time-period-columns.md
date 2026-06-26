---
title: "Time Period Columns"
id: 1500009532001
section: "The Calculated Column"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009532001-Time-Period-Columns
updated_at: 2021-06-17T01:58:40Z
---

# Time Period Columns

# Time Period Columns

Logi application developers frequently need to work with parts of **dates** and **timestamps** and often employ various string parsing techniques to do so. The **Time Period Column** element, described in this topic, allows developers to directly access the date and time parts of data without resorting to VB or Javascript functions and string parsing.

* About the Time Period Column
* [Simple Usage Example](#Simple)
* [Advanced Usage Example](#Advanced)
* [Time Period Column Attributes](#Attributes)

## About the Time Period Column

The Time Period Column is similar to other elements designed to **extend** the **data** available in a datalayer. Like the **Calculated Column** element, the Time Period Column is added as a child element beneath a datalayer and adds a **new column** to the datalayer. This column contains **derived data** which is accessible using an @Data token. In this case, the derived data can be any of the parts of a datetime value.

Time Period Columns can also be configured to be **culture-aware** so that the values derived will agree with the culture settings of the user's browser.

Examples of the Time Period Column in use can be seen in the **Datalayer Columns** sample application on DevNet.

### Dynamic Application

Beginning in v10.0.319, the Time Period Column element has an **Include Condition** attribute:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771601303/timeperiod_10.gif)

If the value of this attribute is left blank or contains a formula that evaluates to *True*, the element is applied to the datalayer. If the value evaluates to *False*, the element is ignored and does not affect the datalayer. This powerful feature allows developers to dynamically determine if the Time Period Column will be added to the datalayer or not.

## Simple Usage Example

The following example illustrates how the Time Period Column works by displaying all of the possible date and time data parts the element can produce.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771601559/timeperiod_01.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778501399/timeperiod_01a.gif)

In the definition shown above, a **Data Table** and a **DataLayer.Static** element have been added. A single **Static Data Row**, with a single column ("OrderDate") whose value is a date and time, has been added to the datalayer.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778501655/timeperiod_02.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778501911/timeperiod_02a.gif)

As shown above, **Time Period Column** elements are then added as children of the datalayer. For the purpose of illustration, one of them has been added for each possible datetime part that can be derived. The **DataColumn** attribute identifies the datalayer column, in this case "OrderDate", from which the Time Period Column's data will be derived. The **ID** attribute provides an arbitrary name for the new column that will be added to the datalayer and will be used later with
an @Data token to reference the derived data. The **TimePeriod** attribute determines which datetime information to derive from the data column. The **TimePeriodCulture** attribute allows the element to derive
data in a culture-aware fashion. These attributes are discussed in more detail in a later section of this topic.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771601943/timeperiod_03.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771602199/timeperiod_03a.gif)

As shown above, a **Data Table Column** element has been added and **Label** elements placed beneath it to display the data in each of the Time Period Columns. Note that the assigned **ID** of a Time Period Column is used with an @Data token in the same manner as any actual data column. *Logi Info developers attempting to duplicate this example may care to use the AutoColumns element instead of adding a Data Table Column element and all the Label and New Line elements shown.*

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778502167/timeperiod_04.gif)

And the results are shown above.

The **TimePeriod** attribute value can be set using **tokens**. Consider a situation, for example, where the user can choose options at runtime, from an Input Select List, such as Quarterly, Monthly, or Yearly. If the select list's **onChange** event is used to refresh the page, then the user's choice will be available as an @Request token and this token can be used to set the TimePeriod attribute value. This allows the content of the Time Period Column to be dynamic based on user input, which
can be very useful
in controlling data to be displayed.

## Advanced Usage Example

Time Period Columns can be really useful in providing **data** for use by **other** elements. The following example of a Crosstab Table uses them to provide data for the necessary sorting and crosstab filters.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778502423/timeperiod_06.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771602711/timeperiod_06a.gif)

In the example definition above, a **Crosstab Table** has been added and its datalayer's SQL query returns data including a column named OrderDate. Two **Time Period Column** elements have been added which create new columns in the datalayer based on OrderDate. The example above shows one of these ("OrderDay") set to derive the day of the week, a number, from OrderDate.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778502679/timeperiod_07.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778502935/timeperiod_07a.gif)

The datalayer's **Sort Filter** element can now use the new OrderDay column as its sort column, as shown above. This ensures the data for the report will be sorted in day-of-the-week order.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771602967/timeperiod_08.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778503191/timeperiod_08a.gif)

The datalayer's **Crosstab Filter** element is configured, as shown above, to use the new OrderDayName column as its crosstab column. This ensures the crosstab columns will be arranged one per day of the week.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778503575/timeperiod_09.gif)

For the sake of brevity, the additional elements used to display the crosstab data are not shown here, but the resulting table is shown above.

In conclusion, the **Time Period Column** element can create derived columns in a datalayer that are immediately available for use in other elements for purposes such as filtering and grouping.

## Time Period Column Attributes

The attributes for the Time Period Column element are described below:

| Attribute | Description |
| --- | --- |
| DataColumn | The name of the column in the datalayer that contains the datetime data from which the Time Period Column will derive its data. |
| ID | A unique identifier for the element. |
| TimePeriod | The time period to be derived from the data column. Options include:   * Year (4 digits) * Quarter (1-4) * Month (number: 1-12) * MonthAbbreviation (3 characters: Jan, Feb, Mar, etc.) * MonthName * Week (number: 1-52) * Date (removes Time from ISO 8601 date format) * DayOfMonth (number: 1-31) * DayOfWeek (number: 0-6) * DayOfWeekAbbreviation (3 characters: Mon, Tue, Wed, etc.) * DayOfWeekName * DayOfYear (number: 1-365) * Hour (number: 1-12 or 1-24) * Minute (number: 1-60) * Second (number: 1-60) * FirstDayOfQuarter * LastDayOfQuarter * FirstDayOfMonth * LastDayOfMonth * FirstDayOfWeek * LastDayOfWeek * FirstDayOfFiscalQuarter * LastDayOfFiscalQuarter * FirstDayOfYear (added in v10.0.479) * LastDayOfYear (added in v10.0.479) * FiscalQuarter * FirstHourOfDay (added in v10.2.314) * FirstMillisecondOfSecond (added in v10.2.314) * FirstMinuteOfHour (added in v10.2.314) * FirstSecondOfMinute (added in v10.2.314)   This attribute can be set using tokens, such as an @Request token. |
| TimePeriodCulture | If set, applies a specific user culture (see discussion below). Default: *en US* |

The FiscalQuarter-related attribute options create values in the datalayer in ISO 8601 date format:

YYYY-MM-DDThh:mmTZD (e.g. 1997-07-16T19:20+01:00)

### Globalization Settings

The value for the first day of the week can be set in the \_Settings definition using the **Globalization** element. Its **First Day of Week** attribute can be set to one of these values:

* 0 = Sunday (the default value)
* 1 = Monday
* 2 = Tuesday
* 3 = Wednesday
* 4 = Thursday
* 5 = Friday
* 6 = Saturday

This attribute value will affect the "FirstDay..." and "LastDay..." values the element calculates (except for FiscalQuarter).

Another Globalization attribute that affects calendars is **First Day of Fiscal Year**. Set this attribute to determine when the fiscal year will start, if not on January 1st. This attribute value specifies the starting month and day, in the format *MM/DD*.

The starting point for the FiscalQuarter..." values the element calculates can be specified by creating a **constant** in the \_Settings definition, named FirstDayOfQ1. Its value specifies the month and year, in the format *MM/YY*.

### Culture Settings

The Time Period Column element itself can be made **culture-aware**. This can affect the text returned by time periods for **names** and **abbreviations** and the numbers returned for the day of the week. The element's **TimePeriodCulture** attribute can be set to a specific culture value or configured to use the client browser's culture settings by entering the @Function.UserCulture~ token. The default is the "invariant" culture, which is basically US English.

Here are three examples of **DayOfWeekName** values, as returned by using the default, French, and Spanish culture settings:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778503831/timeperiod_05.gif)

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778504087/timeperiod_05a.gif)

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771603351/timeperiod_05b.gif)
