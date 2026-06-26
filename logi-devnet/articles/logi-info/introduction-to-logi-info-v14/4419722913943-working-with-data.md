---
title: "Working with Data"
id: 4419722913943
section: "Introduction to Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722913943-Working-with-Data
updated_at: 2022-07-17T02:07:46Z
---

# Working with Data

# Working with Data

This topic provides answers to frequently-asked questions about working with data:

1. In Studio, when adding Data Table rows, do I have to add a datalayer
   for each row?
2. [Can I run a Stored Procedure? The DataLayer.SQL element only seems to
   accept SQL statements.](#_Can_I_run_a_Stored_Procedure?_)
3. [My SQL query is returning DateTime values in this format
   "2008-08-07T14:20Z". How can I work with this?](#CXMLDate)
4. [Do Logi products support the MS SQL Server 2005 XML data type? Can
   you search within the XML data?](#XMLDataType)
5. [What formats can you export reports and/or data to?](#Export)
6. [Do Logi products work with BLOBs stored in table columns?](#BLOBs)
7. [Do Logi products support the MEDIAN function?](#Median)
8. [How can I parse the parts of date and time data values?](#TimePeriodCol)
9. [Is there some way to get a list of the report definitions within a
   Logi application, as data?](#DLDefList)
10. [How can I create simple options for use with Input Select Lists? I
    don't want to build a table for only three options.](#DLStatic)
11. [My table contains dates entered as text, but I want to be able to
    sort by date in my Logi report. How can I do this?](#TextDate)

## 1. In Studio, when adding Data Table rows, do I have to add a datalayer for each row ?

No. A datalayer, for example, that issues a SQL query will contain all of
the rows and columns that were returned in the result set. Your report
definition needs to contain Data Table column and label elements for each
column you wish to display. When the report is browsed, the server will
iterate through and display all rows in the datalayer automatically. See
[Data Table Tutorial - Manual](https://devnet.logianalytics.com/hc/en-us/articles/4419707467415-Data-Table-Tutorial-Manual) for an example of how to create a definition that does this.

## 2. Can I run a Stored Procedure?

The DataLayer.SQL element only seems
to accept SQL statements.  
 In general, Stored Procedures should be run using the DataLayer.SP or
Procedure.SP elements. Input and output parameters can then be used with
stored procedures using the SP Parameters element.

## 3. My SQL query is returning DateTime values in this format "2008-08-07T14:20Z". How can I work with this?

DateTime-type data returned into a data layer by a query against a SQL
data source is usually in ISO 8601 format. If you wish to use
script functions to compare, manipulate, or format the date data, you need
to convert it into a compatible format. Logi's intrinsic
**CXMLDate**function has been provided for this purpose. See
[Special Functions and Attributes](https://devnet.logianalytics.com/hc/en-us/articles/4419707826711-Special-Functions-and-Attributes). We also offer the
[Time Period Columns](https://devnet.logianalytics.com/hc/en-us/articles/4419715572119-Time-Period-Columns) element, which makes it easy to parse data, such as hours or months, from
this format.

## 4. Do Logi products support the MS SQL Server 2005 XML data type? Can you search within the XML data?

Yes. Our products support *any* valid SQL statement, so queries that
utilize XQuery functions and XPath expressions, used to search in and work
with XML data in XML data type columns, are supported.

## 5. What formats can you export reports and/or data to?

Logi Info can export to .pdf, .csv, .xml, .xls/xlsx, and .doc/.docx files
and can insert data into predefined PDF, Word, and Excel templates.

## 6. Do Logi products work with BLOBs stored in table columns?

Yes. The File Column element allows BLOBs and CLOBs stored in table
columns to be retrieved and used. For more information, see [The File Column (BLOBs)](https://devnet.logianalytics.com/hc/en-us/articles/4419707590295-The-File-Column-BLOBs-).

## 7. Do Logi products support the MEDIAN function?

Once data has been retrieved from a datasource it can be manipulated using
a the Aggregate Column element, which supports Average, Concat, Count,
Distinct Count, Maximum, Median, Minimum, Mode, Standard Deviation, and
Sum functions.
Aggregations can include or exclude columns with Null values. By
default, they're *excluded*. Create the constant
rdCalculationsIncludeNulls
and set it to *True* if you want to include them.

## 8. How can I parse the parts of date and time data values?

Once data has been retrieved from a datasource it can be parsed using the
**Time Period Column** element. This element will add a column to the
datalayer that can contain parts of a DateTime value, such as:
*Year*, *Quarter*, *Month*, *MonthAbbreviation*,
*MonthName*, *DayOfYear*, *DayOfMonth*, *DayOfWeek*,
*DayOfWeekAbbreviation*, *DayOfWeekName*, *Hour*,
*Minute*, *Second*, and many more. For more information, see [Time Period Columns](https://devnet.logianalytics.com/hc/en-us/articles/4419715572119-Time-Period-Columns).

## 9. Is there some way to get a list of the report definitions within a Logi application, as data?

Yes, the DataLayer.Definition List element will produce, as rows and
columns, information about the properties of each report, process, widget,
and template definition in the application. This data can then be used
like any other data, for example, in reports, menus, and selection lists.
For more information, see [DataLayer.Definition List](https://devnet.logianalytics.com/hc/en-us/articles/4419707484695-DataLayer-Definition-List).

## 10. How can I create simple options for use with Input Select Lists? I don't want to build a table for three options.

There are two easy ways to do this. First, you can use a DataLayer.Static
element beneath your Input Select List, then add one child Static Data Row
element for each list option. Second, a slightly more flexible approach is
to create a simple XML data file that contains your options and then use a
DataLayer.XML File element beneath your Input Select List. This has the
advantage that the options can be easily edited or expanded with having to
run Studio and change the application.

## 11. My table contains dates entered as text, but I want to be able to sort by date.

How can I do this? Retrieve your data into a datalayer element, then add a Calculated Column
element beneath it. In the Calculated Column element's Formula attribute
use the Logi intrinsicCDATE( ) function to add a column to the
datalayer that contains your text dates converted to proper DateTime data.
The calculated column can appear in the Data Table in your report with a
header link for sorting by date.
