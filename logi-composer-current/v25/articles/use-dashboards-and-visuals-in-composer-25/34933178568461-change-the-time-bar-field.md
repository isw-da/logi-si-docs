---
title: "Change the Time Bar Field"
id: 34933178568461
section: "Use Dashboards and Visuals in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933178568461-Change-the-Time-Bar-Field
updated_at: 2026-05-26T22:09:17Z
---

# Change the Time Bar Field

# Change the Time Bar Field

You can change the time bar field for a visual in the [visual time bar settings](#Changing) or [on the time bar](#Changing2) itself.

While you are working on a dashboard or visual, the time range and playback configuration you have selected for different time fields are retained. So when you switch between different time fields, the time range and playback settings may change. For example, you might have analyzed your data using the following time fields:

| Field | Range | Playback |
| --- | --- | --- |
| Date | January 2024-March 2024 | On (enabled) |
| Ts | April 2024 | Off (disabled) |

When you switch between these fields on the time bar, the ranges and playback settings also switch, as appropriate for each field.

## Change the Time Bar Field Using Visual Settings

**Change the time bar field for a visual using the visual time bar settings**

1. Select the visual in the dashboard or in the Visual Gallery.
2. If you selected the visual on a dashboard, select **Settings** on the [visual drop-down menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933290868621-Use-the-Visual-Menu) to access the [sidebar menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933295031181-Use-the-Visual-Sidebar-Menu) for the visual.
3. Select the visual time bar icon (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167855753357)) on the [sidebar menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933295031181-Use-the-Visual-Sidebar-Menu) for the visual. The [Time Bar sidebar](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933257208973-Use-the-Visual-Style-Sidebar) opens.
4. Select a new time field on the **Time Bar** sidebar.
   The
   **None (Time Bar is Off)** option is not available for the
   **Line** charts.
5. Optionally, select the
   **Enable playback** checkbox to enable the **Play/Pause** button (the Data DVR functionality) on the **Time Bar**. You can enable or disable this option in the **Global Default Settings** section for your data source.
   For more information about the requirements for playback, see [Live Mode and Historical Playback](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933163012621-Live-Mode-and-Historical-Playback).
6. Select **Apply**.

   The time bar for the visual is changed. If the visual is using a unified time bar, all the visuals using the unified time bar are also changed. See [Work with Unified Time Bars](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933192240653-Work-with-Unified-Time-Bars).
7. [Save](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932815496845-Save-a-Dashboard) the dashboard or visual.

## Change the Time Bar Field on the Time Bar

**Change the time bar field for a visual using the time bar**

1. Select the visual.
2. On the left side of the time bar, select the field name.
   A Time Bar dialog pops up listing all the time fields in the data source for the visual.
3. Select a new time field on the dialog.
   The
   **None (Time Bar is Off)** option is not available for the
   **Line** charts.

   The time bar for the visual is changed. If the visual is using a unified time bar, all the visuals using the unified time bar are also changed. See [Work with Unified Time Bars](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933192240653-Work-with-Unified-Time-Bars).
4. Close the Time Bar dialog.
5. [Save](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932815496845-Save-a-Dashboard) the dashboard.
