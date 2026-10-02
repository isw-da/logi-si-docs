> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Visual Type Configuration Properties

This section describes the properties of visualization type configurations, possible values, and the definition of those values for creating or editing visual types (custom charts) for Self-Service Analytics.

<Note>
  You must be an administrator to manage custom visual types.
</Note>

<h2 id="properties">
  Properties
</h2>

`name` - **string**

`name` is the name of visual type the configuration file represents, and displays in the user interface. This name must be unique in your Self-Service Analytics instance, or it will overwrite or be overwritten by a visual type using the same name.

`type` - **string**

`type` is one of the properties Self-Service Analytics uses internally to represent and distinguish visual types. Built-in visuals have unique `type` properties. Any visual you add to the system should use the same value, `CUSTOM`.

`controls` - **array of strings**

`controls` is the list of things you enable this visual type to do. Supported values are included in the chart below:

| Control | Description |
| - | - |
| UberStyle | Allows an instance of this visual type to use the Style Switcher to switch to other visual types. |
| Color | Allows an instance of this visual type to show the Color panel within the sidebar or pop-up editor. |
| Download | Allows instances of this visual type to be downloaded as an image, PDF, or configuration files. |
| Filters | Allows this visual type to be filtered using the filter editor in the sidebar or pop-up editor. |
| Publish | Enables this visualization for publication. If this control is not present, the “Filter” option is shown in a context menu. |
| Settings | Enables the settings panel in the sidebar or pop-up editor. Use the settings panel to edit the variables added to the visualization. |
| Sort | Enables the Sort & Limit panel in the sidebar or pop-up editor. This panel is used to sort and limit the data returned. Only certain variable types support sort and limit. |
| Subscribe | Allows the visual type to be the target of filters added from external sources and other visuals on the dashboard. |
| TimePlayer | Enables the Time panel in the sidebar or pop-up editor. This allows changing the field used for the time bar or turning off the time bar for each instance of the visual. |
| Undo | Allows users to undo changes they make to instances of this visualization. |

<Note>
  Additional properties may be present in a visualization’s `controls` array but they may deprecated, irrelevant to a custom visual type that does not use the properties.
</Note>

`variables` - **array of objects**

`variables` are required for the configuration. This array of objects define data and non-data values associated with instances of this visualization. All supported variable configuration are included in the list below.

* [attribute](#attribute)
* [bool](#bool)
* [box-plot-metric](#box-plot-metric)
* [color](#color)
* [float](#float)
* [group](#group)
* [histogram-group](#histogram-group)
* [integer](#integer)
* [metric](#metric)
* [multi-group](#multi-group)
* [multilist](#multilist)
* [multi-metric](#multi-metric)
* [singlelist](#singlelist)
* [string](#string)
* [text](#text)
* [ungrouped](#ungrouped)
* [ungroupedList](#ungroupedlist)

You can also maintain custom charts using the CLI. See [Maintain Custom Charts Using the Custom Chart CLI](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/custom-charts/custom-chart-maint-cli).

<h2 id="attribute">
  attribute
</h2>

The `attribute` variable is part of the array of objects you use to define data and non-data values for this visualization.

<Note>
  You must be an administrator to manage custom visual types.
</Note>

<h3 id="attribute-type">
  Type
</h3>

```
attribute
```

<h3 id="attribute-editor">
  Editor
</h3>

`attribute` variables are represented in the side panel as a button that users use to select a field. This variable’s selected field is not used as part of the data request by default, but the name is provided for other uses or for manual configuration within the visualization’s code.

<img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/customchart/custom-attribute.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=e376ed07699d241fdade6fcaf6682b2a" alt="" width="786" height="668" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/customchart/custom-attribute.png" />

<h3 id="attribute-variable-specific-properties">
  Variable Specific Properties
</h3>

| Property | Argument | Description |
| - | - | - |
| None. | | |

<h3 id="attribute-generic-properties">
  Generic Properties
</h3>

Generic properties apply to many variables.

<table>
  <colgroup>
    <col style={{width: "22%"}} />

    <col style={{width: "12%"}} />

    <col style={{width: "66%"}} />
  </colgroup>

  <thead>
    <tr>
      <th>Property</th>
      <th>Argument</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`name`</td>
      <td>string</td>
      <td>The name of the property. It must be unique among all variables on the visualization. This name is used to access the data accessor and/or variable value on the controller provided to the visualization.</td>
    </tr>

    <tr>
      <td>`descr`</td>
      <td>string</td>
      <td>A description of the variable for your reference. This is not displayed in the UI.</td>
    </tr>

    <tr>
      <td>`attributeType`</td>
      <td>array of strings</td>

      <td>
        A list of field types to include when selecting fields for this variable. Accepted values:

        <br />

        * `ATTRIBUTE`
        * `TIME`
        * `NUMBER`
        * `INTEGER`
      </td>
    </tr>

    <tr>
      <td>`required`</td>
      <td>boolean</td>
      <td>Triggers the UI to require a value for certain variable types. Not used for this variable type.</td>
    </tr>
  </tbody>
</table>

<h3 id="attribute-deprecated-properties">
  Deprecated Properties
</h3>

| Property |
| - |
| None. |

<h3 id="attribute-samples">
  Samples
</h3>

```json theme={null}
{
	"name": "State",
	"type": "attribute",
	"descr": "A field which represents a US State",
	"attributeType": [
		"ATTRIBUTE"
	],
	"required": false
}
```

See Visual Type Configuration Properties.

<h2 id="bool">
  bool
</h2>

The `bool` variable is part of the array of objects you use to define data and non-data values for this visualization.

<Note>
  You must be an administrator to manage custom visual types.
</Note>

<h3 id="bool-type">
  Type
</h3>

```
bool
```

<h3 id="bool-editor">
  Editor
</h3>

`bool` variables are represented in the side panel as a simple switch.

<img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/customchart/custom-bool.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=dcea7c6cf4c3a2aad046b706adcab685" alt="" width="334" height="39" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/customchart/custom-bool.png" />

<h3 id="bool-variable-specific-properties">
  Variable Specific Properties
</h3>

| Property | Argument | Description |
| - | - | - |
| None. | | |

<h3 id="bool-generic-properties">
  Generic Properties
</h3>

<table>
  <colgroup>
    <col style={{width: "22%"}} />

    <col style={{width: "12%"}} />

    <col style={{width: "66%"}} />
  </colgroup>

  <thead>
    <tr>
      <th>Property</th>
      <th>Argument</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`name`</td>
      <td>string</td>
      <td>The name of the property. It must be unique among all variables on the visualization. This name is used to access the data accessor and/or variable value on the controller provided to the visualization.</td>
    </tr>

    <tr>
      <td>`descr`</td>
      <td>string</td>
      <td>A description of the variable for your reference. This is not displayed in the UI.</td>
    </tr>

    <tr>
      <td>`attributeType`</td>
      <td>array of strings</td>

      <td>
        A list of field types to include when selecting fields for this variable. Accepted values:

        <br />

        * `ATTRIBUTE`
        * `TIME`
        * `NUMBER`
        * `INTEGER`
      </td>
    </tr>

    <tr>
      <td>`required`</td>
      <td>boolean</td>
      <td>Triggers the UI to require a value for certain variable types. Not used for this variable type.</td>
    </tr>
  </tbody>
</table>

<h3 id="bool-deprecated-properties">
  Deprecated Properties
</h3>

| Property |
| - |
| None. |

<h3 id="bool-samples">
  Samples
</h3>

```json theme={null}
{
	"name": "Show Metric Values",
	"type": "bool",
	"defaultValue": true,
	"colorMetric": false,
	"colorNumb": 0,
	"required": false
}
```

See Visual Type Configuration Properties.

<h2 id="box-plot-metric">
  box-plot-metric
</h2>

The `box-plot-metric` variable is part of the array of objects you use to define data and non-data values for this visualization.

<Note>
  You must be an administrator to manage custom visual types.
</Note>

<h3 id="box-plot-metric-type">
  Type
</h3>

```
box-plot-metric
```

<h3 id="box-plot-metric-editor">
  Editor
</h3>

`box-plot-metric` variables are not represented on the settings panel. Enable editing a `box-plot-metric` variable by adding an axis label for the variable using the `createAxisLabel` method on the controller.

<h3 id="box-plot-metric-variable-specific-properties">
  Variable Specific Properties
</h3>

<table>
  <colgroup>
    <col style={{width: "10%"}} />

    <col style={{width: "20%"}} />

    <col style={{width: "12%"}} />

    <col style={{width: "58%"}} />
  </colgroup>

  <thead>
    <tr>
      <th colSpan={2}>Property</th>
      <th>Argument</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>`defaultValue`</td>
      <td>object</td>
      <td>Allows you to set the default configuration for the specified field.</td>
    </tr>

    <tr>
      <td />

      <td>`func`</td>
      <td>string</td>
      <td>Set to `percentiles`. This is the only value supported.</td>
    </tr>

    <tr>
      <td />

      <td>`args`</td>
      <td>array of integers</td>

      <td>
        A list of the percentiles to calculated. Supported values:

        <br />

        * 0
        * 25
        * 50
        * 75
        * 100
      </td>
    </tr>
  </tbody>
</table>

<h3 id="box-plot-metric-generic-properties">
  Generic Properties
</h3>

Generic properties apply to many variables.

<table>
  <colgroup>
    <col style={{width: "22%"}} />

    <col style={{width: "12%"}} />

    <col style={{width: "66%"}} />
  </colgroup>

  <thead>
    <tr>
      <th>Property</th>
      <th>Argument</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`name`</td>
      <td>string</td>
      <td>The name of the property. It must be unique among all variables on the visualization. This name is used to access the data accessor and/or variable value on the controller provided to the visualization.</td>
    </tr>

    <tr>
      <td>`descr`</td>
      <td>string</td>
      <td>A description of the variable for your reference. This is not displayed in the UI.</td>
    </tr>

    <tr>
      <td>`attributeType`</td>
      <td>array of strings</td>

      <td>
        A list of field types to include when selecting fields for this variable. Accepted values:

        <br />

        * `ATTRIBUTE`
        * `TIME`
        * `NUMBER`
        * `INTEGER`
      </td>
    </tr>

    <tr>
      <td>`colorNumb`</td>
      <td>integer</td>
      <td>The number of colors to include in the color palette by default. 0 will choose the smallest palette available.</td>
    </tr>

    <tr>
      <td>`required`</td>
      <td>boolean</td>
      <td>Triggers the UI to require a value for certain variable types. Not used for this variable type.</td>
    </tr>
  </tbody>
</table>

<h3 id="box-plot-metric-deprecated-properties">
  Deprecated Properties
</h3>

| Property |
| - |
| None. |

<h3 id="box-plot-metric-samples">
  Samples
</h3>

```json theme={null}
{
	"name": "Box Plot Metric",
	"type": "box-plot-metric",
	"attributeType": [
		"INTEGER",
		"NUMBER"
	],
	"defaultValue": {
		"func": "percentiles",
		"args": [
			0,
			25,
			50,
			75,
			100
		]
	},
	"colorNumb": 0,
	"required": false
}
```

See Visual Type Configuration Properties.

<h2 id="color">
  color
</h2>

The `color`variable is part of the array of objects you use to define data and non-data values for this visualization.

<Note>
  You must be an administrator to manage custom visual types.
</Note>

<h3 id="color-type">
  Type
</h3>

```
color
```

<h3 id="color-editor">
  Editor
</h3>

Edit `color` variables using the color panel. The visual type must include the control color in order to modify these variables.

<h3 id="color-variable-specific-properties">
  Variable Specific Properties
</h3>

| Property | Argument | Description |
| - | - | - |
| `defaultValue` | string | A color in any CSS color format. The value`_inherit` uses the color from the currently selected theme. |

<h3 id="color-generic-properties">
  Generic Properties
</h3>

Generic properties apply to many variables.

<table>
  <colgroup>
    <col style={{width: "22%"}} />

    <col style={{width: "12%"}} />

    <col style={{width: "66%"}} />
  </colgroup>

  <thead>
    <tr>
      <th>Property</th>
      <th>Argument</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`name`</td>
      <td>string</td>
      <td>The name of the property. It must be unique among all variables on the visualization. This name is used to access the data accessor and/or variable value on the controller provided to the visualization.</td>
    </tr>

    <tr>
      <td>`descr`</td>
      <td>string</td>
      <td>A description of the variable for your reference. This is not displayed in the UI.</td>
    </tr>

    <tr>
      <td>`attributeType`</td>
      <td>array of strings</td>

      <td>
        A list of field types to include when selecting fields for this variable. Accepted values:

        <br />

        * `ATTRIBUTE`
        * `TIME`
        * `NUMBER`
        * `INTEGER`
      </td>
    </tr>

    <tr>
      <td>`required`</td>
      <td>boolean</td>
      <td>Triggers the UI to require a value for certain variable types. Not used for this variable type.</td>
    </tr>
  </tbody>
</table>

<h3 id="color-deprecated-properties">
  Deprecated Properties
</h3>

| Property |
| - |
| None. |

<h3 id="color-samples">
  Samples
</h3>

```json theme={null}
{
	"name": "Label Color",
	"type": "color",
	"descr": "A color for the label",
	"defaultValue": "_inherit",
	"required": false
}
```

See Visual Type Configuration Properties.

<h2 id="float">
  float
</h2>

The `float` variable is part of the array of objects you use to define data and non-data values for this visualization.

<Note>
  You must be an administrator to manage custom visual types.
</Note>

<h3 id="float-type">
  Type
</h3>

```
float
```

<h3 id="float-editor">
  Editor
</h3>

Edit `float` variables using a standard browser number input. If minimum, maximum, or both values are specified in the `config`, a helper message shows below the input to notify the user of these ranges.

<h3 id="float-variable-specific-properties">
  Variable Specific Properties
</h3>

<table>
  <colgroup>
    <col style={{width: "10%"}} />

    <col style={{width: "20%"}} />

    <col style={{width: "12%"}} />

    <col style={{width: "58%"}} />
  </colgroup>

  <thead>
    <tr>
      <th colSpan={2}>Property</th>
      <th>Argument</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>`defaultValue`</td>
      <td>float</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>`config`</td>
      <td>object</td>
      <td>All properties are optional.</td>
    </tr>

    <tr>
      <td />

      <td>`min`</td>
      <td>float</td>
      <td>The minimum value allowed for this variable. Inclusive.</td>
    </tr>

    <tr>
      <td />

      <td>`max`</td>
      <td>float</td>
      <td>The maximum value allowed for this variable. Inclusive.</td>
    </tr>
  </tbody>
</table>

<h3 id="float-generic-properties">
  Generic Properties
</h3>

Generic properties apply to many variables.

<table>
  <colgroup>
    <col style={{width: "22%"}} />

    <col style={{width: "12%"}} />

    <col style={{width: "66%"}} />
  </colgroup>

  <thead>
    <tr>
      <th>Property</th>
      <th>Argument</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`name`</td>
      <td>string</td>
      <td>The name of the property. It must be unique among all variables on the visualization. This name is used to access the data accessor and/or variable value on the controller provided to the visualization.</td>
    </tr>

    <tr>
      <td>`descr`</td>
      <td>string</td>
      <td>A description of the variable for your reference. This is not displayed in the UI.</td>
    </tr>

    <tr>
      <td>`attributeType`</td>
      <td>array of strings</td>

      <td>
        A list of field types to include when selecting fields for this variable. Accepted values:

        <br />

        * `ATTRIBUTE`
        * `TIME`
        * `NUMBER`
        * `INTEGER`
      </td>
    </tr>

    <tr>
      <td>`required`</td>
      <td>boolean</td>
      <td>Triggers the UI to require a value for certain variable types. Not used for this variable type.</td>
    </tr>
  </tbody>
</table>

<h3 id="float-deprecated-properties">
  Deprecated Properties
</h3>

| Property |
| - |
| None. |

<h3 id="float-samples">
  Samples
</h3>

```json theme={null}
{
	"name": "Float Option",
	"type": "float",
	"descr": "A float value",
	"defaultValue": 1.5,
	"config": {
		"min": 1,
		"max": 22.3
		},
		"required": false
}
```

See Visual Type Configuration Properties.

<h2 id="group">
  group
</h2>

The `group` variable is part of the array of objects you use to define data and non-data values for this visualization.

<Note>
  You must be an administrator to manage custom visual types.
</Note>

<h3 id="group-type">
  Type
</h3>

```
group
```

<h3 id="group-editor">
  Editor
</h3>

`group` variables are not represented on the settings panel. Enable editing a `group` variable by adding an axis label for the variable using the `createAxisLabel` method on the controller.

<h3 id="group-variable-specific-properties">
  Variable Specific Properties
</h3>

<table>
  <colgroup>
    <col style={{width: "10%"}} />

    <col style={{width: "10%"}} />

    <col style={{width: "10%"}} />

    <col style={{width: "12%"}} />

    <col style={{width: "58%"}} />
  </colgroup>

  <thead>
    <tr>
      <th>Property</th>

      <th colSpan={2} />

      <th>Argument</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>`config`</td>
      <td>object</td>
      <td>All properties are optional.</td>
    </tr>

    <tr>
      <td />

      <td colSpan={2}>`groupColorSet`</td>
      <td>string</td>
      <td>The name of the color palette to use. The value`_inherit` uses the palette from the currently selected theme.</td>
    </tr>

    <tr>
      <td />

      <td colSpan={2}>`colorGroupIndex`</td>
      <td>integer</td>
      <td>Define this property to enable color configuration for this variable.</td>
    </tr>

    <tr>
      <td />

      <td colSpan={2}>`autoShowColorLegend`</td>
      <td>boolean</td>
      <td>Define as `true` to show the legend by default.</td>
    </tr>

    <tr>
      <td colSpan={3}>`defaultValue`</td>
      <td>object</td>
      <td>Define defaulting sort and limit properties for this variable. All properties are optional.</td>
    </tr>

    <tr>
      <td />

      <td colSpan={2}>`limit`</td>
      <td>integer</td>
      <td>Limit to the number of groups to return.</td>
    </tr>

    <tr>
      <td />

      <td colSpan={2}>`sort`</td>
      <td>object</td>

      <td />
    </tr>

    <tr>
      <td />

      <td />

      <td>`dir`</td>
      <td>string</td>
      <td>Default sort direction. Valid values are `asc` or `desc`.</td>
    </tr>
  </tbody>
</table>

<h3 id="group-generic-properties">
  Generic Properties
</h3>

Generic properties apply to many variables.

<table>
  <colgroup>
    <col style={{width: "22%"}} />

    <col style={{width: "12%"}} />

    <col style={{width: "66%"}} />
  </colgroup>

  <thead>
    <tr>
      <th>Property</th>
      <th>Argument</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`name`</td>
      <td>string</td>
      <td>The name of the property. It must be unique among all variables on the visualization. This name is used to access the data accessor and/or variable value on the controller provided to the visualization.</td>
    </tr>

    <tr>
      <td>`descr`</td>
      <td>string</td>
      <td>A description of the variable for your reference. This is not displayed in the UI.</td>
    </tr>

    <tr>
      <td>`attributeType`</td>
      <td>array of strings</td>

      <td>
        A list of field types to include when selecting fields for this variable. Accepted values:

        <br />

        * `ATTRIBUTE`
        * `TIME`
        * `NUMBER`
        * `INTEGER`
      </td>
    </tr>

    <tr>
      <td>`colorNumb`</td>
      <td>integer</td>
      <td>The number of colors to include in the color palette by default. 0 will choose the smallest palette available.</td>
    </tr>

    <tr>
      <td>`required`</td>
      <td>boolean</td>
      <td>Triggers the UI to require a value for certain variable types. Not used for this variable type.</td>
    </tr>
  </tbody>
</table>

<h3 id="group-deprecated-properties">
  Deprecated Properties
</h3>

| Property |
| - |
| `colorMetric` |
| `groupType` |

<h3 id="group-samples">
  Samples
</h3>

```json theme={null}
{ "name": "Group By", "type": "group", "descr": "The group property", "attributeType": [ "ATTRIBUTE", "TIME", "NUMBER", "INTEGER" ], "defaultValue": { "limit": 20 }, "colorNumb": 0, "config": { "groupColorSet": "_inherit", "colorGroupIndex": 0, "autoShowColorLegend": true }, "required": true }
```

See Visual Type Configuration Properties.

<h2 id="histogram-group">
  histogram-group
</h2>

The `histogram-group` variable is part of the array of objects you use to define data and non-data values for this visualization.

<Note>
  You must be an administrator to manage custom visual types.
</Note>

<h3 id="histogram-group-type">
  Type
</h3>

```
histogram-group
```

<h3 id="histogram-group-editor">
  Editor
</h3>

`histogram-group` variables are not represented on the settings panel. Enable editing a `histogram-group` variable by adding an axis label for the variable using the `createAxisLabel` method on the controller. Other options are not presented to users.

<h3 id="histogram-group-variable-specific-properties">
  Variable Specific Properties
</h3>

<table>
  <colgroup>
    <col style={{width: "10%"}} />

    <col style={{width: "10%"}} />

    <col style={{width: "10%"}} />

    <col style={{width: "12%"}} />

    <col style={{width: "58%"}} />
  </colgroup>

  <thead>
    <tr>
      <th>Property</th>

      <th colSpan={2} />

      <th>Argument</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>`config`</td>
      <td>object</td>
      <td>Sets the default values for this variable.</td>
    </tr>

    <tr>
      <td />

      <td colSpan={2}>`binType`</td>
      <td>string</td>
      <td>How the system should bin the data.</td>
    </tr>

    <tr>
      <td />

      <td />

      <td>`auto`</td>

      <td />

      <td>Define this property to enable color configuration for this variable.</td>
    </tr>

    <tr>
      <td />

      <td />

      <td>`count`</td>

      <td />

      <td>Try to conform the number of bins to the given value.</td>
    </tr>

    <tr>
      <td />

      <td />

      <td>`width`</td>

      <td />

      <td>Try to conform range number of bins to the given value.</td>
    </tr>

    <tr>
      <td />

      <td colSpan={2}>`binsCount`</td>
      <td>integer</td>
      <td>Default number of bins to display when `binType` is set to `count`.</td>
    </tr>

    <tr>
      <td />

      <td colSpan={2}>`binsCount`</td>
      <td>number</td>
      <td>Default number of bins to display when `binType` is set to `width`.</td>
    </tr>

    <tr>
      <td />

      <td colSpan={2}>`values`</td>
      <td>string</td>

      <td>
        `absolute` suggests to the visual type that the actual sum of the bin should be y-axis values.

        <br />

        `relative` suggests to the visual type that the values should be percentages of the whole sum of all bins.
      </td>
    </tr>

    <tr>
      <td />

      <td colSpan={2}>`cumulative`</td>
      <td>boolean</td>
      <td>If `true`, the chart should include a representation of the cumulative value as the bins move from left to right. Typically represented as an overlaid line.</td>
    </tr>
  </tbody>
</table>

<h3 id="histogram-group-generic-properties">
  Generic Properties
</h3>

Generic properties apply to many variables.

<table>
  <colgroup>
    <col style={{width: "22%"}} />

    <col style={{width: "12%"}} />

    <col style={{width: "66%"}} />
  </colgroup>

  <thead>
    <tr>
      <th>Property</th>
      <th>Argument</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`name`</td>
      <td>string</td>
      <td>The name of the property. It must be unique among all variables on the visualization. This name is used to access the data accessor and/or variable value on the controller provided to the visualization.</td>
    </tr>

    <tr>
      <td>`descr`</td>
      <td>string</td>
      <td>A description of the variable for your reference. This is not displayed in the UI.</td>
    </tr>

    <tr>
      <td>`attributeType`</td>
      <td>array of strings</td>

      <td>
        A list of field types to include when selecting fields for this variable. Accepted values:

        <br />

        * `ATTRIBUTE`
        * `TIME`
        * `NUMBER`
        * `INTEGER`
      </td>
    </tr>

    <tr>
      <td>`colorNumb`</td>
      <td>integer</td>
      <td>The number of colors to include in the color palette by default. 0 will choose the smallest palette available.</td>
    </tr>

    <tr>
      <td>`required`</td>
      <td>boolean</td>
      <td>Triggers the UI to require a value for certain variable types. Not used for this variable type.</td>
    </tr>
  </tbody>
</table>

<h3 id="histogram-group-deprecated-properties">
  Deprecated Properties
</h3>

| Property |
| - |
| None. |

<h3 id="histogram-group-samples">
  Samples
</h3>

```json theme={null}
{
	"name": "Group By",
	"type": "histogram-group",
	"attributeType": [
		"INTEGER",
		"NUMBER"
	],
	"colorNumb": 0,
	"config": {
		"binsType": "auto",
		"binsCount": 10,
		"binsWidth": 100,
		"values": "absolute",
		"cumulative": false
	},
	"required": false
}
```

See Visual Type Configuration Properties.

<h2 id="integer">
  integer
</h2>

The `integer` variable is part of the array of objects you use to define data and non-data values for this visualization.

<Note>
  You must be an administrator to manage custom visual types.
</Note>

<h3 id="integer-type">
  Type
</h3>

```
integer
```

<h3 id="integer-editor">
  Editor
</h3>

Edit `integer` variables using a standard browser number input. If minimum, maximum, or both values are specified in the `config`, a helper message shows below the input to notify the user of these ranges.

<img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/customchart/custom-integer.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=5957c04f8c9f87a16b06822d30f2997c" alt="" width="338" height="47" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/customchart/custom-integer.png" />

<h3 id="integer-variable-specific-properties">
  Variable Specific Properties
</h3>

<table>
  <colgroup>
    <col style={{width: "10%"}} />

    <col style={{width: "20%"}} />

    <col style={{width: "12%"}} />

    <col style={{width: "58%"}} />
  </colgroup>

  <thead>
    <tr>
      <th colSpan={2}>Property</th>
      <th>Argument</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>`defaultValue`</td>
      <td>integer</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>`config`</td>
      <td>object</td>
      <td>All properties are optional.</td>
    </tr>

    <tr>
      <td />

      <td>`min`</td>
      <td>integer</td>
      <td>The minimum value allowed for this variable. Inclusive.</td>
    </tr>

    <tr>
      <td />

      <td>`max`</td>
      <td>integer</td>
      <td>The maximum value allowed for this variable. Inclusive.</td>
    </tr>
  </tbody>
</table>

<h3 id="integer-generic-properties">
  Generic Properties
</h3>

Generic properties apply to many variables.

<table>
  <colgroup>
    <col style={{width: "22%"}} />

    <col style={{width: "12%"}} />

    <col style={{width: "66%"}} />
  </colgroup>

  <thead>
    <tr>
      <th>Property</th>
      <th>Argument</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`name`</td>
      <td>string</td>
      <td>The name of the property. It must be unique among all variables on the visualization. This name is used to access the data accessor and/or variable value on the controller provided to the visualization.</td>
    </tr>

    <tr>
      <td>`descr`</td>
      <td>string</td>
      <td>A description of the variable for your reference. This is not displayed in the UI.</td>
    </tr>

    <tr>
      <td>`attributeType`</td>
      <td>array of strings</td>

      <td>
        A list of field types to include when selecting fields for this variable. Accepted values:

        <br />

        * `ATTRIBUTE`
        * `TIME`
        * `NUMBER`
        * `INTEGER`
      </td>
    </tr>

    <tr>
      <td>`required`</td>
      <td>boolean</td>
      <td>Triggers the UI to require a value for certain variable types. Not used for this variable type.</td>
    </tr>
  </tbody>
</table>

<h3 id="integer-deprecated-properties">
  Deprecated Properties
</h3>

| Property |
| - |
| None. |

<h3 id="integer-samples">
  Samples
</h3>

```json theme={null}
{
	"name": "Integer Option",
	"type": "integer",
	"descr": "An integer value",
	"defaultValue": 1,
	"config": {
		"min": 1,
		"max": 22
	},
	"required": false
}
```

See Visual Type Configuration Properties.

<h2 id="metric">
  metric
</h2>

The `metric` variable is part of the array of objects you use to define data and non-data values for this visualization.

<Note>
  You must be an administrator to manage custom visual types.
</Note>

<h3 id="metric-type">
  Type
</h3>

```
metric
```

<h3 id="metric-editor">
  Editor
</h3>

`metric` variables are not represented on the settings panel. Enable editing a `metric` variable by adding an axis label for the variable using the `createAxisLabel` method on the controller.

<h3 id="metric-variable-specific-properties">
  Variable Specific Properties
</h3>

<table>
  <colgroup>
    <col style={{width: "10%"}} />

    <col style={{width: "10%"}} />

    <col style={{width: "10%"}} />

    <col style={{width: "12%"}} />

    <col style={{width: "58%"}} />
  </colgroup>

  <thead>
    <tr>
      <th>Property</th>

      <th colSpan={2} />

      <th>Argument</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>`colorSet`</td>
      <td>string</td>
      <td>The name of the color palette to use by default. The value`_inherit` uses the palette from the currently selected theme. Other available values include `DefaultSequential` and `DefaultQualitative`.</td>
    </tr>

    <tr>
      <td colSpan={3}>`metricType`</td>
      <td>string</td>
      <td>Set to `color` to enable this metric as the color metric. Only set this to one metric on the visualization.</td>
    </tr>

    <tr>
      <td colSpan={3}>`legendType`</td>
      <td>string</td>
      <td>Available values include `palette` and `range`.</td>
    </tr>

    <tr>
      <td colSpan={3}>`config`</td>
      <td>object</td>
      <td>All properties are optional.</td>
    </tr>

    <tr>
      <td />

      <td colSpan={2}>`displayNoneOption`</td>
      <td>boolean</td>
      <td>When set to `true`, users can select `None` when choosing a field for this variable.</td>
    </tr>

    <tr>
      <td colSpan={3}>`defaultValue`</td>
      <td>array of object</td>
      <td>Enable to allow setting of a default configuration for the chosen field.</td>
    </tr>

    <tr>
      <td />

      <td colSpan={2}>`name`</td>
      <td>string</td>
      <td>A value of `none` combined with `config.displayNoneOption` set to `true` will default the selected field to `None`. A value of `count` will automatically select the `Volume`metric.</td>
    </tr>

    <tr>
      <td />

      <td colSpan={2}>`colorConfig`</td>
      <td>object</td>

      <td />
    </tr>

    <tr>
      <td />

      <td />

      <td>`autoShowColorLegend`</td>
      <td>boolean</td>
      <td>If `true`, show a legend for this variable by default.</td>
    </tr>

    <tr>
      <td />

      <td />

      <td>`colorNumb`</td>
      <td>integer</td>
      <td>The number of colors to include in the color palette by default. 0 will choose the smallest palette available.</td>
    </tr>

    <tr>
      <td />

      <td />

      <td>`legendType`</td>
      <td>string</td>
      <td>Available values include `palette` and `range`.</td>
    </tr>

    <tr>
      <td />

      <td />

      <td>`colorScaleType`</td>
      <td>string</td>
      <td>Available values include `gradient` and `distinct`.</td>
    </tr>
  </tbody>
</table>

<h3 id="metric-generic-properties">
  Generic Properties
</h3>

Generic properties apply to many variables.

<table>
  <colgroup>
    <col style={{width: "22%"}} />

    <col style={{width: "12%"}} />

    <col style={{width: "66%"}} />
  </colgroup>

  <thead>
    <tr>
      <th>Property</th>
      <th>Argument</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`name`</td>
      <td>string</td>
      <td>The name of the property. It must be unique among all variables on the visualization. This name is used to access the data accessor and/or variable value on the controller provided to the visualization.</td>
    </tr>

    <tr>
      <td>`descr`</td>
      <td>string</td>
      <td>A description of the variable for your reference. This is not displayed in the UI.</td>
    </tr>

    <tr>
      <td>`attributeType`</td>
      <td>array of strings</td>

      <td>
        A list of field types to include when selecting fields for this variable. Accepted values:

        <br />

        * `ATTRIBUTE`
        * `TIME`
        * `NUMBER`
        * `INTEGER`
      </td>
    </tr>

    <tr>
      <td>`colorNumb`</td>
      <td>integer</td>
      <td>The number of colors to include in the color palette by default. 0 will choose the smallest palette available.</td>
    </tr>

    <tr>
      <td>`required`</td>
      <td>boolean</td>
      <td>Triggers the UI to require a value for certain variable types. Not used for this variable type.</td>
    </tr>
  </tbody>
</table>

<h3 id="metric-deprecated-properties">
  Deprecated Properties
</h3>

| Property |
| - |
| `colorMetric` |
| `groupType` |

<h3 id="metric-samples">
  Samples
</h3>

```json theme={null}
{ "name": "Bar Color", "type": "metric", "attributeType": [ "INTEGER", "NUMBER" ], "defaultValue": [ { "name": "count", "colorConfig": { "colorNumb": 3, "legendType": "palette", "autoShowColorLegend": true } } ], "config": { "displayNoneOption": true }, "colorNumb": 3, "colorSet": "_inherit", "metricType": "color", "legendType": "palette", "required": false }
```

See Visual Type Configuration Properties.

<h2 id="multi-group">
  multi-group
</h2>

The `multi-group` variable is part of the array of objects you use to define data and non-data values for this visualization.

<Note>
  You must be an administrator to manage custom visual types.
</Note>

<h3 id="multi-group-type">
  Type
</h3>

```
multi-group
```

<h3 id="multi-group-editor">
  Editor
</h3>

`multi-group` variables are not represented on the settings panel. Enable editing a `multi-group` variable by adding an axis label for the variable using the `createAxisLabel` method on the controller.

<h3 id="multi-group-variable-specific-properties">
  Variable Specific Properties
</h3>

<table>
  <colgroup>
    <col style={{width: "22%"}} />

    <col style={{width: "12%"}} />

    <col style={{width: "66%"}} />
  </colgroup>

  <thead>
    <tr>
      <th>Property</th>
      <th>Argument</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`config`</td>
      <td>object</td>

      <td />
    </tr>

    <tr>
      <td>`groupLevel`</td>
      <td>array of integers</td>
      <td>A label to show for each grouping level. The number of entries in this array should match the value set for `groupLevel`.</td>
    </tr>

    <tr>
      <td>`groupNames`</td>
      <td>array of strings</td>
      <td>The number of grouping levels to allow.</td>
    </tr>

    <tr>
      <td>`groupTypes`</td>
      <td>array of strings</td>

      <td>
        The set of field types to allow for each grouping level. Each entry should be a space-delimited list of all field types to allow. The number of entries in this array should match the value set for `groupLevel`. Accepted values:

        <br />

        * `ATTRIBUTE`
        * `TIME`
        * `NUMBER`
        * `INTEGER`
        * `MONEY`
        * `NONE`
      </td>
    </tr>

    <tr>
      <td>`groupTypes`</td>
      <td>string</td>
      <td>The name of the color palette to use by default. The value`_inherit` uses the palette from the currently selected theme.</td>
    </tr>

    <tr>
      <td>`colorGroupIndex`</td>
      <td>integer</td>
      <td>Define this property to enable color configuration for this variable.</td>
    </tr>

    <tr>
      <td>`autoShowColorLegend`</td>
      <td>boolean</td>
      <td>If `true`, show a legend for this variable by default.</td>
    </tr>
  </tbody>
</table>

<h3 id="multi-group-generic-properties">
  Generic Properties
</h3>

Generic properties apply to many variables.

<table>
  <colgroup>
    <col style={{width: "22%"}} />

    <col style={{width: "12%"}} />

    <col style={{width: "66%"}} />
  </colgroup>

  <thead>
    <tr>
      <th>Property</th>
      <th>Argument</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`name`</td>
      <td>string</td>
      <td>The name of the property. It must be unique among all variables on the visualization. This name is used to access the data accessor and/or variable value on the controller provided to the visualization.</td>
    </tr>

    <tr>
      <td>`descr`</td>
      <td>string</td>
      <td>A description of the variable for your reference. This is not displayed in the UI.</td>
    </tr>

    <tr>
      <td>`attributeType`</td>
      <td>array of strings</td>

      <td>
        A list of field types to include when selecting fields for this variable. Accepted values:

        <br />

        * `ATTRIBUTE`
        * `TIME`
        * `NUMBER`
        * `INTEGER`
      </td>
    </tr>

    <tr>
      <td>`colorNumb`</td>
      <td>integer</td>
      <td>The number of colors to include in the color palette by default. 0 will choose the smallest palette available.</td>
    </tr>

    <tr>
      <td>`required`</td>
      <td>boolean</td>
      <td>Triggers the UI to require a value for certain variable types. Not used for this variable type.</td>
    </tr>
  </tbody>
</table>

<h3 id="multi-group-deprecated-properties">
  Deprecated Properties
</h3>

| Property |
| - |
| `colorMetric` |
| `groupType` |

<h3 id="multi-group-samples">
  Samples
</h3>

```json theme={null}
{ "name": "Multi Group By", "type": "multi-group", "descr": "Multiple, layered groups", "attributeType": [ "ATTRIBUTE", "TIME" ], "colorNumb": 0, "config": { "groupLevel": 2, "groupNames": [ "Group 1", "Group 2" ], "groupLimits": [ 50, 20 ], "groupTypes": [ "ATTRIBUTE TIME NUMBER INTEGER MONEY", "ATTRIBUTE TIME NUMBER INTEGER MONEY NONE" ], "groupColorSet": "_inherit", "colorGroupIndex": 0, "autoShowColorLegend": true }, "required": true }
```

See Visual Type Configuration Properties.

<h2 id="multi-metric">
  multi-metric
</h2>

The `multi-metric` variable is part of the array of objects you use to define data and non-data values for this visualization.

<Note>
  You must be an administrator to manage custom visual types.
</Note>

<h3 id="multi-metric-type">
  Type
</h3>

```
multi-metric
```

<h3 id="multi-metric-editor">
  Editor
</h3>

`multi-metric` variables are not represented on the settings panel. Enable editing a `multi-metric` variable by adding an axis label for the variable using the `createAxisLabel` method on the controller.

<h3 id="multi-metric-variable-specific-properties">
  Variable Specific Properties
</h3>

<table>
  <colgroup>
    <col style={{width: "10%"}} />

    <col style={{width: "10%"}} />

    <col style={{width: "10%"}} />

    <col style={{width: "12%"}} />

    <col style={{width: "58%"}} />
  </colgroup>

  <thead>
    <tr>
      <th colSpan={3}>Property</th>
      <th>Argument</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>`colorSet`</td>
      <td>string</td>
      <td>The name of the color palette to use by default. The value`_inherit` uses the palette from the currently selected theme. Other available values include `DefaultSequential` and `DefaultQualitative`.</td>
    </tr>

    <tr>
      <td colSpan={3}>`metricType`</td>
      <td>string</td>
      <td>Set to `color` to enable this metric as the color metric. Only set this to one metric on the visualization.</td>
    </tr>

    <tr>
      <td colSpan={3}>`legendType`</td>
      <td>string</td>
      <td>Available values include `palette` and `range`.</td>
    </tr>

    <tr>
      <td colSpan={3}>`defaultValue`</td>
      <td>array of object</td>
      <td>Enable to allow setting of a default configuration for the chosen field.</td>
    </tr>

    <tr>
      <td />

      <td colSpan={2}>`name`</td>
      <td>string</td>
      <td>A value of `none` combined with `config.displayNoneOption` set to `true` will default the selected field to `None`. A value of `count` will automatically select the `Volume`metric.</td>
    </tr>

    <tr>
      <td />

      <td colSpan={2}>`colorConfig`</td>
      <td>object</td>

      <td />
    </tr>

    <tr>
      <td />

      <td />

      <td>`autoShowColorLegend`</td>
      <td>boolean</td>
      <td>If `true`, show a legend for this variable by default.</td>
    </tr>

    <tr>
      <td />

      <td />

      <td>`colorNumb`</td>
      <td>integer</td>
      <td>The number of colors to include in the color palette by default. 0 will choose the smallest palette available.</td>
    </tr>

    <tr>
      <td />

      <td />

      <td>`legendType`</td>
      <td>string</td>
      <td>Available values include `palette` and `range`.</td>
    </tr>

    <tr>
      <td />

      <td />

      <td>`colorScaleType`</td>
      <td>string</td>
      <td>Available values include `gradient` and `distinct`.</td>
    </tr>
  </tbody>
</table>

<h3 id="multi-metric-generic-properties">
  Generic Properties
</h3>

Generic properties apply to many variables.

<table>
  <colgroup>
    <col style={{width: "22%"}} />

    <col style={{width: "12%"}} />

    <col style={{width: "66%"}} />
  </colgroup>

  <thead>
    <tr>
      <th>Property</th>
      <th>Argument</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`name`</td>
      <td>string</td>
      <td>The name of the property. It must be unique among all variables on the visualization. This name is used to access the data accessor and/or variable value on the controller provided to the visualization.</td>
    </tr>

    <tr>
      <td>`descr`</td>
      <td>string</td>
      <td>A description of the variable for your reference. This is not displayed in the UI.</td>
    </tr>

    <tr>
      <td>`attributeType`</td>
      <td>array of strings</td>

      <td>
        A list of field types to include when selecting fields for this variable. Accepted values:

        <br />

        * `ATTRIBUTE`
        * `TIME`
        * `NUMBER`
        * `INTEGER`
      </td>
    </tr>

    <tr>
      <td>`colorNumb`</td>
      <td>integer</td>
      <td>The number of colors to include in the color palette by default. 0 will choose the smallest palette available.</td>
    </tr>

    <tr>
      <td>`required`</td>
      <td>boolean</td>
      <td>Triggers the UI to require a value for certain variable types. Not used for this variable type.</td>
    </tr>
  </tbody>
</table>

<h3 id="multi-metric-deprecated-properties">
  Deprecated Properties
</h3>

| Property |
| - |
| `colorMetric` |

<h3 id="multi-metric-samples">
  Samples
</h3>

```json theme={null}
{ "name": "Y1 Axis", "type": "multi-metric", "attributeType": [ "INTEGER", "NUMBER" ], "defaultValue": [ { "colorConfig": { "autoShowColorLegend": true } } ], "colorNumb": 4, "metricType": "color", "colorSet": "_inherit", "legendType": "palette", "required": false }
```

See Visual Type Configuration Properties.

<h2 id="multilist">
  multilist
</h2>

The `multilist` variable is part of the array of objects you use to define data and non-data values for this visualization.

<Note>
  You must be an administrator to manage custom visual types.
</Note>

<h3 id="multilist-type">
  Type
</h3>

```
multilist
```

<h3 id="multilist-editor">
  Editor
</h3>

`multilist` have two modes:

1. If the `values` property is provided, the variable is represented by a multi-select tag input.

   <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/customchart/custom-multilist.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=4e259a58d2d589f19f88d163940337db" alt="" width="337" height="214" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/customchart/custom-multilist.png" />

2. If `values` is not provided, the variable is represented by a control that provides an arrangeable list of fields that includes an edit button. Users can select which fields should and should not be included.

<h3 id="multilist-variable-specific-properties">
  Variable Specific Properties
</h3>

| Property | Argument | Description |
| - | - | - |
| `defaultValue` | array of strings | Only applicable for the static value list. |
| `values` | array of strings | The options made available to users for selection. |

<h3 id="multilist-generic-properties">
  Generic Properties
</h3>

Generic properties apply to many variables.

<table>
  <colgroup>
    <col style={{width: "22%"}} />

    <col style={{width: "12%"}} />

    <col style={{width: "66%"}} />
  </colgroup>

  <thead>
    <tr>
      <th>Property</th>
      <th>Argument</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`name`</td>
      <td>string</td>
      <td>The name of the property. It must be unique among all variables on the visualization. This name is used to access the data accessor and/or variable value on the controller provided to the visualization.</td>
    </tr>

    <tr>
      <td>`descr`</td>
      <td>string</td>
      <td>A description of the variable for your reference. This is not displayed in the UI.</td>
    </tr>

    <tr>
      <td>`attributeType`</td>
      <td>array of strings</td>

      <td>
        A list of field types to include when selecting fields for this variable. Accepted values:

        <br />

        * `ATTRIBUTE`
        * `TIME`
        * `NUMBER`
        * `INTEGER`
      </td>
    </tr>

    <tr>
      <td>`required`</td>
      <td>boolean</td>
      <td>Triggers the UI to require a value for certain variable types. Not used for this variable type.</td>
    </tr>
  </tbody>
</table>

<h3 id="multilist-deprecated-properties">
  Deprecated Properties
</h3>

| Property |
| - |
| None. |

<h3 id="multilist-samples">
  Samples
</h3>

#### Static Values

```json theme={null}
{ "name": "Test Static Value Multilist", "type": "multilist", "descr": "Select multiple values. Order is not selectable", "values": [ "Value 1", "Value 2", "Value 3", "Value 4" ], "defaultValue": [ "Value 2", "Value 3" ], "required": false }
```

#### Field Selection

```json theme={null}
{ "name": "Test Field Multilist", "type": "multilist", "descr": "Select and arrange multiple fields", "attributeType": [ "ATTRIBUTE", "TIME", "NUMBER", "INTEGER" ], "defaultValue": [], "required": false }
```

See Visual Type Configuration Properties.

<h2 id="singlelist">
  singlelist
</h2>

The `singlelist` variable is part of the array of objects you use to define data and non-data values for this visualization.

<Note>
  You must be an administrator to manage custom visual types.
</Note>

<h3 id="singlelist-type">
  Type
</h3>

```
singlelist
```

<h3 id="singlelist-editor">
  Editor
</h3>

`singlelist` variables are represented in the settings sidebar as a simple drop down.

<img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/customchart/custom-singlelist.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=cbb51b244996deb59d7eb8dc96f79aef" alt="" width="352" height="204" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/customchart/custom-singlelist.png" />

<h3 id="singlelist-variable-specific-properties">
  Variable Specific Properties
</h3>

| Property | Argument | Description |
| - | - | - |
| `defaultValue` | string | |
| `values` | array of strings | The options you make available for users to select from. |

<h3 id="singlelist-generic-properties">
  Generic Properties
</h3>

Generic properties apply to many variables.

<table>
  <colgroup>
    <col style={{width: "22%"}} />

    <col style={{width: "12%"}} />

    <col style={{width: "66%"}} />
  </colgroup>

  <thead>
    <tr>
      <th>Property</th>
      <th>Argument</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`name`</td>
      <td>string</td>
      <td>The name of the property. It must be unique among all variables on the visualization. This name is used to access the data accessor and/or variable value on the controller provided to the visualization.</td>
    </tr>

    <tr>
      <td>`descr`</td>
      <td>string</td>
      <td>A description of the variable for your reference. This is not displayed in the UI.</td>
    </tr>

    <tr>
      <td>`attributeType`</td>
      <td>array of strings</td>

      <td>
        A list of field types to include when selecting fields for this variable. Accepted values:

        <br />

        * `ATTRIBUTE`
        * `TIME`
        * `NUMBER`
        * `INTEGER`
      </td>
    </tr>

    <tr>
      <td>`required`</td>
      <td>boolean</td>
      <td>Triggers the UI to require a value for certain variable types. Not used for this variable type.</td>
    </tr>
  </tbody>
</table>

<h3 id="singlelist-deprecated-properties">
  Deprecated Properties
</h3>

| Property |
| - |
| None. |

<h3 id="singlelist-samples">
  Samples
</h3>

```json theme={null}
{ "name": "Tile Provider", "type": "singlelist", "descr": "Map tile provider", "values": [ "OpenStreetMap (no API key required)", "MapQuest", "MapBox", "N/A" ], "defaultValue": "OpenStreetMap (no API key required)", "required": false }
```

See Visual Type Configuration Properties.

<h2 id="string">
  string
</h2>

The `string` variable is part of the array of objects you use to define data and non-data values for this visualization.

<Note>
  You must be an administrator to manage custom visual types.
</Note>

<h3 id="string-type">
  Type
</h3>

```
string
```

<h3 id="string-editor">
  Editor
</h3>

Users can edit `string` variables using a standard browser text input.

<img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/customchart/custom-string.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=37a9485c3db9a85fe52856213073ab87" alt="" width="337" height="66" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/customchart/custom-string.png" />

<h3 id="string-variable-specific-properties">
  Variable Specific Properties
</h3>

| Property | Argument | Description |
| - | - | - |
| `defaultValue` | string | |

<h3 id="string-generic-properties">
  Generic Properties
</h3>

Generic properties apply to many variables.

<table>
  <colgroup>
    <col style={{width: "22%"}} />

    <col style={{width: "12%"}} />

    <col style={{width: "66%"}} />
  </colgroup>

  <thead>
    <tr>
      <th>Property</th>
      <th>Argument</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`name`</td>
      <td>string</td>
      <td>The name of the property. It must be unique among all variables on the visualization. This name is used to access the data accessor and/or variable value on the controller provided to the visualization.</td>
    </tr>

    <tr>
      <td>`descr`</td>
      <td>string</td>
      <td>A description of the variable for your reference. This is not displayed in the UI.</td>
    </tr>

    <tr>
      <td>`attributeType`</td>
      <td>array of strings</td>

      <td>
        A list of field types to include when selecting fields for this variable. Accepted values:

        <br />

        * `ATTRIBUTE`
        * `TIME`
        * `NUMBER`
        * `INTEGER`
      </td>
    </tr>

    <tr>
      <td>`required`</td>
      <td>boolean</td>
      <td>Triggers the UI to require a value for certain variable types. Not used for this variable type.</td>
    </tr>
  </tbody>
</table>

<h3 id="string-deprecated-properties">
  Deprecated Properties
</h3>

| Property |
| - |
| None. |

<h3 id="string-samples">
  Samples
</h3>

```json theme={null}
{ "name": "Tile Provider API Key", "type": "string", "descr": "API key for the tile provider chosen. OpenStreetMap does not require an API key.", "required": false }
```

See Visual Type Configuration Properties.

<h2 id="text">
  text
</h2>

The `text` variable is part of the array of objects you use to define data and non-data values for this visualization.

<Note>
  You must be an administrator to manage custom visual types.
</Note>

<h3 id="text-type">
  Type
</h3>

```
text
```

<h3 id="text-editor">
  Editor
</h3>

Users can edit `text` variables using a standard browser text input.

<img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/customchart/custom-text.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=c5a81c660ff5d4a6adda72b5d6ff46bb" alt="" width="333" height="94" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/customchart/custom-text.png" />

<h3 id="text-variable-specific-properties">
  Variable Specific Properties
</h3>

| Property | Argument | Description |
| - | - | - |
| `defaultValue` | string | |

<h3 id="text-generic-properties">
  Generic Properties
</h3>

Generic properties apply to many variables.

<table>
  <colgroup>
    <col style={{width: "22%"}} />

    <col style={{width: "12%"}} />

    <col style={{width: "66%"}} />
  </colgroup>

  <thead>
    <tr>
      <th>Property</th>
      <th>Argument</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`name`</td>
      <td>string</td>
      <td>The name of the property. It must be unique among all variables on the visualization. This name is used to access the data accessor and/or variable value on the controller provided to the visualization.</td>
    </tr>

    <tr>
      <td>`descr`</td>
      <td>string</td>
      <td>A description of the variable for your reference. This is not displayed in the UI.</td>
    </tr>

    <tr>
      <td>`attributeType`</td>
      <td>array of strings</td>

      <td>
        A list of field types to include when selecting fields for this variable. Accepted values:

        <br />

        * `ATTRIBUTE`
        * `TIME`
        * `NUMBER`
        * `INTEGER`
      </td>
    </tr>

    <tr>
      <td>`required`</td>
      <td>boolean</td>
      <td>Triggers the UI to require a value for certain variable types. Not used for this variable type.</td>
    </tr>
  </tbody>
</table>

<h3 id="text-deprecated-properties">
  Deprecated Properties
</h3>

| Property |
| - |
| None. |

<h3 id="text-samples">
  Samples
</h3>

```json theme={null}
{ "name": "Text Property", "type": "text", "descr": "API key for the tile provider chosen. OpenStreetMap does not require an API key.", "required": false }
```

See Visual Type Configuration Properties.

<h2 id="ungrouped">
  ungrouped
</h2>

The `ungrouped` variable is part of the array of objects you use to define data and non-data values for this visualization.

<Note>
  You must be an administrator to manage custom visual types.
</Note>

<h3 id="ungrouped-type">
  Type
</h3>

```
ungrouped
```

<h3 id="ungrouped-editor">
  Editor
</h3>

`ungrouped` variables are represented by a series of buttons to allow users to select a set number of fields matched up with labels. Below the field buttons is a number input to choose a limit to the number of records that should be returned. By default, the labels provided are used to attempt to select the correct fields. If no fields match the labels, the first *n* fields are selected.

<img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/customchart/custom-ungrouped.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=cbe4c20a0421a88f4c9a3da567e08bab" alt="" width="786" height="700" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/customchart/custom-ungrouped.png" />

<h3 id="ungrouped-variable-specific-properties">
  Variable Specific Properties
</h3>

<table>
  <colgroup>
    <col style={{width: "10%"}} />

    <col style={{width: "20%"}} />

    <col style={{width: "12%"}} />

    <col style={{width: "58%"}} />
  </colgroup>

  <thead>
    <tr>
      <th colSpan={2}>Property</th>
      <th>Argument</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>`config`</td>
      <td>object</td>
      <td>All properties are required.</td>
    </tr>

    <tr>
      <td />

      <td>`groupLevel`</td>
      <td>integer</td>
      <td>The number of fields to be selected.</td>
    </tr>

    <tr>
      <td />

      <td>`groupNames`</td>
      <td>array of strings</td>
      <td>A list of labels for the fields. The length of this array should match the value set for `groupLevel`.</td>
    </tr>

    <tr>
      <td />

      <td>`limit`</td>
      <td>integer</td>
      <td>The number of ungrouped records to return.</td>
    </tr>
  </tbody>
</table>

<h3 id="ungrouped-generic-properties">
  Generic Properties
</h3>

Generic properties apply to many variables.

<table>
  <colgroup>
    <col style={{width: "22%"}} />

    <col style={{width: "12%"}} />

    <col style={{width: "66%"}} />
  </colgroup>

  <thead>
    <tr>
      <th>Property</th>
      <th>Argument</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`name`</td>
      <td>string</td>
      <td>The name of the property. It must be unique among all variables on the visualization. This name is used to access the data accessor and/or variable value on the controller provided to the visualization.</td>
    </tr>

    <tr>
      <td>`descr`</td>
      <td>string</td>
      <td>A description of the variable for your reference. This is not displayed in the UI.</td>
    </tr>

    <tr>
      <td>`attributeType`</td>
      <td>array of strings</td>

      <td>
        A list of field types to include when selecting fields for this variable. Accepted values:

        <br />

        * `ATTRIBUTE`
        * `TIME`
        * `NUMBER`
        * `INTEGER`
      </td>
    </tr>

    <tr>
      <td>`required`</td>
      <td>boolean</td>
      <td>Triggers the UI to require a value for certain variable types. Not used for this variable type.</td>
    </tr>
  </tbody>
</table>

<h3 id="ungrouped-deprecated-properties">
  Deprecated Properties
</h3>

| Property |
| - |
| None. |

<h3 id="ungrouped-samples">
  Samples
</h3>

```json theme={null}
{ "name": "Latitude/Longitude", "type": "ungrouped", "descr": "Latitude and Longitude fields", "config": { "groupLevel": 2, "groupNames": [ "Latitude", "Longitude" ], "limit": 100000 }, "required": false }
```

See Visual Type Configuration Properties.

<h2 id="ungroupedlist">
  ungroupedList
</h2>

The `ungroupedList`variable is part of the array of objects you use to define data and non-data values for this visualization.

<Note>
  You must be an administrator to manage custom visual types.
</Note>

<h3 id="ungroupedlist-type">
  Type
</h3>

```
ungroupedList
```

<h3 id="ungroupedlist-editor">
  Editor
</h3>

`ungroupedList` variables are represented by two styles of control depending on the presence or absence of the `groupLevel` and `groupNames` properties in the `config`.

If no `groupLevel` and `groupNames` properties are defined, the control provides only an arrangeable list of fields with an edit button which allows selecting or deselecting which fields should be included.

<img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/customchart/custom-ungroupedlist02.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=79e937344e4b1faaf8002973c6807b72" alt="custom chart settings sidebar ungrouped list" width="786" height="668" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/customchart/custom-ungroupedlist02.png" />

If `groupLevel` and `groupNames` are defined in the `config`, the variable is represented by a combination of the UI from the `ungrouped`variable and the UI shown above. This allows you to supply a set number of fields as named properties as well as an undefined number of additional fields for other purposes. When selecting the field for any named properties or for the additional fields list, the fields selected for other uses will not be selectable.

<img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/customchart/custom-ungroupedlist-settings-03.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=d9c325029bdbbffae958f432b9bc8f85" alt="custom chart settings example" width="401" height="738" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/customchart/custom-ungroupedlist-settings-03.png" />

<h3 id="ungroupedlist-variable-specific-properties">
  Variable Specific Properties
</h3>

<table>
  <colgroup>
    <col style={{width: "10%"}} />

    <col style={{width: "20%"}} />

    <col style={{width: "12%"}} />

    <col style={{width: "58%"}} />
  </colgroup>

  <thead>
    <tr>
      <th colSpan={2}>Property</th>
      <th>Argument</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>`config`</td>
      <td>object</td>
      <td>All properties are optional but `groupLevel` and `groupNames` should be provided together if they are provided.</td>
    </tr>

    <tr>
      <td />

      <td>`groupLevel`</td>
      <td>integer</td>
      <td>The number of fields to select.</td>
    </tr>

    <tr>
      <td />

      <td>`groupNames`</td>
      <td>array of strings</td>
      <td>A list of labels for the fields. The length of this array should match the value provided as `groupLevel`.</td>
    </tr>

    <tr>
      <td />

      <td>`limit`</td>
      <td>integer</td>
      <td>The number of ungrouped records that should be returned.</td>
    </tr>

    <tr>
      <td />

      <td>`additionalFieldsLabel`</td>
      <td>string</td>
      <td>The label that will be shown above the field list if `groupLevel` and `groupNames` are provided.</td>
    </tr>
  </tbody>
</table>

<h3 id="ungroupedlist-generic-properties">
  Generic Properties
</h3>

Generic properties apply to many variables.

<table>
  <colgroup>
    <col style={{width: "22%"}} />

    <col style={{width: "12%"}} />

    <col style={{width: "66%"}} />
  </colgroup>

  <thead>
    <tr>
      <th>Property</th>
      <th>Argument</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`name`</td>
      <td>string</td>
      <td>The name of the property. It must be unique among all variables on the visualization. This name is used to access the data accessor and/or variable value on the controller provided to the visualization.</td>
    </tr>

    <tr>
      <td>`descr`</td>
      <td>string</td>
      <td>A description of the variable for your reference. This is not displayed in the UI.</td>
    </tr>

    <tr>
      <td>`attributeType`</td>
      <td>array of strings</td>

      <td>
        A list of field types to include when selecting fields for this variable. Accepted values:

        <br />

        * `ATTRIBUTE`
        * `TIME`
        * `NUMBER`
        * `INTEGER`
      </td>
    </tr>

    <tr>
      <td>`required`</td>
      <td>boolean</td>
      <td>Triggers the UI to require a value for certain variable types. Not used for this variable type.</td>
    </tr>
  </tbody>
</table>

<h3 id="ungroupedlist-deprecated-properties">
  Deprecated Properties
</h3>

| Property |
| - |
| None. |

<h3 id="ungroupedlist-samples">
  Samples
</h3>

```json theme={null}
{ "name": "Test Ungrouped List", "type": "ungroupedList", "descr": "Select multiple fields for ungrouped data", "attributeType": [ "ATTRIBUTE", "INTEGER", "NUMBER" ], "config": { "groupLevel": 2, "groupNames": [ "Latitude", "Longitude" ], "limit": 100000, "additionalFieldsLabel": "Extra Fields" } "required": false }
```

See Visual Type Configuration Properties.
