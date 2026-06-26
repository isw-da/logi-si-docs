---
title: "Process Compress File Sample Application"
id: 360049577474
section: "Samples"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/360049577474-Process-Compress-File-Sample-Application
updated_at: 2022-02-07T20:12:36Z
---

# Process Compress File Sample Application

## **Application Description**

This sample application demonstrates the use of process tasks to compress and extract files and folders on the web server. Examples include:

* Run a report, save it as a file, and compress it into a .zip file

```
<Task ID="taskCompressReport" IdeDisplayStatus="Collapsed">  
 <Remark>  
 <Note Note="This procedure runs the report, saves it as a PDF file to the rdDownload folder," />  
 </Remark>  
 <Remark>  
 <Note Note="then compresses into a .zip file in the CompressedFiles folder." />  
 </Remark>  
 <Remark>  
 <Note Note="---" />  
 </Remark>  
 <Remark>  
 <Note Note="Delete any existing .pdf and .zip file from previous run" />  
 </Remark>  
 <Procedure Type="DeleteFile" Filename="@Function.AppPhysicalPath~\CompressedFiles\@Request.ReportName~.zip" ID="procDeleteExistingZip" />  
 <Procedure Type="DeleteFile" Filename="@Function.AppPhysicalPath~\rdDownload\@Request.ReportName~.pdf" ID="procDeleteExistingPDF" />  
 <Procedure Type="ExportToPDF" Filename="@Function.AppPhysicalPath~\rdDownload\@Request.ReportName~.pdf" ID="procExportPDF" IdeDisplayStatus="Collapsed">  
 <Target Type="PDF" Report="@Request.ReportName~" />  
 </Procedure>  
 <Procedure Type="CompressFile" FilesToCompress="@Function.AppPhysicalPath~\rdDownload\@Request.ReportName~.pdf" CompressedFilename="@Function.AppPhysicalPath~\CompressedFiles\@Request.ReportName~.zip" ID="procCompressFile" />  
 <IfError ID="procIfError" IdeDisplayStatus="Collapsed">  
 <Response Type="Report" IdeDisplayStatus="Collapsed">  
 <Target Type="Report" Report="Default" />  
 <LinkParams StatusMsg="Error: @Procedure.procCompressFile.ErrorMessage~" />  
 </Response>  
 </IfError>  
 <Response Type="Report" IdeDisplayStatus="Collapsed">  
 <Target Type="Report" Report="Default" />  
 <LinkParams StatusMsg="Default.lgx was successfully compressed into the CompressedFiles folder" />  
 </Response>  
</Task>
```

* Compress an entire folder with all its files into a .zip file

```
<Task ID="taskCompressFolder">  
 <Remark>  
 <Note Note="This procedure compresses the _Definitions\_Reports folder into a .zip file in the CompressedFiles folder" />  
 </Remark>  
 <Remark>  
 <Note Note="---" />  
 </Remark>  
 <Remark>  
 <Note Note="Delete existing .zip file from previous run" />  
 </Remark>  
 <Procedure Type="DeleteFile" Filename="@Function.AppPhysicalPath~\CompressedFiles\CompressedReports.zip" ID="procDeleteExistingZip" />  
 <Procedure Type="CompressFolder" CompressedFilename="@Function.AppPhysicalPath~\CompressedFiles\CompressedReports.zip" FolderToCompress="@Function.AppPhysicalPath~\_Definitions\_Reports" ID="procCompressReports" />  
 <IfError ID="procIfError">  
 <Response Type="Report">  
 <Target Type="Report" Report="Default" />  
 <LinkParams StatusMsg="Error: @Procedure.procCompressFolder.ErrorMessage~" />  
 </Response>  
 </IfError>  
 <Response Type="Report" IdeDisplayStatus="Collapsed">  
 <Target Type="Report" Report="Default" />  
 <LinkParams StatusMsg="The _Reports folder and its files were compressed into the CompressedFiles folder" />  
 </Response>  
</Task>
```

* Extract a single file from a .zip file

```
<Task ID="taskExtractReport" IdeDisplayStatus="Collapsed">  
 <Remark>  
 <Note Note="This procedure extracts a compressed report file" />  
 </Remark>  
 <Remark>  
 <Note Note="---" />  
 </Remark>  
 <Remark>  
 <Note Note="Procedure.UnCompressFile will NOT overwrite an existing file, so delete if exists" />  
 </Remark>  
 <Procedure Type="DeleteFile" Filename="@Function.AppPhysicalPath~\ExtractedFiles\DataHub_DataSheet.pdf" ID="procDeleteExistingFile" />  
 <Note Note="extract from the .zip file" />  
 <Procedure Type="UnCompressFile" ID="procUnCompressFile" CompressedFilename="@Function.AppPhysicalPath~\CompressedFiles\DataHub_DataSheet.zip" DestinationFolder="@Function.AppPhysicalPath~\ExtractedFiles" />  
 <IfError ID="procIfError" IdeDisplayStatus="Collapsed">  
 <Response Type="Report" IdeDisplayStatus="Collapsed">  
 <Target Type="Report" Report="Default" />  
 <LinkParams StatusMsg="Error: @Procedure.procUnCompressFile.ErrorMessage~" />  
 </Response>  
 </IfError>  
 <Response Type="Report" IdeDisplayStatus="Collapsed">  
 <Target Type="Report" Report="Default" />  
 <LinkParams StatusMsg="File DataHub_DataSheet.zip successfully extracted to ExtractedFiles folder" />  
 </Response>  
</Task>
```

* Extract an entire folder, with multiple files, from a .zip file

```
<Task ID="taskExtractFolder" IdeDisplayStatus="Collapsed">  
 <Remark>  
 <Note Note="This procedure extracts a compressed folder (and all its files) from a .zip file" />  
 </Remark>  
 <Remark>  
 <Note Note="into the ExtractedFiles folder. " />  
 </Remark>  
 <Remark>  
 <Note Note="--" />  
 </Remark>  
 <Remark>  
 <Note Note="Procedure.UnCompressFolder will NOT overwrite an existing folder, so delete if exists" />  
 </Remark>  
 <Procedure Type="DeleteFolder" Folder="@Function.AppPhysicalPath~\ExtractedFiles\_Reports" ID="procDeleteExistingFolder" />  
 <Procedure Type="UnCompressFolder" CompressedFilename="@Function.AppPhysicalPath~\CompressedFiles\CompressedReportSet.zip" DestinationFolder="@Function.AppPhysicalPath~\ExtractedFiles" ID="procUnCompressFolder" />  
 <IfError ID="procIfError" IdeDisplayStatus="Collapsed">  
 <Response Type="Report" IdeDisplayStatus="Collapsed">  
 <Target Type="Report" Report="Default" />  
 <LinkParams StatusMsg="Error: @Procedure.procUnCompressFolder.ErrorMessage~" />  
 </Response>  
 </IfError>  
 <Response Type="Report" IdeDisplayStatus="Collapsed">  
 <Target Type="Report" Report="Default" />  
 <LinkParams StatusMsg="Folder CompressedReportSet.zip successfully extracted to ExtractedFiles folder" />  
 </Response>  
</Task>
```

## **Installation Instructions**

1. Download and extract the content of the sample application zip file that is attached to this knowledge base article
2. Create a new Logi Application using the Logi Studio IDE - follow the installation wizard instructions
3. Navigate to the \_Settings file, update the path element to point to the installation directory
4. In your file system, navigate to Logi application installation directory and replace the \_Definitions, \_SupportFiles, and \_Themes directory with the content from the sample application zip file
5. Run the sample application
6. Four buttons appear on the sample application: Compress Report, Compress Folder, Extract Report, Extract Folder
7. The content of the compress reports or folders can be found in the CompressedFiles directory under application root directory
8. The content of the extracted reports and folders can be found in the ExtractedFiles directory under the application root directory

## **Further Readings**

Working with Process Task: [Click Here](https://devnet.logianalytics.com/hc/en-us/articles/4419715442583-Process-Tasks)
