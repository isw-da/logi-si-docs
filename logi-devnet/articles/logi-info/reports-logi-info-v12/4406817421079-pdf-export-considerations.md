---
title: "PDF - Export Considerations"
id: 4406817421079
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817421079-PDF-Export-Considerations
updated_at: 2022-06-15T19:10:02Z
---

# PDF - Export Considerations

# PDF - Export Considerations

The following apply when exporting to PDF:

* The Login Info PDF export engine will not export data table captions in Java applications. Developers are advised to use a separate Label element, or a data table Header Row child element, set to *Top* position, instead of using the table's Caption attribute, to provide an exportable caption in Java apps.

* Chart color transparency is not available in exports to PDF. Non-animated charts displayed in Logi HTML reports are rendered as .png images and support transparency, however, when exported to PDF, these charts are rendered as .jpg images, which do not support transparency.
* It's not possible to support links that may use relative URLs in an exported document, as the document can be saved and relocated. As a result, links in general are *not* supported in exported PDFs. They will work when Studio's *Debugging Links* feature is turned on during development, but when that link is removed for a production release, they will no longer work.
* Data table column headers will be repeated on each page of PDF export *only* if there are no sub-elements within the report. This includes Sub Report, Sub Data Table, and More Info Row.
* Data table column headers will be repeated on each page of a PDF export *only* if there are one or more characters in the column header text. If you want a column that has no header text to be repeated, you must include a single space character in its Header attribute value.

* When exporting to a PDF from a web browser on different computers, the page dimensions may be affected by different screen resolutions. In addition, when using different browsers, exported reports may appear differently, as different browsers handle styling differently. Developers may care to use a Printable Paging element in their report definitions, to set absolute page dimensions. For more information, see [Creating Printable Reports](https://devnet.logianalytics.com/hc/en-us/articles/4406817768087).
* Exporting reports that include characters that are read right-to-left, such as Arabic, from a Windows server requires that special OS files be installed, as follows: Go to Regional and Language Options in Control Panel; select "Install files for complex script and right-to-left languages (including Thai)" under the Languages tab; when prompted, insert the Windows OS CD and run the install; restart the computer once the files are completely copied and the restart prompt comes up.
