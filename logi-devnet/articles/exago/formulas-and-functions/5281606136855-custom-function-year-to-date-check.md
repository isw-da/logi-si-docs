---
title: "Custom Function: Year to Date Check"
id: 5281606136855
section: "Formulas and Functions"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281606136855-Custom-Function-Year-to-Date-Check
updated_at: 2022-05-03T22:08:06Z
---

# Custom Function: Year to Date Check

# Custom Function: Year to Date Check

This Custom Function must be implemented by a system administrator before it can be used in a report. Contact the System Administrator for more information.

Returns *true* if the provided date value is within this year to date, otherwise returns *false*.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
>
> This function is intended to be used for conditional aggregates. If one wanted to calculate the sum of one data field within the bounds of this year to date, they would use this structure:
>
> ```
> =AggSum( If( YTDCheck( {dateField} ), {fieldToSum}, 0))
> ```

## Arguments

1. dateValue – A date, dateTime, or date string that will be inspected to see if it is within this year to date.

## Program Code

```
//create return value and grab user input
bool retVal = false;
DateTime myDate = DateTime.Parse(args[0].ToString());

//return true if input date is within this YTD
DateTime firstDay = new DateTime(DateTime.Today.Year, 1, 1);
if(myDate >= firstDay && myDate <= DateTime.Today)
{
  retVal = true;
}
return retVal;
```
