---
title: "ExpressView: Formula Columns (v2021.1+)"
id: 5281612083991
section: "ExpressView"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281612083991-ExpressView-Formula-Columns-v2021-1
updated_at: 2022-05-03T22:09:04Z
---

# ExpressView: Formula Columns (v2021.1+)

# ExpressView: Formula Columns (*v2021.1+*)

ExpressViews are an easy way to display and visualize data. Custom **formula columns** extend the pre-defined data.

In addition to using the data fields that are available in the Data Objects Pane, formulas may be added as custom **formula columns**. Formulas may contain **data objects**, **parameters** and **functions**.

Just like standard columns, a formula column may be either a detail field or group, and may be included in visualizations, formatted, sorted and filtered.

To add a formula column to an ExpressView:

1. In the Data Objects Pane, click the **+ Add Formula** link at the top. A new column will be added to the report and the **Formula Builder** will appear.
   ![01taZ5GgXR.png](https://devnet.logianalytics.com/hc/article_attachments/5432222588695/01taz5ggxr.png)

   Formula Builder with a formula that returns the year portion of a date detail field.
2. The **Selected Section** tab of the **Properties Pane** will open with the available functions that may be used to build a formula.
   1. Either **Search** for a function, or expand the function categories to browse the available functions:
      1. *Arithmetic* — basic mathematical functions, as well as number field manipulation like truncation and rounding.
      2. *Database* — used for determining the type of information contained in a cell. Helpful for error and sanity checks.
      3. *Date* — can be used to do calculations and formatting on date and time values.
      4. *Financial* — common methods for monetary calculations such as interest and depreciation.
      5. *Formatting* — applies bold, underline, or italic formatting to the input.
      6. *Logical* — can be used to handle conditional information.
      7. *Other* — miscellaneous functions
      8. *String* — commonly used for interpreting and manipulating text fields.
      9. *Parameters* — a listing of the available system parameters that may be used in the formula
   2. Hover the mouse over a function name to see a description of it and how to use it.  
      ![VrVgZQkpzn.png](https://devnet.logianalytics.com/hc/article_attachments/5432295230615/vrvgzqkpzn.png)
   3. Either drag-and-drop the function name, or double-click the function name to add it to the Formula Builder.
3. Click the **Apply Changes** ![01taZ5GgXR2.png](https://devnet.logianalytics.com/hc/article_attachments/5432309658007/01taz5ggxr2.png) icon to apply the formula to the column, or **Discard Changes** ![01taZ5GgXR3.png](https://devnet.logianalytics.com/hc/article_attachments/5432275800471/01taz5ggxr3.png) to cancel.

The formula column is now added to the ExpressView, and can be manipulated just as any other column on the report.

## Formula Components

Formulas may contain any combination of **data objects**, **parameters** and **functions**.

### Data Objects

To add a field to the formula, either:

* drag it from the Data Objects Pane to the Formula Builder
* double-click the field name in the Data Objects Pane while the Formula Builder is open
* type its name into the Formula Builder

Data objects must always be enclosed in curly braces. For example, `{Orders.OrderId}`

![n6AnIIw5gR.png](https://devnet.logianalytics.com/hc/article_attachments/5432275826839/n6aniiw5gr.png)

Formula Builder with a single data object in it

### Parameters

Parameters are system-wide variables that may be referenced in formulas. To add a parameter to a formula:

1. Type `@` into the Formula Builder, and a list of available parameters will appear.
   ![nn5xZfl4TB.png](https://devnet.logianalytics.com/hc/article_attachments/5432295332119/nn5xzfl4tb.png)
2. Either double-click the parameter in the list, or use the arrow keys to highlight the desired parameter and then press Enter on the keyboard.

Parameters are case-sensitive and must always be enclosed by @ symbols. For example, `@userId@`

![kCKqNm5T1V.png](https://devnet.logianalytics.com/hc/article_attachments/5432295370647/kckqnm5t1v.png)

Formula Builder with a single parameter in it

A special type of parameter called a **dropdown parameter** can be created by the system administrator. These parameters have two values: the **Value**, used by the server for processing and the **Display Value** that appears in cells and is used in formulas. These distinct values can be accessed with `@ParameterName.Value@` and `@Parameter.DisplayValue@` respectively. For more information, consult with the system administrator.

### Functions

Functions are mechanisms built-in to the application that take an input and return an output. For example, there is a square root function that given an input number will return the square root of the number. For example, `Sqrt(4)` returns `2`.

Many functions can be used together in a formula.

A list of all available functions and operators along with descriptions and examples of how to use them can be found in the [List of Functions](https://devnet.logianalytics.com/hc/en-us/articles/5281615111575-List-of-Functions).

Some examples of functions in formulas:

```
{Employees.LastName} & ", " & {Employees.FirstName}
```

Concatenate employee’s last name and first name in a single column, using two fields

```
Year({Orders.OrderDate})
```

Get only the year portion of an order date, from the `Orders.OrderDate` field

```
If(@userId@ = "Admin", {Manufacturers.name}, {Manufacturers.manufacturer_id})
```

Using a combination of parameters, functions and data objects to display the name of a manufacturer in a column to the administrator, or an obfuscated ID number to all other users

## Quick Functions

**Quick Functions** are pre-defined calculations or operators that transform the fields in either detail fields or group columns. For example, the *Month Name* quick function applied to a date column will transform the column to only the name of the month of that date. Quick Functions can be used in lieu of building a full formula column, work in conjunction with a formula, or work on a standard detail field or group column by themselves.

There are several built-in **Quick Functions**, and the system administrator has the ability to add or remove functions from the list:

* *Day of Month* — Gets the day of the month from a date, as a one or two digit number
* *Day of Week* — Gets the name of the weekday of a date
* *Week of Year* — Gets the ordered number of the week in the year that a date occurs on, from 1 to 53
* *Month Name* — Returns the name of the month
* *Year, Month Name* — Returns the year and month name of a date. For example, `2020 - September`
* *Quarter* — Returns the fiscal quarter of a date in the typical Q1, …, Q4 style
* *Year, Quarter* — Returns the year and quarter name of a date. For example, `2020 - Q3`
* *Year* — Gets the year component of a date, as a four digit number
* *None* — remove the Quick Function from the column and return it to a standard detail field or group column

With a Quick Function on a column, it may be sorted, filtered, aggregated and included in a chart just as any other column type.

Behind the scenes, a Quick Function works like a preset formula column. Quick functions have a **display formula** and a **sort formula**. The **display formula** is applied to the data as it is displayed in the ExpressView Designer, in exported files and it is the value that is compared when filters are applied to a column. The **sort formula** is activated when a sort is applied to a column. This allows a column to be sorted on a different quantity than the display formula. For example, the *Day of Week* quick function will display names of weekdays, but will sort the column in chronological order instead of alphabetical order (that is *Sunday*, *Monday*, *Tuesday*, *Wednesday*, *Thursday*, *Friday*, *Saturday*).

![O8cgJ99eJP.png](https://devnet.logianalytics.com/hc/article_attachments/5432315712279/o8cgj99ejp.png)

An ExpressView with one group column, one detail column on the OrderDate field, and a detail field with the Day of Week quick function applied to OrderDate as it appears in exported Excel file

When an ExpressView is exported to an Advanced Report, the quick functions will be broken down into their component **display** and **sort** **formulas**. The **display formula** will appear on the report, and if an applicable sort had been added to the ExpressView, the **sort formula** will be added to the end of the Advanced Reports sort list.

![O30phOV4VG.png](https://devnet.logianalytics.com/hc/article_attachments/5432310098711/o30phov4vg.png)

The DayOfWeekName Display Function appears in column B of the Advanced Report Designer

![xFNqSV1R3K.png](https://devnet.logianalytics.com/hc/article_attachments/5432222758423/xfnqsv1r3k.png)

The DayOfWeekNumber Sort Function is added to the end of the Advanced Report’s Sorts list

### Using a Quick Function

1. Open the **Column Menu** by either clicking on the **Column Menu**![MoreOptions_Black.png](https://devnet.logianalytics.com/hc/article_attachments/5432306248471/moreoptions_black.png) icon or right-clicking on the column.
2. Point to ![MenuFormula.png](https://devnet.logianalytics.com/hc/article_attachments/5432312815767/menuformula.png)**Quick Functions**.  
   > ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
   >
   > The **Quick Functions** menu item will only be available if there are quick functions configured in the system for the data type in the chosen column. For example, there must be Quick Functions that work on date columns if the chosen column contains a date.
3. Click the name of the desired Quick Function to add to the column.

The name of the Quick Function will appear in the column header.

![Vj7311cbb8.png](https://devnet.logianalytics.com/hc/article_attachments/5432310240791/vj7311cbb8.png)

The Day of Month Quick Function has been applied to this Group column on Orders.OrderDate

When a Quick Function is applied to a formula column, the quick function will apply to the data after the formula. For example, the formula `DateAdd("d",3,{Orders.OrderDate})` combined with the **Day of Month** Quick Function will display the name of the day of the week three days later than the `OrderDate`. If the order was placed on *Tuesday*, the column will display *Friday*.

### Removing a Quick Function

Follow the steps in Using a Quick Function above. At step 3, choose *None*.

Quick Functions will also be removed from a formula column if the formula is changed in a way that the formula returns a different data type than the data type the Quick Function applies to. For example, if a formula that returns a date is changed to one that returns a string, the Quick Function will be removed from the column.
