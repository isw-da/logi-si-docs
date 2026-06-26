---
title: "PerformanceSetting"
id: 4415504742039
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415504742039-PerformanceSetting
updated_at: 2021-12-10T03:09:03Z
---

# PerformanceSetting

# PerformanceSetting

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **queryTimeoutValue**  integer |  | An array of child ValueTreeNode objects. |  |
| **queryTimeoutDefaultValue**  integer |  | The default value for Query Timeout (`3600` s) |  |
| **useNoLockValue**  boolean |  | Use NOLOCK setting - whether the NOLOCK or equivalent clauses will be used in SQL queries. |  |
| **useNoLockDefaultValue**  boolean |  | The default value for Use NOLOCK (`true`) |  |
| **dataSourceLimitValue**  integer |  | Data Source Limit - the number of data sources allowed to be used in a single report. |  |
| **dataSourceLimitDefaultValue**  integer |  | The default value for Data Source Limit (`1000`) |  |
| **queryLimitValue**  integer |  | Query Limit - the number of data sources allowed to be used in a single report. |  |
| **queryLimitDefaultValue**  integer |  | The default value for Query Limit (`100000`) |  |
| **pivotColumnLimitValue**  integer |  | Pivot Column Limit - the number of data sources allowed to be used in a single report. |  |
| **pivotColumnDefaultValue**  integer |  | The default value for Pivot Column Limit (`100000`) |  |
| **fieldLimitValue**  integer |  | Field Limit - the number of data sources allowed to be used in a single report. |  |
| **fieldLimitDefaultValue**  integer |  | The default value for Field Limit (`1000`) |  |
| **filterLimitValue**  integer |  | Filter Limit - the number of data sources allowed to be used in a single report. |  |
| **filterLimitDefaultValue**  integer |  | The default value for Filter Limit (`1000`) |  |
| **tenantId**  string (GUID) | Y | The id of the tenant   null if the setting belongs to system |  |
| **modified**  datetime | Y | The modification datetime |  |

**Sample**:

```
{"queryTimeoutValue":3600,"queryTimeoutDefaultValue":3600,"useNoLockValue":true,"useNoLockDefaultValue":true,"dataSourceLimitValue":1000,"dataSourceLimitDefaultValue":1000,"tenantId":null}
```
