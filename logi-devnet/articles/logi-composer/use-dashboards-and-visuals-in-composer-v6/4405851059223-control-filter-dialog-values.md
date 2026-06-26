---
title: "Control Filter Dialog Values"
id: 4405851059223
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851059223-Control-Filter-Dialog-Values
updated_at: 2021-09-21T01:28:34Z
---

# Control Filter Dialog Values

# Control Filter Dialog Values

You can control the behavior of filter dialogs by data source. These controls are set on the [Fields tab](https://devnet.logianalytics.com/hc/en-us/articles/4405851026455-Fields-Tab) of the [data source configuration](https://devnet.logianalytics.com/hc/en-us/articles/4405851027479-Manage-Data-Source-Configurations).

* For attribute fields, you can require your users to manually enter attribute values to include in the visual or dashboard, instead of letting them select values from a list. See [*Controlling Attribute Field Filters*](#Controll).
* For integer and number fields, you can specify the initial (default) minimum and maximum values available for selection as filters. See [*Controlling Integer and Number Field Filters*](#Controll2).
* For time fields, you can specify the initial (default) minimum and maximum dates and times for the filter or, when shown on the time bar, the initial (default) time range shown. You can change these settings by manipulating the filters and time bar on the visual. See [*Controlling Time Field Filters*](#Controll3).

## Controlling Attribute Field Filters

To control attribute field filters:

1. Edit the data source configuration for which you want to control attribute field filters. See [*Edit a Data Source Configuration*](https://devnet.logianalytics.com/hc/en-us/articles/4405851024663-Edit-a-Data-Source-Configuration). The data source configuration wizard displays.
2. Select the [Fields tab](https://devnet.logianalytics.com/hc/en-us/articles/4405851026455-Fields-Tab) in the data source configuration wizard.
3. Locate the attribute field in the field table on the Fields tab.
4. In the Filter Display column for the attribute, select (check) **Only Allow Custom Values**.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747417111/only-allow-custom-values_138x35.png)
5. When your changes are complete, select **Save**, **Save & Next**, or **Finish** (depending on the tab) to save the data source configuration and close the wizard.

To test this, create a new dashboard visual using the data source. Then filter the data on the visual by the attribute. You will be required to manually enter values to filter for on the dashboard visual. The following example Filters sidebar requests that the user manually add at least one value of the Category field for the filter:

![](https://devnet.logianalytics.com/hc/article_attachments/4406743799063/filter-manual4_288x463.png)

To add a value:

1. Select **Include** or **Exclude** using the drop-down menu in the **Operator** box.
2. Type a value into the search box and select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743717271/add.png). Be sure to specify the values using the proper sentence case. For example, if the values are stored in lowercase letters only, but you enter a value with starting a capital letter, the search will not work.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743799575/filter-manual5_288x276.png)
3. The value is added to the list of selected values.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747417623/filter-manual6_288x471.png)
4. When all values have been added to the list, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743745559/apply1-btn_41x23.png) to apply the filters to the visual. For more information about setting attribute filters, see [*Set an Attribute Filter*](https://devnet.logianalytics.com/hc/en-us/articles/4405851058327-Set-an-Attribute-Filter).

## Controlling Integer and Number Field Filters

To control integer or number field filters:

1. Edit the data source configuration for which you want to control integer or number field filters. See [*Edit a Data Source Configuration*](https://devnet.logianalytics.com/hc/en-us/articles/4405851024663-Edit-a-Data-Source-Configuration). The data source configuration wizard displays.
2. Select the [Fields tab](https://devnet.logianalytics.com/hc/en-us/articles/4405851026455-Fields-Tab) in the data source configuration wizard.
3. Locate the integer or number field in the field table on the **Fields** tab.
4. In the Filter Display column for the attribute, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406747417879/custom-range-btn_92x21.png). The Custom Range dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743799831/custom-range-num_192x152.png)
5. Specify minimum and maximum values for the filter ranges for the field. You can type the numbers directly in the **From** and **To** boxes or use the arrows in the boxes to increment and decrement the values. Custom range values can be integers only and numbers with scientific notation.
6. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743745559/apply1-btn_41x23.png) to apply the custom filter range.
7. When your changes are complete, select **Save**, **Save & Next**, or **Finish** (depending on the tab) to save the data source configuration and close the wizard.

To test this, create a new dashboard visual using the data source. Then filter the data on the visual by the integer or number field you specified a custom range for. The values you can select for the filter are restricted to the custom range you specified in the data source configuration.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747418263/filter-configure-num1_288x496.png)

When your filter values have been specified, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743745559/apply1-btn_41x23.png) to apply the filters to the visual. For more information about setting numeric filters, see [*Set a Numeric Field Filter*](https://devnet.logianalytics.com/hc/en-us/articles/4405851060119-Set-a-Numeric-Field-Filter).

## Controlling Time Field Filters

To control the default time field filter and time bar ranges:

1. Edit the data source configuration for which you want to control time field filters. See [*Edit a Data Source Configuration*](https://devnet.logianalytics.com/hc/en-us/articles/4405851024663-Edit-a-Data-Source-Configuration). The data source configuration wizard displays.
2. Select the [**Fields** tab](https://devnet.logianalytics.com/hc/en-us/articles/4405851026455-Fields-Tab) in the data source configuration wizard.
3. Locate the time field in the field table on the **Fields** tab.
4. In the Filter Display column for the attribute, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406747417879/custom-range-btn_92x21.png). The Custom Range dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743800087/custom-range-time_226x174.png)
5. Specify minimum and maximum values for the filter ranges for the time field in the **From** and **To** boxes.

   Select the value in the **From** or **To** time fields to select a new date and time in the resulting calendar pop-up.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743801367/calendar-popup_174x192.png)
6. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743745559/apply1-btn_41x23.png) to apply the custom filter range.
7. When your changes are complete, select **Save**, **Save & Next**, or **Finish** (depending on the tab) to save the data source configuration and close the wizard.

To test this, create a new dashboard visual using the data source. Then filter the data on the visual by the time field. The values you can select for the filter are restricted to the custom range you specified in the data source configuration. For more information about specifying time filters, see [*Set a Time Field Filter*](https://devnet.logianalytics.com/hc/en-us/articles/4405851063831-Set-a-Time-Field-Filter).

![](https://devnet.logianalytics.com/hc/article_attachments/4406743802007/filter-configure-time1_288x490.png)

When your filter values have been specified, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743745559/apply1-btn_41x23.png) to apply the filters to the visual.
