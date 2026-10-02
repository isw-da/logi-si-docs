> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Export Visuals

Export your visuals in a variety of formats, as an image or data you can share with others. To export visuals for import into another instance of your software, see [Export Visual Gallery Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-gallery#export-visual-gallery-visuals).

<Note>
  Exports do not support special characters. If names associated with your visual, such as visual name, display name, or data source name contain special characters, update the name before export.
</Note>

You can export your data from your visuals in several formats:

* Screenshot (PNG) - an image

* PDF - an image

* Visual Data

  * CSV - Comma separated values file
  * XLSX - Excel compatible file

* Raw Data

  * CSV - Comma separated values file
  * XLSX - Excel compatible file

  <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/export-visual-menus-23-1.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=96b5f1de01d0c9970efbc4d30ce474c7" alt="select a visual export option" width="506" height="220" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/export-visual-menus-23-1.png" />

<Note>
  Grouped table data can not be exported as raw or aggregate visual data.
</Note>

<Note>
  The number of records included is limited by the setting of the `zoomdata.export.data.max.rows` property in the `zoomdata.properties` file. See [Configuration Property Files](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#configuration-property-files).
</Note>

## Export a Visual as XLSX With Formatting

Table visuals can export to Excel (XLSX) files with formatting and conditional formatting when the [report service](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#server-level-variables) is [enabled](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#self-service-report-microservice).

1. Select **Export** from the [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu). Select the export option **XLSX With Formatting**.

2. The Export as XLSX dialog opens.

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/visuals/export-format-xlsx-26-2.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=8e8623e64d3515779c1f39185633fc48" alt="Rename your file and add or remove the time bar using this work area" width="495" height="313" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/visuals/export-format-xlsx-26-2.png" />

3. Accept or change the file name.

4. Select **Export**. Self-Service Analytics prepares an Excel (XLSX) file downloaded by your browser.

Control whether a visual can be exported in your embedded environment using the interactivity sidebar. See [Control How Users Interact With a Visual](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-interactivity).

For more information, see the following articles:

* [Export Visual Gallery Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-gallery#export-visual-gallery-visuals)
* [Export a Visual as an Image](#export-a-visual-as-an-image)
* [Export Visual Data in CSV or XLSX Format](#export-visual-data-in-csv-or-xlsx-format)
* [Export Raw Data in CSV or XLSX Format](#export-raw-data-in-csv-or-xlsx-format)

<h2 id="export-a-visual-as-an-image">
  Export a Visual as an Image
</h2>

**Export a visual as a screenshot or PDF**

1. Select **Export** from the [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu). Select an export option for your visual.

2. Select an image format on the submenu, **Screenshot (PNG)** or **PDF**.

3. If you select **Screenshot (PNG)**, the screenshot is prepared, and automatically downloaded by your browser.

4. If you select **PDF**, the Export as PDF dialog opens.

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/export-visual-PDF.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=e22c37db0ea7b122deb83853b15534d0" alt="" width="498" height="307" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/export-visual-PDF.png" />

5. Use this work area to optionally:

   1. Enter a header and footer for your PDF.
   2. Enable **Add Username** to include your user name on the PDF.
   3. Enable **Add Timestamp** to add a date and time stamp to the PDF.

6. Select **Export**. Self-Service Analytics prepares a PDF downloaded by your browser.

<Note>
  The number of records included is limited by the setting of the `zoomdata.export.data.max.rows` property in the `zoomdata.properties` file. See [Configuration Property Files](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#configuration-property-files).
</Note>

<h2 id="export-raw-data-in-csv-or-xlsx-format">
  Export Raw Data in CSV or XLSX Format
</h2>

When you export raw data from your visuals to XLSX, numeric fields are exported as numbers. Dates are exported as dates in ISO 8601 format. When you export raw data to csv format, both numeric and date fields are exported as strings..

**Export raw data in CSV format**

1. Select **Export** from the [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu). Select an export option for your visual.

2. Select a file format on the submenu, **Raw Data > CSV**.

3. The Export as CSV dialog opens.

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/export-raw-csv-23-1.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=4a2a1b5af074aa916c35dde9e59747f7" alt="Enter csv options here" width="498" height="348" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/export-raw-csv-23-1.png" />

4. Accept or change the default settings:

   * Accept or change the file name.

   * Specify the **Number of Records** to include in the export. The default is 1,000.

     <Note>
       The number of records you can specify is limited by the setting of the `zoomdata.export.data.max.rows` property in the `zoomdata.properties` file. See [Configuration Property Files](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#configuration-property-files).
     </Note>

   * Select a field to sort the data included in the export. The default for **Sort by** field is none. Depending on the field type selected, you have sort order options you can use to organize your data.

5. Select **Export**. Self-Service Analytics prepares a CSV file downloaded by your browser.

<Note>
  The number of records included is limited by the setting of the `zoomdata.export.data.max.rows` property in the `zoomdata.properties` file. See [Configuration Property Files](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#configuration-property-files).
</Note>

**Export raw data in XLSX format**

1. Select **Export** from the [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu). Select an export option for your visual.

2. Select a file format on the submenu, **Raw Data > XLSX**.

3. The Export as XLSX dialog opens.

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/export-raw-xlsx-23-1.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=b124ae38a0ff58f16fc1e6e0d55169f4" alt="Enter XLSX options here" width="496" height="405" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/export-raw-xlsx-23-1.png" />

4. Accept or change the default settings:

   * Accept or change the file name.

   * Specify the **Number of Records** to include in the export. The default is 1,000.

     <Note>
       The number of records you can specify is limited by the setting of the `zoomdata.export.data.max.rows` property in the `zoomdata.properties` file. See [Configuration Property Files](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#configuration-property-files).
     </Note>

   * Select a field to sort the data included in the export. The default for **Sort by** field is none. Depending on the field type selected, you have sort order options you can use to organize your data.

   * Select **Add Time Bar filter description to exported file** to include in the export.

   * Select **Add Visual filter description to exported file** to include in the export.

5. Select **Export**. Self-Service Analytics prepares an XLSX file downloaded by your browser.

<Note>
  The number of records included is limited by the setting of the `zoomdata.export.data.max.rows` property in the `zoomdata.properties` file. See [Configuration Property Files](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#configuration-property-files).
</Note>

<h2 id="export-visual-data-in-csv-or-xlsx-format">
  Export Visual Data in CSV or XLSX Format
</h2>

**Export visual data in CSV or XLSX format**

1. Select **Export** from the [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu). Select an export option for your visual.

2. Select a file format on the submenu, **Visual Data > CSV** or **Visual Data > XLSX**.

3. If you select **CSV**, the Export as CSV dialog opens.

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/export-visual-as-CSV-23-1.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=d35efa46e81020a21f284d5a7cb03ce4" alt="Use or update the file name for your export" width="498" height="198" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/export-visual-as-CSV-23-1.png" />

   Accept or change the file name, then select **Export**. Self-Service Analytics prepares a CSV file downloaded by your browser.

4. If you select **XLSX**, the Export as XLSX dialog opens.

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/export-visual-as-XLSX-23-1.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=6e938a0974e4bcd2f218353f3621af9a" alt="Use this work area to define options for your XLSX file" width="497" height="258" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/export-visual-as-XLSX-23-1.png" />

   Accept or change the default settings:

   * Accept or change the file name.
   * Select **Add Time Bar filter description to exported file** to include in the export.
   * Select **Add Visual filter description to exported file** to include in the export.

5. Select **Export**. Self-Service Analytics prepares an XLSX file downloaded by your browser.

<Note>
  The number of records included is limited by the setting of the `zoomdata.export.data.max.rows` property in the `zoomdata.properties` file. See [Configuration Property Files](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#configuration-property-files).
</Note>

<h2 id="export-visual-data-in-excel-xlsx-format">
  Export Visual Data in Excel (XLSX) Format
</h2>

When you [enable](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#server-level-variables) self service report [microservice](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#self-service-report-microservice) in your environment, users can export self service reports and table visuals, complete with formatting and conditional formatting, to a formatted Excel (XLSX) file format.

<h3 id="export-visual-data-in-excel-xlsx-format-export-a-visual-as-xlsx">
  Export a Visual as XLSX With Formatting
</h3>

Table visuals can export to Excel (XLSX) files with formatting and conditional formatting when the [report service](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#server-level-variables) is [enabled](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#self-service-report-microservice).

1. Select **Export** from the [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu). Select the export option **XLSX With Formatting**.

2. The Export as XLSX dialog opens.

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/visuals/export-format-xlsx-26-2.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=8e8623e64d3515779c1f39185633fc48" alt="Rename your file and add or remove the time bar using this work area" width="495" height="313" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/visuals/export-format-xlsx-26-2.png" />

3. Accept or change the file name.

4. Select **Export**. Self-Service Analytics prepares an Excel (XLSX) file downloaded by your browser.
