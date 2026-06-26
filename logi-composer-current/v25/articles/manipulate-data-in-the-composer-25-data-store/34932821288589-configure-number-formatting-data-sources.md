---
title: "Configure Number Formatting  - Data Sources"
id: 34932821288589
section: "Manipulate Data In The Composer 25 Data Store"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932821288589-Configure-Number-Formatting-Data-Sources
updated_at: 2026-05-26T22:10:00Z
---

# Configure Number Formatting  - Data Sources

# Configure Number Formatting - Data Sources

As a user with [data source privileges](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference), configure number formats for Number fields in a data source at creation, or later when you edit an existing source. This defines the default format for number fields as displayed in visuals, data details of visuals, and sample format fields for consistency across your organization.

There are three places to control the display of numbers in a data source.

* Setting the locale for users to display correct formats, based on a user's geographical location. For example, users based in the United States and users based in Italy would see different currency formats due to the local formatting of the fields. To define the location settings for users within your environment, ask your administrator or see [Specify A User's Regional Settings](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932610886157-Specify-A-User-s-Regional-Settings).
* Configuring the formats for number fields in a data source configuration, as described in the rest of this topic. Bear in mind that defining number formats depends on the region (location) settings configured for your environment.
* Finally, you can [enable users to override the formatting](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933282294029-Control-How-Users-Interact-With-a-Visual) you've defined at the data source and for most visuals at the visual level. Find more visual formatting information in the following topics:

  + [Configure Date and Time Formatting for Visuals](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933263048077-Configure-Date-and-Time-Formatting-for-Visuals)
  + [Configure Number Formatting for Visuals](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933278713485-Configure-Number-Formatting-for-Visuals)
  + [Format Time Table Data Using the Table Context Menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933253788173-Format-Time-Table-Data-Using-the-Table-Context-Menu)
  + [Format Numeric Table Data Using the Table Context Menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933268999949-Format-Numeric-Table-Data-Using-the-Table-Context-Menu)
  + [Available Visual Types](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933207922445-Available-Visual-Types)

**Specify the format for number fields in a data source configuration**

1. Log in as a user with the **Administer Sources** or **Create New Data Sources** [privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference), or write permission for this source.
2. Select **Sources** on the UI menu (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167930919821)). The [Sources](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932895238669-Data-Sources-Page) page appears.
3. Edit the appropriate data source configuration and access the [**Fields** tab](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932906721933-Manage-Fields) of the data source.
4. Locate the number field you want to modify. The **Data Type** column on the **Fields** tab must define the field as a **Number** field.
5. In the sidebar menu, select the settings (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167941033997)) button to open the **Settings** work area. Select the edit (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167941034637)) button in the **Format** work area to edit the date and time format for this field.

   ![Update the format of your number field here](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167319672589 "Format Number Attributes - Data Source")
6. Select one of the following number formats in the drop-down list in the Number Format box. The other fields on the Format dialog change based on the number format you select.

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
7. Select **Apply** to apply to apply your changes, then **Save** to save your changes.
