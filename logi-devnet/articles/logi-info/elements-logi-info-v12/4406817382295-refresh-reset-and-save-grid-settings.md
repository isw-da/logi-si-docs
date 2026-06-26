---
title: "Refresh, Reset, and Save Grid Settings"
id: 4406817382295
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817382295-Refresh-Reset-and-Save-Grid-Settings
updated_at: 2022-04-06T06:05:47Z
---

# Refresh, Reset, and Save Grid Settings

# Refresh, Reset, and Save Grid Settings

There are several possible actions that require links outside of the grid which you might want to make available to Dimension Grid users:

| For This Action | Do This |
| --- | --- |
| Refresh | To refresh the data in the grid, without affecting any other settings, call the report definition recursively and include this Link Param: rdDgRefreshData = TrueThe parameter name is case-sensitive. |
| Reset | To clear all user settings and restore the grid to its default state, call the report definition recursively and include this Link Param: rdDgReset = TrueThe parameter name is case-sensitive. |
| Save Settings | To save all user settings for future sessions, use an Action.Process element to call a process task. In the task use a **Procedure.Save Dimension Grid** element to save the settings. The file name itself can incorporate a login name, a GUID, or another method of making it unique to the user, and can be preserved in a number of ways, including as a Cookie on the user's machine. |
| Restore Settings | Once settings have been saved, they can be restored by calling the report and passing the Link Param: rdDgLoadSaved = *<filename>*Once again, the parameter name is case-sensitive. You can use this method to provide a "default" grid configuration for your users: configure the grid, save its settings, distribute the saved settings file with the report, and call the report with the rdDgLoadSaved parameter in the URL. |

The following XML source code example demonstrates the use of these special parameters:

<Division ID="divControlMenu">  
 <LineBreak LineCount="2" />  
 <Label Caption="Reset" ID="lblReset">  
 <Action Type="Report"
ID="actRestart">  
 <Target
Type="Report" ID="tgtRestart" />  
 <LinkParams **rdDgReset**="True" />  
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
 <LinkParams **rdDgRefreshData**="True" />  
 </Action>  
 </Label>  
 <Label Caption=" | " ID="bar"
/>  
 <Label Caption="Save"
ID="lblSave">  
 <Action Type="Process"
Process="MyTasks" ConfirmMessage="Save the Grid?" TaskID="SaveDG"ID="actSave"/>  
 </Label>  
 <Label Caption=" | " ID="bar"
/>  
 <Label Caption="Restore"
ID="lblRestore">  
 <Action Type="Report">  
 <Target Type="Report"
/>  
 <LinkParams
rdDgLoadSaved="@Cookie.DgFilename~" />  
 </Action>  
 </Label>  
 <LineBreak LineCount="2" />  
</Division>

When saving the grid settings in a Process task, using the **Procedure.Save Dimension Grid** element, you need to provide a fully-qualified file path and file name (including an .xml file extension) in the **Filename** attribute. For example:

C:\inetpub\wwwroot\SampleDimensionGrid\SavedGridData\mySettings.xml

The @Function.AppPhysicalPath~ token may be useful here.

However, when restoring saved settings, two separate values are used so that you do not have to expose the file path in your query string:

1. Set the Dimension Grid element's **Saved Dimension Grid Folder** attribute to the fully-qualified file path for the *folder* that contains the stored settings file. For example:  
     
   C:\inetpub\wwwroot\SampleDimensionGrid\SavedGridData  
     
   The @Function.AppPhysicalPath~ token may be useful here.

2. In the Process task that restores the saved settings, call the report definition that contains the Dimension Grid and pass the link parameter **rdDgLoadSaved** mentioned earlier, and set its value to the filename, with .xml extension, only. Do not include any path information here. For example: mySettings.xml

The Dimension Grid will automatically combine the attribute value and the request variable to obtain the fully-qualified path and filename for the saved settings file.
