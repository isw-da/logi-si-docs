---
title: "Including Reports in the Menu"
id: 4419715452183
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715452183-Including-Reports-in-the-Menu
updated_at: 2022-07-17T02:23:34Z
---

# Including Reports in the Menu

# Including Reports in the Menu

Including a report definition in a menu is very easy: it starts by "tagging" it to be in the menu:

![](https://devnet.logianalytics.com/hc/article_attachments/7522776548631/rptcenter_02.png)

This is done by adding a **ReportCenter Item** element, as shown above, to a report definition.

The actual *text* of the menu item link for a report will be either a) the root element's **Caption** attribute value or, if that's blank, b) the report definition filename (without its file extension). Using the Caption attribute lets you introduce *spaces* in the link text, which can't be included in a definition filename.

You don't have to do anything else and the report will be automatically included in the menu. However, the ReportCenter Item element has the following optional attributes, which can be used to provide additional functionality:

| Attribute | Description |
| --- | --- |
| ReportCenter Allow Schedule | When set to *True*, a clock icon will appear next to menu links for report bookmarks. This icon allows the user to schedule the report to be run and distributed via email. Used when Include Bookmarks attribute (see below) is *True*, and the Logi Scheduler has been installed. Scheduling is only available for report bookmarks, not for reports. Default value: *False* |
| ReportCenter Allowed Export Formats | Specifies the formatting options, *HTML*, *PDF*, and/or *NativeExcel*, that will be available to the user when scheduling report bookmarks for email distribution at runtime. Multiple formats can be specified in a comma-separated list. These options appear in a selection list in the scheduling pop-up panel. Default value: *blank* - provides all three formats. |
| ReportCenter Exclude | Allows the developer to programmatically control the visibility of this menu item, by using tokens in this attribute value which resolve to *True* (Hidden) or *False* (Visible). |
| ReportCenter Export Table ID | Used when bookmarks for reports that contain multiple Data Tables are made available for scheduled distribution. Specifies the element ID of the Data Table to be exported. Information outside of the Data Table, such as headers and footers, will *not* be included in the export. Default value: *blank* - assumes there is only one Data Table. To export the data in an Analysis Grid element, set the value to *dtAnalysisGrid* |
| ReportCenter Folder | Specifies the text for the **menu folder****item** that the current report link will appear under. Creates the folder item if it doesn't exist. Folders can have multiple levels of depth. To create multiple levels, separate each folder name with a the "pipe" ( | ) symbol. For example, to create a "Sales" folder under an "Accounting" folder, enter *Accounting|Sales* Default value: *blank* - no folder |
| ReportCenter Frame ID | Sets the target frame for display of the report when the menu item is clicked. Options include:  *\_blank* - displays report in a new window *\_parent* - displays report in the parent window, useful when the ReportCenter menu is inside an Include Frame. *\_top* - displays the report in the top-most window.  You may also specify an existing Frame ID to re-use the same window for each request. Default value: *blank* for the current browser window |
| ReportCenter Include Bookmarks | Controls the appearance of savedbookmarks for the current report in the ReportCenter Menu. Default value: *False* |
