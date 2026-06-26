---
title: "Introduction to Action Events"
id: 5281598603671
section: "Extensibility"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281598603671-Introduction-to-Action-Events
updated_at: 2022-05-03T22:08:59Z
---

# Introduction to Action Events

# Introduction to Action Events

This topic applies to the **Admin Console** > ![TreeData.png](https://devnet.logianalytics.com/hc/article_attachments/5432184487703/treedata.png)**Extensions** > ![TreeServerEvent.png](https://devnet.logianalytics.com/hc/article_attachments/5432281693719/treeserverevent.png)**Actions Events** settings.

---

**Action Events** can be grouped into two general categories: **Local** and **Global** events.

* **Local** events have two sub-categories:
  + Handlers attached to items in reports and set to fire automatically, or when the item is interacted with in the Report Viewer.
  + Handlers attached to items in the Web Application User Interface and set to fire when that item is clicked.
* **Global** events are active throughout the application, and fire when specific events occur.

This topic explains how to create **Local** and **Global Action Events**, describes the ways in which **Action Events** can interact with the Exago application, and lays out examples for common usage.

## Create, Edit, Delete Action Events

* To **add** a new action event click **![TreeData.png](https://devnet.logianalytics.com/hc/article_attachments/5432184487703/treedata.png) Extensions > ![TreeServerEvent.png](https://devnet.logianalytics.com/hc/article_attachments/5432281693719/treeserverevent.png) Action Events** in the Main Menu and either:
  + click the **Add**![+](https://devnet.logianalytics.com/hc/article_attachments/5432238187799/adminadd.png) icon at the top of the main menu
  + right-click and select ![+](https://devnet.logianalytics.com/hc/article_attachments/5432231941911/addnew.png)**Add** from the context menu
* To **edit** an action event either:
  + double click it
  + select it and click the **Edit** ![pencil](https://devnet.logianalytics.com/hc/article_attachments/5432227755287/adminopen.png) icon at the top of the main menu
  + right-click it and select ![pencil](https://devnet.logianalytics.com/hc/article_attachments/5432185311127/edit.png)**Edit** from the context menu
* To **delete** an action event either:
  + select it and click the **Delete** ![AdminDelete.png](https://devnet.logianalytics.com/hc/article_attachments/5432232296599/admindelete.png) icon at the top of the main menu
  + right-click it and select ![X](https://devnet.logianalytics.com/hc/article_attachments/5432232340503/deletereportsmall.png)**Delete** from the context menu
* To **save** changes and new functions click the **Apply** or **Okay** buttons

They can also be added or modified on a per-session basis via the .NET API using the `Api.SetupData.ActionEvents` server call. This section details how to create **Action Events** through the Web Application but contains important details about programming them which will apply to the .NET API as well.

## Action Event Properties

Each **Action Event** has the following properties:

### Name

A unique identifier for each **Action Event**.

### Function

Can either be custom code or a .NET Assembly method.

#### Custom Code

To save code directly in Exago, select *Custom Code* from the first **Function** dropdown. Clicking on the second dropdown opens the **C****Custom Code** dialog. See the [Writing Action Events](#Writing) or information on how to access the arguments for each Event.

![oFHdaZCB7K.png](https://devnet.logianalytics.com/hc/article_attachments/5432247914391/ofhdazcb7k.png)

Custom Code has four additional properties:

* **Language**: Code can be written in C#, JavaScript (in Windows only) or VB.NET.
* **References:** A semicolon-separated list of any libraries that need to be referenced by the **Action Event**. The DLLs must be present in the `bin` folder of the Exago Web Application, as well as any **Scheduler Service**`bin` folders, and the **REST Web Service API**, if applicable.   
  > ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
  >
  > `System.dll` does not need to be listed as a reference as it is already available.
* **Namespaces:** A semicolon-separated list of namespaces in the referenced DLLs or the **Exago API**library.
* **Code:** The code that will be executed.  
  When done writing code, click the **Test Execution ![✓](https://devnet.logianalytics.com/hc/article_attachments/5432216091799/checkmark.png)** icon to test the code for errors.

#### .NET Assembly Method

There are two ways to reference a .NET Assembly method.

* Create a [Assembly Data Sources](https://devnet.logianalytics.com/hc/en-us/articles/5281582189591-Assembly-Data-Sources). Select the desired assembly from the first Function dropdown. Clicking on the second dropdown will open a list of available methods.
* Add the .NET Assembly to the Bin folder (for the Web Application, Web Service API, and all Scheduler Services, if applicable). Then in the **Custom Code**, add the assembly as a reference, then invoke the method, for example  
  `return Extensions.Events.CensorEmployeeBirthYear(sessionInfo, args);`

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> The Assembly’s DLL will be locked by Exago when it is first accessed. To replace the DLL, unlock it by restarting the IIS App pool.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> If you want to utilize the **sessionInfo** object that is passed to all **Action Events** the Assembly must include a reference to `WebReportsApi.dll`. For more information see [SessionInfo](https://devnet.logianalytics.com/hc/en-us/articles/5281621102743-SessionInfo).

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> All methods used as **Action Events** must be static.

### Event Type

Select an option in this dropdown to create an local event that will be executed when certain client-side actions are taken.

* **None:** This **Action Event** is a **Global Event**. A value must be set for **Global Event Type**.
* **Load:** The **Action Event** will execute when a report item is loaded in the **Report Designer**, **Report Viewer**, or upon **Export**. This type of handler is typically used to interpret and then apply alterations to report data, for example conditionally changing the colors on charts or maps.
  + As of *v2016.2.5+*  **Load** events can affect Export formats (*PDF*, *Excel*, *RTF*, *CSV*).
* **Click:** The **Action Event** will execute when a user clicks on an item in a report or in the Exago UI. This type of handler is typically used to add additional interactive elements to reports or to the **Report Designer**. Click events will not function on Export formats.  
  For information on adding action events to specific reports, see

### Global Event Type

Select an option in this dropdown to create an event that will be triggered when a condition is met in the Exago application. [Global Action Events](https://devnet.logianalytics.com/hc/en-us/articles/5281621334167-Global-Action-Events) contains descriptions of all of the available event handlers.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Selecting a **Global Event Type** will cause Exago to ignore any selected Local **Event Type**.

### Assigned UI Item(s)

This field designates a semicolon-separated list of [Actionable UI Elements](https://devnet.logianalytics.com/hc/en-us/articles/5281613121175-Actionable-UI-Elements) for items in the Exago interface. These elements can be intercepted and modified by entering them in this field.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> This selection field only applies when the **Event Type** is **Click**. This field will be ignored when any other options are selected.

## Writing Action Events

When an **Action Event** is fired, two primary parameter objects are passed: **sessionInfo** and **clientInfo**. These are the main points of interaction with the Exago application.

* **sessionInfo**: Provides access to all the elements of the current Exago session. This is the server-side information. For more information see [SessionInfo](https://devnet.logianalytics.com/hc/en-us/articles/5281621102743-SessionInfo).
  > ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
  >
  > To access **sessionInfo** from a .NET Assembly, include a reference to `WebReportsApi.dll`
* **clientInfo**: A JavaScript object that is accessed from within the client-side script. Provides access to any specified client-side parameters and information about the item attached to the **Action Event**. For a breakdown of the elements in clientInfo, see [ClientInfo](https://devnet.logianalytics.com/hc/en-us/articles/5281598528663-ClientInfo)

**arguments array** – The server-side portion of action events can also access an array of input values called **args**. These parameters are passed manually from client code to server code using the function `clientInfo.ServerCallback(eventName, args...)`.

## Additional Resources

* Admin Support Lab — [Custom Interactivity via HTML & Action Events](https://devnet.logianalytics.com/hc/en-us/articles/5281553332119-Custom-Interactivity-via-HTML-Action-Events) (video)
