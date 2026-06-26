---
title: "Refresh, Reset, and Save Grid Settings"
id: 4419723014807
section: "Use Logi Studio/SSRM - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723014807-Refresh-Reset-and-Save-Grid-Settings
updated_at: 2022-07-17T01:44:48Z
---

# Refresh, Reset, and Save Grid Settings

# Refresh, Reset, and Save Grid Settings

There are several possible actions that require links outside of the grid which you might want to make available to Chart Grid users:

| For This Action | Do This |
| --- | --- |
| Refresh | To refresh the data in the grid, without affecting any other settings, call the report definition again and include this Link Param: rdCgRefreshData = TrueThe parameter name is case-sensitive. |
| Reset | To clear all user settings and restore the grid to its default state, call the report definition again and include this Link Param: rdCgReset = TrueThe parameter name is case-sensitive. |
| Save Settings | To save all user settings for future sessions, use an Action.Process element to call a process task. In the task use a **Procedure.Save Chart Grid** element to save the settings. The file name itself can incorporate a login name, a GUID, or another method of making it unique to the user and must end in ".xml". The file name can be preserved in a number of ways, including as a Cookie on the user's machine. |
| Restore Settings | Access the preserved file name then call the report definition again and pass the Link Param: rdCgLoadSaved = *<filename>* Once again, the parameter name is case-sensitive. |

The following XML source code example demonstrates the use of these special parameters:

<Division ID="divControlMenu">  
 <LineBreak LineCount="2" />  
 <Label Caption="Reset" ID="lblReset">  
 <Action Type="Report"
ID="actRestart">  
 <Target
Type="Report" ID="tgtRestart" />  
 <LinkParams **rdCgReset**="True" />  
 </Action>  
 </Label>  
 <Label Caption=" | " ID="bar"
/>  
 <Label Caption="Refresh Data"
ID="lblRefreshData">  
 <Action Type="Report"
ID="actRefreshData">  
 <Target
Type="Report" ID="tgtRefresData" />  
 <LinkParams **rdCgRefreshData**="True" />  
 </Action>  
 </Label>  
 <Label Caption=" | " ID="bar"
/>  
 <Label Caption="Save"
ID="lblSave">  
 <Action Type="Process"
Process="MyTasks" ConfirmMessage="Save Grid?" TaskID="SaveCG" ID="actSave"/>  
 </Label>  
 <Label Caption=" | " ID="bar"
/>  
 <Label Caption="Restore"
ID="lblRestore">  
 <Action Type="Report">  
 <Target Type="Report"
/>  
 <LinkParams
rdCgLoadSaved="@Cookie.CgFilename~" />  
 </Action>  
 </Label>  
 <LineBreak LineCount="2" />  
</Division>

When saving the grid settings in a Process task, using the **Procedure.Save Chart Grid** element, you need to provide a fully-qualified file path and file name (including an .xml file extension) in the **Filename** attribute. For example:

C:\inetpub\wwwroot\SampleChartGrid\SavedGridData\mySettings.xml

The @Function.AppPhysicalPath~, @Session, and @Constant tokens may be useful here.
However, when restoring saved settings, two separate values are used so that you do not have to expose the file path in your query string:

1. Set the Chart Grid element's **Saved Chart Grid Folder** attribute to the fully-qualified file path for the *folder* that contains the stored settings file. For example: C:\inetpub\wwwroot\SampleChartGrid\SavedGridData. The @Function.AppPhysicalPath~ and @Constant tokens may be useful here.

2. In the Process task that restores the saved settings, call the report definition that contains the Chart Grid and pass the link parameter **rdCgLoadSaved** mentioned earlier, and set its value to the filename, with .xml extension, only. Do not include any path information here. For example: mySettings.xml

The Chart Grid will automatically combine the attribute value and the request variable to obtain the fully-qualified path and filename for the saved settings file.
