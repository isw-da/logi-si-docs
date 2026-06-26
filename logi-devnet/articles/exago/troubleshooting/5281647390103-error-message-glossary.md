---
title: "Error Message Glossary"
id: 5281647390103
section: "Troubleshooting"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281647390103-Error-Message-Glossary
updated_at: 2024-08-21T20:32:55Z
---

# Error Message Glossary

# Error Message Glossary

This topic serves as a glossary of error messages that may be displayed during the configuration or use of Exago BI. A list of potential causes and remedies is also included. If you need more information, contact [Exago Support](https://help.insightsoftware.com/s/contactsupport?language=en_US "Exago support").

## Web Application User Interface

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/25323197519767 "Note")
>
> This topic references `<WebApp>/`, `<WebSvc>/` and `<Sched>/`as a placeholder for the Web Application, Web Service API and Scheduler Service's install location respectively. The default install location is `C:\Program Files\Exago\ExagoWeb\` (`/opt/Exago/` on Linux), `C:\Program Files\Exago\ExagoWebApi\` ( `/opt/Exago/WebServiceApi/` on Linux) or `C:\Program Files\Exago\ExagoScheduler\` (`/opt/Exago/Scheduler/` on Linux); however, these directories can be changed during installation.

These error messages may appear in several locations throughout the Web Application user interface.

---

|  |  |
| --- | --- |
| Error Message | No Data Qualified |
| Possible Causes | Based on the fields, formulas and filters set on this report, no records meet their criteria so there is no data to be included in the report. |
| Potential Remedies | Adjust the fields, formulas and filters on the report so that at least one record is returned from the data source. For more information review these resources:   * [No Data Qualified Options](https://devnet.logianalytics.com/hc/en-us/articles/5281564494999-No-Data-Qualified-Options) * [User Support Lab — No Data Qualified](https://devnet.logianalytics.com/hc/en-us/articles/5281654423959-User-Support-Lab-No-Data-Qualified) (video) |

---

|  |  |
| --- | --- |
| Error Message | Session has timed out; browser page will need to be reloaded or browser restarted |
| Possible Causes | 1. The configuration file, or the static configuration file in a static-dynamic pair was changed 2. Exago is dropping sessions 3. The web server is restarting unexpectedly. 4. Exago is accessed from a different origin as the host application over HTTP |
| Potential Remedies | 1. Changes made to the configuration file in a single configuration file environment, or the static configuration file of static-dynamic file pair will always invalidate all user sessions. Avoid modifying these files when users are engaged with the system. For more information, review [Configuration File Options and Optimizations](https://devnet.logianalytics.com/hc/en-us/articles/5281626054679-Configuration-File-Options-and-Optimizations) and [Modifying Configs in a Production Environment](https://devnet.logianalytics.com/hc/en-us/articles/5281619727383-Modifying-Configs-in-a-Production-Environment). 2. Exago recommends utilizing a State Server. Review [Setting up a State Server](https://devnet.logianalytics.com/hc/en-us/articles/5281581463959-Setting-up-a-State-Server). If a state server is already in use, make sure it is configured properly and running. 3. Check for and troubleshoot disruptions to the web server’s up-time. 4. Review [Cross-Origin Embedding of Exago BI](https://devnet.logianalytics.com/hc/en-us/articles/5281619580311-Cross-Origin-Embedding-of-Exago-BI) for full details about the proper way of deploying Exago cross-origin. |

---

|  |  |
| --- | --- |
| Error Message | An error has occurred. Please contact your administrator.  HTTP Status code: 200 |
| Possible Causes | This generic error message may occur in a variety of circumstances. Use the instructions in **Potential Remedies** below to gather more information, then search this glossary again. |
| Potential Remedies | Append `?ShowErrorDetail=true` to the end of the URL, and try to replicate the behavior which caused the error. (Refer to [See Full Error Details](https://devnet.logianalytics.com/hc/en-us/articles/5281647422487-See-Full-Error-Details) This will allow you to identify the error in more detail and search for a solution.   ``` http://localhost/exago/exagohome.aspx?showerrordetail=true ```   The error message will be displayed as a full stack trace. Use this information to correct issues such as data source connectivity trouble, incorrect web server configuration or to send the information to the Exago Support Group for additional support.  Additional information can be found in the system log. Review the [Accessing the Log File](https://devnet.logianalytics.com/hc/en-us/articles/5281647183383-Accessing-the-Log-File) to locate the log files. |

---

|  |  |
| --- | --- |
| Error Message | There are errors with this report, which prevents it from being executed or scheduled. Please edit report to view and fix errors. |
| Possible Causes | Trying to run a report that has errors on it. This may be due to data objects that are no longer available, incorrect formulas, reports on a Dashboard or Chained Report that are no longer available, or other reasons. |
| Potential Remedies | Instead of running the report, open it in the Report Designer. A **Report Errors** dialog will display listing the errors present on the report with potential resolutions to those errors. Follow the instructions in the Report Errors dialog and then try to execute the report again. |

---

|  |  |
| --- | --- |
| Error Message | HTTP 200 An error has occurred that is preventing completion of this request. Please contact your administrator. |
| Possible Causes | See [An error has occurred. Please contact your administrator](#An) above. |
| Potential Remedies | See [An error has occurred. Please contact your administrator](#An) above. |

---

|  |  |
| --- | --- |
| Error Message | Error saving report |
| Possible Causes | 1. The Scheduler Service is not running, or the Web Application server cannot reach the Scheduler Service. 2. For *pre-v2020.1*, the permissions on the **Admin Console** > **General** > **Main Settings** > **Report Path** do not allow Exago to write to that location. |
| Potential Remedies | 1. Start the Scheduler Service, or check the **Admin Console** > **General** > **Scheduler Settings** and the Scheduler Service Configuration file to insure they are correct and the service is reachable. 2. For *pre-v2020.1*, grant full permissions to the Report Path for the IIS user or to the associated system user (for example apache or exago) |

---

|  |  |
| --- | --- |
| Error Message | Access Denied |
| Possible Causes | 1. The report being executed requires access to a Data Object that is not accessible in the current Role. |
| Potential Remedies | 1. Check the settings for the current Role and insure that all of the Data Objects that are needed are available. For more information, review [Roles](https://devnet.logianalytics.com/hc/en-us/articles/5281625714967-Roles). |

---

|  |  |
| --- | --- |
| Error Message | Error: Access to the path ‘C:\Program Files\Exago\Config\WebReports.xml’ is denied. |
| Possible Causes | Permissions are not set on the config folder. |
| Potential Remedies | Set the IIS user permissions to Full Control on the config folder, or follow the instructions in the Folder Configuration section of the Installing Exago on Linux topic to properly configure permissions. |

---

|  |  |
| --- | --- |
| Error Message | *Abended* appears in the MainLeftPaneScheduleManager.png**Schedule Manager** |
| Possible Causes | See [Report has abended](#Report) below. |
| Potential Remedies | See [Report has abended](#Report) below. |

---

|  |  |
| --- | --- |
| Error Message | Exception occurred configuring log4net: Access to the path ‘C:\Program Files\Exago\WebTemp’ is denied. |
| Possible Causes | Permissions are not set on the temp folder. |
| Potential Remedies | Set the IIS user permissions to Full Control on the temp folder. |

---

|  |  |
| --- | --- |
| Error Message | Folder or Virtual Directory not found: path=[path], mappedPath=[path] |
| Possible Causes | Report folder path is wrong or permissions are not set on the report folder. |
| Potential Remedies | 1. Verify the report path is set correctly in the Admin Console. 2. Set the IIS user permissions to Full Control on the report folder. |

---

|  |  |
| --- | --- |
| Error Message | light bulb The placeholders <report path> and <content ID> are used below to reference the folder and report name, and the content ID (as a GUID) in the system.  Report ‘<report path>:<content ID>’ not found.  **Example**   ``` Report 'My ReportsSalesProducts2020 Profit:70aa978f-7f00-42ab-a2ec-c4548ee4ab53' not found. ``` |
| Possible Causes | The report specified in the error message text was set as a Startup Report, but that report has been deleted from the system. |
| Potential Remedies | Remove the report specified in the error message from the Startup Reports tab of the UserPreferences.png**User Preferences**. For more information, review the Startup Reports section of [User Preferences and Context Sensitive Help](https://devnet.logianalytics.com/hc/en-us/articles/5281553297559-User-Preferences-and-Context-Sensitive-Help). |

---

|  |  |
| --- | --- |
| Error Message | Report has abended |
| Possible Causes | 1. The execution cache for this report is invalid or out of date. 2. A fatal error has occurred on a report being executed by the Scheduler Service, and report execution has stopped. |
| Potential Remedies | 1. Click the Execution Cache icon in the toolbar to refresh the report’s execution cache 2. Investigate the Scheduler Service’s log file to determine root cause. |

---

|  |  |
| --- | --- |
| Error Message | ERR\_CONNECTION\_REFUSED Unable to connect |
| Possible Causes | 1. The Exago server or website is not running 2. The port is not open to the Exago server |
| Potential Remedies | 1. Restart the web server and website. 2. Open the necessary port in the firewall. |

---

|  |  |
| --- | --- |
| Error Message | Error: No connection could be made because the target machine actively refused it |
| Possible Causes | The Scheduler Service is not running, or the Web Application server cannot reach the Scheduler Service. |
| Potential Remedies | Start the Scheduler Service, or check the **Admin Console** > **General** > **Scheduler Settings** and the Scheduler Service Configuration file to insure they are correct and the service is reachable. |

---

|  |  |
| --- | --- |
| Error Message | Error: Please select a cell value. |
| Possible Causes | 1. A **Top N Filter** was added to the report, but a **Value** field was not chosen. |
| Potential Remedies | 1. Return to the **Top/Bottom** tab of the Report Filters dialog, and either remove the **Top N Filter** by unchecking the **Limit the report to the top/bottom values** checkbox or choose a **Value** field from the dropdown. |

---

|  |  |
| --- | --- |
| Error Message | Error loading language file; unable to continue properly The following language file is invalid: [path]. Please check the current value in General->Main Settings. |
| Possible Causes | 1. A language file that is specified in the configuration does not exist, or cannot otherwise be found. |
| Potential Remedies | 1. Verify that every language file in **Admin Console** > **General** > **Main Settings** > **Language File** exists in the `<WebApp>/Config/Languages`directory. |

---

|  |  |
| --- | --- |
| Error Message | HTTP 400 Bad Request |
| Possible Causes | 1. The Web Application and the REST Web Service API are unable to communicate because their is no common encryption protocol between them. |
| Potential Remedies | 1. Add the `SecurityProtocol` node to both the Web Application’s and the REST Web Service API’s **appsettings.config** files. There must be at least one common encryption protocol between the two. For more information, review the [Application Settings](https://devnet.logianalytics.com/hc/en-us/articles/5281615366423-Application-Settings). |

---

|  |  |
| --- | --- |
| Error Message | Object reference not set to an instance of an object. |
| Possible Causes | This is a generic error message that may occur in a variety of situations in the application. If this error message appears right after installing Exago, it is typically caused by the configuration file (WebReports.xml) missing or corrupt or inadequate permissions to reach the configuration file. |
| Potential Remedies | Set the IIS user permissions to Full Control on the config folder, or follow the instructions in the Folder Configuration section of the Installing Exago on Linux topic to properly configure permissions. |

---

|  |  |
| --- | --- |
| Error Message | HTTP 403.14 Forbidden The Web Server is configured to not list the contents of this directory. |
| Possible Causes | No file name is included in the URL to reach the home page or the Admin Console. |
| Potential Remedies | 1. Add the file name to the URL.     ```    http://<YourServer>/Exago/admin.aspx    ``` 2. Add `exagohome.aspx` as the default document in the web server’s configuration. |

---

|  |  |
| --- | --- |
| Error Message | HTTP 404 Not Found   HTTP 404 An error has occurred that is preventing completion of this request. Please contact your administrator. |
| Possible Causes | 1. Using the incorrect URL to the Exago resource 2. In the REST Web Service API, the wrong method was being used (for example GET when a POST was expected) 3. In an environment using cookieless sessions, the session has expired. |
| Potential Remedies | 1. Check that the request URL path is correct. On Linux, paths are case-sensitive. 2. Refer to the List of REST Endpoints to make sure the endpoint supports the method in use. Change to a supported method if necessary. 3. Renew the session. Consider using another cross-origin embedding strategy. Review [Cross-Origin Embedding of Exago BI](https://devnet.logianalytics.com/hc/en-us/articles/5281619580311-Cross-Origin-Embedding-of-Exago-BI). |

---

|  |  |
| --- | --- |
| Error Message | HTTP 500.19 Internal Server Error |
| Possible Causes | The configuration section `standardEndpoints` cannot be read because it is missing a section declaration. Incorrect or missing Application Pool. |
| Potential Remedies | Select the correct Application Pool |

---

|  |  |
| --- | --- |
| Error Message | System.UriFormatException |
| Possible Causes | 1. An incorrect version of the mono runtime is installed. 2. Unpatched `System.Web.dll` when using cookieless sessions |
| Potential Remedies | 1. Insure one of the supported Mono versions is installed. 2. Replace `System.Web.dll` with our  [patched version](https://devnet.logianalytics.com/hc/article_attachments/5432173608983) |

---

|  |  |
| --- | --- |
| Error Message | Uncaught (in promise) Attempting to get language for ID that doesn’t exist, “FormulaEditor\_\_Node” |
| Possible Causes | One or more [Custom Function](https://devnet.logianalytics.com/hc/en-us/articles/5281628193815-Custom-Functions) or [Custom Aggregate Functions](https://devnet.logianalytics.com/hc/en-us/articles/5281616754327-Custom-Aggregate-Functions) exist in a custom named function category, but no language file node exists for that category name. |
| Potential Remedies | Follow the instructions in the Custom Functions or Custom Aggregate Functions topics (links above) and the [Multi-Language Support](https://devnet.logianalytics.com/hc/en-us/articles/5281604247447-Multi-Language-Support) topic to add a language file node. |

|  |  |
| --- | --- |
| Error Message | Error: Groups must go from inner to outer |
| Possible Causes | 1. A **Top N Filter** with a **For Each** group was added to the report, but a **Group** field was not chosen. |
| Potential Remedies | 1. Return to the **Top/Bottom** tab of the Report Filters dialog, and either remove the **Top N Filter** by unchecking the **Limit the report to the top/bottom values** checkbox or choose a **Group** field from the dropdown. |

|  |  |
| --- | --- |
| Error Message | Conditional Format Error: Conditional format return value should evaluate to true or false |
| Possible Causes | **Conditional Formatting** has been applied to a cell on a report, but the conditional formula that is comparing the cell value to the formatting criteria did not return a *true* or *false* value, so the conditional formatting has failed. |
| Potential Remedies | 1. The data type that was returned from the data source for this cell does not match the data types required in the conditional formula. Either apply a filter to eliminate invalid records from the report, or modify the formula accordingly. |

## Admin Console

|  |  |
| --- | --- |
| Error Message | Error: An attempt was made to load a program with an incorrect format. |
| Possible Causes | 1. The SQLite driver being accessed is the wrong version. |
| Potential Remedies | 1. Delete the `SqliteInterop.dll` file from the `/bin` directory. 2. Replace the `SqliteInterop.dll` in the `/bin/x86/` and `/bin/x64/` directories. Exago can supply these if necessary. |

---

|  |  |
| --- | --- |
| Error Message | light bulb The placeholders <data object name> and <database name> are used below to reference the name of a data object and data source name in the environment that will be referenced by name in the error message.  Connection failed for <data object name>: Either the user, ‘IIS APPPOOLDefaultAppPool’, does not have access to the ‘<database name>’ database, or the database does not exist. |
| Possible Causes | 1. The application pool is attempting to access a data source using **Integrated Authentication** but the data source is not setup for that.  light bulb A variant of this error message may also appear in the Web Application’s log file. |
| Potential Remedies | 1. Review the notes about Integrated Authentication in the **Connection String** section of the [Data Sources topic](https://devnet.logianalytics.com/hc/en-us/articles/5281617045911-Data-Sources) to configure the environment properly. |

---

|  |  |
| --- | --- |
| Error Message | Connection to database failed: Storage Management Failed to Initialize. Could not find either the single or double constructor. light bulb This error message may also appear in the Web Application main user interface as well. |
| Possible Causes | Exago was able to locate the Storage Management library but was not able to find one of the two possible expected constructors. |
| Potential Remedies | 1. Verify that the **Admin Console** > **Storage Management** > **Assembly Location** and **Class Name** are correct. Click the **Validate Assembly**CheckmarkAdmin.png icon to make sure a connection can be made to the Storage Management assembly.  light bulb It is recommended to always use an absolute file path to the Storage Management assembly. 2. The Storage Management assembly in the **Assembly Location** noted above is out of date. Check the Web Application’s log file to find the absolute file path that Exago is using to load the library, and update it as needed. |

---

|  |  |
| --- | --- |
| Error Message | light bulb The placeholder <GUID> is used below to reference a Globally Unique Identifier that is appended to the end of the file name. This will vary with each instance of the error message.  Error: Could not find file ‘/opt/Exago/Config/WebReports.xml.<GUID>’  Error: Could not find file ‘C:Program FilesExagoExagoWebConfigWebReports.xml.<GUID>’ |
| Possible Causes | This error message typically appears when temporary files are not accessible  1. The permissions on the `/Config` directory and temp path do not allow the web server to read from one or both. 2. Exago is installed in a web farm and temporary files created by one node in the farm are unreachable by another node in the farm. 3. A cloud temporary path is configured, but the cloud service is not supported or accessible by Exago. |
| Potential Remedies | 1. Configure the permissions appropriately, as described in the corresponding installation topic (Windows, Linux or Azure) 2. Set the `<webfarmsupport>` node in the configuration XML file to true. See [Hidden Flags](https://devnet.logianalytics.com/hc/en-us/articles/5281607060631-Hidden-Flags) and [Set Up Exago in a Web Farm](https://devnet.logianalytics.com/hc/en-us/articles/5281607747991-Set-Up-Exago-in-a-Web-Farm). 3. Make sure the **Admin Console** > **General** > **Main Settings** > **Temp Cloud Service** is a valid connection string to a supported cloud storage method such as Azure blob storage or Amazon S3 or EC2. |

---

|  |  |
| --- | --- |
| Error Message | light bulb The placeholder <database> is used below to reference the name of a CData driver in the environment that will be referenced by name in the error message.  DbConnect Exception Could not find a valid license for using CData ADO.NET Provider for <database> on this system |
| Possible Causes | Licenses are generated by Exago for a specific version of the CData driver. If the driver version has changed, this error message might appear. |
| Potential Remedies | Check the [Updating to the Latest Version (Potentially Breaking Changes)](https://devnet.logianalytics.com/hc/en-us/articles/5281637050775-Updating-to-the-Latest-Version-Potentially-Breaking-Changes-) topic to see if the applicable driver has been updated. If you need more product information, including new purchases and upgrades, contact your Exago Customer Success Manager. |
|  | red exclamation point **Important:**  As of v2024.2.1, CData drivers are no longer available for use in Exago BI products. See **[CData Drivers](https://devnet.logianalytics.com/hc/en-us/articles/5281585000599)**. |

## Exported File Output

These messages may appear in export output files (for example Excel, RTF, PDF, CSV)

|  |  |
| --- | --- |
| Error Message | Chart Error: This chart references one or more cells that are no longer on the report. |
| Possible Causes | A chart has added to a report that references cells that have since been hidden, removed or relocated. |
| Potential Remedies | 1. Correct the cell references on the chart to reference the correct locations. |

---

|  |  |
| --- | --- |
| Error Message | There was an error rendering the chart image. Please contact your administrator. |
| Possible Causes | There is an incompatibility with items on the report and the wkHtmlToImage chart rendering library. |
| Potential Remedies | Switch to the Puppeteer chart rendering library, by setting `useWkHtmlToImage` to *False* in the `appSettings.config` files. For more information, see [Application Settings](https://devnet.logianalytics.com/hc/en-us/articles/5281615366423-Application-Settings) |

---

|  |  |
| --- | --- |
| Error Message | To render a chart, please uncheck “Flatten Groups in Excel and CSV” under “Export Settings” in the Settings menu |
| Possible Causes | A report that includes a visualization was exported as a Microsoft Excel workbook, but the **Flatten Groups in Excel and CSV** option is enabled. |
| Potential Remedies | 1. In the report’s Export Settings, disable **Flatten Groups in Excel and CSV**. 2. Select a different report export format 3. Remove the chart from the report. |

---

|  |  |
| --- | --- |
| Error Message | To see more data, please uncheck “Flatten Groups in Excel and CSV” under “Export Settings” in the Settings menu, or check “Include Detail Rows” in the Report Section Display Options dropdown |
| Possible Causes | A report was exported as a Microsoft Excel workbook with the **Flatten Groups in Excel and CSV** option enabled, and there are no detail rows to include on the report. |
| Potential Remedies | 1. In the report’s Export Settings, disable **Flatten Groups in Excel and CSV**. 2. Make sure detail rows are included in the report. |

## Web Application Log File

---

|  |  |
| --- | --- |
| Error Message | SQL aggregate requirement failed due to: |
| Possible Causes | A report has been disqualified for Database Aggregation. |
| Potential Remedies | Review the List of Database Aggregation exceptions and the Best Practices When Report Building section of [Database Aggregation](https://devnet.logianalytics.com/hc/en-us/articles/5281607025943-Database-Aggregation). |

---

|  |  |
| --- | --- |
| Error Message | Error reading configuration file: /tmp/7be7125d-46ec-4cc1-998d-bf9146c6f7ed.api light bulb The path and file name will vary based on environment and configuration. |
| Possible Causes | Exago cannot read from its temporary files location. |
| Potential Remedies | 1. Change the **Admin Console** > **General** > **Main Settings** > **Temp Path** to a directory outside of the operating system’s temporary directory. Exago will handle its own removal of temporary files. It is possible the operating system may delete files before Exago is done with them. |

---

|  |  |
| --- | --- |
| Error Message | light bulb The placeholders a.b.c.d and w.x.y.z have been used below to represent two different Exago version numbers. These numbers will vary in each environment  Exception during Page\_Load Type: System.Exception Message: Incompatible eWebReports API versions: API=a.b.c.d, eWebReports application=w.x.y.z. If using Web Service API, use Setup application to update, or update API reference if using .NET Assembly API. |
| Possible Causes | The version of `WebReportsApi.dll` that the host application is referencing is different than that of the installed version of Exago. |
| Potential Remedies | Update the reference to the current `WebReportsApi.dll` as described in step #4 of [Updating Recommendations](https://devnet.logianalytics.com/hc/en-us/articles/5281618359959-Updating-Recommendations). |

---

|  |  |
| --- | --- |
| Error Message | ``` Exception during Page_Load Type: System.ArgumentException Message: Illegal characters in path. ```   or   ``` Exception during Page_Load Type: System.NullReferenceException Message: Object reference not set to an instance of an object. ``` |
| Possible Causes | 1. One or more reports in the storage management database contains one of the illegal characters such as  `? : / * “ > <`. 2. The ROOT content item in the storage management database contains anything in place of null for values that should be null such as the name and description fields. |
| Potential Remedies | 1. Remove illegal characters from report names. A simple `SELECT` can be used to find illegal names. 2. Remove any non-null values from the ROOT item, including the string “null”. |

---

|  |  |
| --- | --- |
| Error Message | Exception Getting AllDbConfigs System.IO.FileNotFoundException: Could not load file or assembly ‘Newtonsoft.Json, Version=9.0.0.0, Culture=neutral, PublicKeyToken=30ad4fe6b2a6aeed’ or one of its dependencies. Report Threw Exception System.Exception: Compiler error: Metadata file `WebReportsApi.dll’ could not be found. |
| Possible Causes | The installed Mono version is not one supported by Exago. |
| Potential Remedies | Exago only supports the Mono versions that are listed in our Technical Specifications topic. It is very highly recommended to let the Exago installer install the Mono runtime. See [Technical Specifications](https://devnet.logianalytics.com/hc/en-us/articles/5281616408727-Technical-Specifications). |

---

|  |  |
| --- | --- |
| Error Message | Storage Management Failed to Initialize: Could not invoke any constructor |
| Possible Causes | The path in the **Admin Console** > **Storage Management** > **Database Connection** is invalid and the Storage Management database cannot be reached. |
| Potential Remedies | Verify that the path is correct by clicking the **Check Database Settings** button. Correct the connection string if necessary. |

---

|  |  |
| --- | --- |
| Error Message | Could not find file ‘<path>js.es6.resource’ |
| Possible Causes | 1. In *pre-v2019.2*, the Puppeteer rendering library is enabled and shadow copying is also enabled. |
| Potential Remedies | 1. Disable shadow copying. More information is available from [MSDN](https://docs.microsoft.com/en-us/previous-versions/dotnet/netframework-4.0/ms228159(v=vs.100)?redirectedfrom=MSDN). 2. Update the installed version of Exago to the latest version. |

---

|  |  |
| --- | --- |
| Error Message | WebReports.Api.CloudStorage.CloudStorageBase — Exception obtaining file from cloud : The process cannot access the file because it is being used by another process. |
| Possible Causes | 1. Using an unsupported temp file cloud storage service, or the service is misconfigured. 2. Using an unsupported session state service. |
| Potential Remedies | 1. Ensure that the temporary file cloud storage service is setup correctly. 2. Ensure that the session state service is setup properly. Review [Setting up a State Server](https://devnet.logianalytics.com/hc/en-us/articles/5281581463959-Setting-up-a-State-Server). |

## Scheduler Service Log File

|  |  |
| --- | --- |
| Error Message | System.IO.FileNotFoundException: Could not find file ‘C:\working\6468deff-5fcb-45e8-822f-441be90aec26.xml’. light bulb The path and file name will vary based on environment and configuration. |
| Possible Causes | The Scheduler Service could not locate some or all of its working files. This may be because the Scheduler Service’s working directory was changed or has become unavailable. |
| Potential Remedies | 1. Verify that the `<working_directory>` in the Scheduler Service configuration file exists and is available for reading and writing by the Scheduler Service. 2. Verify that the `<working_directory>` in the Scheduler Service configuration file has not changed. If it has, copy all of the working files from the old location to the new one then restart the Scheduler Service. |

---

|  |  |
| --- | --- |
| Error Message | Could not create WrUserMessage for ‘ExecuteReportEmptyMsg’” In *v2020.1+*, the Report ID will be included in the error message email (if an email address is defined in the Scheduler Service’s configuration file. |
| Possible Causes | A scheduled job produced an empty report. This is different from NDQ where the report has content but no data, it is when the execution returns a completely empty report. |
| Potential Remedies | Locate the report with the ID indicated in the error email or in the Scheduler’s log. Edit the report as necessary. |

## REST Web Service API Log File

---

|  |  |
| --- | --- |
| Error Message | ``` [Rest.RESTErrorHandler.OnException] Error in REST Service Type: WebReports.Rest.ExagoRestException Message: The requested report is either missing, or is not supported for this service. Source: WebReportsRest ``` |
| Possible Causes | 1. The report that is trying to be loaded does not exist anymore, or the path and report name provided are incorrect. 2. One of the `GetExecute()` methods was called on a Dashboard. 3. One of the `GetExecute()` methods was called on an ExpressView in a version of the application *pre-v2019.1.31*, *pre-v2019.2.19* or *pre-v2020.1.1.5*. |
| Potential Remedies | 1. Check that the report exists in the folder that it is expected to be in. Check spelling of path and report name. 2. Dashboards are not supported by the GetExecute() methods. Use a different execution method. For more information, review the [Executing Reports with the API](https://devnet.logianalytics.com/hc/en-us/articles/5281660714135-Executing-Reports-with-the-API) topic. 3. GetExecute() for ExpressView is supported in *v20191.31+*, *2019.2.19+* and *v2020.1.5+* only. Update to one of those versions, or use a different execution method. For more information, review the [Executing Reports with the API](https://devnet.logianalytics.com/hc/en-us/articles/5281660714135-Executing-Reports-with-the-API) topic. |

---

|  |  |
| --- | --- |
| Error Message | ``` Type: System.Exception Message: setupDs is null; setupFn: <path>.api.enc  Source: WebReportsRest TargetSite: WebReports.Api.Api LoadApi(System.String)  StackTrace: at WebReports.Rest.RESTHelper.LoadApi(String sid) ```   This error message will be accompanied by an HTTP 500 error in the REST API along with this response:   ``` {  "reason": "setupDs is null; setupFn: <path>.api.enc",  "stacktrace": null } ```   where <path> represents Exago’s temp files path and a GUID |
| Possible Causes | The session cannot be found because one of the following may have happened:  1. The session was consumed because the **AppUrl** has already been visited. 2. An invalid session ID was supplied in the `?sid=` parameter when making API calls 3. The web server was restarted |
| Potential Remedies | 1. Do not browse to the **AppUrl** until all calls have been made, as this closes the session and prevents any further changes to it. 2. Check to verify that the session ID is correct. Discard the session and start a new one if required. |

## Additional Resources

For more troubleshooting assistance, review these resources:

* [Admin Support Lab — Troubleshooting for Admins](https://devnet.logianalytics.com/hc/en-us/articles/5281571335063-Troubleshooting-for-Admins) (video)
