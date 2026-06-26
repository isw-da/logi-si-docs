---
title: "Excel - Export Considerations"
id: 4419707571095
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707571095-Excel-Export-Considerations
updated_at: 2022-07-17T01:49:45Z
---

# Excel - Export Considerations

# Excel - Export Considerations

The following apply when exporting to Excel:

* Chart color "transparency" may not be available in exports to Excel.
* HTML files embedded in a report may not be exported correctly; success is dependent on the nature of the external HTML file, its adherence to proper XHTML syntax, and other factors.
* Summary Rows, if present in a Data Table, will be exported to Excel but the summarized data will appear in the worksheet as a text value, not a number.
* Bulleted lists are not supported (using the Bullet element)
* The Rectangle element cannot be exported.
* When a Multi-Column List is exported to Excel, its data is exported into a single Excel column, not multiple columns.
