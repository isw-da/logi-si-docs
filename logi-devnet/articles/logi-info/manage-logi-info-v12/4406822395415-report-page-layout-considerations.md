---
title: "Report Page Layout Considerations "
id: 4406822395415
section: "Manage - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822395415-Report-Page-Layout-Considerations
updated_at: 2022-04-06T06:06:58Z
---

# Report Page Layout Considerations 

# Report Page Layout Considerations

Special care must be taken when designing reports that will be globalized, especially if they include user input elements. For example:

* **Avoid using fixed widths and heights**. When elements include sizing attributes, use a percentage, rather than a fixed number of pixels, whenever possible.
* **Plan for the possibility of text-wrapping**. Labels, captions, and other text may become longer when displayed in some languages, overrunning or wrapping within the space provided for them.
* **Separate captions from input elements**. Use Row, Rows, and Column elements to create your own HTML table to contain input elements, rather than an Input Grid. Use separate Label elements for input element captions rather than using their Caption attributes.

In general, any physical boundaries on the report page that may be affected by the size and length of text or data, which may change with different cultures,need to be given special consideration.
