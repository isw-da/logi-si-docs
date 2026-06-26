---
title: "Visualization Variable Descriptions"
id: 4405851154199
section: "Composer v6 Reference Information"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851154199-Visualization-Variable-Descriptions
updated_at: 2021-09-21T01:29:27Z
---

# Visualization Variable Descriptions

# Visualization Variable Descriptions

Composer uses default values provided in a data source configuration to determine how that data source displays a particular visual. Each variable required by the visual, such as "X Axis" or "Group by", is provided its default value which is recorded in an object in the source configuration. These variables point to fields in the data source so that, for instance, "Y Axis" might draw its values from the field "sales\_price". When embedding a visual in a visual, you can provide it with a `variables` key, the value of which lists the visual's variables and the settings that you want for them.

This topic is a reference that explains the syntax of each type of variable description. For information about using these variable descriptions to override a visual's default settings, see
[*Configure Visuals via Visualization Variables*](https://devnet.logianalytics.com/hc/en-us/articles/4405859134487-Configure-Visuals-via-Visualization-Variables) For information about embedding a visual in a custom web application, see
[*Embed a Visual in Your Web Page*](https://devnet.logianalytics.com/hc/en-us/articles/4405850883735-Embed-a-Visual-in-Your-Web-Page).

## Example of a Variables Key and Value

Here is an example of a variables object for the packed bubbles chart.

```
variables: {     
'Bubble Size': 'count',     
'Chart Name': '',     
'Bubble Color': 'price:avg:{"autoShowColorLegend":true}',     
'Chart Description': '',     
'Group By': '{ "name":"usergender", "limit":20, "sort": {"name": "count", "dir": "desc"} }'     
}
```

In the example above, there are some important features described in the following notes.

Notes:

* `'Bubble Size': 'count',`: The `count` metric is a system metric provided by Composer. Its default UI label is "Volume". This metric does not require or accept function.
* `'Chart Name': '',`: `Chart Name` is an example of an optional constant. It can be left null.
* `'Bubble Color': 'price:avg:{"autoShowColorLegend":true}',`: Here, `Bubble Color` is an example of a metric variable used to control a visual's colors. The stringified value is not a standard JSON object.

  + `price` is the field (column) from the data source used as the metric value.
  + `avg` is the aggregation function applied to the metric value. Available functions are listed in [*Supported Aggregation Functions*](https://devnet.logianalytics.com/hc/en-us/articles/4405859304727-Supported-Aggregation-Functions).
  + `{"autoShowColorLegend":true}` is an example of a color-control object. Color-control objects have two purposes.

    1. They control the assignment of colors to the elements of a visual.
    2. They control the display of labels, legends, and so forth ***in the Composer client application***. These parts of a color control object do not affect the embedding of a visual in your custom application.
  + If you omit the color-control object, also omit the second colon (:) in the string.
  + If the metric is `count`, which does not accept or require a function, omit the function and simply use two colons (**::**) to separate count from the color-control object if there is a color-control object, for example:

    ```
    'Color Metric' : 'count::{"colorSet":"ZoomSequential"}'
    ```
* `'Group By': '{ "name":"usergender", "limit":20, "sort": {"name": "count", "dir": "desc"} }'`: Here, `Group By` is an example of a [grouped query](#Grouped). Its value is a stringified group object just like the ones used in [query configurations](https://devnet.logianalytics.com/hc/en-us/articles/4405851145879-Query-Configuration-Object).

## Visual Variables

Composer's Embedding API supports the following types of visual variables.

* [*Grouped Query*](#Grouped)
* [*Multigroup*](#Multi-Group)
* [*Histogram Group*](#Histogra)
* [*Metric*](#Metric)
* [*Multimetric*](#Multi-Me)
* [*Box Plot Metric*](#Box)
* [*Ungrouped Query*](#Ungroupe)
* [*Visual Constants*](#Visual)

The JSON objects that describe them are subject to change and they should be considered part of Composer's internal APIs. For more information about using internal APIs, see [Cautionary Note About Internal APIs](https://devnet.logianalytics.com/hc/en-us/articles/4405859434647-Cautionary-Note-About-Internal-APIs).

For an explanation of how to use the visual variables described below to configure an embedded visual, see [*Configure Visuals via Visualization Variables*](https://devnet.logianalytics.com/hc/en-us/articles/4405859134487-Configure-Visuals-via-Visualization-Variables).

### Grouped Query

Used for making aggregated group-bys from a field (column of data). The grouped query variable's description follows the same format as a group in the [*Query Configuration Object*](https://devnet.logianalytics.com/hc/en-us/articles/4405851145879-Query-Configuration-Object).

```
'Buying Demographic': '{ "name":"usergender", "limit":20, "sort": {"name":"count","dir":"desc"} }'
```

Where:

* `Buying Demographic` is the name of the grouped query
* `name` specifies the field ID of the group.
* `limit` identifies the maximum number of groups to be aggregated
* `sort` contains another simple object
  + `name` specifies the field ID to be used for sorting the groups
  + `dir` identifies the direction of sorting, either `asc` for ascending order or `desc` for descending order

### Multigroup

Provides multiple levels of grouping under a single header. A multi-group variable is a stringified array of grouped queries. Each of the listed groups is described in the same manner as a group in the [*Query Configuration Object*](https://devnet.logianalytics.com/hc/en-us/articles/4405851145879-Query-Configuration-Object).

```
'Multi Group By': '[ {"name":"usergender", "limit":50, "sort":{"name":"count","dir":"desc"}}, {"name":"group", "limit":20, "sort": {"name":"count","dir":"desc"}} ]'
```

For a description of the elements in the array, see the description of a [*Grouped Query*](#Grouped).

### Histogram Group

The histogram group variable type provides a breakdown of metric values by segments, or bins, for example, incomes from $0 to $10000, $10001 to $30000, $30001 to $55000, and so forth. The histogram group is only supported by data sources that also support histograms.

```
'Bins Color': '#1f78b4',  
'Cumulative Line Color': '#ff7f00',  
'Chart Name': '',  
'Chart Description': '',  
'Group By':  '{ 
"binsType":"auto","binsCount":10,"binsWidth":100,"values":"absolute","cumulative":false,"name":"datenumberpattern"}" 
}'
```

Where:

* `Bins Color` is a constant value
* `Cumulative Line Color` is a constant value
* `Chart Name` is a constant value
* `Chart Description` is a constant value
* `Group By` is a histogram group object. This object is not used elsewhere in Composer and it specifies the properties of the distribution "bins" into which metric values are gathered.

### Metric

Provides a measurement of some aggregation. Metric variables require the name of the field (column) of the data source that provides the values for that visual variable, together with the function applied to the values. For example:

```
"Transaction Value": "saleprice:avg"
```

Where:

* `Transaction Value` is the name of the metric variable
* `saleprice`is the name of the field (column) holding the data for the variable
* `avg` is the aggregation function applied to the metric. In this case, as `Transaction Value` data is grouped, the average `saleprice` will be queried.

For a list of available aggregation functions, see
[*Supported Aggregation Functions*](https://devnet.logianalytics.com/hc/en-us/articles/4405859304727-Supported-Aggregation-Functions)
.

### Multimetric

Provides a group of measurements under a single header. Multimetric variables require a space-separated list of the field names (columns) from the data source that provide the values for that visual variable, together with the function applied to the values, separated by colon. For example:

```
"Model Stats": "costperunit:avg priceperunit:avg sales:sum"
```

Where:

* `Model Stats` is the name of the multi-metric variable.
  + `costperunit`,`priceperunit`, and `sales` are each the name of a field (column) containing a metric value in the data source.
  + `avg` and `sum`are the functions applied to those metrics so that `costperunit`
    and `priceperunit` are of those values and `sales` is a sum total of its values.

### Box Plot Metric

Provides data in a bundled package suitable for the high-performance rendering of box plot diagrams. The box plot metric variable is only supported by data sources that also support box plots. To find out if your data source supports box plots, see [*Composer Data Connector Reference*](https://devnet.logianalytics.com/hc/en-us/articles/4405859436055-Composer-Data-Connector-Reference).

```
'Metric': '{"name":"datenumberpattern","func":"percentiles","args":[0,25,50,75,100]}',     
'Group By': '{"name":"gender","limit":50,"sort":{"dir":"desc","name":"count"}}'
```

Where:

* `Metric`
  is a metric object (see
  [*Query Configuration Object*](https://devnet.logianalytics.com/hc/en-us/articles/4405851145879-Query-Configuration-Object)
  ) with an additional key,
  `args`
  , which specifies the box plot's distribution boundaries, given in percentiles. For instance,
  `[0,25,50,75,100]`
  indicates that the boxes should show first (0-25), second (25-50, third (50-75), and fourth (75-100) quartiles.
* `Group By`
  is an example of a standard group object and follows the same format as a group in the
  [*Query Configuration Object*](https://devnet.logianalytics.com/hc/en-us/articles/4405851145879-Query-Configuration-Object) .

### Ungrouped Query

Provides ungrouped (unaggregated) data with one entry per row in the data source. An ungrouped query is a stringified array of field objects, like those in a
[*Query Configuration Object*](https://devnet.logianalytics.com/hc/en-us/articles/4405851145879-Query-Configuration-Object) . Each field object requires the field name of each data source column that provides the values for that visual variable, together with the limit of rows to query from that column. For example:

```
'Fields List': '[ {"name":"_ts","limit":1000}, {"name":"group","limit":1000}, {"name":"category","limit":1000} ]'
```

Where:

* `Fields List`
  is the name of the ungrouped query of fields (columns)
* `name`
  is the field (column) name to query
* `limit`
  is the maximum number of rows to query from the field

### Visual Constants

Provide a constant value as information about a visual. For example:

```
"Chart Description": "A visual that shows you things."
```
