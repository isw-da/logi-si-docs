---
title: "Field Capabilities"
id: 34932887622285
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932887622285-Field-Capabilities
updated_at: 2026-05-26T22:09:45Z
---

# Field Capabilities

# Field Capabilities

When you create your source or create fields in a source, Logi Composer defines default field capabilities for your data. You can adjust the predefined capabilities of native and derived fields on the Fields tab of your source, [enabling or disabling capabilities](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932907558541-Update-Field-Capabilities) as needed. If you update a source, any field capabilities you set remain unchanged.

![search and filter your fields, then enable or disable options as needed, including Details, Filtering, Grouping, Metrics, Playing, and Raw Data](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167271208205 "Bulk Update Field Capabilities work area")

Use **Search** to find specific fields by **Label**, or use the provided filtering options to narrow the list of visible fields:

* Filter by data type: Show **All** data type fields: Attribute (**ABC**), Number (**1.23**) or Time (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167315557773)).
* Filter by type: **All**, **Native**, or **Derived**.

**Note:** 
You can only update the fields you have made visible in this source.

Select the toggle for any of the available options to enable or disable the field capabilities for that field. See [Update Field Capabilities](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932907558541-Update-Field-Capabilities).

**Note:** 
If your source data does not contain enough data for a field capability, enabling or disabling it will have no effect on the field. For example, insufficient data can prevent display of details in detailed data views, even if the Details option is enabled.

## Field Capabilities Options

| Capability | Description |
| --- | --- |
| **Details** | When enabled, the field is visible in detailed data views.   * **Native fields:** Enabled by default if **Raw Data** is not enabled for a field. If Raw Data is enabled, you can enable Details if needed. * **Derived fields:** Enabled by default. |
| **Filtering** | When enabled, you can filter data using this field in filters and filter snippets.  When disabled, you can't use this field in filters. You can use this field to filter data in filter snippets when you pair it with a Display Column. This also masks the data users see, and masks the data in exports of the data. See [Filter Data With Masked Fields](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932973019789-Filter-Data-With-Masked-Fields).   * **Native fields:** Enabled by default. * **Derived fields:** Enabled by default.   **Important:** Applied filter values that later have **Filtering** disabled to not automatically mask or hide those fields. You must recreate the filter that uses these values. |
| **Grouping** | When enabled, the field can be included in grouping.   * **Native fields:** Enabled by default if a `GROUP_ONLY` is not defined for a field. * **Derived fields:** Enabled by default.   See [Using the Raw Data Capability](#raw_data) for more information on using Grouping and Raw Data together. |
| **Metrics** | When enabled, metrics are provided for this field.   * **Native fields:** Enabled by default if the `GROUP_ONLY` flag is not defined for a field. * **Derived fields:** Enabled by default. |
| **Playing** | When enabled, the data can be played in the visual.   * **Native fields:** Enabled by default if a `PLAYABLE` is defined for a field. * **Derived fields:** Disabled by default. |
| **Raw Data** | When enabled, the data is displayed in table visuals and can be exported with the visual to CSV and XLSX formats, using the Raw Data export option in visuals and details menus.  When disabled, field data is hidden and not included in any raw data exports, including dashboard reports, and cannot be included in keysets.  See [Using the Raw Data Capability](#raw_data) for more information.   * **Native fields:** Enabled by default. * **Derived fields:** Enabled by default.   Not supported by hierarchical fields. |

**Note:** Meta flags are defined by the connector for each field during source creation. The connector performs data sampling to define some technical details and create the flags. These flags are not visible in the user interface. Manage using `/api/sources/{sourceId}/fields`.

### Using the Raw Data Capability

Use the **Raw Data** option to control the visibility of raw data for your fields. This allows you to prevent export or use of specific fields that may contain sensitive information. It's enabled by default; disable to prevent export, views, and use of data fields as needed.

**Note:** 
If you disable Raw Data for a field used in an existing visual, the field remains visible in the visual, but cannot be exported with the visual in any format. Once you remove a field from a visual that has Raw Data disabled, you can't add it back in.

| Field Capability Options | Field Behaviors |
| --- | --- |
| **Raw Data: Enabled** | Fields are available for use and access in:   * The Details menu of all visuals, including Export options * Raw and Visual data exports to CSV and XLSX format for all visuals * Visual data exports to PDF and PNG for the raw data table visual * Dashboard exports to XLSX format * Scheduled dashboard reports for table visuals * Available when creating a keyset |
| **Raw Data: Disabled** | Fields are hidden from:   * The raw data table visual, and cannot be readded from the settings menu * The Details menu of all visuals, including Export options * Raw and Visual data exports to CSV and XLSX format for all visuals * Visual data exports to PDF and PNG for the raw data table visual * Dashboard exports to XLSX format * Scheduled dashboard reports for table visuals * Not visible when creating a new keyset   Keysets:   * Disabled data fields can still be used to filter by the full value of the field * You can filter a visual using existing keysets that use the disabled field   Calculation Builder:   * The field is hidden from the Calculation Builder for derived fields and custom metrics unless opened in the source editor * You can edit an existing derived field or custom metric that includes the hidden field * You can filter a visual using existing keysets that use the disabled field |
| **Raw Data: Disabled**  **Grouping: Disabled** | When Grouping and Raw Data is disabled on a field, the field is additionally hidden from:   * All other visuals * Visual data exports for all visuals to PDF and PNG formats * Dashboard exports for all visuals to PDF and PNG formats * Scheduled dashboard reports for all visuals |

**Important:** 
To ensure a field is excluded from all exports, disable Details, Grouping, and Raw Data for that field. The field data can be exposed if Filtering capability is enabled. To prevent this, either turn off filtering, or hide the field but filter by its value by defining a custom value for the field. See [Filter Values Panel - Fields Tab](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932906721933-Manage-Fields#ft03).
