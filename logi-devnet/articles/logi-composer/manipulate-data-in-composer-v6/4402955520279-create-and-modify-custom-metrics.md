---
title: "Create and Modify Custom Metrics"
id: 4402955520279
section: "Manipulate Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402955520279-Create-and-Modify-Custom-Metrics
updated_at: 2021-08-07T17:30:22Z
---

# Create and Modify Custom Metrics

# Create and Modify Custom Metrics

Custom metrics are created and modified using the [*Custom Metrics Editor*](https://devnet.logianalytics.com/hc/en-us/articles/4402955523607-Custom-Metrics-Editor).

To create or modify a custom metric:

1. Access the Custom Metrics Editor in any of the ways described in [*Custom Metrics Editor*](https://devnet.logianalytics.com/hc/en-us/articles/4402955523607-Custom-Metrics-Editor).
2. Enter a name for the custom metric in the space labeled **Untitled Custom Metric**.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404959473559/noteicon.jpg) If you are using non-Latin characters in your functions, the name for your custom metric should start with a letter or an underscore (\_) symbol followed by one or more letters, numbers, underscore, or period characters. Symbols other than the underscore (\_) or period (.) are not allowed.
3. Enter the expression for the custom metric in the editing space. Expressions should follow standard mathematical and logical syntax and are resolved using the standard order of operations. You can manually key in expressions or you can select the elements of your expressions from the menus at the left. The expression should not be assigned to a variable because the resolved value of the expression is assigned to the custom metric, which serves as the 'variable' to which the value is assigned. That is, enter `a / b` rather than `x = a / b`.

   [Row-level expressions](https://devnet.logianalytics.com/hc/en-us/articles/4402955544471-Supported-Row-Level-Functions) and [aggregate functions](https://devnet.logianalytics.com/hc/en-us/articles/4402962963095-Supported-Aggregation-Functions) can be used in custom metrics. In addition, custom metrics can be [filtered](https://devnet.logianalytics.com/hc/en-us/articles/4402955525015-Apply-Filters-to-Custom-Metrics) (using [date and time filter aggregate functions](https://devnet.logianalytics.com/hc/en-us/articles/4402955540631-Date-and-Time-Filter-Aggregation-Functions) and [SQL-like expressions](https://devnet.logianalytics.com/hc/en-us/articles/4402962968599-Supported-SQL-Like-Expressions)).
4. To test your custom metric, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404952887319/run-btn_33x24.png).

   The editor attempts to calculate your custom metric. Any errors are reported. Any results are shown in the Preview area of the Custom Metrics Editor.
5. When you are finished creating or modifying your custom metric definition, select **Save**.
