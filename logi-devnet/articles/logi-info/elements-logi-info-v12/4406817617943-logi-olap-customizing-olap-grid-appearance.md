---
title: "Logi OLAP - Customizing OLAP Grid Appearance"
id: 4406817617943
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817617943-Logi-OLAP-Customizing-OLAP-Grid-Appearance
updated_at: 2022-04-06T06:07:14Z
---

# Logi OLAP - Customizing OLAP Grid Appearance

# Logi OLAP - Customizing OLAP Grid Appearance

OLAP Grid appearance can be changed most easily by applying a theme to the
report definition. Most of the screen shots in this topic were taken
with the *Signal* theme applied.
You can create your own custom theme, based on a standard theme, using
the
[Theme Editor](https://devnet.logianalytics.com/hc/en-us/articles/4406818043031-Theme-Editor) tool.

## Changing Appearance Using Style Classes

OLAP Grid appearance can be also customized using **style** **classes** and Logi Studio provides the following standard style sheet
for all OLAP Grids:

*<YourAppFolder>*\rdTemplate\rdOlapGrid\rdOgStyle.css

Developers can override classes in this style sheet by
*copying* them to their application style sheet and modifying them
there.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png)Do not make changes in the standard style sheet in the
rdTemplate folder.

## Changing Appearance Using Template Modifiers

The OLAP Grid element uses a "template file" to define certain
element properties that are not otherwise available as attributes to the
developer for modification. These include language- and culture-specific
**Caption** attributes that you may want to change for locale-based
reasons (or you may simply want to change the captions to better suit your
application).
The element's **Template Modifier File** attribute identifies a custom
XML file developers can create containing elements that will override the
same elements in the template file.
For example, the OLAP Grid template file:

*<yourAppFolder>*\rdTemplate\rdOlapGrid\rdOgTemplate.lgx

contains several Label elements. One of them has an ID of
"lblShowEmpty"; this controls the caption that appears next to
the "Show empty members" check box. This text can be modified by
changing the **Caption** associated with that Label element.
For example, to change the Label text from its default to "View empty
members", create your own XML file, identify it in the OLAP Grid
element's Template Modifier File attribute, and add this code to it:

<TemplateModifier>  
 <SetAttribute ID="lblShowEmpty"
Caption="View empty members" />  
 </TemplateModifier>
You can set the attributes for any number of elements in this file;
examine the rdOgTemplate.lgx file to learn the ID and Caption attributes
available. The template modifier file can be in any folder accessible to
the web application; if a fully-qualified file path is not provided in the
Template Modifier File attribute value, then the application expects it to
be in your project's \_SupportFiles folder.
More detailed information about template modifier files can be found in
[Template Modifier Files](https://devnet.logianalytics.com/hc/en-us/articles/4406817877655-Template-Modifier-Files).
