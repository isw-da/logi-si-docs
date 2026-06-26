---
title: "Analysis Filter - Customizing the Analysis Filter Appearance"
id: 4419700092951
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419700092951-Analysis-Filter-Customizing-the-Analysis-Filter-Appearance
updated_at: 2022-07-17T02:02:23Z
---

# Analysis Filter - Customizing the Analysis Filter Appearance

# Analysis Filter - Customizing the Analysis Filter Appearance

Analysis Filter appearance can be changed most easily by applying a
theme to the report definition. Most of the screen shots in this
document were taken with the *Signal* theme applied. You can also create your own custom theme, based on a standard theme, using the Theme Editor tool. For more information, see [Themes](https://devnet.logianalytics.com/hc/en-us/articles/4419723357847-Themes).

## Changing Appearance Using Style Classes

Analysis Filter appearance can be also customized using **style** **classes** and the standard classes for it are taken from the Analysis Grid style sheet:

*<yourAppFolder>*\rdTemplate\rdAnalysisGrid\rdAg10Style.css

Developers can override classes in this style sheet by *copying* them to their application style sheet and modifying them there.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599319/criticalicon.png) Do not make changes in the standard style sheet in the rdTemplate folder.

## Changing Appearance Using Template Modifiers

The Analysis Filter element uses a "template file" to define certain element properties that are not otherwise available as attributes to the developer for modification. These include language- and culture-specific **Caption** attributes that you may want to change to match the locale (or you may simply want to change the captions to better suit your application).

The Analysis Filter element's **Template Modifier File** attribute identifies a custom XML file developers can create containing elements that will override the same elements in the template file.

For example, the Analysis Filter template file:

*<yourAppFolder>*\rdTemplate\rdAnalysisFilter\rdAfTemplate.lgx

contains several Label elements. One of them has an ID of "lblFilterColumn\_rdAfID"; this controls the caption text that appears beside the Filter Column drop-down list in Design view. This text can be modified by changing the Caption associated with that Label element.
To change the text from its default "Filter Column" to "Column to filter by", create your own XML file, identify it in the Template Modifier File attribute, and add this code to it:

<TemplateModifier>  
<SetAttribute ID="lblFilterColumn\_rdAfID" Caption="Column to filter by" />  
</TemplateModifier>

You can set the attributes for any number of elements in this file; examine the rdAfTemplate.lgx file to learn the ID and Caption attributes available. The template modifier file can be in any folder accessible to the web application; if a fully-qualified file path is not provided in the Template Modifier File attribute value, then the application expects the file to be in its \_SupportFiles folder.

More detailed information about template modifier files can be found in [Template Modifier Files](https://devnet.logianalytics.com/hc/en-us/articles/4419715482903-Template-Modifier-Files).
