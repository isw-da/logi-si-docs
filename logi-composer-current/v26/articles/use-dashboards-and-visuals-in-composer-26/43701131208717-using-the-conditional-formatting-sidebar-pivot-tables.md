---
title: "Using the Conditional Formatting Sidebar - Pivot Tables"
id: 43701131208717
section: "Use Dashboards and Visuals in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701131208717-Using-the-Conditional-Formatting-Sidebar-Pivot-Tables
updated_at: 2026-05-29T14:10:10Z
---

# Using the Conditional Formatting Sidebar - Pivot Tables

# Using the Conditional Formatting Sidebar - Pivot Tables

Format your visuals by adding color and text formats based on the conditions you define. A sidebar menu work area, Conditional Formatting, allows you to set format conditions to apply to your data. You're not limited to formatting information based on data represented in the table, you can create conditional formatting rules based on any data available in the source that is the basis of the pivot table.

1. Select the pivot table visual in the Visual Gallery or on a dashboard.
2. If you selected the visual on a dashboard, select **Settings** on the [visual drop-down menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701184743565-Use-the-Visual-Menu) to access the [sidebar menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701215106445-Use-the-Visual-Sidebar-Menu) for the visual.
3. Select the conditional formatting option ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243122806925) on the [sidebar menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701215106445-Use-the-Visual-Sidebar-Menu) for the visual. The Conditional Formatting sidebar opens.

   ![Use to create conditional formatting rules](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243161545357 "Conditional Formatting work area - table")
4. Using the Conditional Formatting sidebar, you can configure formatting options for your pivot table visuals. See [Configure Conditional Formatting](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701183616525-Configure-Conditional-Formatting).
5. After making changes, select **Apply** to apply the conditional formatting rules you have specified.
6. Save the visual or dashboard to save your changes.

## Conditional Format Options

The available options for rules and formatting change to reflect your selections.

### Conditional Formatting Sidebar

![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243122809741)

* Select **Add Rule** to add a conditional formatting rule. See [Configure Conditional Formatting](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701183616525-Configure-Conditional-Formatting).
* Select an existing rule to edit the rule, or the delete icon ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243161549837) to delete the rule.
* Select and drag rules to change their order.

### Add or Edit Conditional Formatting Rule

![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242313972109)

### Select When To Apply Formatting

Select the add icon ![add icon](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243122817165 "add icon") in **Select When To Apply Formatting** to define the conditions to apply your formatting.

### Select Where To Apply Formatting

Select the add icon ![add icon](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243122817165 "add icon") for **Formatting** to define the formatting for your condition.

Select the delete icon ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243161549837) to delete a formatting option.

### Select When To Apply Formatting

**Group** attribute: Select a group of data to define values for that aggregated data. Optionally, select the add icon ![add icon](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243122817165 "add icon") to add a derived field or custom metric.

![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242332621453)

Example: Format Group attributes that meet the condition: the `Range` of **Volume** grouped by **Income Bracket** is `Between` a defined range of values.

![example of formatting applied to a group condition](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242304802317 "Group Conditional Formatting work area")

### Select Values for a Custom Metric

| Selection | Description |
| --- | --- |
| Values | Select a range of values to format. Options include:   * **Cell Value** - format the data based on the value of the cell. * **Row Total** - format the data based on the value of the row total. * **Column Total** - format the data based on the value of the column total. |
| Operator | Select an operator to use. Options may include **Between**, **Equal**, **Not Equal**, **Greater Than**, **Greater Than or Equal**, **Less Than**, and **Less than or Equal**. Depending on the Operator you select, different definition fields are available to use. |
| From, To | Define a value range for **Between**. |
| Value | Define a value for **Equal**, **Not Equal**, **Greater Than**, **Greater Than** or **Equal**, **Less Than**, and **Less than or Equal**. |

### Select Values for a Number

| Selection | Description |
| --- | --- |
| Range | Displays the range for this value. |
| Values | Select a range of values to format. Options include:   * **Cell Value** - format the data based on the value of the cell. * **Row Total** - format the data based on the value of the row total. * **Column Total** - format the data based on the value of the column total. |
| Aggregation | Select an aggregation option for Values. Options include **Avg**, **Min**, **Max**, **Sum**, **Count**, **Distinct Count**, and **Last Value**. |
| Operator | Select an operator to use. Options may include **Between**, **Equal**, **Not Equal**, **Greater Than**, **Greater Than or Equal**, **Less Than**, and **Less than or Equal**. Depending on the Operator you select, different definition fields are available to use. |
| From, To | Define a value range for **Between**. |
| Value | Define a value for **Equal**, **Not Equal**, **Greater Than**, **Greater Than** or **Equal**, **Less Than**, and **Less than or Equal**. |

### Select Values for Count Of

| Selection | Description |
| --- | --- |
| Values | Select a range of values to format. Options include:   * **Cell Value** - format the data based on the value of the cell. * **Row Total** - format the data based on the value of the row total. * **Column Total** - format the data based on the value of the column total. |
| Aggregation | Select an aggregation option for Values. Options include **Count**and **Distinct Count**. |
| Operator | Select an operator to use. Options may include **Between**, **Equal**, **Not Equal**, **Greater Than**, **Greater Than or Equal**, **Less Than**, and **Less than or Equal**. Depending on the Operator you select, different definition fields are available to use. |
| From, To | Define a value range for **Between**. |
| Value | Define a value for **Equal**, **Not Equal**, **Greater Than**, **Greater Than or Equal**, **Less Than**, and **Less than or Equal**. |

## Formatting

Select the add icon ![add icon](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243122817165 "add icon") to add a formatting option you'll apply to your condition. Select the delete icon ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243161549837) to remove the formatting option.

| Format Option | Description |
| --- | --- |
| Text Color | Select to define the text color format to apply to your condition.  Enter the color number in hexadecimal, or use the color picker to enter RGB values or pick your color visually. |
| Background Color | Select to define the background color to apply to your condition.  Enter the color number in hexadecimal, or use the color picker to enter RGB values or pick your color visually. |
| Bold | Select to enable or disable bold formatting to apply to your condition. |
| Italic | Select to enable or disable italic formatting to apply to your condition. |
| Underline | Select to enable or disable underline formatting to apply to your condition. |

![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243122818701)

In the above example, formatting based on the **Actualsales** condition is applied first, then formatting based on the **State** condition overrides that rule.

Mix and match rules as needed to achieve the look and feel you want.
