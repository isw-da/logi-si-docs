---
title: "Configure Number Formatting"
id: 4405851006231
section: "Manipulate Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851006231-Configure-Number-Formatting
updated_at: 2021-09-21T01:27:58Z
---

# Configure Number Formatting

# Configure Number Formatting

Administrators and users assigned [data source privileges](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference) can configure number formatting for number fields in a data source. This allows you to define the format for certain fields based on location, field types, and the measure of unit in use. When you define the type of value for number fields, users can then interact with the values in visuals created using those fields.

There are two ways of controlling the display of numbers.

* Setting the locale for users to display correct formats, based on a user's geographical location. For example, users based in the United States and users based in Russia would see different currency formats due to the local formatting of the fields. To define the location settings for users within your environment, ask your administrator or see [*Specify User Regional Settings*](https://devnet.logianalytics.com/hc/en-us/articles/4405850865943-Specify-User-Regional-Settings).
* Configuring the formats for number fields in a data source configuration, as described in the rest of this topic. Bear in mind that defining number formats depends on the region (location) settings configured for your environment.

You can define number formats when you create a new data source or you can edit the fields of previously created data sources.

To specify the format for number fields in a data source configuration:

1. Make sure you are logged in as a Composer administrator or as a user assigned to a group that can edit data source configurations.
2. Edit the data source configuration and access the [**Fields** tab](https://devnet.logianalytics.com/hc/en-us/articles/4405851026455-Fields-Tab) of the data source configuration wizard.
3. Locate the NUMBER field you want to modify. The **Type** column on the **Fields** tab must define the field as a **Number** field.
4. In the **Configure** column, under **Format**, select the numerical format value to open the **Format** dialog.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747434903/format-dialog_160x259.png)
5. Select one of the following number formats in the drop-down list in the Number Format box. The other fields on the Format dialog change based on the number format you select.

   * **Plain Number**: Select this format to indicate that the field stores plain number values. After selecting this format type, specify the following additional format information on the Format dialog:

     | Format Option | Description |
     | --- | --- |
     | Unit Multiple | Select the unit of measure you want to use for the field from the drop-down list. Valid values are **None**, **Thousands (K)**, **Millions (M)**, **Billions (B)**, and **Trillions (T)**. The unit multiple is used in visuals. For example, a value of 1,500,000 would show as 1.5M in visuals. |
     | Decimal Place | Specify the number of decimal places used in the data. |
     | Negative Display | Select the desired negative value format from the drop-down list. Valid values are the dash (-) in front of a negative value or parentheses surrounding negative values. For example, value of negative 30 could show as -30 or (30) in visuals. |
     | Use 1000 Separator | If you want commas used to separate number values into thousands, millions, billions, and trillions, check the **Use 1000 Separator** box. For example, if this box is checked, 2500 appears as 2,500 in visuals. |
     | Apply to all number fields in "<data-source-name>" | Check this box if you want the same number format to be applied to all number fields in this data source configuration. |
   * **Percentage**: Select this format to indicate that the field stores percentage values. After selecting this format type, specify the following additional format information on the Format dialog:

     | Format Option | Description |
     | --- | --- |
     | Decimal Place | Specify the number of decimal places used in the data. |
     | Negative Display | Select the desired negative value format from the drop-down list. Valid values are the dash (-) in front of a negative value or parentheses surrounding negative values. For example, value of negative 30.25 percent could show as -30.25% or (30.25%) in visuals. |
     | Use 1000 Separator | If you want commas used to separate number values into thousands, millions, billions, and trillions, check the **Use 1000 Separator** box. |
     | Apply to all number fields in "<data-source-name>" | Check this box if you want the same number format to be applied to all number fields in this data source configuration. |
   * **Money**: Select this format to indicate that the field stores currency values. After selecting this format type, specify the following additional format information on the Format dialog:

     | Format Option | Description |
     | --- | --- |
     | Symbol | Select the currency symbol you want used for money values in visuals. |
     | Unit Multiple | Select the unit of measure you want to use for the field from the drop-down list. Valid values are **None**, **Thousands (K)**, **Millions (M)**, **Billions (B)**, and **Trillions (T)**. The unit multiple is used in visuals. For example, a value of 1,500,000 would show as 1.5M in visuals. |
     | Decimal Place | Specify the number of decimal places used in the data. |
     | Negative Display | Select the desired negative value format from the drop-down list. Valid values are the dash (-) in front of a negative value or parentheses surrounding negative values. For example, value of negative 30 dollars and 25 cents could show as -$30.25 or ($30.25) in visuals. |
     | Use 1000 Separator | If you want commas used to separate number values into thousands, millions, billions, and trillions, check the **Use 1000 Separator** box. |
     | Apply to all number fields in "<data-source-name>" | Check this box if you want the same number format to be applied to all number fields in this data source configuration. |
   * **Storage**: Select this format to indicate that the field stores computer storage values. After selecting this format type, specify the following additional format information on the Format dialog:

     | Format Option | Description |
     | --- | --- |
     | Unit Multiple | Select the unit of measure you want to use for the field from the drop-down list. Valid values are **Bytes (B)**, **Kilobytes (KB)**, **Megabytes (MB)**, **Gigabytes (GB)**, **Terabytes (TB)**, **Petabytes (PB)**, and **Exabytes (EB)**. The unit multiple is used in visuals. For example, a value of 950 kilobytes would show as 950KB in visuals. |
     | Decimal Place | Specify the number of decimal places used in the data. |
     | Apply to all number fields in "<data-source-name>" | Check this box if you want the same number format to be applied to all number fields in this data source configuration. |
   * **Scientific Notation**: Select this format to indicate that the field stores values using scientific decimals. After selecting this format type, specify the following additional format information on the Format dialog:

     | Format Option | Description |
     | --- | --- |
     | Decimal Place | Specify the number of decimal places used in the data. |
     | Apply to all number fields in "<data-source-name>" | Check this box if you want the same number format to be applied to all number fields in this data source configuration. |
6. Review the **Example** at the top of the Format dialog. It shows an example of how the number values might appear, based on your settings.
7. Select **Apply** to make your changes.
8. When all your data source configuration changes are complete, select **Save**, **Save & Next**, or **Finish** (depending on the tab) to save the data source configuration and close the wizard.
