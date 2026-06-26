---
title: "Configure Date and\u00a0Time Formatting for Visuals"
id: 43701179815949
section: "Use Dashboards and Visuals in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701179815949-Configure-Date-and-Time-Formatting-for-Visuals
updated_at: 2026-05-29T14:10:00Z
---

# Configure Date and Time Formatting for Visuals

# Configure Date and Time Formatting for Visuals

Date and time formats for Time attributes [are set at the source](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116424973-Manage-Fields#Settings). You can override source formats by changing a visual directly, without affecting the underlying source format. For information on other settings that may apply to Time attributes, see [Configure Date and Time Formatting - Data Sources](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701095259917-Configure-Date-and-Time-Formatting-Data-Sources).

**Note:** 
You can also override formatting for the Number attribute at the visual level. See [Configure Number Formatting for Visuals](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701184419213-Configure-Number-Formatting-for-Visuals).

## Configure Formatting for Visuals - Time Attributes

1. Select the visual with time attributes you want to format in a dashboard or the visual gallery.
2. Select a Metric, X or Y axis, Group, Color, Trend line, size, or other available measure. A dialog for your selection opens.

   ![Select Format to format a time attribute](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242256569485 "Time metric work area")
3. Locate your time field using **Search**, or navigate to the field or fields you want to format. Select the menu ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243159686541) for a field, then select Format. The **Format: <field>** work area opens.

   ![Use this work area to format your time field attribute on a visual metric](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242262189581 "Format Time Attribute Work Area")
4. Define your format options, and select **Apply** to apply to this field.
5. Repeat for all fields you want to modify.

   **Note:** 
   To clear your applied changes to a field, open the formatting work area and select **Reset**.

### Format Options Time Attribute for Visuals

When you configure formatting at the visual level, you may not see all the options listed below, depending on the visual you're updating and the available time segments included in the source data.

| Format Option | Description |
| --- | --- |
| Second | Select **Numeric** (0-59) or **2-Digit** (00-59). |
| Minute | Select **Numeric** (0-59) or **2-Digit** (00-59). |
| Hour | Select **Numeric** (1-24) or **2-Digit** (01-24). |
| Hour12 | Select a 12 or 24 hour format option for Hour12.   * **Auto** displays the hour format defined in the source data. * **True** overrides the source format, displaying the hours in 12 hour format, with an appended **AM** or **PM**. * **False** overrides the source format, displaying the hours in 24 hour format. |
| Day | Select **Numeric** (1-7) or **2-Digit** (01-07). |
| Month | Select **Numeric** (1-12), **2-Digit** (01-12), **Long** (January, March), **Short** (Jan, Mar), or **Narrow** (J, M). |
| Weekday | Select **Long** (Friday, Sunday), **Short** (Fri, Sun), **Narrow** (F, S), or **None**. The default is **None**, to show no day of the week. |
| Quarter | Select **Range**, **Narrow**, **Numeric** (1-4), or **2-Digit** (01-04). Set Granularity to Quarter; you can define Quarter formatting after the visual reloads with Quarter granularity. |
| Year | Select **Numeric** (2022) or **2-Digit** (22). |
