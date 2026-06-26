---
title: "Custom Aggregate Function: AggCountIf()"
id: 5281622698391
section: "Formulas and Functions"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281622698391-Custom-Aggregate-Function-AggCountIf
updated_at: 2022-05-03T22:08:09Z
---

# Custom Aggregate Function: AggCountIf()

# Custom Aggregate Function: AggCountIf()

Review the documentation on [Custom Aggregate Functions](https://devnet.logianalytics.com/hc/en-us/articles/5281616754327-Custom-Aggregate-Functions) for full details on developing and implementing this function.

|  |  |
| --- | --- |
| Description | Returns the count of values of `dataToAggregate` with a corresponding *true*`condition`.  Only those records with a *true*`condition` are included in the count. `condition` is *true* if it meets any one of the following conditions:  * it is the Boolean type `true` * it is the string “*true*“ * it is the function `True()` * it is a non-zero number, or can be converted to a non-zero number |
| Arguments | * `dataToAggregate`: the data field to count, accepts data fields or cell references. Required. * `condition`: a Boolean value or expression that when *true* will include this item in the count. Required. * `recordLevel`: indicates whether to aggregate by recordLevel (*true*) or entity level (*false*). Optional, defaults *true* if not provided. |
| Namespaces | * WebReports.Api.Common * WebReports.Api.Custom |
| Example | To return the number of current products: `AggCountIf({Products.ProductName}, Not({Products.Discontinued}))` 60 To return the number of orders whose revenue was greater than $15,000.00: `AggCountIf({Orders.OrderId}, if({OrderDetails.Revenue} > 15000))` 5 |

## Program Code

```
public class AggCountIf : ICustomAggregator
{
    int count = 0;
  
	public void AddValue(SessionInfo sessionInfo, object value, params object[] args)
	{
        bool isTrue;
        double number;
        if ((bool.TryParse(args[0].ToString(), out isTrue) && isTrue) || 
            (double.TryParse(args[0].ToString(), out number) && number != 0))
            ++this.count;
	}
  
	public object Result(SessionInfo sessionInfo)
	{
		return this.count;
	}
}
```
