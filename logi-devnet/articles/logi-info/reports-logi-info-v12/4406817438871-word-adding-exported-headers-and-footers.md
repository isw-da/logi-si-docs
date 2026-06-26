---
title: "Word - Adding Exported Headers and Footers"
id: 4406817438871
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817438871-Word-Adding-Exported-Headers-and-Footers
updated_at: 2022-04-06T06:06:04Z
---

# Word - Adding Exported Headers and Footers

# Word - Adding Exported Headers and Footers

Exported reports are paginated and you may want to have a report header and/or footer appear on each exported page. This can be done, without affecting the normal appearance of the HTML report output in a browser, using the **Printable Paging** element.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563294871/exportword_04.png)  

As shown above, the Printable Paging element has been added beneath the report's top-level Report element. It has its own **Page Header** and **Page Footer** child elements which are containers for **Label** elements. In the example above, the captions of the footer label could use the @Date.Today~ and @Function.PageNumber~ tokens to get their values.

When the report is run, the header and footer under the Printable Paging element will *not* be visible. When the report is exported, the header and footer *will be* visible on each exported page.
