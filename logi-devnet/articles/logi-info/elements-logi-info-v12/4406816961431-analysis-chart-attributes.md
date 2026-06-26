---
title: "Analysis Chart - Attributes"
id: 4406816961431
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406816961431-Analysis-Chart-Attributes
updated_at: 2022-04-06T06:03:06Z
---

# Analysis Chart - Attributes

# Analysis Chart - Attributes

The Analysis Chart element can be quickly configured and has the following attributes:

| Attribute | Description |
| --- | --- |
| ID | (Required) Specifies a unique identifier for this element. |
| Allow Control Hiding | Specifies whether a "gear" icon will be visible that allows the user to hide the control panel. Default Value: *False.* |
| Analysis Chart Types | Specifies a comma-delimited list of the chart types that will be available in the Analysis Chart. Possible values are *Pie*, *Bar*, *Line*, *Spline*, *Scatter*, *Heatmap* and *Gauge*. "Spline" is the Curved Line chart. The first type in the list will be the initial/starting chart type.  The Pie chart option only appears when there is at least one Analysis Chart Column with Data Type=*Text*. Bar charts require a column with a *Text* or *Date* type. |
| Batch Selection | Specifies whether the chart will be updated immediately as each control panel item is changed (*False*) or only when a now-visible OK button is clicked (*True*). Setting this to *True* can speed up the user experience by reducing the number of updates requested from the server. |
| Class | Specifies a user-defined style sheet class to be used with the Analysis Chart. We recommend the use of a Theme for the best appearance. |
| Color | Specifies the chart colors. Enter a color by name, decimal RGB value, or hex RGB value. Prefix hex values with the pound sign, like #112233. Each bar in a Bar Chart can be made a different color by entering multiple colors, in a comma-separated list. |
| Control Panel Location | Specifies whether the Control Panel appears above (Top) or beside (Left) the Chart Area. Default value: *Top* |
| Height | Specifies the height, in pixels, of the chart image. Does *not* include the Control Panel. Leave blank for a default size, which can vary by chart type and data. |
| Save File | Specifies the fully-qualified file path and name of the file to which runtime user configuration changes will be saved. Must include the .xml file extension and can use an @Function token.  Example: @Function.AppPhysicalPath~\SaveFiles\AFSaveFile.xml Example: [@Function.AppPhysicalPath](mailto:@Function.AppPhysicalPath)~\UserSaveFiles\@Function.UserName~.xml  Save files can also be stored in a database, see [Bookmarks](https://devnet.logianalytics.com/hc/en-us/articles/4406822405143-Bookmarks). |
| Security Right ID | When using Logi Security, specifies one or more Security Right IDs, separated by commas. Users with these Security Right IDs will be able to view the Analysis Chart, users without them will not. |
| Template Modifier File | Identifies a custom XML file developers can create containing elements that will override the same elements in the template file, for language- and culture-customization of captions. |
| Width | Specifies the width, in pixels, of the chart image. Does *not* include the Control Panel. Leave blank for a default size, which can vary by chart type and data. |
