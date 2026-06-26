---
title: "Assembly Data Sources"
id: 5281582189591
section: "Installation and Configuration"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281582189591-Assembly-Data-Sources
updated_at: 2023-04-03T17:52:19Z
---

# Assembly Data Sources

# Assembly Data Sources

Exago BI supports the ability to retrieve data from .NET assemblies. **Assembly Data Sources** are custom programmatic .NET Framework binaries for transforming and exposing arbitrary data in a format that can be read by Exago BI.

Assembly Data Sources can be used as data connectors and drivers for unconventional data sources. They can also be used as Extract, Transform, Load (ETL) layers for processing, combining, and caching data before it reaches the reporting engine. This topic describes how to write custom .NET Assembly Data Sources for Exago BI.

Assembly Data Sources must be written for and compiled with [supported versions of the .NET Framework](https://devnet.logianalytics.com/hc/en-us/articles/5281616408727-Technical-Specifications), and must be compiled as a class library (.dll).

## Interface

Assembly Data Sources must implement the following interface.

The entry point or points for Exago BI are public static methods, which accept at minimum an integer *Call Type* parameter and return an ADO.NET **[`System.Data.DataSet`](https://msdn.microsoft.com/en-us/library/system.data.dataset(v=vs.110).aspx)** object. The *Call Type* parameter name must be defined in **Admin Console** > **General** > **Programmable Object Settings** > **Call Type Parameter Name**.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Although the return type is a DataSet, each Assembly Data Source method is expected to return only a single data table. This is usually done by merging in a **[`System.Data.DataTable`](https://msdn.microsoft.com/en-us/library/system.data.datatable(v=vs.110).aspx)** object which has a schema and has been populated with data.
>
> If a DataSet with multiple tables is returned, only the first one will be recognized.

Entry methods can optionally accept some or all other parameters described in the **Programmable Object Settings**, in order to have additional context for the method call. All the parameters in use must have defined names in the **Admin Console**.

Entry methods may also access a **WebReports.Api.Common SessionInfo object**. This contains the active session’s configuration settings and references to the active API objects. It can be used to identify properties as well as mutate session state. An assembly reference to `bin\WebReportsApi.dll` is required for the **SessionInfo** class definition.

### Method Examples

Considering the following parameter names defined in **Admin Console** > **General** > **Programmable Object Settings**:

* **Call Type Parameter Name**: *CallType*
* **Column Parameter Name**: *Columns*
* **Filter Parameter Name**: *Filter*

The following are a few examples of valid entry method signatures:

* ```
  public static DataSet Method(int CallType)
  ```
* ```
  public static DataSet Method(int CallType, string Columns, string Filter)
  ```
* ```
  public static DataSet Method(int CallType, string Columns = "")
  ```
* ```
  public static DataSet Method(SessionInfo Session, int CallType)
  ```
* ```
  public static object Method(SessionInfo Session, object CallType)
  ```

There can be more than one entry method. Each public static method in the class will appear as a virtual table when adding the Assembly Data Source in the Admin Console.

Alternatively, one method can support multiple tables by incorporating the **Object ID** parameter, which passes the object ID as defined in the configuration. See [Handling Multiple Data Tables](#Handling).

#### Additional Notes

1. Methods cannot be overloaded, as it will be ambiguous which one Exago BI should use.
2. For security reasons, only the entry methods in the class should be public, so that any other utility or methods are not erroneously visible in the Admin Console.

### Class Definition

The entry methods must reside within a public class (non-static) within a defined namespace. The class must be at the top level of the namespace, not within another class. Its default constructor must be public (defining the constructor is optional).

#### Example

```
namespace AssemblyDataSource {
    public class Tables {
        public Tables() { ... } /* optional */
        public static DataSet EntryMethod(...) {...}
    }
}
```

## Implementation

Each Assembly Data Source query is a discrete atomic operation. While Exago BI can optionally cache the assembly in memory, the application will not maintain a connection between queries. Unless you store application state on disk, queries will have no knowledge of each other.

Assembly Data Source method calls are synchronous, meaning that the main application thread will wait until the method returns before continuing.

Exago BI queries Assembly Data Sources for three distinct reasons:

* **Schema**: The column/field names and data types. This is called whenever the schema needs to be retrieved (such as expanding a Data Object’s fields in the ExpressView data objects pane) and the **[Schema Access Type](https://devnet.logianalytics.com/hc/en-us/articles/5281608202519-Data-Objects#Schema)** is set to *Datasource*. The frequency of schema calls can be significantly reduced by specifying a static schema for the Assembly Data Source in the [**Column Metadata**](https://devnet.logianalytics.com/hc/en-us/articles/5281608202519-Data-Objects#Column2).
* **Data**: The data values for the table. This is called whenever a report is executed.
* **Filter values**: Data values for a single column, possibly filtered by an input string. This is called when values need to be populated for a filter dropdown list.

Each type of query requires a different amount of information to be returned. The **Programmable Data Object** parameters are passed alongside each query to indicate the information that Exago BI is expecting. With this in mind, you can write ADS with certain optimizations to improve performance. It is highly recommended to use the Programmable Data Object parameters for this reason.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> If performance is a strict concern, consider that databases will almost always be more performant for large data sets than Assembly Data Sources.

See [Optimizing for Query Types](#Optimizi).

### Data Format

Exago BI expects an ADO.NET DataSet object to be returned from the Assembly Data Source method. A DataSet is an in-memory representation of a relational data model.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> To return no data, for any reason, construct and return a DataSet with the schema and no rows. Sending null or an empty schema will cause an exception to be thrown.

Exago BI reads only the first DataTable in a set, at index `DataSet.Tables[0]`, regardless of the number of tables comprising the set. To return multiple tables from an ADS, return a different DataSet depending on an input parameter or method name. See [Handling Multiple Data Tables](#Handling).

See **[DataSets, DataTables, and DataViews](https://docs.microsoft.com/en-us/dotnet/framework/data/adonet/dataset-datatable-dataview/index)** for the ADO.NET DataSet documentation.

### Optimizing for Query Types

Avoid retrieving the full data set whenever possible. This is usually the most computationally intensive query task. A number of Programmable Object Parameters are passed to the Assembly Data Source in order to determine the amount of processing required for each query.

![The ADS query types, what data they expect, and how the data is processed by Exago](https://devnet.logianalytics.com/hc/article_attachments/5432288117527/adsdiagram.png)

The ADS query types, what data they expect, and how the data is processed by Exago BI

#### Using the Call Type Parameter

**Call Type** is an integer parameter, with value 0 for a schema query, 1 for a data set query, and 2 for a filter values query.

Schema queries are expected to be quick, and do not require the actual data table. Returning a static schema is the most performant way to handle this. Do not make the application wait to populate the full table.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
>
> It is highly recommended to set the [**Schema Access Type**](https://devnet.logianalytics.com/hc/en-us/articles/5281608202519-Data-Objects#Schema) for the Assembly Data Source to *Metadata* in order to eliminate schema queries to the data source. This will significantly improve the responsiveness of the user interface.

Filter values query a single data column, with a text filter applied to limit the number of values returned. Therefore this call type works best with the Column and Filter parameters.

#### Column, Filter, and Full Filter Parameters

For data queries (Call Type 1), it is not strictly necessary to implement these parameters to filter the data in the Assembly Data Source, because Exago BI filters the data regardless once it is returned to the application.

### Suppressing Application Filtering & Sorting v2018.1

You have the option to suppress the default application filtering and sorting of data returned for data queries. You can choose to filter and sort in the Assembly Data Source code instead, which allows for more control over the manner in which these processes are done.

To suppress application filtering and sorting for selected objects, set the[**Suppress Sort and Filter** setting for each Data Object in the Admin Console](https://devnet.logianalytics.com/hc/en-us/articles/5281608202519-Data-Objects#Suppress) to *True*for each object.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
>
> Suppression only occur for reports where the object is joined exclusively to zero or more programmable objects which also have suppression enabled. In-memory processing such as advanced joins, Special Cartesian processing, and sort and filter formulas will override this setting and force application processing to occur.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> Exago BI will not filter the dropdown values for filter values queries (Call Type 2) by default. It is highly recommended to apply filtering for these queries in the Assembly Data Source to avoid inaccurate and potentially insecure behavior for the filter dropdown lists. Therefore, these parameters should not be seen as optional for all but the most trivial applications.

The following table shows the parameter values for either data or filter values queries.

| Call Type | 1 Data | 2 Filter values |
| --- | --- | --- |
| Column | List of requested column database names  “col1,col2,col3” | Requested column database name  “col2” |
| Filter | Data object filter SQL  “(col1 = ‘value’) AND (tenantId = ‘id’)” | Filter dropdown value  “value” |
| Full Filter | Report filter SQL  “([obj].[col1] = ‘value’) AND ([obj].[tenantId] = ‘id’)” | Tenant and row-level filter SQL  “([obj].[tenantId] = ‘id’)” |
| Sort | Sort SQL  “col3 asc, col1 desc” | Sort SQL  “col3 asc, col1 desc” |
| Expected Return | DataSet with requested columns, optionally filtered | DataSet with single column, filtered |

The Column parameter will give the list of fields necessary for a report execution (data query) or the field requested by a filter dropdown (filter values query). It may be more performant to build the DataSet with only the requested columns.

Filtering for data queries is only required if the **Suppress Sort and Filter** setting (*v2018.1+*) is *True*. Otherwise Exago BI automatically filters the data set in memory for data queries.

You must apply filtering for filter value queries.

What is a filter values query?

Several activities in the application involve querying a table for a list of values from a single field, possibly filtered by a user input string. This occurs when users interact with filter dropdowns, so that they can view and select valid field data when creating report filters.

![Dropdown.png](https://devnet.logianalytics.com/hc/article_attachments/5432220673431/dropdown.png)

Example of interaction with a filter dropdown

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Report Viewer and Dashboard interactive filters are populated by the data query for the report execution, not by a separate filter values query.

You can prevent this type of query entirely by setting the **Admin Console** > ![TreeGeneral.png](https://devnet.logianalytics.com/hc/article_attachments/5432174178839/treegeneral.png)**General** > ![TreeGeneralNode.png](https://devnet.logianalytics.com/hc/article_attachments/5432159353239/treegeneralnode.png)**Filter Settings** > **Read Database for Filter Values** setting to *False.*

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> It is not possible to implement Filter Dependencies in an Assembly Data Source.

Typing into a filter dropdown field causes it to return values filtered by the input text. This filtering must be done manually in the Assembly Data Source for two reasons:

1. **Accuracy**— Dropdown lists are not filtered by Exago BI, so typing to filter will be ineffective if not implemented manually.
2. **Security** — Row and column tenancy filters must be applied to the dropdown list so that users cannot view data values without access rights.

The **Column**, **Filter**, **Sort** and **Full Filter** parameters must be combined together to generate the proper filtering. With Call Type 2, the **Column** parameter contains the name of the requested data field, and the **Filter** parameter contains the input text. These can be combined to generate the necessary SQL `WHERE` clause.

**Example:**

```
string SQL = string.Format("(CONVERT({0}, System.String) LIKE '%{1}%')", Columns, Filter);
// Note: DateTime columns should use a different comparison
```

The **Full Filter** parameter already contains the necessary tenancy SQL specified in the data object and active role settings, so this can be easily added to the input filter SQL to create the full clause. Then apply it to the data set and return only the resulting rows.

As of *v2019.1.11+* the **Sort** Parameter can be used to indicate in which direction the user is scrolling a filter dropdown. ASC indicates scrolling down or DESC indicates scrolling up.

```
SQL += " AND " + FullFilter + Sort;
DataRow[] DropdownRows = FullTable.Select(SQL);
// Note: In a proper implementation be sure to sanitize the SQL before passing it to the db
```

#### Additional Considerations

* DateTime comparisons should be handled in a different manner than with a `LIKE` operator.
* Only distinct values are shown in the dropdown, so there is no need to use a `DISTINCT` clause in the SQL statement.
* A maximum of 100 values are shown in the list. You can choose to implement a `TOP 100` clause, if it would improve performance.
* As of Exago BI*v2017.3+*, for database sources, end-users have the option of selecting whether their filter dropdown input should apply a Starts With or Contains rule to the data field filter. This behavior cannot currently be implemented in an Assembly Data Source, because the value of this setting is not passed in a parameter.
* As of *v2017.3+*, values are queried incrementally as the user scrolls the dropdown list, for supported sources. This is also not currently supported by Assembly Data Sources.

### Sort Parameter

It is only required to sort in an Assembly Data Source if the **Suppress Sort and Filter** setting (*v2018.1+*) is set to *True* for the Data Object associated with it. Otherwise Exago BI automatically sorts the data set in memory for data queries.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> Formula sorts use the application’s internal formula engine. It is impossible to handle formula sorts in an Assembly Data Source code.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> The Sort parameter is irrelevant for filter values queries. Filter values are always sorted in ascending order.

### Handling Multiple Data Tables

There are two ways which an Assembly Data Source can allow for multiple data tables to be returned as separate objects in the Exago BI data model. The first involves using multiple entry methods. The second involves specifying table names in the metadata.

#### Multiple Methods

Separate tables can be implemented as separate entry methods within the ADS. This has several advantages:

* Each public method from a source will appear as a “table” in the **Admin Console** when adding objects to the data model.
* Method names can describe the tables in a self-documenting manner.

##### Example:

```
/* Public methods seen by Exago BI */
public static DataSet EmployeeTable(int call) { return GetTableData("Employee", call); }
public static DataSet ProductsTable(int call) { return GetTableData("Products", call); }
/* Common data retrieval method */
private static DataSet GetTableData(string tableName, int call) { ... }
```

However, this does not allow retrieval of previously undefined tables without editing the Assembly Data Source and adding additional methods in support. So for a database where objects are likely to be added, programmatic maintenance of the Assembly Data Source will be required.

#### Single Method with Parameters

The Data Object and Data Object ID parameters correspond to the user-input metadata fields *Category* and *ID* (respectively) in each data object’s properties in the **Admin Console**. The ID field, in particular, can accept arbitrary input without affecting the user interface. So table names or identifiers can be defined in the ID field. Thus, one entry method can support multiple tables based on a conditional string from the metadata. This allows an Assembly Data Source to support a more dynamic data structure, since any subsequent tables can be added simply by editing the metadata.

##### Example:

```
public static DataSet GetTableData(string objectId, int call)
{
    switch (objectId)
    {
        case "Employee": { ... }
        case "Products": { ... }
        default: { throw ... }
    }
}
```

However, adding metadata elements to the config can be error-prone, so ensure that admins always have the up-to-date mapping of IDs to tables.

## Configuration

Once written, the following steps are taken for Exago BI to access the Assembly Data Source.

1. Ensure that the assembly is in a location accessible by the IIS application pool user (and the Scheduler Service, if in use) with read and execute permissions.
2. Add the Assembly Data Source to the Admin Console Data Sources (with `Type=Assembly`) using the following connection string format:

   ```
   assembly=pathtoassembly.dll;class=Namespace.Class
   ```
3. Click the **Test ![connectionverification.png](https://devnet.logianalytics.com/hc/article_attachments/5432286089623/connectionverification.png)**icon to verify that the assembly and class are accessible.
4. Define the method parameter names in the **Programmable Object Settings**.
5. Add the entry methods to the **Admin Console** Data Objects, then add any relevant joins and metadata aliasing.

## Maintenance

There are several notes to keep in mind when updating an ADS and/or updating Exago BI.

### System Locks

The web server maintains a lock on the assembly as long as it is running. Additionally, if using any classes in the **`WebReports.Api.Scheduler`** namespace, or if there are any scheduled or **cached** reports that use the Assembly Data Source, the Scheduler Services lock it as well.

Therefore, when updating the Assembly Data Source, the web server and Scheduler Services will need to be disabled while the file is replaced.

### WebReportsApi.dll Version

If you are using `SessionInfo` or any other Exago .NET API classes, the Assembly Data Source must be recompiled with the new version of the WebReportsApi.dll assembly whenever Exago BI is updated.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Utility libraries, such as SQLUtils.dll are updated less frequently than the main web application binaries. Even if only referencing utilities, verify nevertheless that the Assembly Data Source works without needing recompilation.

## Example

The following example is provided for reference. While trivial, the example is fully working and demonstrates a typical Assembly Data Source framework. It can be freely used, extended, and redistributed for any custom implementation.

[Assembly Data Source example implementation](https://devnet.logianalytics.com/hc/article_attachments/5432266392343/sampleads.zip "Download the Assembly Data Source example implementation")
