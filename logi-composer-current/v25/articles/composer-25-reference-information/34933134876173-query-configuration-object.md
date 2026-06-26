---
title: "Query Configuration Object"
id: 34933134876173
section: "Composer 25 Reference Information"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933134876173-Query-Configuration-Object
updated_at: 2026-05-26T22:09:20Z
---

# Query Configuration Object

# Query Configuration Object

The query configuration is contained in a JSON object including specific key:value pairs. You do not need to include unused keys. The exceptions are:

* the `time` key, which must specify a `timeField` value if a `player` is to be used by the query
* you must use one and only one of the following keys: `fields`, `groups`, and `dimensions`. Using none or more than one of these keys results in an error.

Additionally, if you use the query configuration object to create a query that is then used to supply data to an embedded visual, it must have the following keys:

* `filters`, though it can be defined as `[]` if you do not want to apply any filter
* `metrics`, without which the visual will not have data to present

## Example

var yourConfigObject = {
// time zone
tz: 'UTC',
// field used for time
// start and finish times/dates
// format: {+/-}YYYY-MM-DD HH:mm:ss.SSS
// + means inclusive, - means exclusive
time: {
timeField: '\_ts',
from: '+2016-10-23 22:30:15.500',
to: '-2016-11-23 22:30:15.500'
},
// rate of querying, in seconds
// timeWindowScale: 'ROLLING' means that start time advances with end time
// timeWindowScale: 'PINNED' means that start time does not advance with end time
player: {
speed: 1,
pauseAfterRead: false,
timeWindowScale: 'ROLLING'
},
filters: [
{ path: 'usersentiment', operation: 'BETWEEN', value: [-0.5, 0.5] },
{ path: 'color', operation: 'IN', value: [‘red’, 'green', 'blue'] },
{ path: 'age', operation: 'LT', value: 21 },
{ path: 'color', operation: 'NOTIN', value: ['red', 'green', 'blue'] }
],
// count does not take a metric function. Other metrics require one.
// func can be 'sum', 'avg', 'min', 'max', 'count', 'countd'
metrics: [
{ name: 'price', func: 'avg' },
{ name: 'count' }
],
// metricFunc is used to sort by metric values. It is required if you sort by a metric other than count. It accepts the same options as metric's func key.
groups: [
{ name: 'usercity', limit: 200, sort: { dir: 'asc', name: 'usercity' } },
{ name: 'department', limit: 10, sort: { dir: 'asc', name: 'count' } },
{ name: 'color', limit: 5, sort: { dir: 'asc', name: 'usersentiment', metricFunc: 'avg' } }
],
// Your query must have groups or fields, but may not have both groups and fields.
fields: [
{ name: 'price', limit: 50 },
{ name: 'usercity', limit: 50 }
],
};

Each possible parameter is described below.

## `tz: ''`

Sets the timezone used by the web app. Use ISO standard abbreviations. The value defaults to the Composer server time.

## `time: {}`

A time object, which specifies the time range to be included in the query. Essentially, this parameter filters the query based on time using the time field, from, and to elements.

| Key | Usage | Notes | Examples |
| --- | --- | --- | --- |
| `timeField` | String.  Sets the field to be used as the time measurement. | This field refers to the data source columns containing the time measurement, rather than any label that appears in the user interface. |  |
| `from` | String.  Sets the earliest time from which data should be included in the query. | Use the format `[-/+]YYYY-MM-DD HH:mm:ss.SSS` (preceded by a + or - to include or exclude the specified time). | `+2024-10-23 10:30:15.500` to start at 23 October 2024 10:30:15.5, inclusive |
| `to` | String.  Sets the latest time to which data should be included in the query. | Use the format `[-/+]YYYY-MM-DD HH:mm:ss.SSS` (preceded by a + or - to include or exclude the specified time). | `-2025-01-10 10:30:15.500` to start at 10 January 2025 10:30:15.5, exclusive. |

## `player: {}`

A player object, which specifies parameters for retrieving data from a source. It consists of the speed, pauseAfterRead, and timeWindowScale elements. If you include a player object in the query, you must also include a time object that includes at least the timeField element.

| Key | Usage | Notes | Examples |
| --- | --- | --- | --- |
| `speed` | Integer.  Sets the interval at which data should be retrieved, in seconds. | Accepted values are: 1 (every second), 60 (every minute), 3600 (every hour), and 86400 (daily). | 60 |
| `pauseAfterRead` | Boolean.  Sets whether the data stream, if applicable, should be paused after initial retrieval. | `data set empty` message may result when `pauseAfterRead` is set to false with a non-live data source. | true |
| `timeWindowScale` | String.  `'ROLLING'` or `'PINNED'`. Sets whether the time interval of retrieved data “rolls” or stays “pinned” to its original starting point (the from element of the time object). | The retrieval of a rolling time window starts at the point where the last retrieval finished. The retrieval of a pinned time window always starts at the same point, which is provided by the from element.  The image below shows rolling time windows above the timeline, and pinned windows beneath it. | `'ROLLING'`  `'PINNED'` |

## `filters: [{},{}]`

Array of filter objects. Filter objects are applied to the data query using logical-and operations so that data is passed from the data query only if it satisfies all applied filters. Each filter consists of a path, an operation, and a value.

| Key | Usage | Notes | Examples |
| --- | --- | --- | --- |
| `path` | String.  The name of the group or metric on which the filter operates. | This name is that of the data source column containing the group or metric of the filter, rather than the label that appears in the user interface. | `customer_gender`  `customer_age`  `user_occupation` |
| `operation` | String.  The logical operator used by the filter. | Valid options include the following:   |  |  | | --- | --- | | logical operation | key value | | < | 'LT' | | <= | 'LE' | | == | 'EQUALS' (case sensitive) | | == | 'EQUALSI' (case insensitive) | | >= | 'GE' | | > | 'GT' | | in a set | 'IN' | | not in a set | 'NOTIN' | | between two values | 'BETWEEN' | | != | 'NOTEQUALS' | | text search | 'TEXT\_SEARCH' | | filter-level AND | 'AND' | | filter-level OR | 'OR' | | `'EQUALSI'`  `'BETWEEN'`  `'NOTIN'` |
| `value` | Single value or array of values.  The value(s) considered by the logical operation. | If two or more values are needed, such as for a logical set or for a ‘BETWEEN’ operation, they should be provided in an array.  Single values, such as required for an ‘EQUALS’ or ‘LT’ operation, should be provided as simple values. | `'female' [21,65]`  `['teacher','lawyer', 'plumber']` |

## `groups: [{},{}]`

Array of group objects. Group objects specify which data is returned by a query and how it is grouped. Each group object has a name, limit, and a sort object.

**Note:** 
If `groups` is defined, `fields` and `dimensions` must be omitted.

| Key | Usage | Notes | Examples |
| --- | --- | --- | --- |
| `name` | String.  The name of the attribute to be used for grouping data. | This name is the name of the data source column containing the attribute, rather than the label that appears in the user interface. | `'home_state'` |
| `limit` | The maximum number of distinct items to be included in the data set. | If the limit is set lower than the total number of items in a group, not all members of the group will be included in the returned data set.  For example, if the limit is set to 25, then the group us\_state could not return data from all fifty US states. | 50 |
| `sort` | A sort object. See below. |  | `{dir: 'desc', name: 'home_state'}` |

## `sort: {}`

A sort object. Sort objects describe the way in which a group is ordered. Each sort object consists of the name of the group or metric for the sorting and the direction in which the group’s data is sorted.

| Key | Usage | Notes | Examples |
| --- | --- | --- | --- |
| `name` | String.  The name of the group or metric on which the filter operates. | This name is that of the data source column containing the group or metric by which groups are to be sorted, rather than the label that appears in the user interface. | `'home_state'` |
| `dir` | String.  The direction of the sorting. | Valid options are `'asc'` and `'desc'` for ascending and descending sorts, respectively. | `'asc'` |
| `metricFunc` | String.  Required to sort by a metric value. Not permitted if you sort by count or by a group. | Valid options include the following:`'min'`, `'max'`, `'avg'`, `'sum'`, `'calc'`, `'distinct_count'`, `'last_value'`, `'percentiles'` | `'sum'` |

Array of group objects. Group objects specify which data is returned by a query and how it is grouped. Each group object has a name, limit, and a sort object.

## `fields: [{},{}]`

Array of field objects. A field object is used to take a whole column of data without grouping it by the items found in the column. Each field object consists of the name of a column.

**Note:** 
If `fields` is defined, `groups` and `dimensions` must be omitted.

| Key | Usage | Notes | Examples |
| --- | --- | --- | --- |
| `name` | String. | This name is that of the data source column containing the field. | `'home_state'` |
| limit | Integer. | The maximum number of records to report. | 50 |

## `metrics: [{},{}]`

Array of metric objects. Each metric object indicates a column to be returned and used by the data query as a metric. Each metric object can have a name and function.

| Key | Usage | Notes | Examples |
| --- | --- | --- | --- |
| `name` | String.  The name of the metric. | This name is that of the data source column containing the metric, rather than the label that appears in the user interface. | `'user_age'` |
| `function` | String.  Determines the function applied to the metric. | Valid options include the following:`'min'`, `'max'`, `'avg'`, `'sum'`, `'calc'`, `'distinct_count'`, `'last_value'`, `'percentiles'` | `'avg'` |
