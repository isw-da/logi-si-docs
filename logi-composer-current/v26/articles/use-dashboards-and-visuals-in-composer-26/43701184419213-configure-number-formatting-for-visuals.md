---
title: "Configure Number Formatting for Visuals"
id: 43701184419213
section: "Use Dashboards and Visuals in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701184419213-Configure-Number-Formatting-for-Visuals
updated_at: 2026-05-29T14:10:01Z
---

# Configure Number Formatting for Visuals

# Configure Number Formatting for Visuals

Formats for Number attributes [are set at the source](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116424973-Manage-Fields#Settings). You can override source formats by changing a visual directly, without affecting the underlying source format. For information on other settings that may apply to Number attributes, see [Configure Number Formatting - Data Sources](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701095045005-Configure-Number-Formatting-Data-Sources).

**Note:** 
You can also override formatting for the Time attribute at the visual level. See [Configure Date and Time Formatting for Visuals](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701179815949-Configure-Date-and-Time-Formatting-for-Visuals).

## Configure Formatting for Visuals - Number Attributes

1. Select the visual with time attributes you want to format in a dashboard or the visual gallery.
2. Select a Metric, X or Y axis, Group, Color, Trend line, size, or other available measure. A dialog for your selection opens.

   ![Select Format to format a numeric attribute](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242262328717 "Number metric work area")
3. Locate your number field using **Search**, or navigate to the field or fields you want to format. Select the menu ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243150009869) for a field, then select Format. The **Format: <field>** work area opens.

   ![Use this work area to format your numeric field attribute on a visual metric](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242279871757 "Format Number Attribute Work Area")
4. Define your format options, and select **Apply** to apply to this field.
5. Repeat for all fields you want to modify.

   **Note:** 
   To clear your applied changes to a field, open the formatting work area and select **Reset**.

### Format Options Number Attribute for Visuals

Select one of the following number formats in the drop-down list in the Number Format box. The other fields on the Format dialog change based on the number format you select.

* **Plain Number**: Select this format to display the field as plain number values. Additional format information you can select includes:

  | Format Option | Description |
  | --- | --- |
  | Unit Multiple | Select the unit of measure you want to use for the field from the drop-down list. Valid values are **None**, **Thousands (K)**, **Millions (M)**, **Billions (B)**, and **Trillions (T)**. The unit multiple is used in visuals. For example, a value of 1,500,000 would show as 1.5M in visuals. |
  | Decimal Place | Specify the number of decimal places used in the data. |
  | Negative Display | Select the desired negative value format from the drop-down list. Valid values are the dash (-) in front of a negative value or parentheses surrounding negative values. For example, value of negative 30 could show as -30 or (30) in visuals. |
  | Use 1000 Separator | If you want commas used to separate number values into thousands, millions, billions, and trillions, check the **Use 1000 Separator** box. For example, if this box is checked, 2500 appears as 2,500 in visuals. |
* **Percentage**: Select this format to display the field as percentage values. Additional format information you can select includes:

  | Format Option | Description |
  | --- | --- |
  | Decimal Place | Specify the number of decimal places used in the data. |
  | Negative Display | Select the desired negative value format from the drop-down list. Valid values are the dash (-) in front of a negative value or parentheses surrounding negative values. For example, value of negative 30.25 percent could show as -30.25% or (30.25%) in visuals. |
  | Use 1000 Separator | If you want commas used to separate number values into thousands, millions, billions, and trillions, check the **Use 1000 Separator** box. |
* **Money**: Select this format to display the field as currency values. Additional format information you can select includes:

  | Format Option | Description |
  | --- | --- |
  | Symbol | Select the currency symbol you want used for money values in visuals. |
  | Unit Multiple | Select the unit of measure you want to use for the field from the drop-down list. Valid values are **None**, **Thousands (K)**, **Millions (M)**, **Billions (B)**, and **Trillions (T)**. The unit multiple is used in visuals. For example, a value of 1,500,000 would show as 1.5M in visuals. |
  | Decimal Place | Specify the number of decimal places used in the data. |
  | Negative Display | Select the desired negative value format from the drop-down list. Valid values are the dash (-) in front of a negative value or parentheses surrounding negative values. For example, value of negative 30 dollars and 25 cents could show as -$30.25 or ($30.25) in visuals. |
  | Use 1000 Separator | If you want commas used to separate number values into thousands, millions, billions, and trillions, check the **Use 1000 Separator** box. |
* **Storage**: Select this format to display the field as computer storage values. Additional format information you can select includes:

  | Format Option | Description |
  | --- | --- |
  | Unit Multiple | Select the unit of measure you want to use for the field from the drop-down list. Valid values are **Bytes (B)**, **Kilobytes (KB)**, **Megabytes (MB)**, **Gigabytes (GB)**, **Terabytes (TB)**, **Petabytes (PB)**, and **Exabytes (EB)**. The unit multiple is used in visuals. For example, a value of 950 kilobytes would show as 950KB in visuals. |
  | Decimal Place | Specify the number of decimal places used in the data. |
* **Scientific Notation**: Select this format to display the field as scientific decimals. Additional format information you can select includes:

  | Format Option | Description |
  | --- | --- |
  | Decimal Place | Specify the number of decimal places used in the data. |
