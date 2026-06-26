---
title: "Convert Attributes to Time Fields in Data Source Field Specifications"
id: 43701078376461
section: "Manipulate Data In The Composer 26 Data Store"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701078376461-Convert-Attributes-to-Time-Fields-in-Data-Source-Field-Specifications
updated_at: 2026-05-29T14:11:09Z
---

# Convert Attributes to Time Fields in Data Source Field Specifications

# Convert Attributes to Time Fields in Data Source Field Specifications

If your data contains time-related fields (attributes) that are not stored in a recognized time format, you can convert the fields to time fields using the [Fields](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116424973-Manage-Fields) tab of the [data source configuration](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701068934669-Manage-Data-Sources). As long as any string field contains date or time data, you change it to a time pattern recognized by Composer.

**Important:** 
As of Composer v7.10, implicit field type conversions are no longer supported. When you want to convert one field type to another, a derived field is created with the new field type you selected. When you upgrade from an earlier version of Composer, some of the fields in your data sources may be converted into a derived field supported by the upgrade. See [Source Field Migration](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701100844557-Source-Field-Migration).

**Note:** 
The process described here is **not** the recommended process. Instead, insightsoftware recommends that you convert the data using a derived field, as described in [Convert Attributes to Time Fields Using Derived Fields](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701078414349-Convert-Attributes-to-Time-Fields-Using-Derived-Fields).

Composer uses Java's SimpleDateFormat for time conversions. See [SimpleDateFormat](https://docs.oracle.com/javase/7/docs/api/java/text/SimpleDateFormat.html).

**Note:** 
Group functionality does **not** work for fields for which the type is manually set to **Time**. You cannot specify these fields as the Group, Group By, or Trend fields for a visual. You **can** use these fields in filters and apply them as filters on the time bar. However, you may find that the results shown in your visual are incorrect. This may happen because the manually configured time formats are different and, consequently, not in lexicographic order. For example, suppose you have two strings:

* String `20230801` (August 1, 2023) matches the time format `yyyyMMdd`.
* String `08012024` (August 1, 2024) matches the time format `MMddyyyy`.

When filtering time data by these fields, Composer treats the time values as numbers. So, when filtered in ascending order, 08012024 will sort before 20230801, which is not correct (August 1, 2024 occurred after August 1, 2023, not before). The resulting visual will not be correct.

**Convert an attribute field to a time field as a derived field in your data source configuration**

1. Make sure you are logged in as an administrator.
2. Select **Sources** on the [UI menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701160499853-The-Composer-UI-Menu) (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243266854669)). The [Sources](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701081381901-Data-Sources-Page) page appears.
3. In the sources table on the [Sources](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701081381901-Data-Sources-Page) page, locate and select the data source configuration you want to edit.
4. Select the [Fields](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116424973-Manage-Fields) tab.
5. Locate and select the time field (Data Type: Attribute) in the list of fields.
6. Select **Convert** in the Data Type area of the Settings tab for the field and select **Convert to Time**.  
   ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242623826573)
7. Rename the field in the **Label** field, and define time granularity in the **Origin Field Format**.  
   ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242639879693)

   Valid time parts include:

   * YYYY - four digit year
   * MM - two digit month
   * DD - two digit day
   * HH - two digit 24-hour format
   * MI - two digit minute
   * SS - two digit seconds
   * MS - two digit miliseconds

   **Note:** 
   The information returned is limited by the information available in the original field. For example, if a field's data is stored in hours, you will get values up to the hour level. If you request granularity not available, zeros are returned for information not available, for example, 0 minutes, 0 seconds, and 0 milliseconds.
8. When your changes are complete, select **Save** create the derived field.

**Convert a number field to a time field as a derived field in your data source configuration**

1. Make sure you are logged in as an administrator.
2. Select **Sources** on the [UI menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701160499853-The-Composer-UI-Menu) (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243266854669)). The [Sources](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701081381901-Data-Sources-Page) page appears.
3. In the sources table on the [Sources](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701081381901-Data-Sources-Page) page, locate and select the data source configuration you want to edit.
4. Select the [Fields](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116424973-Manage-Fields) tab.
5. Locate and select the time field (Data Type: Number) in the list of fields.
6. Select **Convert** in the Data Type area of the Settings tab for the field and select **Convert to Time**.  
   ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242651195917)
7. Rename the field in the **Label** field, and select an available time granularity in the **Origin Field Format**.  
   ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242655475213)

   Valid time parts include:

   * YYYY - four digit year
   * MM - two digit month
   * DD - two digit day
   * HH - two digit 24-hour format
   * MI - two digit minute
   * SS - two digit seconds
   * MS - two digit miliseconds

   **Note:** 
   The information returned is limited by the information available in the original field. For example, if a field's data is stored in hours, you will get values up to the hour level. If you request granularity not available, zeros are returned for information not available, for example, 0 minutes, 0 seconds, and 0 milliseconds.
8. When your changes are complete, select **Save** create the derived field.
