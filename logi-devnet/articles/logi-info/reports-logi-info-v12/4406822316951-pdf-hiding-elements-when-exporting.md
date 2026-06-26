---
title: "PDF - Hiding Elements when Exporting"
id: 4406822316951
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822316951-PDF-Hiding-Elements-when-Exporting
updated_at: 2022-04-06T06:06:01Z
---

# PDF - Hiding Elements when Exporting

# PDF - Hiding Elements when Exporting

When exporting to PDF, developers commonly want to hide some of the elements in the report page, like the Export button or link. This can be done very easily using **Show Modes**.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563305367/exportpdf_07.png)![](https://devnet.logianalytics.com/hc/article_attachments/4417563305495/exportpdf_07a.png)

Consider the example shown above. The definition, on the left, includes a button that can be clicked to export the report to a PDF. However, when it's exported, shown on the right, the **Export to PDF** button appears in the PDF itself. We don't want that button to appear in the PDF.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583950743/exportpdf_08.png)![](https://devnet.logianalytics.com/hc/article_attachments/4417563306007/exportpdf_08a.png)

The first step in "hiding" the button in the export is to place the button beneath a **Division** element. This element supports Show Modes, which the button, by itself, does not. Set the Division element's **Show Modes** attribute value to an arbitrary string, such as "NoExport", as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563306391/exportpdf_09.png)![](https://devnet.logianalytics.com/hc/article_attachments/4417575713687/exportpdf_09a.png)

Then set the Target.PDF element's **Report Show Modes** attribute value to an arbitrary string that *does not match* the string used in the previous step, as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575714327/exportpdf_10.png)

When the report is run and exported, as shown above, the PDF no longer includes the **Export to PDF** button. Any element whose Show Modes attribute value does not match the Target.PDF element's Report Show Modes attribute will not appear in the export.
