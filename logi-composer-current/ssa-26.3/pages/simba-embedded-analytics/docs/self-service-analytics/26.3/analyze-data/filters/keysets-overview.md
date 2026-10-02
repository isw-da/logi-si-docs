> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Use Keysets

Keysets are collections of unique data values that can be saved and used in further analysis of your data. They allow you to perform multipass and multisource filtering of your data.

You can create a keyset by selecting a single field for the keyset from visual data. Filtering the visual data before creating the keyset limits the unique data values the keyset includes. The field you select for the keyset is known as the keyset's *key field*. For example, from a visual that lists airport codes nationwide but that has been filtered to show only Virginia airports, you can create a keyset listing only Virginia airport codes by selecting the airport code field as the keyset's key field.

You can also create and update a keyset from a CSV file.

You can apply a keyset as a visual filter.

* This limits the visual's result set to records containing values stored in the keyset.
* Apply keyset filters to visuals from the same or different data sources. However, the data source for the target visual must contain a field storing the same kind of data as the keyset's key field.
* You can update a keyset at any time by uploading new values for the keyset.

<Note>
  When working with multiple filter types on the same visual or filter snippet, row-level filters (including wildcard filters) are applied first to a visual or filter snippet, keyset filters are applied second, and group filters are applied last on the aggregated result set.
</Note>

To control whether keysets can be created or managed from a visual, use the interactivity sidebar. See [Control How Users Interact With a Visual](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-interactivity).

See the following topics.

* [Create a Keyset](#create-a-keyset)
* [Create a Keyset From the Visual Result Set](#create-a-keyset-from-the-visual-result-set)
* [Create a Keyset From a Data Point](#create-a-keyset-from-a-data-point)
* [Create a Keyset From a CSV File](#create-a-keyset-from-a-csv-file)
* [Review and Apply a Keyset as a Visual Filter](#review-and-apply-a-keyset-as-a-visual-filter)
* [Delete a Keyset](#delete-a-keyset)
* [Upload Keyset Data From a CSV File Using the API](#upload-keyset-data-from-a-csv-file-using-the-api)
* [Update Keyset Values From a CSV File Using the API](#update-keyset-values-from-a-csv-file-using-the-api)

<h2 id="create-a-keyset">
  Create a Keyset
</h2>

You can create a keyset in several ways. Keysets are shared by all users of your Self-Service Analytics instance.

* [Create a Keyset From the Visual Result Set](#create-a-keyset-from-the-visual-result-set)
* [Create a Keyset From a Data Point](#create-a-keyset-from-a-data-point)
* [Create a Keyset From a CSV File](#create-a-keyset-from-a-csv-file)
* [Update Keyset Values From a CSV File Using the UI](#update-keyset-values-from-a-csv-file-using-the-ui)

To control whether keysets can be created or managed from a visual, use the interactivity sidebar. See [Control How Users Interact With a Visual](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-interactivity).

<h2 id="create-a-keyset-from-a-csv-file">
  Create a Keyset From a CSV File
</h2>

You can create a keyset from a CSV file. The CSV file must meet the following requirements:

* The data values in the file must be in a single column.
* The file must be UTF-8 formatted.
* The file cannot contain more than 1000 rows.
* The data type of the CSV values (number, time, attribute, etc.) must match the data type of the field to which the CSV keyset data will be applied.

**Create a keyset from a CSV file**

1. Review a visual in the Visual Gallery or in a dashboard.

2. Select the filter icon on the [visual](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters#apply-a-row-level-filter-to-a-visual-or-filter-snippet) or [dashboard](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters#apply-a-row-level-filter-to-a-dashboard) to access the appropriate filter sidebar.

   * To access the visual filter sidebar, select its filter icon (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=0a044ea0662c55e06133074a55d93cd9" alt="select the filter icon to open the filters sidebar and add or edit filters" width="17" height="17" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '17px', height: '17px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png" />) or select **Settings** from the [visual menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu) (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" />) and then select <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-filter.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=4b06f0c1f1b48c50da73f73672d5b1c6" alt="" width="20" height="21" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '21px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-filter.png" /> on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu).

   * To access the dashboard filter sidebar, select its filter icon (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=0a044ea0662c55e06133074a55d93cd9" alt="select the filter icon to open the filters sidebar and add or edit filters" width="17" height="17" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '17px', height: '17px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png" />). The dashboard-level filter icon is available only when all the visuals are from the same data source.

   The Filters sidebar appears, showing any filters that have been applied.

3. Select **Add Filter**.

4. Select a filter field on the Filter sidebar. Remember that the field data type must match the data type of the CSV data you will upload (for example, if the field is a numeric field, the CSV data must be also be numeric).

   The Filters sidebar displays three tabs:

   * The **Value** tab allows you to select values for the filter.

   * The **Wildcard** tab allows you to specify a row-level wildcard filter for the visual.

   * The **Keyset** tab allows you to select a keyset for the filter or to upload a CSV file as a keyset.

     <Note>
       If your example uses numeric data, the tabs may vary. See [Set a Numeric Field Filter](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters-attr#set-a-numeric-field-filter).
     </Note>

5. Select the **Keyset** tab. The keysets and saved filters defined in your environment are listed.

6. Select **Upload Keyset Values**. An Upload Keyset Values panel appears in the Filters sidebar allowing you to specify information about the CSV file and the keyset you are creating.

   <Note>
     If the upload file contains more records than are allowed by your Self-Service Analytics environment configuration, the keyset will not upload and an error occurs.
   </Note>

7. Enter a name for the keyset in the **Name** box. Because the keyset will be shared by all users of your Self-Service Analytics instance, be sure to enter a unique name.

8. Optionally, enter a description for the keyset in the **Description** box.

9. In the **Choose a file to Add Keyset Values** box, browse for and select the CSV file containing the keyset values you want to upload.

   <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/keyset-jewelry.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=0fb0fe4ea7cecca9193d93fa158e9132" alt="Set your keyset details here, and upload a new keyset if needed" width="439" height="651" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/keyset-jewelry.png" />

10. Select **Upload Keyset** to upload the CSV file for the keyset.

    If the upload occurs successfully, a message displays that the upload was successful and the keyset details appear in the Filter sidebar. The keyset is now available to all users of your Self-Service Analytics instance.

11. When you are finished setting your filter values, select **Continue** and examine your updates. If they are correct, select **Apply**.

<h2 id="create-a-keyset-from-a-data-point">
  Create a Keyset From a Data Point
</h2>

You can create a keyset from a data point in a visual using the context menu. The result set used for the keyset is automatically filtered by the data point you select.

**Create a keyset from a data point**

1. Create a visual.

2. Select a data point in the visual. The context menu appears:

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/visuals/ctx-menu-viz-262.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=8f20db0db002a751168684ef92d52231" alt="Select a data point to open the context menu" width="1107" height="491" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/visuals/ctx-menu-viz-262.png" />

3. Select **Keyset**. The Save Keyset dialog appears.

   <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/save-keyset-22-4.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=27826051301ef88d4e6d4ea762e42586" alt="Use this work area to define a keyset for your source" width="498" height="652" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/save-keyset-22-4.png" />

4. Enter a name for the keyset in the **Name** box. The keyset is shared by all users of the Self-Service Analytics instance, and must be a unique name.

5. Optionally, enter a description for the keyset in the **Description** box.

6. In the **Select a Field as Key** box, select a field to use as the key for the keyset. This should be the field by which the original visual was grouped. A list of keyset values for the field you selected appears on the Save Keyset dialog. These values can include an empty value.

7. Select **Save** to save the keyset.

<h2 id="create-a-keyset-from-the-visual-result-set">
  Create a Keyset From the Visual Result Set
</h2>

You can create a keyset from the result set of a visual. Filtering the visual data before creating the keyset will limit the unique data values included in the keyset.

**Create a keyset from a visual result set**

1. Create a visual and filter it as desired.

   <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/va-airports.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=e19fb049854d1121e0b124496acfeff4" alt="" width="676" height="275" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/va-airports.png" />

2. Select <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" /> and then **Create Keyset** from the [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu). The Save Keyset dialog appears.

   <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/save-keyset2.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=d78a5df957181e8dc5fe62bdda9706e2" alt="" width="501" height="495" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/save-keyset2.png" />

3. Enter a name for the keyset in the **Name** box. Because the keyset will be shared by all users of the Self-Service Analytics instance, be sure to enter a unique name.

4. Optionally, enter a description for the keyset in the **Description** box.

5. In the **Select a Field as Key** box, enter the field that should be used as the key for the keyset. A list of keyset values for the field you selected appears on the Save Keyset dialog. These values can include an empty value.

6. Select **Save** to save the keyset.

<h2 id="update-keyset-values-from-a-csv-file-using-the-ui">
  Update Keyset Values From a CSV File Using the UI
</h2>

You can update the values of a keyset from a CSV file. The CSV file must meet the following requirements:

* The data values in the file must be in a single column.
* The file must be UTF-8 formatted.
* The file cannot contain more than 1000 rows.
* The data type of the CSV values (number, time, attribute, etc.) must match the data type of the field to which the CSV keyset data will be applied.

**Update keyset values from a CSV file**

1. Review a visual in the Visual Gallery or in a dashboard.

2. Select the filter icon on the [visual](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters#apply-a-row-level-filter-to-a-visual-or-filter-snippet) or [dashboard](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters#apply-a-row-level-filter-to-a-dashboard) to access the appropriate filter sidebar.

   * To access the visual filter sidebar, select its filter icon (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=0a044ea0662c55e06133074a55d93cd9" alt="select the filter icon to open the filters sidebar and add or edit filters" width="17" height="17" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '17px', height: '17px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png" />) or select **Settings** from the [visual menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu) (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" />) and then select <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-filter.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=4b06f0c1f1b48c50da73f73672d5b1c6" alt="" width="20" height="21" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '21px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-filter.png" /> on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu).

   * To access the dashboard filter sidebar, select its filter icon (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=0a044ea0662c55e06133074a55d93cd9" alt="select the filter icon to open the filters sidebar and add or edit filters" width="17" height="17" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '17px', height: '17px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png" />). The dashboard-level filter icon is available only when all the visuals are from the same data source.

   The Filters sidebar appears showing any filters that have been applied.

3. Select **Add Filter** or, if the keyset is already used to filter the visual, select the keyset name. If you select **Add Filter**, proceed to the next step. If you select the keyset name, the keyset details are displayed and you should skip to Step 6 of this procedure.

4. Select the filter field on the Filter sidebar. Remember that the field data type must match the data type of the CSV data you will upload (for example, if the field is a numeric field, the CSV data must be also be numeric).

   The Filters sidebar displays three tabs:

   * The **Value** tab allows you to select values for the filter.
   * The **Wildcard** tab allows you to specify a row-level wildcard filter for the visual.
   * The **Keyset** tab allows you to select a keyset for the filter or to upload a CSV file as a keyset.

5. Select the **Keyset** tab. The keysets and saved filters defined in your environment are listed.

6. Select the keyset to which you want to reupload keyset values. The keyset details appear.

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/keyset-details.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=835ff2c3d3a539ada0170c433c642f78" alt="Review and edit your keyset values" width="350" height="760" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/keyset-details.png" />

7. Select **Reupload Values**. An Upload Keyset Values panel appears in the Filters sidebar allowing you to specify information about the CSV file and the keyset you are updating.

   <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/keyset-jewelry.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=0fb0fe4ea7cecca9193d93fa158e9132" alt="Set your keyset details here, and upload a new keyset if needed" width="439" height="651" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/keyset-jewelry.png" />

   The Name and Description fields are read-only when you update keyset values from a CSV file.

8. In the **Choose a file to Add Keyset Values** box, browse for and select the CSV file containing the updated keyset values you want to upload.

   <Note>
     If the upload file contains more records than are allowed by your environment configuration, the keyset will not upload and an error occurs.
   </Note>

9. Select **Upload Keyset** to upload the CSV file for the keyset.

   If the upload occurs successfully, a message displays that the upload was successful and the keyset details appear in the Filter sidebar. The keyset is now available to all users of this instance.

10. When you are finished setting your filter values, select **Continue** and examine your updates. If they are correct, select **Apply**.

<h2 id="update-keyset-values-from-a-csv-file-using-the-api">
  Update Keyset Values From a CSV File Using the API
</h2>

You can update keyset data from a CSV file using the API. Use the `PUT /api/keysets/upload/<keyset-id>` API endpoint to do this. The keyset ID was assigned when the keyset was initially uploaded using a CSV file. See [Upload Keyset Data From a CSV File Using the API](#upload-keyset-data-from-a-csv-file-using-the-api).

It should be in the following format. A header should not be included.

```
fileData: <file-information>
fileName:<CSV-file-name>
keySetId:<keyset-ID>
keySetName:<keyset-name>
keySetDesc:<optional-keyset-description>
sourceId:<data-source-id>
```

For more information, see your API documentation.

API documentation is provided in your environment at this link: `https://<Self-Service Analytics-URL>/composer/swagger-ui.html`.

<h2 id="upload-keyset-data-from-a-csv-file-using-the-api">
  Upload Keyset Data From a CSV File Using the API
</h2>

You can upload keyset data from a CSV file using the API. Use the `POST /api/keysets/upload` API endpoint to do this. The CSV file must provide the field name, file data, the file name, the keyset name, and the data source definition ID. A keyset description is optional.

You must be the owner of the keyset or be a user with the **Administer Dashboards** [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference).

The CSV file should be in the following format. A header should not be included.

```
fieldName:<field-name>
fileData: <file-information>
fileName:<CSV-file-name>
keySetName:<keyset-name>
keySetDesc:<optional-keyset-description>
sourceId:<data-source-id>
```

The response from this endpoint includes a unique ID for the keyset. You will need this ID if you update the keyset from a CSV file.

For more information, see your API documentation.

API documentation is provided in your environment at this link: `https://<Self-Service Analytics-URL>/composer/swagger-ui.html`.

<h2 id="review-and-apply-a-keyset-as-a-visual-filter">
  Review and Apply a Keyset as a Visual Filter
</h2>

You can review and apply a keyset as a visual filter to visuals that use the same or different data sources. Visuals are limited to records containing values stored in the keyset. You can update a keyset at any time by uploading new values for the keyset.

<Note>
  To apply a keyset to a visual, the data source for the target visual must include a field storing the same data as the key field used for the keyset. The key field is defined when the keyset is created. See [Create a Keyset](#create-a-keyset).
</Note>

**Review and apply a keyset as a visual filter**

1. For the purposes of this procedure, suppose you want to list the planned sales for jewelry.Take a keyset containing a list of jewelry (see [Create a Keyset](#create-a-keyset)), and apply it to a bar chart showing planned sales by category.

   <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/planned-sales-category.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=f0a1ea0d558d5a89672be89637f706ff" alt="Shows your data as a bar chart" width="1908" height="800" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/planned-sales-category.png" />

2. Select the filter icon on the [visual](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters#apply-a-row-level-filter-to-a-visual-or-filter-snippet) or [dashboard](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters#apply-a-row-level-filter-to-a-dashboard) to access the appropriate filter sidebar.

   * To access the visual filter sidebar, select its filter icon (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=0a044ea0662c55e06133074a55d93cd9" alt="select the filter icon to open the filters sidebar and add or edit filters" width="17" height="17" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '17px', height: '17px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png" />) or select **Settings** from the [visual menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu) (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" />) and then select <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-filter.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=4b06f0c1f1b48c50da73f73672d5b1c6" alt="" width="20" height="21" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '21px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-filter.png" /> on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu).

   * To access the dashboard filter sidebar, select its filter icon (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-dash.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=68279f203a0950b32bfab88e7273d5ba" alt="" width="20" height="19" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '19px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-dash.png" />). The dashboard-level filter icon is available only when all the visuals are from the same data source.

   The Filters sidebar appears showing any filters that have been applied.

3. Select **Add Filter**.

4. Locate the data field in the Filters sidebar list that contains the same kind of data as the data in the keyset you want to use. In our example, it is Category.

   The Filters sidebar displays three tabs:

   * The **Value** tab allows you to select values for the filter.

   * The **Wildcard** tab allows you to specify a row-level wildcard filter for the visual.

   * The **Keyset** tab allows you to select a keyset for the filter or to upload a CSV file as a keyset.

     <Note>
       This example uses a non-numeric filter. See [Set a Numeric Field Filter](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters-attr#set-a-numeric-field-filter).
     </Note>

5. Select the **Keyset** tab. The keysets and saved filters defined in your environment are listed.

   <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sales-category.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=a7aa1dfaaa4911c5c99492b1e73b3abf" alt="Define your keyset values here" width="347" height="761" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sales-category.png" />

6. Select the keyset you want to apply. Details about the keyset appear on the Filters sidebar.

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/keyset-details.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=835ff2c3d3a539ada0170c433c642f78" alt="Review and edit your keyset values" width="350" height="760" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/keyset-details.png" />

   Sort the data in the keyset as needed by selecting the up and down arrows (<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/up-down-arrow.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=ac406f27618637435f3280b4663b79da" alt="" width="13" height="18" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '13px', height: '18px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/up-down-arrow.png" />) in the Preview area. This sort has no effect on the visual result set when the keyset is applied.

7. When you are finished setting your filter values, select **Continue** and examine your updates. If they are correct, select **Apply**.

   The visual is filtered by the keyset data.

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/jewelry-planned-sales.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=e9dedad6c41ee9f6ad283d8c77862b1b" alt="Your filtered sales data" width="1919" height="800" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/jewelry-planned-sales.png" />

   Select the **x** in the upper right corner of the Filters sidebar to close it.

<h2 id="delete-a-keyset">
  Delete a Keyset
</h2>

You can only delete a keyset if it is not used by any visual in the environment.

<Note>
  Keysets can only be deleted by the user account that created them or by any Self-Service Analytics user belonging to a group with the **Administer Dashboards** privilege. In addition, they can only be deleted if they are not used by any visual in the environment.
</Note>

**Delete a keyset**

1. Select the filter icon on the [visual](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters#apply-a-row-level-filter-to-a-visual-or-filter-snippet) or [dashboard](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters#apply-a-row-level-filter-to-a-dashboard) to access the appropriate filter sidebar.

   * To access the visual filter sidebar, select its filter icon (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=0a044ea0662c55e06133074a55d93cd9" alt="select the filter icon to open the filters sidebar and add or edit filters" width="17" height="17" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '17px', height: '17px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png" />) or select **Settings** from the [visual menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu) (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" />) and then select the filter (<img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-filter.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=4b06f0c1f1b48c50da73f73672d5b1c6" alt="" width="20" height="21" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '21px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-filter.png" />) icon on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu).

   * To access the dashboard filter sidebar, select its filter icon (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-dash.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=68279f203a0950b32bfab88e7273d5ba" alt="" width="20" height="19" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '19px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-dash.png" />). The dashboard-level filter icon is available only when all the visuals are from the same data source.

   The Filters sidebar appears showing any filters that have been applied.

2. Select **Add Filter**.

3. Locate and select the field in the Filters sidebar to which the keyset applies. A second page with a Keyset tab appears in the Filters sidebar.

4. Select the Keyset tab. The keysets defined in your environment that apply to the field you have selected are listed.

5. Select the delete icon (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/delete-open.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=02c9cbe530b9f34bd9a73851fdf499e2" alt="" width="16" height="18" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '16px', height: '18px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/delete-open.png" />) next to the keyset name. A warning dialog appears.

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/keyset-delete.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=3b5ec8c0981d1701ee29d0f6a1cc2bfe" alt="keyset warning dialog" width="392" height="113" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/keyset-delete.png" />

6. Select **Delete**. The keyset is deleted.
