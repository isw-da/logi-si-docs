---
title: "Custom Functions"
id: 5281628193815
section: "Installation and Configuration"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281628193815-Custom-Functions
updated_at: 2023-04-03T17:52:19Z
---

# Custom Functions

# Custom Functions

This topic applies to the **Admin Console** > ![TreeData.png](https://devnet.logianalytics.com/hc/article_attachments/5432184487703/treedata.png)**Extensions** > ![TreeFunction.png](https://devnet.logianalytics.com/hc/article_attachments/5432240624151/treefunction.png)**Functions** settings.

---

Exago BI comes with a number of functions that can be used to make formulas in the **Formula Editor**. Administrators may create additional custom functions using high level coding languages which will be accessible to end-users of the **Report Designer**. Functions can be added to a preexisting folder or a function can be put into a new custom folder.

**Custom Functions** can be written in C#, VB.NET, or JavaScript (Windows only). Functions can take as many input arguments as needed.

Functions can get and set elements of the current session state of Exago BI such as **Parameter** values. See [SessionInfo](https://devnet.logianalytics.com/hc/en-us/articles/5281621102743-SessionInfo) for more information.

## Create, Edit, Delete, Restore Custom Functions

* To **add** a new custom function click **![TreeData.png](https://devnet.logianalytics.com/hc/article_attachments/5432184487703/treedata.png) Extensions > ![TreeFunction.png](https://devnet.logianalytics.com/hc/article_attachments/5432240624151/treefunction.png)Functions** in the Main Menu and either:
  + click the **Add**![+](https://devnet.logianalytics.com/hc/article_attachments/5432238187799/adminadd.png) icon at the top of the main menu
  + right-click and select ![+](https://devnet.logianalytics.com/hc/article_attachments/5432231941911/addnew.png)**Add** from the context menu
* To **edit** a function either:
  + double click it
  + select it and click the **Edit** ![pencil](https://devnet.logianalytics.com/hc/article_attachments/5432227755287/adminopen.png) icon at the top of the main menu
  + right-click it and select ![pencil](https://devnet.logianalytics.com/hc/article_attachments/5432185311127/edit.png)**Edit** from the context menu
* To **delete** an object either:
  + select it and click the **Delete** ![AdminDelete.png](https://devnet.logianalytics.com/hc/article_attachments/5432232296599/admindelete.png) icon at the top of the main menu
  + right-click it and select ![X](https://devnet.logianalytics.com/hc/article_attachments/5432232340503/deletereportsmall.png)**Delete** from the context menu
* To **restore** the default custom functions that come with the application either:
  + right-click **![TreeData.png](https://devnet.logianalytics.com/hc/article_attachments/5432184487703/treedata.png) Extensions > ![TreeFunction.png](https://devnet.logianalytics.com/hc/article_attachments/5432240624151/treefunction.png)Functions** in the Main Menu and select ![RefreshSmall.png](https://devnet.logianalytics.com/hc/article_attachments/5432216675479/refreshsmall.png)**Restore All Formula Functions** from the context menu
  + **General** > ![TreeGeneralNode.png](https://devnet.logianalytics.com/hc/article_attachments/5432159353239/treegeneralnode.png)**Filter Settings** > **Restore All Default Formula Functions** and click on the ![Refresh.png](https://devnet.logianalytics.com/hc/article_attachments/5432258806679/refresh.png)**Restore** button.
* To **save** changes and new functions click the **Apply** or **Okay** buttons

## Custom Function Properties

Each **Custom Function** has the following properties.

### Name

A name for the function that will be displayed to the end users. Required.

### Description

A description of the function that will be displayed to the end users.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
>
> To support multi-language functionality, you can supply an Id from a language file instead of a static string. For more information, see [Multi-Language Support](https://devnet.logianalytics.com/hc/en-us/articles/5281604247447-Multi-Language-Support).

### Minimum Number of Arguments pre-v2017.2

The minimum number of values that an end user must enter in the function separated by commas.

### Maximum Number of Arguments pre-v2017.2

The maximum number of values that an end user may enter in the function separated by commas.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Arguments are passed to the code as an array of generic objects, accessed as `args[ ]`.

### Category

A way of grouping similar functions. You can assign custom functions to an existing Exago BI category or create a new category.

To create a new category:

1. For all applicable language files, add a new language translation ID for the new category name. The element ID must begin with `FormulaEditor` and end with `Node`. For example:

   ```
    <element id="FormulaEditorVeryCoolFunctionsNode">Very Cool Functions</element>
   ```
2. Select *Other* from the **Category** dropdown list.
3. An input field entitled **Specific Category Name** will appear. Enter the language file ID created in step 1.

![](https://devnet.logianalytics.com/hc/article_attachments/5432216702487/category-name.png)

The language filed ID is provided in the **Specify Category Name (Optional)** field

  
![](https://devnet.logianalytics.com/hc/article_attachments/5432240797591/custom-category-name.png)

Formula Editor dialog showing the custom category name **Very Cool Functions**

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> Providing a static text string that does not match a language file ID for the **Specify Category Name (Optional)** field is not valid.

### Return Type v2018.2.6+

A return type must be specified for each Custom Function. This field can be defined as a *String*, *Integer*, *Decimal*, or *Date*, and determines the expected return type of each function.

### Prevent In-Database Grouping When Included in Detail Section v2019.1.5+

You may use this flag to specify whether this function has side-effects and should disqualify including reports from aggregating in the database (thus skipping the function when in a suppressed Detail section). For example, most functions that build or manipulate memory storage with Get/SetStoredValue should have this flag set to true.

### Language

The high-level language of the code for the function. Can be C# or VB.NET, or JavaScript (Windows only).

### References

A semicolon-separated list of any DLLs that need to be referenced by the Custom Function. The DLLs must be present in the `bin` folder of the Exago BI Web Application, Scheduler Services, and the Web Service API if applicable. This folder can be found in the installation directory of the respective component.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
>
> `System.dll` does not need to be listed as a reference as it is already available.

### Namespaces

A semicolon-separate list of any namespaces that need to be referenced by the Custom Function.

### Program Code

The program code for the Custom Function. Press the green check mark to verify the code executes properly. Required.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> To use a .NET Assembly for custom functions, first add it to the applicable `bin` folders. Then add the assembly as a reference in the Custom Code window, and invoke the method, for example, `return Extensions.Functions.DayBefore(args);`.

### Arguments

Starting with version *v2017.2* there are several enhancements to the way function arguments are implemented and used.

Click **Edit Argument Info** to show a dialog for managing arguments. Then click **Add Argument** for each argument the function will have. Arguments have the following properties:

#### Name

The name of the argument, which will appear as a placeholder in the function parentheses and in the function’s description tooltip.

#### Description

A description for what the argument is used for. You should mention the expected data type, if it is not obvious. This will appear in a tooltip when the placeholder name is selected.

Can also be a **language file ID**. See [Multi-Language Support](https://devnet.logianalytics.com/hc/en-us/articles/5281604247447-Multi-Language-Support).

#### Optional

Whether this argument is required or optional. Optional arguments are surrounded by brackets [ ] in the function’s description tooltip.

#### Variable Argument Count

If selected, the last argument in the list accepts more than one value. Variable arguments are followed by an ellipsis (…) in the function’s description tooltip.

## SessionInfo

See [SessionInfo](https://devnet.logianalytics.com/hc/en-us/articles/5281621102743-SessionInfo).

## Default Custom Functions v2017.2+

Exago BI ships with several built-in custom functions in *v2017.2+*. These are functions that are common in many reporting environments, but the manner in which they work may be different depending on locality, time zone, or other factors. For this reason, these functions have been exposed in the Admin Console so that administrators may change how they work.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
>
> If these functions are unavailable, such after an upgrade, in the **Admin Console** navigate to **General** > [Filter Settings](https://devnet.logianalytics.com/hc/en-us/articles/5281628457495-Filter-Settings) > **Restore All Default Formula Functions** and click on the ![Refresh.png](https://devnet.logianalytics.com/hc/article_attachments/5432258806679/refresh.png)**Restore** button.

The following custom functions ship with Exago BI:

### MonthName

|  |  |
| --- | --- |
| Description | Given a date value, returns the name of the month of that date. The month name is retrieved from the active language dictionary. For example, given the date “01/01/2017”, MonthName() will return “January” in an English-speaking environment, and “Enero” in a Spanish-speaking environment. |
| Arguments | * `inputDateOrNumber`: A formatted date string, a Date or DateTime value, or an integer value. Required. |
| References | * mscorlib.dll |
| Example | These examples are in an English-speaking environment: `MonthName("02/29/2020")` February `MonthName(3)` March  `MonthName(1989-07-06 22:19:21)` July |

### QuarterName

|  |  |
| --- | --- |
| Description | Given a date value, returns the fiscal quarter of the date, as “Q1”, “Q2”, “Q3”, or “Q4”. By default, Q1 encompasses January 01 – March 31, Q2 encompasses April 01 – June 30, Q3 encompasses July 01 – Sept 30, and Q4 encompasses Oct 01 – Dec 31. But since different countries or financial landscapes may use different systems of quarters, the behavior of the function is exposed and customizable. |
| Arguments | * `inputDate`: A formatted date string, Date value, or DateTime value. Required. |
| Example | `QuarterName("02/29/2020")` Q1 `QuarterName(1989-07-06 22:19:21)` Q3 |

### QuarterNumber

|  |  |
| --- | --- |
| Description | Given a date value, returns the fiscal quarter of the date, as “1”, “2”, “3”, or “4”. By default, Q1 encompasses January 01 – March 31, Q2 encompasses April 01 – June 30, Q3 encompasses July 01 – Sept 30, and Q4 encompasses Oct 01 – Dec 31. But since different countries or financial landscapes may use different systems of quarters, the behavior of the function is exposed and customizable. |
| Arguments | * `inputDate`: A formatted date string, Date value, or DateTime value. Required. |
| Example | `QuarterNumber("02/29/2020")` 1 `QuarterNumber(1989-07-06 22:19:21)` 3 |

## Additional Resources

* Admin Support Lab — [Custom Functions](https://devnet.logianalytics.com/hc/en-us/articles/5281547321623-Custom-Functions) (video)
* Admin Support Lab — [Date Check Custom Functions](https://devnet.logianalytics.com/hc/en-us/articles/5281531812887-Date-Check-Custom-Functions) (video)
* Admin Support Lab — [Dynamic Rank Custom Function](https://devnet.logianalytics.com/hc/en-us/articles/5281539713687-Dynamic-Rank-Custom-Function) (video)
