> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Self Service Reports

<Note>
  To use self service reports, you will need to enable it in your environment. See [Server-Level Variables](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#server-level-variables).
</Note>

After you have successfully connected to your data stores and configured your data sources, you can immediately start using your data to generate self service reports. Quickly build, edit, and filter reports. Group your data and apply conditional formatting to highlight specific information. Add header and footer information to provide context to the information you're presenting in each report.

A self service report is an easy to create from a data source. Create as many self service reports as you need to share with users add to an SFTP location ([if enabled in your environment](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#server-level-variables)), distribute as a PDF, or [share as a scheduled report](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-schedule#schedule-a-self-service-report-or-dashboard-report).

<h2 id="performance-memory-management-and-scheduling">
  Performance, Memory Management, and Scheduling
</h2>

Self Service Reports are designed to provide flexible and efficient report generation while maintaining optimal system performance. Report complexity directly impacts memory consumption: advanced features and extensive data transformations require additional computational resources.

To ensure the best reporting experience, we recommend careful data selection, mindful use of complex conditional formatting, and awareness of potential memory constraints during large-scale report generation. Layout, paper size and orientation for export, as well as conditional formatting and grouping can affect performance. More complex reports may require additional processing time and resources, so design the reports accordingly. For more information, see [Report Type Performance](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#report-type-performance).

To ensure optimal performance and reliability when scheduling Self-Service Reports, keep in mind that this system is designed to handle multiple concurrent schedules efficiently. However, we recommend you space out schedules to avoid overlaps and potential conflicts. For more information, see [Report Type Performance](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#report-type-performance).

Additionally, there is a limit on the size of emails that can be sent, determined by your SMTP provider that includes both the message body and any attachments. Exceeding this may result in delivery failures due to those restrictions.

Before you begin, make sure that the data sources you want to use have been added and you have privileges to access the sources and create reports.

Before you begin, make sure that the data sources you want to use have been added and you have privileges to access the sources and create reports.

For more information, see:

* [Self Service Report Microservice](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#self-service-report-microservice)
* [Use the Self Service Reports Library](#use-the-self-service-reports-library)
* [Create Self Service Reports](#create-self-service-reports)
* [Format Self Service Reports](#format-self-service-reports)
* [Edit and Delete a Self Service Report](#edit-and-delete-a-self-service-report)
* [Schedule a Self Service Report or Dashboard Report](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-schedule#schedule-a-self-service-report-or-dashboard-report)
* [Scheduled Self Service Reports and Dashboard Report Prerequisites](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-schedule#scheduled-self-service-reports-and-dashboard-report)
* [Use the Report Icon Bars](#use-the-report-icon-bars)

<Note>
  You can bypass the visualization cache and query the underlying data source by selecting the Refresh icon in the [reports icon bar](#use-the-report-icon-bars).
</Note>

<h2 id="create-self-service-reports">
  Create Self Service Reports
</h2>

Generate and manage reports using the self-service reporting capability. Create customized reports using a table visual, adding a report header and footer as needed.

Additionally, you can apply filtering, conditional formatting, and grouping to your data. Apply aggregate functions on different fields to produce the report you need. Export easily as a PDF or Excel (XLSX) file, including all of your customizations.

When you create a report, the size, layout, paper size and orientation for export, as well as conditional formatting and grouping can affect performance. For more information, see [Report Type Performance](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#report-type-performance).

### Create a Self Service Report

<Note>
  In this release, when your admin enables the Enhanced Experience user interface, you will see changes to workflows you may have used in previous releases.
</Note>

Create a report from any available data source that supports tables. You can apply any [filtering](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters#apply-row-level-filters), [grouping](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/rdt#group-and-ungroup-table-data), or [conditional formatting](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/rdt-condt-format-using#using-the-conditional-formatting-sidebar-tables) as needed. Add a header and footer to provide information and context as needed. After you create a report, you can favorite it, save a copy of it, and easily export it (up to 15 columns of data) as a PDF. Self service reports support up to 10 columns of grouped data.

1. Navigate to the [Reports work area](#use-the-self-service-reports-library).

2. Select **Create Report**. A blank **Untitled report** work area opens. Edit an editable area of the report, or connect a data source using the **Select source** button to open the **Select a Source** modal.

   <Note>
     Before or after you select a source, you can edit the title, header, footer, and trademark text of this report.
   </Note>

   <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/reports/sel-src-rpt-26-2.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=902f24f8632b0dc6f3e209a98e134358" alt="Select a source to build your report. Search by name or sort by Connection Type. Optionally Enable Groups Header/Footer" width="498" height="368" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/reports/sel-src-rpt-26-2.png" />

3. Select an available source from the options provided in the **Select a Source** modal. Scroll through the options, filter sources by connection type, or use the **Search** feature to find specific sources. After you make your selection, a **Select Columns** modal opens.

   <Note>
     Only sources with data that can be presented in a table are shown.
   </Note>

   Optionally, enable the toggle provided to **Enable Groups Header/Footer**.

4. Select one or more columns from your data source to build your report. Scroll through the options or use the **Search** feature to find specific fields.

   <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/reports/sel-col-rpt-26-2.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=91dc83e5caf5ee6308dd901289330ae9" alt="select columns for a self service report" width="496" height="559" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/reports/sel-col-rpt-26-2.png" />

   <Warning>
     When selecting what data you want to include in your report, keep in mind that larger data sets with more complex conditional formatting can negatively affect performance times. See [Report Type Performance](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#report-type-performance).
   </Warning>

   <Note>
     Control the fields used and shown to users for self service reports by adjusting the field visibility in your sources. See [Hide Fields](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-fields-tab#hide-fields).
   </Note>

5. When you have picked all of the columns you wish to include in the report, select **Create Report**. After your report is generated, it displays the report data in an editable widget in the **Untitled report** work area.

   <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/ssr/report-unt-26-2.jpg?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=7325c2bc0650a4390f91673ab0d4fc75" alt="use this work area to design your self service report" width="1304" height="675" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/ssr/report-unt-26-2.jpg" />

   <Warning>
     When selecting what data you want to include in your report, keep in mind that larger data sets with more complex conditional formatting can negatively affect performance times. See [Report Type Performance](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#report-type-performance).
   </Warning>

6. Name and save your report when you're ready, updating the name, adding a description, and assigning tags as needed.

   You can now edit this report: add and remove columns, [group data](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/rdt#group-and-ungroup-table-data), sort data, format your data, and apply [conditional formatting](#create-a-self-service-report-conditional-formatting).

   Optionally, [edit the header and footer](#the-report-header-and-footer) of this report, or select the **Report Header & Footer** icon to disable the header and footer of this report.

<h4 id="the-report-header-and-footer">
  **The Report Header and** Footer
</h4>

<Note>
  By default, the report header and footer are enabled for all reports. Select the **Report Header & Footer** icon in the reports icon bar to toggle the header and footer sections on and off.
</Note>

1. Select edit icon in the header or footer area of the report to make changes to it. The selected section expands and opens for editing. Apply formatting as needed. See [Format Self Service Reports](#format-self-service-reports).

2. Enter the header or footer text you would like to include, then select the edit icon again to save your changes. The section shrinks and your changes are visible in the report work area.

3. By default, the current date is included in the footer work area, and you can optionally add trademark text, copyright information, or other static information alongside the date.

4. When you are satisfied with your edits, **Save** your changes.

   <Warning>
     The name of the report, the date of the report, pagination information, and any trademark information you provide are included in all reports, even if the headers and footers are disabled.
   </Warning>

<h4 id="create-a-self-service-report-conditional-formatting">
  Conditional Formatting
</h4>

[Conditional formatting](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/rdt-condt-format-using#configure-conditional-formatting) increases report generation time significantly. A report with conditional formatting can take from twice as long to significantly longer than an equivalent report without it. Conditional formatting in complex reports exported to PDF format place a higher load on your environment, resulting in a percentage of error rates.

Self service reports support conditional formatting on reports with and without [grouped data](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/rdt#group-and-ungroup-table-data). You can apply conditional formatting rules as you would for a table visual. See [Configure Conditional Formatting](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/rdt-condt-format-using#configure-conditional-formatting).

<h3 id="export-your-self-service-report">
  Export Your Self Service Report
</h3>

When your users create self service reports and scheduled service reports, this can induce some load on your environment and the self service microservice. This microservice was added to enhance performance of self service report creation and Excel (XLSX) exports with formatting and conditional formatting for table visuals and reports.

For more information about performance considerations for self service reporting, exports of reports and table visuals, see [Self Service Report Microservice](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#self-service-report-microservice).

1. After you create and save your report, or make changes to a report and save it, you can access and select the export icon.

2. Select the export icon to open the export menu.

3. Select **PDF** or **Data (XLSX)**. If you select **Data (XLSX)**, your data is prepared and downloads as formatted.

   If you select **PDF**, a preview window displaying the first few rows of entries in your report opens.

4. By default, your PDF report previews with a **Page Size & Orientation** of **US Letter - Portrait**. Use this option, or select from [other available layouts](#page-size-and-orientation).

   Depending on the number of columns in your report, as well as page and orientation limitations, you can optionally select the number of columns to include up to a displayed maximum, and adjust the font size up to a displayed maximum.

5. If you like the look of your report, select **Export PDF** to download the report. Select **Cancel** to go back and make changes to your report.

Many factors can influence the amount of time and resources required to generate and export your report. Creating a report that reaches maximum column counts, maximum font size selection, multiple complex conditional formatting rules, in combination with your page size and orientation selections may not generate as expected. We have provided some guidelines to help you provide your users with efficient, balanced report generation. See [Report Type Performance](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#report-type-performance).

<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/reports/export-report-01-26-2.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=084809c2cc86aa1b051f328851380df6" alt="Use this work area to preview your report before committing to an export" width="1550" height="914" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/reports/export-report-01-26-2.png" />

<h4 id="page-size-and-orientation">
  Page Size and Orientation
</h4>

Page size and orientation options include:

* US Letter - Portrait
* US Letter - Landscape
* A4 - Portrait
* A4 - Landscape
* A3 - Portrait
* A3 - Landscape

<h2 id="edit-and-delete-a-self-service-report">
  Edit and Delete a Self Service Report
</h2>

All self service reports you create can be edited, updated, and deleted as needed.

**Edit the data in a self service report**

1. Log in as an administrator or a user who has been assigned to a group who can create and edit self service reports.
2. Select the **Library** option from the [main menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access#the-main-menu), then the **Reports** tab in the library The library displays dashboards in a table (list) format.
3. Select the report in the list. The report opens.
4. Adjust the data in the report, adding or removing columns, [grouping](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/rdt#group-and-ungroup-table-data) or [ungrouping data](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/rdt#group-and-ungroup-table-data), changing the order of columns, or applying [conditional formatting](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/rdt-condt-format-using#using-the-conditional-formatting-sidebar-tables) as needed. Use the [reports icon bar](#use-the-report-icon-bars) to make other adjustments, such as refreshing the data, marking the report as a favorite, or saving a copy of the report with a new name.
5. Save your report.

**Edit the header and footer in a self service report**

1. Log in as an administrator or a user who has been assigned to a group who can create and edit self service reports.

2. Select the **Library** option from the [main menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access#the-main-menu), then the **Reports** tab in the library. The library displays reports in a table (list) format.

3. Select the report in the list. The report opens.

4. Adjust the headers and footers. Toggle the Report Header and Footer widgets to enable or disable using [reports icon bar](#use-the-report-icon-bars). When enabled, select the Edit icon to change the info presented in the header and footer.

5. Save your report.

   <Warning>
     The name of the report, the date of the report, pagination information, and any trademark information you provide are included in all reports, even if the headers and footers are disabled.
   </Warning>

**Delete a report from the library**

1. Log in as an administrator or a user who has been assigned to a group who can create and edit self service reports.
2. Select the **Library** option from the [main menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access#the-main-menu), then the **Reports** tab in the library The library displays reports in a table (list) format.
3. Locate the report you want to delete.
4. Select delete (<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/trashcan.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=2f005e6454f4553621ce9f5926d15d6a" alt="" width="17" height="19" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '17px', height: '19px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/trashcan.png" />) icon in the **Actions** column.
5. Confirm by selecting the **Delete** button on the warning dialog.

**Delete a report from the report itself**

1. [Edit](#edit-and-delete-a-self-service-report) the report.
2. Select delete (<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/trashcan.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=2f005e6454f4553621ce9f5926d15d6a" alt="" width="17" height="19" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '17px', height: '19px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/trashcan.png" />) icon from the [reports icon bar](#use-the-report-icon-bars).
3. Confirm by selecting the **Delete** button.

<h2 id="format-self-service-reports">
  Format Self Service Reports
</h2>

### Header and Footer Formatting

Format the header and footer rich text snippet widgets of your self service report to provide information about the report data. Provide context, link external resources, or add images.

As you add and update your text, use keyboard shortcuts to undo and redo formatting changes. If you employ custom attributes in your environment, incorporate them as needed.

<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/ssr-repts/format-menu-26-2.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=67eb67f79cd991e4ba77885de16cce8d" alt="use to format the look and feel of this widget" width="366" height="44" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/ssr-repts/format-menu-26-2.png" />

Format options include:

<table>
  <thead>
    <tr>
      <th>Formatting Option</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>Text Style (Paragraph Level Format)</td>

      <td>
        Three text style options are available for formatting the text of your snippet at the paragraph level. After making a selection, you can apply additional format options as needed.

        <br />

        * **Body**: Default text format.
        * **Header 1**: A bold text format, larger than **Body** and **Header 2**.
        * **Header 2**: A bold text format, larger than **Body** and smaller than **Header 1**.
      </td>
    </tr>

    <tr>
      <td>Align</td>

      <td>
        Align your paragraphs. There are four alignment options:

        <br />

        * **Align Left**: Select to left align a paragraph.
        * **Align Center**: Select to center align a paragraph.
        * **Align Right**: Select to right align a paragraph.
      </td>
    </tr>

    <tr>
      <td>Bold</td>
      <td>Apply bold formatting to selected text, if the default text style is not bold.</td>
    </tr>

    <tr>
      <td>Italic</td>
      <td>Apply italic formatting to selected text.</td>
    </tr>

    <tr>
      <td>Underline</td>
      <td>Underline the selected text.</td>
    </tr>

    <tr>
      <td>Bullet List</td>
      <td>Select to start a bulleted list. Alternatively, select text and convert it to a bulleted list of body text.</td>
    </tr>

    <tr>
      <td>Numbered List</td>
      <td>Select to start a numbered list. Alternatively, select text and convert it to a numbered list of body text.</td>
    </tr>

    <tr>
      <td>Add Image</td>

      <td>
        Select to insert an image. Opens the Add Image work area.

        <br />

        * Provide an **Image URL** to include an image; Self-Service Analytics imports the image into the rich text snippet (header or footer).
        * If needed, provide **Alternative Text** for your image.

        <br />

        <Note>
          Keep your header and footer image sized between 200kb and 500kb for [optimal rendering](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#file-size-and-media) performance.
        </Note>
      </td>
    </tr>

    <tr>
      <td>Clear Formatting</td>
      <td>Select to clear color and font formatting (bold, italic, underline) from a paragraph.</td>
    </tr>
  </tbody>
</table>

<h3 id="format-self-service-reports-conditional-formatting">
  Conditional Formatting
</h3>

[Conditional formatting](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/rdt-condt-format-using#configure-conditional-formatting) increases report generation time significantly. A report with conditional formatting can take from twice as long to significantly longer than an equivalent report without it. Conditional formatting in complex reports exported to PDF format place a higher load on your environment, resulting in a percentage of error rates.

Self service reports support conditional formatting on reports with and without [grouped data](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/rdt#group-and-ungroup-table-data). You can apply conditional formatting rules as you would for a table visual. See [Configure Conditional Formatting](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/rdt-condt-format-using#configure-conditional-formatting).

<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/reports/cnd-fmt-rep-26-2.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=158849f3caa4891dfa9166334cf1be89" alt="Use the conditional formatting sidebar menu to apply conditional formatting to data and grouped data" width="1246" height="869" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/reports/cnd-fmt-rep-26-2.png" />

<h2 id="use-the-report-icon-bars">
  Use the Report Icon Bars
</h2>

When you create or edit a report, a series of icons are available you can use to perform specific report functions.

<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/ssr-repts/ssr-icons-02-26.2.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=79fa620f7ce7d61535c0d9684d5e4242" alt="view a report as a non-editor" width="344" height="49" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/ssr-repts/ssr-icons-02-26.2.png" />

<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/ssr-repts/ssr-icons-26-2.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=b197d8934be795e77c1e4a67a5293a12" alt="options available for reports for exporting, refreshing, deleting, saving, and more" width="407" height="53" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/ssr-repts/ssr-icons-26-2.png" />

Select an icon to perform the function described in the following table.

<Note>
  The visibility of these icons on a report are affected by interactivity settings defined for dashboards in the library. See [Control How Users Interact With a Dashboard](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-interactivity).
</Note>

<table>
  <thead>
    <tr>
      <th>Icon</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/view-mode-26-2.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=b61226fd4880622f9cb1f0ed9fea6e5b" alt="toggle between view and edit mode" width="36" height="30" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '36px', height: '30px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/view-mode-26-2.png" />
      </td>

      <td>Toggle view mode between Viewer and Editor modes.</td>
    </tr>

    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/ss-export.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=424bda57a7392435084861da01595ee7" alt="export this item" width="42" height="42" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '42px', height: '42px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/ss-export.png" />
      </td>

      <td>
        Export a report. Enabled if there are no unsaved changes to your report.

        <br />

        Select to open a preview window of your report; review and export or cancel the export. See [Export Your Self Service Report](#export-your-self-service-report).
      </td>
    </tr>

    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/share-ssr-26-2.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=a1b1ca8ab4d325c5af8799bebc193636" alt="select to share your self service report" width="36" height="37" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '36px', height: '37px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/share-ssr-26-2.png" />
      </td>

      <td>Share your report.</td>
    </tr>

    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-refresh.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=53cc532b6fce4e41f7756425d1b87639" alt="select to refresh the underlying data behind an object, or the specific field" width="34" height="34" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '34px', height: '34px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-refresh.png" />
      </td>

      <td>Refresh the data in the report.</td>
    </tr>

    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-fav.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=b316dd7cb31ab07c459eb50f712f6211" alt="select the favorite icon to add or remove the item from your favorited items" width="35" height="34" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '35px', height: '34px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-fav.png" />
      </td>

      <td>Mark the report as a favorite.</td>
    </tr>

    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/ssr-head-foot.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=ca83531f4552a1abf12b2b46be38f849" alt="select to enable or disable header and footer" width="40" height="38" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '40px', height: '38px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/ssr-head-foot.png" />
      </td>

      <td>Select to enable and disable the header and footer. See [Edit the header and footer in a self service report](#edit-and-delete-a-self-service-report).</td>
    </tr>

    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/ssr-sched.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=f44b70aa9d2d00e61408da7dda4dc05d" alt="create a schedule for the self service report" width="37" height="37" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '37px', height: '37px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/ssr-sched.png" />
      </td>

      <td>Schedule a self service report to be sent. See [Schedule a Self Service Report or Dashboard Report](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-schedule#schedule-a-self-service-report-or-dashboard-report).</td>
    </tr>

    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/ssr-delete.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=b035a371c8b5441f62356131ffda1ccb" alt="delete the report" width="35" height="35" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '35px', height: '35px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/ssr-delete.png" />
      </td>

      <td>Delete the report. See [Edit and Delete a Self Service Report](#edit-and-delete-a-self-service-report).</td>
    </tr>

    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/save-as-26-2.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=f3207624e63cc3b32da04e7f49d7181a" alt="save your item with a new name" width="38" height="38" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '38px', height: '38px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/save-as-26-2.png" />
      </td>

      <td>Save a report with a new name (which copies it).</td>
    </tr>

    <tr>
      <td>
        <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/save-26-2.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=f14ab267840c87743de88f0eafdb23d5" alt="save your item" width="38" height="38" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '38px', height: '38px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/save-26-2.png" />
      </td>

      <td>Save a report.</td>
    </tr>
  </tbody>
</table>

<h2 id="use-the-self-service-reports-library">
  Use the Self Service Reports Library
</h2>

The work area of the reports library contains all reports in your environment to which you have access. Make a report a favorite, delete it (if your [privileges](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference) allow), and open the report.

If you have not been given access to reports, you will see no reports in the reports library. You may be able to create reports, but you may not be able to save them. Contact your system administrator to increase your [privileges](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference).

### Access the Reports Library

To access the reports library, select the **Reports** card from the home page, or select **Library** on the [menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access#the-main-menu), then the Reports tab. The reports library opens, and reports display in a table (list) format.

<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/ssr/rpt-lib-26-2.jpg?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=c67faa2735d6d30ff3ee850ad67a8f5e" alt="use to manage your reports" width="1368" height="424" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/ssr/rpt-lib-26-2.jpg" />

### Search Field

You can use the search field to filter the reports in this work area by report Name, Description (if provided), Data Source, or Author. For example, if you type a **C** in the search box, only reports that include the letter *C* in the selected field searched are shown in the working area. See [Search and Filter Lists](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access#search-and-filter-lists).

### Buttons

The buttons on the page allow easy access to saved dashboards, as well as other dashboards created by other users in your environment. They also allow you to create a new dashboard, filter the dashboards that are shown, import, or export dashboards.

| Button | Description |
| - | - |
| **All** | Removes any filters for the reports library and displays all reports available to you within your environment. |
| <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/buttons/dash-favorites.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=3f42e7b5a7ec088f144961fc4e0b8168" alt="" width="32" height="32" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '32px', height: '32px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/buttons/dash-favorites.png" /> | Displays only the reports you have marked as favorites. |
| <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/buttons/sym-my-items.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=b2b406bede3716ad5058ae7e353fc7c6" alt="" width="32" height="33" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '32px', height: '33px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/buttons/sym-my-items.png" /> | Displays only reports you created and saved. Reports created and saved by other users are hidden. |
| <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/dashboard-embed.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=64e9abef187115e782e94be2349f4b08" alt="" width="33" height="33" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '33px', height: '33px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/dashboard-embed.png" /> | Select to generate an embeddable report link. |

### List of Reports

The columns for this list are described below. Several of these columns can be used to sort the contents of the list: select the column header to sort first to last and again to sort last to first. You can search for items by the contents of several columns. See [Search and Filter Lists](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access#search-and-filter-lists).

<table>
  <thead>
    <tr>
      <th>Column</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>Select (not labeled)</td>
      <td>Select or deselect one or more items.</td>
    </tr>

    <tr>
      <td>Fav</td>
      <td>Identifies favorite reports using a star icon. If the star is colored (<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/star-filled.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=2ee76d6f85fbd0c028cac5946b824b24" alt="" width="16" height="19" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '16px', height: '19px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/star-filled.png" />), the report is a favorite. If the star is empty (<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/star-open.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=7e48cb6585e2fe8ca8a2c41ec3d77e7c" alt="" width="16" height="17" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '16px', height: '17px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/star-open.png" />), the report is not a favorite. If you change the favorite status of a report while viewing or editing it, that change is reflected here.</td>
    </tr>

    <tr>
      <td>Name</td>
      <td>The name of the self service report. This is a searchable field.</td>
    </tr>

    <tr>
      <td>Description (not labeled)</td>
      <td>The description icon is visible if a description associated with a report. This is a searchable field.</td>
    </tr>

    <tr>
      <td>Tags</td>
      <td>Content tags applied to the report. Select the filter icon to open a drop down list and select tags to filter your list or to [narrow your search results](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access#filter-lists-and-search-results-using-tags). If several tags are associated with an item, hover over the ellipsis to see all tags for this resource. This is a searchable field.</td>
    </tr>

    <tr>
      <td>Filter icon</td>
      <td>Select to filter the contents by one or more content tags.</td>
    </tr>

    <tr>
      <td>Data Source</td>
      <td>The name of the data sources used by the report. This is a searchable field.</td>
    </tr>

    <tr>
      <td>Author</td>
      <td>The user who created the report. This is a searchable field.</td>
    </tr>

    <tr>
      <td>Modified Date</td>
      <td>The date the report was last modified.</td>
    </tr>

    <tr>
      <td>Schedule</td>

      <td>
        Select the clock (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/dashboard-schedule.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=9e7a1179faaedda7e8026e3ccd40ddcd" alt="select the schedule report icon to schedule a dashboard or report with others" width="18" height="18" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '18px', height: '18px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/dashboard-schedule.png" />) in this column to create a scheduled for this report. The Scheduled Reports dialog appears.

        <br />

        See [About Scheduled Reports](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-schedule).
      </td>
    </tr>

    <tr>
      <td>Permissions</td>
      <td>Select the permissions icon in this column to assign permissions to a report. The Report Permissions dialog appears.</td>
    </tr>

    <tr>
      <td>Actions</td>

      <td>
        Shows icons you can select to perform actions for the report.

        <br />

        * Select the delete icon (<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/trashcan.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=2f005e6454f4553621ce9f5926d15d6a" alt="" width="17" height="19" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '17px', height: '19px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/trashcan.png" />) in this column to delete a report.
        * Select the code snippet icon (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/dashboard-embed.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=64e9abef187115e782e94be2349f4b08" alt="" width="32" height="32" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '32px', height: '32px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/dashboard-embed.png" />) icon to generate an embeddable code snippet for the report. The Embed Code dialog appears. See [Embed Components Into Your Application](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/embed/dash-embed/dash-embed).
      </td>
    </tr>
  </tbody>
</table>
