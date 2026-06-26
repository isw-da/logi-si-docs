---
title: "Grouping on Separate Excel Export Worksheets"
id: 5281582742551
section: "Extensibility"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281582742551-Grouping-on-Separate-Excel-Export-Worksheets
updated_at: 2022-05-03T22:08:59Z
---

# Grouping on Separate Excel Export Worksheets

# Grouping on Separate Excel Export Worksheets

The default behavior when exporting an report to a Microsoft Excel workbook is that all data appears in a single worksheet (tab).

If a report contains Group Sections, an Excel export can optionally create a new worksheet for each new instance of the outermost group.

The name of each worksheet will be the data field on which the group breaks. If the group breaks on a data category, the [Unique Key Field](https://devnet.logianalytics.com/hc/en-us/articles/5281608202519-Data-Objects#Unique) from the Data Object’s configuration will be used to name the worksheet.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This feature only applies to Excel export file outputs. To display groups on different pages in PDF and RTF export file outputs, add a Page Break in the report design. See [Create, Modify, Delete Sections](https://devnet.logianalytics.com/hc/en-us/articles/5281572597527-Advanced-Reports-Sections-v2021-1-#Create,).

## Implementation

The report must contain at least one [**Group Header** section](https://devnet.logianalytics.com/hc/en-us/articles/5281572597527-Advanced-Reports-Sections-v2021-1-#Group). Elements preceding the first group header will appear on the first worksheet as normal. Each time a new group header is reached for the outermost group, including the very first one, the workbook will create a new worksheet with the contents of that group.

There are two ways to enable grouping on separate worksheets. Either:

* Use this .NET API property of the Report class:

  ```
  myReport.GroupsOnSeparateWorksheets = true;
  ```
* Set the following property in the `<main>` section of the report’s XML definition to *True*:

  ```
  <groups_on_separate_worksheets>True</groups_on_separate_worksheets>
  ```

  > ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Critical")
  >
  > Search the XML for this node first, adding it to a report that already has it will break the report and cause errors to appear in the user interface.

## Example

Consider a report that displays summary data of the orders made by each customer of the organization. The report below includes a **Group Header** section that breaks on the sort field `Customers.CompanyName`.

![H7mxAv3EZW.png](https://devnet.logianalytics.com/hc/article_attachments/5432265181975/h7mxav3ezw.png)

### Group On Separate Worksheets Disabled (Default)

If this report is exported to an Excel workbook, the resulting output looks like something like this:

![WF4IoL3mUz.png](https://devnet.logianalytics.com/hc/article_attachments/5432248913943/wf4iol3muz.png)

Note that the entire report, including multiple customer company names (the outermost group header), is displayed on a single tab (worksheet), and that the name of the worksheet is the title of the report: *Orders per Customer*.

### Group On Separate Worksheets Enabled

By enabling the **Group on Separate Worksheets** property on this report, the resulting output looks like something like this:

![QI33ASve11.png](https://devnet.logianalytics.com/hc/article_attachments/5432270959255/qi33asve11.png)

Note that the first worksheet is still named the title of the report, *Orders per Customer* but now there is a new worksheet created each time a new Customer’s Company Name occurs, one worksheet for each customer’s name.
