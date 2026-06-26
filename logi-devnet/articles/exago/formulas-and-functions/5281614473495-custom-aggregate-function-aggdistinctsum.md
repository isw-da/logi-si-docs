---
title: "Custom Aggregate Function: AggDistinctSum()"
id: 5281614473495
section: "Formulas and Functions"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281614473495-Custom-Aggregate-Function-AggDistinctSum
updated_at: 2022-05-03T22:08:08Z
---

# Custom Aggregate Function: AggDistinctSum()

# Custom Aggregate Function: AggDistinctSum()

Review the documentation on [Custom Aggregate Functions](https://devnet.logianalytics.com/hc/en-us/articles/5281616754327-Custom-Aggregate-Functions) for full details on developing and implementing this function.

|  |  |
| --- | --- |
| Description | Returns the sum of only unique values in a series. |
| Arguments | * `dataToAggregate`: the value to sum, accepts data fields or cell references. Required. * `recordLevel`: indicates whether to aggregate by recordLevel (*true*) or entity level (*false*). Optional, defaults to *true* if not provided. |
| Namespaces | * WebReports.Api.Common * WebReports.Api.Custom * System.Collections.Generic |
| References | * System.Core.dll |
| Example | `AggDistinctSum({OrderDetails.Revenue})` |

## Program Code

```
public class AggDistinctSum : ICustomAggregator
{
    HashSet<Decimal> list = new HashSet<Decimal>();
  
	public void AddValue(SessionInfo sessionInfo, object value, params object[] args)
	{
		Decimal curVal;
  
        if (value == null)
            curVal = 0;
        else if (!Decimal.TryParse(value.ToString(), out curVal))
        {
            throw new WrAggregationException(@"Tried to take the sum of a set 
                                              containing a non-number");
        }
  
        this.list.Add(curVal);
	}

	public object Result(SessionInfo sessionInfo)
	{
	    Decimal sum = 0;
        foreach (Decimal val in this.list)
        {
            sum += val;
        }
        return sum;
	}
}
```
