---
title: "Custom Function: Month Check"
id: 5281600092695
section: "Formulas and Functions"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281600092695-Custom-Function-Month-Check
updated_at: 2022-05-03T22:08:08Z
---

# Custom Function: Month Check

# Custom Function: Month Check

This Custom Function must be implemented by a system administrator before it can be used in a report. Contact the System Administrator for more information.

Returns *true* if the provided date value is within a full specified month, or a specified month to date. Returns *false* otherwise.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
>
> This function is intended to be used for conditional aggregates. If one wanted to calculate the sum of one data field within the bounds of a given month or month to date, they would use this structure:
>
> ```
> =AggSum( If( MonthCheck( {dateField}, monthsBack, toDate ), {fieldToSum}, 0))
> ```

## Arguments

1. `dateValue` — A date, dateTime, or date string that will be inspected to see if it is within this year to date.
2. `monthsBack` — Number of months back from current month. A value of 0 would be “this month”, 1 would be “last month”, etc.
3. `toDate` — Boolean value, set to true to calculate month to date for the specified month, set to false to use the full month.

## Program Code

```
//create return value and grab user input
bool retVal = false;
DateTime myDate = DateTime.Parse(args[0].ToString());
int monthsBack = Convert.ToInt32(args[1].ToString());
bool toDate = Convert.ToBoolean(args[2]);
//subtract appropriate amount of months from today's date
DateTime dateBound = DateTime.Today.AddMonths(-1 * monthsBack);

//create boundary day - this will be last day of month, or current day number if toDate flag is set
int boundaryDay = toDate ? dateBound.Day : DateTime.DaysInMonth(dateBound.Year, dateBound.Month);

//return true if input date is within specified month/MTD
DateTime firstDay= new DateTime(dateBound.Year, dateBound.Month, 1);
DateTime lastDay = new DateTime(dateBound.Year, dateBound.Month, boundaryDay);

if(myDate >= firstDay && myDate <= lastDay)
{
  retVal = true;
}

return retVal;
```
