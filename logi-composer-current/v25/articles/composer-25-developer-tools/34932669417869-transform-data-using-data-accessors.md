---
title: "Transform Data Using Data Accessors"
id: 34932669417869
section: "Composer 25 Developer Tools"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932669417869-Transform-Data-Using-Data-Accessors
updated_at: 2026-05-26T22:06:13Z
---

# Transform Data Using Data Accessors

# Transform Data Using Data Accessors

When working with charting libraries, it is often necessary to structure your data elements in a way the charting libraries understand.

For instance, given the following structure of data element received from the server:

{
"group": ["$0 to $25,000"],
"current": {
"count": 400,
"metrics": {
"price": {
"sum": 52150
}
}
}
}

You may need to transform it to:

{
"name": "$0 to $25,000",
"value": "52150"}

We are interested in the values specified in the `group` array and the metric value defined in `price.sum`. You may be inclined to create a new data array by mapping each data element to the necessary structure like:

var newData = data.map(function(d) {
return {
name: d.group[0],
value: d.current.metrics.price.sum,
};
});

The downside of this approach is that you have now hardcoded the paths of your metric values to a specific field name (“price”) and a specific aggregation function (“sum”).

## A Better Approach Using Data Accessors

A `Data Accessor` is an object with methods that can be used to extract information about the current configuration of query variables. A data accessor can also extract data values out of the data elements received from query execution results.

Example:

var groupAccessor = controller.dataAccessors['Group By'];
var metricAccessor = controller.dataAccessors.Metric;
var newData = data.map(function(d) {
return {
name: groupAccessor.raw(d),
value: metricAccessor.raw(d),
};
});

To access a data accessor, use the `controller.dataAccessors` object. The query variable’s name exists as property in this object. The most commonly used method in data accessors is `raw` which accepts a Composer data element and returns a value corresponding to the query variable. In the above example, we used the `groupAccessor` and `metricAccessor` to retrieve the group and metric values without hard-coding the name of the fields.
