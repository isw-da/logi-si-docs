---
title: "Visual Type Configuration Properties"
id: 43701046187277
section: "Composer 26 Developer Tools"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701046187277-Visual-Type-Configuration-Properties
updated_at: 2026-05-29T14:08:02Z
---

# Visual Type Configuration Properties

# Visual Type Configuration Properties

This section describes the properties of visualization type configurations, possible values, and the definition of those values for creating or editing visual types (custom charts) for Composer.

**Note:** 
You must be an administrator to manage custom visual types.

## Properties

`name` - **string**

`name` is the name of visual type the configuration file represents, and displays in the user interface. This name must be unique in your Composer instance, or it will overwrite or be overwritten by a visual type using the same name.

`type` - **string**

`type` is one of the properties Composer uses internally to represent and distinguish visual types. Built-in visuals have unique `type` properties. Any visual you add to the system should use the same value, `CUSTOM`.

`controls` - **array of strings**

`controls` is the list of things you enable this visual type to do. Supported values are included in the chart below:

| Control | Description |
| --- | --- |
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

**Note:** 
Additional properties may be present in a visualization’s `controls` array but they may deprecated, irrelevant to a custom visual type that doesn't use the properties.

`variables` - **array of objects**

`variables` are required for the configuration. This array of objects define data and non-data values associated with instances of this visualization. All supported variable configuration are included in the list below.

* [attribute](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701045636877-attribute)
* [bool](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701012960013-bool)
* [box-plot-metric](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701027775501-box-plot-metric)
* [color](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701027785741-color)
* [float](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701092126733-float)
* [group](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701045783949-group)
* [histogram-group](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701075515149-histogram-group)
* [integer](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701045844237-integer)
* [metric](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701075577869-metric)
* [multi-group](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700996832909-multi-group)
* [multilist](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701013269773-multilist)
* [multi-metric](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701075642125-multi-metric)
* [singlelist](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701045999117-singlelist)
* [string](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701092459917-string)
* [text](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700996967053-text)
* [ungrouped](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701013390349-ungrouped)
* [ungroupedList](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701046144909-ungroupedList)

You can also maintain custom charts using the CLI. See [Maintain Custom Charts Using the Custom Chart CLI](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701075906189-Maintain-Custom-Charts-Using-the-Custom-Chart-CLI).
