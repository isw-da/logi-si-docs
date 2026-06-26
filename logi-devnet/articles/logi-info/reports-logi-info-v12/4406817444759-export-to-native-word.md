---
title: "Export to Native Word"
id: 4406817444759
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817444759-Export-to-Native-Word
updated_at: 2022-04-06T06:06:08Z
---

# Export to Native Word

# Export to Native Word

Exporting reports into **Microsoft Word** documents is a popular method of formatting and presenting data.

The following topics discuss techniques for exporting to Word:

* [Exporting a Report Manually](https://devnet.logianalytics.com/hc/en-us/articles/4406822325271-Word-Exporting-a-Report-Manually#Manually)
* [Exporting a Report Programmatically](https://devnet.logianalytics.com/hc/en-us/articles/4406817443735-Word-Exporting-a-Report-Programmatically-#Programmatically)
* [Adding Exported Headers and Footers](https://devnet.logianalytics.com/hc/en-us/articles/4406817438871-Word-Adding-Exported-Headers-and-Footers#Footers)
* [Forcing Page Breaks in Exports](https://devnet.logianalytics.com/hc/en-us/articles/4406817445783-Word-Forcing-Page-Breaks-in-Exports#Forcing)
* [Hiding Elements When Exporting](https://devnet.logianalytics.com/hc/en-us/articles/4406817446807-Word-Hiding-Elements-When-Exporting#Hiding)
* [Exporting More Info Rows](https://devnet.logianalytics.com/hc/en-us/articles/4406822324375-Word-Exporting-More-Info-Rows#MoreInfo)
* [Cascading Style Sheet Support](https://devnet.logianalytics.com/hc/en-us/articles/4406817439895-Word-Cascading-Style-Sheet-Support#CSS)
* [Debugging Exports](https://devnet.logianalytics.com/hc/en-us/articles/4406817441047-Word-Debugging-Exports#Debugging)
* [Export Considerations](https://devnet.logianalytics.com/hc/en-us/articles/4406822323479-Word-Export-Considerations#Considerations)

  

## About Exporting Reports to Native Word

Exporting data into a Word document allows for additional formatting to be applied, and for narrative text to be included with visualizations. Logi Info includes specific elements for exporting data into documents that can be edited using Microsoft's widely-used Word program.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) Aways use the **Action.Export Native Word** element in your Logi applications. Earlier versions of Logi Info used the deprecated Action.Export Word Or Excel element and it's been retained in Logi Studio only for backward compatibility.

### Manual or Programmatic Export

You can configure your application to export data to Word in two ways:

* **Manually** - The user clicks a link or button in a report to initiate the export and the result is made available for viewing in a browser or can be saved locally. The export elements are added into the report definition.
* **Programmatically** - The export occurs when a [Process Tasks](https://devnet.logianalytics.com/hc/en-us/articles/4406817796375-Process-Tasks) executes, triggered by an user-initiated event or scheduled event, and the result is written out as a Word file on the web server. The export elements are added into the process definition.

You may use both techniques in the same application.
