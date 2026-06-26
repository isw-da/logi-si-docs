---
title: "FilterValue and General Format Best Practices"
id: 5281584461591
section: "Formulas and Functions"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281584461591-FilterValue-and-General-Format-Best-Practices
updated_at: 2022-05-03T22:08:05Z
---

# FilterValue and General Format Best Practices

# FilterValue and General Format Best Practices

The **FilterValue** function may take up to three arguments:

1. *Required*: the filter’s index in the list of filters
2. *Optional*: the sub-index, starting with *1* for filters that contain multiple values (for example filters with an **Is Between**, **Is Not Between**, **Is One Of** or **Is Not One Of** operator). If omitted, filters with multiple values will return a comma-separated list of values.
3. *Optional:* a Boolean to determine if the value should be formatted following the user’s culture setting

For example, consider a report with three filters:

1. `Categories.CategoryName` Is One Of (‘*Confections*‘, ‘*Dairy Products*‘, ‘*Condiments*‘, ‘*Beverages*‘)
2. `Products.UnitPrice` > ‘*7.75*‘
3. `Orders.OrderDate` Is Between ‘*12/01/2020*‘ And ‘*12/31/2020*‘

`FilterValue(1)` will return *Confections, Dairy Products, Condiments, Beverages*

`FilterValue(2)` will return *7.75*

`FilterValue(3,1)` will return *2020-12-01*

The third argument determines if the return value is formatted.

`FilterValue(3,2,1)` will return *12/31/2020*

Most of the time, the third argument should be used when concatenating strings with the return value of `FilterValue()`. For example:

```
=Concatenate("Last order placed on", FilterValue(3,2,1))
```

[General Formatting](https://devnet.logianalytics.com/hc/en-us/articles/5281564235671-Cell-Formatting#General) is the default cell format in advanced reports. If `FilterValue()` has to be used as output into a cell, it is recommended that either the cell format be changed to **Text** and the optional parameter is used.
