---
title: "Chained Reports"
id: 5281546622615
section: "Overview"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281546622615-Chained-Reports
updated_at: 2022-05-03T22:09:27Z
---

# Chained Reports

# Chained Reports

**Chained Reports** combine multiple reports into a single multi-page document. They are a convenient way to bundle related reports into a format suitable for printing or sending to a mailing list.

For example, you could combine a report on total monthly sales over time, product sales for the month, and a report highlighting this month’s top selling employee. And you could schedule it to be emailed regularly at the end of every month.

A benefit of Chained Reports is that unless you want to use collation (see [Collating Reports](#Collatin)), they do not need to have anything in common. You could chain entirely disparate reports together without a problem.

**Dashboards** are also exported in the form of Chained Reports in which each report or visualization tile is displayed on a single page in the report. See [Exporting Dashboards (v2019.2+)](https://devnet.logianalytics.com/hc/en-us/articles/5281619023767-Exporting-Dashboards-v2019-2-) for directions on how to export a Dashboard as a Chained Report.

## Creating a Chained Report

1. Click the **Create New Report ![MainLeftPaneNewReport.png](https://devnet.logianalytics.com/hc/article_attachments/5432314432023/mainleftpanenewreport.png)** icon in the Main Menu and select ![ThumbnailChainedReport.png](https://devnet.logianalytics.com/hc/article_attachments/5432434895255/thumbnailchainedreport.png)**Chained Report**.
2. On the **Name** tab, enter a name for the report and select a folder to save it to. It does not have to be in the same folder as the reports that it contains. Optionally add description text to the **Enter a description for the report** field.  
   > ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
   >
   > A report name may contain all characters except for the following:  
   >  `/ : * ? " < > |`
3. Advance to the **Reports** tab, add the reports to include in the Chained Report. Supported report types are **Advanced Reports**, **Express Reports**, **CrossTab Reports** and **ExpressView**.The order of the reports in the list is the order they will appear in the output. Click and drag a report or use the **Move Item** **Up**![^](https://devnet.logianalytics.com/hc/article_attachments/5432225168663/movegridrowup.png) or **Move Item** **Down**![V](https://devnet.logianalytics.com/hc/article_attachments/5432338912791/movegridrowdown.png) icons to move a report up or down in the list respectively. Click the **Delete**![X](https://devnet.logianalytics.com/hc/article_attachments/5432124748951/deleteitem.png) icon to remove a report from the list. Click the **Edit Report Options ![Edit.png](https://devnet.logianalytics.com/hc/article_attachments/5432185311127/edit.png)** icon to set options for handling prompting filters and parameters on the report.
   * **Report Filter Prompt** — the filter field of this particular filter
   * **Report Parameter Prompt** — the parameter name
   * **Action** — choose how to obtain a value for the filter or parameter
     + *Common Prompt* (default) — all reports which contain this filter field or parameter will use the specified value. In the **Data (Prompt Text or Value)** field, enter the text to prompt the user for a value. For filters by default, the prompt text will be *Specify value for {fieldname}* where {fieldname} represents the name of the common filter field.  
       > ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
       >
       > Filter dependency is not honored when executing a Chained Report in this mode.
     + *Report Prompt* — only this report will use the specified value. In the **Data (Prompt Text or Value)** field, enter the text to prompt the user for a value. For filters by default, the prompt text will be the filter title from the corresponding report. Changing the filter text in this dialog only changes it for the Chained Report, not for the corresponding report itself.
     + *Assign Value* — the Chained Report will not prompt for a value for this filter or parameter. In the **Data (Prompt Text or Value)** field, enter the value to use. For filters by default, if a value is provided in the corresponding report its value will appear here. Changing the value in this dialog only changes it for the Chained Report, not for the corresponding report itself.  
       > ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
       >
       > Values for prompting filters and parameters cannot be set when scheduling a Chained Report. If a Chained Report is intended to be scheduled, use the *Assign Value* option to specify values.
4. Advance to the **Options** tab to set certain report options
   * **Default Export Type** — choose the file type to which the Chained Report will export by default. Available types are limited by report export restrictions, and by the **Allowed Export Types** option. HTML is not supported. Choose *Default* to use the environment’s default export type.
   * **Allowed Export Types** — choose which file types the Chained Report is allowed to export to. At least one type must be selected.  
     > ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
     >
     > If one of the component reports in the chain cannot export to a certain file type, then the Chained Report cannot export to that type. All of the reports must share at least one export type, or else the Chained Report will have no compatible type to run as. Supported types are *PDF*, *RTF*, *CSV*, and *XLS* (Excel).
   * **No Data Qualified Action** — choose what to display if there is no data to display when the report is executed. Select from:
     + *Show Placeholder* — show the report without any data in it
     + *Skip Report* — show nothing, and move on to the next report in the chain
   * **Collate Reports on** — check to collate the Chained Report. This option is enabled only when all of the reports in the chain share at least one common sort field. The sort field must be a standard column type without a formula. See [Collating Reports](#Collatin).
   * **Page break after each report** — choose whether to start a new page after every report. This only affects PDF and RTF files.  
     > ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
     >
     > When building a chained report with the **Page break after each report** checkbox unchecked, consider placing the title of the component reports in a **Report Header** section instead of a **Page Header** section. Consider the examples in Table A below.
5. Click **Save and Close** to save the report and close the wizard.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Reports with document templates can be added to a Chained Report. The Chained Report must be exported to the same file type as the template. Multiple templates of the same file type can be chained together, with the exception of Microsoft Word based templates. See [Advanced Reports: Templates](https://devnet.logianalytics.com/hc/en-us/articles/5281564145303-Advanced-Reports-Templates).

Table A — Best Practice for Report Titles when **Page break after each report** is unchecked

| Report Title in Page Header Section | Report Title in Report Header Section |
| --- | --- |
| rGdO8s0Jpd.png | 4KYtPDqb1A.png |

## Collating Reports

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> Collation is recommended for advanced users as it can have potential performance implications if used incorrectly. Review [Best Practices](#Best).

Collation breaks up the reports in the **Chained Report** by a chosen sort field, and then groups together the reports by each instance of that sort. Essentially, this turns a sort field into a common grouping for the reports, working in much the same way a group section would. This can allow you to use individual reports as pieces in a composite report.

Some common uses for collation include:

* Grouping disparate reports by order number, or employee number, or something else in common
* Combining mostly identical reports, only with different filters or joins, into a composite report
* Making a composite report with multiples of a feature which normal reports can only have one of, such as a detail section

### Execution of Collated Reports

1. Report 1, filtered by group 1
2. Report 2, filtered by group 1
3. Report 1, filtered by group 2
4. Report 2, filtered by group 2
5. Report 1, filtered by group 3
6. Report 2, filtered by group 3

…and so on.

To accomplish the collation, the application will run each report for each filtered group. An non-collated chained report containing two reports will only execute those two reports. A collated chained report with the same two reports sorted on a field with 100 values will execute 200 individual reports.

The system administrator can limit the number of individual report executions. If a collated chained report requires more executions than this limit, the entire chained report will stop and display an error message like this:

![Historial Employee Data was not run because it would cause 6 report executions (2 reports multiplied by 3 sort fields in the chain), which exceeds the set maximum of 4. To run this collated chained report, try reducing the number of reports or sorts in the chain.](https://devnet.logianalytics.com/hc/article_attachments/5432479033623/taptgkvxbk.png)

If this error message appears, change how the report collates with the recommendations in the [Best Practices](#Best).

Consider the example reports below. Report 1 lists all salespeople in the company and Report 2 lists the orders placed by that salesperson.

Table B — Non-collated Report

| Report 1 | Report 2 |
| --- | --- |
| firefox_x95pLXnTXw.png | x5x13cB3SQ.png |
| Chained Output | |
| When this chain is executed, only two reports run: one for each of the reports in the chain. ZwqKfeqPeX.png This yields a final output file that resembles the figure below: iuRYEIA69H.png | |

When those same two reports are collated by checking the **Collate reports on** checkbox, and choosing *Employees.LastName* as the field,

Table C — Collated Report

| Report 1 | Report 2 |
| --- | --- |
| firefox_x95pLXnTXw.png | x5x13cB3SQ.png |
| Chained Output | |
| When this chain is run, since there are two reports in the chain and nine employee last names, there are eighteen reports to execute: two for each of the nine employees. g9pmtdwpI5.png This yields a final output file that resembles the figure below. Now, instead of showing one complete report after the other, the two reports are **collated** by the *Employee’s Last Name*. AFxIm1tqLm.png | |

### Best Practices

Since **collating** a chained report can greatly increase the number of component reports to execute, there are a few considerations to alleviate the load on the system:

* Minimize the number of reports in the chain
* Minimize the number of data points in the sort field (for example reduce the number of employees) with a filter
