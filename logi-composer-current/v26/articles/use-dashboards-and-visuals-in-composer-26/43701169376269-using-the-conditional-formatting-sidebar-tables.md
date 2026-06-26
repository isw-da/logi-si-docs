---
title: "Using the Conditional Formatting Sidebar - Tables"
id: 43701169376269
section: "Use Dashboards and Visuals in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701169376269-Using-the-Conditional-Formatting-Sidebar-Tables
updated_at: 2026-05-29T14:10:09Z
---

# Using the Conditional Formatting Sidebar - Tables

# Using the Conditional Formatting Sidebar - Tables

Format your visuals by adding color and text formats based on the conditions you define. A sidebar menu work area, Conditional Formatting, allows you to set format conditions to apply to your data.

**Note:** Composer displays a warning icon if you try to create a conditional formatting rule for tables that include a field or group not present in the visual. The resulting rule will not include the missing field or group.

1. Select the visual in the Visual Gallery or on a dashboard.
2. If you selected the visual on a dashboard, select **Settings** on the [visual drop-down menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701184743565-Use-the-Visual-Menu) to access the [sidebar menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701215106445-Use-the-Visual-Sidebar-Menu) for the visual.
3. Select the conditional formatting option ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242331005965) on the [sidebar menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701215106445-Use-the-Visual-Sidebar-Menu) for the visual. The Conditional Formatting sidebar opens.

   ![Use to create conditional formatting rules](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242349048333 "Conditional Formatting work area - table")
4. Use the Conditional Formatting sidebar to configure formatting options for your table visuals. See [Configure Conditional Formatting](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701183616525-Configure-Conditional-Formatting).
5. After making changes, select **Apply** to apply the conditional formatting rules you have specified.
6. Save the visual or dashboard to save your changes.

## Conditional Format Options

The available options for rules and formatting change to reflect your selections.

### Conditional Formatting Sidebar

![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243146668685)

* Select **Add Rule** to add a conditional formatting rule. See [Configure Conditional Formatting](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701183616525-Configure-Conditional-Formatting).
* Select an existing rule to edit the rule, or the delete icon ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243132108941) to delete the rule.
* Select and drag rules to change their order.

### Add or Edit Conditional Formatting Rule

![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242313039757)

### Select When To Apply Formatting

Select the add icon ![add icon](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243132109837 "add icon") in **Select When To Apply Formatting** to define the conditions to apply your formatting.

### Select Where To Apply Formatting

Enable **Format entire row** in **Select Where To Apply Formatting**to format the entire row. Disable to format only the applicable cell.

Select the add icon ![add icon](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243132109837 "add icon") for **Formatting** to define the formatting for your condition.

Select the delete icon ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243132108941) to delete a formatting option.

### Select When To Apply Formatting

* **Row** attribute: Select a row attribute to define the values for formatting by this data. Optionally, select the add icon ![add icon](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243132109837 "add icon") to add a derived field or custom metric.

  ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242303509645)

  Example: Apply a background color to a specific **State** condition.

  ![example of conditional formatting by row attribute](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242331509261 "Conditional Formatting summary")
* **Group** attribute: Select an attribute that you’ve grouped your data by to define values for that aggregated data. Optionally, select the add icon ![add icon](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243132109837 "add icon") to add a derived field or custom metric.

  ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242268384269)

  Example: Format Group attributes that meet the condition: the `Sum` of **Actualsales** grouped by **Product**`Between` a defined range of values.

  ![example of formatting applied to a group condition](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242301712781 "Group Conditional Formatting work area")

### Select Values for an Attribute

| Selection | Description |
| --- | --- |
| Operator | Select **Include** to include the selected values for this attribute.  Select **Exclude** to exclude the selected values for this attribute. |
| Customize | Enter a custom value and select **Add** to add it to the values list.  Select the delete icon  to remove it from the values list. |
| Search | Search for specific values in your list. |
| Select All | Select the checkbox to include all listed values.  Clear the checkbox to remove all selected values. |

![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242268599437)

### Select Values for a Number

| Selection | Description |
| --- | --- |
| Range | Displays the range for this value. |
| Operator | Select an operator to use.  Options may include **Between**, **Not Between**, **Equal**, **Not Equal**, **Greater Than**, **Greater Than** or **Equal**, **Less Than**, **Less than or Equal**, **Include**, and **Exclude**.  Depending on the Operator you select, different definition fields are available to use. |
| From, To | Define a value range for **Between**and **Not Between**. |
| Value | Define a value for **Equal**, **Not Equal**, **Greater Than**, **Greater Than** or **Equal**, **Less Than**, and **Less than or Equal**. |
| Customize | Optionally define for **Include**, and **Exclude**.  Enter a custom value and select **Add** to add it to the values list.  Select the delete icon  to remove it from the values list. |
| Search | For **Include**, and **Exclude**. Search for specific values in your list. |
| Select All | Define for **Include**, and **Exclude**.  Select the checkbox to include all listed values.  Clear the checkbox to remove all selected values. |

### Select Values for a Date

| Selection | Description |
| --- | --- |
| Range | Displays the range for this value. |
| Operator | Select an operator to use.  Options may include **Between**, **Is NULL**, and **Is not NULL**.  Depending on the Operator you select, different definition fields are available to use. |
| From, To | Define a value range for **Between**, using **Static Time** or **Dynamic Time**. See [Set a Time Field Filter](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701087681293-Set-a-Time-Field-Filter). |
| Presets ... | Select an available **Preset...** for **Between**.  See [Set a Time Field Filter](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701087681293-Set-a-Time-Field-Filter). |

## Formatting

Select the add icon ![add icon](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243132109837 "add icon") to add a formatting option you'll apply to your condition. Select the delete icon ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243132108941) to remove the formatting option.

| Format Option | Description |
| --- | --- |
| Text Color | Select to define the text color format to apply to your condition.  Enter the color number in hexadecimal, or use the color picker to enter RGB values or pick your color visually. |
| Background Color | Select to define the background color to apply to your condition.  Enter the color number in hexadecimal, or use the color picker to enter RGB values or pick your color visually. |
| Bold | Select to enable or disable bold formatting to apply to your condition. |
| Italic | Select to enable or disable italic formatting to apply to your condition. |
| Underline | Select to enable or disable underline formatting to apply to your condition. |

![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242301943181)

In the above example, formatting based on the **Actualsales** condition is applied first, then formatting based on the **State** condition overrides that rule.

Mix and match rules as needed to achieve the look and feel you want.
