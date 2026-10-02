> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Started with the Self-Service Analytics Application Framework

Self-Service Analytics's application framework provides you with the tools you need to query data or embed visuals from Self-Service Analytics in your own application. If you want to use Self-Service Analytics visuals or data in your own custom application, then read on. You might be looking for information about creating your own custom charts, see [Maintain Custom Charts Using the Custom Chart CLI](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/custom-charts/custom-chart-maint-cli).

<Note>
  insightsoftware recommends using [Trusted Access](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/trusted-access-ov) for all embed-related workflows.
</Note>

## Uses of the Application Framework

<table>
  <tbody>
    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/api/query-alone.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=97d413f9dfd8843dd8daa10944763897" alt="" width="139" height="68" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/api/query-alone.png" />
      </td>

      <td>
        **You can use a query to get data from Self-Service Analytics and use it in your own applications.**

        <br />

        You might want to go this route if:

        <br />

        * You just need the data.
        * You already have a visual built into your application and you want to keep it, but need data for it.
      </td>
    </tr>

    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/api/query-beneath.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=42980d86662b3f0f39b3f7c51fd05330" alt="" width="95" height="129" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/api/query-beneath.png" />
      </td>

      <td>
        **You can embed a Self-Service Analytics visual in your application and use your query to supply it with data.**

        <br />

        You might want to go this route if:

        <br />

        * You already have a data query set up.
        * You need to use the same query for more than one visual or for visuals and other purposes.
      </td>
    </tr>

    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/api/query-embedded.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=9c2ca88c05d4bd50a92ef89e4d09d3fa" alt="" width="117" height="116" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/api/query-embedded.png" />
      </td>

      <td>
        **You can embed a Self-Service Analytics visual and give it the information it needs to create its own query.**

        <br />

        You might want to go this route if you really just need one visual based on its own query.
      </td>
    </tr>
  </tbody>
</table>

## Dependencies

The application framework depends upon jQuery. insightsoftware recommends that you link jQuery v1.8 or later.

## Accessing the Application Framework

Self-Service Analytics's application framework is provided by linking the `zoomdata-client.js` file in your web application. You can find `zoomdata-client.js` on your installation at

```
https://<yourserver>/composer/sdk/zoomdata-client.js
```

replacing `<yourserver>` with the URL for your server.

Best practice: Use the `zoomdata-client.js` file found on the Self-Service Analytics installation that will be supplying your data and visuals. There is not usually a problem using different versions, but following this guidance avoids such issues and may help Self-Service Analytics support your work.

Linking the zoomdata-client.js file into your web application gives you access to the `ZoomdataSDK` object. The main purpose of the ZoomdataSDK object is to create a Self-Service Analytics client for your application. Typically, one Self-Service Analytics client is enough, but if you need to access multiple Self-Service Analytics servers, you will need one client for each one.

## Typical Workflows

There is a lot of flexibility with the application framework, but some steps must precede others. When steps must be kept in a particular order, the application framework uses promises to do so. Below is an example of the most common workflow.

### Typical Workflow to Query Data

This workflow creates a query and then queries data from it. This workflow is useful if you already have visuals in your application and you need to supply them with data from Self-Service Analytics. It's also useful if you just want the data.

1. Create a Self-Service Analytics client. Steps to create a client are found in [Use a Data Query](#use-a-data-query).
2. [Create a Self-Service Analytics query.](#configure-the-query)
3. [Run the Self-Service Analytics query.](#run-the-query)
4. [Gather and use the queried data.](#find-your-data)

To help you get going, [download it from GitHub](https://github.com/Zoomdata/SDK20-ApplicationFW-samples).

## Next Steps

It might be that you only need to embed a visual or use data from Self-Service Analytics in your own application. Consider the information at the following links:

* [Use a Data Query](#use-a-data-query)
* [REST API Overview](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/api/rest-api/restapi-overview2)
* [Maintain Custom Charts Using the Custom Chart CLI](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/custom-charts/custom-chart-maint-cli)
* [Trusted Access](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/trusted-access-ov)

<h2 id="use-a-data-query">
  Use a Data Query
</h2>

The Self-Service Analytics JavaScript client library provides functions to query the Self-Service Analytics server for data. This guide uses a method that does not provide event handling for the queries. To assist you in querying for data without handling events, Self-Service Analytics provides:

* This topic, which includes annotated steps for using a query in your own web app.

For information about the structure of the query configuration object, see [Query Configuration Object](#query-configuration-object).

### How a Query Works

The Self-Service Analytics object is used to create a Self-Service Analytics client object. This client is then used to create a query object. To run the query, you pass it and a data processing function to `client.runQuery()`. The client.runQuery() function retrieves data and passes it to the data processing function.

### Steps for Using a Query in Your Web App

These high-level steps for using a query in a web application will guide your work.

1. [Link Dependencies](#link-dependencies)
2. [Organize Application and Security Parameters](#organize-application-and-security-parameters)
3. [Configure the Query](#configure-the-query)
4. [Code the Query](#code-the-query)
5. [Run the Query](#run-the-query)
6. [Find Your Data](#find-your-data)

<h3 id="link-dependencies">
  Link Dependencies
</h3>

Using Self-Service Analytics data queries depends on the `zoomdata-client.js` library. You can link to this library on your Self-Service Analytics server at `composer/sdk/zoomdata-client.js`.

The application framework and example code used in this topic also depend on jQuery (`jQuery.js`). Self-Service Analytics recommends that you link jQuery v1.8 or later. Your script must have access to this library to use the example.

<h3 id="organize-application-and-security-parameters">
  Organize Application and Security Parameters
</h3>

Connecting the webpage to your Self-Service Analytics server requires supplying the Self-Service Analytics server with application and security parameters in the form of JavaScript objects. These two objects are themselves bundled together as a single object to be passed to the `createClient()` method. For example:

```
ZoomdataSDK.createClient({ credentials: credentialConfig, application: applicationConfig })
```

For more information about the application configuration object, see [Application Configuration Object](#application-configuration-object).

For more information about the security configuration object, see [Security Configuration Object](#security-configuration-object).

<h3 id="configure-the-query">
  Configure the Query
</h3>

Before you can create a query, you must create a query configuration object. This object is used to create a query using the Self-Service Analytics client's member function `createQuery()`. For example, the query configuration object below gathers from its data source up to 200 `productGroup` items, sorting them in ascending order and measuring them by their average price, filtering out any groups whose average price is not less than 100.

```javascript theme={null}
var queryConfig = { tz: 'EST', time: { timeField: '_ts' }, player: {}, filters: [{ path: 'price', operation: 'LT', value: 100 }], groups: [{ name: 'productGroup', limit: 200, sort: { dir: 'asc', name: 'productGroup' } }, { name: 'productCategory', limit: 200, sort: {dir: 'asc', name: 'productCategory'} }], metrics: [{ name: 'price', func: 'avg' }] };
```

<h3 id="code-the-query">
  Code the Query
</h3>

The `createClient()` and `runQuery()` functions are used to create and run a query. The `runQuery()` function returns a promise, so you can chain `then()` and `done()` functions to it.

**To code a query:**

1. Instantiate a Self-Service Analytics client if you do not already have one that you want to use.

   ```javascript theme={null}
   ZoomdataSDK.createClient({
   	credentials: credentialConfig,
   	application: applicationConfig }).then((client) => {
        		     // where client is the newly created instance of the client
                  });
   ```

2. Use the client’s `createQuery()` method to create the query. The required parameters are a data source available to the client (based on the server it accesses and its permissions) and a query configuration object.

   ```javascript theme={null}
   client.createQuery({name: 'Real Time Sales'}, queryConfig).then((queryInstance) => {
   			// resulting queryInstance can be used to query for data from the data source
   		});
   ```

<h3 id="run-the-query">
  Run the Query
</h3>

The Self-Service Analytics client library offers different ways to run the query to gather data. This tutorial uses the `client.runQuery()` method, which applies a function to each data object resulting from the query. There is also a `client.run()` method, which returns a thread that contains both the data and other messages that are useful for working with data.

To run a query with client.runQuery():

1. Supply `runQuery()` with these parameters:

   1. a query, which you can create using the steps found in Coding a Query
   2. a function to execute on each object resulting from the query, which should take one parameter

   ```javascript theme={null}
   client.runQuery( theQuery, function( dataObject ) {
   	console.log( 'Data object returned by query: ', dataObject );
   });
   ```

2. Typically, you should chain a .catch() function to handle errors after the event handling function

   ```javascript theme={null}
   .catch( function( theError ) { console.log( 'Error: ', theError ); });
   ```

The function `runQuery()` extracts a data object, rather than a single piece of data, from your query and passes it to your data processing function. For more information about finding the data you need in the returned data object, see [Find Your Data](#find-your-data).

#### Full Example

```javascript theme={null}
ZoomdataSDK.createClient({
	credentials: credentialConfig,
	application: applicationConfig })
.then(client => {
       client.createQuery({name: 'Real Time Sales'}, queryConfig)
              .then(query => {
                    client.runQuery( query, function( dataObject ) {
				// dataObject contains array of data from back end responses.
				console.log( 'Data object returned by query: ', dataObject );
                     });
             })
})
});
```

<h3 id="find-your-data">
  Find Your Data
</h3>

The `runQuery()` function returns a data object or more commonly an array of data objects. These objects each have the same structure, which can be predicted by the query configuration and also discovered programmatically.

#### Structure of the Data Object

Each data object consists of the following objects:

* **current** : an object that contains a count value and a metrics object

  * **count** : indicates the number of rows of data represented in the data object

  * **metrics** : contains one object for each metric

    ```yaml theme={null}
    current: count: 131 metrics: revenue: avg: $23.32 profit: avg: $13.16
    ```

    * individual metric objects contain a key:value pair. The key is the operation of the metric, such as `'``avg``'` or `'min'`. The value is the metric value, for example:
    * The current object above indicates that 131 rows of data are in the queried group, and have an average revenue of \$23.32 and average profit of \$13.16

* **group** : an array listing the groups aggregated in the data object

  * for example

    ```yaml theme={null}
    group: 0: 'Gaithersburg' 1: 'Coffee'
    ```

    The groups object above represents rows of data that satisfy both grouping requirements: `'Gaithersburg'` and `'Coffee'`, which, depending on the data set, may represent sales of coffee in Gaithersburg.

#### Isolate a Piece of Data Manually

If you know the structure of the query in advance, you can reliably anticipate the structure of the data object. The query returns metrics, groups, and fields in the order they are found in the query object.

To verify the order, use a `console.log()` statement to output to the debugging console a sample data object returned by the query.

<img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/api/data-object.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=2bc7c85c73f10522c64c6e30cb80b42f" alt="" width="378" height="266" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/api/data-object.png" />

Individual elements of the data object can be isolated and used as a JavaScript object. For example, to access the average price in the data object above, use either of the following expressions.

```
theDataObject.current.metrics.price.avg
```

or

```
theDataObject['current']['metrics']['price']['avg']
```

<h4 id="isolate-a-piece-of-data-programmatically">
  Isolate a Piece of Data Programmatically
</h4>

You will not always know in advance which metrics, groups, and fields are involved in a data structure. The Query API provides accessor functions to identify programmatically the metrics, groups, and fields involved in a query. These functions are useful in the event that a query is subject to change at runtime. These accessors include:

* `query['metrics'].get()`
* `query['groups'].get()`
* `query['fields'].get()`

Each of the accessors above returns an array of objects with one object for each metric, group, or field, respectively. These objects are structured as they are structured in the query configuration object. For more information about query configuration objects, see [Query Configuration Object](#query-configuration-object). In the event that there are no metrics, groups, or fields in the query, that particular accessor will return an empty array.

Using the accessors, you can use the following steps to programmatically iterate through the metrics, groups, or fields used by your data query.

1. [Create an array with the names of metrics, groups, or fields](#isolate-a-piece-of-data-programmatically)
2. [Use the array to iterate through the returned data objects](#isolate-a-piece-of-data-programmatically)

Each of these steps is described below in more detail.

To create an array with the names of metrics, groups, or fields:

These steps use metrics as an example. You can also use groups or fields with the same procedure by replacing metrics with groups or fields.

1. Call query\['metrics'].get() and assign the returned array to a variable.

   ```javascript theme={null}
   var metrics = query['metrics'].get();
   ```

2. Iterate through the returned array using its forEach() method. Pass to forEach() an anonymous function to extract the name of each metric and add it to an array of the purpose of storing only the names of metrics.

   ```javascript theme={null}
   var metricNames = []; metrics.forEach( function(metric) { metricNames.push( metric.name ); });
   ```

These steps combined produce an array containing only the names of the metric objects, in the same order that they appear in both the returned metric object list and in the query configuration object.

To use the array to iterate through the returned data objects:

These steps use metrics as an example. You can also use groups or fields with the same procedure by replacing metrics with groups or fields.

Use the anonymous function to touch each data point and perform on it whatever operation you need.

```javascript theme={null}
dataObjectArray.forEach( function(dataObject) { console.log( metricName, ' is: ', dataObject['current']['metrics'][metricName]['avg'] ); });
```

In the same way, you can gather and automatically process data by field or group.

## Configure Visuals Using Visualization Variables

When a visual is embedded into a custom application, it uses the default settings determined by the metrics and fields or groups present in the data query that supplies the visual with data. For more information about configuring and creating a data query, see [Query Configuration Object](#query-configuration-object) or [Use a Data Query](#use-a-data-query).

When embedding a visual, you also have the option of overriding default configurations by modifying the configuration of visual settings. You modify the default settings with the `variables` key in the parameter passed to the `visualize()` method.

Before you can encode settings into an embedded visual, you must identify every required setting as well as any optional settings that you wish to use. Visual settings can be identified using an internal REST API method.

The REST API method used in these steps is considered internal to the Self-Service Analytics application. Internal APIs should not be used except as directed. For more information about using internal APIs, see [Cautionary Note About Internal APIs](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/api/rest-api/restapi-overview2#cautionary-note-about-internal-apis).

<h2 id="identify-a-visual-s-visualizationid">
  Identify a Visual's `visualizationID`
</h2>

You can identify a Self-Service Analytics visual's `visualizationID` while working with it. For example, to programmatically identify a visual's default settings using a REST API call, you must have the `visualizationID` handy.

**Identify a visual's `visualizationID`**

1. Open the visual in its dashboard.

2. Find the number at the end of the URL in the address bar of your browser. The `visualizationID` is the section of the number after the plus sign (+).

   <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/vis-id.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=5102ccf5ce14260b2dfe128b8879c940" alt="" width="576" height="334" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/vis-id.png" />

After you have identified the `visualizationID` of a visual, you can use it in other steps such as calling REST API methods.

<h2 id="identify-a-visual-s-sourceid">
  Identify a Visual's `sourceID`
</h2>

You can identify a Self-Service Analytics visual's `sourceID` while working with it. For example, to programmatically identify a visual's default settings using a REST API call, it is easiest to use the `sourceID` in the call to look at its source configuration.

**To identify the `sourceID` of a visual's source:**

1. Open the visual in its dashboard.

2. Find the number at the end of the URL in the address bar of your browser. The `sourceID` is the section of the number before the plus sign (+).

   <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/source-id.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=2f257453871bb9d12f7ce125c2c257ee" alt="" width="576" height="334" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/source-id.png" />

After you have identified the `sourceID` of a visual, you can use it in other steps such as calling REST API methods.

<h2 id="query-configuration-object">
  Query Configuration Object
</h2>

The query configuration is contained in a JSON object including specific key:value pairs. You do not need to include unused keys. The exceptions are:

* the `time` key, which must specify a `timeField` value if a `player` is to be used by the query
* you must use one and only one of the following keys: `fields`, `groups`, and `dimensions`. Using none or more than one of these keys results in an error.

Additionally, if you use the query configuration object to create a query that is then used to supply data to an embedded visual, it must have the following keys:

* `filters`, though it can be defined as `[]` if you do not want to apply any filter
* `metrics`, without which the visual will not have data to present

<h3 id="query-configuration-object-example">
  Example
</h3>

```javascript theme={null}
var yourConfigObject = { // time zone tz: 'UTC', // field used for time // start and finish times/dates // format: {+/-}YYYY-MM-DD HH:mm:ss.SSS // + means inclusive, - means exclusive time: { timeField: '_ts', from: '+2016-10-23 22:30:15.500', to: '-2016-11-23 22:30:15.500' }, // rate of querying, in seconds // timeWindowScale: 'ROLLING' means that start time advances with end time // timeWindowScale: 'PINNED' means that start time does not advance with end time player: { speed: 1, pauseAfterRead: false, timeWindowScale: 'ROLLING' }, filters: [ { path: 'usersentiment', operation: 'BETWEEN', value: [-0.5, 0.5] }, { path: 'color', operation: 'IN', value: [‘red’, 'green', 'blue'] }, { path: 'age', operation: 'LT', value: 21 }, { path: 'color', operation: 'NOTIN', value: ['red', 'green', 'blue'] } ], // count does not take a metric function. Other metrics require one. // func can be 'sum', 'avg', 'min', 'max', 'count', 'countd' metrics: [ { name: 'price', func: 'avg' }, { name: 'count' } ], // metricFunc is used to sort by metric values. It is required if you sort by a metric other than count. It accepts the same options as metric's func key. groups: [ { name: 'usercity', limit: 200, sort: { dir: 'asc', name: 'usercity' } }, { name: 'department', limit: 10, sort: { dir: 'asc', name: 'count' } }, { name: 'color', limit: 5, sort: { dir: 'asc', name: 'usersentiment', metricFunc: 'avg' } } ], // Your query must have groups or fields, but may not have both groups and fields. fields: [ { name: 'price', limit: 50 }, { name: 'usercity', limit: 50 } ], };
```

Each possible parameter is described below.

<h3 id="tz">
  `tz: ''`
</h3>

Sets the timezone used by the web app. Use ISO standard abbreviations. The value defaults to the Self-Service Analytics server time.

<h3 id="time">
  `time: {}`
</h3>

A time object, which specifies the time range to be included in the query. Essentially, this parameter filters the query based on time using the time field, from, and to elements.

<table>
  <thead>
    <tr>
      <th scope="col">Key</th>
      <th scope="col">Usage</th>
      <th scope="col">Notes</th>
      <th scope="col">Examples</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`timeField`</td>

      <td>
        String.

        <br />

        Sets the field to be used as the time measurement.
      </td>

      <td>This field refers to the data source columns containing the time measurement, rather than any label that appears in the user interface.</td>

      <td />
    </tr>

    <tr>
      <td>`from`</td>

      <td>
        String.

        <br />

        Sets the earliest time from which data should be included in the query.
      </td>

      <td>Use the format `[-/+]YYYY-MM-DD HH:mm:ss.SSS` (preceded by a + or - to include or exclude the specified time).</td>
      <td>`+2024-10-23 10:30:15.500` to start at 23 October 2024 10:30:15.5, inclusive</td>
    </tr>

    <tr>
      <td>`to`</td>

      <td>
        String.

        <br />

        Sets the latest time to which data should be included in the query.
      </td>

      <td>Use the format `[-/+]YYYY-MM-DD HH:mm:ss.SSS` (preceded by a + or - to include or exclude the specified time).</td>
      <td>`-2025-01-10 10:30:15.500` to start at 10 January 2025 10:30:15.5, exclusive.</td>
    </tr>
  </tbody>
</table>

<h3 id="player">
  `player: {}`
</h3>

A player object, which specifies parameters for retrieving data from a source. It consists of the speed, pauseAfterRead, and timeWindowScale elements. If you include a player object in the query, you must also include a time object that includes at least the timeField element.

<table>
  <thead>
    <tr>
      <th scope="col">Key</th>
      <th scope="col">Usage</th>
      <th scope="col">Notes</th>
      <th scope="col">Examples</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`speed`</td>

      <td>
        Integer.

        <br />

        Sets the interval at which data should be retrieved, in seconds.
      </td>

      <td>Accepted values are: 1 (every second), 60 (every minute), 3600 (every hour), and 86400 (daily).</td>
      <td>60</td>
    </tr>

    <tr>
      <td>`pauseAfterRead`</td>

      <td>
        Boolean.

        <br />

        Sets whether the data stream, if applicable, should be paused after initial retrieval.
      </td>

      <td>`data set empty` message may result when `pauseAfterRead` is set to false with a non-live data source.</td>
      <td>true</td>
    </tr>

    <tr>
      <td>`timeWindowScale`</td>

      <td>
        String.

        <br />

        `'ROLLING'` or `'PINNED'`. Sets whether the time interval of retrieved data “rolls” or stays “pinned” to its original starting point (the from element of the time object).
      </td>

      <td>
        The retrieval of a rolling time window starts at the point where the last retrieval finished. The retrieval of a pinned time window always starts at the same point, which is provided by the from element.

        <br />

        The image below shows rolling time windows above the timeline, and pinned windows beneath it.<img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/api/time-window-scale.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=b03cbbd66c34befa192cea313dc39120" alt="" width="211" height="84" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/api/time-window-scale.png" />
      </td>

      <td>
        `'ROLLING'`

        <br />

        `'PINNED'`
      </td>
    </tr>
  </tbody>
</table>

<h3 id="filters">
  `filters: [{},{}]`
</h3>

Array of filter objects. Filter objects are applied to the data query using logical-and operations so that data is passed from the data query only if it satisfies all applied filters. Each filter consists of a path, an operation, and a value.

<table>
  <thead>
    <tr>
      <th scope="col">Key</th>
      <th scope="col">Usage</th>
      <th scope="col">Notes</th>
      <th scope="col">Examples</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`path`</td>

      <td>
        String.

        <br />

        The name of the group or metric on which the filter operates.
      </td>

      <td>This name is that of the data source column containing the group or metric of the filter, rather than the label that appears in the user interface.</td>

      <td>
        `customer_gender`

        <br />

        `customer_age`

        <br />

        `user_occupation`
      </td>
    </tr>

    <tr>
      <td>`operation`</td>

      <td>
        String.

        <br />

        The logical operator used by the filter.
      </td>

      <td>
        Valid options include the following:

        <br />

        <table>
          <tbody>
            <tr>
              <td>logical operation</td>
              <td>key value</td>
            </tr>

            <tr>
              <td>\<</td>
              <td>'LT'</td>
            </tr>

            <tr>
              <td>\<=</td>
              <td>'LE'</td>
            </tr>

            <tr>
              <td>==</td>
              <td>'EQUALS' (case sensitive)</td>
            </tr>

            <tr>
              <td>==</td>
              <td>'EQUALSI' (case insensitive)</td>
            </tr>

            <tr>
              <td>>=</td>
              <td>'GE'</td>
            </tr>

            <tr>
              <td>></td>
              <td>'GT'</td>
            </tr>

            <tr>
              <td>in a set</td>
              <td>'IN'</td>
            </tr>

            <tr>
              <td>not in a set</td>
              <td>'NOTIN'</td>
            </tr>

            <tr>
              <td>between two values</td>
              <td>'BETWEEN'</td>
            </tr>

            <tr>
              <td>!=</td>
              <td>'NOTEQUALS'</td>
            </tr>

            <tr>
              <td>text search</td>
              <td>'TEXT\_SEARCH'</td>
            </tr>

            <tr>
              <td>filter-level AND</td>
              <td>'AND'</td>
            </tr>

            <tr>
              <td>filter-level OR</td>
              <td>'OR'</td>
            </tr>
          </tbody>
        </table>
      </td>

      <td>
        `'EQUALSI'`

        <br />

        `'BETWEEN'`

        <br />

        `'NOTIN'`
      </td>
    </tr>

    <tr>
      <td>`value`</td>

      <td>
        Single value or array of values.

        <br />

        The value(s) considered by the logical operation.
      </td>

      <td>
        If two or more values are needed, such as for a logical set or for a ‘BETWEEN’ operation, they should be provided in an array.

        <br />

        Single values, such as required for an ‘EQUALS’ or ‘LT’ operation, should be provided as simple values.
      </td>

      <td>
        `'female' [21,65]`

        <br />

        `['teacher','lawyer', 'plumber']`
      </td>
    </tr>
  </tbody>
</table>

<h3 id="groups">
  `groups: [{},{}]`
</h3>

Array of group objects. Group objects specify which data is returned by a query and how it is grouped. Each group object has a name, limit, and a sort object.

<Note>
  If `groups` is defined, `fields` and `dimensions` must be omitted.
</Note>

<table>
  <thead>
    <tr>
      <th scope="col">Key</th>
      <th scope="col">Usage</th>
      <th scope="col">Notes</th>
      <th scope="col">Examples</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`name`</td>

      <td>
        String.

        <br />

        The name of the attribute to be used for grouping data.
      </td>

      <td>This name is the name of the data source column containing the attribute, rather than the label that appears in the user interface.</td>
      <td>`'home_state'`</td>
    </tr>

    <tr>
      <td>`limit`</td>
      <td>The maximum number of distinct items to be included in the data set.</td>

      <td>
        If the limit is set lower than the total number of items in a group, not all members of the group will be included in the returned data set.

        <br />

        For example, if the limit is set to 25, then the group us\_state could not return data from all fifty US states.
      </td>

      <td>50</td>
    </tr>

    <tr>
      <td>`sort`</td>
      <td>A sort object. See below.</td>

      <td />

      <td>`{dir: 'desc', name: 'home_state'}`</td>
    </tr>
  </tbody>
</table>

<h3 id="sort">
  `sort: {}`
</h3>

A sort object. Sort objects describe the way in which a group is ordered. Each sort object consists of the name of the group or metric for the sorting and the direction in which the group’s data is sorted.

<table>
  <thead>
    <tr>
      <th scope="col">Key</th>
      <th scope="col">Usage</th>
      <th scope="col">Notes</th>
      <th scope="col">Examples</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`name`</td>

      <td>
        String.

        <br />

        The name of the group or metric on which the filter operates.
      </td>

      <td>This name is that of the data source column containing the group or metric by which groups are to be sorted, rather than the label that appears in the user interface.</td>
      <td>`'home_state'`</td>
    </tr>

    <tr>
      <td>`dir`</td>

      <td>
        String.

        <br />

        The direction of the sorting.
      </td>

      <td>Valid options are `'asc'` and `'desc'` for ascending and descending sorts, respectively.</td>
      <td>`'asc'`</td>
    </tr>

    <tr>
      <td>`metricFunc`</td>

      <td>
        String.

        <br />

        Required to sort by a metric value. Not permitted if you sort by count or by a group.
      </td>

      <td>Valid options include the following:`'min'`, `'max'`, `'avg'`, `'sum'`, `'calc'`, `'distinct_count'`, `'last_value'`, `'percentiles'`</td>
      <td>`'sum'`</td>
    </tr>
  </tbody>
</table>

Array of group objects. Group objects specify which data is returned by a query and how it is grouped. Each group object has a name, limit, and a sort object.

<h3 id="fields">
  `fields: [{},{}]`
</h3>

Array of field objects. A field object is used to take a whole column of data without grouping it by the items found in the column. Each field object consists of the name of a column.

<Note>
  If `fields` is defined, `groups` and `dimensions` must be omitted.
</Note>

| Key | Usage | Notes | Examples |
| - | - | - | - |
| `name` | String. | This name is that of the data source column containing the field. | `'home_state'` |
| limit | Integer. | The maximum number of records to report. | 50 |

<h3 id="metrics">
  `metrics: [{},{}]`
</h3>

Array of metric objects. Each metric object indicates a column to be returned and used by the data query as a metric. Each metric object can have a name and function.

<table>
  <thead>
    <tr>
      <th scope="col">Key</th>
      <th scope="col">Usage</th>
      <th scope="col">Notes</th>
      <th scope="col">Examples</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`name`</td>

      <td>
        String.

        <br />

        The name of the metric.
      </td>

      <td>This name is that of the data source column containing the metric, rather than the label that appears in the user interface.</td>
      <td>`'user_age'`</td>
    </tr>

    <tr>
      <td>`function`</td>

      <td>
        String.

        <br />

        Determines the function applied to the metric.
      </td>

      <td>Valid options include the following:`'min'`, `'max'`, `'avg'`, `'sum'`, `'calc'`, `'distinct_count'`, `'last_value'`, `'percentiles'`</td>
      <td>`'avg'`</td>
    </tr>
  </tbody>
</table>

<h2 id="application-configuration-object">
  Application Configuration Object
</h2>

The application configuration object contains the parameters that your client needs to identify a Self-Service Analytics server.

<h3 id="application-configuration-object-example">
  Example
</h3>

```javascript theme={null}
var applicationConfig = {
secure: true,
host: 'www.yourcompanysite.com',
port: 8443,
path: '/zoomdata'
};
```

The values for each key should be as follows:

* **secure**: true to use HTTPS (secure) protocol, otherwise `false`
* **host**: the base URL where your Self-Service Analytics server is hosted
* **port**: the port that your Self-Service Analytics uses to communicate; by default, this is `8443`
* **path**: the path from your base URL for your Self-Service Analytics server; by default, this is `‘/zoomdata’`

<h2 id="security-configuration-object">
  Security Configuration Object
</h2>

The security configuration object contains the required access token you generate for your client to access Self-Service Analytics.

<Note>
  insightsoftware recommends using [Trusted Access](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/trusted-access-ov) for all embed-related workflows.
</Note>

<h3 id="security-configuration-object-example">
  Example
</h3>

```javascript theme={null}
var credentialsConfig = {
access_token: TRUSTED_ACCESS_TOKEN,
};
```

The security configuration object should contain the required trusted access token you generate.

* **access\_token**: Trusted access token for accessing the Self-Service Analytics server. See [Generate a User's Access Token](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/trusted-access-ov#generate-a-user-s-access-token). The client created should have credentials matching those used to create the trusted access token.

<h2 id="events-created-by-client">
  Events Created by Client
</h2>

### Thread Events

| Event | Description |
| - | - |
| thread:start | Thread is starting. |
| thread:stop | Thread is stopping. |
| thread:pause | Thread is pausing. Relevant only for time bar visuals. |
| thread:unpause | Thread is resuming. Relevant only for time bar visuals. |
| thread:updateSpeed | Thread's speed is updating. Relevant only for time bar visuals. |
| thread:message | Thread is sending data, which is returned as a packet by the listener to a callback function. |
| thread:error | An error occurred on the thread. The error message is included in the event, which is returned as a packet by the listener to a callback function. |
| thread:startVisDone | Thread has finished starting the visual. |
| thread:stopVisDone | Thread has finished stopping the visual. |
| thread:noData | Thread has found no data. |
| thread:dirtyData | Data is currently being read. Not fully sharpened yet. |
| thread:notDirtyData | All the data has been read and is fully sharpened. |
| thread:pauseDone | Thread has finished pausing. For time bar sources. |
| thread:unpauseDone | Thread has finished resuming. For time bar sources. |
| thread:pagination | Pagination for most visuals. |
| thread:pivotPaging | Separate paging event for Pivot Table visual. |
| thread:viewport | Viewport has updated. |
| thread:timeline | Reports time window currently being queried. |

### Visualization Events

| Event | Description |
| - | - |
| showReflinePopup | Show Reference Line pop-up. |
| interaction | Interaction with the visual. Includes event details. |
| actionList:open | Action list opened. |
| actionList:close | Action list closed. |
| tooltip:show | Display tooltip. |
| tooltip:update | Updating tooltip. |
| tooltip:move | Moving tooltip. |
| tooltip:hide | Hide tooltip. |
| filters:add | Add a filter. |
| filters:remove | Remove a filter. |
| showWarning | Show a warning. |
| releaseInteractiveElement | Released an interactive element you no longer want to be interactive. |
| registerInteractiveElement | Registered a new interactive element. |
| requestData | Requesting data. |
| axisLabels:create | Create axis labels for your visual. |
| axisLabel:create | Create an axis label for your visual. |
| axisLabels:remove | Remove all axis labels from visual. |
| stop | Visual is stopping. |
| request:pickAttribute | Visual has requested attribute picker. |
| request:pickMetric | Visual has requested metric picker. |
| request:registered | Visual queries whether some element is interactive. |
| request:getTicksStep | Visual is requesting the tick step. |

<h2 id="self-service-analytics-visual-metrics-and-attributes-reference">
  Self-Service Analytics Visual Metrics and Attributes Reference
</h2>

Different visual types support different numbers of metrics and attributes and have different metric identifiers. The table below lists these for each visual type available.

<table>
  <thead>
    <tr>
      <th scope="col">Icon</th>
      <th scope="col">Visual Type</th>
      <th scope="col">Number of Metrics</th>
      <th scope="col">Metric Identifiers</th>
      <th scope="col">Number of Attributes</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-arc.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=5fb167d5432d15fc53f6beb814351a13" alt="" width="29" height="21" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '29px', height: '21px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-arc.png" />
      </td>

      <td>[Single Metric Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/arc)</td>
      <td>at least 1</td>
      <td>Arc color</td>
      <td>none</td>
    </tr>

    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-bar.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=7ff00bc843f09a7298fb52df35c8ee0e" alt="" width="29" height="28" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '29px', height: '28px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-bar.png" />
      </td>

      <td>[Bar, Line, and Combo Charts](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/bar-standard)</td>
      <td>at least 1</td>
      <td>Bar height, bar color, segment size, color</td>
      <td>at least 1</td>
    </tr>

    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-bar-histogram.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=64a65fde56bbc5e826d8f701b26a8b0c" alt="" width="29" height="27" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '29px', height: '27px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-bar-histogram.png" />
      </td>

      <td>[Bars: Histograms](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/bar-standard#bars-histograms)</td>
      <td>1</td>
      <td>Bar height, bar color</td>
      <td>1</td>
    </tr>

    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-bar-mult.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=ba7e927b539727d2b7716dd3f4249a7a" alt="" width="29" height="27" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '29px', height: '27px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-bar-mult.png" />
      </td>

      <td>[Bars: Multiple Metric Charts](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/bar-standard#bars-multiple-metric-charts)</td>
      <td>Multiple</td>
      <td>Bar height, bar color</td>
      <td>1</td>
    </tr>

    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-boxplot.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=66b59710cfb8f5fccae147e571353a2e" alt="" width="29" height="28" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '29px', height: '28px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-boxplot.png" />
      </td>

      <td>[Box Plots](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/scatter-plot#box-plots)</td>
      <td>2</td>
      <td>Position and size</td>
      <td>1</td>
    </tr>

    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-bullet.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=5523bcef5a0d4ba1e2f0dd1fd6ebe231" alt="" width="26" height="27" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '26px', height: '27px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-bullet.png" />
      </td>

      <td>[Bullet Gauges](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/arc#bullet-gauges)</td>
      <td>1</td>
      <td>Bar length</td>
      <td>1</td>
    </tr>

    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-combo.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=917bb589158111e003ad332c7ab30475" alt="" width="33" height="32" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '33px', height: '32px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-combo.png" />
      </td>

      <td>[Combo Charts](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/bar-standard#combo-charts)</td>
      <td>2-4; at least 2</td>
      <td>Bar or line color; additional y-axes on right</td>
      <td>1</td>
    </tr>

    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-donut.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=ecccfe7c8f4692c4db9970ae717dbe66" alt="" width="29" height="26" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '29px', height: '26px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-donut.png" />
      </td>

      <td>[Donut Charts](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/pie#donut-charts)</td>
      <td>1</td>
      <td>Segment size, color</td>
      <td>1</td>
    </tr>

    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-float.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=e1cde123ca06acd6c5cd6dc51e506066" alt="" width="29" height="25" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '29px', height: '25px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-float.png" />
      </td>

      <td>[Floating Bubble Charts](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/scatter-plot#floating-bubble-charts)</td>
      <td>2</td>
      <td>Position and size</td>
      <td>2</td>
    </tr>

    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-heatmap.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=f9c07fa5e73f7b8a6a0a449f35b63f73" alt="" width="29" height="25" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '29px', height: '25px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-heatmap.png" />
      </td>

      <td>[Heat Maps](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/scatter-plot#heat-maps)</td>
      <td>1</td>
      <td>Segment color</td>
      <td>2</td>
    </tr>

    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-kpi.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=f85f9ea2b00e984248618c3c04f8f810" alt="" width="29" height="22" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '29px', height: '22px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-kpi.png" />
      </td>

      <td>[KPI Charts](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/arc#kpi-charts)</td>
      <td>1</td>
      <td>Segment color</td>

      <td />
    </tr>

    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-line-bar.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=b84399c703ef9ea12449b8953ebc5ea6" alt="" width="29" height="28" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '29px', height: '28px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-line-bar.png" />
      </td>

      <td>[Edit Line & Bar Trend Charts](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/bar-standard#edit-line-bar-trend-charts)</td>
      <td>2</td>
      <td>Bar color</td>
      <td>time</td>
    </tr>

    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-line-attr.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=f848c3564e54ef8b4d984a922a304ec4" alt="" width="29" height="28" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '29px', height: '28px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-line-attr.png" />
      </td>

      <td>[Line Trend: Attribute Value Charts](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/bar-standard#line-trend-attribute-value-charts)</td>
      <td>1</td>
      <td>Point location</td>
      <td>2 and time field</td>
    </tr>

    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-line-mult.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=b9cb009cc2a593e8dbb5636d8ef907d9" alt="" width="29" height="27" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '29px', height: '27px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-line-mult.png" />
      </td>

      <td>[Line Trend: Multiple Metric Charts](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/bar-standard#line-trend-multiple-metric-charts)</td>
      <td>Multiple</td>
      <td>Point location</td>
      <td>1</td>
    </tr>

    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-list-filter.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=b90a066c7c0603da2793022c67a3ea1b" alt="" width="29" height="30" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '29px', height: '30px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-list-filter.png" />
      </td>

      <td>[List Filter Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/list-filter-widget)</td>
      <td colSpan={3}>Only one field can be selected for a list filter visual.</td>
    </tr>

    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-map-marker.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1b91fcca6b8410167268c3b79d210d8b" alt="" width="29" height="40" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '29px', height: '40px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-map-marker.png" />
      </td>

      <td>[Marker Maps](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/map-chart-styles#marker-maps)</td>
      <td>2</td>
      <td>Color</td>
      <td>1</td>
    </tr>

    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-map-us.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=e7f9d49f21ddccbf446dce43ed4d1b68" alt="" width="29" height="19" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '29px', height: '19px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-map-us.png" />
      </td>

      <td>[US Region Maps](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/map-chart-styles#us-region-maps)</td>
      <td>3</td>
      <td>Color</td>
      <td>1</td>
    </tr>

    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-map-world.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=79f662a5a401459caa933829373b630a" alt="" width="29" height="30" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '29px', height: '30px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-map-world.png" />
      </td>

      <td>[World Maps](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/map-chart-styles#world-maps)</td>
      <td>1</td>
      <td>Color</td>
      <td>1</td>
    </tr>

    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-packed.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=cf2240536f093753b799e8d0832b2d09" alt="" width="29" height="28" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '29px', height: '28px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-packed.png" />
      </td>

      <td>[Packed Bubble Charts](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/pie#packed-bubble-charts)</td>
      <td>2</td>
      <td>Bubble size, bubble color</td>
      <td>1</td>
    </tr>

    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-pie.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=c8e8b60a16b8d0f2fe7154c85ffdc670" alt="" width="29" height="30" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '29px', height: '30px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-pie.png" />
      </td>

      <td>[Circular, Tree, and Cloud Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/pie)</td>
      <td>1</td>
      <td>Segment size, color</td>
      <td>1</td>
    </tr>

    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-pivot.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=d5e2e34e684385c6b797beeb24b3c20d" alt="" width="29" height="27" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '29px', height: '27px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-pivot.png" />
      </td>

      <td>[Pivot Tables](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/pivot-tables)</td>
      <td>Multiple</td>

      <td />

      <td>Multiple</td>
    </tr>

    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-rdt.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=2d1657e403677d37b82a9a132d4e360d" alt="" width="38" height="36" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '38px', height: '36px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-rdt.png" />
      </td>

      <td>[Tables](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/rdt)</td>
      <td>Multiple</td>

      <td />

      <td>Multiple</td>
    </tr>

    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-scatter.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=31f74e69f8c1e835f1c3f93a6bd3487a" alt="" width="41" height="34" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '41px', height: '34px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-scatter.png" />
      </td>

      <td>[Comparison and Relationship Charts](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/scatter-plot)</td>
      <td>3</td>
      <td>Position and size</td>
      <td>1</td>
    </tr>

    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-sun.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=3480e1d078195e4245f8c5d730d97cc9" alt="sunburst visual icon" width="37" height="32" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '37px', height: '32px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-sun.png" />
      </td>

      <td>[Sunburst](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/pie#sunburst)</td>
      <td>3-4</td>
      <td>Segment size, color</td>
      <td>1</td>
    </tr>

    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-treemap.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=adbd00e5fe0f65a09ae841e16074ef90" alt="" width="29" height="28" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '29px', height: '28px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-treemap.png" />
      </td>

      <td>[Tree Maps](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/pie#tree-maps)</td>
      <td>2</td>
      <td>Segment size, color</td>
      <td>1</td>
    </tr>

    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-waterfall.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=65896b1ec068708fe5a9c9201ac53a5d" alt="" width="29" height="28" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '29px', height: '28px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-waterfall.png" />
      </td>

      <td>[Waterfall](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/bar-standard#waterfall)</td>
      <td>2 or more</td>
      <td>Size, Color</td>
      <td>at least 1</td>
    </tr>

    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-wordcloud.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=88067ef7fd12dbf013359e1dad620c5f" alt="" width="29" height="27" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '29px', height: '27px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/cht-wordcloud.png" />
      </td>

      <td>[Word Clouds](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/pie#word-clouds)</td>
      <td>2</td>
      <td>Font size, color</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
