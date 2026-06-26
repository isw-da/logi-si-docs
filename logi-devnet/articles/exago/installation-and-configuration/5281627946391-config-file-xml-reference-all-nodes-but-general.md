---
title: "Config File XML Reference (All Nodes but General)"
id: 5281627946391
section: "Installation and Configuration"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281627946391-Config-File-XML-Reference-All-Nodes-but-General
updated_at: 2024-11-14T19:10:11Z
---

# Config File XML Reference (All Nodes but General)

# Config File XML Reference (All Nodes but General)

This reference guide describes the structure of the config file XML elements. Use this guide if you build or edit the config XML directly, without using the **Admin Console**.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/25323356730135 "Tip")
>
> For the settings nodes within `<general></general>`, see [Config File XML & API Setting Reference (General Nodes)](https://devnet.logianalytics.com/hc/en-us/articles/5281643841175-Config-File-XML-API-Setting-Reference-General-Nodes-).

The config file’s outer nodes are as follows:

```
<?xml version="1.0" standalone="yes"?>
<webreports>
</webreports>
```

All following nodes are within the `<webreports>` element. They are organized below in alphabetical order, not necessarily the order they appear in the configuration file.

## How to Use This Document

XML objects are represented in tables with the following format:

| Node | Description | Type | Required |
| --- | --- | --- | --- |

**Node** is the XML node name. Nodes in **bold font** are objects, which are represented below the table.

**Description** is the name of the field as it appears in the **Admin Console**. If there is no mapped field, or the field is implicit, the description is in *italic font*.

**Type** is the value type. If the type is a constant or enum, the possible values are listed below the table. Constants are case sensitive.

**Required** indicates whether the node requires a value. (1+) indicates that there can be multiple nodes.

## Action Events

The [Introduction to Action Events](https://devnet.logianalytics.com/hc/en-us/articles/5281598603671-Introduction-to-Action-Events) topic includes detailed descriptions of each of these settings.

Outer node: `<actionevent></actionevent>`

| Node | Description | Type | Required |
| --- | --- | --- | --- |
| name | Name | string | yes |
| id | *Unique Id* | int | yes |
| event\_type | Global Event Type | constant | yes |
| datasource\_id | *Id of assembly data source* | int | no |
| func\_name | *Assembly function name* | string | no |
| user\_action | Event Type | constant | yes |
| language | Language | constant | no |
| program\_code | *Program code* | string | no |
| **uiaction** | Assigned UI Item(s) | object | no (1+) |
| **reference** | References | object | no (1+) |
| **namespace** | Namespaces | object | no (1+) |

Possible values for **event\_type**: *None*, or see [Global Action Events](https://devnet.logianalytics.com/hc/en-us/articles/5281621334167-Global-Action-Events)

Possible values for **user\_action**: *None, Load, Click*

Possible values for **language**: *CSharp, JavaScript, VB*

### uiaction

| Node | Description | Type | Required |
| --- | --- | --- | --- |
| element\_id | *Element Id* | constant | yes |

Possible values for **element\_id**: See [Actionable UI Elements](https://devnet.logianalytics.com/hc/en-us/articles/5281613121175-Actionable-UI-Elements)

### reference

| Node | Description | Type | Required |
| --- | --- | --- | --- |
| name | *Reference name* | string | yes |

### namespace

| Node | Description | Type | Required |
| --- | --- | --- | --- |
| name | *Namespace name* | string | yes |

### Example

```
<actionevent>
  <name>DoubleClick</name>
  <id>0</id>
  <event_type>OnDoubleClickReport</event_type>
  <user_action>Click</user_action>
  <language>CSharp</language>
  <program_code>return Extensions.ActionEvents.DoubleClick(sessionInfo);</program_code>
  <uiaction>
    <element_id>RunReportBtn</element_id>
  </uiaction>
  <reference>
    <name>Extensions.dll</name>
  </reference>
</actionevent>
```

## Custom Options

The [Custom Options](https://devnet.logianalytics.com/hc/en-us/articles/5281625285911-Custom-Options) topic includes detailed descriptions of each of these settings.

Outer node: `<customoption></customoption>`

| Node | Description | Type | Required |
| --- | --- | --- | --- |
| option\_id | Id | string | yes |
| option\_type | Type | constant | yes |
| **option\_list\_item** | *Option list item* | object | no (1+) |

Possible values for **option\_type**: *Int, Decimal, Bool, Text, List*

### option\_list\_item

| Node | Description | Type | Required |
| --- | --- | --- | --- |
| option\_list\_item\_id | *List item Id* | string | yes |

### Example

```
<customoption>
  <option_id>Hello</option_id>
  <option_type>List</option_type>
  <option_list_item>
    <option_list_item_id>World</option_list_item>
  </option_list_item>
</customoption>
```

## Data Sources

The [Data Sources](https://devnet.logianalytics.com/hc/en-us/articles/5281617045911-Data-Sources) topic includes detailed descriptions of each of these settings.

Outer node: `<datasource></datasource>`

| Node | Description | Type | Required |
| --- | --- | --- | --- |
| id | *Unique Id* | int | yes |
| name | Name | string | yes |
| dbtype | Type | constant | yes |
| dataconnstr | Connection String | string | yes |
| schema | Schema/Owner Name | string | no |
| odbcdelim | Column Delimiter(s) | string | no |

Possible values for **dbtype**: *mssql, oracle, msolap, odbc, websvc, assembly, mysql, file, postgres, db2, informix, cdata*

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/25323340497175 "Critical") **Important:**
>
> As of v2024.1.2, CData drivers are no longer available for use in Exago BI products. See **[CData Drivers](https://devnet.logianalytics.com/hc/en-us/articles/5281585000599)**.

### Example

```
<datasource>
  <id>0</id>
  <name>Northwind</name>
  <dbtype>odbc</dbtype>
  <schema>dbo</dbtype>
  <dataconnstr>DRIVER=SQLite3 ODBC Driver;Database=C:Northwind.sqlite;</dataconnstr>
  <odbcdelim>`</odbcdelim>
</datasource>
```

## Data Objects

The [Data Objects](https://devnet.logianalytics.com/hc/en-us/articles/5281608202519-Data-Objects) topic includes detailed descriptions of each of these settings.

When a Data Object is a clone of another only the id, entity\_name, cloned\_from, inherit\_category and inherit\_description, category, object\_description and db\_name apply.

Outer node: `<entity></entity>`

| Node | Description | Type | Required |
| --- | --- | --- | --- |
| id | Id | string | no |
| entity\_name | Alias | string | no |
| cloned\_from | v2019.1+*`<id>` of the parent data object that this one is a clone of.* | string | no |
| inherit\_category | v2019.2.18+ Inherit Folder *For cloned data objects, true if the category/folder the object appears in should be copied from its parent. False if the clone should have its own category folder. If false, `<category>` must be provided.* | Boolean | no |
| inherit\_description | v2019.2.18+ Inherit Description *For cloned data objects, true if the description of the clone should be copied from its parent. False if the clone should have its own description. If false, `<object_description>` must be provided.* | Boolean | no |
| db\_name | Name *For cloned data objects, a value here overrides the object in the Data Source (that is table, view) this clone points to while continuing to use the same metadata as its `cloned_from` object.* | string | yes |
| sql\_stmt | Custom SQL Object | string | no |
| object\_description | Description | string | no |
| category | Category | string | no |
| datasource\_id | *Id of data source* | int | yes |
| object\_type | *Object type* | constant | yes |
| schema\_access\_type | Schema Access Type | constant | no |
| **key** | Unique Key Fields | object | yes (1+) |
| **param** | Parameters | object | no (1+) |
| **tenant** | Tenant Columns | object | no (1+) |
| **filter\_dropdown** | Filter Dropdown Object | object | no |
| **column\_metadata** | Column Metadata | object | no (1+) |
| **transform** | *Vertical table transform* | object | no |
| affinity | v2018.1+ Report or config affinity | constant | no |
| suppress\_sort\_filter | v2018.1+Suppress Sort and Filter | Boolean | no |
| canreexecuteindb | v2021.1 Interactive Filtering in Database | Boolean | no |

Possible values for **object\_type**: *table, view, procedure, function, assembly, sqlstmt, websvc, file*

Possible values for **schema\_access\_type**: *Metadata, Datasource*

Possible values for **affinity**: *Global, Report*

### key

| Node | Description | Type | Required |
| --- | --- | --- | --- |
| col\_name | *Column name* | string | yes |

### param

| Node | Description | Type | Required |
| --- | --- | --- | --- |
| id | *Parameter name* | string | yes |

### tenant

| Node | Description | Type | Required |
| --- | --- | --- | --- |
| col\_name | *Column name* | string | yes |
| parameter\_id | *Parameter name* | string | yes |

### filter\_dropdown

| Node | Description | Type | Required |
| --- | --- | --- | --- |
| db\_name | *Data object name* | string | yes |
| sql\_stmt | *SQL statement* | string | no |
| datasource\_id | *Id of data source* | int | yes |
| object\_type | *Object type* | constant | yes |

Possible values for **object\_type**: *table, view, procedure, function, assembly, sqlstmt, websvc, file*

### column\_metadata

| Node | Description | Type | Required |
| --- | --- | --- | --- |
| col\_source | *Specify as custom col* | constant | no |
| col\_name | *Column name* | string | yes |
| col\_description | Column Description | string | no |
| col\_type | Data Type | constant | no |
| col\_alias | Column Alias | string | no |
| visible | Visible | bool | no |
| filterable | Filterable | constant | no |
| sortable | Sortable | bool | no |
| col\_sortandgroupbyvalue | Sort and Group-By Value | string | no |
| col\_value | Column Value | string | no |

Possible values for **col\_source**: *ExagoFormula*

Possible values for **col\_type**: *string, date, datetime, time, int, decimal, image, float, Boolean, guid, currency*

Possible values for **filterable**: *All, Dynamic, Static, None*

### transform

| Node | Description | Type | Required |
| --- | --- | --- | --- |
| col\_name | *Data field names column* | string | yes |
| val\_name | *Data values column* | string | yes |
| datatype\_name | *Data types column* | string | no |
| **non\_transform\_col** | *Fields exempt from transform* | object | no |

### non\_transform\_col

| Node | Description | Type | Required |
| --- | --- | --- | --- |
| col\_name | *Data field name* | string | yes |
| data\_type | *Data type* | enum | no |

Possible values for **data\_type**: 0: string, 1: date, 2: datetime, 3: time, 4: integer, 5: decimal, 6: float, 7: bit, 8: guid, 9: image, 10: currency

### Example

```
<entity>
  <id>ODE</id>
  <entity_name>OrderDetails</entity_name>
  <db_name>OrderDetail</db_name>
  <sql_stmt>SELECT *</sql_stmt>
  <category>Order Information</category>
  <datasource_id>1</datasource_id>
  <object_type>table</object_type>
  <key>
    <col_name>OrderId</col_name>
  </key>
  <key>
    <col_name>ProductId</col_name>
  </key>
  <param>
    <id>count</id>
  </param>
  <tenant>
    <col_name>CategoryName</col_name>
    <parameter_id>count</parameter_id>
  </tenant>
  <filter_dropdown>
    <db_name>Category</db_name>
    <sql_stmt>SELECT *</sql_stmt>
    <datasource_id>-1</datasource_id>
    <object_type>table</object_type>
  </filter_dropdown>
  <column_metadata>
    <col_source>ExagoFormula</col_source>
    <col_name>Total</col_name>
    <col_type>currency</col_type>
    <col_alias>Total</col_alias>
    <filterable>false</filterable>
    <col_value>{ODE.Quantity}*({ODE.UnitPrice}-{ODE.Discount})</col_value>
  </column_metadata>
  <column_metadata>
    <col_name>UnitPrice</col_name>
    <col_type>currency</col_type>
  </column_metadata>
</entity>
```

## Functions

The following topics include detailed descriptions of each of these settings

* [Custom Functions](https://devnet.logianalytics.com/hc/en-us/articles/5281628193815-Custom-Functions)
* [Custom Filter Functions](https://devnet.logianalytics.com/hc/en-us/articles/5281644078487-Custom-Filter-Functions)
* [Custom Aggregate Functions](https://devnet.logianalytics.com/hc/en-us/articles/5281616754327-Custom-Aggregate-Functions)

Outer node: `<function><function>`

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/25323356730135 "Note")
>
> Functions and Filter Functions use the same XML syntax. Filter functions have weight > 0 (which indicates its order in the filter list).

| Node | Description | Type | Required |
| --- | --- | --- | --- |
| name | Name | string | yes |
| description | Description | string | no |
| category | Category | constant | no |
| min\_args | pre-v2017.2 Minimum Number of Arguments | int | no |
| max\_args | pre-v2017.2 Maximum Number of Arguments | int | no |
| arguments\_json | v2017.2+*Arguments information* | ***json*** object | yes |
| variable\_arguments | v2017.2+ Variable Argument Count | bool | yes |
| available\_in | *Formula*, *filter* or *custom aggregate* | enum | yes |
| filter\_return\_type | Filter Type | constant | no |
| weight | List Order | int | yes |
| language | Language | constant | yes |
| program\_code | *Program Code* | string | yes |
| disable\_database\_grouping | v2019.1.5+ Prevent In-Database Grouping When Included in Detail Section | bool | yes |
| **reference** | References | object | no (1+) |
| **namespace** | Namespaces | object | no (1+) |

Possible values for **category**: *Aggregate, Operators, Logical, Date, Financial, Database, Arithmetic, String, Formatting, Other*

Possible values for **available\_in**:

0. Unavailable
1. Formula
2. Filter
3. Aggregate

Possible values for **filter\_return\_type**: *date, string, integer, decimal*

Possible values for **language**: *CSharp, JavaScript, VB*

### reference

| Node | Description | Type | Required |
| --- | --- | --- | --- |
| name | *Reference name* | string | yes |

### namespace

| Node | Description | Type | Required |
| --- | --- | --- | --- |
| name | *Namespace name* | string | yes |

### arguments\_json v2017.2+

A JSON formatted array of objects with the following format:

| Node | Description | Type | Required |
| --- | --- | --- | --- |
| Name | Name | string | yes |
| Required | Required | bool | yes |
| Description | Description | string | yes |

### Example

```
<function>
  <name>IncrementBy</name>
  <description>Count up by value steps.</description>
  <category>Other</category>
  <arguments_json>[{"Name":"counter","Required":false,"Description":"Number to increment by. Default: 1."}]</arguments_json>
  <variable_arguments>false</variable_arguments>
  <available_in>1</available_in>
  <filter_return_type>String</filter_return_type>
  <weight>0</weight>
  <language>CSharp</language>
  <program_code>return Extensions.CustomFunctions.IncrementBy(sessionInfo, args);</program_code>
  <reference>
    <name>Extensions.dll</name>
  </reference>
</function>
```

## Joins

The [Join Configuration](https://devnet.logianalytics.com/hc/en-us/articles/5281644535703-Join-Configuration) topic includes detailed descriptions of each of these settings.

Outer node: `<join></join>`

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/25323356730135 "Note")
>
> For entity names, use Id if set, otherwise use db\_name.

| Node | Description | Type | Required |
| --- | --- | --- | --- |
| entity\_from\_name | *From object (left)* | string | yes |
| entity\_to\_name | *To object (right)* | string | yes |
| join\_type | Join Type | constant | yes |
| relation\_type | Relation Type | constant | yes |
| weight | Weight | int | yes |
| **joincol** | pre-v2017.2 Join Columns | object | yes (1+) |
| **clause** | v2017.2+ Join Clause | object | yes (1+) |
| affinity | v2018.1+*Join affinity* | constant | yes |

Possible values for **join\_type**: *inner, leftouter, rightouter, fullouter*

Possible values for **relation\_type**: 11: one to one, 1M: one to many

Possible values for **affinity**: Global, Report

### joincol (deprecated in *v2017.2*)

| Node | Description | Type | Required |
| --- | --- | --- | --- |
| col\_from\_name | *From column (left)* | string | yes |
| col\_to\_name | *To column (right)* | string | yes |

### clause v2017.2+

| Node | Description | Type | Required |
| --- | --- | --- | --- |
| left\_entity | *From object (left) (v2017.3+)* | string | no |
| left\_side | *From expression (left)* | string | yes |
| right\_side | *To expression (right)* | string | yes |
| conjunction | *Joining conjunction* | constant | yes |
| comparison | *Comparison operator* | constant | yes |
| left\_side\_type | *From expression type* | constant | yes |
| right\_side\_type | *To expression type* | constant | yes |
| level | *Parenthesis nesting level* | int | yes |

**left\_entity** overrides the base (implicit) *from object***entity\_from\_name** for the specific join clause; this is necessary for some uses of the *IN* operator

Possible values for **conjunction**: *AND*, *OR*

Possible values for **comparison**: *EQ* (=), *NE* (<>), *LT* (<), *GT* (>), *LE* (<=), *GE* (>=), *IN*

Possible values for **left\_side\_type**, **right\_side\_type**: *Column*, *Constant*, *SubQuery*, *Expression*

### Example

```
<join>
  <entity_from_name>PRO</entity_from_name>
  <entity_to_name>CAT</entity_to_name>
  <clause>
    <left_side>ProductId</left_side>
    <right_side>CategoryId</right_side>
    <conjunction>AND</conjunction>
    <comparison>EQ</comparison>
    <right_side_type>Column</right_side_type>
    <left_side_type>Column</left_side_type>
    <level>0</level>
  </clause>
</join>
```

## Parameters

The [Parameters](https://devnet.logianalytics.com/hc/en-us/articles/5281625630615-Parameters) topic includes detailed descriptions of each of these settings.

Outer node: `<parameter></parameter>`

| Node | Description | Type | Required |
| --- | --- | --- | --- |
| id | Name | string | yes |
| data\_type | Type | constant | yes |
| value | Value | string | no |
| hidden | Hidden | bool | yes |
| prompt\_text | Prompt Text | string | no |
| **parameter\_dropdown** | Parameter Dropdown Object | object | no |

Possible values for **data\_type**: *string, date, integer, decimal, Boolean*

### parameter\_dropdown

| Node | Description | Type | Required |
| --- | --- | --- | --- |
| db\_name | *Database object name* | string | yes |
| sql\_stmt | *SQL statement* | string | no |
| datasource\_id | *Unique Id of data source* | int | yes |
| object\_type | *Object type* | constant | yes |
| value\_field | Value Field | string | yes |
| display\_value\_field | Display Value Field | string | no |
| display\_data\_type | Display Type | constant | yes |
| sp\_params | *Stored proc parameters* | string | no |

Possible values for **object\_type**: *table, view, procedure, function, assembly, sqlstmt, websvc, file*

Possible values for **display\_data\_type**: *string, date, integer, decimal*

### Example

```
<parameter>
  <id>count</id>
  <data_type>integer</data_type>
  <hidden>False</hidden>
  <prompt_text />
  <parameter_dropdown>
    <db_name>Category</db_name>
    <sql_stmt />
    <datasource_id>1</datasource_id>
    <object_type>view</object_type>
    <value_field>Category_View</value_field>
    <display_value_field />
    <display_data_type>string</display_data_type>
    <sp_params />
  </parameter_dropdown>
</parameter>
```

## Quick Functions v2021.1+

**Quick Functions** are pre-defined calculations or operators that transform the fields in either detail fields or group columns in ExpressView. Learn more in [Quick Functions](https://devnet.logianalytics.com/hc/en-us/articles/5281612083991-ExpressView-Formula-Columns-v2021-1-#Quick).

Outer node: `<quickfunction></quickfunction>`

| Node | Description | Type | Required |
| --- | --- | --- | --- |
| *id* | A unique identifier used internally by the application | string | yes |
| *language\_id* | The element ID in the language file that will be displayed in the Designer for this Quick Function’s name For more information, review [Multi-Language Support](https://devnet.logianalytics.com/hc/en-us/articles/5281604247447-Multi-Language-Support) | string | yes |
| *display\_formula* | An Exago formula, preceded with the equals sign, that will be applied to the output displayed to the user Use the placeholder `{cell_text}` to include the contents of the cell in the formula  [List of Functions](https://devnet.logianalytics.com/hc/en-us/articles/5281615111575-List-of-Functions), [Custom Functions](https://devnet.logianalytics.com/hc/en-us/articles/5281628193815-Custom-Functions) and [Parameters](https://devnet.logianalytics.com/hc/en-us/articles/5281625630615-Parameters)may be used in the formula. Do not use aggregate functions or data object fields.  Special characters must be XML encoded (for example use `&amp;` for the concatenation character &) | string | yes |
| *sort\_text* | An Exago formula, preceded with the equals sign, that will be applied to the data to order it when the column is sorted or when it is a group Use the placeholder `{cell_text}` to include the contents of the cell in the formula  [List of Functions](https://devnet.logianalytics.com/hc/en-us/articles/5281615111575-List-of-Functions), [Custom Functions](https://devnet.logianalytics.com/hc/en-us/articles/5281628193815-Custom-Functions) and [Parameters](https://devnet.logianalytics.com/hc/en-us/articles/5281625630615-Parameters)may be used in the formula. Do not use aggregate functions or data object fields.  Special characters must be XML encoded (for example use `&amp;` for the concatenation character &) | string | yes |
| *supported\_data\_types* | The column data types that the Quick Function may be applied to Separate multiple values with this delimiter: `|*{*}*|` | string from [QuickFunctionDataType v2021.1+](https://devnet.logianalytics.com/hc/en-us/articles/5281610137879-Constants-and-Enumerators#QuickFun) | yes |
| *return\_data\_type* | The data type that this Quick Function returns A column will be transformed to this data type if different than the column’s existing type | int from [DataType](https://devnet.logianalytics.com/hc/en-us/articles/5281610137879-Constants-and-Enumerators#DataType) | yes |

### Examples

#### year

The **year** Quick Function uses the [Year](https://devnet.logianalytics.com/hc/en-us/articles/5281584402455-Date-Functions#Year)() function to transform a Date or DateTime column into an integer value of the year portion of the date.

##### WebReports.xml

```
<quickfunction>
    <id>year</id>
    <language_id>Year_wrQuickFunction</language_id>
    <display_formula>=Year({cell_text})</display_formula>
    <sort_text>=Year({cell_text})</sort_text>
    <return_data_type>2</return_data_type>
    <supported_data_types>Date</supported_data_types>
</quickfunction>
```

##### en-us.xml

Below is an except from the English language file where the name of this Quick Function as it appears in the Designer is defined.

Copy

Language file definition for the Year Quick Function

```
1
2
3
4
5
<DateFunctions>  
      ...  
 <element id="Year_wrQuickFunction">Year</element>  
     ...  
</DateFunctions>
```

```
<DateFunctions>
  	...
 <element id="Year_wrQuickFunction">Year</element>
 	...
</DateFunctions>
```

#### month-name

The **month-name** Quick Function uses the [MonthName v2017.2+](https://devnet.logianalytics.com/hc/en-us/articles/5281584402455-Date-Functions#MonthNam) function to transform a Date or DateTime column into a string value representing the name of the month portion of the date (for example *January*, *February*, *March*, etc…). Note the use of the [Month](https://devnet.logianalytics.com/hc/en-us/articles/5281584402455-Date-Functions#Month)() function in the `<sort_text>` node to keep the list ordered chronologically instead of alphabetically.

##### WebReports.xml

```
<quickfunction>
    <id>month-name</id>
    <language_id>MonthName_wrQuickFunction</language_id>
    <display_formula>=MonthName({cell_text})</display_formula>
    <sort_text>=Month({cell_text})</sort_text>
    <return_data_type>0</return_data_type>
    <supported_data_types>Date</supported_data_types>
</quickfunction>
```

##### en-us.xml

Below is an except from the English language file where the name of this Quick Function as it appears in the Designer is defined.

```
<DateFunctions>
  	...
 <element id="MonthName_wrQuickFunction">Month Name</element>
 	...
</DateFunctions>
```

## Roles

The [Roles](https://devnet.logianalytics.com/hc/en-us/articles/5281625714967-Roles) topic includes detailed descriptions of each of these settings.

Outer node: `<role></role>`

| Node | Description | Type | Required |
| --- | --- | --- | --- |
| id | ID | string | yes |
| active | Active | bool | yes |
| **rolegeneral** | *General settings* | object | yes |
| **security** | *Security settings* | object | yes |

### rolegeneral

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/25323356730135 "Note")
>
> Settings pertaining to Express Reports were removed from the Admin Console in *v2019.2* but they remain available here in the config file. No other functionality was removed.

| Node | Description | Type | Required |
| --- | --- | --- | --- |
| reportpath | Report Path | string | no |
| dateformat | Date Format | string | no |
| timeformat | Time Format | string | no |
| datetimeformat | DateTime Format | string | no |
| separatorsymbol | Numeric Separator Symbol | string | no |
| currencysymbol | Numeric Currency Symbol | string | no |
| readfiltervalues | Read Database for Filter Values | bool | no |
| dbtimeout | Database Timeout | int | yes |
| showgrid | Show Grid Lines in Report Viewer | bool | no |
| showcrosstabreports | Allow Creation/Editing of CrossTab Reports | bool | no |
| showDashboardreports | Allow Creation/Editing of Dashboard Reports | bool | no |
| showchainedreports | Allow Creation/Editing of Chained Reports | bool | no |
| showexpressviews | Allow Creation/Editing of ExpressViews | bool | no |
| allowexpressviewliveedit | Allow Editing ExpressView with Live Data | bool | no |
| showexpressreports | Allow Creation/Editing of Express Reports | bool | no |
| showexpressreportsgrouping | Show Grouping | bool | no |
| showexpressreportsformulabutton | Show Formula Button | bool | no |
| showexpressreportsstylingtoolbar | Show Styling Toolbar | bool | no |
| showexpressreportsthemes | Show Themes | bool | no |
| showadvancedreports | Allow Creation/Editing of Advanced Reports | bool | no |
| showschedulereports | Show Report Scheduling Option | bool | no |
| showschedulereportsmanager | Show Schedule Reports Manager | bool | no |
| schedulemanagerviewlevel | Scheduler Manager User View Level | constant | no |
| showschedulereportsemail | Show Email Report Options | bool | no |
| decimalsymbol | Numeric Decimal Symbol | string | no |
| languagefile | *Language File* | string | no |
| servertimezoneoffset | Server Time Zone Offset | decimal light bulb Set to *0* to use the **ClientTimeZoneName**. *If null, Exago will use the External Interface (a deprecated extensibility feature) to calculate the time zone change*. | no |
| showDashboardnewvisualizationbutton | Allow Creation/Editing of Dashboard Visualizations | bool | no |
| allowreportcustomsqlobjects | Allow Creation of Custom SQL Objects in Advanced Reports (*v2018.1+*) | bool | no |

Possible values for **schedulemanagerviewlevel**: *user, company, all*

### security

| Node | Description | Type | Required |
| --- | --- | --- | --- |
| **folders** | Folder Security | object | yes |
| **dataobjects** | Data Object Security | object | yes |
| **dataobjectrows** | Data Row Security | object | no |
| includereportcustomsqlobjects | v2018.1+ Allow User to View Report-Level Custom SQL Objects | bool | no |

### folders

| Node | Description | Type | Required |
| --- | --- | --- | --- |
| include\_all | Include All Folders | bool | yes |
| read\_only | All Folders Read Only | bool | yes |
| allow\_management | Allow Folder Management | bool | yes |
| **folder** | Folders | object | no (1+) |

#### folder

| Node | Description | Type | Required |
| --- | --- | --- | --- |
| name | Folder Name | string | yes |
| read\_only | Read Only | bool | yes |
| propagate | *Propagate status to sub-folders* | bool | yes |

#### dataobjects

| Node | Description | Type | Required |
| --- | --- | --- | --- |
| include\_all | Include All Data Objects | bool | yes |
| **dataobject** | Objects | object | no (1+) |

#### dataobject

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/25323356730135 "Note")
>
> For name, use Id if set, otherwise use db\_name.

| Node | Description | Type | Required |
| --- | --- | --- | --- |
| name | Data Object Name | string | yes |

### dataobjectrows

| Node | Description | Type | Required |
| --- | --- | --- | --- |
| **dataobjectrow** | Filters | object | no (1+) |

#### dataobjectrow

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/25323356730135 "Note")
>
> For name, use Id if set, otherwise use db\_name.

| Node | Description | Type | Required |
| --- | --- | --- | --- |
| name | Data Object Name | string | yes |
| filter | Filter String | string | yes |

### Example

```
  <role>
    <id>Restricted</id>
    <active>False</active>
    <rolegeneral>
      <reportpath />
      <dateformat />
      <timeformat />
      <datetimeformat />
      <separatorsymbol />
      <currencysymbol />
      <readfiltervalues />
      <dbtimeout>0</dbtimeout>
      <showgrid />
      <showcrosstabreports />
      <showDashboardreports />
      <showchainedreports />
      <showexpressviews />
      <allowexpressviewliveedit />
      <showexpressreports />
      <showexpressreportsgrouping />
      <showexpressreportsformulabutton />
      <showexpressreportsstylingtoolbar />
      <showexpressreportsthemes />
      <showadvancedreports />
      <showschedulereports />
      <showschedulereportsmanager />
      <schedulemanagerviewlevel />
      <cachevisibilitylevel />
      <showschedulereportsemail />
      <decimalsymbol />
      <languagefile />
      <servertimezoneoffset>0</servertimezoneoffset>
      <clienttimezonename />
      <showDashboardnewvisualizationbutton />
      <allowreportcustomsqlobjects />
    </rolegeneral>
    <security>
      <includereportcustomsqlobjects>False</includereportcustomsqlobjects>
      <folders>
        <include_all>False</include_all>
        <read_only>False</read_only>
        <allow_management>True</allow_management>
        <folder>
          <name>Sales Reports</name>
          <read_only>False</read_only>
          <propagate>True</propagate>
        </folder>
      </folders>
      <dataobjects>
        <include_all>True</include_all>
      </dataobjects>
      <dataobjectrows />
    </security>
  </role>
```

## Server Events

The [Introduction to Server Events](https://devnet.logianalytics.com/hc/en-us/articles/5281583100439-Introduction-to-Server-Events) topic includes detailed descriptions of each of these settings.

Outer node:  
`<serverevent></serverevent>`

| Node | Description | Type | Required |
| --- | --- | --- | --- |
| name | Name | string | yes |
| id | *Unique Id* | int | yes |
| event\_type | Global Event | constant | yes |
| datasource\_id | *Id of assembly data source* | int | no |
| func\_name | *Assembly function name* | string | no |
| language | Language | constant | no |
| program\_code | *Program code* | string | no |
| **reference** | References | object | no (1+) |
| **namespace** | Namespaces | object | no (1+) |

Possible values for **event\_type**: *None*, or refer to the [List of Server Events](https://devnet.logianalytics.com/hc/en-us/articles/5281621453975-List-of-Server-Events).

Possible values for **language**: *CSharp, JavaScript, VB*

### reference

| Node | Description | Type | Required |
| --- | --- | --- | --- |
| name | *Reference name* | string | yes |

### namespace

| Node | Description | Type | Required |
| --- | --- | --- | --- |
| name | *Namespace name* | string | yes |

### Example

```
<serverevent>
  <name>ExpandAllFolders</name>
  <id>0</id>
  <event_type>OnAfterLoadReportsList</event_type>
  <language>CSharp</language>
  <program_code>Extensions.ServerEvents.ExpandAllFolders(sessionInfo, (TreeNodeCollection)args[0]);
return null;</program_code>
  <reference>
    <name>Extensions.dll</name>
  </reference>
  <reference>
    <name>WebReports.dll</name>
  </reference>
  <namespace>
    <name>WebReports.UI.Controls</name>
  </namespace>
</serverevent>
```

## Storage Management

The [Storage Management: Introduction](https://devnet.logianalytics.com/hc/en-us/articles/5281647019287-Storage-Management-Introduction) topic contains detailed descriptions of each of these settings.

Each of these settings may be accessed via the .NET API’s **`WebReports.Api.Api.SetupData.StorageMgmtConfig`** namespace. For example:

```
api.SetupData.StorageMgmtConfig.ClassName = "WebReports.ContentDatabase.StorageMgmtDatabase";
```

Outer node: `<storagemgmt></storagemgmt>`

| Node | Description | Type | Required |
| --- | --- | --- | --- |
| assembly **API key:** *Assembly* | Full path to the DLL implementing the IStorageManagement interface | string | yes |
| class **API key:** *ClassName* | Name of the class in the assembly that implements IStorageManagement | string | yes |
| report\_list\_cache\_timeout **API key:***ReportListCacheTimeout* | Number of seconds before the report list cache expires | integer | yes |
| report\_xml\_cache\_timeout **API key:***ReportXmlCacheTimeout* | Number of seconds before the report definition XML cache expires | integer | yes |
| theme\_list\_cache\_enabled **API key:***ThemeListCacheTimeout* | Whether or not theme list caching is turned on or off | Boolean | yes |
| report\_xml\_cache\_enabled **API key:***ReportXmlCacheEnabled* | Whether or not report definition XML caching is enabled | Boolean | yes |
| default\_inherit\_flag **API key:***DefaultInheritFlag* | Determines if new content will inherit permissions of its parent. | Boolean | yes |
| default\_party\_type\_id **API key:***DefaultPartyTypeId* | If default\_inherit\_flag is *False*, this is the party\_type\_id that new content will be assigned. | integer | no |
| default\_access\_flags **API key:***DefaultAccessFlags* | If default\_inherit\_flag is *False*, this is the access\_flags bitmap that new content will be assigned. v2021.1+If default\_inherit\_flag is *False*, this is a comma-separated list of [ContentPermission v2021.1+](https://devnet.logianalytics.com/hc/en-us/articles/5281610137879-Constants-and-Enumerators#ContentP) items that new content will be assigned. | integer v2020.1–v2021.1 [ContentPermission v2021.1+](https://devnet.logianalytics.com/hc/en-us/articles/5281610137879-Constants-and-Enumerators#ContentP)v2021.1+ | yes |
| option option nodes are used to store Storage Management options and settings data in name-value pairs | | Name | Value Description | | --- | --- | | DbType | Database type | | DbProvider | Database provider | | ConnectionString | Connection string to Storage Management database | | ReportListCacheKey | Key which is used to determine when the report list cache should be replenished. | | | |
| table\_prefix **API key:***TablePrefix* | Provide an optional prefix for all Storage Management database tables. Review [Storage Management: Database Schema](https://devnet.logianalytics.com/hc/en-us/articles/5281630919319-Storage-Management-Database-Schema) for information. This option can be used to add a schema if it exists. **Examples**:   1. `test_` will result in tables named *test\_content*, *test\_party\_type*, *test\_content\_access* and *test\_storage\_meta* 2. `dbo.` will result in tables named *dbo.content*, *dbo.party\_type*, *dbo.content\_access* and *dbo.storage\_meta* | string | no |
| identity | <identity> nodes define Storage Management identity keys in name-value pairs. This facilitates adding identity nodes beyond the included ownerId, userId, classId and companyId or changing their names. light bulb Adding identity keys will also require changes to the Party Type table. | | |

### Example

This example implements Exago’s out-of-the-box implementation of the IStorageManagement interface and includes an additional custom identity key named `location`.

```
<storagemgmt>
    <assembly>WebReports.ContentDatabase.dll</assembly>
    <class>WebReports.ContentDatabase.StorageMgmtDatabase</class>
    <report_list_cache_timeout>30</report_list_cache_timeout>
    <report_xml_cache_timeout>30</report_xml_cache_timeout>
    <theme_list_cache_timeout>600</theme_list_cache_timeout>
    <report_list_cache_enabled>False</report_list_cache_enabled>
    <report_xml_cache_enabled>False</report_xml_cache_enabled>
    <default_inherit_flag>False</default_inherit_flag>
    <default_party_type_id>0</default_party_type_id>
    <option name="DbType" value="SQLite" />
    <option name="DbProvider" value="SQLite" />
    <option name="ConnectionString" value="Data Source=D:StorageMgmt.sqlite" />
    <option name="ReportListCacheKey" value="" />
    <table_prefix>sm_</table_prefix>
    <identity name="userId" value="Astro Boy" />
    <identity name="classId" value="Exago, Inc." />
    <identity name="location" value="Kingston" />
    <identity name="companyId" value="Development" />
  </storagemgmt>
```
