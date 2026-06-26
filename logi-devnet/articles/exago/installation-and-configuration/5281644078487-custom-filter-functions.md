---
title: "Custom Filter Functions"
id: 5281644078487
section: "Installation and Configuration"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281644078487-Custom-Filter-Functions
updated_at: 2023-04-03T17:52:19Z
---

# Custom Filter Functions

# Custom Filter Functions

This topic applies to the **Admin Console** > ![TreeData.png](https://devnet.logianalytics.com/hc/article_attachments/5432184487703/treedata.png)**Extensions** >**![TreeFilterFunction.png](https://devnet.logianalytics.com/hc/article_attachments/5432125960215/treefilterfunction.png) Filter Functions** settings.

---

**Custom Filter Functions** provide the ability to make functions that will dynamically calculate a value for a filter using high level code.

Filter Functions can be written in C#, JavaScript, or VB.NET. Filter Functions written in C# and VB.NET can get and set elements from the current session of Exago BI, such as Parameter values. See [SessionInfo](https://devnet.logianalytics.com/hc/en-us/articles/5281621102743-SessionInfo) for more information.

## Create, Edit, Delete, Restore Custom Filter Functions

* To **add** a new custom filter function click **![TreeData.png](https://devnet.logianalytics.com/hc/article_attachments/5432184487703/treedata.png) Extensions > ![TreeFilterFunction.png](https://devnet.logianalytics.com/hc/article_attachments/5432125960215/treefilterfunction.png) Filter Functions** in the Main Menu and either:
  + click the **Add**![+](https://devnet.logianalytics.com/hc/article_attachments/5432238187799/adminadd.png) icon at the top of the main menu
  + right-click and select ![+](https://devnet.logianalytics.com/hc/article_attachments/5432231941911/addnew.png)**Add** from the context menu
* To **edit** a function either:
  + double click it
  + select it and click the **Edit** ![pencil](https://devnet.logianalytics.com/hc/article_attachments/5432227755287/adminopen.png) icon at the top of the main menu
  + right-click it and select ![pencil](https://devnet.logianalytics.com/hc/article_attachments/5432185311127/edit.png)**Edit** from the context menu
* To **delete** an object either:
  + select it and click the **Delete** ![AdminDelete.png](https://devnet.logianalytics.com/hc/article_attachments/5432232296599/admindelete.png) icon at the top of the main menu
  + right-click it and select ![X](https://devnet.logianalytics.com/hc/article_attachments/5432232340503/deletereportsmall.png)**Delete** from the context menu
* To **restore** the default custom filter functions that come with the application either:
  + right-click **![TreeData.png](https://devnet.logianalytics.com/hc/article_attachments/5432184487703/treedata.png) Extensions >****![TreeFilterFunction.png](https://devnet.logianalytics.com/hc/article_attachments/5432125960215/treefilterfunction.png) Filter Functions** in the Main Menu and select ![RefreshSmall.png](https://devnet.logianalytics.com/hc/article_attachments/5432216675479/refreshsmall.png)**Restore All Default Date Filter Functions** from the context menu
  + navigate to ![TreeGeneral.png](https://devnet.logianalytics.com/hc/article_attachments/5432174178839/treegeneral.png)**General** > ![TreeGeneralNode.png](https://devnet.logianalytics.com/hc/article_attachments/5432159353239/treegeneralnode.png)[Filter Settings](https://devnet.logianalytics.com/hc/en-us/articles/5281628457495-Filter-Settings) > **Restore All Default Date Filter Functions** and click on the ![Refresh.png](https://devnet.logianalytics.com/hc/article_attachments/5432258806679/refresh.png)**Restore** button.
* To **save** changes and new functions click the **Apply** or **Okay** buttons

## Custom Filter Function Properties

Each Custom Filter Function has the following properties:

#### Name

A name for the filter function that will be displayed to the end users. Required.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
>
> To support multi-language functionality, you can supply an Id from a language file instead of a static string. For more information, see [Multi-Language Support](https://devnet.logianalytics.com/hc/en-us/articles/5281604247447-Multi-Language-Support).

#### Description

A description of the function.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
>
> To support multi-language functionality, you can supply an Id from a language file instead of a static string. For more information, see [Multi-Language Support](https://devnet.logianalytics.com/hc/en-us/articles/5281604247447-Multi-Language-Support).

#### Filter Type

Determines the data type that the filter function should be available for. Either *Date*, *String*, *Integer* or *Decimal*.

#### List Order

The order the filter function will appear among other filter functions of the same type. Functions with a lower number will appear higher on the list. If two functions have the same list value they will display in alphabetic order.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> All of the built in filter functions start with list value 100 or greater.

![screen.CFF_info.png](https://devnet.logianalytics.com/hc/article_attachments/5432216785047/screen.cff_info.png)

#### Language

The high-level language of the code for the date function. May be C#, JavaScript, or VB.NET.

#### References

A semicolon-separated list of any DLLs that need to be referenced by the Custom Filter Function. The DLLs must be present in the `bin` folder of the Exago BI Web Application, Scheduler Services, and the Web Service API if applicable. This folder can be found in the installation directory of the respective component.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> `System.dll` does not need to be listed as a reference as it is already available.

#### Namespaces

A semicolon-separated list of any namespaces that need to be referenced by the **Custom Filter Function**.

#### Program Code

The program code for the Custom Filter Function. The code must return the data type that was set in the **Filter Type** setting.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
>
> Parameters may be referenced within custom functions by placing their name between @s. For example, @userId@

![screen.CFF_code.png](https://devnet.logianalytics.com/hc/article_attachments/5432245975959/screen.cff_code.png)

A Custom Filter Function that returns the date value of the last day of the current quarter

Click the **Test custom code execution**![✓](https://devnet.logianalytics.com/hc/article_attachments/5432241036951/greencheck.png) icon to verify that the code properly compiles.

## Default Custom Filter Functions v2016.3+

See [Default Custom Filter Functions v2016.3+](https://devnet.logianalytics.com/hc/en-us/articles/5281644854295-Default-Custom-Filter-Functions-v2016-3-)

## Additional Resources

* [Default Custom Filter Functions v2016.3+](https://devnet.logianalytics.com/hc/en-us/articles/5281644854295-Default-Custom-Filter-Functions-v2016-3-)
* Admin Support Lab — [Custom Filter Functions](https://devnet.logianalytics.com/hc/en-us/articles/5281547230231-Custom-Filter-Functions) (video)
