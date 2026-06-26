---
title: "Custom Aggregate Function: AggConcat()"
id: 5281605820567
section: "Formulas and Functions"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281605820567-Custom-Aggregate-Function-AggConcat
updated_at: 2022-05-03T22:08:09Z
---

# Custom Aggregate Function: AggConcat()

# Custom Aggregate Function: AggConcat()

Review the documentation on [Custom Aggregate Functions](https://devnet.logianalytics.com/hc/en-us/articles/5281616754327-Custom-Aggregate-Functions) for full details on developing and implementing this function.

|  |  |
| --- | --- |
| Description | Returns a concatenated string of values separated by a specified delimiter string. |
| Arguments | * `dataToAggregate`: the value to concatenate, accepts data fields or cell references. Required. * `delimiter`: the string to separate each value with. Optional, defaults to comma and a space if not provided. * `recordLevel`: indicates whether to aggregate by recordLevel (*true*) or entity level (*false*). Optional, defaults to *true* if not provided. |
| Namespaces | * WebReports.Api.Common * WebReports.Api.Custom |
| Example | `AggConcat({Categories.CategoryName}, ":")` Beverages:Condiments:Seafood `AggConcat({Categories.CategoryName})` Beverages, Condiments, Seafood |

## Program Code

```
public class AggJoin : ICustomAggregator
{
    System.Text.StringBuilder stringBuilder = new System.Text.StringBuilder();
    string delimiter = ", ";
  
	public void AddValue(SessionInfo sessionInfo, object value, params object[] args)
	{
        // Skip blank values
	 if (value == null || value.ToString() == string.Empty)
            return;
  
        if (args.Length != 0)
        	this.delimiter = args[0].ToString();
  
        this.stringBuilder.Append(value);
        this.stringBuilder.Append(this.delimiter);
	}

	public object Result(SessionInfo sessionInfo)
	{
        string retVal = this.stringBuilder.ToString();
  
        // Remove the trailing delimiter
        if (this.delimiter.Length > 0 && retVal.Length > 0)
            retVal = retVal.Remove(retVal.Length - this.delimiter.Length);
  
        return retVal;
	}
}
```
