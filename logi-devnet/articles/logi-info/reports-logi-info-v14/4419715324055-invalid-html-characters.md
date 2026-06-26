---
title: "Invalid HTML Characters"
id: 4419715324055
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715324055-Invalid-HTML-Characters
updated_at: 2023-03-03T01:15:05Z
---

# Invalid HTML Characters

# Invalid HTML Characters

The Logi Server Engine may generate errors if it needs to read a string of characters as XML and that XML includes un-escaped, invalid XHTML characters.

A primary examples of this is when AJAX-style requests are used, such as Data Table sorting or paging (when **Ajax Paging** = *True* has been set), or use of an **Action.Refresh Element** that includes a Data Table or other data object. In these cases, the XML data may be indistinguishable from XML tags and reserved characters.

This can also happen when HTML is included in a report definition using the techniques discussed earlier.

The most common culprit in this scenario is the inclusion of unencoded "&" characters. In situations like those described above, the application will fail and produce an error message that looks like a parsing error.

Replacing the "&" character with "&amp;"is often an easy solution.
