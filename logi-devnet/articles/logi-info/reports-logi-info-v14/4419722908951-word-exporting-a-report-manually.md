---
title: "Word - Exporting a Report Manually"
id: 4419722908951
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722908951-Word-Exporting-a-Report-Manually
updated_at: 2022-07-17T01:49:28Z
---

# Word - Exporting a Report Manually

# Word - Exporting a Report Manually

Here's an example of how to create a report with a link that exports manually:

### 

1. In your Report definition, add an **Action.Export Native Word** element to a Label, Image, Button or Chart element, as shown above.
2. Add the required **Target.Native Word** element.
3. If the report to export *is* the current report, you don't need to do anything else. Just save your definition and browse your report; it's that simple.
4. All Target.Native Word element attributes are *optional*. The default settings will export the current report in its entirety.
5. If the report to export *is not* the current report, specify that report by setting the Target.Native Word element's **Report Definition File** attribute.
6. The exported file will be given a random file name and a .doc file extension (Word 2003 and earlier) unless you specify a specific file name and the .docx extension (Word 2007+) in the **Export Filename** attribute.

What Happens: The report is exported to a temporary file which is created in your project folder's rdDownload folder on the web server. The temp file is then returned to the client and opened in your browser. You may be prompted to *View* or *Save* the file. Temporary files on the server are cleaned up automatically over time.
