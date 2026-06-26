---
title: "Format Numeric Table Data Using the Table Context Menu"
id: 43701213266061
section: "Use Dashboards and Visuals in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701213266061-Format-Numeric-Table-Data-Using-the-Table-Context-Menu
updated_at: 2026-05-29T14:10:06Z
---

# Format Numeric Table Data Using the Table Context Menu

# Format Numeric Table Data Using the Table Context Menu

Numeric data and date formats [are set at the source](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116424973-Manage-Fields#Settings). You can change them directly in a table or pivot table using the table context menu. Your format changes apply directly to that visual, and affects every instance of that visual in your dashboards, without affecting the underlying source formatting. See [Format Time Table Data Using the Table Context Menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701213292429-Format-Time-Table-Data-Using-the-Table-Context-Menu). To edit number for other visuals, see [Configure Number Formatting for Visuals](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701184419213-Configure-Number-Formatting-for-Visuals).

**Format numeric table data using the table context menu**

1. Select a table visual in a dashboard or in the Visual Gallery.
2. Locate the field in the table and select ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243134598669) next to its column heading to access the table context menu.

   ![select to format numbers in a table column](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242276964365 "table context menu with number formatting")
3. Select **Format <field>** on the context menu. A Format work area opens.

   ![select formatting options in the format work area](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242344956045 "Number Format Work area plain")

   **Note:** 
   Select a Number Format, then select other options for this field. Select **Apply** to apply your changes to the data in the table column, or **Reset** reapply the source formatting.

   The other fields on the Format dialog change based on the Number Format you select. See [Number Format Options](#Number).
4. Optionally, repeat for other fields in the table.
5. Save the visual, or the dashboard and visual.

**Format aggregated data using the table context menu**

1. Select a table visual in a dashboard or in the Visual Gallery.
2. Locate the field that includes aggregated in the table and select ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243134598669) next to its column heading to access the table context menu.

   ![select to format aggregated numbers in a table column](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242327495949 "table context menu with number formatting aggregated")
3. Select **Format <field>** on the context menu. A Format work area opens.

   ![select formatting options in the format work area for raw or aggregated numbers](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242297410061 "Number Format Work area plain for aggregated numbers")
4. Select the tab of the data you want to format: the aggregate data, shown here as **Actualsales (Sum)**, or the raw data, shown here as **Actualsales (Raw data)**.

   **Note:** 
   You can apply different formatting options to your raw and aggregate data.

   ![table with different formatting options applied to aggregate and raw data](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242259430157 "table with different formatting options applied to aggregate and raw data")
5. Select a Number Format, then select other options for this field. select **Apply** to apply your changes to the data in the table column, or **Reset** reapply the source formatting.

   **Note:** 
   The other fields on the Format dialog change based on the Number Format you select. See [Number Format Options](#Number).
6. Optionally, repeat for other fields in the table.
7. Save the visual, or the dashboard and visual.

## Number Format Options

The available fields for each number format change to reflect the options available for your selected format:

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
