---
title: "Word - Export Considerations"
id: 4419722907031
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722907031-Word-Export-Considerations
updated_at: 2022-07-17T01:49:31Z
---

# Word - Export Considerations

# Word - Export Considerations

The following apply when exporting to Word:

* Chart color transparency is not available in exports to Word. Non-animated charts displayed in Logi HTML reports are rendered as .png images and support transparency, however, when exported to Word, these charts are rendered as .jpg images, which do not support transparency.
* Embedded HTML files in a Logi report may not be exported correctly; success is dependent on the nature of the external HTML file, its adherence to proper XHTML syntax, and other factors.
* Background colors are only applied within tables
* Bulleted lists are not supported (using the Bullet element)
* Rectangle element is not supported
* Layout Positioning is not supported
* HideDuplicates element is not supported

keywords: MoreInfoRow
