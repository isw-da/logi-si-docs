> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Import Dashboards

<Note>
  In this release, when your admin enables the Enhanced Experience user interface, you will see changes to workflows you may have used in previous releases.
</Note>

**Import one or more dashboards**

1. Log in as an admin or user with the **Manage Connections**, **Administer Sources**, **Administer Visuals** and **Administer Dashboards** [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference). If you are logged in as a tenant admin, verify you're in or switch to the appropriate tenant.

2. Select the **Discovery Board** card on your home page or **Library** from the main menu. The dashboard library opens.

3. Select **Import Dashboard** in the library work area. The Import Dashboards dialog opens.

4. Browse to and choose the `json` file for the dashboards you want to import, then select **Open**.

   The Import Dashboards dialog populates with information about the objects that make up your dashboards and the settings you can use to define how your software inserts each object.

   <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/dashboards/imp-dash-26-2.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=29c9a8e5e3aaadce0cdb0aa745ed94a6" alt="Use this work are to define what JSON file to import, for which tenants, using what insertion strategies, matching strategies, tags, and access levels" width="647" height="1322" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/dashboards/imp-dash-26-2.png" />

5. Add and remove tenants by selecting the **Tenants** field. Add or remove them from the list or field.

   <Note>
     Only system admins or members of the Content Distributors group see the Tenants field. If this field is not shown, the content is imported into the tenant you are currently working in.
   </Note>

6. Optionally, enable or disable **Ignore Warnings**.

   When you enable **Ignore Warnings**, a Tags field is added to the Import work area. Add or create tags to apply to objects that do not import cleanly.

   * If errors occur during import, your software adds the tags you select to the affected objects.
   * Use the tags to find dashboards, visuals, filter snippets, or sources you need to fix.

   <Note>
     When you enable Ignore Warnings, items that can be imported with warnings are imported and tagged. Use these tags to find and fix the warnings in tagged objects. When disabled, no objects are imported, and errors are returned to aid in troubleshooting.
   </Note>

7. Select an **Insertion Strategy** for each group of objects.

   <Note>
     The groups of objects varies based on what objects are in your JSON file. For example, dashboards that contain only local visuals will not import visuals as separate objects to include in the Visual Gallery.
   </Note>

   * **Always create objects**: Select to create an object every time, even if an existing object exists with the same name or unique ID. The object is created, appended with a date and time to the name, and assigned a unique ID.
   * **Reuse existing objects**: Select to create an object if no object with the same name exists. If an object with the same name or unique ID exists, the original object is reused.
   * **Update existing objects**: Select to update (overwrite) an existing object with the same name or unique ID. If an object with the same name does not exist, an object is created.

8. Use the default **Matching Strategy** or select the appropriate strategies for your sources in the order you want the strategies to be processed. See [Matching Strategies](#matching-strategies).

9. Enable **Share Default Access With All Users** to immediately give your users access to the content you import.

10. After you have confirmed your choices, select **Import**. The visuals are imported and a success message is returned if objects import successfully or with accepted warnings. Any items imported with warnings have your selected tags applied

<Note>
  If you import an exported source that has an associated translation file, you must re-upload the translation for that source.
</Note>

### Dashboard Import Defaults

* Dashboards with a unique name are imported with that name. If the name is not unique, the newly imported dashboard is imported and the name appended with a date and time.

  <Warning>
    Trying to import a dashboard that uses the same source name as an existing source but uses different connection details or credentials may cause issues. Change the name of the source before you export it from one instance and import it into another.
  </Warning>

* Items unique to a dashboard, such as local visuals, rich text snippets, and filter snippets are created with the new dashboard.

<h3 id="matching-strategies">
  Matching Strategies
</h3>

When you import objects into your environment, combine these matching strategies with your selected insertion strategies to meet your organization's needs. The strategies are applied in the order you select. When you create new objects, matching strategies are not used.

#### Dashboards

| Strategy | Notes |
| - | - |
| By Name | The default strategy used if no other strategies are selected. |
| By Origin ID | |

#### Visuals

| Strategy | Notes |
| - | - |
| By Name | The default strategy used if no other strategies are selected. |
| By Origin ID | |

#### Sources

| Strategy | Notes |
| - | - |
| By Name | The default strategy used if no other strategies are selected. |
| By Origin ID | |

#### Connections

| Strategy | Notes |
| - | - |
| By Id, Type, and Parameters | A default strategy used if no other strategies are selected. Used with **By Type and Parameters** if it's not deselected. |
| By Type and Parameters | A default strategy used if no other strategies are selected. Used with **By Id, Type, and Parameters**. |
| By Name | |
| By Name and Type | |
| By Origin ID | |
| By Type and Parameter Keys | |

<h2 id="import-and-convert-dashboards-earlier-versions">
  Import and Convert Dashboards - Earlier Versions
</h2>

You can easily import dashboards from an earlier version of as needed.

* Dashboards exported from Composer 7.10 and later can be imported to Composer versions 7.10.x, 8.1 – 8.4, and 22.4 and later.
* Dashboards exported from Composer 7.9 and earlier can only be imported to the same major Composer version.

Imported dashboards from earlier versions of may need conversion to a responsive dashboard layout. Select the **Convert Now** option on the provided prompt to convert an imported dashboard. See [Dashboard Layouts](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-layout).

<h2 id="export-dashboards">
  Export Dashboards
</h2>

You can export your dashboards in a variety of formats. Exported dashboards enable you to share your data with others. JSON configuration exports allow you to transfer a dashboard to another environment. See Import Dashboards.

<Note>
  Special characters are not supported for exports. If your visual name or the name of the data source contains special characters, change the name before continuing.
</Note>

<Note>
  To export a dashboard, you must be a user belonging to a group with the **Export Dashboards** [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference).
</Note>

Dashboards can be exported in the following formats:

* PNG Screenshot (as an image).
* PDF file (as an image).
* JSON configuration (for one or more entire dashboards). JSON exports include [dashboard interactivity profile](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-interactivity) settings to allow import of the same interactivity profile.
* XLSX format - as a spreadsheet with Raw Data or Visual Data. Each visual is included on its own sheet.

**Export a dashboard**

1. On the dashboard, select export icon on the dashboard icon bar. A drop-down menu appears.

   <img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/export-dashboard-menu-23-2.png?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=cbe202ebf768b8490b6d734aaca03972" alt="Select how you want your dashboard data exported" width="385" height="218" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/export-dashboard-menu-23-2.png" />

2. Select an export file format.

   * When you select **Screenshot (PNG)**, your environment creates a PNG file. This is downloaded to your browser.

   * When you select **PDF** format, the Export as PDF dialog appears.

     <img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/export-dashboard-pdf.png?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=f1d0d118b111de5a4f3bca4d55e70725" alt="" width="384" height="267" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/export-dashboard-pdf.png" />

     Optionally, specify a header and footer for the PDF. Slide the **Add Username** switch on (to the right) to add a user name to the PDF. Slide the **Add Timestamp** switch on (to the right) to add a time stamp to the PDF. Then select **Export**.

   * When you select **Configuration (JSON)** format, the JSON file is automatically downloaded to your browser.

   * When you select **Data (XLSX) > Raw Data** or **Data (XLSX) > Visual Data** format, the XLSX file is automatically downloaded to your browser.

**Export multiple dashboards**

1. Log in as a user with the [**Export Dashboards** privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference). Open the Library to view a list of the dashboards you can access.
2. Select to export one or more dashboards by selecting the checkbox for a dashboard to export. The **Export Selected Items** button becomes active.
3. Select **Export Selected Items**. You browser downloads the selected items in JSON format, placing them in the location you select or the default location for your browser downloads.

Dashboards exported using the export API can include source cache settings for the data and statistics caches in the payload.

API documentation is provided in your environment at this link: `https://<Self-Service Analytics-URL>/composer/swagger-ui.html`.
