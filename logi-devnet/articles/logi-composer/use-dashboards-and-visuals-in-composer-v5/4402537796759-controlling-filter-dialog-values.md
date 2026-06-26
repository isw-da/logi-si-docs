---
title: "Controlling Filter Dialog Values"
id: 4402537796759
section: "Use Dashboards and Visuals in Composer v5"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402537796759-Controlling-Filter-Dialog-Values
updated_at: 2021-09-15T02:21:34Z
---

# Controlling Filter Dialog Values

# Controlling Filter Dialog Values

You can control the behavior of filter dialogs by data source. These controls are set on the [Fields tab](https://devnet.logianalytics.com/hc/en-us/articles/4402537783063-Fields-Tab) of the [data source configuration](https://devnet.logianalytics.com/hc/en-us/articles/4402552802199-Manage-Data-Source-Configurations).

* For attribute fields, you can require your users to manually enter attribute values to include in the visual or dashboard, instead of letting them select values from a list. See [*Controlling Attribute Field Filters*](#Controll).
* For integer and number fields, you can specify the initial (default) minimum and maximum values available for selection as filters. See [*Controlling Integer and Number Field Filters*](#Controll2).
* For time fields, you can specify the initial (default) minimum and maximum dates and times for the filter or, when shown on the time bar, the initial (default) time range shown. You can change these settings by manipulating the filters and time bar on the visual. See [*Controlling Time Field Filters*](#Controll3).

## Controlling Attribute Field Filters

To control attribute field filters:

1. Edit the data source configuration for which you want to control attribute field filters. See [*Editing a Data Source Configuration*](https://devnet.logianalytics.com/hc/en-us/articles/4402537781143-Editing-a-Data-Source-Configuration). The data source configuration wizard displays.
2. Select the [Fields tab](https://devnet.logianalytics.com/hc/en-us/articles/4402537783063-Fields-Tab) in the data source configuration wizard.
3. Locate the attribute field in the field table on the Fields tab.
4. In the Filter Display column for the attribute, select (check) **Only Allow Custom Values**.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406763979031/only-allow-custom-values_138x35.png)
5. When your changes are complete, select **Save**, **Save & Next**, or **Finish** (depending on the tab) to save the data source configuration and close the wizard.

To test this, create a new dashboard visual using the data source. Then filter the data on the visual by the attribute. You will be required to manually enter values to filter for on the dashboard visual. The following example Filters sidebar requests that the user manually add at least one value of the Category field for the filter:

![](https://devnet.logianalytics.com/hc/article_attachments/4406763979415/filter-manual4_288x463.png)

To add a value:

1. Select **Include** or **Exclude** using the drop-down menu in the **Operator** box.
2. Type a value into the search box and select ![](https://devnet.logianalytics.com/hc/article_attachments/4406753440151/add.png). Be sure to specify the values using the proper sentence case. For example, if the values are stored in lowercase letters only, but you enter a value with starting a capital letter, the search will not work.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406763979799/filter-manual5_288x276.png)
3. The value is added to the list of selected values.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406763980055/filter-manual6_288x471.png)
4. When all values have been added to the list, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406753455127/apply1-btn_41x23.png) to apply the filters to the visual. For more information about setting attribute filters, see [*Setting an Attribute Filter*](https://devnet.logianalytics.com/hc/en-us/articles/4402537796119-Setting-an-Attribute-Filter).

## Controlling Integer and Number Field Filters

To control integer or number field filters:

1. Edit the data source configuration for which you want to control integer or number field filters. See [*Editing a Data Source Configuration*](https://devnet.logianalytics.com/hc/en-us/articles/4402537781143-Editing-a-Data-Source-Configuration). The data source configuration wizard displays.
2. Select the [Fields tab](https://devnet.logianalytics.com/hc/en-us/articles/4402537783063-Fields-Tab) in the data source configuration wizard.
3. Locate the integer or number field in the field table on the **Fields** tab.
4. In the Filter Display column for the attribute, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406763980311/custom-range-btn_92x21.png). The Custom Range dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406763980695/custom-range-num_192x152.png)
5. Specify minimum and maximum values for the filter ranges for the field. You can type the numbers directly in the **From** and **To** boxes or use the arrows in the boxes to increment and decrement the values. Custom range values can be integers only and numbers with scientific notation.
6. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406753455127/apply1-btn_41x23.png) to apply the custom filter range.
7. When your changes are complete, select **Save**, **Save & Next**, or **Finish** (depending on the tab) to save the data source configuration and close the wizard.

To test this, create a new dashboard visual using the data source. Then filter the data on the visual by the integer or number field you specified a custom range for. The values you can select for the filter are restricted to the custom range you specified in the data source configuration.

![](https://devnet.logianalytics.com/hc/article_attachments/4406753470743/filter-configure-num1_288x496.png)

When your filter values have been specified, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406753455127/apply1-btn_41x23.png) to apply the filters to the visual. For more information about setting numeric filters, see [*Setting a Numeric Field Filter*](https://devnet.logianalytics.com/hc/en-us/articles/4402537797399-Setting-a-Numeric-Field-Filter).

## Controlling Time Field Filters

To control the default time field filter and time bar ranges:

1. Edit the data source configuration for which you want to control time field filters. See [*Editing a Data Source Configuration*](https://devnet.logianalytics.com/hc/en-us/articles/4402537781143-Editing-a-Data-Source-Configuration). The data source configuration wizard displays.
2. Select the [**Fields** tab](https://devnet.logianalytics.com/hc/en-us/articles/4402537783063-Fields-Tab) in the data source configuration wizard.
3. Locate the time field in the field table on the **Fields** tab.
4. In the Filter Display column for the attribute, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406763980311/custom-range-btn_92x21.png). The Custom Range dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406763980951/custom-range-time_226x174.png)
5. Specify minimum and maximum values for the filter ranges for the time field in the **From** and **To** boxes.

   Select the value in the **From** or **To** time fields to select a new date and time in the resulting calendar pop-up.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406763981335/calendar-popup_174x192.png)
6. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406753455127/apply1-btn_41x23.png) to apply the custom filter range.
7. When your changes are complete, select **Save**, **Save & Next**, or **Finish** (depending on the tab) to save the data source configuration and close the wizard.

To test this, create a new dashboard visual using the data source. Then filter the data on the visual by the time field. The values you can select for the filter are restricted to the custom range you specified in the data source configuration. For more information about specifying time filters, see [*Setting a Time Field Filter*](https://devnet.logianalytics.com/hc/en-us/articles/4402552813847-Setting-a-Time-Field-Filter).

![](https://devnet.logianalytics.com/hc/article_attachments/4406763981591/filter-configure-time1_288x490.png)

When your filter values have been specified, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406753455127/apply1-btn_41x23.png) to apply the filters to the visual.
