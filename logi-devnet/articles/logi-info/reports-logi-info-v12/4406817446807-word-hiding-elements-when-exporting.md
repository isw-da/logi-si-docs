---
title: "Word - Hiding Elements When Exporting"
id: 4406817446807
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817446807-Word-Hiding-Elements-When-Exporting
updated_at: 2022-04-06T06:06:07Z
---

# Word - Hiding Elements When Exporting

# Word - Hiding Elements When Exporting

When exporting to Word, youcommonly want to hide some of the elements in the report page, like the Export button or link. This can be done very easily using Show Modes, see [Show Modes](https://devnet.logianalytics.com/hc/en-us/articles/4406818147095-Show-Modes).

![](https://devnet.logianalytics.com/hc/article_attachments/4417583941143/exportword_06.png)

In the example shown above, the definition on the left includes a Label (styled as a button) that can be clicked to export the report to Word. However, when it's exported, shown on the right, the Export button appears in the Word document. We don't want that text to appear in the document.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575702935/exportword_07.png)

To "hide" the button in the exported document, simply place the elements beneath a **Division** element, as shown above. This element supports Show Modes, which the Label does not.
Then set the Division element's **Show Modes** attribute value to the built-in *rdBrowser* value, as shown above. Elements with this ShowMode value will only be visible in the browser.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583941399/exportword_08.png)

When the report is run and exported, as shown above, the document no longer includes the "Export to Word" button.
