---
title: "PDF - Adding Exported Headers and Footers"
id: 4406817416599
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817416599-PDF-Adding-Exported-Headers-and-Footers
updated_at: 2022-04-06T06:05:57Z
---

# PDF - Adding Exported Headers and Footers

# PDF - Adding Exported Headers and Footers

Reports exported to PDF are paginated and you may want to have a report header and/or footer appear on each exported page. This can be done, without affecting the normal appearance of the HTML report output in a browser, using the **Printable Paging** element.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583954199/exportpdf_05.png)

As shown above, the **Printable Paging** element is added beneath the report's top-level Report element. It has its own **Page Header** and **Page Footer** child elements which are containers for **Label** and other elements. In the example above, the captions of the footer labels could use the @Date.Today~, @Function.PageCount~, and @Function.PageNumber~
tokens.

When the report is run and viewed in a browser, the header and footer under the Printable Paging element will *not* be visible. When the report is exported to PDF, the header and footer *will be* visible on each exported page.

Suppose you want to have different-looking headers or footers on an exported page depending on the page number? For example, you might want Page 1 to have a fancy header and the following pages, a less-fancy header. Developers can do this using **Division** elements:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563309463/exportpdf_05a.png)![](https://devnet.logianalytics.com/hc/article_attachments/4417575715735/exportpdf_05b.png)

As shown in the example above, place Division elements beneath the Page Header element and then set their **Condition** attributes to evaluate the PageNumber token. The Condition attribute value for the first division is shown, and the value for the second division might be @Function.PageNumber~ > 1. Each division, and its child elements, will appear in the export then, depending on the page number. The same functionality
is available in exported report footers.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) Adding a header or footer beneath the Printable Paging element will **increase** rendering time. Their inclusion causes the export engine to have to make multiple passes through the entire report while generating the PDF, and the performance hit incurred may be acceptable for short reports but not for longer reports. The alternative
is to use regular Report Header and Report Footer elements, which will appear in the report in a browser, rather than the Printable Paging element's Page Header and Page Footer child elements.
