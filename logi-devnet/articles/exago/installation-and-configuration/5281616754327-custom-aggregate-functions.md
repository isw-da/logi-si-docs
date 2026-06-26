---
title: "Custom Aggregate Functions"
id: 5281616754327
section: "Installation and Configuration"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281616754327-Custom-Aggregate-Functions
updated_at: 2023-04-03T17:52:19Z
---

# Custom Aggregate Functions

# Custom Aggregate Functions

Exago BI comes with a number of functions to make formulas in the **Formula Editor**. Administrators may create additional custom functions, using high level coding languages, accessible to end-users of the **Report Designer**. In Exago BI*v2019.2+* administrators may also create custom aggregate functions. Custom Aggregate Functions are available in any formula editor in which the existing built-in aggregate functions are also available.

**Custom Aggregate Functions** are written in C# or VB.NET and can take as many input arguments as needed. They can get and set elements of the current session state of Exago BI such as Parameter values. See [SessionInfo](https://devnet.logianalytics.com/hc/en-us/articles/5281621102743-SessionInfo).

## Creating Custom Aggregate Functions

**Custom Aggregate Functions** may be created programmatically through the .NET API or manually through the Web Application. This section details how to create **Custom Aggregate Functions** through the Web Application but contains important details about programming the aggregate function which will apply to the .NET API as well.

1. In the **Admin Console**, navigate to **Extensions** > **Aggregate Functions** then click the  **Add ![+](https://devnet.logianalytics.com/hc/article_attachments/5432238187799/adminadd.png)** icon at the top of main menu. This will open a new **Custom Aggregate Function** tab.

Each **Custom Aggregate Function** has the following properties:

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
>
> The **Description** and **Category** properties below support multi-language functionality, where an Id from a language file instead of a static string may be supplied. See [Multi-Language Support](https://devnet.logianalytics.com/hc/en-us/articles/5281604247447-Multi-Language-Support).

## Name

A name for the function that will be displayed to the end user and will be used to call the function. This name may only contain letters, numbers and underscores, and must be different from any of the built-in aggregate functions.

## Description

A description of the function that will be displayed to the end user when building a formula in the Formula Editor.

## Category

A way of categorizing/grouping similar functions together. Custom Aggregate Functions may be assigned to any existing category or to a new category. By default, custom aggregate functions are added to the *Aggregate* category unless a different one is chosen.

To create a new category:

1. For all applicable language files, add a new language translation ID for the new category name. The element ID must begin with `FormulaEditor` and end with `Node`. For example:

   ```
    <element id="FormulaEditorVeryCoolFunctionsNode">Very Cool Functions</element>
   ```
2. Select *Other* from the **Category** dropdown list.
3. An input field entitled **Specific Category Name (Optional)** appears. Enter the language file ID created in step 1.

![](https://devnet.logianalytics.com/hc/article_attachments/5432216702487/category-name.png)

The language filed ID is provided in the **Specify Category Name (Optional)** field

  
![](https://devnet.logianalytics.com/hc/article_attachments/5432240797591/custom-category-name.png)

Formula Editor dialog showing the custom category name **Very Cool Functions**

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Critical")
>
> Providing a static text string that does not match a language file ID for the **Specify Category Name (Optional)** field is not valid.

## Return Type

A return type must be specified for each **Custom Aggregate Function**. This field can be defined as a *String*, *Integer*, *Decimal*, or *Date*, and determines the expected return type of the function.

## Prevent In-Database Grouping When Included in Detail Section

If the **Custom Aggregate Function** is called from a **Detail** section of a report and that Detail section is suppressed (hidden), setting this flag to *True* will prevent Exago BI from requesting the aggregation be done in the database. Instead aggregation will be done in memory insuring that the **Custom Aggregate Function** is called for each Detail row.

If *False*, Exago BI’s normal behavior determined by the **Database Aggregation** setting is utilized. If applicable, aggregation will be done in the database and then the **Custom Aggregate Function** will be called afterwards. This might cause trouble if the function is intended to work on unaggregated or ungrouped data.

For example, most functions that build or manipulate memory storage with **GetStoredValue**/**SetStoredValue** should have this flag set to *True*.

This flag will have no affect if the **Custom Aggregate Function** is called from any other section besides a **Detail** section.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> If Exago BI’s **Database Aggregation** setting is *False*, then aggregations will never be done in the database regardless of the setting of the **Prevent In-Database Grouping When Included in Detail Section** flag.

## Arguments

Click **Edit Argument Info** to show a dialog for managing arguments.

![Edit argument dialog](https://devnet.logianalytics.com/hc/article_attachments/5432216886295/xuakoyuhli.png)

Edit Argument Dialog

Arguments are passed to the code as an array of generic objects, accessed as **`args[]`**. **Custom Aggregate Functions** have two required arguments, `dataToAggregate` and `recordLevel`.

* **dataToAggregate**: the data field or formula to aggregate. Can be renamed, but must always be the first argument.
* **recordLevel**: indicates whether aggregation should occur at the record level or entity level. If *true*, aggregation occurs on the record level. Can be renamed, but must always be the last argument. Refer to the topics on [Aggregate Functions](https://devnet.logianalytics.com/hc/en-us/articles/5281614243735-Aggregate-Functions) and the **Admin Console**‘s [Other Settings](https://devnet.logianalytics.com/hc/en-us/articles/5281608505879-Other-Settings) for more information on how this argument works.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> `recordLevel` evaluates to true if it is set to any true value (as returned by functions like [True()](https://devnet.logianalytics.com/hc/en-us/articles/5281592227095-Logical-Functions#True2), a nonzero number, or a non-empty string).

To add additional arguments to the function, click the ![+](https://devnet.logianalytics.com/hc/article_attachments/5432278803479/addbtn.png)**Add Argument** button.

To remove arguments from the function, click the **Delete Row ![X](https://devnet.logianalytics.com/hc/article_attachments/5432124748951/deleteitem.png)** icon at the end of the respective row.

Arguments have the following properties:

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
>
> Both **Name** and **Description** properties below support multi-language, where an Id from a language file instead of a static string may be supplied. See [Multi-Language Support](https://devnet.logianalytics.com/hc/en-us/articles/5281604247447-Multi-Language-Support)

### Name

The name of the argument, which will appear as a placeholder in the function parentheses and in the function’s description tooltip.

### Description

A description for what the argument is used for which will appear as a tooltip when the placeholder name is selected.

### Optional

Check the box if a value for the argument does not need to be supplied when the function is called. Leave the box unchecked if a value must be supplied.

If a user does not supply a required argument, the formula editor will highlight the error.

Optional arguments are surrounded by brackets [ ] in the function’s description tooltip.

## Program Code

### Language

The programming language of the code for the function. Either C# or VB.NET.

### References

A semicolon-separated list of any libraries that need to be referenced by the **Custom Aggregate Function**. The DLLs must be present in the `bin` folder of the Exago BI Web Application, as well as any **Scheduler**`bin` folders, and the **Web Service API**, if applicable.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> `System.dll` does not need to be listed as a reference as it is already available.

### Namespaces

A semicolon-separated list of any namespaces that need to be referenced by the **Custom Aggregate Function**.

`WebReports.Api.Custom; WebReports.Api.Common;` will be added automatically as they are required.

### Code Editor

The code editor contains the program code for the **Custom Aggregate Function**. Unlike **Custom Functions**, the program code for **Custom Aggregate Functions** accommodates a full class definition.

A **Custom Aggregate Function** must contain at most one class that implements the [`ICustomAggregator`](#ICustomA) interface. The code may include more than one class definition, but no more than one class should implement `ICustomAggregator`.

Depending on which language chosen, the code editor will pre-fill with a code stub as a general starting suggestion. This stub is an empty class which implements the `ICustomAggregator` interface. Examples of both C# and VB stubs are shown below.

```
public class MyCustomAggregator : ICustomAggregator
{
	public void AddValue(SessionInfo sessionInfo, object value, params object[] args)
	{
		
	}

	public object Result(SessionInfo sessionInfo)
	{
		
	}
}
```

[Copy](javascript:void(0);)

ICustomAggregator VB.NET Code Stub

```
1
2
3
4
5
6
7
8
9
10
PublicClass MyCustomAggregator  
    Inherits ICustomAggregator  
  
    PublicOverridesSub AddValue(ByVal sessionInfo As SessionInfo, ByVal value AsObject, ParamArray args AsObject())  
    EndSub  
  
    PublicOverridesFunction Result(ByVal sessionInfo As SessionInfo) AsObject  
    EndFunction  
EndClass
```

```
Public Class MyCustomAggregator
    Inherits ICustomAggregator

    Public Overrides Sub AddValue(ByVal sessionInfo As SessionInfo, ByVal value As Object, ParamArray args As Object())
    End Sub

    Public Overrides Function Result(ByVal sessionInfo As SessionInfo) As Object
    End Function
End Class
```

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> To use a .NET Assembly for custom aggregate functions, first add it to the applicable bin folders. Then add the assembly as a reference in the Code Editor.

During report execution, the conditions under which Exago BI will call `AddValue` change depending on what is passed to the **Custom Aggregate Function**’s *dataToAggregate* argument. This mirrors the behavior of the built-in [aggregate functions](https://devnet.logianalytics.com/hc/en-us/articles/5281614243735-Aggregate-Functions#Aggregat):

* If a **data field** is passed, and the function’s *recordLevel* argument is *false*, `AddValue` is called when the key of the data field’s data object in the current record is different from that of the previous record. If *recordLevel* is *true*, `AddValue` is called for every record.
* If a **parameter** is passed, `AddValue` is called for every record.
* If a **formula** or cell reference is passed, `AddValue` is called for every record.

`Result` is called when the current break section has terminated. The aggregation result should be returned here. An explanation of when section processing ends is below in the following paragraphs.

When this **Custom Aggregate Function** is used on a report, Exago BI instantiates a new instance of the class implementing `ICustomAggregator` once at the beginning of report execution, and again every time the section that the **Custom Aggregate Function** appears in breaks. This means that `ICustomAggregator` implementations will only aggregate within whichever section iteration is currently being processed, and aggregation starts over at the beginning of each new section.

A section breaks when its corresponding sorting entity’s unique key changes. For example, consider a report with Products organized into Category groups. To know when a new product Category starts and the previous Category ends (and thus when to display the appropriate section headers/footers and to perform aggregation), Exago BI searches for the unique key of the Category entity to switch to a new value, this is a section break.

If the custom aggregate function is in a:

* **Detail** section, a new `ICustomAggregator` is instantiated once before the first record is processed, then again before every other record is processed.
* **Group Header**, a new `ICustomAggregator` is instantiated once before the first record is processed, then again after every other Group Header with the same group break is processed.
* **Report Footer**, a new `ICustomAggregator` is instantiated only once, before the first record is processed.

Click the **Test Execution ![✓](https://devnet.logianalytics.com/hc/article_attachments/5432216091799/checkmark.png)** icon to test the code for errors.

---

## ICustomAggregator Interface

```
public interface ICustomAggregator
{
    void AddValue(SessionInfo sessionInfo, object value, params object[] args);
    object Result(SessionInfo sessionInfo);
}
```

The `ICustomAggregator` interface defines two functions, `AddValue` and `Result`. There must be one and only one class defined in the **Custom Aggregate Function**‘s program code that implements both of these functions.

```
void AddValue(SessionInfo sessionInfo, object value, params object[] args)
```

* `value`: The value to aggregate. The cell data derived from the `dataToAggregate` argument passed to the custom aggregate function is passed here.
* `args`: subsequent arguments passed to the custom aggregate function are made available here. `args[0]` here will be the argument following `dataToAggregate` in the custom aggregate function call.

```
object Result(SessionInfo sessionInfo);
```

Called when the current break group has terminated. The aggregation result should be returned.

---

To complete the creation of the **Custom Aggregate Function**:

2. Click **Apply** or **Okay**. Exago BI checks the code for compilation errors and displays a warning if any are found.
3. If there are no warnings, the **Custom Aggregate Function** is now available for use.

## Editing Custom Aggregate Functions

1. In the **Admin Console**, navigate to **Extensions** > **Aggregate Functions**.
2. Click on the name of the **Aggregate Function** to be edited, then click on the **Edit**![pencil](https://devnet.logianalytics.com/hc/article_attachments/5432227755287/adminopen.png) icon at the top of the main menu.
3. Review the section on [creating **Custom Aggregate Functions**](#Creating) to understand all of the available fields.

## Deleting Custom Aggregate Functions

1. In the **Admin Console**, navigate to **Extensions** > **Aggregate Functions**.
2. Click on the name of the **Aggregate Function** to be deleted, then click on the **Delete**![X](https://devnet.logianalytics.com/hc/article_attachments/5432232296599/admindelete.png) icon at the top of the main menu.

## Examples

* [Custom Aggregate Function: AggConcat()](https://devnet.logianalytics.com/hc/en-us/articles/5281605820567-Custom-Aggregate-Function-AggConcat-)
* [Custom Aggregate Function: AggCountIf()](https://devnet.logianalytics.com/hc/en-us/articles/5281622698391-Custom-Aggregate-Function-AggCountIf-)
* [Custom Aggregate Function: AggDistinctAvg()](https://devnet.logianalytics.com/hc/en-us/articles/5281605909143-Custom-Aggregate-Function-AggDistinctAvg-)
* [Custom Aggregate Function: AggDistinctSum()](https://devnet.logianalytics.com/hc/en-us/articles/5281614473495-Custom-Aggregate-Function-AggDistinctSum-)
* [Custom Aggregate Function: AggSumIf()](https://devnet.logianalytics.com/hc/en-us/articles/5281622824855-Custom-Aggregate-Function-AggSumIf-)
* [Custom Aggregate Function: ArgumentMax()](https://devnet.logianalytics.com/hc/en-us/articles/5281622876567-Custom-Aggregate-Function-ArgumentMax-)
* [Custom Aggregate Function: ArgumentMin()](https://devnet.logianalytics.com/hc/en-us/articles/5281622850327-Custom-Aggregate-Function-ArgumentMin-)

## Additional Resources

* Admin Support Lab — [Custom Aggregate Functions](https://devnet.logianalytics.com/hc/en-us/articles/5281547157527-Custom-Aggregate-Functions) (video)
