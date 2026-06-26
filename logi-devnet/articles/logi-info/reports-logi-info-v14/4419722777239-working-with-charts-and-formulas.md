---
title: "Working with Charts and Formulas"
id: 4419722777239
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722777239-Working-with-Charts-and-Formulas
updated_at: 2022-07-17T02:24:52Z
---

# Working with Charts and Formulas

# Working with Charts and Formulas

Charts and formulas in the template are automatically updated when the
report is run. Microsoft Excel requires at least *two values* in a
formula so that the formula is updated properly when new data rows are
inserted into the worksheet. You're encouraged to use dummy values in
order to test formulas, charts and other objects included in the report
template.

![](https://devnet.logianalytics.com/hc/article_attachments/7522847840279/createxltemp_03_589x195.png)

Extra rows can be added to the data range for the purposes of testing a
formula or adding a chart. To prevent them from being included in the
final report, developers can use special ranges called
**disposable ranges**. Logi Studio provides a way to declare a range
"disposable" and the Logi report server removes these ranges in
the final report. See
[Excel Template](https://devnet.logianalytics.com/hc/en-us/articles/4419715031191-Excel-Template)
for more details.
