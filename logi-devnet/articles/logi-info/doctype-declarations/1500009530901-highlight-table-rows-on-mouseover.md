---
title: "Highlight Table Rows on MouseOver"
id: 1500009530901
section: "Doctype Declarations"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009530901-Highlight-Table-Rows-on-MouseOver
updated_at: 2021-06-17T01:58:23Z
---

# Highlight Table Rows on MouseOver

# Highlight Table Rows on MouseOver

In order to increase the "readability" of data tables, especially wide data tables, it's often useful to be able to **highlight the entire row** that the cursor is hovering over.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771754135/tblrows_06.png)

This effect is shown in the example above and can be created using a simple style class.

The CSS used to create the effect is:

|  |  |
| --- | --- |
|  | #yourTableElementID  TR:hover TD   {     background-color: #f2e8da;    } |

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif)Note that, in order for this to work with **Internet Explorer**, your application must be configured for a **Doctype** (i.e. the General element's Doctype attribute value in the \_Settings definition cannot be set to *None*).
