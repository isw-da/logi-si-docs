---
title: "Analysis Chart - Customizing Analysis Chart Appearance"
id: 4406822082967
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822082967-Analysis-Chart-Customizing-Analysis-Chart-Appearance
updated_at: 2022-04-06T06:03:07Z
---

# Analysis Chart - Customizing Analysis Chart Appearance

# Analysis Chart - Customizing Analysis Chart Appearance

Analysis Chart appearance can be changed most easily by applying a
theme to the report definition. Most of the screen shots in this
document were taken with the *Signal* theme applied.

You can create your own custom theme, based on a standard theme, [Using the Theme Editor](https://devnet.logianalytics.com/hc/en-us/articles/4406818044055-Using-the-Theme-Editor) tool.

## Changing Appearance Using Style Classes

Analysis Chart appearance can be also customized using **style** **classes** and Info Studio provides the following standard style sheet for all Analysis Charts:

*<YourAppFolder>*\rdTemplate\rdAnalysisChart\rdAcStyle.css

Developers can override classes in this style sheet by *copying* them to their application style sheet and modifying them there.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) Do not make changes in the standard style sheet in the rdTemplate folder.

## Changing Appearance Using Template Modifiers

The Analysis Chart element uses a "template file" to define certain element properties that are not otherwise available as attributes to the developer for modification. These include language- and culture-specific **Caption** attributes that you may want to change to match the locale (or you may simply want to change the captions to better suit your application).

The Analysis Chart element's **Template Modifier File** attribute identifies a custom XML file developers can create containing elements that will override the same elements in the template file.

For example, the Analysis Chart template file:

*<yourAppFolder>*\rdTemplate\rdAnalysisChart\rdAcTemplate.lgx

contains several Label elements. One of them has an ID of "lblChartXLabelColumn\_rdAcID"; this controls the caption text that appears beside the Label Column input select list. This text can be modified by changing the Caption associated with that Label element.
To change the text from its default "Label Column" to "X-axis Data Column", create your own XML file, identify it in the Template Modifier File attribute, and add this code to it:

<TemplateModifier>  
<SetAttribute ID="lblChartXLabelColumn\_rdAcID" Caption="X-axis Data Column" />  
</TemplateModifier>

You can set the attributes for any number of elements in this file; examine the rdAcTemplate.lgx file to learn the ID and Caption attributes available. The template modifier file can be in any folder accessible to the web application; if a fully-qualified file path is not provided in the Template Modifier File attribute value, then the application expects the file to be in its \_SupportFiles folder.

More detailed information can be found in [Template Modifier Files](https://devnet.logianalytics.com/hc/en-us/articles/4406817877655-Template-Modifier-Files).
