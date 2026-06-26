---
title: "Custom Metric Examples"
id: 4402955524247
section: "Manipulate Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402955524247-Custom-Metric-Examples
updated_at: 2021-08-07T17:30:25Z
---

# Custom Metric Examples

# Custom Metric Examples

  

The following commonly used custom metrics demonstrate custom metric syntax. These examples work with your data source only if your data source contains fields of the same name and type. Change the fields to make them work with your data sources.

The following custom metric is the sum of a metric (`totalfatalinjuries`) between a specific date (`2018-01-01`) and the current date:

```
SUM(totalfatalinjuries) WHERE eventdate BETWEEN '2018-01-01' AND DATE()
```

in which:

* `totalfatalinjuries` can be replaced by your own metric
* `eventdate` can be replaced by your own date attribute
* `2018-01-01` can be replaced by a different specific date

The following aggregated field formula is the sum of a metric (`totalfatalinjuries`) from the previous period:

```
SUM(totalfatalinjuries) TRANSFORM eventdate = PreviousPeriod()
```

in which:

* `totalfatalinjuries` can be replaced by your own metric
* `eventdate` can be replaced by your own date attribute

The following custom metric produces the difference between the current sum of a metric (`totalfatalinjuries`) and the sum of the same metric from the previous period:

```
SUM(totalfatalinjuries) - (SUM(totalfatalinjuries) TRANSFORM eventdate = PreviousPeriod())
```

in which:

* `totalfatalinjuries` can be replaced by your own metric
