---
title: "Word - Hiding Elements When Exporting"
id: 4419722911127
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722911127-Word-Hiding-Elements-When-Exporting
updated_at: 2022-07-17T01:49:23Z
---

# Word - Hiding Elements When Exporting

# Word - Hiding Elements When Exporting

When exporting to Word, youcommonly want to hide some of the elements in the report page, like the Export button or link. This can be done very easily using Show Modes, see [Show Modes](https://devnet.logianalytics.com/hc/en-us/articles/4419707995543-Show-Modes).

![](https://devnet.logianalytics.com/hc/article_attachments/4419706826135/exportword_06.png)

In the example shown above, the definition on the left includes a Label (styled as a button) that can be clicked to export the report to Word. However, when it's exported, shown on the right, the Export button appears in the Word document. We don't want that text to appear in the document.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706826391/exportword_07.png)

To "hide" the button in the exported document, simply place the elements beneath a **Division** element, as shown above. This element supports Show Modes, which the Label does not.
Then set the Division element's **Show Modes** attribute value to the built-in *rdBrowser* value, as shown above. Elements with this ShowMode value will only be visible in the browser.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699723415/exportword_08.png)

When the report is run and exported, as shown above, the document no longer includes the "Export to Word" button.
