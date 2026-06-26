---
title: "Analysis Grid Developers - Customizing Analysis Grid Appearance"
id: 4419715054103
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715054103-Analysis-Grid-Developers-Customizing-Analysis-Grid-Appearance
updated_at: 2022-07-17T02:09:25Z
---

# Analysis Grid Developers - Customizing Analysis Grid Appearance

# Analysis Grid Developers - Customizing Analysis Grid Appearance

Analysis Grid appearance can be changed most easily by applying a theme to the report definition. Most of the screen shots in this topic were taken with the *Signal* theme applied.

You can create your own custom theme, based on a standard theme, [Use the Theme Editor](https://devnet.logianalytics.com/hc/en-us/articles/4419723274775-Use-the-Theme-Editor) tool.

## Changing Appearance Using Style Classes

Analysis Grid appearance can also be customized using **style classes** and Logi Studio provides the following standard style sheet for all Analysis Grids:

*<YourAppFolder>*\rdTemplate\rdAnalysisGrid\rdAg10Style.css

Developers can override classes in this style sheet by *copying* them into their own application style sheet and modifying them there.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png)

* Do not make changes in the standard style sheet in the rdTemplate folder!
* If you're using a Theme, it will override some of the Analysis Grid classes.

## Changing Appearance Using Template Modifiers

The Analysis Grid element uses a "template file" to define certain element properties that are not otherwise available as attributes to the developer for modification. These include language- and culture-specific **Caption** attributes that you may want to change for locale-based reasons (or you may simply want to change the captions to better suit your application).

The element's **Template Modifier File** attribute identifies a custom XML file developers can create containing elements that will override the same elements in the template file.

For example, the Analysis Grid template file:

*<yourAppFolder>*\rdTemplate\rdAnalysisGrid\rdAg10Template.lgx

contains several Label elements. One of them has an ID of "lblInstructCols"; this controls the "help text" that is displayed when the Layout icon is clicked. This text can be modified by changing the Caption associated with that Label element.
To change the text from its default "Reorder and hide columns" to "Rearrange and hide columns", create your own XML file, identify it in the Template Modifier File attribute, and add this code to it:

<?xml version="1.0" encoding="UTF-8"?>  
<TemplateModifier>  
 <SetAttribute ID="lblInstructCols" Caption="Rearrange and hide columns" />  
</TemplateModifier>

You can set the attributes for any number of elements in this file; examine the rdAgTemplate.lgx file to learn the ID and Caption attributes available. The template modifier file can be in any folder accessible to the web application; if a fully-qualified file path is not provided in the Template Modifier File attribute value, then the application expects it to be in your applications's \_SupportFiles folder.

For more detailed information about template modifier files, see [Template Modifier Files](https://devnet.logianalytics.com/hc/en-us/articles/4419715482903-Template-Modifier-Files).

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png)![](https://devnet.logianalytics.com/hc/article_attachments/7522745474327/_newplus.jpg) New for 14.1 You can also format your chart's label and caption directly in the user interface. For more information, see  [New for 14.1 Analysis Grid - Editing Chart Labels and Captions](https://devnet.logianalytics.com/hc/en-us/articles/4419707287959-Analysis-Grid-Editing-Chart-Labels-and-Captions-).
