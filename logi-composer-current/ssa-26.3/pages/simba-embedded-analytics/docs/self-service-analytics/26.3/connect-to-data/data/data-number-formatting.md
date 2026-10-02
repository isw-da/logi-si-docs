> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Configure Number Formatting - Data Sources

As a user with [data source privileges](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference), configure number formats for Number fields in a data source at creation, or later when you edit an existing source. This defines the default format for number fields as displayed in visuals, data details of visuals, and sample format fields for consistency across your organization.

There are three places to control the display of numbers in a data source.

* Setting the locale for users to display correct formats, based on a user's geographical location. For example, users based in the United States and users based in Italy would see different currency formats due to the local formatting of the fields. To define the location settings for users within your environment, ask your administrator or see [Specify A User's Regional Settings](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#specify-a-user-s-regional-settings).

* Configuring the formats for number fields in a data source configuration, as described in the rest of this topic. Bear in mind that defining number formats depends on the region (location) settings configured for your environment.

* Finally, you can [enable users to override the formatting](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-interactivity) you have defined at the data source and for most visuals at the visual level. Find more visual formatting information in the following topics:

  * [Configure Date and Time Formatting](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/vis-number-formatting#configure-date-and-time-formatting)
  * [Number and Date Formatting for Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/vis-number-formatting)
  * [Format Time Table Data Using the Table Context Menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/rdt#format-time-table-data-using-the-table-context-menu)
  * [Format Numeric Table Data Using the Table Context Menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/rdt#format-numeric-table-data-using-the-table-context-menu)
  * [Available Visual Types](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/available-visual-types)

**Specify the format for number fields in a data source configuration**

1. Log in as a user with the **Administer Sources** or **Create New Data Sources** [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference), or write permission for this source.

2. Select the **Source** card on your home page or **Data Sources** from the main menu. The **Sources** work area appears.

3. Edit the appropriate data source configuration and access the [**Fields** tab](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-fields-tab) of the data source.

4. Locate the number field you want to modify. The **Data Type** column on the **Fields** tab must define the field as a **Number** field.

5. In the sidebar menu, select the settings (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-chtsettings.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=74af55ee44cca52b9f7f4ae157440a81" alt="Select the settings icon on the sidebar menu to open settings options" width="28" height="33" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '28px', height: '33px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-chtsettings.png" />) button to open the **Settings** work area. Select the edit (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/edit4gry.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=87563143361325e376add708486db9b2" alt="" width="24" height="24" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '24px', height: '24px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/edit4gry.png" />) button in the **Format** work area to edit the date and time format for this field.

   <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/connectors/format-dialog-num-source-23-1.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=1bbe9040205d02073e55374ff39fe4ae" alt="Update the format of your number field here" width="381" height="396" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/connectors/format-dialog-num-source-23-1.png" />

6. Select one of the following number formats in the drop-down list in the Number Format box. The other fields on the Format dialog change based on the number format you select.

   * **Plain Number**: Select this format to display the field as plain number values. Additional format information you can select includes:

     | Format Option | Description |
     | - | - |
     | Unit Multiple | Select the unit of measure you want to use for the field from the drop-down list. Valid values are **None**, **Thousands (K)**, **Millions (M)**, **Billions (B)**, and **Trillions (T)**. The unit multiple is used in visuals. For example, a value of 1,500,000 would show as 1.5M in visuals. |
     | Decimal Place | Specify the number of decimal places used in the data. |
     | Negative Display | Select the desired negative value format from the drop-down list. Valid values are the dash (-) in front of a negative value or parentheses surrounding negative values. For example, value of negative 30 could show as -30 or (30) in visuals. |
     | Use 1000 Separator | If you want commas used to separate number values into thousands, millions, billions, and trillions, check the **Use 1000 Separator** box. For example, if this box is checked, 2500 appears as 2,500 in visuals. |

   * **Percentage**: Select this format to display the field as percentage values. Additional format information you can select includes:

     | Format Option | Description |
     | - | - |
     | Decimal Place | Specify the number of decimal places used in the data. |
     | Negative Display | Select the desired negative value format from the drop-down list. Valid values are the dash (-) in front of a negative value or parentheses surrounding negative values. For example, value of negative 30.25 percent could show as -30.25% or (30.25%) in visuals. |
     | Use 1000 Separator | If you want commas used to separate number values into thousands, millions, billions, and trillions, check the **Use 1000 Separator** box. |

   * **Money**: Select this format to display the field as currency values. Additional format information you can select includes:

     | Format Option | Description |
     | - | - |
     | Symbol | Select the currency symbol you want used for money values in visuals. |
     | Unit Multiple | Select the unit of measure you want to use for the field from the drop-down list. Valid values are **None**, **Thousands (K)**, **Millions (M)**, **Billions (B)**, and **Trillions (T)**. The unit multiple is used in visuals. For example, a value of 1,500,000 would show as 1.5M in visuals. |
     | Decimal Place | Specify the number of decimal places used in the data. |
     | Negative Display | Select the desired negative value format from the drop-down list. Valid values are the dash (-) in front of a negative value or parentheses surrounding negative values. For example, value of negative 30 dollars and 25 cents could show as -\$30.25 or (\$30.25) in visuals. |
     | Use 1000 Separator | If you want commas used to separate number values into thousands, millions, billions, and trillions, check the **Use 1000 Separator** box. |

   * **Storage**: Select this format to display the field as computer storage values. Additional format information you can select includes:

     | Format Option | Description |
     | - | - |
     | Unit Multiple | Select the unit of measure you want to use for the field from the drop-down list. Valid values are **Bytes (B)**, **Kilobytes (KB)**, **Megabytes (MB)**, **Gigabytes (GB)**, **Terabytes (TB)**, **Petabytes (PB)**, and **Exabytes (EB)**. The unit multiple is used in visuals. For example, a value of 950 kilobytes would show as 950KB in visuals. |
     | Decimal Place | Specify the number of decimal places used in the data. |

   * **Scientific Notation**: Select this format to display the field as scientific decimals. Additional format information you can select includes:

     | Format Option | Description |
     | - | - |
     | Decimal Place | Specify the number of decimal places used in the data. |

7. Select **Apply** to apply to apply your changes, then **Save** to save your changes.

<h2 id="configure-date-and-time-formatting-data-sources">
  Configure Date and Time Formatting - Data Sources
</h2>

As a user with [data source privileges](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference), configure date and time for Time fields in a data source at creation, or later when you edit an existing source. This defines the default format for time fields as displayed in visuals, data details of visuals, and sample format fields for consistency across your organization.

There are three places to control the format of date and time information.

* Set the locale for users to display the appropriate order of fields, based on a user's geographical location. For example, users based in the United States and users based in Italy see different date order formats due to the local formatting of the fields. To define the location settings for users within your environment, ask your administrator or see [Specify A User's Regional Settings](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#specify-a-user-s-regional-settings).

* Configure the formats for Time fields in a data source configuration, as described in the rest of this topic. The order dates and times are presented in depend on the region (location) settings for your environment: you're changing the format of each time or date field to suit your organization's needs.

* Finally, you can [enable users to override the formatting](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-interactivity) you have defined at the data source and for most visuals at the visual level. Find more visual formatting information in the following topics:

  * [Configure Date and Time Formatting](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/vis-number-formatting#configure-date-and-time-formatting)
  * [Number and Date Formatting for Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/vis-number-formatting)
  * [Format Time Table Data Using the Table Context Menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/rdt#format-time-table-data-using-the-table-context-menu)
  * [Format Numeric Table Data Using the Table Context Menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/rdt#format-numeric-table-data-using-the-table-context-menu)
  * [Available Visual Types](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/available-visual-types)

<Note>
  If you change the format for dates and times for a field used by current visuals in your data source, the formats used in the visual reflect those changes. If you adjust the granularity of a field in your data source, the change is reflected in the granularity modal of the visual after the change.
</Note>

**Specify the format for Time fields in a data source configuration**

1. Log in as a user with the **Administer Sources** or **Create New Data Sources** [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference), or write permission for this source.

2. Select the **Source** card on your home page or **Data Sources** from the main menu.

3. Select to edit the appropriate data source configuration, and switch to the [**Fields** tab](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-fields-tab).

4. Locate the time field you want to modify. The **Data Type** column on the **Fields** tab must define the field as a **Time** field.

5. In the Settings sidebar menu, select the edit (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/edit2.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=d3604bc03d607058dd859e1c7bd373ff" alt="" width="24" height="23" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '24px', height: '23px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/edit2.png" />) button to open the **Format** work area.

   <img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/date-time-format-options-83.png?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=c5d512a5dbad1d79dc9fe56a90097e20" alt="Set the format options for your data source date and time" width="340" height="912" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/date-time-format-options-83.png" />

6. The changes you make are reflected in the **Sample Date** preview field.

7. When you are finished formatting your date and time values, select **Apply** and examine your updates. If they are correct, select **Save** to save these changes to the source.

<h2 id="configure-date-and-time-fields">
  Configure Date and Time Fields
</h2>

You can use number and attribute fields as time fields by creating a derived field to use as time data. See [Convert Attributes to Time Fields in Data Source Field Specifications](#convert-attributes-to-time-fields-in-data-source-field).

## Supported Date and Time Formats

You can use number and attribute fields as time fields by creating a derived field to use as time data. See [Convert Attributes to Time Fields in Data Source Field Specifications](#convert-attributes-to-time-fields-in-data-source-field).

<h2 id="convert-attributes-to-time-fields-in-data-source-field">
  Convert Attributes to Time Fields in Data Source Field Specifications
</h2>

If your data contains time-related fields (attributes) that are not stored in a recognized time format, you can convert the fields to time fields using the [Fields](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-fields-tab) tab of the [data source configuration](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview). As long as any string field contains date or time data, you change it to a time pattern recognized by Self-Service Analytics.

<Note>
  The process described here is **not** the recommended process. Instead, insightsoftware recommends that you convert the data using a derived field, as described in [Convert Attributes to Time Fields Using Derived Fields](#convert-attributes-to-time-fields-using-derived-fields).
</Note>

Self-Service Analytics uses Java's SimpleDateFormat for time conversions. See [SimpleDateFormat](https://docs.oracle.com/javase/7/docs/api/java/text/SimpleDateFormat.html).

<Note>
  Group functionality does **not** work for fields for which the type is manually set to **Time**. You cannot specify these fields as the Group, Group By, or Trend fields for a visual. You **can** use these fields in filters and apply them as filters on the time bar. However, you may find that the results shown in your visual are incorrect. This may happen because the manually configured time formats are different and, consequently, not in lexicographic order. For example, suppose you have two strings:
</Note>

* String `20230801` (August 1, 2023) matches the time format `yyyyMMdd`.
* String `08012024` (August 1, 2024) matches the time format `MMddyyyy`.

When filtering time data by these fields, Self-Service Analytics treats the time values as numbers. So, when filtered in ascending order, 08012024 will sort before 20230801, which is not correct (August 1, 2024 occurred after August 1, 2023, not before). The resulting visual will not be correct.

<Note>
  In this release, when your admin enables the Enhanced Experience user interface, you will see changes to workflows you may have used in previous releases.
</Note>

**Convert an attribute field to a time field as a derived field in your data source configuration**

1. Make sure you are logged in as an administrator.

2. Select the **Sources** card on your home page or **Data Sources** from the main menu. The [Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#data-sources-page) page appears.

3. In the sources table on the [Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#data-sources-page) page, locate and select the data source configuration you want to edit.

4. Select the [Fields](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-fields-tab) tab.

5. Locate and select the time field (Data Type: Attribute) in the list of fields.

6. Select **Convert** in the Data Type area of the Settings tab for the field and select **Convert to Time**.<br /><img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/7.9-date-time-convert-ds.png?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=2f4f2567167808e67c9b42228e319411" alt="" width="253" height="600" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/7.9-date-time-convert-ds.png" />

7. Rename the field in the **Label** field, and define time granularity in the **Origin Field Format**.<br /><img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/7.9-attribute-to-time-conversion.png?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=ec6052f558cba4ad7aa8eb416d9b19d6" alt="" width="448" height="329" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/7.9-attribute-to-time-conversion.png" />

   Valid time parts include:

   * YYYY - four digit year
   * MM - two digit month
   * DD - two digit day
   * HH - two digit 24-hour format
   * MI - two digit minute
   * SS - two digit seconds
   * MS - two digit milliseconds

   <Note>
     The information returned is limited by the information available in the original field. For example, if a field's data is stored in hours, you will get values up to the hour level. If you request granularity not available, zeros are returned for information not available, for example, 0 minutes, 0 seconds, and 0 milliseconds.
   </Note>

8. When your changes are complete, select **Save** create the derived field.

**Convert a number field to a time field as a derived field in your data source configuration**

1. Make sure you are logged in as an administrator.

2. Select the **Source** card on your home page or **Data Sources** from the main menu. The [Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#data-sources-page) page appears.

3. In the sources table on the [Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#data-sources-page) page, locate and select the data source configuration you want to edit.

4. Select the [Fields](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-fields-tab) tab.

5. Locate and select the time field (Data Type: Number) in the list of fields.

6. Select **Convert** in the Data Type area of the Settings tab for the field and select **Convert to Time**.<br /><img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/num-time-convert-710.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=ef237bc985116219c6d1c369d4e85e91" alt="" width="340" height="769" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/num-time-convert-710.png" />

7. Rename the field in the **Label** field, and select an available time granularity in the **Origin Field Format**.<br /><img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/num-time-convert-2-710.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=747bc76d7f32693f7f2e669c6c9afb0c" alt="" width="447" height="288" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/num-time-convert-2-710.png" />

   Valid time parts include:

   * YYYY - four digit year
   * MM - two digit month
   * DD - two digit day
   * HH - two digit 24-hour format
   * MI - two digit minute
   * SS - two digit seconds
   * MS - two digit milliseconds

   <Note>
     The information returned is limited by the information available in the original field. For example, if a field's data is stored in hours, you will get values up to the hour level. If you request granularity not available, zeros are returned for information not available, for example, 0 minutes, 0 seconds, and 0 milliseconds.
   </Note>

8. When your changes are complete, select **Save** create the derived field.

<h2 id="convert-attributes-to-time-fields-using-derived-fields">
  Convert Attributes to Time Fields Using Derived Fields
</h2>

If your data contains time-related fields (attributes) that are not stored in a recognized time format, you can convert them to time fields using a [derived field](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/derived-fields). After the derived field is defined, you can use it instead of the original attribute in your visuals. This is the preferred method because the data in the derived field is constructed as data is read from the data store.

**Convert an attribute field to a time field in a derived field**

1. Log in as an administrator or user with the ability to modify a data source configuration.
2. Start creating a derived field as described in [Create and Modify Derived Fields](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/derived-fields#create-and-modify-derived-fields).
3. Use the `TEXT_TO_TIME` function in a [row-level expression](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#row-level-expressions) in the derived field to convert your field to a time field. See [Text Functions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#text-functions).
4. Test and save the derived field. See [Create and Modify Derived Fields](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/derived-fields#create-and-modify-derived-fields).

## Timezone Conversion for Users

Displaying the source data in dashboards and visualizations in the timezone of individual users instead of the default timezone stored at the source. Additionally, you can convert a `TIME` field to a custom timezone.

<Danger>
  If you are upgrading from an earlier version of Self-Service Analytics, this may be a breaking change: the introduction of the system attribute `User.timeZone` may cause a conflict if you used this as a custom attribute. See [Upgrade Workflow](#upgrade-workflow).
</Danger>

The functionality is available in the following data sources and for the data stored in the UTC timezone:

* MS SQL
* Snowflake
* MongoDB
* BigQuery
* Hive
* SparkSQL
* Impala
* PostgreSQL
* Redshift

### Enable `TIME` Conversion To User Timezones

Before you convert a `TIME` field for use by users, define their timezone in user regional settings. Next, convert the `TIME` field in the source.

<h4 id="define-a-user-s-timezone">
  Define a User's Timezone
</h4>

1. Log in as a system administrator or a user who has been assigned to a group with [group management privileges](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference).

   If the user name you log in with is also associated with other tenants, verify that the correct tenant is selected. See [Switch Tenants](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/acct-manage#switch-tenants).

2. Select **Users** (formerly *Users and Groups*) from the Administration menu. The Users work area appears, listing all defined users in this tenant.

3. Select a user, then select the **Regional Settings** tab.

4. Select the **Time Zone** for the user from the options available in the drop-down selector.

5. Select **Save** to save the user

#### Convert a `TIME` Field of a Source

When you convert field, your software creates a derived field that includes the `User.timeZone` system attribute used as an interpolated value, for example `to_timezone(TIME_field, '${User.timeZone|UTC}'))`. Use the created derived field in dashboards and visualizations. The data will be recalculated using the account of each individual user with the custom timezone.

1. Log in as a user with the **Administer Sources** [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference), or a user with **read** and **write** [permission](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/ds-permissions) for the data source.
2. Select **Data Sources** from the main menu. The [Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#data-sources-page) page appears.
3. Select a source to open it, then select a time field in the **Fields** tab.
4. Select the **Settings**sidebar menu, then select **Convert** and the **Convert to User Timezone** option to convert the data type. A field conversion modal window opens.
5. In the Time to Time Zone Conversion work area, define a **Label** for the newly created field, then select **User Time Zone** for the Time Zone field if not already selected.
6. Select **Save** to create the new field.

<h4 id="alternative-convert-a-timezone-once-using-a-function">
  Alternative: Convert a Timezone Once Using a Function
</h4>

You can convert a field with the `TIME` data type into a selected timezone manually using the `to_timezone` function. Specify the function as shown below to return static timezone conversion.

| Syntax | Example | Use Case |
| - | - | - |
| `to_timezone(TIME_field, 'IANA timezone identifier')` | `to_timezone(TIME_field, 'Europe/Kyiv')` | Converts a field `TIME_field` from its UTC stored timezone to the selected timezone, `Europe/Kyiv`. |

<Warning>
  Conversion is available only for `TIME` fields stored in the UTC timezone at the data source. Conversions performed on the data stored in a custom timezone may be inaccurate.
</Warning>

<h3 id="upgrade-workflow">
  Upgrade Workflow
</h3>

If you are upgrading from an earlier version of Self-Service Analytics, this may be a breaking change: the introduction of the system attribute `User.timeZone` may cause a conflict if you used this as a custom attribute.

When you upgrade to the latest version of Self-Service Analytics this feature triggers the following changes:

* Custom user attributes you manually created with the name the `User.timeZone` in earlier Logi Composer versions (23.2 and earlier) are automatically converted to the system attributes if their value corresponds to the IANA timezone standard ISO 8601 (for example, `‘Europe/Kyiv’, ‘UTC+5’`).
* All custom user attributes `User.timeZone` that do not correspond to the IANA timezone standard are removed.

To ensure a smooth upgrade process, select an upgrade workflow ahead of updating Self-Service Analytics depending on your needs:

* If you want to start using your custom attribute `User.timeZone` for timezone conversion purposes, the attribute will be automatically changed to the system value at upgrade. To ensure this takes place, verify before upgrade that the values of the attribute are provided in IANA format before you upgrade Self-Service Analytics.
* If you want to preserve your custom attribute for other purposes, we recommend renaming the attribute before you upgrade Self-Service Analytics. For example, change `User.timeZone` to `User.timeZone_custom`. do not change the value of the attributes before running the upgrade script.

### API Changes

The APIs in `/api/users` has been expanded to include the `"timeZone": "string"` parameter. This displays the user's timezone formatted as an IANA timezone identifier, ISO 8601 (for example, "Europe/Kyiv"). The default value is `UTC`.

<Warning>
  `User.timeZone` is now a reserved system attribute to support this feature. See [Upgrade Workflow](#upgrade-workflow) for alternative approaches.
</Warning>

#### Payload Changes

<h5 id="logi-composer-v23-2-and-earlier">
  Logi Composer v23.2 and earlier:
</h5>

```json theme={null}
{ "id": "string", "fullname": "string", "email": "string", "accountId": "string", "name": "string", "password": "string", "localeSettingsId": "string", "languageLocaleId": "string" }
```

<h5 id="logi-composer-v23-3-and-later">
  Logi Composer v23.3 and later:
</h5>

```json theme={null}
{ "id": "string", "fullname": "string", "email": "string", "accountId": "string", "name": "string", "password": "string", "localeSettingsId": "string", "languageLocaleId": "string", "timeZone": "Europe/Kyiv" }
```

<h2 id="fiscal-calendars">
  Fiscal Calendars
</h2>

<Note>
  Fiscal Calendars functionality is disabled by default. To enable, [contact technical support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support) for assistance.
</Note>

<Warning>
  This is an experimental feature.
</Warning>

Use fiscal calendars in your environment to view your data based on a calendar system you define in your environment. Use the REST API endpoint `/api/calendars` to define one or more fiscal calendars to use in your sources.

API documentation is provided in your environment at this link: `https://<Self-Service Analytics-URL>/composer/swagger-ui.html`.

Once defined, you can assign a fiscal calendar for use in specific data sources and convert a time field into a new a derived field you can use as a time field in the data source.

* [Define a Fiscal Calendar](#define-a-fiscal-calendar)
* [Use a Fiscal Calendar](#use-a-fiscal-calendar)

<h2 id="define-a-fiscal-calendar">
  Define a Fiscal Calendar
</h2>

<Note>
  Fiscal Calendars functionality is disabled by default. To enable, [contact technical support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support) for assistance.
</Note>

<Warning>
  This is an experimental feature.
</Warning>

You can define multiple fiscal calendars for use in your environment, enabling your users to create dashboards and visuals that reflect data as structured in your preferred calendar time frame.

### Create a Fiscal Calendar

Administrators and users who are assigned to a group with the [Administer Calendars privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference) can use the REST API endpoint `/api/calendars` to define one or more fiscal calendars to define calendars for your users.

API documentation is provided in your environment at this link: `https://<Self-Service Analytics-URL>/composer/swagger-ui.html`.

When you create a fiscal calendar, you can define which month of your quarters is the longest month, and optionally shift the month your year begins. Send an array for the **CalendarResource** `type` as `MONTH_SHIFT`, `FISCAL_445`, or include both.

The name you select for a calendar is displayed in the user interface.

**Set the first month of your fiscal year**

If you optionally include and define a `MONTH_SHIFT`, use an integer value ranging from `-11` to `11` to set the start month of your fiscal year. Do not use `0`: it is an invalid selection.

* For February of the previous calendar year, use `-11`.
* For November of the current calendar year, use `11`.
* If no `MONTH_SHIFT` is provided, the default start month of the year is January.

**Set the five week month of your fiscal year**

When you define the fiscal calendar, you can set which month of the quarters will be five weeks long using **quarterType**.

* `QUARTER_445_WEEKS` - the last month of each quarter is the five week month.
* `QUARTER_454_WEEKS` - the middle month of each quarter is the five week month.
* `QUARTER_544_WEEKS` - the first month of each quarter is the five week month.

There are several more settings used to define your fiscal calendar. See the REST API for more information.

Once you have created one or more fiscal calendars, users who can create and update sources can [select appropriate calendars](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-global-settings-tab#other-settings) to use for a source, and define a derived field **Time (FISCAL)** field that uses a selected calendar.

See [Use a Fiscal Calendar](#use-a-fiscal-calendar).

<h2 id="use-a-fiscal-calendar">
  Use a Fiscal Calendar
</h2>

<Note>
  Fiscal Calendars functionality is disabled by default. To enable, [contact technical support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support) for assistance.
</Note>

<Warning>
  This is an experimental feature.
</Warning>

After a user with appropriate privileges has [defined one or more fiscal calendars](#define-a-fiscal-calendar) to your environment, you can use these calendars in any of your sources.

**Select an alternative calendar**

1. Open and [edit an existing source](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#edit-a-data-source) or create a [new source](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#define-a-source).

2. Navigate to the [Global Settings tab](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-global-settings-tab) and select an available calendar listed under **Alternative Calendars Settings**.

   <Note>
     The default calendar is used for all sources unless you specifically select an alternative calendar.
   </Note>

3. Select one or more calendars for your source as needed. Clear the checkbox for a calendar to not use that specific calendar with this source and prevent fiscal time field conversion.

4. After completing your changes, select **Save Settings** to make available your selected calendars to new and existing visuals that use this source.

**Create a Time (FISCAL) field for your selected calendar**

1. After you have [selected one or more calendars](#use-a-fiscal-calendar) for your source, navigate to the [Fields tab](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-fields-tab) to convert a time field to a time field that uses one of the calendars you have added to this source.
2. Select the time field you want to use in the list of available fields.
3. Select the **Convert** option in the Data Details work area on the Settings tab. Select the option presented, **Convert to Fiscal Time** to open a conversion dialog.
4. Enter a **Label** for the new derived field, and select a **Fiscal Calendar** from the list of available options. **Save** your changes.
5. Your new derived field is added to the list of available fields with a data type of **Time (Fiscal)**. It is similar to standard time fields, with the exception that you cannot define a **Time Zone** for this new derived field.

<Note>
  Alternatively, you can select **Add Derived Field** from the Fields tab and create the field using the `to_chrono_datetime` function. Include the `calendar_id` and `dateTime` field in the editor.
</Note>

Once created, you can use this new field in visuals, expressions, filters, and using presets as needed.

* Objects that use a fiscal time field are marked with a **FISCAL** indicator.

* When you export data that relies on fiscal calendars, the data is presented in the appropriate date and time format.

* If you remove an alternative calendar from your source, you cannot make new derived fields based on that calendar.

<h2 id="preset-time-ranges">
  Preset Time Ranges
</h2>

The following table describes all the preset time ranges available in Self-Service Analytics.

<Note>
  If you are using a field that has time zone information disabled (select **Not Specified**), only the time-related information is shown in the user interface and exported with your data. Time zone labels are not included.
</Note>

| Preset type | Data Cached? | Start date | End date |
| - | - | - | - |
| Current Hour | No | Beginning of the current hour | Current time |
| Current Minute | No | Beginning of the current minute | Current time |
| Current Month | No | First day of the current month (for example 08/01/2024 12:00:00 AM) | Last day of the current month (for example 08/31/2024 11:59:59 PM) |
| Current Month-to-Date | No | First day of the current month (for example 08/01/202412:00:00 AM) | Current date and time |
| Current Quarter | No | First day of the current quarter (for example, 07/01/202412:00:00 AM) | Last day of the current quarter (for example 09/30/202411:59:59 PM) |
| Current Quarter-to-Date | No | First day of the current quarter (for example 07/01/202412:00:00 AM) | Current date and time |
| Current Week | No | Sunday of the week with current day (for example Sunday, 08/11/202412:00:00 AM) | Saturday of the week with current day (for example 08/17/202411:59:59 PM) |
| Current Week-to-Date | No | Sunday of the week with current day (for example Sunday, 08/11/202412:00:00 AM) | Current date and time |
| Current Year | No | First day of the current year (for example 01/01/202412:00:00 AM) | Last day of the current year (for example 12/31/202411:59:59 PM) |
| Current Year-to-Date | No | First day of the current year (for example 01/01/202412:00:00 AM) | Current date and time |
| Max Available Range | No | Minimum time value in the data set known to Self-Service Analytics | Maximum time value in the data set known to Self-Service Analytics |
| Previous Hour | No | Beginning of the previous hour (for example Aug 20 2024 12:00:00 PM) | End of the previous hour (for example Aug 20 2024 12:59:59 PM) |
| Previous Minute | No | Beginning of the previous minute | End of the previous minute |
| Previous Month | Yes | First day of the previous month (for example 07/01/202412:00:00 AM) | Last day of the previous month (for example 07/31/2024 11:59:59 PM) |
| Previous Month-to-Date | No | First day of the previous month (for example 07/01/2024 12:00:00 AM) | The current date. For example, if today is 08/05/2024 12:00:00 AM, the information returned is from 07/01/2022 12:00:00 AM through 08/05/2024 12:00:00 AM. |
| Previous Quarter | Yes | First day of the previous quarter (for example 04/01/2024 12:00:00 AM) | Last day of the previous quarter (for example, 06/30/2024 11:59:59 PM) |
| Previous Quarter-to-Date | No | First day of the previous quarter (for example 04/01/202412:00:00 AM) | The current date. For example, if today is 08/05/2024 12:00:00 AM, the information returned is from 04/01/2022 12:00:00 AM through 08/05/2024 12:00:00 AM. |
| Previous Week | Yes | Sunday of the previous week (for example, 08/04/2024 12:00:00 AM) | Saturday of the previous week (for example 08/10/2024 11:59:59 PM) |
| Previous Week-to-Date | No | Sunday or Monday of the previous week, depending on locale (for example 07/27/2024 12:00:00 AM) | The current date. For example, if today is 08/02/2024 12:00:00 AM, the information returned is from 07/25/2022 12:00:00 AM through 08/02/2024 12:00:00 AM. |
| Previous Year | Yes | First day of the previous year (for example 01/01/2023 12:00:00 AM) | Last day of the previous year (for example, 12/31/2023 11:59:59 PM) |
| Previous Year-to-Date | No | First day of the previous year (for example 01/01/2023 12:00:00 AM) | The current date. For example, if today is 08/05/202412:00:00 AM, the information returned is from 01/01/2023 12:00:00 AM through 08/05/2024 12:00:00 AM. |
| Rolling 7 days | No | 7 days before the current date and time | Current date and time |
| Rolling 24 hours | No | 24 hours before the current date and time | Current date and time |
| Rolling 30 days | No | 30 days before the current date and time | Current date and time |
| Rolling 90 days | No | 90 days before the current date and time | Current date and time |
| Rolling 365 days | No | 365 days before the current date and time | Current date and time |
| Rolling Hour | No | 60 minutes before the current date and time | Current date and time |
| Rolling Minute | No | One minute before the current date and time | Current date and time |
| Today | No | Start of the current day (for example, 08/20/2024 12:00:00 AM) | Current date and time |
| Yesterday | Yes | Beginning of the previous day (for example, 08/19/2024 12:00:00 AM) | End of the previous day (08/19/2024 11:59:59 PM) |
