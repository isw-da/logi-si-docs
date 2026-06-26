---
title: "Time Period Columns Attributes"
id: 4406818045079
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406818045079-Time-Period-Columns-Attributes
updated_at: 2022-04-06T06:09:50Z
---

# Time Period Columns Attributes

# Time Period Columns Attributes

The attributes for the Time Period Column element are described below:

| Attribute | Description |
| --- | --- |
| Data Column | (Required) Specifies the name of the column in the datalayer that contains the DateTime data from which the Time Period Column will derive its data. |
| ID | (Required) Specifies a unique identifier for the element. |
| Time Period | (Required) Specifies the time period to be derived from the data column. Options include:  * Date (removes Time from ISO 8601 *YYYY-MM-DD* date format) * DayOfMonth (number: *1-31*) * DayOfWeek (number: *0-6*) * DayOfWeekAbbreviation (3 characters: *Mon, Tue, Wed*, etc.) * DayOfWeekName (string: *Sunday, Monday, Tuesday*, etc.) * DayOfYear (number: *1-365*) * FirstDayOfFiscalQuarter (DateTime) *see note below* * FirstDayOfFiscalYear (DateTime) *see note below* * FirstDayOfMonth (number: *1-31*) * FirstDayOfQuarter (DateTime) * FirstDayOfWeek (DateTime) * FirstDayOfYear (DateTime) * FirstHourOfDay (DateTime) * FirstMillisecondOfSecond (number: *1-9999*) * FirstMinuteOfHour (DateTime) * FirstSecondOfMinute (DateTime) * FiscalQuarter (number: *1-4*) * FiscalYear (number: 4-digit year) *see note below* * Hour (number: *1-12* or *1-24*) * LastDayOfFiscalQuarter (DateTime) * LastDayOfFiscalYear (DateTime) *see note below* * LastDayOfMonth (DateTime) * LastDayOfQuarter (DateTime) * LastDayOfWeek (DateTime) * LastDayOfYear (DateTime) * Minute (number: *0 -59*) * Month (number: *1-12*) * MonthAbbreviation (3 characters: *Jan, Feb, Mar*, etc.) * MonthName (string: *January, February, March*, etc.) * Quarter (number: *1-4*) * Second (number: *0-59*) * Week (number: *1-52*) * Year (number: 4-digit year)  This attribute can be set using tokens, such as an @Request token. |
| Include Condition | If the value of this attribute is left blank or contains a formula that evaluates to *True*, the Time Period column is applied to the datalayer. If the value evaluates to *False*, the element is ignored and does not affect the datalayer. |
| Time Period Culture | If set, applies a specific user culture (see discussion below). Default: *en US* |

**Fiscal Periods** - Results are dependent on the Fiscal-related values set in the \_Settings definition using the **Globalization** element (see next section).
**DateTime Values** - Options that create DateTime values in the datalayer put them in ISO 8601 date format:

YYYY-MM-DDThh:mmTZD (e.g. 1997-07-16T19:20+01:00)

## Globalization Settings

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

The starting point for the "FiscalQuarter..." values the element calculates can be specified by creating a **constant** in the \_Settings definition, named FirstDayOfQ1. Its value specifies the month and year, in the format *MM/YY*.

## Culture Settings

The Time Period Column element itself can be made **culture-aware**. This can affect the text returned by time periods for **names** and **abbreviations** and the numbers returned for the day of the week. The element's **Time Period Culture** attribute can be set to a specific culture value or configured to use the client browser's culture settings by entering the @Function.UserCulture~ token. The default is the "invariant" culture, which is basically US English.

Here are three examples of **DayOfWeekName** values, as returned by using the default, French, and Spanish culture settings:

![](https://devnet.logianalytics.com/hc/article_attachments/4417562991511/timeperiod_11.png)
