---
title: "Constants and Enumerators"
id: 5281610137879
section: "REST Web Service API"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281610137879-Constants-and-Enumerators
updated_at: 2022-05-03T22:07:52Z
---

# Constants and Enumerators

# Constants and Enumerators

There are many variables in the APIs that require a specific type of value from a set of values. These sets of values are called *enumerated types*, and each value in a type is called an enumerator, or *enum*. Enumerated types are no more than a set of named values, which act as constants in the API.

When an API variable requires an enum, it must be set to one of the constants that are defined in the specified enumerated type. For example, if a variable requires a Report Type enum, it accepts the values *Advanced*, *Express*, *Dashboard*, *Chained* or *ExpressView*. Other values will cause an invalid type error.

Some API variables are not enumerated types, but may require a set of constants regardless. These constants have no numeric equivalent.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> Numeric values should not be used as enum types as these values are not constants.

## wrApiAction

| Enum Name | Numeric Value | Description |
| --- | --- | --- |
| Default | 0 | If a report is loaded, this is equivalent to ExecuteReport. Otherwise, this is equivalent to Home. |
| Home | 1 | Open the home page. |
| ExecuteReport | 2 | Execute the loaded report (specify format with [wrExportType](#wrExport)). |
| EditReport | 3 | Open the loaded report in the appropriate editor. |
| NewAdvancedReport | 4 | Open the New Advanced Report Wizard. |
| *NewReport* | 4 | *Deprecated*: Use NewAdvancedReport instead. |
| NewCrossTabReport | 5 | Open the New CrossTab Report Wizard. |
| NewExpressReport | 6 | Open the New Express Report Wizard. |
| NewDashboardReport | 7 | Open the Dashboard Designer for a new Dashboard. |
| NewExpressView | 8 | Open the ExpressView Designer for a new ExpressView. |
| ScheduleReport | 9 | Open the Schedule Report Wizard for the loaded report. |
| ScheduledReportsManager | 10 | Open the Scheduled Report Manager. |

## Cache Visibility Level

| Enum Name | Numeric Value | Description |
| --- | --- | --- |
| User | 1 | Cache visibility set at the UserId parameter level |
| Company | 2 | Cache visibility set at the CompanyId parameter level |
| Global | 3 | Global cache visibility |

## Code Language

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Each value has multiple names.

| Enum Name | Numeric Value | Description |
| --- | --- | --- |
| c# cs csharp | 0 | C Sharp |
| js javascript | 1 | JavaScript |
| vb visualbasic | 2 | Visual Basic |

## wrContentType v2020.1+

| Enum Name | Numeric Value | Description |
| --- | --- | --- |
| Report | 0 | Item is a report. |
| Folder | 1 | Item is a folder. |
| Theme | 2 | Item is a chart or map theme. |
| Template | 3 | Item is a template file. |
| All | 99 | Reference all content types. |

## ContentPermission v2021.1+

The **ContentPermission** enumeration was updated in *v2021.1*. Review [Access Flags v2021.1+](https://devnet.logianalytics.com/hc/en-us/articles/5281647019287-Storage-Management-Introduction#Access) for more detailed descriptions of each of these access flags and their impact on the user experience.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
>
> To determine the `content_access.access_flags` value, sum the decimal values of the desired flags from the table below. For example, to only allow renaming and deleting, the value is *20* since *4+16=20*.

| Enum Name | Numeric Value | Description |
| --- | --- | --- |
| None | Hex: 0x0000 Dec: 0 | User has no access to the content. |
| CanEdit | Hex: 0x0001 Dec: 1 | User can edit the content. |
| Reserved | Hex: 0x0002 Dec: 2 | This enum is reserved for future use. |
| CanRename | Hex: 0x0004 Dec: 4 | User can rename the content. |
| CanShare | Hex: 0x0008 Dec: 8 | User can share the content. |
| CanDelete | Hex: 0x0010 Dec: 16 | User can delete the content. |
| Reserved | Hex: 0x0020 Dec: 32 | This enum is reserved for future use. |
| CanCopy | Hex: 0x0040 Dec: 64 | User can duplicate the content. |
| Reserved | Hex: 0x0080 Dec: 128 | This enum is reserved for future use. |
| CanView | Hex: 0x0100 Dec: 256 | The content appears in the user’s Report Tree. |
| CanSchedule | Hex: 0x0200 Dec: 512 | The user may schedule or email the report. |
| CanMove | Hex: 0x0400 Dec: 1024 | The user may move this item to another folder. |
| FullAccess | Hex: 0xFFFF Dec: 65535 | All access is granted. |
| ReadOnly | Hex: 0x0348 Dec: 840 | The user may view, copy, schedule it and share the item but nothing else. |

## ContentPermission v2020.1–v2021.1

Used in the Storage Management system for *v2020.1—v2021.1*. Review [Access Flags v2020.1–v2021.1](https://devnet.logianalytics.com/hc/en-us/articles/5281647019287-Storage-Management-Introduction#Access2) for more detailed descriptions of each of these access flags and their impact on the user experience. For the **ContentPermission** enumeration in *v2021.1+*, see [ContentPermission v2021.1+](#ContentP) above.

| Enum Name | Numeric Value | Description |
| --- | --- | --- |
| None | Hex: 0x0000 Dec: 0 | User has no access to the content. |
| CanEdit | Hex: 0x0001 Dec: 1 | User can edit the content. |
| CanSave | Hex: 0x0002 Dec: 2 | User can save the content. |
| CanRename | Hex: 0x0004 Dec: 4 | User can rename the content. |
| CanShare | Hex: 0x0008 Dec: 8 | User can share the content. |
| CanDelete | Hex: 0x0010 Dec: 16 | User can delete the content. |
| CanExecute | Hex: 0x0020 Dec: 32 | User can delete the content. |
| CanCopy | Hex: 0x0040 Dec: 64 | User can duplicate the content. |
| CanDownload | Hex: 0x0080 Dec: 128 | User can download the content. |
| CanView | Hex: 0x0100 Dec: 256 | The content appears in the user’s Report Tree. |
| FullAccess | Hex: 0xFFF Dec: 65535 | All access is granted. |

## Data Source Type

| Enum Name | Numeric Value | Description |
| --- | --- | --- |
| MsSql | 0 | Microsoft SQL Server |
| MySql | 1 | MySQL |
| ODBC | 2 | ODBC |
| Postgres | 3 | PostreSQL |
| Oracle | 4 | Oracle |
| DB2 | 5 | IBM DB2 |
| Informix | 6 | IBM Informix |
| Assembly | 7 | .NET Assembly |
| WebService | 8 | Web Service |
| File | 9 | Excel file |
| MsOlap | 10 | OLAP |
| Sqlite | 11 | SQLite v2021.1.8+ |

## DataType

The **DataType** enumeration is used in the REST Web Service API when processing [Column Metadata](https://devnet.logianalytics.com/hc/en-us/articles/5281608202519-Data-Objects#Column) and when getting the value of the EntityColumn.DataTypeEnum property in the .NET API.

| Enum Name | Numeric Value | Description |
| --- | --- | --- |
| String | 0 | String |
| Date | 1 | Date, that is day, month, year |
| DateTime | 2 | Date & time |
| Time | 3 | Time, that is hour, minute, second (am/pm) |
| Integer | 4 | Integer number |
| Decimal | 5 | Decimal number |
| Float | 6 | Floating-point number |
| Bit | 7 | Bit |
| Guid | 8 | Globally (universally) unique identifier, aka. UUID |
| Image | 9 | Image |
| Currency | 10 | Currency |

## DataType

The **DataType** constants are used throughout the application including when defining the return type (the `<return_data_type>`) of Quick Functions.

| Constant Name | Integer Value | Description |
| --- | --- | --- |
| StringDataType | 0 | A string |
| DateDataType | 1 | A date |
| IntegerDataType | 2 | An integer |
| OldBitDataType | 3 | Deprecated — a single bit. Users should use BitDataType (13) instead |
| NumericDataType | 4 | A number |
| FloatDataType | 5 | A floating point number |
| DecimalDataType | 6 | A decimal number |
| GuidDataType | 7 | Globally (universally) unique identifier, aka. UUID |
| DateTimeDataType | 8 | A DateTime |
| TimeDataType | 9 | Time — this data type is currently not in use in the application |
| ImageDataType | 10 | An binary image |
| CurrencyDataType | 11 | A currency value |
| AmbiguousFormulaDataType | 12 | A formula returns a different data type based on its outcome (for example `=if(temperature > 98.6, temperature, false)` |
| BooleanDataType | 13 | A Boolean (true/false) value |
| BitDataType | 13 | A single bit |

## DataObjectType

| Constant Name | Description |
| --- | --- |
| Assembly | .NET Assembly |
| File | Excel file |
| Function | User-defined function |
| Procedure | Stored procedure |
| SqlStmt | Custom SQL statement |
| Table | Data table |
| View | SQL view |
| WebSvc | Web Service method |
| MdxStmt | OLAP MDX query |

## DashboardLayoutFit

| Enum Name | Description |
| --- | --- |
| All | All tiles are resized horizontally and vertically to fit on the canvas  Same as selecting **Scale to Screen** in the Dashboard Designer Canvas Format menu |
| Width | Tiles are resized horizontally to fit within a specified canvas width  Same as selecting **Specify Height** in the Dashboard Designer Canvas Format menu |
| None | The tiles are not resized. The canvas has a specified height and width  Same as selecting **Specify Height and Width** in the Dashboard Designer Canvas Format menu |

## wrDockLocation

Used to set the location of the interactive dock in the Report Viewer with the .NET API’s `SetupData.General.DockPlacement` setting.

| Enum Name | Numeric Value | Description |
| --- | --- | --- |
| Left | 0 | The pane is docked on the left. |
| Right | 1 | The pane is docked on the right. |

## ExecuteDataType v2021.1+

Used in the REST Web Service API GetExecute() methods to determine how to return the data to the host application.

| Enum Name | Numeric Value | Description |
| --- | --- | --- |
| Auto | 0 | Automatically determine the appropriate return data action. This is the default if no other value is explicitly chosen. |
| Data | 1 | Return a base64 encoded representation of the output file. To display the output data, process the information from the ExecuteData property and send it to the browser. When deploying Exago in a web farm architecture, this is the only acceptable value when using GetExecute() methods. |
| Url | 2 | Return a URL that can be passed back to the browser. The browser can then display or download the resulting file. |

## ExportFlag v2020.1+

Used in the Storage Management System.

| Enum Name | Numeric Value | Description |
| --- | --- | --- |
| Default | 0 | Use the system default export type. |
| None | 0 | There is no default export type, so revert to the system default. |
| Html | 1 | Run in the browser, using the appropriate viewer. |
| Pdf | 2 | Export as a PDF file. |
| Rtf | 4 | Export as an RTF file. |
| Csv | 8 | Export as a comma-separated value text file. |
| Excel | 16 | Export as a Microsoft Excel workbook. |

## wrExportType

| Enum Name | Numeric Value | Description |
| --- | --- | --- |
| Html | 0 | Run in the browser, using the appropriate viewer. |
| Excel | 1 | Export as an Excel file. |
| Pdf | 2 | Export as a PDF file. |
| Rtf | 3 | Export as an RTF file. |
| Csv | 4 | Export as a comma-separated value text file. |
| Word | 5 | Export as a Word file. |
| Default | 6 | Default type specified by the loaded report; if not specified, default type specified by the current config. |
| PdfSnapshot | 10 | Export a Dashboard screenshot as a PDF file. See [Exporting Dashboards (v2019.2+)](https://devnet.logianalytics.com/hc/en-us/articles/5281619023767-Exporting-Dashboards-v2019-2-) for more information. |

## Filterable Type

| Enum Name | Description |
| --- | --- |
| All | Field supports all filter types |
| True | Field supports all filter types |
| None | Field cannot be filtered |
| False | Field cannot be filtered |
| Dynamic | Field supports only dynamic (interactive) filters |
| Static | Field supports only static (report) filters |

## Filter Operator Type

| Enum Name | Numeric Value | Description |
| --- | --- | --- |
| EqualTo | 0 | Data value is equal to the filter value |
| NotEqualTo | 1 | Data value is less than the filter value (number, date) |
| LessThan | 2 | Data value is less than or equal to the filter value (number, date) |
| LessThanOrEqualTo | 3 | Data value is greater than the filter value (number, date) |
| GreaterThan | 4 | Data value is greater than or equal to the filter value (number, date) |
| GreaterThanOrEqualTo | 5 | Data value is not equal to the filter value |
| StartsWith | 6 | Data value starts with the filter value (string, number) |
| NotStartsWith | 7 | Data value does not start with the filter value (string, number) |
| EndsWith | 8 | Data value ends with the filter value (string, number) |
| NotEndsWith | 9 | Data value does not end with the filter value (string, number) |
| Contains | 10 | Data value contains the filter value (string, number) |
| NotContains | 11 | Data value does not contain the filter value (string, number) |
| Between | 12 | Data value is between the two filter values |
| NotBetween | 13 | Data value is not between the two filter values |
| OneOf | 14 | Data value is equal to one of the filter values |
| NotOneOf | 15 | Data value is not equal to any of the filter values |

## FolderStatus

| Enum Name | Description |
| --- | --- |
| Exists | This folder exists |
| DoesNotExist | This folder does not exist |
| Created | This folder was successfully created |
| Deleted | This folder was successfully deleted |
| Renamed | This folder was successfully renamed |

## JobStatus v2019.2+

A read-only property showing the current status of a schedule. Used in [REST — SchedulesV2](https://devnet.logianalytics.com/hc/en-us/articles/5281646521623-REST-SchedulesV2).

| Enum Name | Numeric Value | Description |
| --- | --- | --- |
| Ready | 0 | The schedule will run at its next scheduled run time. |
| Running | 1 | The schedule is currently running and the reports are executing. |
| Completed | 2 | The schedule has completed its final event, and will not run again. It will be removed from the list when the scheduler is flushed. |
| Suspended | 3 | The schedule has been suspended and will not be run again. |
| Deleted | 4 | The schedule has been deleted, and will be removed from the list when the cache is flushed. |
| Abended | 5 | The last run failed due to an error. The schedule will not run again. |
| UserAbort | 6 | Schedule is running, but user has requested to delete it. |
| Transmitting | 7 | Schedule is finished and waiting for data to be transmitted to client for synchronous execution. |
| Removed | 8 | Schedule should be removed if it hasn’t already. |
| Immediate | 9 | As soon as resources are available, the schedule will be run. |
| Timedout v2019.2.32+v2020.1.15+v2021.1.3+ | 10 | The job has hit the execution time out set in the Scheduler Service’s configuration file. |

## Join Type

| Enum Name | Description |
| --- | --- |
| Inner | Inner join |
| LeftOuter | Left outer join |
| RightOuter | Right outer join |
| FullOuter | Full outer join (left outer join + right outer join) |

## Join Relation Type

| Enum Name | Description |
| --- | --- |
| OneToOne | One-to-one relationship |
| OneToMany | One-to-many relationship |

## Parameter Type

| Enum Name | Numeric Value | Description |
| --- | --- | --- |
| String | 0 | String |
| Date | 1 | Date, that is day, month, year |
| Integer | 2 | Integer number |
| Decimal | 3 | Decimal number |

## QuickFunctionDataType v2021.1+

Used for defining the input type (the `<supported_data_types>`) of a Quick Function.

| Enum Name | Description |
| --- | --- |
| Date | A Date or DateTime |
| Number | A numeric value |
| Text | Text |

## wrRowRangeSqlMethod

Used in the `dbconfigs.json` file. See [Managing the dbconfigs.json File](https://devnet.logianalytics.com/hc/en-us/articles/5281593110167-Managing-the-dbconfigs-json-File).

| Enum Name | Description |
| --- | --- |
| None | Disable range limiting SQL. |
| LimitOffset | `SELECT ... LIMIT rangeSize OFFSET offsetRow` |
| OffsetFetch | `SELECT ... OFFSET offsetRow ROWS FETCH NEXT rangeSize ROWS ONLY` |
| RowNumberWithTop | `SELECT TOP endingRow ROW_NUMBER() Over(Order By (...)) as wrRowNum ... as wrRowNumbered WHERE wrRowNumbered.wrRowNum BETWEEN startingRow AND endingRowField` |
| RowNumber | `SELECT ROW_NUMBER() Over(Order By (...)) as wrRowNum ... as wrRowNumbered WHERE wrRowNumbered.wrRowNum BETWEEN startingRow AND endingRowField` |
| RowNumberNoAlias | `SELECT ROW_NUMBER() Over(Order By (...)) as wrRowNum ... WHERE wrRowNum BETWEEN startingRow AND endingRowField` |

## RecurrenceRange v2019.2+

Determines the ending of a scheduled report recurrence. Used in [REST — SchedulesV2](https://devnet.logianalytics.com/hc/en-us/articles/5281646521623-REST-SchedulesV2).

| Enum Name | Description |
| --- | --- |
| NoEndDate | This schedule has no end date and will recur indefinitely. |
| EndAfterNOccurences | This schedule shall run only for a specified number of instances. The number of instances is specified in the OccurencesToEnd property. |
| EndByDate | This schedule shall run until a specified date is reached. The date is specified in the RangeEndDate property. |

## RecurrenceType v2019.2+

Determines the frequency of scheduled report recurrence. Used in [REST — SchedulesV2](https://devnet.logianalytics.com/hc/en-us/articles/5281646521623-REST-SchedulesV2).

| Enum Value | Description |
| --- | --- |
| Once | This schedule will only run one time. |
| Daily | The schedule will repeat every day, every weekday, or every number of days. |
| Weekly | The schedule will repeat every week, or every number of weeks, on one or more days |
| Monthly | The schedule will repeat every month, or every number of months, on a certain day. |
| Yearly | The schedule will repeat every year on a certain day. |

## wrReportType

| Enum Name | Numeric Value | Description |
| --- | --- | --- |
| Advanced | 0 | Advanced Report (CrossTab Reports are also considered Advanced Reports) |
| *Standard* | 0 | *Deprecated*: Use Advanced instead. |
| Express | 1 | Express Report |
| Dashboard | 2 | Dashboard |
| Chained | 3 | Chained Report |
| ExpressView | 5 | ExpressView |
| Folder | 6 | Report Folder |

## ReportValidationErrorType

The types of report validation errors that can happen. Not all validation error types are applicable to all report objects.

| Enum Name |
| --- |
| SortFormulaSyntaxError |
| FilterFormulaSyntaxError |
| DataObjectNotFound |
| SortDataFieldNotFound |
| FilterDataFieldNotFound |
| LinkedDataFieldNotFound |
| MinMaxFilterDataFieldNotFound |
| JoinDataObjectNotFound |
| JoinNotFound |
| JoinDataFieldNotFound |
| ChartDataFieldNotFound |
| MapDataFieldNotFound |
| CellDataFieldNotFound |
| RowGroupNameNotFound |
| RowGroupFormulaNameNotFound |
| ChartCellIdNotFound |
| MapCellIdNotFound |
| MergedCellsAcrossSections |
| CrossTabIdNotFound |
| CrossTabCellIdNotFound |
| ColumnSortByFieldNotFound |
| ChildReportNotFound |
| ExpressViewColumnMissingEntity |
| ExpressViewColumnMissingField |
| ExpressViewGroupMissingField |
| ExpressViewFilterMissingField |
| ExpressViewChartMissingField |
| EtlReportDesignerModeNotEtl |
| EtlReportTypeNotAdvanced |
| EtlDataTypeNotSet |
| EtlDataTypeNotFound |
| EtlReportFormatInvalid |
| EtlCellBlank |
| EtlHeaderCellValueDuplicate |
| EtlPossibleDataTypeError |
| EtlCellSpan |
| None |
| ReportParameterNameUsed |

## ScheduleExportType v2019.2+

The export type for a report run on a schedule. Used in [REST — SchedulesV2](https://devnet.logianalytics.com/hc/en-us/articles/5281646521623-REST-SchedulesV2).

| Enum Name | Description |
| --- | --- |
| Pdf | Export as a PDF file. |
| Rtf | Export as an RTF file. |
| Excel | Export as a Microsoft Excel workbook file. |
| Csv | Export as a CSV text file. |

## ScheduleFilterOperator v2019.2+

Utilized when adding filters to scheduled reports via the REST Web Service API. Used in [REST — SchedulesV2](https://devnet.logianalytics.com/hc/en-us/articles/5281646521623-REST-SchedulesV2).

| Enum Name | Description |
| --- | --- |
| EqualTo | Evaluates as *true* when **FilterText** is equal to **Values**, otherwise *false*. |
| NotEqualTo | Evaluates as *true* when **FilterText** is not equal to **Values**, otherwise *false*. |
| LessThan | Evaluates as *true* when **FilterText** is less than **Values**, otherwise *false*. |
| LessThanOrEqualTo | Evaluates as *true* when **FilterText** is less than or equal to **Values**, otherwise *false*. |
| GreaterThan | Evaluates as *true* when **FilterText** is greater than **Values**, otherwise *false*. |
| GreaterThanOrEqualTo | Evaluates as *true* when **FilterText** is greater than or equal too **Values**, otherwise *false*. |
| StartsWith | Evaluates as *true* when **FilterText** starts with **Values**, otherwise *false*. |
| NotStartsWith | Evaluates as *true* when **FilterText** does not start with **Values**, otherwise *false*. |
| EndsWith | Evaluates as *true* when **FilterText** ends with **Values**, otherwise *false*. |
| NotEndsWith | Evaluates as *true* when **FilterText** does not end with **Values**, otherwise *false*. |
| Contains | Evaluates as *true* when **Values** is contained within **FilterText**, otherwise *false*. |
| NotContains | Evaluates as *true* when **Values** is not contained within **FilterText**, otherwise *false*. |
| Between | Evaluates as *true* when **FilterText** is between two values contained in **Values**, otherwise *false*. |
| NotBetween | Evaluates as *true* when **FilterText** is not between two values contained in **Values**, otherwise *false*. |
| OneOf | Evaluates as *true* when **FilterText** matches at least one of **Values**, otherwise *false*. |
| NotOneOf | Evaluates as *true* when **FilterText** does not match any of **Values**, otherwise *false*. |

## ScheduleJobType v2019.2+

A read-only property that shows the type of job assigned to a schedule. Used in [REST — SchedulesV2](https://devnet.logianalytics.com/hc/en-us/articles/5281646521623-REST-SchedulesV2).

| Enum Name | Description |
| --- | --- |
| Report | This job runs a report. |
| Batch | This job runs a batch report. |
| Email | This job handles the disposition of a **Report** or **Batch** job by sending the output as an email. |
| Disk | This job handles the disposition of a **Report** or **Batch** job by saving the output to disk. |

## ScheduleRecurrenceType v2019.2+

A read-only property that shows the type of job recurrence assigned to a schedule. Used in [REST — SchedulesV2](https://devnet.logianalytics.com/hc/en-us/articles/5281646521623-REST-SchedulesV2).

| Enum Name | Description |
| --- | --- |
| Once | This schedule only runs once. |
| Daily | This schedule recurs daily. |
| Weekly | This schedule recurs weekly. |
| Monthly | This schedule recurs monthly. |
| Yearly | This schedule recurs yearly. |

## ScheduleManagerViewLevel

| Enum Name | Numeric Value | Description |
| --- | --- | --- |
| User | 1 | Filter schedules by current UserId parameter |
| Company | 2 | Filter schedules by current CompanyId parameter |
| All | 3 | Show all schedules |

## TreeShortcut

Used in the Storage Management System.

| Enum Name | Numeric Value | Description |
| --- | --- | --- |
| Default | 0 | The report will take the default action defined in the system’s configuration. |
| Run | 1 | The report will run in the Report Viewer |
| Export | 2 | The report will be exported |

## wrUserMessageType

Used when [Displaying User Messages](https://devnet.logianalytics.com/hc/en-us/articles/5281582292759-Displaying-User-Messages).

| Enum Name | Numeric Value | Description |
| --- | --- | --- |
| Id | 0 | The user message will display the string associated with the Id in the Language Files. |
| Text | 1 | The user message will display the string message |

## wrUserPreferenceStorage

Used when setting the [User Preference Storage Method](https://devnet.logianalytics.com/hc/en-us/articles/5281636299927-User-Settings#User) setting programatically.

| Enum Name | Numeric Value | Description |
| --- | --- | --- |
| Cookie | 0 | User preferences are stored in the user’s local browser storage. |
| ExternalInterface | 1 | User Preferences are stored and retrieved via an External Interface.  This refers to a deprecated extensibility feature that is no longer supported. It should not be used in new installations. |
| ServerEvent | 2 | User Preferences are stored and retrieved via [Introduction to Server Events](https://devnet.logianalytics.com/hc/en-us/articles/5281583100439-Introduction-to-Server-Events). |
| None | 3 | Users cannot modify User Preference features, and the user interface icon is hidden. |
