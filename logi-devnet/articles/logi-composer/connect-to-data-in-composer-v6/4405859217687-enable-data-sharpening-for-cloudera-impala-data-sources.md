---
title: "Enable Data Sharpening for Cloudera Impala Data Sources"
id: 4405859217687
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859217687-Enable-Data-Sharpening-for-Cloudera-Impala-Data-Sources
updated_at: 2021-09-21T01:27:20Z
---

# Enable Data Sharpening for Cloudera Impala Data Sources

# Enable Data Sharpening for Cloudera Impala Data Sources

Data Sharpening works with certain partitioned Impala data sources. The partitioned field should be a time-based attribute and in a [supported time format](https://devnet.logianalytics.com/hc/en-us/articles/4405851010711-Supported-Date-and-Time-Formats) (for example, yyyy-MM-dd). Follow the steps below to set up Data Sharpening for an Impala data source.

To configure Data Sharpening for a Cloudera Impala data source configuration:

1. Log into Composer (either as an administrator or as a user who has been assigned to a group with [data source management privileges](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference)).
2. Select **Sources** on the [UI menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859444119-The-Composer-UI-Menu) (![](https://devnet.logianalytics.com/hc/article_attachments/4406743720343/hamburger.png)) or the [top-level navigation menu](https://devnet.logianalytics.com/hc/en-us/articles/4405851152407-The-Top-Level-Navigation-Banner), or select the **Sources** box on the [Home page](https://devnet.logianalytics.com/hc/en-us/articles/4405851121559-Home-Page). The [Sources](https://devnet.logianalytics.com/hc/en-us/articles/4405851037719-Sources-Page) page appears.
3. Select your Impala data source to start the data source configuration wizard.
4. Select the **Fields** tab. Locate the time field you will use as the driving time field for data sharpening. This is the time field that needs to be specified in the global default settings.
5. Identify the partition type that will be used, and change the setting in the **Partitions** column. Select a partition type from the drop-down list. An example is provided in [*Example*](#Example) that illustrates this step.
6. In the **Configure** column, select an appropriate time granularity, as shown below. Consider the 10% rule to ensure Data Sharpening runs when you want it to. See [*When Data Sharpening Occurs*](https://devnet.logianalytics.com/hc/en-us/articles/4405851008919-When-Data-Sharpening-Occurs) for more information.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743907351/granularity_768x263.png)

   An example is provided in [*Example*](#Example) that illustrates this step.
7. Select the **Visuals** tab.
8. Select the **Global Default Settings**. The time bar, search, and Data Sharpening settings for the data source appear.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747434647/ds-global-defaults_288x518.png)
9. Make sure **Enable Timebar** is switched on. This enables the Data Sharpening settings. If this is switched off, you cannot configure Data Sharpening settings. For more information about time bar default settings, see [*Configure Time Bar Defaults*](https://devnet.logianalytics.com/hc/en-us/articles/4405859324311-Configure-Time-Bar-Defaults).
10. Turn the **Prefer Sharpening** switch on to enable Data Sharpening for the data source.
11. Optionally, use the **Max Queries** slider to specify the maximum number of queries used for Data Sharpening. The default maximum is 10 queries.
12. Select **Finish** or **Save** to save your data source configuration.

## Example

The following scenario is used in this example of setting up Data Sharpening for a Cloudera Impala data source.

* You have 3 years of historical data on Cloudera Impala
* The time stamp in your data provides granularity to the day level (in column **Order\_Date**)
* Your data is partitioned by month (using column **Order\_Date\_Month** that contains data from column **Order\_Date**, but is truncated to the month)

To set up Data Sharpening for the Impala data source on its Fields tab:

1. Log into Composer (either as an administrator or as a user who has been assigned to a group with [data source management privileges](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference)).
2. Select **Sources** on the [UI menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859444119-The-Composer-UI-Menu) (![](https://devnet.logianalytics.com/hc/article_attachments/4406743720343/hamburger.png)) or the [top-level navigation menu](https://devnet.logianalytics.com/hc/en-us/articles/4405851152407-The-Top-Level-Navigation-Banner), or select the **Sources** box on the [Home page](https://devnet.logianalytics.com/hc/en-us/articles/4405851121559-Home-Page). The [Sources](https://devnet.logianalytics.com/hc/en-us/articles/4405851037719-Sources-Page) page appears.
3. Select the Impala data source to start the data source configuration wizard.
4. Select the **Fields** tab.
5. Determine whether there are sub-folders in Impala. If so, the **Label** must include the full date format (for example, month=202001, which is in time format **yyyyMM**).
6. Configure the Impala source as follows on the **Fields** tab:

   1. For the **Order\_Date** field, make sure **Day** granularity is selected.
   2. For the **Order\_Date\_Month** field:

      * In the **Partitions** column, set the partitioned time field to **Date** (or verify that it is selected).
      * In the **Default** column, set the option to **Pattern** and enter the appropriate time format (for this example, the time format should be **yyyyMM**).

        Select granularity to be **Month** (make sure time granularity of the partitioned column is more than the granularity of the linked time field).
      * Link the partition to the date field. Select a time field from the drop-down list (for this example, **Order\_Date** should be selected).
7. Select the **Visuals** tab of the data source configuration and, in **Global Default Settings**, select **Order\_Date** from the drop-down menu list. **Order\_Date** is the driving time field.
8. Be sure you enable Data Sharpening by toggling **Prefer Sharpening** on. Optionally adjust the maximum number of queries for data Sharpening using the **Max Queries** slider. See [*Enable Data Sharpening and Configure Its Defaults*](https://devnet.logianalytics.com/hc/en-us/articles/4405851007127-Enable-Data-Sharpening-and-Configure-Its-Defaults) for more information.
9. Select **Finish** or **Save** to save your data source configuration.

For sharpening to work in this example, the time range must be at least 10 times greater than the time interval for the selected visual. So if one month's data shows in the visual, and the time granularity is set to **Day**, Data Sharpening should run (most months have more than 30 days, which meets the 10% threshold).

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) If your Impala partition breaks out time attributes into separate fields, Data Sharpening is not immediately possible. For example, if YEAR, MONTH, and DAY are all separate partitioned fields, they must be combined into one field for Data Sharpening to function.
