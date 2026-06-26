---
title: "Custom Metric Examples"
id: 34932848105101
section: "Manipulate Data In The Composer 25 Data Store"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932848105101-Custom-Metric-Examples
updated_at: 2026-05-26T22:07:02Z
---

# Custom Metric Examples

# Custom Metric Examples

  

The following commonly used custom metrics demonstrate custom metric syntax. These examples work with your data source only if your data source contains fields of the same name and type. Change the fields to make them work with your data sources.

The following custom metric is the sum of a metric (`totallatearrivals`) between a specific date (`2018-01-01`) and the current date:

SUM(totallatearrivals) WHERE eventdate BETWEEN '2018-01-01' AND DATE()

in which:

* `totallatearrivals` can be replaced by your own metric
* `eventdate` can be replaced by your own date attribute
* `2018-01-01` can be replaced by a different specific date

The following aggregated field formula is the sum of a metric (`totallatearrivals`) from the previous period:

SUM(totallatearrivals) TRANSFORM eventdate = PreviousPeriod()

in which:

* `totallatearrivals` can be replaced by your own metric
* `eventdate` can be replaced by your own date attribute

The following custom metric produces the difference between the current sum of a metric (`totallatearrivals`) and the sum of the same metric from the previous period:

SUM(totallatearrivals) - (SUM(totallatearrivals) TRANSFORM eventdate = PreviousPeriod())

in which:

* `totallatearrivals` can be replaced by your own metric
