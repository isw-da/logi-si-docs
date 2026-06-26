---
title: "Create a Download Link from Popup Menu"
id: 360051475493
section: "Samples"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/360051475493-Create-a-Download-Link-from-Popup-Menu
updated_at: 2022-04-24T15:18:38Z
---

# Create a Download Link from Popup Menu

### Question:

How do I create a link or force the user to download a file instead of viewing it in the browser?

### Answer:

Most major browsers default to opening PDF files in a new tab or window of the browser. This includes opening files directly from the system if no program has been installed to open and view PDF files.

To circumvent this default behavior we can use a process task to create a physical file within a location on the server. Then use the 'download' attribute of the HTML <a> tag to create a clickable and downloadable link. Further information on this attribute can be found here: <https://www.w3schools.com/TAGS/att_a_download.asp>

To set this up within Logi Info Studio you'll need to add an Action Process element below a Popup Option element.

![mceclip0.png](https://devnet.logianalytics.com/hc/article_attachments/360079259273/mceclip0.png)

This then points to a Task element that will download the PDF to a location in the application directory. This process task will then need to pass a Link Parameter element value to the conditional Division element that will be shown when the report definition is loaded and thus displaying the HTML link for download.

Report Definition Source:

```
 <DefaultRequestParams ReportPrintName="MyFile@Function.GUID~" />  
 <Body>  
 <Button Caption="Export" ID="btn">  
 <Action ID="aP" Type="Popup">  
 <PopupOption ID="AnalysisGridViewMenuPDF" IdeDisplayStatus="Collapsed">  
 <Label Caption="PDF - View" />  
 <Action ID="PDF_Export" Type="PDF">  
 <Target ExportFilename="@Request.ReportPrintName~.pdf" Type="PDF" />  
 </Action>  
 </PopupOption>  
 <PopupOption ID="AnalysisGridDownloadMenuPDF">  
 <Label Caption="PDF - Download" />  
 <Action ID="apPDFdownload" Process="PDFdownload" TaskID="taskPDFdownload" Type="Process">  
 <LinkParams ReportPrintName="@Request.ReportPrintName~" />  
 </Action>  
 </PopupOption>  
 </Action>  
 </Button>  
 <Division ID="divAutoDownload" Condition="&quot;@Request.ShowDownloadLink~&quot;=&quot;True&quot;">  
 <Label Caption="&lt;a id=&quot;PDFdownloadlink&quot; href=&quot;{your app URL}/rdDownload/@Request.ReportPrintName~.pdf&quot; download=&quot;@Request.ReportPrintName~.pdf&quot;&gt;Click to Download @Request.ReportPrintName~&lt;/a&gt;" Format="HTML" />  
 </Division>  
 </Body>
```

 Process Definition Source:

```
<Task ID="taskPDFdownload">  
 <Procedure Type="ExportToPDF" Filename="@Function.AppPhysicalPath~/rdDownload/@Request.ReportPrintName~.pdf" ID="procE2PDF">  
 <Target Type="PDF" Report="myexport" />  
 </Procedure>  
 <Response Type="Report">  
 <Target Type="Report" Report="myexport" />  
 <LinkParams ShowDownloadLink="True" />  
 </Response>  
</Task>
```
