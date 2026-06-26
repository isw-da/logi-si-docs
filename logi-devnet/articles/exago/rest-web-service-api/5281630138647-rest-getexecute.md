---
title: "REST \u2014 GetExecute"
id: 5281630138647
section: "REST Web Service API"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281630138647-REST-GetExecute
updated_at: 2022-05-03T22:07:50Z
---

# REST — GetExecute

# REST — GetExecute

Use the **[GetExecute](https://devnet.logianalytics.com/hc/en-us/articles/5281660714135-Executing-Reports-with-the-API#GetExecu)** methods to execute reports in the API without opening an instance of Exago. If executing as text, that is HTML, CSV, or JSON, then the output data is returned directly in the **ExecuteData** property.

If executing as binary (that is PDF, RTF, or Excel workbook), then **ExecuteData** will return different responses depending on if Exago is running in a web-farm environment or not.

| Not In a Web Farm | In a Web Farm |
| --- | --- |
| Either as:  * URL string in the following format:    ```   ExecuteExport.aspx?{parameters}   ```     To download the output data, append the URL to the end of the Exago base URL and launch the full URL string in a browser:     ```   http://{yoursite}/{exago}/{ExecuteExportUrl}   ```     The string is one-use only. To re-download the file, you must create a new Export Url. * A base64 encoded representation of the output file.To display the output data, process the information from the **ExecuteData** property and send it to the browser. | A base64 encoded representation of the output file. To display the output data, process the information from the **ExecuteData** property and send it to the browser. |

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> All requests require a [Session Id](https://devnet.logianalytics.com/hc/en-us/articles/5281669654679-REST-Sessions#Session) URL parameter and basic request headers. In the following topic, headers are omitted in the interest of brevity.

Since GetExecute does not load the full Exago user interface, report interactivity is not supported for these functions. However, the following Server Events are triggered by GetExecute in order to ensure that the data returned accurately reflects the report design:

* [Global Event: OnReportExecuteInit](https://devnet.logianalytics.com/hc/en-us/articles/5281591136663-Global-Event-OnReportExecuteInit)
* [Global Event: OnReportExecuteStart](https://devnet.logianalytics.com/hc/en-us/articles/5281599371543-Global-Event-OnReportExecuteStart)
* [Global Event: OnReportExecuteEnd](https://devnet.logianalytics.com/hc/en-us/articles/5281622175511-Global-Event-OnReportExecuteEnd)
* [Global Event: OnAfterReportExportSuccess](https://devnet.logianalytics.com/hc/en-us/articles/5281621560215-Global-Event-OnAfterReportExportSuccess)

## Report JSON

The path to the report is passed as part of a JSON object, with optional sorts and filters. Any sorts and filters are added only for this execution, and do not persist throughout the session.

Table B — Report JSON Properties

| **Name** | **Type** | **Writable** | **Description** |
| --- | --- | --- | --- |
| Id | string | required\* | Can be used to retrieve a report from the Storage Management database in lieu of the ReportPath property below in *v2021.1+* |
| ReportPath | string | required\* | Full path from the root folder to the report |
| DataType | [ExecuteDataType v2021.1+](https://devnet.logianalytics.com/hc/en-us/articles/5281610137879-Constants-and-Enumerators#ExecuteD) | yes | Choose how Exago shall return the data to the client, either as raw data or as a URL. |
| Sorts | array of **[Sort JSON](#Sort)** | yes | Any sorts to apply to the report during execution |
| Filters | array of **[Filter JSON](#Filter)** | yes | Any filters to apply to the report during execution |

\* either the **Id** or **ReportPath** must be **specified** but not both

## Execute a Report

**Type** indicates which format you want to receive the output data: html, csv, pdf, pdfsnapshot, rtf, excel, json.

```
POST /Reports/Execute/{Type}
```

### Using curl

```
curl http://{webservice}/rest/Reports/Execute/csv?sid={sid} -X POST ^
	-d "{'ReportPath':'Inventory\\Products'}"
```

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Windows file paths are delimited with double-backslashes: `\\`. With **Storage Management** in *v2020.1+*, the double slash is no longer necessary.

### Output JSON

GetExecute returns the following JSON object:

Table C — Output JSON

| Name | Type | Description |
| --- | --- | --- |
| ReportPath | string | Full path from the root folder to this report |
| ExportType | string | Format of export data |
| DataType | [ExecuteDataType v2021.1+](https://devnet.logianalytics.com/hc/en-us/articles/5281610137879-Constants-and-Enumerators#ExecuteD) | How Exago has returned the data to the client, either as binary encoded string or as a URL. |
| ExecuteData | string | The output of the GetExecute() method, either as a URL or binary encoded string based on the **DataType** property. |
| IsError | Boolean | Whether there were any errors when executing the report |
| ErrorList | array of string | If IsError = true, a list of errors encountered when executing this report |

### Examples

Output a CSV file:

```
POST /rest/Reports/Execute/csv
```

```
Status: 200 OK

{
  "ReportPath":  "Inventory\\Categories",
  "ExportType":  "csv",
  "DataType":    "Data",
  "ExecuteData": ""Categories"\r\n"Beverages"\r\n"Condiments"\r\n"Confections"\r\n"Dairy Products"\r\n"Grains/Cereals"\r\n"Meat/Poultry"\r\n"Produce"\r\n"Seafood"\r\n",
  "IsError":     false,
  "ErrorList":   null
}
```

Output a PDF file:

```
POST /rest/Reports/Execute/pdf
```

```
Status: 200 OK
{
	"ReportPath": "Products",
	"ExportType": "Pdf",
	"DataType": "Data",
	"ExecuteData": "JVBERi0xLjQKJeLjz9MKMyAwIG9iaiA8PC9MZW5ndGggNDE5NC9GaWx0ZXIvRmxhdGVEZWNvZGU+PnN0cmVhbQp4nO2dW3PbNhaA3/0r+NCZdmfWXBAEL3h00jbbrdu0SbDAxODgyNCAwMDAwMCBuIAowMDAwMDE5MjU2IDAwMDAwIG4gCjAwMDAwMTkzMDEgMDAwMDAgbiAKdHJhaWxlcgo8PC9TaXplIDE2L0luZm8gMTUgMCBSL0lEIFs8ZDEyNmY0ZDQ2ZDI4OGUwNTA1YWM2MGZlYTMwOTBmYTM+PDYwNTE5NjU1NGM1OWVlODI2YmNkNzdiNDFjZmM4YWI5Pl0vUm9vdCAxNCAwIFI+PgpzdGFydHhyZWYKMTk0NDYKJSVFT0YK",
	"IsError": false,
	"ErrorList": null
}
```

## Sort JSON

Each run-time sort is supplied using the following JSON object:

Table D — Sort JSON Properties

| Name | Type | Writable | Description |
| --- | --- | --- | --- |
| EntityName | string | required | Data object to sort on |
| ColumnName | string | required | Column to sort on |
| AscendingFlag | Boolean | yes (false) | Whether to sort in ascending (versus descending) order |

## Filter JSON

Each run-time filter is supplied using the following JSON object:

Table E — Filter JSON Properties

| Name | Type | Writable | Description |
| --- | --- | --- | --- |
| FilterText | string | required | The value of the filter, either a Category name or a formula. For example:  * Employees.EmployeeName * =Month(Employees.BirthDate) |
| DataType | enum | yes (“string”) | [DataType](https://devnet.logianalytics.com/hc/en-us/articles/5281610137879-Constants-and-Enumerators#DataType2) |
| Operator | enum as integer | yes (0) | [Filter Operator Type](https://devnet.logianalytics.com/hc/en-us/articles/5281610137879-Constants-and-Enumerators#Filter) (only accepts integer value) |
| Values | array of string | yes | Values to filter with |
| *EntityName* | string | deprecated (as of *v2018.1*) | Data object to filter on |
| *ColumnName* | string | deprecated (as of *v2018.1*) | Column to filter on |

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> DateTime strings passed as filter values must be able to be parsed by the .NET method **[DateTime.Parse](https://msdn.microsoft.com/en-us/library/system.datetime.parse(v=vs.110).aspx)** using the current thread culture.

## Execute with Sorts and Filters

**Type** indicates which format you want to receive the output data: html, csv, pdf, pdfsnapshot, rtf, excel, json.

```
POST /rest/Reports/Execute/{Type}
```

### Using curl

```
curl http://{webservice}/rest/Reports/Execute/csv?sid={sid} -X POST ^
	-d @reportExecuteResource.txt
```

#### reportExecuteResource.txt

```
"{
  'ReportPath': 'Inventory\\Categories',
  'Sorts': [
    {
      'EntityName': 'Categories',
      'ColumnName': 'CategoryName',
      'AscendingFlag': false
    }
  ],
  'Filters': [
    {
      'FilterText': 'Category.CategoryName'
      'DataType': 'string',
      'Operator': 14,
      'Values': [
        'Beverages',
        'Produce',
        'Seafood'
      ],
    }
  ]
}"
```

### Example response

```
Status: 200 OK

{
  "ReportPath":  "Inventory\\Categories",
  "ExportType":  "csv",
  "DataType":    "Data",
  "ExecuteData": ""Categories"\r\n"Seafood"\r\n"Produce"\r\n"Beverages"\r\n",
  "IsError":     false,
  "ErrorList":   null
}
```
