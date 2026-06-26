---
title: "Action Elements Example: Export to PDF"
id: 4419715352471
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715352471-Action-Elements-Example-Export-to-PDF
updated_at: 2022-07-17T02:24:10Z
---

# Action Elements Example: Export to PDF

# Action Elements Example: Export to PDF

This example shows a simple link that exports the current report to a PDF and is typical of the Action.Export-type elements:

![](https://devnet.logianalytics.com/hc/article_attachments/7522839985943/introacts_05.png)

1. Add a **Label** element to your report and set its **Caption** attribute value as desired.
2. Beneath it, add an **Action.Export PDF** element. Its default attribute settings are used for this example.
3. Beneath it, add a **Target.PDF** element. By leaving its **Report Definition File** attribute blank, the default (the current report) will be exported.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) Set the **Show Links** attribute to *True* if you want links exported from the report to be "clickable" in the PDF.
The Label caption will appear on the page as an HTML link; when clicked, the report will be exported. Action.Export PDF can be used as a child of a number of elements, including Button, Image, Charts, and more.
For more information about exporting to PDF, see our [Exporting to Adobe PDF](https://devnet.logianalytics.com/hc/en-us/articles/4419722896151-Export-to-Adobe-PDF).
