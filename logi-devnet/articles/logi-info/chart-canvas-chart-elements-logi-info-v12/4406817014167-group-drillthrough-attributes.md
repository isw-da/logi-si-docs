---
title: "Group Drillthrough Attributes"
id: 4406817014167
section: "Chart Canvas Chart Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817014167-Group-Drillthrough-Attributes
updated_at: 2022-04-06T06:03:21Z
---

# Group Drillthrough Attributes

# Group Drillthrough Attributes

The Group Drillthrough element has the following attributes:

| Attribute | Description |
| --- | --- |
| ID | (Required) Specifies a unique element ID. |
| Caption | Specifies the text of a caption that will appear at the top of the detail report. |
| Export | Specifies which exports will be available in the detail report, in a comma-separated list. Options include *CSV, Excel*, and *PDF*. The default value is *no exports*, which hides the Export icon. |
| Frame ID | Specifies the target window for the detail report. Leave blank for the current browser window, or enter NewWindow to open a new browser window. You can also specify an existing FrameID to re-use the same window for each request. |
| Group Filter ID | Specifies the unique element ID of the Group Filter element used to group the data that will be shown in the detail report. Provides differentiation when multiple Group Drillthrough elements are being used beneath multiple Series elements. May be left blank if there's just one Group Filter in the report. |
| Image | This attribute is ignored when the element is used with Chart Canvas Charts. |
| Security Right ID | If entered, controls access to this element via Logi security. Supply the ID of a Right defined in the application's settings/security section. Only users that have a Role referenced in the Right will be able to see the element. (Be careful - when the Right is not defined in the settings, the element is visible.) Multiple Right IDs, separated by commas may be entered. In this case, the user will see the element if he has access to any one of the Rights. |
| Show Modes | Specifies a text string that controls whether elements will be displayed or hidden. Leave this blank for the element to always be displayed or set it to None to hide it (it can be displayed again later with an Action.Show Element element). Set it to your own string value to have it appear only when the report's (root element's) Show Modes includes that value. Show Modes can contain multiple, comma-delimited values. |
| Template Modifier File | Specifies the name of an optional Template Modifier File, used to programmatically modify the Report Author super-element UI or behavior at runtime. See [Customizing Detail Report Columns](https://devnet.logianalytics.com/hc/en-us/articles/4406817013143-Customizing-Detail-Report-Columns) for more information about template modifiers. You can provide a fully-qualified file path and name for the file, within the application root folder or, if a fully-qualified file path is not provided, the application expects the file to be in its \_SupportFiles folder. |
