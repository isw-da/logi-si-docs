---
title: "Folder Management"
id: 5281620756119
section: "Extensibility"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281620756119-Folder-Management
updated_at: 2022-05-03T22:08:18Z
---

# Folder Management

# Folder Management

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Critical")
>
> All legacy content storage mechanisms and the contents of this topic were deprecated in Exago *v2020.1+*. For more information, review [Storage Management: Introduction](https://devnet.logianalytics.com/hc/en-us/articles/5281647019287-Storage-Management-Introduction).

By default, Exago stores the reports in a file system folder. The location of this folder is specified in the ‘Report Path’ property set in the **Admin** **Console**. Alternatively, report, template and folder storage, and retrieval can be handled by building a .NET Assembly. This would allow for reports, folders and templates to be stored in a database. To do this, specify the .NET Assembly in the Report Path of [Main Settings](https://devnet.logianalytics.com/hc/en-us/articles/5281644565527-Main-Settings). The .NET Assembly should contain all of the methods specified in **List of Methods**.

## List of Methods

The following methods will use the **parameters** ‘companyId’, and ‘userId’ which should be set through the API as users enter Exago from the host application.

The folder management code can use alternative method signatures to be passed Exago’s SessionInfo object for additional flexibility. See **Accessing SessionInfo in Folder Management** for more information.

### `string GetReportListXml(string companyId, string userId)`pre-v2017.1

|  |  |
| --- | --- |
| Description | Returns a string listing folders and report names in XML format (see example below). |
| Remarks | For reports set the flag `<leaf_flag>` to *True*. For folders set this flag to *False*.  If an error occurs return null and a generic error will be displayed to the user.  **Note:** As of *v2017.1*, this method is obsolete. Use *GetReportList* instead.  light bulb For the best user experience, keep the number of items in the Report Tree less than 1000. |
| Example | ``` <entity>    <name>Travis' Reports</name>    <leaf_flag>false</leaf_flag>    <readonly_flag>false</readonly_flag>    <entity>       <type>advanced</type>       <name>Sales Report</name>       <description>Contains sales information</description>       <leaf_flag>true</leaf_flag>       <readonly_flag>false</readonly_flag>    </entity>    <entity>       <type>expressview</type>       <name>Employee Reports</name>       <description>Contains employee information</description>       <leaf_flag>false</leaf_flag>       <readonly_flag>false</readonly_flag>       <entity>          <type>Dashboard</type>          <name>Employee Benefits Report</name>          <description>HR and Employee info</description>          <leaf_flag>true</leaf_flag>          <readonly_flag>false</readonly_flag>       </entity>    </entity> </entity> ``` |

### `string GetReportList(string companyId, string userId)`

|  |  |
| --- | --- |
| Description | Returns a string listing folders and report names in XML format (see example below). |
| Remarks | For reports set the flag `<leaf_flag>` to *True*. For folders set this flag to *False*.  If an error occurs return null and a generic error will be displayed to the user.  light bulb For the best user experience, keep the number of items in the Report Tree less than 1000. |
| Example | ``` <entity>    <name>Travis' Reports</name>    <leaf_flag>false</leaf_flag>    <readonly_flag>false</readonly_flag>    <entity>       <type>advanced</type>       <name>Sales Report</name>       <description>Contains sales information</description>       <leaf_flag>true</leaf_flag>       <readonly_flag>false</readonly_flag>    </entity>    <entity>       <type>expressview</type>       <name>Employee Reports</name>       <description>Contains employee information</description>       <leaf_flag>false</leaf_flag>       <readonly_flag>false</readonly_flag>       <entity>          <type>Dashboard</type>          <name>Employee Benefits Report</name>          <description>HR and Employee info</description>          <leaf_flag>true</leaf_flag>          <readonly_flag>false</readonly_flag>       </entity>    </entity> </entity> ``` |

### `string GetReportXml(string companyId, string userId, string reportName)`pre-v2017.1

|  |  |
| --- | --- |
| Description | Returns a string containing the report in XML format. |
| Remarks | If an error occurs return null and a generic error will be displayed to the user.  **Note:** As of *v2017.1* this method is obsolete. Use *GetReport* instead. |

### `string GetReport(string companyId, string userId, string reportName)`

|  |  |
| --- | --- |
| Description | Returns a string containing the report in xml format. |
| Remark | If an error occurs return null and a generic error will be displayed to the user. |

`### wrReportType? GetReportType(string companyId, string userId, string reportName)`

|  |  |
| --- | --- |
| Description | Returns the type of report as a wrReportType enum, or as an int describing the report type:   * 0 = Advanced * 1 = Express * 2 = Dashboard * 3 = Chained * 4 = Visualization * 5 = ExpressView |
| Remark | Returns null if reportName does not exist. Any invalid type returns null. This will cause any report management methods to fail. |

`### string SaveReport(string companyId, string userId, string reportName, string reportXml)`

|  |  |
| --- | --- |
| Description | Saves a report (reportName is fully qualified) |
| Remark | Returns an error message if one occurs, else return null.  To support multi-language functionality, you can supply an Id from a language file instead of a static string. For more information, see [Multi-Language Support](https://devnet.logianalytics.com/hc/en-us/articles/5281604247447-Multi-Language-Support). |

`### string DeleteReport(string companyId, string userId, string reportName)`

|  |  |
| --- | --- |
| Description | Deletes a report (reportName is fully qualified) |
| Remark | Returns an error message if one occurs, else return null.  To support multi-language functionality, you can supply an Id from a language file instead of a static string. For more information, see [Multi-Language Support](https://devnet.logianalytics.com/hc/en-us/articles/5281604247447-Multi-Language-Support). |

`### string RenameReport(string companyId, string userId, string reportName, string newReportName)`

|  |  |
| --- | --- |
| Description | Renames a report (reportName & newReportName are fully qualified). If this method is not provided, DeleteReport and SaveReport will be called. |
| Remark | Returns an error message if one occurs, else return null.  To support multi-language functionality, you can supply an Id from a language file instead of a static string. For more information, see [Multi-Language Support](https://devnet.logianalytics.com/hc/en-us/articles/5281604247447-Multi-Language-Support). |

`### string AddFolder(string companyId, string userId, string folderName)`

|  |  |
| --- | --- |
| Description | Adds a report folder (folderName is fully qualified).  Folder should not be named to one that already exists. |
| Remark | Returns an error message if one occurs, else return null.  To support multi-language functionality, you can supply an Id from a language file instead of a static string. For more information, see [Multi-Language Support](https://devnet.logianalytics.com/hc/en-us/articles/5281604247447-Multi-Language-Support). |

`### string DeleteFolder(string companyId, string userId, string folderName)`

|  |  |
| --- | --- |
| Description | Deletes a report folder (folderName is fully qualified). |
| Remark | Exago’ default report template management will not allow a folder to be deleted that contains any reports.  Returns an error message if one occurs, else return null.  To support multi-language functionality, you can supply an Id from a language file instead of a static string. For more information, see [Multi-Language Support](https://devnet.logianalytics.com/hc/en-us/articles/5281604247447-Multi-Language-Support). |

`### string RenameFolder(string companyId, string userId, string oldName, string newName)`

|  |  |
| --- | --- |
| Description | Renames a report folder (folder names are fully qualified). Folder should not be moved to a location where a Folder with a matching name already exists. |
| Remark | Returns an error message if one occurs, else return null.  To support multi-language functionality, you can supply an Id from a language file instead of a static string. For more information, see [Multi-Language Support](https://devnet.logianalytics.com/hc/en-us/articles/5281604247447-Multi-Language-Support). |

`### string MoveFolder(string companyId, string userId, string oldName, string newName)`

|  |  |
| --- | --- |
| Description | Moves a report folder (folder names are fully qualified).  Folder should not be renamed to one that already exists. |
| Remark | Returns an error message if one occurs, else return null.  To support multi-language functionality, you can supply an Id from a language file instead of a static string. For more information, see [Multi-Language Support](https://devnet.logianalytics.com/hc/en-us/articles/5281604247447-Multi-Language-Support). |

`### bool ExistFolder(string companyId, string userId, string folderName)`

|  |  |
| --- | --- |
| Description | Determines if a folder exists. |
| Remark | Returns true or false. |

`### List<string> GetTemplateList(string companyId,  string userId)`

|  |  |
| --- | --- |
| Description | Returns a list of strings or a string array containing the available templates. |
| Remark | If an error occurs return null and a generic error will be displayed to the user. |

`### byte[] GetTemplate(string companyId, string userId, string templateName)`

|  |  |
| --- | --- |
| Description | Returns a byte array containing the template. |
| Remark | If an error occurs return null and a generic error will be displayed to the user. |

`### string SaveTemplate(string companyId, string userId, string templateName, byte[] templateData)`

|  |  |
| --- | --- |
| Description | Saves a template |
| Remark | Returns an error message if one occurs, else return null.  To support multi-language functionality, you can supply an Id from a language file instead of a static string. For more information, see [Multi-Language Support](https://devnet.logianalytics.com/hc/en-us/articles/5281604247447-Multi-Language-Support). |

`### List<string> GetThemeList(string companyId,  string userId, string themeType)`

|  |  |
| --- | --- |
| Description | Returns a list of strings or a string array containing the available themes. |
| Remark | Valid values of themeType: “CrossTab”, “Express”, “Chart”, “Map”, “Gauge”, “ExpressView”  If an error occurs return null and a generic error will be displayed to the user. |

`### bool ExistTheme(string companyId, string userId, string themeType, string themeName)`

|  |  |
| --- | --- |
| Description | Determines if a theme exists. |
| Remark | Valid values of themeType: “CrossTab”, “Express”, “Chart”, “Map”, “Gauge”, “ExpressView”  Returns true or false. |

### `string GetThemeXml(string companyId, string userId, string themeType, string themeXml)`pre-2017.1

|  |  |
| --- | --- |
| Description | Returns a string representing the theme in xml format.  **Note:**As of *v2017.1*, this method is obsolete. Use *GetTheme* instead. |
| Remark | Valid values of themeType: “CrossTab”, “Express”, “Chart”, “Map”, “Gauge”, “ExpressView”  If an error occurs return null and a generic error will be displayed to the user. |

`### string GetTheme(string companyId, string userId, string themeType, string themeName)`

|  |  |
| --- | --- |
| Description | Returns a string representing the theme. |
| Remark | Valid values of themeType: “CrossTab”, “Express”, “Chart”, “Map”, “Gauge”, “ExpressView”  If an error occurs return null and a generic error will be displayed to the user. |

`### string SaveTheme(string companyId, string userId, string themeType, string themeName, string themeData)`

|  |  |
| --- | --- |
| Description | Saves a theme. |
| Remark | Valid values of themeType: “CrossTab”, “Express”, “Chart”, “Map”, “Gauge”, “ExpressView”  Returns an error message if one occurs, else return null.  **Note:** As of *v2017.1*, we recommend renaming the themeXml parameter to themeData, to reflect the fact that the newer themes are no longer XML.  To support multi-language functionality, you can supply an Id from a language file instead of a static string. For more information, see [Multi-Language Support](https://devnet.logianalytics.com/hc/en-us/articles/5281604247447-Multi-Language-Support). |

## Accessing SessionInfo in Folder Management

This section only applies to Folder Management using a .NET Assembly.

After adding a reference to `WebReportsApi.dll` you may gain additional flexibility by replacing companyId and userId with Exago’ sessionInfo object in the methods listed above. The sessionInfo object grants access to all of the parameters, configuration, and report information of the Exago session. See [SessionInfo](https://devnet.logianalytics.com/hc/en-us/articles/5281621102743-SessionInfo) for more information.

To utilize the sessionInfo Object, **replace** the companyId and userId parameters in the method signatures above with sessionInfo sessionInfo (see example below).

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> To use the sessionInfoObject all of the methods must be static.

Utilizing the sessionInfo object will allow the folder management code to access much more information about the user and/or Exago. For example the capability to access the sessionInfo object could be used to pass additional parameters to the folder management code such as the preferred language of the user or from which part of the host application they entered Exago.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> Passing the sessionInfo object will lock the folder management Assembly. In order to unlock the assembly, either IIS will need to be restarted, or the application pool running Exago will need to be recycled.

The following is an example of the method signature for GetReportXml to utilize the sessionInfo object:

`### string GetReportXml(SessionInfo sessionInfo, string reportName)`

|  |  |
| --- | --- |
| Description | Returns a string containing the report in XML format. |
| Remark | If an error occurs return null and a generic error will be displayed to the user.  companyId and userId can still be retrieved using the calls `sessionInfo.SetupData.Parameters.GetValue(‘companyId’)` and `sessionInfo.SetupData.Parameters.GetValue(‘userId’)` respectively.  The sessionInfo object must be the first parameter in the method. |

## Additional Resources

* Admin Support Lab — [Folder Management](https://devnet.logianalytics.com/hc/en-us/articles/5281547526295-Folder-Management) (video)
