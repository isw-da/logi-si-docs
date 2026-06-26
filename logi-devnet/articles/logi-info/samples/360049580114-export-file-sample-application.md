---
title: "Export File Sample Application"
id: 360049580114
section: "Samples"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/360049580114-Export-File-Sample-Application
updated_at: 2024-10-04T13:15:23Z
---

# Export File Sample Application

## **Application Description**

This sample application demonstrates the use of process tasks to export reports to various formats:

* Export report as a CSV file

```
<Procedure Type="If" ID="procIfExportCSV" Expression="&quot;@Request.ReportFormat~&quot; = &quot;CSV&quot;" IdeDisplayStatus="Collapsed">  
 <Procedure Type="ExportToCSV" Filename="@Function.AppPhysicalPath~\ExportedReports\@Session.expFileName~.csv" ID="procExportCSV" IdeDisplayStatus="Collapsed">  
 <Target Type="CSV" Report="Default" ExportDataTableID="dtWorldPopulation" />  
 <IfError IdeDisplayStatus="Collapsed">  
 <Response Type="Report" ID="respReport" IdeDisplayStatus="Collapsed">  
 <Target Type="Report" Report="Default" />  
 <LinkParams StatusMsg="Error: The export failed!" inpFileName="@Session.expFileName~" />  
 </Response>  
 </IfError>  
 </Procedure>  
</Procedure>
```

* Export report data to an Excel file, and format the data for use in Excel

```
<Procedure Type="If" ID="procIfExportExcel" Expression="&quot;@Request.ReportFormat~&quot; = &quot;XLSX&quot;" IdeDisplayStatus="Collapsed">  
 <Procedure Type="ExportToNativeExcel" Filename="@Function.AppPhysicalPath~\ExportedReports\@Session.expFileName~.xlsx" ID="procExportExcel" IdeDisplayStatus="Collapsed">  
 <Remark>  
 <Note Note="Use Excel Output Format attribute to set Excel 97-2003 (.xls) or 2007 (.xlsx) format" />  
 </Remark>  
 <Remark>  
 <Note Note="Specify an Export Data Table ID so only the data itself is exported" />  
 </Remark>  
 <Target Type="NativeExcel" Report="Default" ExcelOutputFormat="Excel2007" ExportDataTableID="dtWorldPopulation" />  
 <IfError IdeDisplayStatus="Collapsed">  
 <Response Type="Report" ID="respReport" IdeDisplayStatus="Collapsed">  
 <Target Type="Report" Report="Default" />  
 <LinkParams StatusMsg="Error: The export failed!" inpFileName="@Session.expFileName~" />  
 </Response>  
 </IfError>  
 </Procedure>  
</Procedure>
```

* Export report as a Word document

```
<Procedure Type="If" ID="procIfExportWord" Expression="&quot;@Request.ReportFormat~&quot; = &quot;DOCX&quot;" IdeDisplayStatus="Collapsed">  
 <Procedure Type="ExportToNativeWord" Filename="@Function.AppPhysicalPath~\ExportedReports\@Session.expFileName~.doc" ID="procExportWord" IdeDisplayStatus="Collapsed">  
 <Target Type="NativeWord" Report="Default" />  
 <IfError IdeDisplayStatus="Collapsed">  
 <Response Type="Report" ID="respReport" IdeDisplayStatus="Collapsed">  
 <Target Type="Report" Report="Default" />  
 <LinkParams StatusMsg="Error: The export failed!" inpFileName="@Session.expFileName~" />  
 </Response>  
 </IfError>  
 </Procedure>  
</Procedure>
```

* Export report as an Adobe PDF file

```
<Procedure Type="If" ID="procIfExportPDF" Expression="&quot;@Request.ReportFormat~&quot; = &quot;PDF&quot;" IdeDisplayStatus="Collapsed">  
 <Procedure Type="ExportToPDF" Filename="@Function.AppPhysicalPath~\ExportedReports\@Session.expFileName~.pdf" ID="procExportPDF" IdeDisplayStatus="Collapsed">  
 <Target Type="PDF" Report="Default" />  
 <IfError IdeDisplayStatus="Collapsed">  
 <Response Type="Report" ID="respReport" IdeDisplayStatus="Collapsed">  
 <Target Type="Report" Report="Default" />  
 <LinkParams StatusMsg="Error: The export failed!" inpFileName="@Session.expFileName~" />  
 </Response>  
 </IfError>  
 </Procedure>  
</Procedure>
```

* Export report data to an XML data file

```
<Procedure Type="If" ID="procIfExportXML" Expression="&quot;@Request.ReportFormat~&quot; = &quot;XML&quot;" IdeDisplayStatus="Collapsed">  
 <Procedure Type="ExportToXml" Filename="@Function.AppPhysicalPath~\ExportedReports\@Session.expFileName~.xml" ID="procExportXML" IdeDisplayStatus="Collapsed">  
 <Target Type="XML" Report="Default" />  
 </Procedure>  
</Procedure>
```

![ExportFileApp.PNG](https://devnet.logianalytics.com/hc/article_attachments/360074563194)

## **Installation Instructions**

1. Download and extract the content of the sample application zip file that is attached to this knowledge base article
2. Create a new Logi Application using the Logi Studio IDE - follow the installation wizard instructions
3. Navigate to the \_Settings file, update the path element to point to the installation directory
4. In your file system, navigate to Logi application installation directory and replace the \_Definitions, \_SupportFiles, and \_Themes directory with the content from the sample application zip file
5. Run the sample application
6. Five buttons appear on the sample application: CSV, Excel, Word, PDF, XML
7. The content of the compress reports or folders can be found in the ExportedReports directory under application root directory

## **Further Readings**

Working with Process Task: [Click Here](https://devnet.logianalytics.com/hc/en-us/articles/4419715442583-Process-Tasks)

Click [here](https://devnet.logianalytics.com/hc/article_attachments/360075773473) to download the items referred to in this article.
