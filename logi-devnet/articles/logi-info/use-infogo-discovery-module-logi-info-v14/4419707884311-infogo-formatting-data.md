---
title: "InfoGo - Formatting Data"
id: 4419707884311
section: "Use InfoGo/Discovery Module - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707884311-InfoGo-Formatting-Data
updated_at: 2022-07-17T02:23:18Z
---

# InfoGo - Formatting Data

# InfoGo - Formatting Data

You can format the appearance of the data in the Table by clicking a **table column header** and selecting **Format** and then the desired option:

![](https://devnet.logianalytics.com/hc/article_attachments/7522751660695/image-20220510-152830_497x741.png)

These options allow you to apply, or remove, a variety of standard
data formats. More information about these formats is available in [Format Data](https://devnet.logianalytics.com/hc/en-us/articles/4419722930327-Format-Data).

The Percent of Total format applies a calculation that determines each data value's percentage of the summed values and displays it as a percent.

![](https://devnet.logianalytics.com/hc/article_attachments/7522745474327/_newplus.jpg) New for 14.2 When utilizing the Percent or Percent of Total formatting options you can further customize the decimal place by selecting **Percent Decimal Places**:

![](https://devnet.logianalytics.com/hc/article_attachments/7522751680407/image-20220308-040005.png)

Both a number string value and an empty value is considered valid input. If the value is not a number, it will be ignored. An "empty" value will remove the setting, and decimal places will return to the default value, zero or two.

Enter the desired decimal place and select **OK**:

![](https://devnet.logianalytics.com/hc/article_attachments/7522766053911/image-20220308-040127.png)

![](https://devnet.logianalytics.com/hc/article_attachments/7522774430103/noteicon.jpg) This setting is column-specific, meaning different columns with different percentage values can be customized to display different decimal places.

Two special format options insert visualizations right into the column:

![](https://devnet.logianalytics.com/hc/article_attachments/7522774448023/usinginfogo125_29.png)

Selecting the **Bar Gauges** option will produce a horizontal bar
gauge within the column, as shown above. The actual data value will
appear in a tooltip if you hover your mouse over the gauge. Selecting
the **Cell Colors** option will display the column value using an
imbedded Cell Color Slider, as shown above. You can drag the slider in
the column header to customize the color ranges.

The Cell Colors feature has been changed to allow you to apply conditional colors:

![](https://devnet.logianalytics.com/hc/article_attachments/7522787801751/usinginfogo125_29a.png)

Its previous functionality is now represented by a new Format menu item, Cell Color Slider, as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/7522774487831/screen_shot_2022-01-03_at_8.10.30_pm_524x591.png)

The menu's Cell Colors item displays the pop-up dialog box shown above, where you can select data value ranges and cell background colors. ![](https://devnet.logianalytics.com/hc/article_attachments/7522745474327/_newplus.jpg) New for 14.2 The Values field can be customized to match the boolean format.

![](https://devnet.logianalytics.com/hc/article_attachments/7522745474327/_newplus.jpg) New for 14.1 You can also format conditional colors on the group level by selecting the **Group Level** tab:

![](https://devnet.logianalytics.com/hc/article_attachments/7522751807639/screen_shot_2022-01-03_at_8.10.38_pm_534x692.png)

Previously established grouping is available in the Group drop-down menu. Choose your **Group** and **Aggregate** using the drop-down menus.

Enter a numeric value in the field on the left and assign a color to the Count by entering a Hex code or using the Color Picker:

![](https://devnet.logianalytics.com/hc/article_attachments/7522751834135/screen_shot_2022-01-03_at_8.12.33_pm__1__558x736.png)

Select **OK** to apply your changes.

Your Analysis Grid reflects the conditional colors applied to the cells, like below:

![](https://devnet.logianalytics.com/hc/article_attachments/7522756377367/screen_shot_2022-01-03_at_8.13.08_pm_1011x823.png)

![](https://devnet.logianalytics.com/hc/article_attachments/7522755629847/noteicon.jpg) To utilize this feature you must have an aggregation defined at the group level.
