> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage the Fields Work Areas

## Manage Fields

<Note>
  In this release, when your admin enables the Enhanced Experience user interface, you will see changes to workflows you may have used in previous releases. If you are running an earlier release or your admin has not enabled the new interface, see [Fields Tab (Earlier Releases)](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116424973-Manage-Fields#v25.3).
</Note>

Access the Fields tab for your source by selecting the Output icon in the [Source Creation](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-source-creation-tab) work area. You can manage your data using the Fields tab or Custom Metrics tab.

<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/sources/fields-tab-26-2.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=5855c14a790439bc4238896ae909d8fa" alt="use this work area to manage the visibility of fields and other information related to your data" width="804" height="641" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/sources/fields-tab-26-2.png" />

You can quickly and easily change the visibility of fields and custom metrics in this work area, or perform more management and settings changes, such as changing a field's **Label** by selecting the **Expand View** link to open a larger work area.

Use the Options menu to make changes to your source directly from the canvas. Use any of the options shown to **Upload Translation File**, **Update Field Capabilities**, **Add Derived Field**, **Add Custom Metric**, or **Add Hierarchy Field**.

<h3 id="expand-view-fields">
  Expand View - Fields
</h3>

When you expand the view of your fields or custom metrics into a larger work area, you can easily access the **Settings**, **Filter Values** (fields only), **Info**, and **Field Metadata** of a selected field to manage your fields data. Search fields, or use any of the options shown to **Upload Translation File**, **Update Field Capabilities**, **Add Derived Field**, or **Add Hierarchy Field**.

<img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/fields-exp-cmp-26-2.jpg?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=c4d7de9bda6c4e9cd96490addb5f3afe" alt="Use this work area to define how your data is formatted and used and perform bulk changes to your data layout" width="1290" height="615" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/fields-exp-cmp-26-2.jpg" />

<Note>
  Fields Metadata is not available for Custom Metrics.
</Note>

Manage your fields and custom metrics using any of the available panels discussed below.

* [Fields Table](#fields-table)

  * [Settings Panel - Fields Tab](#settings-panel-fields-tab)
  * [Filter Values Panel - Fields Tab](#filter-values-panel-fields-tab)
  * [Info Panel - Fields Tab](#info-panel-fields-tab)

* [Custom Metrics Table](#custom-metrics-table)

  * [Settings Panel - Custom Metrics Tab](#settings-panel-custom-metrics-tab)
  * [Info Panel - Custom Metrics Tab](#info-panel-custom-metrics-tab)

<h2 id="fields-table">
  Fields Table
</h2>

The Fields table lists all the fields in the records of the data source available in the Output you selected on the [Source Creation](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-source-creation-tab) tab. Use this work area to further configure them. To define the field metadata, 1,000 records are sampled.

<Note>
  Use the **Search** field to find a field by Label name.
</Note>

The following table describes the settings you can alter for individual data fields. To refresh your data source metadata, select the refresh button for Manual Refresh on the [Cache tab](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-global-settings-tab#cache-tab). See [Trigger Refresh Jobs](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/console#trigger-refresh-jobs) for more information.

<table>
  <thead>
    <tr>
      <th>Column</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>**Visible**</td>

      <td>
        By default, all fields are visible, and you can include data from these fields in your visuals. If you want to hide specific fields, select the toggle to hide the field. Hidden fields can be added to and used in derived fields and custom metrics, but not visuals. See [Hide Fields](#hide-fields).

        <br />

        If a hidden native field is the default metric for a new visual, another metric is used in its place.
      </td>
    </tr>

    <tr>
      <td>**Label**</td>
      <td>By default, the name of the field as defined in the data source. To change, edit the Label field in the Settings side panel.</td>
    </tr>

    <tr>
      <td>**Type**</td>
      <td>Shows the field type. Fields from your data source are **Native**. Derived fields are **Derived**.</td>
    </tr>

    <tr>
      <td>**Data Type**</td>

      <td>
        The data type for each field is defined, by default, by Self-Service Analytics and shown here.

        <br />

        If available, select **Convert** in the Data Details section of the Settings side panel to create a derived field of this data as another data type. Options include Time, Number, or Attribute.

        <br />

        In environments where alternate calendars are enabled, a new Time derived field based on the selected calendar is created. See [Fiscal Calendars](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/data-number-formatting#fiscal-calendars).
      </td>
    </tr>

    <tr>
      <td>**Actions**</td>

      <td>
        Shows what actions, if any, you can take for this field. You can only delete derived fields here.

        <br />

        <Note>
          If you try to delete a visual, filter snippet, dashboard, self service report, dashboard link, source, or source field, Self-Service Analytics displays an error message naming any objects dependent on the item you’re trying to delete. You can delete the item after you’ve removed the association from the dependent object. See [Fields Usage](#fields-usage).
        </Note>
      </td>
    </tr>
  </tbody>
</table>

<h3 id="settings-panel-fields-tab">
  Settings Panel - Fields Tab
</h3>

Select a field in the fields table to edit and update information for each field. Depending on the field selected, available options change. Select **Save** to save any changes you make here.

<table>
  <thead>
    <tr>
      <th>Setting</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>**Expression**</td>
      <td>The expression used to define this derived field. Select the edit <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/edit.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=e8c7d89552adf3d133e97050d5a2d000" alt="" width="19" height="20" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '19px', height: '20px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/edit.png" /> button to change.</td>
    </tr>

    <tr>
      <td>**Data Details**</td>

      <td>
        Depending on the Data Type of the field, different options are available you can adjust.

        <br />

        * Data Type: Convert to an available data type. The original field is not converted: a new derived field with the new data type is created. Data types that may be available are Time, Number, or Attribute.

        <br />

        * Default Aggregation: Select an available default aggregation type. For explanations, see [Metric Aggregation Functions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#metric-aggregation-functions).

        <br />

        * For numeric data types, select from: Sum, Avg, Min, Max, Count, or Distinct Count.
        * For attribute data types, select from Count or Distinct Count.

        <br />

        * Granularity: Select a default smallest increment level of time granularity to include in visuals. Valid granularity options are **Year**, **Quarter**, **Month**, **Week**, **Day**, **Hour**, **Minute**, **Second**, or **Millisecond**. You can edit a visual to include a larger granularity increment than the default for this field, but not a smaller increment.

        <br />

        * Time Zone:

        <br />

        * Select a time zone to present data in a specific time zone with the time zone labeled.

        <br />

        * Select **User Time Zone** to present data in user’s time zone, labeled.

        <br />

        * Select **Not Specified** to display time information with no time zone data label.

        <br />

        Your selection here also affects exported data.
      </td>
    </tr>

    <tr>
      <td>**Format**</td>

      <td>
        The number or time format for this field. Select the edit <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/edit.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=e8c7d89552adf3d133e97050d5a2d000" alt="" width="20" height="22" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '22px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/edit.png" /> button to change the format type and edit display details for field.

        <br />

        * Number field options: **Plain Number**, **Percentage**, **Money**, **Storage**, or **Scientific Notation**. See [Configure Number Formatting - Data Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/data-number-formatting).
        * Time field options: Adjust the display format of any available date or time field. See [Configure Date and Time Formatting - Data Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/data-number-formatting#configure-date-and-time-formatting-data-sources).
      </td>
    </tr>

    <tr>
      <td>**URL Formatting**</td>

      <td>
        Enable to display a hyperlink associated with this Attribute or Number field as a link in the Data Details table for a visual. When selected, the URL opens in a new browser tab.

        <br />

        Select the **Interpolated Expression** add icon <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/add.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=9a24b95d9385f23950764407d5e9111a" alt="add icon" width="16" height="16" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '16px', height: '16px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/add.png" /> and enter the link address, such as `https://www.website.com/${value}`.
      </td>
    </tr>

    <tr>
      <td>**Partition**</td>
      <td>If you are using Cloudera Impala, Apache Drill, Hive, or Spark SQL as your data source, the Partition section shows if fields within your source are partitioned. Enable to optionally adjust the Partition Field and Partition Function of the partition.</td>
    </tr>
  </tbody>
</table>

<h3 id="filter-values-panel-fields-tab">
  Filter Values Panel - Fields Tab
</h3>

Select a field in the fields table to define filter values for each field. Choose a static override option if you want to specify Custom Value and Range. Depending on the field selected, available options change. Select **Reset** to clear unsaved changes and return to previously saved settings. Select **Save** to save any changes you make here.

<table>
  <thead>
    <tr>
      <th>Source of Filter Values</th>
      <th>Setting</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>**Default**</td>

      <td />

      <td>
        Select to inherit values from the data source.

        <br />

        Select **Reset** to reset any changes you have made, even saved changes, to **Default**.
      </td>
    </tr>

    <tr>
      <td>**Dynamic Override**</td>

      <td />

      <td>
        Select values from predefined entities. Apply to Attribute, Number, or Time fields.

        <br />

        * Data Entity: Select an available data entity by name from the list.
        * Field: Select field.
        * Preview: Select the number of rows to preview (10-100).
      </td>
    </tr>

    <tr>
      <td>**Static Override**</td>

      <td />

      <td>
        Select to manually enter filter values.

        <br />

        You can enable **Custom Value**, **Custom Range**, or both. If the values you define are invalid, you can not save your settings.
      </td>
    </tr>

    <tr>
      <td />

      <td>Custom Range</td>

      <td>
        Enable to define a custom range from available values. Apply to Number and Time fields.

        <br />

        Adjust **Min** and **Max** to suit your needs. Applies to all visuals. These fields must defined.
      </td>
    </tr>

    <tr>
      <td />

      <td>Custom Value</td>

      <td>
        Enable to define custom values for this field at the source level. Apply to Attribute and Number fields.

        <br />

        * Enter a custom value or variable, then select **Add** to add the value. Repeat as needed. Select delete icon to delete a value or variable.
        * Alternatively, set no values or variables. Appropriate users can define values at the visual level.
      </td>
    </tr>
  </tbody>
</table>

<h3 id="info-panel-fields-tab">
  Info Panel - Fields Tab
</h3>

Select a field in the fields table to review information about or update the label for each field. Depending on the field selected, available options change. Select **Save** to save any changes you make here.

<table>
  <thead>
    <tr>
      <th>Setting</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>**Name**</td>

      <td>
        The name of the field as defined in the data from the data store. Unique.

        <br />

        When you add a derived field, the software generates the Name using information in the Label field. The Name must be unique; the software appends a number if needed.

        <br />

        <Note>
          This product supports underscores and periods in data store field Names. No other special characters or white spaces are supported. Names can start with a letter or an underscore, followed by letters, digits, underscores, and periods.
        </Note>
      </td>
    </tr>

    <tr>
      <td>**Label**</td>
      <td>The Label information for the field as defined in the data store, or that you define when you create a derived field. Edit as needed for use in your visuals and dashboards. 255 characters. The Label field does not need to be unique.</td>
    </tr>

    <tr>
      <td>**Data Entity Label**</td>
      <td>The name of the data entity source for this field.</td>
    </tr>
  </tbody>
</table>

<h3 id="field-metadata-fields-tab">
  Field Metadata - Fields Tab
</h3>

Select a field in the fields table to add, review, update contextual information for that field. Users with access to the source can see this information, and it can be consumed by artificial intelligence tools or other software you integrate into your environment. This information is exported when you export source, or dashboards and visuals information that

Add, update, edit, or delete a paired **Property** and **Value**. Select **Save** to save any changes you make here.

| Option or Setting | Description |
| - | - |
| Plus Sign Button **(+)** | Select to add a property and value pair for the selected field. |
| **Property** | The name of the property you want to add to the selected field. |
| **Value** | The value to attribute to this property for the field. |
| Delete Button **(-)** | Select to remove a property and value pair for the selected field. |

<h4 id="field-metadata-fields-tab-manage-field-metadata">
  Manage Field Metadata
</h4>

Optionally, add metadata at the field level stored as a keyed pair of Property and Value in your environment. Use in several ways:

* As information consumed by an integrated AI tool: for example, Simba Intelligence or other tool can read the information and interpret it without adding it to the visual.
* As internal information for users who can view the data in your source.

<img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/paired-values-meta-26-1.png?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=3fb5fe6a347a7e967be65c756d03086b" alt="Add Field Metadata work area" width="434" height="350" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/paired-values-meta-26-1.png" />

1. Select **Field Metadata** in the expanded view of your source.

2. Add a **Property** and **Value** pair to append to your data to add context for tools you use to explore and share your data.

3. Select the plus (**+**) icon to add another pair, or the minus (**-**) icon next to an existing pair to remove it.

4. Select **Save** to apply your changes.

   As needed, update or remove the fields you need.

The metadata you define is available using the API, and exported with the source (JSON format); when you move, share, and copy or export your source or visuals and dashboards that use that source to share with others.

API documentation is provided in your environment at this link: `https://<Self-Service Analytics-URL>/composer/swagger-ui.html`.

<h2 id="custom-metrics-table">
  Custom Metrics Table
</h2>

The Custom Metrics table lists custom metrics you have defined for the data and allows you to define others. You can also select **Add Custom Metric** from the **Options** menu to add a [custom metric](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/custom-metrics#create-and-modify-custom-metrics) to this table.

* When you create a new source, Volume is presented as a custom metric, using the **Count(\*)** expression. Edit or delete as needed to reflect your information as desired.
* When you upgrade from an older release, volume metrics for existing sources are converted to a custom metric.

<Note>
  Use the **Search** field to find a custom metric by Label name.
</Note>

<table>
  <thead>
    <tr>
      <th>Column</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>**Visible**</td>

      <td>
        By default, all the fields are selected and are visible. This means that you can visualize the data from these fields on your visuals. If you want to hide specific fields, select the toggle to hide the field. Hidden fields can be used in custom metrics. However, they cannot be used in dashboard visuals. See [Hide Fields](#hide-fields).

        <br />

        If a hidden native field is the default metric for a new visual, another metric is used in its place.
      </td>
    </tr>

    <tr>
      <td>**Label**</td>
      <td>The Label information for the field you define when you create a custom metric. To change, edit the Label field in the Settings side panel.</td>
    </tr>

    <tr>
      <td>**Type**</td>
      <td>Shows the field type. Custom metrics are always Custom Metric.</td>
    </tr>

    <tr>
      <td>**Data Type**</td>
      <td>Shows the data type. For custom metrics, this is always Number.</td>
    </tr>

    <tr>
      <td>**Actions**</td>
      <td>Shows what actions, if any, you can take for this field. Generally, you can only delete custom metrics.</td>
    </tr>
  </tbody>
</table>

<h3 id="settings-panel-custom-metrics-tab">
  Settings Panel - Custom Metrics Tab
</h3>

Select a field in the custom metrics table to edit and update information for each metric. Select **Save** to save any changes you make here.

| Setting | Description |
| - | - |
| **Expression** | The expression used to define this custom metric. Select the edit button to change. |
| **Format** | The number format for this field. Select the edit button to change the format type and edit display details for the format type. Options are **Plain Number**, **Percentage**, **Money**, **Storage**, or **Scientific Notation**. See [Configure Number Formatting - Data Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/data-number-formatting). |

<h3 id="info-panel-custom-metrics-tab">
  Info Panel - Custom Metrics Tab
</h3>

Select a field in the Custom Metrics table to review information about or update the label for each field. Depending on the field selected, available options may change. Select **Save** to save any changes you make here.

<table>
  <thead>
    <tr>
      <th>Setting</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>**Name**</td>

      <td>
        The name of the metric as you define during custom metric creation. Unique.

        <br />

        When you add a custom metric, the software generates the Name using information in the Label field. The Name must be unique; the software appends a number if needed.

        <br />

        <Note>
          supports underscores and periods in data store field Names. No other special characters or white spaces are supported. Names can start with a letter or an underscore, followed by letters, digits, underscores, and periods.
        </Note>
      </td>
    </tr>

    <tr>
      <td>**Label**</td>
      <td>The Label information for the field you define when you create a custom metric. Edit as needed use in your visuals and dashboards. 255 characters. The Label field does not need to be unique.</td>
    </tr>
  </tbody>
</table>

<h4 id="info-panel-custom-metrics-tab-manage-field-metadata">
  Manage Field Metadata
</h4>

Optionally, add metadata at the field level stored as a keyed pair of Property and Value in your environment. Use in several ways:

* As information consumed by an integrated AI tool: for example, Simba Intelligence or other tool can read the information and interpret it without adding it to the visual.
* As internal information for users who can view the data in your source.

<img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/paired-values-meta-26-1.png?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=3fb5fe6a347a7e967be65c756d03086b" alt="Add Field Metadata work area" width="434" height="350" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/paired-values-meta-26-1.png" />

1. Select **Field Metadata** in the expanded view of your source.

2. Add a **Property** and **Value** pair to append to your data to add context for tools you use to explore and share your data.

3. Select the plus (**+**) icon to add another pair, or the minus (**-**) icon next to an existing pair to remove it.

4. Select **Save** to apply your changes.

   As needed, update or remove the fields you need.

The metadata you define is available using the API, and exported with the source (JSON format); when you move, share, and copy or export your source or visuals and dashboards that use that source to share with others.

API documentation is provided in your environment at this link: `https://<Self-Service Analytics-URL>/composer/swagger-ui.html`.

<h2 id="hide-fields">
  Hide Fields
</h2>

By default, all fields in a data source are visible and available for use in [custom metrics](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/custom-metrics), [derived fields](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/derived-fields), [self service reports](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/ssr-manage), and in your dashboard visuals. However, there may be source fields, [derived fields](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/derived-fields), or [custom metrics](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/custom-metrics) in the data that you prefer to hide.

Hidden fields can be used in [custom metrics](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/custom-metrics), dashboard visuals, and [derived fields](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/derived-fields).

### When to Hide Fields

You can hide a field already used in a derived field, custom metric, or visual. The next time a user opens a visual that uses that hidden field, they are prompted to re-render the visual by selecting another available field.

<Note>
  In this release, when your admin enables the Enhanced Experience user interface, you will see changes to workflows you may have used in previous releases. If you are running an earlier release or your admin has not enabled the new interface, see [How to Hide a Field (Earlier Releases)](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701117118477-Hide-Fields#v25.3).
</Note>

### How to Hide a Field

Hide source fields, derived fields, or custom metrics using the Properties panel of a data source.

**Hide a field**

1. Make sure you are logged in as a user with the **Administer Sources** [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference), or a user with **read** and **write** [permission](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/ds-permissions) for the data source. Open the source you want to edit.

2. Select the Properties panel for this data source by selecting the **Output** icon in the work area. If you need a larger work area, select the **Expand View** link to open a larger work area.

3. To hide a field or derived field, disable (toggle off) the corresponding **Visible** toggle in the Fields table. By default, all included fields for a data source are enabled and visible.

4. To hide a custom metric, disable (toggle off) the corresponding **Visible** toggle in the Custom Metrics table. By default, all custom metrics for a data source are enabled and visible.

   <img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/cmp-field-25-4.jpg?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=7f53db1c76556ec4e98a6ac4314e8fb5" alt="use this work area to manage the visibility of fields and other information related to your data" width="635" height="800" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/cmp-field-25-4.jpg" />

5. Exit the source data configuration work area when you have finished defining field visibility.

## Upload a Translation File For a Source

Provide localization support by uploading metadata dictionaries for your data sources by uploading a translation file in CSV format for each data source you create. Use this translation file to define label translation for fields and custom metrics for your users in their preferred language.

<Note>
  In this release, when your admin enables the Enhanced Experience user interface, you will see changes to workflows you may have used in previous releases. If you are running an earlier release or your admin has not enabled the new interface, see [Upload or Replace a Translation File (Earlier Releases)](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116659853-Upload-a-Translation-File-For-a-Source#v25.3).
</Note>

### Translation File Prerequisites

* Build your metadata dictionary as a comma separated values file (.csv) as shown below, using appropriate Locale labels for each language.
* Include as many or as few of the fields as you need from your data source, in any order. Self-Service Analytics displays the appropriate translation with each included field in the language defined by the user's settings. If no translation is provided, the original field name is shown.
* Provide a translation entry for each language represented. If your file is missing a language entry for a field, Self-Service Analytics rejects the file upload.

```
Field Label,ua_UK,en_GB
city,місто,city
county,округ,county
zip code,поштовий індекс,postcode
date,дата,date
income bracket,рівень доходу,income range
product category,категорія продукту,product category
satisfaction,задоволення,satisfaction
year,рік,year
```

<Note>
  If you import an exported source that has an associated translation file, you must re-upload the translation for that source.
</Note>

### Upload or Replace a Translation File

**Upload a translation file**

1. Log in as a user with the **Administer Sources** [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference), or a user with **read** and **write** [permission](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/ds-permissions) for the data source.

2. Select the Output for your source, then select **Upload Translation File** from the Add menu. Self-Service Analytics prompts you to upload your file from your system.

   <img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/cmp-field-25-4-sm.jpg?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=01f89dbcc415b04b144ffad79eab041c" alt="Select Add or Configure to add a custom metric, upload a translation file, add a hierarchy field, or a derived field." width="635" height="380" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/cmp-field-25-4-sm.jpg" />

3. Browse to your file, then select **Open**. Self-Service Analytics returns a success message. Translated fields are indicated by the translation icon (<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/translation-symbol.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=ae1d461f5295314ca103fe324256787b" alt="" width="20" height="20" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '20px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/translation-symbol.png" />) in the appropriate table.

   <img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/translation-success-23-1.png?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=fc116788e3a8c8f6cdb2338ac6d9dca9" alt="the translation symbol indicates a translation is available for the field" width="576" height="181" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/translation-success-23-1.png" />

**Replace a translation file**

1. Log in as a user with the **Administer Sources** [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference), or a user with **read** and **write** [permission](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/ds-permissions) for the data source.
2. Select the Fields tab for the source, then select **Upload Translation File**. Self-Service Analytics prompts you to upload your file from your system.
3. Browse to your revised file, then select **Open**. Self-Service Analytics overwrites the existing metadata dictionary and returns a success message. Translated fields are indicated by the translation icon (<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/translation-symbol.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=ae1d461f5295314ca103fe324256787b" alt="" width="20" height="20" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '20px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/translation-symbol.png" />) in the appropriate table.

## Field Capabilities

When you create your source or create fields in a source, Self-Service Analytics defines default field capabilities for your data. You can adjust the predefined capabilities of native and derived fields on the Fields tab of your source, [enabling or disabling capabilities](#update-field-capabilities) as needed. If you update a source, any field capabilities you set remain unchanged.

<img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/bulk-update-cmp-25-4.png?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=a64ef4d853fbdc2e8f36261e91dcc62e" alt="search and filter your fields, then enable or disable options as needed, including Details, Filtering, Grouping, Metrics, Playing, and Raw Data" width="994" height="585" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/bulk-update-cmp-25-4.png" />

Use **Search** to find specific fields by **Label**, or use the provided filtering options to narrow the list of visible fields:

* Filter by data type: Show **All** data type fields: Attribute (**ABC**), Number (**1.23**) or Time (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/calendar.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=73e021b92ecc5133c711b9707be64b6e" alt="" width="20" height="20" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '20px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/calendar.png" />).
* Filter by type: **All**, **Native**, or **Derived**.

<Note>
  You can only update the fields you have made visible in this source.
</Note>

Select the toggle for any of the available options to enable or disable the field capabilities for that field. See [Update Field Capabilities](#update-field-capabilities).

<Note>
  If your source data does not contain enough data for a field capability, enabling or disabling it will have no effect on the field. For example, insufficient data can prevent display of details in detailed data views, even if the Details option is enabled.
</Note>

<h3 id="field-capabilities-options">
  Field Capabilities Options
</h3>

<table>
  <thead>
    <tr>
      <th>Capability</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>**Details**</td>

      <td>
        When enabled, the field is visible in detailed data views.

        <br />

        * **Native fields:** Enabled by default if **Raw Data** is not enabled for a field. If Raw Data is enabled, you can enable Details if needed.
        * **Derived fields:** Enabled by default.
      </td>
    </tr>

    <tr>
      <td>**Filtering**</td>

      <td>
        When enabled, you can filter data using this field in filters and filter snippets.

        <br />

        When disabled, you can not use this field in filters. You can use this field to filter data in filter snippets when you pair it with a Display Column. This also masks the data users see, and masks the data in exports of the data. See [Filter Data With Masked Fields](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/widgets/fltrsnp-ov#filter-data-with-masked-fields).

        <br />

        * **Native fields:** Enabled by default.
        * **Derived fields:** Enabled by default.

        <br />

        <Warning>
          Applied filter values that later have **Filtering** disabled to not automatically mask or hide those fields. You must recreate the filter that uses these values.
        </Warning>
      </td>
    </tr>

    <tr>
      <td>**Grouping**</td>

      <td>
        When enabled, the field can be included in grouping.

        <br />

        * **Native fields:** Enabled by default if a `GROUP_ONLY` is not defined for a field.
        * **Derived fields:** Enabled by default.

        <br />

        See [Using the Raw Data Capability](#using-the-raw-data-capability) for more information on using Grouping and Raw Data together.
      </td>
    </tr>

    <tr>
      <td>**Metrics**</td>

      <td>
        When enabled, metrics are provided for this field.

        <br />

        * **Native fields:** Enabled by default if the `GROUP_ONLY` flag is not defined for a field.
        * **Derived fields:** Enabled by default.
      </td>
    </tr>

    <tr>
      <td>**Playing**</td>

      <td>
        When enabled, the data can be played in the visual.

        <br />

        * **Native fields:** Enabled by default if a `PLAYABLE` is defined for a field.
        * **Derived fields:** Disabled by default.
      </td>
    </tr>

    <tr>
      <td>**Raw Data**</td>

      <td>
        When enabled, the data is displayed in table visuals and can be exported with the visual to CSV and XLSX formats, using the Raw Data export option in visuals and details menus.

        <br />

        When disabled, field data is hidden and not included in any raw data exports, including dashboard reports, and cannot be included in keysets.

        <br />

        See [Using the Raw Data Capability](#using-the-raw-data-capability) for more information.

        <br />

        * **Native fields:** Enabled by default.
        * **Derived fields:** Enabled by default.

        <br />

        Not supported by hierarchical fields.
      </td>
    </tr>
  </tbody>
</table>

<Note>
  Meta flags are defined by the connector for each field during source creation. The connector performs data sampling to define some technical details and create the flags. These flags are not visible in the user interface. Manage using `/api/sources/{sourceId}/fields`.
</Note>

<h4 id="using-the-raw-data-capability">
  Using the Raw Data Capability
</h4>

Use the **Raw Data** option to control the visibility of raw data for your fields. This allows you to prevent export or use of specific fields that may contain sensitive information. It's enabled by default; disable to prevent export, views, and use of data fields as needed.

<Note>
  If you disable Raw Data for a field used in an existing visual, the field remains visible in the visual, but cannot be exported with the visual in any format. Once you remove a field from a visual that has Raw Data disabled, you can not add it back in.
</Note>

<table>
  <thead>
    <tr>
      <th>Field Capability Options</th>
      <th>Field Behaviors</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>**Raw Data: Enabled**</td>

      <td>
        Fields are available for use and access in:

        <br />

        * The Details menu of all visuals, including Export options
        * Raw and Visual data exports to CSV and XLSX format for all visuals
        * Visual data exports to PDF and PNG for the raw data table visual
        * Dashboard exports to XLSX format
        * Scheduled dashboard reports for table visuals
        * Available when creating a keyset
      </td>
    </tr>

    <tr>
      <td>**Raw Data: Disabled**</td>

      <td>
        Fields are hidden from:

        <br />

        * The raw data table visual, and cannot be readded from the settings menu
        * The Details menu of all visuals, including Export options
        * Raw and Visual data exports to CSV and XLSX format for all visuals
        * Visual data exports to PDF and PNG for the raw data table visual
        * Dashboard exports to XLSX format
        * Scheduled dashboard reports for table visuals
        * Not visible when creating a new keyset

        <br />

        Keysets:

        <br />

        * Disabled data fields can still be used to filter by the full value of the field
        * You can filter a visual using existing keysets that use the disabled field

        <br />

        Calculation Builder:

        <br />

        * The field is hidden from the Calculation Builder for derived fields and custom metrics unless opened in the source editor
        * You can edit an existing derived field or custom metric that includes the hidden field
        * You can filter a visual using existing keysets that use the disabled field
      </td>
    </tr>

    <tr>
      <td>
        **Raw Data: Disabled**

        <br />

        **Grouping: Disabled**
      </td>

      <td>
        When Grouping and Raw Data is disabled on a field, the field is additionally hidden from:

        <br />

        * All other visuals
        * Visual data exports for all visuals to PDF and PNG formats
        * Dashboard exports for all visuals to PDF and PNG formats
        * Scheduled dashboard reports for all visuals
      </td>
    </tr>
  </tbody>
</table>

<Warning>
  To ensure a field is excluded from all exports, disable Details, Grouping, and Raw Data for that field. The field data can be exposed if Filtering capability is enabled. To prevent this, either turn off filtering, or hide the field but filter by its value by defining a custom value for the field. See [Filter Values Panel - Fields Tab](#filter-values-panel-fields-tab).
</Warning>

<h2 id="update-field-capabilities">
  Update Field Capabilities
</h2>

When you create your source or create fields in a source, Self-Service Analytics defines default field capabilities for your data. You can adjust the predefined capabilities of native and derived fields on the Fields tab of your source, enabling or disabling capabilities as needed.

<Note>
  In this release, when your admin enables the Enhanced Experience user interface, you will see changes to workflows you may have used in previous releases. If you are running an earlier release or your admin has not enabled the new interface, see [Update the field capabilities for your source (earlier releases)](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116297741-Update-Field-Capabilities).
</Note>

**Update the field capabilities for your source**

1. Access the Fields tab for your source.

2. Select the **Output**, then select **Update Field Capabilities** from the **Options** menu. The Bulk Update Field Capabilities work area opens.

   <img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/bulk-update-cmp-25-4.png?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=a64ef4d853fbdc2e8f36261e91dcc62e" alt="search and filter your fields, then enable or disable options as needed, including Details, Filtering, Grouping, Metrics, Playing, and Raw Data" width="994" height="585" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/bulk-update-cmp-25-4.png" />

   Use **Search** to find specific fields by **Label**, or use the provided filtering options to narrow the list of visible fields:

   * Filter by data type: Show **All** data type fields: Attribute (**ABC**), Number (**1.23**) or Time (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/calendar.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=73e021b92ecc5133c711b9707be64b6e" alt="" width="20" height="20" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '20px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/calendar.png" />).
   * Filter by type: **All**, **Native**, or **Derived**.

   <Note>
     You can only update the fields you have made visible in this source.
   </Note>

   Select the toggle for any of the available options to enable or disable the field capabilities for that field. See Manage the Fields Work Areas

3. Only visible fields are shown in this work area. **Search** for an individual field by name, or filter the fields by data type (attribute, numeric, date) or type (native, derived).

4. Enable or disable the field capabilities for all visible fields in the source. Capabilities include: **Details**, **Filtering**, **Grouping**, **Metrics**, **Playing**, and **Raw Data**. See [Field Capabilities Options](#field-capabilities-options).

5. **Save** your changes.

<h2 id="fields-usage">
  Fields Usage
</h2>

does not allow you to remove a field from a source definition if any objects rely on this field. For example, if your native field `field_1` is used in a derived field expression such as `year_to_time(field_1)`, you can not remove it from the source.

The table below is a list of objects where a field can be used.

| Object Type Referencing the Field | Cannot Delete from Source Configuration | Can Delete from Source Configuration |
| - | - | - |
| derived field | If used in derived fields. | |
| custom metric | If used in custom metrics. | |
| global settings > time controls | If used by global defaults, such as time controls. | |
| global settings | If used by global defaults, such as time controls or global filters. | |
| row security | If used in row security. | |
| column security | | If used in column security. |
| visual | If used by a visual. | |
| key set | If a key set exists for the data source. | |
| filter set | If a filter set exists for the data source. | |
| row level filters (dashboards and visuals) | If used in a row level filter. | |
| field link (cross-source link) | If used in a cross-source link as part of dashboard interactions. | |
| same source link | | If the same source link is in a publisher or subscriber link. |
| actions | If used in an action. | |
| partition configuration | If used in a partition configuration. | |
| join configuration | If used in a join configuration. | |

<Note>
  If you try to delete a visual, filter snippet, dashboard, self service report, dashboard link, source, or source field, Self-Service Analytics displays an error message naming any objects dependent on the item you’re trying to delete. You can delete the item after you’ve removed the association from the dependent object. See Manage the Fields Work Areas.
</Note>

## Source Field Migration

When you upgrade from an earlier version of Logi Composer to v7.10 or later, several field types in your existing sources are migrated and converted to supported field types. Self-Service Analytics no longer supports implicit field type conversions: when you change the field type for a field, you effectively create a new derived field. See [Create and Modify Derived Fields](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/derived-fields#create-and-modify-derived-fields).

<h3 id="field-type-conversion-previous-releases-to-current-release">
  Field Type Conversion: Previous Releases to Current Release
</h3>

Scenario: You have a `date_year` field defined as an integer in your original database.

* Logi Composer (previous releases):

  * `date_year` is defined as a number or integer (dependent on your version).
  * You set the `type` as Time with Custom Pattern `yyyy`.
  * Composer treats the field as a `time` field.

* Self-Service Analytics, on upgrade, will now have two fields for each affected field in your source.

  * Field 1: `date_year_original`. The Label text is appended with `Original`. The field type is set to `number` and the field is not visible (Visible toggle disabled in the Fields tab).
  * Field 2: `date_year` as in your original source. The Label text and other settings are unchanged. This is a derived field, using the expression `year_to_time(date_year_original)`

<Note>
  If you create a new data source that uses the `date_year` integer from your source, you can create a derived field to change the `number` into `time`, using the expression `year_to_time(date_year)`.
</Note>

Possible field type conversions and limitations performed on upgrade are listed in table below. This is not an all-inclusive list:

<table>
  <thead>
    <tr>
      <th>Data Type conversion</th>
      <th>Derived Field Expression</th>
      <th>Requires Derived Field Support</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>ATTRIBUTE to NUMBER</td>
      <td>`text_to_num(field_name)`</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td>ATTRIBUTE to TIME</td>
      <td>`text_to_time(field_name, 'pattern')`</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td>NUMBER to TIME</td>

      <td>
        `year_to_time(date_year)`

        <br />

        `ms_to_time(date_milliseconds)`

        <br />

        `unix_time_to_time(date_seconds)`
      </td>

      <td>No</td>
    </tr>

    <tr>
      <td>NUMBER to ATTRIBUTE</td>
      <td>`num_to_text(field_name)`</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td>TIME to NUMBER</td>
      <td>`time_to_unix_time(field_name)`</td>
      <td>Yes</td>
    </tr>
  </tbody>
</table>
