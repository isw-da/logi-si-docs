---
title: "Introduction to Server Events"
id: 5281583100439
section: "Extensibility"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281583100439-Introduction-to-Server-Events
updated_at: 2022-05-03T22:09:00Z
---

# Introduction to Server Events

# Introduction to Server Events

This topic applies to the **Admin Console** > ![TreeData.png](https://devnet.logianalytics.com/hc/article_attachments/5432184487703/treedata.png)**Extensions** > ![play](https://devnet.logianalytics.com/hc/article_attachments/5432281693719/treeserverevent.png "None of the Server Event Handlers are Global Server Event Handlers")![globe](https://devnet.logianalytics.com/hc/article_attachments/5432247835031/treeservereventglobe.png "At least one of the Server Event Handlers is a Global Server Event Handler")**Server Events** settings.

---

**Server Event Handlers** provide code that Exago BI can execute when certain events happen during the application runtime. This code can either come from a .NET Assembly or be written in a high-level programming language.

## Create, Edit, Delete Server Event Handlers

* To **add** a new server event click **![TreeData.png](https://devnet.logianalytics.com/hc/article_attachments/5432184487703/treedata.png) Extensions > ![TreeServerEvent.png](https://devnet.logianalytics.com/hc/article_attachments/5432281693719/treeserverevent.png) Server Events** in the Main Menu and either:
  + click the **Add**![+](https://devnet.logianalytics.com/hc/article_attachments/5432238187799/adminadd.png) icon at the top of the main menu
  + right-click and select ![+](https://devnet.logianalytics.com/hc/article_attachments/5432231941911/addnew.png)**Add** from the context menu
* To **edit** an event either:
  + double click it
  + select it and click the **Edit** ![pencil](https://devnet.logianalytics.com/hc/article_attachments/5432227755287/adminopen.png) icon at the top of the main menu
  + right-click it and select ![pencil](https://devnet.logianalytics.com/hc/article_attachments/5432185311127/edit.png)**Edit** from the context menu
* To **delete** a server event either:
  + select it and click the **Delete** ![AdminDelete.png](https://devnet.logianalytics.com/hc/article_attachments/5432232296599/admindelete.png) icon at the top of the main menu
  + right-click it and select ![X](https://devnet.logianalytics.com/hc/article_attachments/5432232340503/deletereportsmall.png)**Delete** from the context menu
* To **save** changes and new server events click the **Apply** or **Okay** buttons

## Server Event Handler Properties

Each **Server Event Handler** has the following properties:

### Name

Provides a unique identifier for each Event Handler

### Function

Choose between *Custom Code* or the name of a .NET Assembly. If there are no [.NET Assembly Data Sources](https://devnet.logianalytics.com/hc/en-us/articles/5281582189591-Assembly-Data-Sources) available, *Custom Code* is the only available option.

#### Custom Code

To save code directly in Exago, select *Custom Code* from the first function dropdown. Clicking on the second dropdown opens the custom code dialog.

![Ct2ri5FsKK.png](https://devnet.logianalytics.com/hc/article_attachments/5432219522327/ct2ri5fskk.png)

Custom Code dialog

**Custom Code** has three additional properties:

* **Language**: Code can be written in C#, JavaScript (in Windows only) or VB.NET.
* **References**: A semicolon-separated list of any DLLs that need to be referenced by the code. The DLLs must be present in the `bin` folder of the Exago BI Web Application, Scheduler Services, and the Web Service API if applicable. This folder can be found in the installation directory of the respective component.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
>
> `System.dll` does not need to be listed as a reference as it is already available.

* **Namespaces:** A semicolon-separated list of namespaces in the referenced DLLs or the Exago BIAPI library.
* **Code:** The code that will be executed by Exago BI when called. See [Arguments](#Argument) for information on how to access the arguments for each Event. When finished, click the **Test Custom Code** ![Checkmark.png](https://devnet.logianalytics.com/hc/article_attachments/5432216091799/checkmark.png) icon to check if the code compiles.

#### .NET Assembly

There are two ways to reference a .NET Assembly method.

1. Create a .NET Assembly [**Data Source**](https://devnet.logianalytics.com/hc/en-us/articles/5281617045911-Data-Sources). Select the desired assembly from the first **Function** dropdown. Clicking on the second dropdown will open a list of available methods.
2. Add the .NET Assembly  to the `bin` folder of the Exago BI Web Application, Scheduler Services, and the Web Service API if applicable. This folder can be found in the installation directory of the respective component. Then in the **Custom Code** window, add the assembly as a reference and invoke the method, for example:

   ```
   return Extensions.Events.CensorEmployeeBirthYear(sessionInfo, args);
   ```

### Global Event

Determine when this **Server Event Handler** will be called, either whenever specific event type occurs, or only when that event occurs for specific reports.

* Select a **Global Event** from the list to indicate that the **Event Handler** should be called whenever this event occurs in the application for all report executions.
* Leave **Global Event** set to *None* to indicate the **Event Handler** is meant for a specific report. For example, selecting *OnReportExecuteStart* from this dropdown will cause the Event Handler to be called at the start of any Report Execution.

## Arguments

**Server Event Handlers** can access the following information in order to inspect the session state, and utilize built-in methods:

* **sessionInfo** – The **[sessionInfo](https://devnet.logianalytics.com/hc/en-us/articles/5281621102743-SessionInfo)**object provides access to elements of Exago BI’s current session such as parameters, filters, and the current report.
* **args**– Events may have access to an array of values called ***args***. For each Event the content of the array will be different.

## .NET Assemblies

The following are important details for using .NET Assemblies as **Server Event Handlers**.

* The Assembly DLL is locked by Exago BI when first accessed. To replace the DLL, unlock it by restarting the IIS App Pool (and Scheduler Services, if applicable).
* The first argument of all Event Handlers is the **[sessionInfo](https://devnet.logianalytics.com/hc/en-us/articles/5281621102743-SessionInfo)**object which can be used to access elements within the Exago BI session. To make use of this object the assembly must reference `WebReportsApi.dll`.  
  If the code does not need to make use of sessionInfo then the method signature in the assembly can declare sessionInfo as an object instead of as a sessionInfo data type.
* All methods used as Event Handlers must be static.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> If `WebReportsApi.dll` or another Exago BI DLL is referenced by the assembly, then it must be recompiled to the current version whenever Exago BI is updated.
