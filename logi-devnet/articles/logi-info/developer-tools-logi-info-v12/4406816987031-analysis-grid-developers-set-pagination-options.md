---
title: "Analysis Grid Developers - Set Pagination Options"
id: 4406816987031
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406816987031-Analysis-Grid-Developers-Set-Pagination-Options
updated_at: 2022-04-06T06:03:14Z
---

# Analysis Grid Developers - Set Pagination Options

# Analysis Grid Developers - Set Pagination Options

This feature allows users to determine how many **rows of data** will appear in the data table:

![](https://devnet.logianalytics.com/hc/article_attachments/4417584190359/workag_15.png)

Selecting the paging option **Show all rows** will display *all* of the data at once in the data table; **Show paging**
will display a subset of rows and also include the paging controls.
Developers may not want to allow users to select all rows as it may result in a lengthy delay while data is
retrieved. You have the option to hide this
radio button from users by setting the Analysis Grid element's **Disable Show All Rows** attribute to *True*.

When Show Paging is selected, one of three styles of **paging controls** is displayed, depending on how the developer configures the Analysis Grid element in the report definition:

![](https://devnet.logianalytics.com/hc/article_attachments/4417591975959/workag_16.png)

If the Analysis Grid element's **Show Page Number** attribute is set to *True*, the navigation controls, with page number display and input, as shown above, will appear.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584190743/workag_17.png)

If the Show Page Number attribute is set to *False*, the navigation controls will appear, as shown above, but without a page number.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584191255/workag_18.png)

And, finally, if the Show Page Number attribute is set to *Numbered*, or is left blank, the navigation icons will appear, as shown above, along with a range of page numbers. In addition, two other attributes will become active: **Numbered Page Count**, which specifies how many numbers will be shown at a time (default = *10*), and **Current Page Class**, which allows the number for the current page to be styled (color, size, background, etc.) differently
from the others.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) The look of the navigation controls will vary depending on which Theme is applied.
