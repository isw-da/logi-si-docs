---
title: "Inserting Code Directly   "
id: 4419707960727
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707960727-Inserting-Code-Directly
updated_at: 2022-07-17T01:29:49Z
---

# Inserting Code Directly   

# Inserting Code Directly

The **Include Script** element can be used to insert script, entered into one of its attributes, directly into the HTML output when a page is generated. Script inserted in this way runs in the browser.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699995287/scripting_04.png)

The example above shows the Include Script element as a child of the **Report Header** but it can be the child of the Body, Page Footer, and about 20 other elements. The inserted script will appear in the HTML code between < SCRIPT> tags (do *not* include these tags in the Include Script element's **Included Script** attribute value).

You can also use Include Script to insert tags, such as HTML < META> tags, into the page's < HEAD> section. For more information, see [Insert HTML into Reports](https://devnet.logianalytics.com/hc/en-us/articles/4419722951831-Insert-HTML-into-Reports).
