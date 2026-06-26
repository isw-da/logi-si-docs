---
title: "REST \u2014 Data Objects"
id: 5281637743511
section: "REST Web Service API"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281637743511-REST-Data-Objects
updated_at: 2022-05-03T22:07:52Z
---

# REST — Data Objects

# REST — Data Objects

**Data Objects** (referred to as Entities internally and in the API) are the manner by which Exago views and accesses the tables, views, procedures, etc… from the **Data Sources**. Data objects represent the structure of the data, but the actual data is only accessed at report run-time.

## Data Object JSON

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> All requests require a [Session Id](https://devnet.logianalytics.com/hc/en-us/articles/5281669654679-REST-Sessions#Session) URL parameter and basic request headers. In the following topic, headers are omitted in the interest of brevity.

Data Objects are represented as JSON objects with the following properties:

| Name | Type | Writable | Description |
| --- | --- | --- | --- |
| Id | string | required-create | The unique Id of this data object |
| Name | string | required | The display name (“alias”) of this data object |
| Schema | string | yes | The schema of this data object |
| SchemaAccessType | string | yes | How Exago should retrieve the schema for the data object. There are three possibilities:  * *Default* — Follow the global **Schema Access Type** setting in [Other Settings](https://devnet.logianalytics.com/hc/en-us/articles/5281608505879-Other-Settings). * *Datasource* — Queries the data source for the schema. * *Metadata* — Reads the schema from the stored metadata. |
| CategoryName | string | yes | The Category/Folder group this object will appear in |
| DataName | string | required | The name of this data object in its data source red exclamation point The name of data objects may not contain the following characters:   ``` { } [ ] , . % ```   To create a data object for a database table (or other backing model) with one of these characters in its name, create a Custom SQL Object with a simple `SELECT` clause. For example for a table named `sales.figures.2020`:   ``` SELECT * FROM [sales.figures.2020] ```   Note that the identifier delimiters (the `[ ]`) around the table name will vary with the database type. |
| DataSourceId | integer | required | The Id of the data source of this data object (see **[Data Sources](https://devnet.logianalytics.com/hc/en-us/articles/5281617045911-Data-Sources)**) |
| DataType | enum | yes (“Table”) | **[DataObjectType](https://devnet.logianalytics.com/hc/en-us/articles/5281610137879-Constants-and-Enumerators#DataObje)** |
| SqlStatement | string | yes | The custom SQL of this data object if it’s **DataType** is *SqlStmt* |
| canreexecuteindb | Boolean | yes | See **[Interactive Filtering in Database v2021.1+](https://devnet.logianalytics.com/hc/en-us/articles/5281608202519-Data-Objects#Interact)** |
| Parameters | array of strings | yes | Any parameters for stored procedure, .NET Assembly or Web Service API calls |
| KeyColumns | array of strings | yes | The unique key fields of this data object |
| TenantColumns | array of **Ten****ant Column** | yes | The tenant fields of this data object |
| FilterDropdownObject | **Filter Dropdown** | yes | The filter dropdown object of this data object |

### Example

```
{
  "Id":            "Employees_0",
  "Name":          "Employees",
  "Schema":        "dbo",
  "CategoryName":  "",
  "DataName":      "Employees",
  "DataSourceId":  "0",
  "DataType":      "Table",
  "SqlStatement":  "",
  "canreexecuteindb": true,
  "Parameters":    [],
  "KeyColumns":    ["EmployeeID"],
  "TenantColumns": [
    {
      "Column":    "EmployeeID",
      "Parameter": "UserId"
    }
  ],
  "FilterDropdownObject": {
    "FilterDbName":       "Employee_List",
    "FilterDataSourceId": -1,
    "FilterObjectType":   "view",
    "FilterSchema":       "",
    "FilterSqlStmt":      ""
  }
}
```

## Tenant Column JSON

Tenant Columns are represented as JSON objects with the following properties:

| Name | Type | Writable | Description |
| --- | --- | --- | --- |
| Column | string | required | The tenant data field |
| Parameter | string | required | The tenant parameter |

### Example

```
"TenantColumns": [
    {
      "Column":    "EmployeeID",
      "Parameter": "UserId"
    }
]
```

## Filter Dropdown JSON

A Data Object’s Filter Dropdown is represented as a JSON object with the following properties:

| Name | Type | Writable | Description |
| --- | --- | --- | --- |
| FilterDbName | string | required | The name of this data object in its data source |
| FilterObjectType | enum | yes | **[DataObjectType](https://devnet.logianalytics.com/hc/en-us/articles/5281610137879-Constants-and-Enumerators#DataObje)** |
| FilterSchema | string | yes | The schema for this data object |
| FilterSqlStmt | string | yes | The custom SQL for this data object if it is of type SqlStmt |

### Example

```
"FilterDropdownObject": {
    "FilterDbName":       "Employee_List",
    "FilterObjectType":   "view",
    "FilterSchema":       "",
    "FilterSqlStmt":      ""
}
```

## Data Field JSON

Data fields for each object are represented as JSON objects with the following properties. The actual data in the fields is not accessible via REST. Data fields cannot be created or deleted. However, some metadata for existing fields can be edited.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> The **IsFilterable** property name changed to **Filterable** in *v2019.1.13*.

| Name | Type | Writable | Description |
| --- | --- | --- | --- |
| Id | string | no | The unique name for this data field |
| Name | string | yes | The display name for this data field |
| Type | enum | yes | **Data Field Type** |
| IsFilterable (*pre-2019.1.13*) Filterable (*v2019.1.13+*) | bool (*pre-v2017.2*) const (*v2017.2+*) | yes | Whether this field is filterable [Filterable Type](https://devnet.logianalytics.com/hc/en-us/articles/5281610137879-Constants-and-Enumerators#Filterab) |
| IsVisible | Boolean | yes | Whether this field is visible to end users. Set to *false* to hide it or *true* to show it. |
| Value | string | yes | The content of the data field. Enclose other Exago data fields in curly braces { }. There are three possibilities:   * *An Exago formula* — A custom function used to define the field value. Can use other fields from the same data object. (for example `“Concatenate({Orders.ShipCountry},'+ ',{Orders.ShipCity})”`) * *A SQL formula* — SQL statement used to define the field value. (for example `“Concat(ShipCountry, ' + ', ShipCity)”`) * *A static value* — Static content (for example “*12345*“) |
| Description | string | yes | A text description of the data field what will be shown to the end user |
| ColumnSource | string | yes | Describes the content of the **Value** property. Either:   * *Data* — use for either a static value, or when **Value** contains a single column name * *ExagoFormula* — use when the **Value** is an Exago formula * *SqlFormula* — use when the **Value** is a SQL formula |
| SortAndGroupBy | string | yes | Either an Exago formula or another data field name that will be used to sort/group the values in this column. Enclose column names in curly braces { }. If *null*, sorting/grouping on a field is not enabled. |

## List All Data Objects

List all the data objects in the current configuration. Output is an array of objects, each representing an individual data object.

```
GET /rest/Entities
```

| Name | Type | Description |
| --- | --- | --- |
| Id | string | The unique Id of this data object |
| Name | string | The display name (“alias”) of this data object |

### Using curl

```
curl http://{webservice}/rest/Entities?sid={sid} -X GET
```

### Example response

```
Status: 200 OK
[
  {
    "Id":   "Customers_0",
    "Name": "Customers"
  },
  {
    "Id":   "Employees_0",
    "Name": "Employees"
  },
  ...
]
```

## List Properties of a Single Data Object

Show the properties of the data object specified by its Id.

```
GET /rest/Entities/{Id}
```

### Using curl

```
curl http://{webservice}/rest/Entities/{Id}?sid={sid} -X GET
```

### Example response

```
Status: 200 OK

{
"Id":"system_departments_0",
"Name":"Departments",
"Schema":"",
"CategoryName":"Roster",
"DataName":"system_departments",
"DataSourceId":"4",
"DataType":"Table",
"SqlStatement":"",
"Parameters":[],
"KeyColumns":["id"],
"TenantColumns":[],
"FilterDropdownObject":null
}
```

## Add a New Data Object

```
POST /rest/Entities
```

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Requires a DataName or a custom SqlStatement. One or more KeyColumns are required for most data types.

### Using curl

```
curl http://{webservice}/rest/Entities?sid={sid} -X POST ^
	-d @newDataObject.txt
```

#### newDataObject.txt

```
 {
   "Id":"Employees_1",
   "Name":"Employees",
   "Schema":"dbo",
   "DataName":"Employees",
   "DataSourceId":0,
   "KeyColumns":[
      "EmployeeID"
   ]
}
```

### Example response

```
Status: 201 Created
Location: /{webservice}/rest/Entities/Employees_1

{
  "Id":            "Employees_1",
  "Name":          "Employees",
  "Schema":        "dbo",
  "CategoryName":  "",
  "DataName":      "Employees",
  "DataSourceId":  "0",
  "DataType":      "Table",
  "SqlStatement":  "",
  "Parameters":    [],
  "KeyColumns":    ["EmployeeID"],
  "TenantColumns": [],
  "FilterDropdownObject": null
}
```

## Edit a Data Object

Only supply the properties to be edited.

```
PATCH /rest/Entities/{Id}
```

### Using curl

```
curl http://{webservice}/rest/Entities/{Id}?sid={sid} -X PATCH ^
	-d "{'Name':'Staff List'}"
```

### Example response

```
Status: 204 No Content
```

## Delete a Data Object

```
DELETE /rest/Entities/{Id}
```

### Using curl

```
curl http://{webservice}/rest/Entities/{Id}?sid={sid} -X DELETE
```

### Example response

```
Status: 204 No Content
```

## List the Data Fields of a Data Object

List all the data fields in the data object specified by its Id. Output is an array of objects, each representing an individual data field.

```
GET /rest/Entities/{Id}/Fields
```

| Name | Type | Description |
| --- | --- | --- |
| Id | string | The unique Id of this data field |
| Name | string | The display name of this data field |

### Using curl

```
curl http://{webservice}/rest/Entities/{Id}/Fields?sid={sid} -X GET
```

### Example response

```
Status: 200 OK

[
  {
    "Id":   "Address",
    "Name": "Address"
  },
  {
    "Id":   "BirthDate",
    "Name": "Date of Birth"
  },
  {
    "Id":   "EmployeeID",
    "Name": "ID Number"
  },
  {
    "Id":   "FirstName",
    "Name": "First Name"
  },
  {
    "Id":   "LastName",
    "Name": "Last Name"
  },
  ...
]
```

## List Data Field Properties

List the properties of the data field specified by its Id, of the Data Object specified by its Id.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> Performing a GET for the data fields will result in fixing the current column metadata list as the only defined columns. The column metadata can be further altered, but will not be reflected in the Entity Columns collection until the session is launched in a browser.

```
GET /rest/Entities/{Id}/Fields/{Field Id}
```

### Using curl

```
curl http://{webservice}/rest/Entities/{Id}/Fields/{Field Id}?sid={sid} -X GET
```

### Example response

```
Status: 200 OK

{
  "Id":           "LastName",
  "Name":         "Last Name",
  "Type":         "String",
  "IsFilterable": true,
  "IsVisible":    true
}
```

## Add Data Field/Column Metadata

Add new metadata that doesn’t already exist to a data field/column.

```
POST /rest/Entities/{Id}/Fields/{Field Id}
```

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> Setting the **Type** property to a data type that does not match the actual type in the data source will cause errors when reports are run or designed.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> Adding additional column metadata will result in fixing the current column metadata list as the only defined columns. The column metadata can be further altered, but will not be reflected in the Entity Columns collection until the session is launched in a browser.

## Edit Data Field/Column Metadata

Only supply the properties to be edited.

```
PATCH /rest/Entities/{Id}/Fields/{Field Id}
```

### Using curl

```
curl http://{webservice}/rest/Entities/{Id}/Fields/{Field Id}?sid={sid} -X PATCH ^
	-d "{'Name':'Surname'}"
```

### Example response

```
Status: 204 No Content
```
