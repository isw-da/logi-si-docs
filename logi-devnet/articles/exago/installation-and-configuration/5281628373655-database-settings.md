---
title: "Database Settings"
id: 5281628373655
section: "Installation and Configuration"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281628373655-Database-Settings
updated_at: 2023-04-03T17:52:19Z
---

# Database Settings

# Database Settings

This topic applies to the **Admin Console** > ![TreeGeneral.png](https://devnet.logianalytics.com/hc/article_attachments/5432174178839/treegeneral.png)**General** > ![TreeGeneralNode.png](https://devnet.logianalytics.com/hc/article_attachments/5432159353239/treegeneralnode.png)**Database Settings**.

---

The **Database Settings** allow administrators to adjust how Exago interfaces with the data sources. Additional type-specific settings allow you to specify which driver to utilize when connecting to each data source.

## Settings

### Database Settings

#### Database Timeout

A value that is passed to the data provider’s `CommandTimeout` property as Exago queries the business intelligence data source. It is up to the data provider what to do with this value. This timeout has no effect on connections to Folder Management or Storage Management databases, if applicable.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This value is passed on to the data source provider when the report is executed. Each data source driver, data source or individual database may interpret this setting slightly differently. Consult the official product documentation associated with the data source implementation for complete details how this setting will impact the environment.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This setting will also control the maximum number of seconds that a Web Service API method can run. If set to *0* the Web Service API time out will be *infinite*.

#### Database Row Limit

Maximum number of rows returned on an execution. This only applies to Tables, Views and Functions. Set to *0* to return all rows.

#### Row Limit Step Size

Maximum number of rows returned on a query. Set to *0* to return all rows. Set greater than *0* to enable [Incremental Loading](https://devnet.logianalytics.com/hc/en-us/articles/5281629053335-Incremental-Loading) for **Advanced Reports** and **ExpressView**. The value determines how many rows are returned for each user-initiated data query.

#### Disable Non-Joined Data Objects

If *True* users are not able to add Data Objects to a report that do not have a join path with at least one other Data Object on the report. Set to *False* to disable this restriction.

For versions *pre-2018.1*:

This setting does not have an affect on ExpressView.

For versions *v2018.1+*:

This setting does not have an affect for ExpressView unless **Admin Console** > **General** > **Feature/UI Settings** > **ExpressView Settings** > **Fields Enabled in Data Fields Tree** is set to *Direct Joins Only*.

#### Enable Special Cartesian Processing

If *True* any one-to-many Joins will cause special processing to avoid data repeating on the report. Set to *False* to disable this behavior.

#### Aggregate and Group in Database

If *True*, aggregate and grouping calculations will be done in the database when possible. This will provide a performance boost for reports with group sections.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> Before enabling this, ensure that all One-To-Many Joins in the configuration are correctly identified and set as *One-To-Many* in the[Join Configuration](https://devnet.logianalytics.com/hc/en-us/articles/5281644535703-Join-Configuration). If these joins are not properly identified, reports which utilize them will return incorrect aggregate data. See [Database Aggregation](https://devnet.logianalytics.com/hc/en-us/articles/5281607025943-Database-Aggregation) for more information.

#### Convert Formula Filters and Sorts to SQL v2018.2–v2020.1

#### Convert Formulas to SQL v2020.1+

If *True*, formula filters and sorts will be converted to SQL when possible. The converted SQL statements will be placed in the WHERE (for formula filters) and ORDER BY (for formula sorts) clauses when querying data for the report. If set to *False*, all formula filtering and sorting will occur in-memory.

For more information, please see the **[Converting Formula Sorts to SQL](#Converti)** section below.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Due to innate difference between Exago’s formula engine and SQL database engines, there may be discrepancies in data returned between two methods. Additionally, because the converted SQL formulas may contain arbitrary input, the connection string must be read-only access.

### Type-Specific Database Settings

Each type of Data Source has the following settings available.

Click the **AutoFill ![Autofill.png](https://devnet.logianalytics.com/hc/article_attachments/5432233475735/autofill.png)**icon to automatically fill the **Data Provider**, **Table Schema Properties**, **View Schema Properties**, **Function Schema Properties** and **Procedure Schema Properties** fields for each database type. Fields will be filled with data from the drivers provided with the application.

#### Data Provider

Specify the name that can be used programmatically to refer to the data provider.

This matches the *InvariantName* found as a property of **DbProviderFactories** in the server’s `machine.config` file.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> The `machine.config` file is located in the `%SystemRoot%\Microsoft\.NETFramework\%VersionNumber%\CONFIG` directory.

#### Table Schema Properties

Specifies how to retrieve the schema of tables.

#### View Schema Properties

Specifies how to retrieve the schema of views.

#### Function Schema Properties

Specifies how to retrieve the schema of functions.

#### Procedure Schema Properties

Specifies how to retrieve the schema of procedures.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
>
> For any of the Schema Property settings you can dynamically refer to properties from the Data Source’s connection string by surrounding the property name in @ symbols. For example, `@database@` will be replaced with the database name from the connection string of the Data Source being queried.

## Converting Formula Sorts to SQL

When **Convert Formula Filters and Sorts to SQL** is *True*, Exago attempts to push all formulasorts to the database instead of running them in memory.

For example, a report may be sorted by the following formula, which organizes the data based upon whether or not an *Order* has a *Revenue* of greater than or equal to $1000.

```
=(OrderDetails.Revenue)>=1000
```

This formula sort would be converted to the following SQL statement and appended to the ORDER BY clause of the query during report execution.

```
ORDER BY
  (CASE WHEN dbo.[OrderDetails].[Quantity] * dbo.[OrderDetails].[UnitPrice] >=
   1000 THEN '1' ELSE '0' END) asc
```

### Formula Dictionary

All defined Exago formula to SQL statement translations can be found in the `dbconfigs.json` file, under the **Formula Dictionary** property of each database type. The formula dictionary is comprised of formula names paired with the corresponding SQL syntax translation. In *v2021.2+*, the `and`, `switch`, `or`, `DateAdd`, `DateDiff` and `Concatenate` functions are represented as JSON objects with zero or more properties. This is helpful when a database has different implementations of internal functions for handling dates and times, for example. See [Writing SQL Translations](#Writing) below for more information.

SQL syntax translations may be added in this file for any [Custom Functions](https://devnet.logianalytics.com/hc/en-us/articles/5281628193815-Custom-Functions) that are defined. Translations can be overloaded, meaning multiple versions of a translation with a variable amount of arguments are allowed. Exago will choose the correct translation based on the number of arguments that are passed to it. Functions with an unbounded number of arguments, however, cannot be defined.

See [Managing the dbconfigs.json File](https://devnet.logianalytics.com/hc/en-us/articles/5281593110167-Managing-the-dbconfigs-json-File) for more information.

### Writing SQL Translations

Each function is paired with its standard SQL translation as a string array, except for `and`, `switch`, `or`, `DateAdd`, `DateDiff` and `Concatenate` in *v2021.2+*.

Arguments are represented as digits enclosed in curly braces, starting from 0, indicating the order in which they are passed from the ExagoBI application. For example, `"if": [ "(CASE WHEN {0} THEN {1} ELSE {2} END)" ]` uses the first argument passed to the `If()` function for the comparison, the second argument if the comparison is true and the third argument if the comparison is false.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> For the date function translations, the very first argument representing the interval to add or subtract (which would be `{0}`) is not needed, so only `{1}` and `{2}` representing the quantity of the interval, and the date to be changed appear in the translation.

The function translations below use a JSON object instead of an array of strings. This feature requires *v2021.2+*.

#### `And`

The `and` translation has no additional properties. It emits the same SQL regardless of database in use.

##### Example

```
"and": {  }
```

#### `Or`

The `or` translation has no additional properties. It emits the same SQL regardless of database in use.

##### Example

```
"or" : {  }
```

#### `Switch`

The `switch` translation has no additional properties.

##### Example

```
"switch" : {  }
```

#### `DateAdd`

The `DateAdd` translation may implement 1 or more of the following properties:

* **year** — the SQL to add years to the date
* **month** — the SQL to add months to the date
* **day** — the SQL to add days to the date
* **week** — the SQL to add weeks to the date
* **hour** — the SQL to add hours to the date
* **minute** — the SQL to add minutes to the date
* **second** — the SQL to add seconds to the date
* **quarter** — the SQL to add quarters to the date
* **default** — the SQL when a non-constant is passed for the *interval* argument of the function

##### Example

```
"dateadd": {
    "year": "DATE_ADD({2}, INTERVAL {1} YEAR)",
    "month": "DATE_ADD({2}, INTERVAL {1} MONTH)",
    "day": "DATE_ADD({2}, INTERVAL {1} DAY)",
    "week": "DATE_ADD({2}, INTERVAL ({1}*7) DAY)",
    "hour": "DATE_ADD({2}, INTERVAL {1} HOUR)",
    "minute": "DATE_ADD({2}, INTERVAL {1} MINUTE)",
    "second": "DATE_ADD({2}, INTERVAL {1} SECOND)",
    "quarter": "DATE_ADD({2}, INTERVAL ({1} * 3) MONTH)",
    "default": "CASE {0} WHEN 'yyyy' THEN DATE_ADD({2}, INTERVAL {1} YEAR) WHEN 'm' THEN DATE_ADD({2}, INTERVAL {1} MONTH) WHEN 'y' THEN DATE_ADD({2}, INTERVAL {1} DAY) WHEN 'd' THEN DATE_ADD({2}, INTERVAL {1} DAY) WHEN 'w' THEN DATE_ADD({2}, INTERVAL ({1}*7) DAY) WHEN 'h' THEN DATE_ADD({2}, INTERVAL {1} HOUR) WHEN 'n' THEN DATE_ADD({2}, INTERVAL {1} MINUTE) WHEN 's' THEN DATE_ADD({2}, INTERVAL {1} SECOND) WHEN 'ww' THEN DATE_ADD({2}, INTERVAL ({1}*7) DAY) WHEN 'q' THEN DATE_ADD({2}, INTERVAL ({1} * 3) MONTH) END"
}
```

#### `DateDiff`

The `DateDiff` translation may implement 1 or more of the following properties:

* **year** — the SQL to calculate the difference in years
* **month** — the SQL to calculate the difference in months
* **day** — the SQL to calculate the difference in days
* **week** — the SQL to calculate the difference in weeks
* **hour** — the SQL to calculate the difference in hours
* **minute** — the SQL to calculate the difference in minutes<.li>
* **second** — the SQL to calculate the difference in seconds
* **quarter** — the SQL to calculate the difference in quarters
* **default** — the SQL when a non-constant is passed for the *interval* argument of the function

##### Example

```
"datediff": {
    "year": "TIMESTAMPDIFF(YEAR, CAST({1} AS DATE), CAST({2} AS DATE))",
    "month": "TIMESTAMPDIFF(MONTH, CAST({1} AS DATE), CAST({2} AS DATE))",
    "day": "TIMESTAMPDIFF(DAY, CAST({1} AS DATE), CAST({2} AS DATE))",
    "week": "FLOOR(TIMESTAMPDIFF(DAY, CAST({1} AS DATE), CAST({2} AS DATE))/7)",
    "hour": "TIMESTAMPDIFF(HOUR, {1}, {2})",
    "minute": "TIMESTAMPDIFF(MINUTE, {1}, {2})",
    "second": "TIMESTAMPDIFF(SECOND, {1}, {2})",
    "quarter": "FLOOR(TIMESTAMPDIFF(MONTH, CAST({1} AS DATE), CAST({2} AS DATE))/3)",
    "default": "CASE {0} WHEN 'yyyy' THEN TIMESTAMPDIFF(YEAR, CAST({1} AS DATE), CAST({2} AS DATE)) WHEN 'm' THEN TIMESTAMPDIFF(MONTH, CAST({1} AS DATE), CAST({2} AS DATE)) WHEN 'd' THEN TIMESTAMPDIFF(DAY, CAST({1} AS DATE), CAST({2} AS DATE)) WHEN 'w' THEN FLOOR(TIMESTAMPDIFF(DAY, CAST({1} AS DATE), CAST({2} AS DATE))/7) WHEN 'h' THEN TIMESTAMPDIFF(HOUR, {1}, {2}) WHEN 'n' THEN TIMESTAMPDIFF(MINUTE, {1}, {2}) WHEN 's' THEN TIMESTAMPDIFF(SECOND, {1}, {2}) WHEN 'ww' THEN FLOOR(TIMESTAMPDIFF(DAY, CAST({1} AS DATE), CAST({2} AS DATE))/7) WHEN 'q' THEN FLOOR(TIMESTAMPDIFF(MONTH, CAST({1} AS DATE), CAST({2} AS DATE))/3) END"
}
```

#### `Concatenate`

The `Concatenate` translation implements these properties

* **mode** — determines if the translation will use a function or an operator. Provide either one of these values:
  + *infix-operator* — use an operator (for example `a || b || c`) for concatenation
  + *function-variable-args* to use a function (for example `CONCAT(a, b, c)`) for concatenation. When using *function-variable-args*, specify the name of the function with the **functionname** property.
* **functionname** — the name of the database function to use for concatenation when **mode** is *function-variable-args*.

##### Example

```
"concatenate": {
	"mode": "function-variable-args",
	"functionname": "CONCAT"
},
```

For example, in *v2021.2.0+*, the entire Formula Dictionary for MySQL is:

```
"FormulaDictionary" : {
	"and": { },
	"if": [ "(CASE WHEN {0} THEN {1} ELSE {2} END)" ],
	"switch": { },
	"or": { },
	"len": [ "CHAR_LENGTH({0})" ],
	"null": [ "NULL" ],
	"dbnull": [ "NULL" ],
	"date": [ "STR_TO_DATE('{0}/{1}/{2}', '%Y/%m/%d')" ],
	"dateadd": {
		"year": "DATE_ADD({2}, INTERVAL {1} YEAR)",
		"month": "DATE_ADD({2}, INTERVAL {1} MONTH)",
		"day": "DATE_ADD({2}, INTERVAL {1} DAY)",
		"week": "DATE_ADD({2}, INTERVAL ({1}*7) DAY)",
		"hour": "DATE_ADD({2}, INTERVAL {1} HOUR)",
		"minute": "DATE_ADD({2}, INTERVAL {1} MINUTE)",
		"second": "DATE_ADD({2}, INTERVAL {1} SECOND)",
		"quarter": "DATE_ADD({2}, INTERVAL ({1} * 3) MONTH)",
		"default": "CASE {0} WHEN 'yyyy' THEN DATE_ADD({2}, INTERVAL {1} YEAR) WHEN 'm' THEN DATE_ADD({2}, INTERVAL {1} MONTH) WHEN 'y' THEN DATE_ADD({2}, INTERVAL {1} DAY) WHEN 'd' THEN DATE_ADD({2}, INTERVAL {1} DAY) WHEN 'w' THEN DATE_ADD({2}, INTERVAL ({1}*7) DAY) WHEN 'h' THEN DATE_ADD({2}, INTERVAL {1} HOUR) WHEN 'n' THEN DATE_ADD({2}, INTERVAL {1} MINUTE) WHEN 's' THEN DATE_ADD({2}, INTERVAL {1} SECOND) WHEN 'ww' THEN DATE_ADD({2}, INTERVAL ({1}*7) DAY) WHEN 'q' THEN DATE_ADD({2}, INTERVAL ({1} * 3) MONTH) END"
	},
	"datediff": {
		"year": "TIMESTAMPDIFF(YEAR, CAST({1} AS DATE), CAST({2} AS DATE))",
		"month": "TIMESTAMPDIFF(MONTH, CAST({1} AS DATE), CAST({2} AS DATE))",
		"day": "TIMESTAMPDIFF(DAY, CAST({1} AS DATE), CAST({2} AS DATE))",
		"week": "FLOOR(TIMESTAMPDIFF(DAY, CAST({1} AS DATE), CAST({2} AS DATE))/7)",
		"hour": "TIMESTAMPDIFF(HOUR, {1}, {2})",
		"minute": "TIMESTAMPDIFF(MINUTE, {1}, {2})",
		"second": "TIMESTAMPDIFF(SECOND, {1}, {2})",
		"quarter": "FLOOR(TIMESTAMPDIFF(MONTH, CAST({1} AS DATE), CAST({2} AS DATE))/3)",
		"default": "CASE {0} WHEN 'yyyy' THEN TIMESTAMPDIFF(YEAR, CAST({1} AS DATE), CAST({2} AS DATE)) WHEN 'm' THEN TIMESTAMPDIFF(MONTH, CAST({1} AS DATE), CAST({2} AS DATE)) WHEN 'd' THEN TIMESTAMPDIFF(DAY, CAST({1} AS DATE), CAST({2} AS DATE)) WHEN 'w' THEN FLOOR(TIMESTAMPDIFF(DAY, CAST({1} AS DATE), CAST({2} AS DATE))/7) WHEN 'h' THEN TIMESTAMPDIFF(HOUR, {1}, {2}) WHEN 'n' THEN TIMESTAMPDIFF(MINUTE, {1}, {2}) WHEN 's' THEN TIMESTAMPDIFF(SECOND, {1}, {2}) WHEN 'ww' THEN FLOOR(TIMESTAMPDIFF(DAY, CAST({1} AS DATE), CAST({2} AS DATE))/7) WHEN 'q' THEN FLOOR(TIMESTAMPDIFF(MONTH, CAST({1} AS DATE), CAST({2} AS DATE))/3) END"
	},
	"day": [ "DAY({0})" ],
	"dayofyear": [ "DAYOFYEAR({0})" ],
}
```

For example, the following contains part of the Formula Dictionary for the MySQL database *pre-v2021.2*:

```
"FormulaDictionary": 
{
   "and": ["({0} AND {1})"],
   "false":["(1=0)"],
   "if": ["(CASE WHEN {0} THEN {1} ELSE {2} END)"],
   "or": ["({0} OR {1})"],
   "len": ["CHAR_LENGTH({0})"],
   "true":["(1=1)"],
   "date": ["STR_TO_DATE('{0}/{1}/{2}', '%Y/%m/%d')"],
   ...
},
```

### Notes on Behavior

Please take the following information into consideration when utilizing this feature:

* Non-SQL databases (for example, Mongo, ElasticSearch, Excel) do not support this feature. All sorting for reports using non-SQL databases is done in-memory.
* DB2 is supported by this feature; however, there are limitations regarding what formulas can be translated to SQL when using this database type. In *v2020.1.2+*, most functions are translated to SQL except for `DateAdd`, `DateDiff`, `MonthName`, `Time` and `Mid`.
* SQLite supports translating most functions to SQL with the exception of the [Financial Functions](https://devnet.logianalytics.com/hc/en-us/articles/5281591957399-Financial-Functions), [Arithmetic and Geometric Functions](https://devnet.logianalytics.com/hc/en-us/articles/5281599710103-Arithmetic-and-Geometric-Functions) and some of the [Database and Data Type Functions](https://devnet.logianalytics.com/hc/en-us/articles/5281622983703-Database-and-Data-Type-Functions) and [String Functions](https://devnet.logianalytics.com/hc/en-us/articles/5281606630807-String-Functions).
* If a sort contains reference to an object from a different data source than the one that is being queried for report execution, then all sorting will occur in-memory.
* If a sort contains reference to an object from an Excel data source, then all sorting will occur in-memory.
* If no sorts exist on a report then no SQL will be appended to the query.
* Boolean expressions will prioritize *False* values when set to ascending and *True* values when set to descending.
* If sorts that cannot be properly translated to SQL exist on a report, then SQL statements will be generated and appended to the database query up to the sort that cannot be translated. For example, if the third sort on a report is untranslatable, then only the first two sorts will be translated and appended.
* Calculations that are pushed to the database may differ in comparison to those run in-memory by Exago. For example, pi (π) is rounded to the 15th digit in Exago but is only rounded to the 6th digit in MySQL by default. These differences in calculations vary depending on the database type and should be taken into consideration when enabling this feature.
