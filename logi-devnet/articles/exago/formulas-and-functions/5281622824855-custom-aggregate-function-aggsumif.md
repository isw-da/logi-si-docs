---
title: "Custom Aggregate Function: AggSumIf()"
id: 5281622824855
section: "Formulas and Functions"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281622824855-Custom-Aggregate-Function-AggSumIf
updated_at: 2022-05-03T22:08:06Z
---

# Custom Aggregate Function: AggSumIf()

# Custom Aggregate Function: AggSumIf()

Review the documentation on [Custom Aggregate Functions](https://devnet.logianalytics.com/hc/en-us/articles/5281616754327-Custom-Aggregate-Functions) for full details on developing and implementing this function.

|  |  |
| --- | --- |
| Description | Returns the sum of values of `dataToAggregate` with a corresponding *true*`condition`.  Only those records with a *true*`condition` are included in the sum. `condition` is *true* if it meets any one of the following conditions:  * it is the Boolean type `true` * it is the string “*true*“ * it is the function `True()` * it is a non-zero number, or can be converted to a non-zero number |
| Arguments | * `dataToAggregate`: the data field to sum, accepts data fields or cell references. Required. * `condition`: a Boolean value or expression that when *true* will include this item in the sum. Required. * `recordLevel`: indicates whether to aggregate by recordLevel (*true*) or entity level (*false*). Optional, defaults *true* if not provided. |
| Namespaces | * WebReports.Api.Common * WebReports.Api.Custom |
| Example | To return the total number of products ordered in quarter 4: `AggSumIf({OrderDetails.Quantity}, If(QuarterNumber({Orders.OrderDate})=4))` 255 |

## Program Code

```
public class AggSumIf : ICustomAggregator
{
    double sum = 0;
  
	public void AddValue(SessionInfo sessionInfo, object value, params object[] args)
	{
        // Treat non-numbers as 0
        double input;
        if (!double.TryParse(value.ToString(), out input))
            return;
  
        bool isTrue;
        double number;
        // true, "true", and non-zero numbers are valid truthy values
        if ((bool.TryParse(args[0].ToString(), out isTrue) && isTrue) ||
            (double.TryParse(args[0].ToString(), out number) && number != 0))
            this.sum += input;
	}
  
	public object Result(SessionInfo sessionInfo)
	{
		return this.sum;
	}
}
```
