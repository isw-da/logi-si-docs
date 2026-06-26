---
title: "Create and Modify Custom Metrics"
id: 34932813034765
section: "Manipulate Data In The Composer 25 Data Store"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932813034765-Create-and-Modify-Custom-Metrics
updated_at: 2026-05-26T22:06:58Z
---

# Create and Modify Custom Metrics

# Create and Modify Custom Metrics

Custom metrics are created and modified using the [Custom Metrics Editor](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932820475405-Custom-Metrics-Editor).

**Create or modify a custom metric**

1. Access the Custom Metrics Editor in any of the ways described in [Custom Metrics Editor](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932820475405-Custom-Metrics-Editor).
2. Enter a label for the custom metric in the space labeled **Untitled Custom Metric**.

   **Note:** 
   If you are using non-Latin characters in your functions, the label for your custom metric should start with a letter or an underscore (\_) symbol followed by one or more letters, numbers, underscore, or period characters. Symbols other than the underscore (\_) or period (.) are not allowed.
3. Enter the expression for the custom metric in the editing space. Expressions should follow standard mathematical and logical syntax and are resolved using the standard order of operations. You can manually key in expressions or you can select the elements of your expressions from the menus at the left. The expression should not be assigned to a variable because the resolved value of the expression is assigned to the custom metric, which serves as the 'variable' to which the value is assigned. That is, enter `a / b` rather than `x = a / b`.

   [Row-level expressions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932902575629-Supported-Row-Level-Functions) and [aggregate functions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932900526221-Supported-Aggregation-Functions) can be used in custom metrics. In addition, custom metrics can be [filtered](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932814261773-Apply-Filters-to-Custom-Metrics) (using [date and time filter aggregate functions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932852083725-Date-and-Time-Filter-Aggregation-Functions) and [SQL-like expressions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932861652621-Supported-SQL-Like-Expressions)).
4. To test your custom metric, select **Run**.

   The editor attempts to calculate your custom metric. Any errors are reported. Any results are shown in the Preview area of the Custom Metrics Editor.
5. When you are finished creating or modifying your custom metric definition, select **Save**.
