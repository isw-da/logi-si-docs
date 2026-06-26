---
title: "Change the Default Date and Time Format"
id: 4405851009815
section: "Manipulate Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851009815-Change-the-Default-Date-and-Time-Format
updated_at: 2021-09-21T01:28:02Z
---

# Change the Default Date and Time Format

# Change the Default Date and Time Format

You can change the format (pattern) of recognized time fields in your data on the [Fields](https://devnet.logianalytics.com/hc/en-us/articles/4405851026455-Fields-Tab) tab of a [data source configuration](https://devnet.logianalytics.com/hc/en-us/articles/4405851027479-Manage-Data-Source-Configurations).

To change a time field's format:

1. Make sure you are logged in as a Composer administrator.
2. Select **Sources** on the UI menu (![](https://devnet.logianalytics.com/hc/article_attachments/4406743720343/hamburger.png)). The [Data Sources](https://devnet.logianalytics.com/hc/en-us/articles/4405851037719-Sources-Page) page appears.
3. In the My Data Sources table on the [Data Sources](https://devnet.logianalytics.com/hc/en-us/articles/4405851037719-Sources-Page) page, locate and select the data source configuration you want to edit. The data source configuration wizard appears.
4. Select the [Fields](https://devnet.logianalytics.com/hc/en-us/articles/4405851026455-Fields-Tab) tab in the data source configuration wizard.
5. Locate the time field in the list of fields.
6. In the Configure column of the table, specify the time format (pattern) for the field.
   The
   **Time Pattern** list (with
   **Default** displayed) provides two options:

   * **Default**: Select this option if the time format in the data source conforms to one of the standards recognized by Composer.
   * **Custom**: Select this option when you need to enter a unique time format. A new text box will appear, allowing you to specify the unique time format.
7. Specify a granularity for the time field.
   The
   **Granularity** list lets you select the default unit of time to use for this time field.

   Valid granularity options are **Millisecond**, **Second**, **Minute**, **Hour**, **Day**, **Week**, **Month**, **Quarter**, or **Year**. If some of these granularity options do not appear, verify that the granularity specified for this field on the **Fields** tab of the data source definition is set at the correct granularity level.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) The refinement level of the field data in a data store defines the minimum level of granularity that should be set for the field. Specifying granularity for a field that is lower than the refinement level of the field data will not produce a visual with data grouped at the requested lower level. For example, if a field's data is stored in hours, requesting the granularity of that data lower than hours will produce the values up to the hour level, and the more detailed level information will be zeros (i.e., 0 minutes, 0 seconds, and 0 milliseconds).
8. Specify the time zone for the time field. The **Time Zone** option lets you select a time zone: The time zone label will be displayed in visuals and dashboards for this data source.
9. When your changes are complete, select **Save**, **Save & Next**, or **Finish** (depending on the tab) to save the data source configuration and close the wizard.
