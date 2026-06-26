---
title: "Analysis Grid - Exporting Data"
id: 4419715063959
section: "Use Dashboards & Visuals - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715063959-Analysis-Grid-Exporting-Data
updated_at: 2022-07-17T02:25:20Z
---

# Analysis Grid - Exporting Data

# Analysis Grid - Exporting Data

Analysis Grid tables include three export functions, controlled by the **export** icon:

![](https://devnet.logianalytics.com/hc/article_attachments/7522880923671/usingag_25.png)

Depending on your application's configuration, you may see some, all, or none of the Export options shown above. They allow you to export the table's data, as follows:

**Excel** - The data is exported into an .xlsx or .xls file, as raw data. The
file can be viewed in Excel (if installed on your computer) or can be
saved to your file system. Table column headers are exported into
the first row of the Excel worksheet, as shown above, and numbers are exported as text. ![](https://devnet.logianalytics.com/hc/article_attachments/7522745474327/_newplus.jpg) New for 14.2 Unless however, if your application has been configured for it, the report title and filter information display in the first row. Depending on your application's configuration,
the data may be formatted and specific worksheet column widths may be set.

![](https://devnet.logianalytics.com/hc/article_attachments/7522856133783/usingag_26.png)

**CSV** - The data is exported into a .csv file, as raw data. The
file can be viewed in Notepad (or any text editor) and in Excel (if
installed on your computer) or can be saved to your file system.
Table column headers are exported into the first row. ![](https://devnet.logianalytics.com/hc/article_attachments/7522745474327/_newplus.jpg) New for 14.2 Unless however, if your application has been configured for it, the report title and filter information display in the first row. All fields are
enclosed in double-quotes and separated by commas.

![](https://devnet.logianalytics.com/hc/article_attachments/7522880937879/usingag_27.png)


**PDF** - An image of the table is exported into a temporary .pdf
file. This file can be viewed in your browser using the Adobe Acrobat
plug-in, similar plug-ins, or, in some cases, native browser technology.
Viewers usually let you save the export as a file, if desired, or print
it. Table headers will be displayed at the top of each PDF page. ![](https://devnet.logianalytics.com/hc/article_attachments/7522745474327/_newplus.jpg) New for 14.2 Unless however, if your application has been configured for it, the report title and filter information display at the top of the page.



![](https://devnet.logianalytics.com/hc/article_attachments/7522864211863/usingag_28.png)

## Export Row Limit

When working with very large data sets, exports may not be practical.
To prevent unacceptably long exports, your application may have been configured with a limit on the number of rows that can be exported. If the number of rows in your Table (across all pages) exceeds this limit, the export controls will be disabled. If this is the case, you may be able to reduce the number of rows in the Table and re-enabled the export feature
by adding one or more Filters on the data.
