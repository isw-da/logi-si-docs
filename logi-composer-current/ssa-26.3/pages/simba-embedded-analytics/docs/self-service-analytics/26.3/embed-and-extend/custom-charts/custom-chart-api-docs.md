> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Custom Chart API

## Getting Started

The custom chart API provides developers with an interface to create interactive charts that integrate with the native Self-Service Analytics chart controls. To get started with the custom chart API, you need to install the [Custom Chart CLI](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/custom-charts/custom-chart-maint-cli#install-and-configure-the-custom-chart-cli). The tool is designed to help you manage all aspects of the custom chart creation process in Self-Service Analytics.

<Note>
  You must be an administrator to configure the chart CLI.
</Note>

For more detailed step-by-step instructions on getting started, see [A Custom Chart Tutorial](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/custom-charts/custom-chart-tut-ov).

<h2 id="install-self-service-analytics-s-custom-chart-cli">
  Install Self-Service Analytics’s Custom Chart CLI
</h2>

`npm install composer-chart-cli@latest -g`

<h2 id="use-the-self-service-analytics-custom-chart-cli">
  Use the Self-Service Analytics Custom Chart CLI
</h2>

1. Configure the CLI. `cmp-chart config`
2. Create a new custom chart. `cmp-chart init <some_path>/<your_chart_name>`
3. From the newly created custom chart directory, run `npm install` — This will install your custom chart's development dependencies.
4. Compile the custom chart code that will be pushed to the server `—npm run build`
5. Push the custom chart to the server — `cmp-chart push`
6. Enable the custom chart for a source. Navigate to the [Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#data-sources-page) page, locate a data source configuration to edit, and select the more menu (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" />) button. Select **Available Visual Types**, then locate and enable your chart in the Custom Visual Types list.
7. Create a new dashboard with your custom chart. You should see a chart widget with a Group and Metric picker.
8. You are now ready to continue building out your custom chart.

## Add Custom Chart Packages

Run `cmp-chart import <name> <filepath.zip>` to add the specified custom chart to the Self-Service Analytics server.

For more information about working with custom charts, see these topics:

* [Chart Variables](#chart-variables)
* [Controller](#controller)
* [Create Your Own Chart Container](#create-your-own-chart-container)
* [Receive Chart Data](#receive-chart-data)
* [Transform Data Using Data Accessors](#transform-data-using-data-accessors)
* [Get Values From Constant Variables](#get-values-from-constant-variables)
* [React to Resize Events](#react-to-resize-events)
* [Update Queries with Axis Labels or Pickers](#update-queries-with-axis-labels-or-pickers)
* [Add Tooltips](#add-tooltips)
* [Interacting with the Context Menu](#interacting-with-the-context-menu)
* [Listening to Other Query Events](#listening-to-other-query-events)

<h2 id="controller">
  Controller
</h2>

The global object controller exposes the Self-Service Analytics custom chart API. The controller object contains several properties holding information about the chart. These include, but are not limited to:

* HTML Element to be used as a chart container (`controller.element`)
* Object with properties containing the configuration of each query variable (`controller.dataAccessors`)
* Object with the information about the current Self-Service Analytics data source (`controller.source`)
* Object with properties to access the value of each constant variable (`controller.variables`)

Handler functions can override several methods of the `controller` object to react to chart events like data updates, chart resizing, and query errors. Triggering these events execute the specified handler function.

For more information about the `controller` properties and methods, visit the individual guides for tips on how to use custom chart API.

<h2 id="chart-variables">
  Chart Variables
</h2>

Chart variables serve as configuration parameters that can be read from the chart’s code and are used to promote reusability of charts across Self-Service Analytics data sources. There are two types of chart variables in Self-Service Analytics:

* [Query Variables](#query-variables)
* [Constant Variables](#constant-variables)

<h3 id="query-variables">
  Query Variables
</h3>

These variables drive the type of query that executes against the backend database. For example, a chart with a single query variable of type **Group** aggregates the data based on the configured field and uses **count** as the aggregation function. If the developer additionally adds a query variable of type **Multi-Metric**, the data includes the aggregated values of the configured metrics based on the aggregation functions specified.

<h3 id="constant-variables">
  Constant Variables
</h3>

These variables are useful for chart settings specified as numeric, text, or list values. For example, a custom chart might use a service that requires an API key. A chart developer can create a **string** constant variable for the API key to allow users to specify a different key per data source.

### Supported Variable Types

A list of the various variable types supported by Self-Service Analytics custom charts and their configurations can be found [here](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/custom-charts/custom-chart-config).

<h2 id="add-tooltips">
  Add Tooltips
</h2>

Charting libraries often include a tooltip implementation that may not look similar to the tooltips included with Self-Service Analytics native charts. As a developer, you can re-use the tooltip design in your custom charts by leveraging the `show` and `hide` methods in `controller.tooltip`.

To show a tooltip, use `controller.tooltip.show`. The `show` method takes an object as its only argument with the following properties:

| Option | Description |
| - | - |
| `x` | The x coordinate on the screen where the tooltip should render. |
| `y` | The y coordinate on the screen where the tooltip should render. |
| `data` | Function that returns a Self-Service Analytics data element. |

Optional properties:

| Option | Description |
| - | - |
| `event` | Takes a native browser event to specify the tooltip position. Use as an alternative to x and y properties. |
| `content` | Function that returns an HTML string to replace the content inside of the tooltip boxes. This can be used to render custom tooltips. |

Example:

```javascript theme={null}
myChart.on('mouseover', function(param) {
  controller.tooltip.show({
    x: param.x,
    y: param.y,
    data: function() {
      return param.composerDataElement;
    },
  });
});
```

In the above example, we have a reference to chart instance stored in the `myChart` variable. It hooks into the `mouseover`event of the chart and provides a handler function. The chart provides the handler function with an object argument `param` with the x and y screen coordinates that describe where the tooltip should display.

In this example, the chart has also provided the original Self-Service Analytics data element for the hovered point. `controller.tooltip.show` can be called with an object that specifies the tooltip location and data for the tooltip.

To hide the tooltip, we can call the `controller.tooltip.hide` method.

Example:

```javascript theme={null}
myChart.on('mouseout', function() {
  controller.tooltip.hide();
})
```

Here you hook into the `mouseout` event and provide a handler function that calls the `controller.toolitp.hide` method.

<h2 id="create-your-own-chart-container">
  Create Your Own Chart Container
</h2>

Self-Service Analytics provides a reference to an HTML DIV element that developers can use as a container for their charts. This element is accessed via the `controller.element` property. Sometimes, it is useful to create an inner chart container inside the `controller.element` div to gain full control over its styling via the CSS chart components.

Example:

```javascript theme={null}
// In visualization.js

var chartContainer = document.createElement('div');
chartContainer.style.width = '100%';
chartContainer.style.height = '100%';
chartContainer.classList.add('chart-container');
controller.element.appendChild(chartContainer);
```

To add a border around the chart container:

```
/* In GENERIC-TABLESTYLE.css */

div.chart-container {
  border: 1px solid black;
}
```

Now you can use the div with the class `chart-container` to render your chart.

<h2 id="get-values-from-constant-variables">
  Get Values From Constant Variables
</h2>

The values of constant variables are accessed by reading the properties of `controller.variables`. This object contains a property for each constant variable defined.

Example:

```javascript theme={null}
var apiKey = controller.variables['API Key'];

// use the apiKey in your code
```

In the above example, the chart has a constant variable of type “string” defined with the name “API Key”. We access the value by reading the property “API Key” from `controller.variables`.

<h2 id="interacting-with-the-context-menu">
  Interacting with the Context Menu
</h2>

The Self-Service Analytics context menu is a native control that you can add to custom charts to provide users with a set of standard chart interactions. Your chart must be running an aggregated data query to leverage and provide access to the context menu.

Default context menu actions:

| Action | Description |
| - | - |
| Details | Open a panel with a Raw Data table chart displaying the full set of records matching the selected data point. |
| Filter | Open a panel to select other charts in the dashboard to filter with a condition matching the selected data point. |
| Keyset | Open a panel to create a keyset from a data point. |
| Trend | Switches the current chart to the included **Line Chart: Multiple Metrics** chart and adds the selected data point as a filter. |
| Drill Down (formerly Zoom) | Open a panel to select a new attribute to drill into. The selection automatically changes the group-by field in the query and adds a filter condition matching the selected data point. |
| Remove | Removes the selected data point by adding a filter to the query to exclude it. |
| Settings | Opens the visual sidebar menu. |

Optional context menu options:

| Action | Description |
| - | - |
| Actions | Invoke an action for the visual. Only visible if an action template is defined and enabled for the data source. |
| Link | Access a dashboard that has been linked to the visual. Only visible if a dashboard link exists. |
| Create Alert | Open the create alert work area. |

### Create a Context Menu with Custom Actions

Add custom actions to your context menu, and bind methods to left and right mouse click actions in place of default actions.

```javascript theme={null}
			menuEventsConfig: {
			click: 'filter',
			contextmenu: 'openMenu',
			customActions: [{
			name: 'google help',
			action: (data) => window.open (''https://www.google.com/', '_blank').focus(),
			},
		}]
```

Define your base configuration object. This is optional; if you do not define a base configuration object, Self-Service Analytics deploys the default context menu behavior.

Optionally, include a `customActions` items array. Your `customActions` can be bound as a method for the left or right mouse click in place of one of the [default actions](#interacting-with-the-context-menu).

Defining `customActions`:

<table>
  <thead>
    <tr>
      <th>Option</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`name`</td>

      <td>
        A name for each of the `customActions`.

        <br />

        Required.
      </td>
    </tr>

    <tr>
      <td>`action`</td>

      <td>
        The action you define for the `customActions`.

        <br />

        Required.
      </td>
    </tr>

    <tr>
      <td>`icon`</td>

      <td>
        An icon to associate with the `customActions`.

        <br />

        Optional.
      </td>
    </tr>
  </tbody>
</table>

<h2 id="listening-to-other-query-events">
  Listening to Other Query Events
</h2>

Chart developers may need to apply particular logic to their charts whenever a query event is triggered. Handler functions can be defined to override the following list of query methods:

* `controller.onStart`: Called as soon as the query execution begins.
* `controller.onNoDataFound`: Called when no data is available for the given query.
* `controller.onNotDirtyData`: Called as soon as all of the data is received.
* `controller.onStreamError`: Called when the query execution returns an error from the server.

<h2 id="react-to-resize-events">
  React to Resize Events
</h2>

When a user resizes a chart widget, you must account for the new widget dimensions. You can specify your own resize handler function by overriding the `controller.resize` method.

Example:

```javascript theme={null}
controller.resize = function(newWidth, newHeight) {
  // If needed, use the newWidth and newHeight values to resize chart
}
```

The specified handler executes every time a user action causes the widget dimensions to change. The following list provides a few examples of actions that trigger the resize event:

* A user changes the dimensions of the browser window.
* A user changes the dimensions of an individual widget.

Hiding or displaying controls like the Time Bar may reduce or increase the space available for widgets in a dashboard.

<h2 id="receive-chart-data">
  Receive Chart Data
</h2>

To receive the results of queries executed against a Self-Service Analytics data source, chart developers can override the `controller.update` method with a function that will receive the array of data elements.

Example:

```javascript theme={null}
// In visualization.js

/* This function will get called when new data is received from the server */
controller.update = function(data) {
  // code to update the chart with new data
  // the data argument is an array of objects (data elements)
};
```

### Structure of a Data Element in Aggregated Queries

When working with aggregated queries that have `Group` or `Multi-Group` variables defined, you can expect to receive data elements with the following structure:

```json theme={null}
{
  "group": ["Books", "$0 to $25,000"],
  "current": {
    "count": 1267,
    "metrics": {
      "price": {
        "sum": 1077100
      }
    }
  }
}
```

The above JSON represents the results of a chart query generated by defining a `Multi-Group` variable and `Metric` variable. The `Multi-Group` variable contains two levels of grouping (“Product Group” & “User Income” fields), and the `Metric` variable has a configuration using the “Price” field and the “SUM” function. The count property represents the total count of records for the grouping combination. This property is always available in all aggregated queries.

<h3 id="structure-of-a-data-element-in-non-aggregated-queries">
  Structure of a Data Element in Non-Aggregated Queries
</h3>

When working with non-aggregated queries, the data elements in the array received from the server represent a row of data in the data source. Each row is made up of an array of values; one for each of the fields requested:

```
 ["Male", "Visa", "400"]
```

The above JSON represents the results of a chart query generated by defining an `Ungrouped` variable with three fields requested: “Gender”, “Payment Type”, “Price”.

<h2 id="transform-data-using-data-accessors">
  Transform Data Using Data Accessors
</h2>

When working with charting libraries, it is often necessary to structure your data elements in a way the charting libraries understand.

For instance, given the following structure of data element received from the server:

```json theme={null}
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
```

You may need to transform it to:

```json theme={null}
{
  "name": "$0 to $25,000",
  "value": "52150"}
```

We are interested in the values specified in the `group` array and the metric value defined in `price.sum`. You may be inclined to create a new data array by mapping each data element to the necessary structure like:

```javascript theme={null}
var newData = data.map(function(d) {
  return {
    name: d.group[0],
    value: d.current.metrics.price.sum,
  };
});
```

The downside of this approach is that you have now hardcoded the paths of your metric values to a specific field name (“price”) and a specific aggregation function (“sum”).

### A Better Approach Using Data Accessors

A `Data Accessor` is an object with methods that can be used to extract information about the current configuration of query variables. A data accessor can also extract data values out of the data elements received from query execution results.

Example:

```javascript theme={null}
var groupAccessor = controller.dataAccessors['Group By'];
var metricAccessor = controller.dataAccessors.Metric;

var newData = data.map(function(d) {
  return {
    name: groupAccessor.raw(d),
    value: metricAccessor.raw(d),
  };
});
```

To access a data accessor, use the `controller.dataAccessors` object. The query variable’s name exists as property in this object. The most commonly used method in data accessors is `raw` which accepts a Self-Service Analytics data element and returns a value corresponding to the query variable. In the above example, we used the `groupAccessor` and `metricAccessor` to retrieve the group and metric values without hard-coding the name of the fields.

<h2 id="update-queries-with-axis-labels-or-pickers">
  Update Queries with Axis Labels or Pickers
</h2>

Axis Labels or Axis Pickers are Self-Service Analytics native controls that can be added to charts to provide a way for users to change query parameters dynamically. Chart developers can these controls by calling the method `controller.createaAxisLabel`. The `createAxislabel` method takes an object as its only argument with the following properties:

<table>
  <thead>
    <tr>
      <th>Option</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`picks`</td>

      <td>
        Name of the query variable.

        <br />

        <Note>
          Use the data accessor’s `getName` method to avoid hardcoding variable names.
        </Note>
      </td>
    </tr>

    <tr>
      <td>`position`</td>

      <td>
        Location of the axis label in the chart widget.

        <br />

        Valid options: `bottom`, `left`, `right`, `top`
      </td>
    </tr>

    <tr>
      <td>`orientation`</td>

      <td>
        Orientation of the axis label text.

        <br />

        Valid options: `vertical`, `horizontal`
      </td>
    </tr>
  </tbody>
</table>

Example:

```yaml theme={null}
controller.createAxisLabel({
  picks: 'Group By',
  position: 'bottom',
  orientation: 'horizontal',
});

controller.createAxisLabel({
  picks: 'Size',
  position: 'bottom',
  orientation: 'horizontal',
});
```

The above example adds two axis pickers to the chart that provide users with the ability to change the fields used for the `Group By` and `Size` query variables.
