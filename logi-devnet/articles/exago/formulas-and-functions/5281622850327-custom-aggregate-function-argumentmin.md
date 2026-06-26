---
title: "Custom Aggregate Function: ArgumentMin()"
id: 5281622850327
section: "Formulas and Functions"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281622850327-Custom-Aggregate-Function-ArgumentMin
updated_at: 2022-05-03T22:08:07Z
---

# Custom Aggregate Function: ArgumentMin()

# Custom Aggregate Function: ArgumentMin()

Review the documentation on [Custom Aggregate Functions](https://devnet.logianalytics.com/hc/en-us/articles/5281616754327-Custom-Aggregate-Functions) for full details on developing and implementing this function.

|  |  |
| --- | --- |
| Description | Returns the corresponding `correspondingValue` associated with the minimum value of `minimizedValue`. |
| Arguments | * `minimizedValue`: the field to find the minimum value of. Required. * `correspondingValue`: the corresponding value to return. Required. * `recordLevel`: indicates whether to aggregate by recordLevel (*true*) or entity level (*false*). Optional, defaults to *true* if not provided. |
| Namespaces | * WebReports.Api.Common * WebReports.Api.Custom |
| Example | To return the last name of the employee who has the least amount of revenue: `ArgumentMin({OrderDetails.Revenue}, {Employees.LastName})` |

## Program Code

```
public class MinMapAggregator: ICustomAggregator
{
 IComparable min;
 object minKey;

 public void AddValue(SessionInfo sessionInfo, object value, params object[] args)
 {
  // Treat nulls as zero
  if (value == null)
   value = 0;
  else if (!(value is IComparable))
  {
   throw new WrAggregationException(@"Tried to take the minimum of a set 
                                                      containing a non-comparable value");
  }

  if (this.min == null || this.min.CompareTo(value) == 1)
  {
   this.min = (IComparable)value;
   // The "key" to associate with the minimum value is passed as the second
   // argument to this aggregate function, which shows up here as the first item
   // in the args array.
   this.minKey = args[0];
  }
 }

 public object Result(SessionInfo sessionInfo)
 {
  return this.minKey;
 }
}
```
