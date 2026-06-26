---
title: "REST \u2014 Role Security"
id: 5281652540567
section: "REST Web Service API"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281652540567-REST-Role-Security
updated_at: 2022-05-03T22:07:49Z
---

# REST — Role Security

# REST — Role Security

Roles are collections of security settings for users of the application. They are used to distinguish classes of users by access rights. Setting an active role will cause it to take effect for the application session, once the AppUrl is launched in the browser. Once in an application session, the active role cannot be changed. Only one role can be active at a time.

Roles do not affect access to the API.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> All requests require a [Session Id](https://devnet.logianalytics.com/hc/en-us/articles/5281669654679-REST-Sessions#Session) URL parameter and basic request headers. In the following topic, headers are omitted in the interest of brevity.

## Role JSON

A role’s base status is represented as a JSON object with the following properties:

| Name | Type | Writable | Description |
| --- | --- | --- | --- |
| Id | string | required-create | The unique Id of this role |
| IsActive | Boolean | yes (true) | Whether this role is active |

#### Example

```
{
  "Id":       "Client",
  "IsActive": false
}
```

## List Roles

List all the roles in the current configuration. Output is an array of objects, each representing an individual role.

```
GET /rest/Roles
```

| Name | Type | Description |
| --- | --- | --- |
| Id | string | The unique Id of this role |

#### Using curl

```
curl http://{webservice}/rest/Roles?sid={sid} -X GET
```

#### Example response

```
Status: 200 OK

[
  {
    "Id":   "Admin"
  },
  {
    "Id":   "Client"
  },
  ...
]
```

## Create a Role

Creating a new role activates it by default.

```
POST /rest/Roles
```

#### Using curl

```
curl http://{webservice}/rest/Roles?sid={sid} -X POST ^
	-d "{'Id':'User'}"
```

#### Example response

```
Status: 201 Created
Location:/{webservice}/rest/Roles/User

{
  "Id":       "User",
  "IsActive": true
}
```

## Show Role Status

```
GET /rest/Roles/{Id}
```

#### Using curl

```
curl http://{webservice}/rest/Roles/{Id}?sid={sid} -X GET
```

#### Example response

```
Status: 200 OK

{
  "Id":       "User",
  "IsActive": true
}
```

## Activate or Deactivate a Role

Only supply the properties to be edited.

```
PATCH /rest/Roles/{Id}
```

#### Using curl

```
curl http://{webservice}/rest/Roles/{Id}?sid={sid} -X PATCH ^
	-d "{'IsActive':false}"
```

#### Example response

```
Status: 204 No Content
```

## Delete a Role

```
DELETE /rest/Roles/{Id}
```

#### Using curl

```
curl http://{webservice}/rest/Roles/{Id}?sid={sid} -X DELETE
```

#### Example response

```
Status: 204 No Content
```

## Role Settings JSON

Each role has a group of settings that may be used to override the base config. Each key corresponds with a setting in the Admin Console, which is noted in the Description field. If a setting is blank or null, then the value from the base config is not overridden for this role. The settings are represented as a JSON object with the following properties:

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> All properties are read/write. No properties are required. Default values are inherited from the base config.

| Name | Type | Description |
| --- | --- | --- |
| ReportPath | string | Report Path |
| LanguageFile | string | Language File |
| ServerTimeZoneOffset | integer | Server Time Zone Offset |
| ReadFilterValues | Boolean | Read Database for Filter Values |
| DbTimeout | integer | Database Timeout |
| ScheduleManagerViewLevel | enum | [ScheduleManagerViewLevel](https://devnet.logianalytics.com/hc/en-us/articles/5281610137879-Constants-and-Enumerators#Schedule) |
| DateFormat | string | Date Format |
| TimeFormat | string | Time Format |
| DateTimeFormat | string | DateTime Format |
| SeparatorSymbol | string | Numeric Separator Symbol |
| CurrencySymbol | string | Numeric Currency Symbol |
| ShowGrid | Boolean | Show Grid Lines in Report Viewer |
| ShowCrossTabReports | Boolean | Allow Creation/Editing of CrossTab Reports |
| ShowExpressReports | Boolean | Allow Creation/Editing of Express Reports |
| ShowExpressReportsGrouping | Boolean | Show Grouping in the Express Report Designer |
| ShowExpressReportsFormulas | Boolean | Show Formula Button in the Express Report Designer |
| AllowReportCustomSQLObjects v2018.1+ | Boolean | Allow Creation of Custom SQL Objects in Advanced Reports |
| ShowExpressReportsStyling | Boolean | Show Styling Toolbar in the Express Report Designer |
| ShowExpressReportsThemes | Boolean | Show Themes in the Express Report Designer |
| ShowScheduleReports | Boolean | Show report scheduling options |
| ShowScheduleReportsManager | Boolean | Show Schedule Manager in the main menu |
| ShowScheduleReportsEmail | Boolean | Show Email Report Options |
| DecimalSymbol | string | Numeric Decimal Symbol |

The following settings have been added to versions *v2018.1.27+*, *v2018.2.16+*, *2019.1.2+* of Exago:

| Name | Type | Description |
| --- | --- | --- |
| ShowAdvancedReports | Boolean | Allow Creation/Editing of Advanced Reports |
| ShowDashboardReports | Boolean | Allow Creation/Editing of Dashboard Reports |
| ShowDashboardNewVisualizationButton | Boolean | Allow Creation/Editing of Dashboard Visualizations |
| ShowExpressViews | Boolean | Allow Creation/Editing of ExpressViews |
| AllowExpressViewLiveEdit | Boolean | Allow Editing ExpressView with Live Data |
| ShowChainedReports | Boolean | Allow Creation/Editing of Chained Reports |
| CacheVisibilityLevel | wrCacheVisibility | [Cache Visibility Level](https://devnet.logianalytics.com/hc/en-us/articles/5281610137879-Constants-and-Enumerators#Cache) |

#### Example

```
{
  "ReportPath":                 "C:\\Exago\\Reports",
  "LanguageFile":               null,
  "ServerTimeZoneOffset":       0,
  "ReadFilterValues":           true,
  "DbTimeout":                  0,
  "ScheduleManagerViewLevel":   "All",
  "DateFormat":                 "MM/dd/yyyy",
  "TimeFormat":                 "hh:mm:ss a",
  "DateTimeFormat":             "MM/dd/yyyy hh:mm:ss a",
  "SeparatorSymbol":            ",",
  "CurrencySymbol":             "$",
  "ShowGrid":                   true,
  "ShowCrossTabReports":        true,
  "ShowExpressReports":         true,
  "ShowExpressReportsGrouping": true,
  "ShowExpressReportsFormulas": true,
  "ShowExpressReportsStyling":  true,
  "ShowExpressReportsThemes":   true,
  "ShowAdvancedReports":        true,
  "ShowDashboardReports":       true,
  "ShowDashboardNewVisualizationButton": true,
  "ShowExpressViews":           true,
  "AllowExpressViewLiveEdit":   true,
  "ShowChainedReports":         true,
  "CacheVisibilityLevel":       "Global",
  "ShowScheduleReports":        true,
  "ShowScheduleReportsManager": true,
  "ShowScheduleReportsEmail":   true,
  "DecimalSymbol":              "."
}
```

## Show Role Settings

Show the settings for the role specified by its Id.

```
GET /rest/Roles/{Id}/Settings
```

#### Using curl

```
curl http://{webservice}/rest/Roles/{Id}/Settings?sid={sid} -X GET
```

#### Example response

```
Status: 200 OK

{
  "ReportPath":                 "C:\\Exago\\Reports",
  "LanguageFile":               null,
  "ServerTimeZoneOffset":       0,
  "ReadFilterValues":           true,
  "DbTimeout":                  0,
  "ScheduleManagerViewLevel":   "All",
  "DateFormat":                 "MM/dd/yyyy",
  "TimeFormat":                 "hh:mm:ss a",
  ...
}
```

## Edit Role Settings

Only supply the properties to be edited.

```
PATCH /rest/Roles/{Id}/Settings
```

#### Using curl

```
curl http://{webservice}/rest/Roles/{Id}/Settings?sid={sid} -X PATCH ^
	-d "{'ShowAdvancedReports':false}"
```

#### Example response

```
Status: 204 No Content
```

## Folder Permissions JSON

Each role has a set of folder permissions which allow or disallow access to folders for the current session. The permissions are represented as a JSON object with the following properties:

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> All properties are read/write. No properties are required.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> For the best user experience, keep the number of items in the Report Tree less than 1000.

| Name | Type | Description |
| --- | --- | --- |
| IncludeAll | Boolean | If *True*, all folders are visible to this role except the ones specified in Folders. If *False*, only the folders specified in Folders are visible to this role. |
| ReadOnly | Boolean | If *True*, all folders are read-only except the folders marked ReadOnly = ‘true’. If *false*, only the folders marked ReadOnly = ‘true’ are read-only. |
| AllowManagement | Boolean | If *True*, users will be able create, rename and delete folders via the user interface. If *False*, users cannot take action on folders and the Add Folder buttons are hidden from the user interface. |
| CreateFolders | Boolean | If *True*, when adding Folders to the Role via the API, Exago will check if the folder exists and add it if not. If *False* no check will be performed. Once the session is launched, this property no longer applies. |
| Folders | array of [Folder JSON](#Folder) | The folders with properties specific to this role |

### Folder JSON

Each folder in the Folders property is represented as a JSON object with the following properties:

| Name | Type | Description |
| --- | --- | --- |
| Name | string | Full path from the root folder to this folder |
| ReadOnly | Boolean | Whether this folder is ReadOnly |
| Propagate | Boolean | Whether this folder’s subfolders share its ReadOnly property |

#### Example

```
{
  "IncludeAll":      false,
  "ReadOnly":        false,
  "AllowManagement": true,
  "CreateFolders":   false,
  "Folders": [
    {
      "Name":      "ExamplesClient",
      "ReadOnly":  true,
      "Propagate": true
    }
  ]
}
```

## List Folder Permissions

Show the folder permissions for the role specified by its Id.

```
GET /rest/Roles/{Id}/Folders
```

#### Using curl

```
curl http://{webservice}/rest/Roles/{Id}/Folders?sid={sid} -X GET
```

#### Example response

```
Status: 200 OK

{
  "IncludeAll":      false,
  "ReadOnly":        false,
  "AllowManagement": true,
  "CreateFolders":   false,
  "Folders": [
    {
      "Name":      "Examples",
      "ReadOnly":  true,
      "Propagate": true
    }
  ]
}
```

## Edit Folder Permissions

Only supply the properties to be edited. Supplying a Folders property will overwrite the entire collection.

```
PATCH /rest/Roles/{Id}/Folders
```

#### Using curl

```
curl http://{webservice}/rest/roles/{Id}/folders?sid={sid} -X PATCH ^
	-d "{'ReadOnly':true}"
```

#### Example response

```
Status: 204 No Content
```

## Data Object Permissions JSON

Each role has a set of data object permissions which allow or disallow access to data objects for the current session. The permissions are represented as a JSON object with the following properties:

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> All properties are read/write. No properties are required.

| Name | Type | Description |
| --- | --- | --- |
| IncludeAll | Boolean | If *true*, all data objects are available to this role except the ones specified in Entities. If *false*, only the data objects specified in Entities are visible to this role. |
| Entities | array of **Data Object** | The data objects with properties specific to this role |

### Data Object JSON

Each Data Object in the Entities property is represented as a JSON object with the following properties:

| Name | Type | Description |
| --- | --- | --- |
| Id | string | The unique Id of this data object |

#### Example

```
{
  "IncludeAll": true,
  "Entities": [
    {
      "Id": "EMP"
    },
    {
      "Id": "ETE"
    }
  ]
}
```

## List Data Object Permissions

Show the data object permissions for the role specified by its Id.

```
GET /rest/Roles/{Id}/Entities
```

#### Using curl

```
curl http://{webservice}/rest/Roles/{Id}/Entities?sid={sid} -X GET
```

#### Example response

```
Status: 200 OK

{
  "IncludeAll": false,
  "Entities": [
    {
      "Id": "EMP"
    }
  ]
}
```

## Edit Data Object Permissions

Only supply the properties to be edited. Supplying an Entities property will overwrite the entire collection.

```
PATCH /rest/Roles/{Id}/Entities
```

#### Using curl

```
curl http://{webservice}/rest/roles/{Id}/entities?sid={sid} -X PATCH ^
	-d "{'IncludeAll':false}"
```

#### Example response

```
Status: 204 No Content
```

## Row Filters JSON

Add security filters to data objects so that users can only view specific rows in the data object. The collection of row filters for this role is represented as a JSON object with the following properties:

| Name | Type | Description |
| --- | --- | --- |
| DataObjectRows | array of **Row Filter** | The row filters for this role |

### Row Filter JSON

Each row filter in the **DataObjectRows** property is represented as a JSON object with the following properties:

| Name | Type | Description |
| --- | --- | --- |
| Id | string | The Id of the data object to filter |
| Filter | string | The filter string. The filter string should be valid, standard SQL to be added to the ‘WHERE’ clause sent to the Data Source. This filter string can include Exago system parameters (for example @userId@) or custom SQL including subqueries (for example `IN (SELECT EmployeeID FROM Employees WHERE EmployeeID <4)`). The **Filter String** must contain the actual name of objects in the Data Source (for example tables, views, columns, etc…) rather than their Exago aliases. |

#### Example

```
{
  "DataObjectRows": [
    {
      "Id":     "EMP",
      "Filter": "EmployeeID = 1"
    },
    {
      "Id":     "ETE",
      "Filter": "EmployeeID = 2"
    }
  ]
}
```

## List Row Filters

Show the row filters for the role specified by its Id.

```
GET /rest/Roles/{Id}/DataObjectRows
```

#### Using curl

```
curl http://{webservice}/rest/Roles/{Id}/DataObjectRows?sid={sid} -X GET
```

#### Example response

```
Status: 200 OK

{
  "DataObjectRows": [
    {
      "Id":     "EMP",
      "Filter": "EmployeeID = 3"
    },
    ...
  ]
}
```

## Edit Row Filters

This will overwrite the entire filter collection.

```
PATCH /rest/Roles/{Id}/DataObjectRows
```

#### Using curl

```
curl http://{webservice}/rest/Roles/{Id}/DataObjectRows?sid={sid} -X PATCH ^
	-d "{'DataObjectRows':[{'Id':'EMP','Filter':'Client'}]}"
```

#### Example response

```
Status: 204 No Content
```
