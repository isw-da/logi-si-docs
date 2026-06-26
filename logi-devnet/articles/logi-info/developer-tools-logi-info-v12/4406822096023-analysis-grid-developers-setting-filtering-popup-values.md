---
title: "Analysis Grid Developers - Setting Filtering Popup Values"
id: 4406822096023
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822096023-Analysis-Grid-Developers-Setting-Filtering-Popup-Values
updated_at: 2022-04-06T06:03:13Z
---

# Analysis Grid Developers - Setting Filtering Popup Values

# Analysis Grid Developers - Setting Filtering Popup Values

Analysis Grid Column elements have a **Popup Values for Filter** attribute, which can be set to *List* or *Calendar*.

![](https://devnet.logianalytics.com/hc/article_attachments/4417591976471/workag_12.png)

The example above shows what happens when it's to *List*. When this column is selected in the Filter panel, users can either type in a value or click a browse button.
Clicking the button will cause a modal pop-up option list to be displayed, and the value for
the filter can then be chosen from the list.

If the attribute is set to Calendar, then a pop-up calendar will appear. Obviously, this attribute value should only be used for date-type columns.
