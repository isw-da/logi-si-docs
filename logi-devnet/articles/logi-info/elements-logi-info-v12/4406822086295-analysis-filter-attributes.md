---
title: "Analysis Filter - Attributes"
id: 4406822086295
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822086295-Analysis-Filter-Attributes
updated_at: 2022-04-06T06:03:07Z
---

# Analysis Filter - Attributes

# Analysis Filter - Attributes

The Analysis Filter element has the following attributes:

| Attribute | Description |
| --- | --- |
| ID | (Required) Specifies a unique identifier for this element. |
| Case Sensitive | Specifies whether comparisons will be case-sensitive. For elements using DataLayer.ActiveSQL, this attribute value may be set to *DataSourceCollation*, causing case-sensitivity to be defined by the database column's "collation", which may be case-sensitive or not. This option can provide better performance for case-insensitive filters.  For an Analysis Filter used with DataLayer.Active SQL and Sql Compare Filter elements, the default is *DataSourceCollation*. The default is *True* for all other elements. |
| Disable Design View | Specifies whether to display the filter in Design view mode. This allows the user full control of filter *creation* and updates. Normally, a report run without an Analysis Filter Save File specified initially appears in Design view. When redisplayed, the report's Analysis Filter appears in Simple view.  Disabling Design view causes the Analysis Filter to appear only in the Simple view.  Default Value: *False.* |
| Disable Simple View | Specifies whether to display the filter in Simple view mode. This allows the user to do easy updates of existing filters. Normally, a report run without an Analysis Filter Save File specified initially appears in Design view. When redisplayed, the report's Analysis Filter appears in Simple view.  Disabling Simple view causes the Analysis Filter to appear only in Design view.  Default Value: *False.* |
| Filter Caption Element ID | Specifies the ID a Label element that will display a one-line description of the filter(s) in use, allowing filtering criteria to be shown anywhere in the report page. To use it, add a Label element to the report and give it a unique ID, leave its Caption attribute blank, and specify its ID in this attribute. The Label's Caption will be filled at runtime with the filter's description/caption. For example: [Customer ID] = VINET |
| Filter List Location | Specifies whether, when using the Design view, the list of defined filters appears beneath the input controls or beside them to the right. This allows management of the space the filter uses.  Default Value: *Bottom* (beneath the controls) |
| No Filters Simple Caption | Specifies text to be displayed in Simple view when no filters have been defined.  Default value: *(No filters)* |
| Refresh Element IDs | Specifies, in a comma-separated list, the IDs of the elements to be refreshed within the page, using AJAX, when a filter is checked or unchecked or a filter definition or value is changed. If left blank, then the entire page will be refreshed when a filter value changes. |
| Request Forwarding | Set to *True* to pass all request parameters received by this page to the next page. Values set using a Default Request Values element are not forwarded. Default value: *False*.  Request parameters cannot be forwarded if there is an Input element with the same name on the page, because this would result in an attempt to pass two values with the same name. |
| Save File | Specifies the fully-qualified file path and name of an XML file where user runtime filter changes will be saved. Must include the .xml file extension and can use an @Function token.   Example: @Function.AppPhysicalPath~\Filters\AFSaveFile.xml Example: [@Function.AppPhysicalPath](mailto:@Function.AppPhysicalPath)~\UserFilters\@Function.UserName~.xml  Save files can also be stored in a database, see [Bookmarks](https://devnet.logianalytics.com/hc/en-us/articles/4406822405143-Bookmarks). |
| Save File Starter | Specifies the fully-qualified file path and name of an XML file to be used as the initial Save File in cases when the Save File does not exist yet. For example, when the Save File is different for each user, the Save File Starter file can include a set of default filters.  Create a Save File Starter file by setting a Save File value, then defining filters to create the desired default set, then moving and/or renaming the Save File into the Save File Starter location.  Example: @Function.AppPhysicalPath~\Filters\InitialFilters.xml |
| Security Right ID | If specified, access to this element is controlled via Logi security. Specify the ID of a Right defined in the application's settings/security section. Only users that Right will be able to see the element. Multiple Right IDs may be entered in a comma-separated list. In that case, the element will be visible to users with any one of the Rights specified. |
| Template Modifier File | Specifies the full name of a template modifier file to be used to alter the Analysis Filter element. See [Analysis Filter - Using the Analysis Filter Elements](https://devnet.logianalytics.com/hc/en-us/articles/4406816973591-Analysis-Filter-Using-the-Analysis-Filter-Elements) for more information about template modifiers. The template modifier file can be in any folder accessible to the web application; if a fully-qualified file path is not provided in this attribute value, then the application expects it to be in your project's \_SupportFiles folder. |

The columns that can be selected in the Design view control panel when creating filters are defined by **Analysis Filter Column** elements, one per column, that are added as children of the Analysis Filter element.
