---
title: "Create  Self Service Reports"
id: 46982018753165
section: "Use Dashboards, Reports  and Visuals in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/46982018753165-Create-Self-Service-Reports
updated_at: 2026-08-26T07:12:53Z
---

# Create  Self Service Reports

# Create Self Service Reports

Generate and manage reports using the self-service reporting capability. Create customized reports using a table visual, adding a report header and footer as needed.

Additionally, you can apply filtering, conditional formatting, and grouping to your data. Apply aggregate functions on different fields to produce the report you need. Export easily as a PDF or Excel (XLSX) file, including all of your customizations.

When you create a report, the size, layout, paper size and orientation for export, as well as conditional formatting and grouping can affect performance. For more information, see [Report Type Performance](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/47077282029965-Self-Service-Report-Microservice#Report).

## Create a Self Service Report

**Note:** In this release, when your admin enables the Enhanced Experience user interface, you will see changes to workflows you may have used in previous releases.

Create a report from any available data source that supports tables. You can apply any [filtering](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701133247245-Apply-Row-Level-Filters), [grouping](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701183802381-Group-and-Ungroup-Table-Data), or [conditional formatting](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701169376269-Using-the-Conditional-Formatting-Sidebar-Tables) as needed. Add a header and footer to provide information and context as needed. After you create a report, you can favorite it, save a copy of it, and easily export it (up to 15 columns of data) as a PDF. Self service reports support up to 10 columns of grouped data.

1. Navigate to the [Reports work area](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/46982003574285-Use-the-Self-Service-Reports-Library).
2. Select **Create Report**. A blank **Untitled report** work area opens. Edit an editable area of the report, or connect a data source using the **Select source** button to open the **Select a Source** modal.

   **Note:** Before or after you select a source, you can edit the title, header, footer, and trademark text of this report.

   ![Select a source to build your report. Search by name or sort by Connection Type. Optionally Enable Groups Header/Footer](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/48417945417485 "Select a Source work area")
3. Select an available source from the options provided in the **Select a Source** modal. Scroll through the options, filter sources by connection type, or use the **Search** feature to find specific sources. After you make your selection, a **Select Columns** modal opens.

   **Note:** Only sources with data that can be presented in a table are shown.

   Optionally, enable the toggle provided to **Enable Groups Header/Footer**.
4. Select one or more columns from your data source to build your report. Scroll through the options or use the **Search** feature to find specific fields.

   ![select columns for a self service report](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/48417945440525 "select columns for a report")

   **Important:** When selecting what data you want to include in your report, keep in mind that larger data sets with more complex conditional formatting can negatively affect performance times. See [Report Type Performance](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/47077282029965-Self-Service-Report-Microservice#Report).

   **Note:** Control the fields used and shown to users for self service reports by adjusting the field visibility in your sources. See [Hide Fields](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701117118477-Hide-Fields).
5. When you have picked all of the columns you wish to include in the report, select **Create Report**. After your report is generated, it displays the report data in an editable widget in the **Untitled report** work area.

   ![use this work area to design your self service report](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/48417965559053 "create your self service report")

   **Important:** When selecting what data you want to include in your report, keep in mind that larger data sets with more complex conditional formatting can negatively affect performance times. See [Report Type Performance](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/47077282029965-Self-Service-Report-Microservice#Report).
6. Name and save your report when you're ready, updating the name, adding a description, and assigning tags as needed.

   You can now edit this report: add and remove columns, [group data](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701183802381-Group-and-Ungroup-Table-Data), sort data, format your data, and apply [conditional formatting](#Conditio).

   Optionally, [edit the header and footer](#The) of this report, or select the **Report Header & Footer** icon to disable the header and footer of this report.

### **The Report Header and** Footer

**Note:** By default, the report header and footer are enabled for all reports. Select the **Report Header & Footer** icon in the reports icon bar to toggle the header and footer sections on and off.

1. Select edit icon in the header or footer area of the report to make changes to it. The selected section expands and opens for editing. Apply formatting as needed. See [Format Self Service Reports](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/46981992392077-Format-Self-Service-Reports).
2. Enter the header or footer text you would like to include, then select the edit icon again to save your changes. The section shrinks and your changes are visible in the report work area.
3. By default, the current date is included in the footer work area, and you can optionally add trademark text, copyright information, or other static information alongside the date.
4. When you are satisfied with your edits, **Save** your changes.

   **Important:** The name of the report, the date of the report, pagination information, and any trademark information you provide are included in all reports, even if the headers and footers are disabled.

### Conditional Formatting

[Conditional formatting](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701183616525-Configure-Conditional-Formatting) increases report generation time significantly. A report with conditional formatting can take from twice as long to significantly longer than an equivalent report without it. Conditional formatting in complex reports exported to PDF format place a higher load on your environment, resulting in a percentage of error rates.

Self service reports support conditional formatting on reports with and without [grouped data](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701183802381-Group-and-Ungroup-Table-Data). You can apply conditional formatting rules as you would for a table visual. See [Configure Conditional Formatting](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701183616525-Configure-Conditional-Formatting).

## Export Your Self Service Report

When your users create self service reports and scheduled service reports, this can induce some load on your environment and the self service microservice. This microservice was added to enhance performance of self service report creation and Excel (XLSX) exports with formatting and conditional formatting for table visuals and reports.

For more information about performance considerations for self service reporting, exports of reports and table visuals, see [Self Service Report Microservice](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/47077282029965-Self-Service-Report-Microservice).

1. After you create and save your report, or make changes to a report and save it, you can access and select the export icon.
2. Select the export icon to open the export menu.
3. Select **PDF** or **Data (XLSX)**. If you select **Data (XLSX)**, your data is prepared and downloads as formatted.

   If you select **PDF**, a preview window displaying the first few rows of entries in your report opens.
4. By default, your PDF report previews with a **Page Size & Orientation** of **US Letter - Portrait**. Use this option, or select from [other available layouts](#Page).

   Depending on the number of columns in your report, as well as page and orientation limitations, you can optionally select the number of columns to include up to a displayed maximum, and adjust the font size up to a displayed maximum.
5. If you like the look of your report, select **Export PDF** to download the report. Select **Cancel** to go back and make changes to your report.

Many factors can influence the amount of time and resources required to generate and export your report. Creating a report that reaches maximum column counts, maximum font size selection, multiple complex conditional formatting rules, in combination with your page size and orientation selections may not generate as expected. We have provided some guidelines to help you provide your users with efficient, balanced report generation. See [Report Type Performance](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/47077282029965-Self-Service-Report-Microservice#Report).

![Use this work area to preview your report before committing to an export](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/48417945491597 "PDF Export Preview")

### Page Size and Orientation

Page size and orientation options include:

* US Letter - Portrait
* US Letter - Landscape
* A4 - Portrait
* A4 - Landscape
* A3 - Portrait
* A3 - Landscape
