---
title: "Custom Aggregate Function: AggDistinctAvg()"
id: 5281605909143
section: "Formulas and Functions"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281605909143-Custom-Aggregate-Function-AggDistinctAvg
updated_at: 2022-05-03T22:08:07Z
---

# Custom Aggregate Function: AggDistinctAvg()

# Custom Aggregate Function: AggDistinctAvg()

Review the documentation on [Custom Aggregate Functions](https://devnet.logianalytics.com/hc/en-us/articles/5281616754327-Custom-Aggregate-Functions) for full details on developing and implementing this function.

|  |  |
| --- | --- |
| Description | Returns the average of only unique values in a series of values. |
| Arguments | * `dataToAggregate`: the value to include the calculation, accepts data fields or cell references. Required. * `recordLevel`: indicates whether to aggregate by recordLevel (*true*) or entity level (*false*). Optional, defaults to *true* if not provided. |
| Namespaces | * WebReports.Api.Common * WebReports.Api.Custom * System.Collections.Generic |
| References | * System.Core.dll |
| Example | `AggDistinctAvg({OrderDetails.Quantity})` |

## Program Code

```
public class AggDistinctAvg : ICustomAggregator
{
    HashSet<Decimal> list = new HashSet<Decimal>();
  
	public void AddValue(SessionInfo sessionInfo, object value, params object[] args)
	{
		Decimal curVal;
  
        if (value == null)
            curVal = 0;
        else if (!Decimal.TryParse(value.ToString(), out curVal))
        {
            throw new WrAggregationException(@"Tried to take the average of a set
                                              containing a non-number");
        }
  
        this.list.Add(curVal);
	}

	public object Result(SessionInfo sessionInfo)
	{
        Decimal sum = 0;
        foreach (Decimal val in list)
        {
            sum += val;
        }
        return sum/this.list.Count; // should never be 0
	}
}
```
