---
title: "ExpressView: Customizing Appearance (pre-v2021.1)"
id: 5281589042071
section: "ExpressView"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281589042071-ExpressView-Customizing-Appearance-pre-v2021-1
updated_at: 2022-05-03T22:09:07Z
---

# ExpressView: Customizing Appearance (pre-v2021.1)

# ExpressView: Customizing Appearance (*pre-v2021.1*)

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> This topic applies to the ExpressView Designer in *pre-v2021.1*. For *v2021.1+*, refer to [ExpressView: Introduction (v2021.1+)](https://devnet.logianalytics.com/hc/en-us/articles/5281589443095-ExpressView-Introduction-v2021-1-)

**ExpressViews** can be styled in a variety of ways:

* Click the **Formatting and Style ![FormatMenu.png](https://devnet.logianalytics.com/hc/article_attachments/5432316815895/formatmenu.png)**icon in the right pane to make universal report styling changes such as **Theme**.

![formattingpane.png](https://devnet.logianalytics.com/hc/article_attachments/5432318839831/formattingpane.png)

* Click the **Selected Section ![SelectedCellMenu.png](https://devnet.logianalytics.com/hc/article_attachments/5432314102935/selectedcellmenu.png)**icon and choose a section of the report to make formatting changes.
* Right-click a section of the report for interactive editing that includes formatting options and data structuring options such as sorting, grouping, and filtering.

![rightclickhtmlEV.png](https://devnet.logianalytics.com/hc/article_attachments/5432291862935/rightclickhtmlev.png)

## Premade Themes

If there are any available, you can select a premade theme to use for the **ExpressView**, or to use as a baseline for further customization. On the **Formatting** page, click the **Theme** tab. Then select a theme from the **Theme Selector** list:

**Legacy**

This is the default theme.

**Custom**

This option indicates that you are not currently using a premade theme.

Selecting a premade theme overrides any custom styling you have.

![screen.expressview_theme_select.png](https://devnet.logianalytics.com/hc/article_attachments/5432296675095/screen.expressview_theme_select.png)

*Selecting a premade theme*

## Styling Data Cells

Cells, columns, group headers, and group footers can be styled using the **Report Formatting and****Style** pane, the **Selected Section** pane, or by right-clicking sections of the report. Each of the three options is used for different purposes:

* **Universal report styling changes** such as theme, row shading, and group colors are made using the **![FormatMenu.png](https://devnet.logianalytics.com/hc/article_attachments/5432316815895/formatmenu.png)****Report Formatting and Style** pane. See the following two sections for more details on row and group colors.
* The **Selected Section ![SelectedCellMenu.png](https://devnet.logianalytics.com/hc/article_attachments/5432314102935/selectedcellmenu.png)**pane is used to make **data format changes** such as Date or Number format or to create formulas in a column. It can also be used to **style multiple cells or sections at one time** when used with the CTRL key. To use the multi-select feature, click the **Selected Section ![SelectedCellMenu.png](https://devnet.logianalytics.com/hc/article_attachments/5432314102935/selectedcellmenu.png)**icon, hold the CTRL key while clicking all of the desired sections, and then make changes in the right pane.

* **To make styling changes to independent sections**, you can right-click specific areas and use interactive editing or you can click the **Selected Section**![selectedcelliconEV.png](https://devnet.logianalytics.com/hc/article_attachments/5432296690199/selectedcelliconev.png)icon, click the appropriate section, and make changes in the right pane.

### Changing data row colors

The background colors for the data rows can be customized, and you can set the pattern by which the colors alternate. This affects every data section in the **ExpressView**.

To set the background colors:

1. On the **Formatting** page, click the **Row Shading** tab. By default there are two colors which alternate every other row.
2. Choose the number of colors that you want to alternate between:
   * To make all rows the same color, click ![RemoveColor.png](https://devnet.logianalytics.com/hc/article_attachments/5432296718231/removecolor.png) to delete all the colors except one.
   * To make rows alternate between more than two colors, click ![AddItem.png](https://devnet.logianalytics.com/hc/article_attachments/5432277408023/additem.png) to add more colors.
3. Enter a hex value or use the color picker to set each color.

![bCJyooYp35.png](https://devnet.logianalytics.com/hc/article_attachments/5432277431959/bcjyooyp35.png)

*Choosing data row colors*

### Changing group colors

The headers and footers for group columns are prefixed by a different color depending on the level of grouping. These colors can be customized, and you can set the pattern by which the colors alternate. This affects every group header and footer in the **ExpressView**.

To set the group level colors:

1. On the **Formatting** page, click the **Group Colors** tab. By default, nested groups alternate between four colors.
2. Choose the number of colors that you want to alternate between:
   * To make all group levels the same color, click ![AccordionDeleteItem.png](https://devnet.logianalytics.com/hc/article_attachments/5432268623511/accordiondeleteitem.png) to delete all the colors except one.
   * To make group levels alternate between more than four colors, click ![AddItem.png](https://devnet.logianalytics.com/hc/article_attachments/5432277408023/additem.png) to add more colors.
3. Enter a hex value or use the color picker to set each color.

![s3DS3V7NNp.png](https://devnet.logianalytics.com/hc/article_attachments/5432347471639/s3ds3v7nnp.png)

*Choosing radial menu colors*
