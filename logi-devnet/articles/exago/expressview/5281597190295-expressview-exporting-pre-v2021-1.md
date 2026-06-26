---
title: "ExpressView: Exporting (pre-v2021.1)"
id: 5281597190295
section: "ExpressView"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281597190295-ExpressView-Exporting-pre-v2021-1
updated_at: 2022-05-03T22:09:06Z
---

# ExpressView: Exporting (pre-v2021.1)

# ExpressView: Exporting (*pre-v2021.1*)

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> This topic applies to the ExpressView Designer in *pre-v2021.1*. For *v2021.1+*, refer to [ExpressView: Introduction (v2021.1+)](https://devnet.logianalytics.com/hc/en-us/articles/5281589443095-ExpressView-Introduction-v2021-1-)

An **ExpressView** can be exported either as a **file** or an **Advanced Report**. A copy of the ExpressView is used to export to an Advanced Report. This means that the original ExpressView remains available and the new Advanced Report can be edited independently of it.

## Export to Advanced Report

ExpressView is a great starting point to quickly add fields to a report, before delving into some of the more advanced reporting capabilities. The ExpressView format is not compatible with the Report Designer, but you can export it to an Advanced Report and edit the copy.

To export an ExpressView to an Advanced Report:

1. Click the **Settings ![SettingsMenu.png](https://devnet.logianalytics.com/hc/article_attachments/5432122354839/settingsmenu.png)**icon at the top of pane on the right side of the screen.
2. Click the **Create Advanced Report** header to open it.
3. Enter a name for the report and select a folder where it will be stored.
4. Click **Create Advanced Report** button.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Beginning in *v2018.2*, Advanced Reports converted from ExpressViews will retain reprinting of group headers by default if detail section spills to the next page.

![evtoadvconvertreprintheaders.png](https://devnet.logianalytics.com/hc/article_attachments/5432223559703/evtoadvconvertreprintheaders.png)

## Export to File

If you choose to save an ExpressView as a file, it be exported as *PDF*, *RTF*, *CSV*, or *Excel*. Each format has some advantages and disadvantages.

* **PDF** is closest to the look of the ExpressView, and is suitable for printing and emailing. But if there is a large amount of data, you may have too many pages, or too large a file size.
* **RTF** retains the basic look of the ExpressView, and can be opened in a word processor for any additional editing. But it may look different depending on the program it is viewed with, and it is not suitable for viewing large amounts of data.
* **CSV** retains only the data, and none of the look of the ExpressView. It is best used if you need to process a large amount of data in an accounting or analysis program.
* **Excel** retains the data, visualization, and optionally, some styling. It is a good hybrid format if you have a lot of data, but you still need it in a visually presentable form.

### Export Settings

You can make some customizations to the appearance that the exported files will take. With the Settings page open, click the **Export Settings** tab to see the available options:

* **Page Options** affect the size which *PDF*, *RTF* and *Excel* exports will show on a screen and on print.
* **General Options** allow you to restrict available export types, and choose a default type.
* **Other Options**:
  + **Include Setup Info**: Choose whether to include some information about the fields, sorts, and filters in the body of the file.
  + **Use Group Color Styling**: Choose whether to include the group header coloring in the output file.
  + **‘No Data Qualified’ Mode**: If the ExpressView returns no data, choose whether to render an empty file, or show a user message instead.
  + **Flatten Groups in Excel and CSV**: For Excel or CSV files, choose whether to automatically ungroup, or “flatten” all group columns into data columns. This may make the output more suitable for data analysis.
  + **Keep Cell Styling in Excel**: For Excel files, choose whether to show styling, such as font and row shading, or to show only the bare data.
