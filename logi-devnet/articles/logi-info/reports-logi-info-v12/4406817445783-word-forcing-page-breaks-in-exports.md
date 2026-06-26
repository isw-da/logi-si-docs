---
title: "Word - Forcing Page Breaks in Exports"
id: 4406817445783
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817445783-Word-Forcing-Page-Breaks-in-Exports
updated_at: 2022-04-06T06:06:08Z
---

# Word - Forcing Page Breaks in Exports

# Word - Forcing Page Breaks in Exports

When a report is paginated during an export, it may be useful to be able to force a page break, for example, to ensure that sections of the report start on new pages. This can be done using the **Printer Page Break** element.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563294231/exportword_05.png)

You can add one or more **Printer Page****Break** elements beneath the **Body** element to break the exported pages where desired. In the example above, these elements ensure that the "dtProducts" table and the "dtOrders" table start on new pages. When the report is viewed in the browser, however, like the Printable Paging element, the Printer Page Break element has no effect.

## Forcing a Data Table Row Break

When working with data tables with multi-line rows, you may want to ensure that rows break cleanly across pages of their Word exports. In other words, they want to prevent different lines of the same data table row from appearing on different Word document pages. This can be accomplished through CSS, using code like:

.noPageBreakCell { page-break-inside: avoid; }

Assigning the above class to a **Data Table Column** element will create the desired effect.
