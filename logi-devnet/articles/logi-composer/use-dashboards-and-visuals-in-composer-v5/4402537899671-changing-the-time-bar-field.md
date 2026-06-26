---
title: "Changing the Time Bar Field"
id: 4402537899671
section: "Use Dashboards and Visuals in Composer v5"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402537899671-Changing-the-Time-Bar-Field
updated_at: 2021-09-15T02:22:39Z
---

# Changing the Time Bar Field

# Changing the Time Bar Field

You can change the time bar field for a visual in the [visual time bar settings](#Changing) or [on the time bar](#Changing2) itself.

While you are working on a dashboard or visual, the time range and playback configuration you have selected for different time fields are retained. So when you switch between different time fields, the time range and playback settings may change. For example, you might have analyzed your data using the following time fields:

| Field | Range | Playback |
| --- | --- | --- |
| Date | January 2019-March 2019 | On (enabled) |
| Ts | April 2019 | Off (disabled |

When you switch between these fields on the time bar, the ranges and playback settings also switch, as appropriate for each field.

## Changing the Time Bar Field Using Visual Settings

To change the time bar field for a visual using the visual time bar settings:

1. Select the visual in the dashboard or in the Visual Gallery.
2. If you selected the visual on a dashboard, select **Edit Visual** on the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537941655-Using-the-Visual-Menu) to access the [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537948311-Using-the-Sidebar-Menu) for the visual.
3. Select the visual time bar icon (![](https://devnet.logianalytics.com/hc/article_attachments/4406763900183/dashboard-schedule.png)) on the [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537948311-Using-the-Sidebar-Menu) for the visual. The [Time Bar sidebar](https://devnet.logianalytics.com/hc/en-us/articles/4402537938967-Using-the-Visual-Style-Sidebar) opens.
4. Select a new time field on the **Time Bar** sidebar.
   The
   **None (Time Bar is Off)** option is not available for the
   **Line** charts.
5. Optionally, select the
   **Enable playback** checkbox to enable the **Play/Pause** button (the Data DVR functionality) on the **Time Bar**. You can enable or disable this option in the **Global Default Settings** section for your data source.
   For more information about the requirements for playback, see [*Live Mode and Historical Playback*](https://devnet.logianalytics.com/hc/en-us/articles/4402552905879-Live-Mode-and-Historical-Playback).
6. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406753455383/apply-btn_122x22.png).

   The time bar for the visual is changed. If the visual is using a unified time bar, all of the visuals using the unified time bar are also changed. See [*Working with Unified Time Bars*](https://devnet.logianalytics.com/hc/en-us/articles/4402552909207-Working-with-Unified-Time-Bars).
7. [Save](https://devnet.logianalytics.com/hc/en-us/articles/4402537747863-Saving-a-Dashboard) the dashboard.

## Changing the Time Bar Field on the Time Bar

To change the time bar field for a visual using the time bar:

1. Select the visual.
2. On the left side of the time bar, select the field name.
   A Time Bar dialog pops up listing all the time fields in the data source for the visual.
3. Select a new time field on the dialog.
   The
   **None (Time Bar is Off)** option is not available for the
   **Line** charts.

   The time bar for the visual is changed. If the visual is using a unified time bar, all of the visuals using the unified time bar are also changed. See [*Working with Unified Time Bars*](https://devnet.logianalytics.com/hc/en-us/articles/4402552909207-Working-with-Unified-Time-Bars).
4. Close the Time Bar dialog.
5. [Save](https://devnet.logianalytics.com/hc/en-us/articles/4402537747863-Saving-a-Dashboard) the dashboard.
