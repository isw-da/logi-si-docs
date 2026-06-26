---
title: "PDF - Exporting a Report Manually"
id: 4419715289367
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715289367-PDF-Exporting-a-Report-Manually
updated_at: 2022-07-17T02:24:27Z
---

# PDF - Exporting a Report Manually

# PDF - Exporting a Report Manually

Here's an example of how to create a report with a link that allows the report to be exported manually:

### 

1. In your report definition, add an **Action.Export PDF** element as the child of a **Label**, **Image**, **Button** or **Chart** element, as shown above.
2. Beneath it, add the required **Target.PDF** element.
3. If the report to export *is* the current report, you don't need to do anything else. Just save your definition, preview or browse your report, and click the link to export it. It should open in the PDF viewer associated with your browser. It's that simple.
4. ![](https://devnet.logianalytics.com/hc/article_attachments/7522745474327/_newplus.jpg) New for 14.2 To specify the way PDFs exports are generated, set the Content Disposition attribute in the Target.PDF element to either **Attachment** or **Inline.** By default, the attribute is "empty", PDFs use browser settings. When the attribute is set to "Attachment", you are prompted to download the PDF. When the attribute is set to "Inline", you are prompted to display the PDF inside the Web page.
5. In order to export the current report while maintaining any **sort order** the user may have applied, set the Target.PDF's **Report Definition File** attribute to *CurrentReport*.
6. If the report to export *is not* the current report, specify that report by setting the Target.PDF's **Report Definition File** attribute appropriately.
7. If you wish to export *only* a specific Data Table, provide its ID in the **Export Data Table ID** attribute. This prevents anything else in the report, such as headers or footers, images, etc., from being exported.

What happens: the report is exported to a *temporary* PDF file which is created in your project folder's rdDownload folder on the web server. The temp file is then opened automatically in your browser. Temporary files are cleanedup automatically over time.

If you wish to export to PDF in "landscape" page orientation, you should use the **Printable Paging** element, as described in [Creating Printable Reports](https://devnet.logianalytics.com/hc/en-us/articles/4419707767831-Creating-Printable-Reports).
