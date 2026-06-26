---
title: "Selecting the Positioning Scheme"
id: 4419723113495
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723113495-Selecting-the-Positioning-Scheme
updated_at: 2022-07-17T01:40:12Z
---

# Selecting the Positioning Scheme

# Selecting the Positioning Scheme

While Flow positioning is the default, the positioning scheme can be selected on a report-by-report basis.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699862935/positionele_04.png)

The positioning scheme is controlled, as shown above, by selecting the **Report** (root or top) element in a definition and selecting the desired scheme in its **Element Positioning** attribute value. A blank entry selects the default scheme, *Flow* positioning.

Two things happen when **Absolute** positioning is selected. First, all elements that can contain other elements (Division, Body, Row, etc.) are given two "hidden" attributes: **absoluteTop**, and **absoluteLeft**. These attributes do not appear in the Attribute panel but are managed behind-the-scenes by Studio. The element will also have **Height** and **Width** attributes which may or may not be visible depending on the nature of the element. These attributes allow the Logi
Server engine to accurately place elements on the page when a report is being generated.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699863191/positionele_05.png)

The second thing that happens is that the bottom of the Workspace panel acquires a new tab, the **Layout** tab, as shown above. Clicking this tab opens the **Layout editor**.

## Switching Back from Absolute to Flow

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599319/criticalicon.png) You should use caution when converting to Absolute positioning. Switching back to Flow positioning later may not completely return your report to its former state. When you switch back to Flow positioning from Absolute positioning, Studio will remove *most* of the attributes mentioned above. However, blanket removal is not possible, as you may have added desired attributes, such as Height
and Width, manually.
So, don't switch to Absolute positioning unless you really, absolutely,
have a need
to do so.
