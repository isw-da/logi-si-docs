---
title: "ExpressView: Formula Columns (pre-v2021.1)"
id: 5281581864471
section: "ExpressView"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281581864471-ExpressView-Formula-Columns-pre-v2021-1
updated_at: 2022-05-03T22:09:05Z
---

# ExpressView: Formula Columns (pre-v2021.1)

# ExpressView: Formula Columns (*pre-v2021.1*)

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> This topic applies to the ExpressView Designer in *pre-v2021.1*. For *v2021.1+*, refer to [ExpressView: Introduction (v2021.1+)](https://devnet.logianalytics.com/hc/en-us/articles/5281589443095-ExpressView-Introduction-v2021-1-)

**Formulas** can be used to create custom data columns in ExpressView. Formulas are calculated once per each row, based on the other data values in that row. For each row calculation, a formula value is returned for that row, which populate a new column of data. You can use these columns just like any others – format the data, add to a visualization, or group based on formula columns. They are treated the same as data columns.

To add a formula column to an ExpressView, open the **![MainLeftPaneDataFieldsSelected.png](https://devnet.logianalytics.com/hc/article_attachments/5432222814999/mainleftpanedatafieldsselected.png)****Data Pane** then click **+ Add Formula** at the top of the pane. A blank column will be added to the ExpressView, and the **Formula Builder**will open.

In the right pane, the **Formula** section of the **Selected Cell** ![SelectedCellMenu.png](https://devnet.logianalytics.com/hc/article_attachments/5432314102935/selectedcellmenu.png) page shows the available built-in functions and parameters. Hover over a function to see its description and an example of how to use it. To add a function or parameter to the formula, drag it from the Formula page to the Formula Builder window, type its name into the Formula Builder, or double-click the name of the function while the formula editor dialog is open. You can use the **Search** field in the to filter the functions by name.

![formulaeditor.png](https://devnet.logianalytics.com/hc/article_attachments/5432315971991/formulaeditor.png)

Formula editor dialog

To add a data field to the formula, either:

* drag it from the Data Pane to the Formula Builder window
* type its name into the Formula Builder
* double-click the field name while the Formula Builder is open

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Double-clicking the field names will place the fields wherever the cursor is in the formula editor at that time. Double-clicking enabled in *v2018.2* and later.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
>
> To use a data field, function, or parameter as a function argument, drag it to the argument placeholder until the placeholder turns blue. Or click the placeholder and type the name of the desired argument.

![screen.expressview_drag_field_to_formula.png](https://devnet.logianalytics.com/hc/article_attachments/5432292678295/screen.expressview_drag_field_to_formula.png)  

Dragging a field to a function argument

Typing in the Formula Builder shows a list of functions, parameters, and data fields that match the text. Click on an item, or use the up and down arrow keys, to highlight an item and see its description. To add the selected item to the formula, press the **Enter** key.

A special type of parameter called a **dropdown parameter** can be created by the system administrator. These parameters have two values: the **Value**, used by the server for processing and the **Display Value** that appears in cells and is used in formulas. These distinct values can be accessed with `@ParameterName.Value@` and `@Parameter.DisplayValue@` respectively. For more information, contact the system administrator.

When you are finished, click the **Apply Changes ![custom.FormulaCheckmark.png](https://devnet.logianalytics.com/hc/article_attachments/5432292711831/custom.formulacheckmark.png)**icon at the top of the of the Formula Builder to save the formula.

To edit an existing formula column, click Selected Cell ![SelectedCellMenu.png](https://devnet.logianalytics.com/hc/article_attachments/5432314102935/selectedcellmenu.png), open the Formula tab, then click the column to reopen the Formula Builder.
