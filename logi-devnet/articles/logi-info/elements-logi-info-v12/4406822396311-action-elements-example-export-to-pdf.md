---
title: "Action Elements Example: Export to PDF"
id: 4406822396311
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822396311-Action-Elements-Example-Export-to-PDF
updated_at: 2022-04-06T06:07:00Z
---

# Action Elements Example: Export to PDF

# Action Elements Example: Export to PDF

This example shows a simple link that exports the current report to a PDF and is typical of the Action.Export-type elements:

![](https://devnet.logianalytics.com/hc/article_attachments/4417583868567/introacts_05.png)

1. Add a **Label** element to your report and set its **Caption** attribute value as desired.
2. Beneath it, add an **Action.Export PDF** element. Its default attribute settings are used for this example.
3. Beneath it, add a **Target.PDF** element. By leaving its **Report Definition File** attribute blank, the default (the current report) will be exported.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) Set the **Show Links** attribute to *True* if you want links exported from the report to be "clickable" in the PDF.
The Label caption will appear on the page as an HTML link; when clicked, the report will be exported. Action.Export PDF can be used as a child of a number of elements, including Button, Image, Charts, and more.
For more information about exporting to PDF, see our [Export to Adobe PDF](https://devnet.logianalytics.com/hc/en-us/articles/4406817419799-Export-to-Adobe-PDF).
