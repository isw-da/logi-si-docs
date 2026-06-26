---
title: "Convert Attributes to Time Fields in Data Source Field Specifications"
id: 4405859290903
section: "Manipulate Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859290903-Convert-Attributes-to-Time-Fields-in-Data-Source-Field-Specifications
updated_at: 2021-09-21T01:28:03Z
---

# Convert Attributes to Time Fields in Data Source Field Specifications

# Convert Attributes to Time Fields in Data Source Field Specifications

If your data contains time-related fields (attributes) that are not stored in a recognized time format, you can convert the fields to time fields using the [Fields](https://devnet.logianalytics.com/hc/en-us/articles/4405851026455-Fields-Tab) tab of the [data source configuration](https://devnet.logianalytics.com/hc/en-us/articles/4405851027479-Manage-Data-Source-Configurations). As long as any string field contains date or time data, you can set its type to **Time** and specify a time pattern recognized by Composer.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) The process described here is **not** the recommended process. Instead, Composer recommends that you convert the data using a derived field, as described in [*Convert Attributes to Time Fields Using Derived Fields*](https://devnet.logianalytics.com/hc/en-us/articles/4405859291927-Convert-Attributes-to-Time-Fields-Using-Derived-Fields).

Composer uses Java's SimpleDateFormat for time conversions. See [SimpleDateFormat](https://docs.oracle.com/javase/7/docs/api/java/text/SimpleDateFormat.html).

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) Group functionality does **not** work for fields for which the type is manually set to **Time**. You cannot specify these fields as the Group, Group By, or Trend fields for a visual. You **can** use these fields in filters and apply them as filters on the time bar. However, you may find that the results shown in your visual are incorrect. This may happen because the manually configured time formats are different and, consequently, not in lexicographic order. For example, suppose you have two strings:

* String `20170801` (August 1, 2017) matches the time format `yyyyMMdd`.
* String `08012018` (August 1, 2018) matches the time format `MMddyyyy`.

When filtering time data by these fields, Composer treats the time values as numbers. So, when filtered in ascending order, 08012018 will sort before 20170801, which is not correct (August 1, 2018 occurred after August 1, 2017, not before). The resulting visual will not be correct.

To convert an attribute field to a time field in the field table of a data source configuration:

1. Make sure you are logged in as a Composer administrator.
2. Select **Sources** on the [UI menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859444119-The-Composer-UI-Menu) (![](https://devnet.logianalytics.com/hc/article_attachments/4406743720343/hamburger.png)). The [Data Sources](https://devnet.logianalytics.com/hc/en-us/articles/4405851037719-Sources-Page) page appears.
3. In the My Data Sources table on the [Data Sources](https://devnet.logianalytics.com/hc/en-us/articles/4405851037719-Sources-Page) page, locate and select the data source configuration you want to edit. The data source configuration wizard appears.
4. Select the [Fields](https://devnet.logianalytics.com/hc/en-us/articles/4405851026455-Fields-Tab) tab in the data source configuration wizard.
5. Locate the time field in the list of fields.
6. Change the value in the **Type** column for the field to **Time**.

   The
   **Configure** column changes to display two selectable drop-down menu lists: **Time Pattern** and **Granularity** as well as the **Time Zone** option.
7. Specify the time format (pattern) for the field.
   The
   **Time Pattern** list (with
   **Default** displayed) provides two options:
   **Default** and **Custom**. Select the **Custom** option to specify a unique time format in a text box.
8. Specify a granularity for the time field.
   The
   **Granularity** list lets you select the default unit of time to use for this time field.

   Valid granularity options are **Millisecond**, **Second**, **Minute**, **Hour**, **Day**, **Week**, **Month**, **Quarter**, or **Year**. If some of these granularity options do not appear, verify that the granularity specified for this field on the **Fields** tab of the data source definition is set at the correct granularity level.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) The refinement level of the field data in a data store defines the minimum level of granularity that should be set for the field. Specifying granularity for a field that is lower than the refinement level of the field data will not produce a visual with data grouped at the requested lower level. For example, if a field's data is stored in hours, requesting the granularity of that data lower than hours will produce the values up to the hour level, and the more detailed level information will be zeros (i.e., 0 minutes, 0 seconds, and 0 milliseconds).
9. Specify the time zone for the time field. The **Time Zone** option lets you select a time zone: The time zone label will be displayed in visuals and dashboards for this data source.
10. When your changes are complete, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743833239/save-white-btn.png), ![](https://devnet.logianalytics.com/hc/article_attachments/4406743834903/save-next-btn.png), or ![](https://devnet.logianalytics.com/hc/article_attachments/4406743835287/finish-btn.png) (depending on the tab) to save the data source configuration and close the wizard.
