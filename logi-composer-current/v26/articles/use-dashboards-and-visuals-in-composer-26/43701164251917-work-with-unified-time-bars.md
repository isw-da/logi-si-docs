---
title: "Work with Unified Time Bars"
id: 43701164251917
section: "Use Dashboards and Visuals in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701164251917-Work-with-Unified-Time-Bars
updated_at: 2026-05-29T14:09:32Z
---

# Work with Unified Time Bars

# Work with Unified Time Bars

When you work with your dashboard, you can apply the settings that you have configured on your time bar to multiple visuals from the same data source. This enables you to view and playback the data on different visuals for the same time period and filtered by the same time filter.
The time bar shared by the visuals is called a unified time bar.

**Note:** 
You can only use a unified time bar for visuals for which the time bar has been enabled.

By default, new visuals from the same data source are applied to the same unified time bar on a dashboard, provided the dashboard has only one time bar configured for visuals using that data source.
If the existing visuals on the dashboard use different time bars, new visuals are not assigned to the unified time bar and must be configured manually to do so.

## Apply a Unified Time Bar to Multiple Visuals

If you have several visuals from the same data source or your visuals contain [cross-source links](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701012571789-Use-Cross-Source-Links), you can use different time bar settings for different visuals.

**Apply a unified time bar to multiple visuals that use the same data source on your dashboard**

1. Select a visual on the dashboard and configure the time bar settings, as described above.
2. Select the time attribute on the left side of the time bar. The Time Bar dialog appears.

   **Note:** If you are using a field that has time zone information disabled (select **[Not Specified](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701080606477-Configure-Time-Bar-Defaults#Default_Time_Attribute)**), only the time-related information is shown in the user interface and exported with your data. Time zone labels are not included.
3. In the Time Bar dialog, select the visuals from your dashboard you want to use a unified time bar. The available visuals are listed in the
   **Applies to** section. The visuals selected will share a unified time bar. The unselected visuals will maintain their own individual time bars.

   **Note:** 
   If your dashboard contains visuals from different data sources, the
   **Applies to** section lists the visuals separated by data source. The active section in the **Applies to** list depends on the visual selected in the dashboard.
4. Save the dashboard.

## Change the Unified Time Bar Attribute

**Change the unified time bar attribute**

1. Select a visual on the dashboard that is using the time bar.
2. Select the time attribute on the left side of the time bar. The Time Bar dialog appears.
3. In the Time Bar dialog, select a different time attribute. all the visuals using the unified time bar will adjust to use the new time attribute.

   **Note:** 
   If your dashboard contains visuals from different data sources, the
   **Applies to** section lists the visuals separated by data source. The active section in the **Applies to** list depends on the visual selected in the dashboard.
4. Save the dashboard.

## Change the Unified Time Bar Range

**Change the unified time bar range**

1. Select a visual on the dashboard that is using the time bar.
2. Do one of the following:

   * Select the range setting on the time bar and select a new static time range, dynamic time range, or preset time range for the time bar. See [Adjust the Time Bar Range](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701166967181-Adjust-the-Time-Bar-Range).
   * Use the time bar sliders to adjust the range.
3. Save the dashboard.

## Remove a Visual from the Unified Time Bar

**Remove a visual from a unified time bar**

1. Select the visual on the dashboard.
2. Select the time attribute on the left side of the time bar. The Time Bar dialog appears.
3. In the Time Bar dialog, clear the checkbox associated with the visual in the **Applies to** section. The visual will no longer share the unified time bar.

   **Note:** 
   If your dashboard contains visuals from different data sources, the
   **Applies to** section lists the visuals separated by data source. The active section in the **Applies to** list depends on the visual selected in the dashboard.
4. Save the dashboard.

For example, suppose you need to filter the data in the
***Sales by Hour*** visual by the
***Inserted*** attribute for
***JAN 10 2017 6 AM*** on the
***Real Time Sales*** visual.
When you select
**Apply** to apply the filter, you will have to confirm breaking the unification. The
***Real Time Sales*** visual is updated and the time bar changes accordingly.
