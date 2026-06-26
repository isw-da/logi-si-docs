---
title: "Composer 6.9.2 Enhancements"
id: 4405859456535
section: "Logi Composer Version 6 Release Notes"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859456535-Composer-6-9-2-Enhancements
updated_at: 2022-04-25T15:19:14Z
---

# Composer 6.9.2 Enhancements

# Composer 6.9.2 Enhancements

This topic describes the significant enhancements in Composer 6.9.2.

* [*Custom Metric Date and Time Aggregation Function Changes*](#CustomMetrics)
* [*Dashboard Import Changes*](#DashImport)

## Custom Metric Date and Time Aggregation Function Changes

Custom metrics now support the `now()` and `time_add` functions used by row-level expressions. The original custom metric `DATE()`, `DateADD`, and `DateSUB` functions still work but should no longer be used. They are deprecated in this release and will be removed in a future release. Instead, use the `now()` and `time_add` functions.

The following table provides examples of how the original functions can be replaced by the `now()` and `time_add` functions.

| Original Function Specification | New Function Specification |
| --- | --- |
| `DATE()` | `NOW()` |
| `DateADD('YEAR', 1, '2021-01-01')` | `TIME_ADD('YEAR', 1, '2021-01-01')` |
| `DateADD('MONTH', 1, DATE())` | `TIME_ADD('YEAR', 1, NOW())` |
| `DateSUB('YEAR', 1, '2021-01-01')` | `TIME_ADD('YEAR', -1, '2021-01-01')` |

See [*Date and Time Filter Aggregation Functions*](https://devnet.logianalytics.com/hc/en-us/articles/4405851015447-Date-and-Time-Filter-Aggregation-Functions).

## Dashboard Import Changes

You can now use the API to import a dashboard using a new overwrite policy, so that dashboards with the same name are overwritten instead of being imported with a slightly altered name. A new query parameter, `strategy`, has been added for the `POST /api/dashboards/import` endpoint. Valid values can be `OVERWRITE` or `USE_EXISTING_OR_CREATE`.

* Specify `OVERWRITE` to implement the new overwrite policy.
* Specify `USE_EXISTING_OR_CREATE` to continue to use the existing import policy (importing the dashboard with a slightly altered name). This is the default value and will be used if `strategy` is not specified.

For more information about requesting the overwrite policy and its behavior, see [*Overwrite Policy Behavior*](https://devnet.logianalytics.com/hc/en-us/articles/4405850983831-Import-a-Dashboard#overwrite).
