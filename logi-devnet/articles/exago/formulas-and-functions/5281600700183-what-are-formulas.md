---
title: "What are formulas?"
id: 5281600700183
section: "Formulas and Functions"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281600700183-What-are-formulas
updated_at: 2022-05-03T22:08:57Z
---

# What are formulas?

# What are formulas?

Formulas allow you to do calculations, parse strings, insert images, and much more. Formulas are the composition of functions, parameters, Data Fields, and references to other cells.

## Functions

A function takes zero or more inputs, called arguments, and returns a value based on some calculation or manipulation of those arguments. For example, a Year() function takes a date as an argument and returns only the year portion of the date. Use the Year() function on a report or on a chart to display or work with only the year portion of a date.

There are many categories of functions to choose from, and the system administrator has the ability to add their own Custom Functions to the system to fill a specific need. Functions can be combined together with other functions and with other operators. Nearly all formulas used in this application will use at least one function.

For a complete list of functions, including description, remarks and examples, refer to the [List of Functions](https://devnet.logianalytics.com/hc/en-us/articles/5281615111575-List-of-Functions).

## Parameters

Parameters are special variables that can be assigned when logging in to the application, or they can be prompted for when executing a report. There are also several built-in parameters.

To use a parameter in a formula, enter its name between `@` signs. Parameters can be used as function arguments or alone in a cell following an `=` sign.

For a list of parameters and their descriptions, see [Formula Editor](https://devnet.logianalytics.com/hc/en-us/articles/5281623158039-Formula-Editor). The system administrator has the ability to create additional parameters.

A special type of parameter called a **dropdown parameter** can be created by the system administrator. These parameters have two values: the **Value**, used by the server for processing and the **Display Value** that appears in cells and is used in formulas. These distinct values can be accessed with `@ParameterName.Value@` and `@Parameter.DisplayValue@` respectively. For more information, contact the system administrator.

### Examples

* `@AssetValue@`
* `@AccountCode.Value@`
* `@Employee.DisplayValue@`

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Parameters are case sensitive (`pageNumber` is not the same as `pagenumber`). Parameter names may not contain the at symbol (`@`).

## Data Fields

To use a Data Field as part of a formula, enter its name between curly braces.

Example: `{Orders.OrdersID}`

## Cell References

To reference another cell’s value, enter the column name with a capital letter and the row number between square brackets. A cell reference can be used in formulas or alone in a cell following an = sign.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Cell references will update if rows or columns are added or deleted; however dragging a cell will not update cell references. This may cause errors in some formulas.

Example: `[A2]`

## Adding Formulas to a Report

This section covers adding formulas to an Advanced Report. However, formulas may also be used on ExpressView and in Dashboards. Refer to [ExpressView: Formula Columns (v2021.1+)](https://devnet.logianalytics.com/hc/en-us/articles/5281612083991-ExpressView-Formula-Columns-v2021-1-) and [Dashboard Designer (v2019.2+)](https://devnet.logianalytics.com/hc/en-us/articles/5281580652951-Dashboard-Designer-v2019-2-) for more information about using formulas in those Report Design environments.

### Formula Editor

1. Click in the cell in which you want the formula to appear.
2. Click the **Formula Editor** ![FormulaLarge.png](https://devnet.logianalytics.com/hc/article_attachments/5432236378775/formulalarge.png) icon in the toolbar.
3. Create the desired formula by sele
4. cting the desired functions and clicking the button or by drag-and-dropping them into the Formula box.  
   ![hvBSrT3K6n.png](https://devnet.logianalytics.com/hc/article_attachments/5432263018519/hvbsrt3k6n.png)
5. Click **Okay**.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> When nesting functions, begin with the outermost function and add them moving inward.

Example: `=TRUNCATE(SQRT(162))` will first find the square root of 162, then remove the numbers after the decimal point returning only the whole number portion. Details of the [Truncate](https://devnet.logianalytics.com/hc/en-us/articles/5281599710103-Arithmetic-and-Geometric-Functions#Truncate) and [Sqrt](https://devnet.logianalytics.com/hc/en-us/articles/5281599710103-Arithmetic-and-Geometric-Functions#Sqrt) functions can be found in their respective topic sections.

### Manual Entry

1. Navigate to the **Report Designer**.
2. Enter the formula into a cell by:
   * clicking in the desired cell and entering the formula into the formula bar just below the toolbar, or ![VWtTZsTIWu.png](https://devnet.logianalytics.com/hc/article_attachments/5432281120535/vwttzstiwu.png)
   * double clicking in the desired cell and directly entering the formula into the cell text box ![LgCbNETv4M.png](https://devnet.logianalytics.com/hc/article_attachments/5432242904087/lgcbnetv4m.png)
3. Press the **Enter** key on the keyboard to save the formula into the cell
