---
title: "Standard Logi Application Folders"
id: 4406817720471
section: "Introduction to Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817720471-Standard-Logi-Application-Folders
updated_at: 2022-04-06T06:07:47Z
---

# Standard Logi Application Folders

# Standard Logi Application Folders

A Logi application is comprised of Logi Server Engine files, *definition* files, and *support* files, stored in specific folders, under an application root folder. Development work consists primarily of creating definition files and adding support files.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) In keeping with standard web server file security conventions, files in folders under the Logi application root folder are "available" to the application, meaning that the account the web server uses to run the application has file access permissions in these folders. Files *outside* the root folder are generally not available.

You *must not* modify the names or contents of these standard folders:

* **bin** - The Logi Server Engine files for a .NET application.
* **assemblies** - Files that map .NET modules into Java servlets (Java application only).
* **rdTemplate** - Component definitions, style, and scripting files used by the Logi Server Engine.
* **rdDataCache** - Temporary data cache files (this folder is created automatically when the application runs).
* **rdDownload** - Temporary files created by the application (also created automatically).
* **WEB-INF** - The Logi Server Engine files for a Java application.

You may notice that each Logi Info application contains its own set of Logi Engine files and this makes the size of each application fairly large. Why not provide one copy of the engine files in a central location? When each application has its own engine files, there are no problems distributing or running it when *multiple applications of differing versions* are run on the same web server.

You *can* create and modify files in these standard folders, but *do not modify* the actual folder names:

* **\_Data** - Appears when a special Logi definition is created that makes an application a JSON data provider.
* **\_Definitions** - (Required) Report, process, and settings files that you create. Standard subfolders include \_Processes and \_Reports, which are part of every application.
* **\_Metadata** - Appears when the Web Metadata Builder is used to create metadata files.
* **\_MobileReports** - Appears when you create special mobile report definitions.
* **\_SupportFiles** - (Required) Image, style sheet, HTML, JavaScript, and XML files you import or create.
* **\_Templates** - Appears when you create special definitions for use with Word, Excel, and PDF templates.
* **\_Themes** - Used when custom Themes are added to the application.
* **\_Plugins** - Used when plug-in .DLLs and/or Java files are part of the application.
* **\_Widgets** - Appears when you create special Logi Widget definitions.

You can also add custom folders beneath the application root folder, for example, to contain data or exported files. Take care when creating these folders to ensure that they're given the same file access permissions as the root folder (permissions aren't always inherited, especially when copying files and folders).
