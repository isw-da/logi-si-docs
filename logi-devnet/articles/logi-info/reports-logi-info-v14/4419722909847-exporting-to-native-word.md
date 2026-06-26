---
title: "Exporting to Native Word"
id: 4419722909847
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722909847-Exporting-to-Native-Word
updated_at: 2022-07-17T02:07:48Z
---

# Exporting to Native Word

# Exporting to Native Word

Exporting reports into **Microsoft Word** documents is a popular method of formatting and presenting data.

The following topics discuss techniques for exporting to Word:

* [Exporting a Report Manually](https://devnet.logianalytics.com/hc/en-us/articles/4419722908951-Word-Exporting-a-Report-Manually#Manually)
* [Exporting a Report Programmatically](https://devnet.logianalytics.com/hc/en-us/articles/4419715295895-Word-Exporting-a-Report-Programmatically-#Programmatically)
* [Adding Exported Headers and Footers](https://devnet.logianalytics.com/hc/en-us/articles/4419715294487-Word-Adding-Exported-Headers-and-Footers#Footers)
* [Forcing Page Breaks in Exports](https://devnet.logianalytics.com/hc/en-us/articles/4419707576727-Word-Forcing-Page-Breaks-in-Exports#Forcing)
* [Hiding Elements When Exporting](https://devnet.logianalytics.com/hc/en-us/articles/4419722911127-Word-Hiding-Elements-When-Exporting#Hiding)
* [Exporting More Info Rows](https://devnet.logianalytics.com/hc/en-us/articles/4419722907927-Word-Exporting-More-Info-Rows#MoreInfo)
* [Cascading Style Sheet Support](https://devnet.logianalytics.com/hc/en-us/articles/4419722906007-Word-Cascading-Style-Sheet-Support#CSS)
* [Debugging Exports](https://devnet.logianalytics.com/hc/en-us/articles/4419707575447-Word-Debugging-Exports#Debugging)
* [Export Considerations](https://devnet.logianalytics.com/hc/en-us/articles/4419722907031-Word-Export-Considerations#Considerations)

  

## About Exporting Reports to Native Word

Exporting data into a Word document allows for additional formatting to be applied, and for narrative text to be included with visualizations. Logi Info includes specific elements for exporting data into documents that can be edited using Microsoft's widely-used Word program.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) Aways use the **Action.Export Native Word** element in your Logi applications. Earlier versions of Logi Info used the deprecated Action.Export Word Or Excel element and it's been retained in Logi Studio only for backward compatibility.

### Manual or Programmatic Export

You can configure your application to export data to Word in two ways:

* **Manually** - The user clicks a link or button in a report to initiate the export and the result is made available for viewing in a browser or can be saved locally. The export elements are added into the report definition.
* **Programmatically** - The export occurs when a [Process Tasks](https://devnet.logianalytics.com/hc/en-us/articles/4419715442583-Process-Tasks) executes, triggered by an user-initiated event or scheduled event, and the result is written out as a Word file on the web server. The export elements are added into the process definition.

You may use both techniques in the same application.
