---
title: "Alert Definition Data Query Structures"
id: 43700990917901
section: "Composer 26 Developer Tools"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700990917901-Alert-Definition-Data-Query-Structures
updated_at: 2026-05-29T14:07:10Z
---

# Alert Definition Data Query Structures

# Alert Definition Data Query Structures

The data query used in an alert definition always specifies a filter condition to be evaluated. Different kinds of data query conditions can be specified: raw, KPI, single group by, or multigroup by queries. Simple filters and aggregate filters are used to establish these query conditions.

This section describes and provides examples for the filter structure and the structures for all query types.

* [Simple Filters](#Filters)
* [Aggregate Filters](#Aggregat)
* [Raw Data Query Conditions](#Raw)
* [KPI Data Query Conditions](#KPI%C2%A0Data)
* [Single Group By Queries](#Single)
* [Multigroup By Queries](#Multiple)

## Simple Filters

**Note:** 
Because alert conditions are checked periodically, filter conditions must be set properly, especially if the queried data is limited to a dynamic timeframe.

Filters are specified using the following structure. The example specifies a dynamic filter that looks for sales records with sale dates that occurred in the last month.

"filters": [
{
"operation": "BETWEEN",
"path": {
"name": "sale\_date"
},
"value": [
"$start\_of\_month\_-1\_month",
"$end\_of\_month\_-1\_month"
]
}
],

The following parameters are included in the filter structure.

| Parameter | Specifies |
| --- | --- |
| `operation` | The filter operation. |
| `path` | The field in the data source that should be evaluated. Use the `name` field to specify the field name. |
| `value` | The values or range of values for the filter. |

## Aggregate Filters

Aggregate filters define thresholds using the `aggregateFilters` object in the following structure. Usually a single threshold is defined, but more complex aggregate filters can be specified. The following aggregate filter example searches for groups (for example, product categories) with 1 to 1000 sales records in which the sum of the sales price fell between $2 and $700,000.

"aggregateFilters": [
{
"metric": {
"type": "COUNT"
},
"operation": "BETWEEN",
"value": [
1,
1000
]
},
{
"metric": {
"type": "FIELD",
"field": {
"name": "price"
},
"function": "SUM"
},
"operation": "BETWEEN",
"value": [
2,
700000
]
}
],

The following parameters are included in the `aggregateFilters` query structure.

| Parameter | Specifies |
| --- | --- |
| `metric` | The type of metric. |
| `operation` | The filter operation. |
| `value` | The values or range of values for the filter. |

## Raw Data Query Conditions

A raw data query condition supports only simple filters. The following sample raw query condition searches for sales records with sale dates that occurred in the last month and with prices that equal or exceed $1,000,000.00. When records are found meeting these conditions, and alert notification is sent.

{
...
"condition": {
"sourceId": "<rts-source-id>",
"dataQuery": {
"queryType": "RAW",
"filters": [
{
"operation": "BETWEEN",
"path": {
"name": "sale\_date"
},
"value": [
"$start\_of\_month\_-1\_month",
"$end\_of\_month\_-1\_month"
]
},
{
"path": {
"name": "price"
},
"operation": "GE",
"value": 1000000
}
]
},
"activateAlertWhenData": "EXISTS"
}
}

The following parameters are included in the raw data query structure.

| Parameter | Specifies |
| --- | --- |
| `queryType` | The type of query. For raw data query conditions, this is always `RAW`. The other possible value for this parameter (but not for raw query conditions) is `AGGREGATE`. |
| `filters` | The [filter conditions](#Filters) for the raw data query. |

## KPI Data Query Conditions

A KPI query condition is a single-dimension query, without aggregations. Filters can be used to reduce the data to be evaluated. The threshold is defined by aggregate filters.

The following sample KPI query condition searches for sales records from the state of Alabama with sale dates that occurred in the last month and with total planned sales between $1 and $3,035.00. If no records can be found that meet these conditions, an alert notification is sent.

{
...
"condition": {
"sourceId": "<rts-source-id>",
"dataQuery": {
"queryType": "AGGREGATE",
"filters": [
{
"operation": "BETWEEN",
"path": {
"name": "sale\_date"
},
"value": [
"$start\_of\_month\_-1\_month",
"$end\_of\_month\_-1\_month"
]
},
{
"path": {
"name": "state"
},
"operation": "EQ",
"value": "Alabama"
}
],
"dimensions": [
{
"aggregations": []
}
],
"aggregateFilters": [
{
"metric": {
"type": "FIELD",
"field": {
"name": "plannedsales"
},
"function": "SUM"
},
"operation": "BETWEEN",
"value": [
1.00,
3035.00
]
}
]
},
"activateAlertWhenData": "NOT\_EXISTS"
}
}

The following parameters are included in the KPI data query structure.

| Parameter | Specifies |
| --- | --- |
| `queryType` | The type of query. For KPI data query conditions, this is always `AGGREGATE`. The other possible value for this parameter (but not for KPI query conditions) is `RAW`. |
| `filters` | The [filter conditions](#Filters) for the KPI data query. |
| `dimensions` | The aggregation type (`TERM` or `TIME`). No aggregation type is supported for KPI data query conditions. |
| `aggregateFilters` | The [threshold conditions](#Aggregat) for the KPI data query. |

## Single Group By Queries

Single group by queries are similar to KPI data queries, but add one aggregation. Filters can be used to reduce the data to be evaluated. The threshold is defined by aggregate filters. The window attribute may be defined for the dimension section. But it does not affect the query execution logic.

The following sample single group by query condition searches for sales records from the state of Alabama, aggregated by product group, with sale dates that occurred in the last month and with total planned sales between $1 and $3,035.00. If no records can be found that meet these conditions, an alert notification is sent.

{
...
"condition": {
"sourceId": "<rts-source-id>",
"dataQuery": {
"queryType": "AGGREGATE",
"filters": [
{
"operation": "BETWEEN",
"path": {
"name": "sale\_date"
},
"value": [
"$start\_of\_month\_-1\_month",
"$end\_of\_month\_-1\_month"
]
},
{
"path": {
"name": "state"
},
"operation": "EQ",
"value": "Alabama"
}
],
"dimensions": [
{
"aggregations": [
{
"type": "TERMS",
"field": {
"name": "product\_group"
}
}
]
}
],
"aggregateFilters": [
{
"metric": {
"type": "FIELD",
"field": {
"name": "planned\_sales"
},
"function": "SUM"
},
"operation": "BETWEEN",
"value": [
1.00,
3035.00
]
}
]
},
"activateAlertWhenData": "NOT\_EXISTS"
}
}

The following parameters are included in the single group data query structure.

| Parameter | Specifies |
| --- | --- |
| `queryType` | The type of query. For single group by data query conditions, this is always `AGGREGATE`. The other possible value for this parameter (but not for single group by query conditions) is `RAW`. |
| `filters` | The [filter conditions](#Filters) for the single group by data query. |
| `dimensions` | The aggregation type (`TERM` or `TIME`). Both `TERM` and `TIME` aggregations are supported. However, time aggregations cannot request the **Include Blanks** function. |
| `aggregateFilters` | The [threshold conditions](#Aggregat) for the single group by data query. |

## Multigroup By Queries

Multigroup by queries are the same as Single Group By queries, except that they allow for more than one aggregation.

**Note:** 
Top of the Top sorting is not supported; only simple sorting is supported. We recommend that no sorting be specified at all.

The following sample multigroup by query condition searches for sales records from the state of Alabama, aggregated by sales day and city, with sale dates that occurred in the last month and with total planned sales between $1 and $1.050.00. If records can be found that meet these conditions, an alert notification is sent.

{
...
"condition": {
"sourceId": "<rts-source-id>",
"dataQuery": {
"queryType": "AGGREGATE",
"filters": [
{
"operation": "BETWEEN",
"path": {
"name": "sale\_date"
},
"value": [
"$start\_of\_month\_-1\_month",
"$end\_of\_month\_-1\_month"
]
},
{
"path": {
"name": "state"
},
"operation": "EQ",
"value": "Alabama"
}
],
"dimensions": [
{
"aggregations": [
{
"type": "TERMS",
"field": {
"name": "user\_city"
}
},
{
"type": "TIME",
"field": {
"name": "saledate"
},
"granularity": "DAY"
}
]
}
],
"aggregateFilters": [
{
"metric": {
"type": "FIELD",
"field": {
"name": "planned\_sales"
},
"function": "SUM"
},
"operation": "BETWEEN",
"value": [
1000.00,
1050.00
]
}
]
},
"activateAlertWhenData": "EXISTS"
}
}

The following parameters are included in the multigroup by data query structure.

| Parameter | Specifies |
| --- | --- |
| `queryType` | The type of query. For multigroup by data query conditions, this is always `AGGREGATE`. The other possible value for this parameter (but not for multigroup by query conditions) is `RAW`. |
| `filters` | The [filter conditions](#Filters) for multigroup by data query. |
| `dimensions` | The aggregation type (`TERM` or `TIME`). Both `TERM` and `TIME` aggregations are supported. However, time aggregations cannot request the **Include Blanks** function. |
| `aggregateFilters` | The [threshold conditions](#Aggregat) for the multigroup by data query. |
