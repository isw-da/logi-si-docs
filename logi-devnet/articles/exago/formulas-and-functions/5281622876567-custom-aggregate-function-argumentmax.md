---
title: "Custom Aggregate Function: ArgumentMax()"
id: 5281622876567
section: "Formulas and Functions"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281622876567-Custom-Aggregate-Function-ArgumentMax
updated_at: 2022-05-03T22:08:07Z
---

# Custom Aggregate Function: ArgumentMax()

# Custom Aggregate Function: ArgumentMax()

Review the documentation on [Custom Aggregate Functions](https://devnet.logianalytics.com/hc/en-us/articles/5281616754327-Custom-Aggregate-Functions) for full details on developing and implementing this function.

|  |  |
| --- | --- |
| Description | Returns the corresponding `correspondingValue` associated with the maximum value of `maximizedValue`. |
| Arguments | * `maximizedValue`: the field to find the maximum value of. Required. * `correspondingValue`: the corresponding value to return. Required. * `recordLevel`: indicates whether to aggregate by recordLevel (*true*) or entity level (*false*). Optional, defaults to *true* if not provided. |
| Namespaces | * WebReports.Api.Common * WebReports.Api.Custom |
| Example | To return the name of the most played artist: `ArgumentMax({Spins.Plays}, {Artists.Name})` Jamiroquai |

## Program Code

```
public class MaxMapAggregator: ICustomAggregator
{
	IComparable max;
	object maxKey;

	public void AddValue(SessionInfo sessionInfo, object value, params object[] args)
	{
		// Treat nulls as zero
		if (value == null)
			value = 0;
		else if (!(value is IComparable))
		{
			throw new WrAggregationException(@"Tried to take the maximum of a set 
                                                      containing a non-comparable value");
		}

		if (this.max == null || this.max.CompareTo(value) == -1)
		{
			this.max = (IComparable)value;
			// The "key" to associate with the maximum value is passed as the second
			// argument to this aggregate function, which shows up here as the first item
			// in the args array.
			this.maxKey = args[0];
		}
	}

	public object Result(SessionInfo sessionInfo)
	{
		return this.maxKey;
	}
}
```
