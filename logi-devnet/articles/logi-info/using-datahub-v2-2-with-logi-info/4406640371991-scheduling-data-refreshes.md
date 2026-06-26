---
title: "Scheduling Data Refreshes"
id: 4406640371991
section: "Using DataHub v2.2 With Logi Info"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406640371991-Scheduling-Data-Refreshes
updated_at: 2022-04-01T03:13:25Z
---

# Scheduling Data Refreshes

# Scheduling Data Refreshes

Logi DataHub allows you to create
Dataviews using data from databases, applications, and files. As a "snapshot" of this data, the DataHub repository will likely require periodic updating in order to "refresh" the data. This topic discusses that operation.

* [About Refreshing Data](#About)
* [Immediate Refresh](#Now)
* [Schedule a Refresh](#Schedule)

## About Refreshing Data

DataHub makes it easy to refresh the data in your repository on a scheduled basis or manually. Essentially you will need to schedule a "data reload" for each data object.
From the Dataview Status page, you also have the option of manually triggering an immediate reload.

During a refresh operation, DataHub will compare the schema from the data source with the column information previously loaded. If they match the scheduled reload will continue. If the schema no longer matches, however, the reload will stop and warning will be displayed.

## Immediate Refresh

To immediately refresh data, navigate to the page for the desired Dataview and click its **Dataview Status** tab:

![](https://devnet.logianalytics.com/hc/article_attachments/5160421554455/schedrefresh_01.png)

If there are multiple objects, select the desired one, then click **Refresh Now**, as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/5160417943319/schedrefresh_02.png)

A prompt will appear requesting that you select the type of refresh to execute. If you select:

* **Replace Data** - All data in the cache will be *replaced* by new data retrieved from the data source.
* **Append Data** - New data retrieved from the data source will be *appended* to the existing data. Existing data will not be updated.

Click the Refresh Now icon ![](https://devnet.logianalytics.com/hc/article_attachments/5160417963927/iconrefresh_19x18.png) to start the data loading operation immediately.

## Schedule a Refresh

The most convenient way to refresh data is to schedule it to occur at regular intervals.

If there are multiple objects, select the desired one, then click **Add Schedule**, and these controls will be displayed:

![](https://devnet.logianalytics.com/hc/article_attachments/5160421582103/schedrefresh_03.png)

Use these steps to create a scheduled refresh:

1. **Refresh Type** - Select *Replace Data* to replace all data with new data retrieved from the data source. Select *Append Data* to have new data retrieved from the data source appended to the existing data - existing data will not be updated.
2. **Location** - (File-type data sources only) Enter a fully-qualified file name with path. Click **Test** to ensure that server and scheduler can access the file.
3. **Recurs** - Select the frequency (*Daily*, *Weekly*, *Monthly*), interval, and start time for the backup.
4. **Timezone** - Select the appropriate time zone.
5. **Start** and **End Date** - Enter the Start Date (required) and End Date (optional) for the backup. Leaving the End Date blank will cause to backup to continue to occur at the specified frequency and interval until the schedule is modified or deleted.

![](https://devnet.logianalytics.com/hc/article_attachments/5160446913687/noteicon.png) Remember that, when the refresh occurs, the Dataview will be unavailable to other users until the operation completes.

Click the **Save** icon ![](https://devnet.logianalytics.com/hc/article_attachments/5160421520791/iconsave.png) to save the schedule.

Click the **Refresh Now** icon ![](https://devnet.logianalytics.com/hc/article_attachments/5160453662231/iconrefresh.png) to refresh the data immediately.

Click the **Reset** icon ![](https://devnet.logianalytics.com/hc/article_attachments/5160421523351/iconreset.png) to clear any changes in the controls during this sequence.

Click the **Delete** icon ![](https://devnet.logianalytics.com/hc/article_attachments/5160453662999/icondelete.png) to delete this schedule.

Click the **Cancel** icon ![](https://devnet.logianalytics.com/hc/article_attachments/5160421588503/iconcancel_18x18.png) to cancel this operation and hide the controls.

Once the schedule has been saved, you'll notice some changes in the Dataview Status tab:

![](https://devnet.logianalytics.com/hc/article_attachments/5160447182103/schedrefresh_04.png)

As shown above, a special "scheduled" icon (circled above) appears in the selected object graphic, the scheduled time appears with a link (highlighted above, click to edit) in the object details, and an **Edit Schedule** button is now visible.
