---
title: "Customizing Report Author Appearance"
id: 4406822489495
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822489495-Customizing-Report-Author-Appearance
updated_at: 2022-04-06T06:08:22Z
---

# Customizing Report Author Appearance

# Customizing Report Author Appearance

Report Author appearance can be changed most easily by applying a
theme to the report definition. Most of the screen shots in this
topic were taken with the *Signal* theme applied.

You can create your own custom theme, based on a standard theme, using the [Using the Theme Editor](https://devnet.logianalytics.com/hc/en-us/articles/4406818044055-Using-the-Theme-Editor) tool.

## Changing Appearance Using Style Classes

Report Author appearance can be also customized using **style** **classes** and Info Studio provides the following standard style sheet:

*<YourAppFolder>*\rdTemplate\rdReportAuthor\reportAuthor.css

Developers can override classes in this style sheet by *copying* them to their application style sheet and modifying them there.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) Do not make changes in the standard style sheet in the rdTemplate folder.

## Changing Appearance Using Template Modifiers

The Report Author element uses a "template file" to define certain
element properties that are not otherwise available as attributes to the
developer for modification. These include language- and
culture-specific **Caption** attributes that you may want to change for
locale-based reasons (or you may simply want to change the captions to
better suit your application).

The Report Author element's **Template Modifier File** attribute
identifies a custom XML file developers can create containing elements
that will override the same elements in the template file.

The appearance of the Visual Gallery pop-up panel can also be modified using a Template Modifier File.

For example, the Report Author template file:

*<yourAppFolder>*\rdTemplate\rdReportAuthor\ReportAuthorTemplate.lgx

contains several Label elements. One of them has an ID =
"lblSwitchToDesignModeTrue"; this controls one of the Design button captions. It can be modified
by changing the Caption associated with that Label element.
To change the caption from its default "Design" to "Create", create your own XML file, identify it in the Template Modifier
File attribute, and add this code to it:

<TemplateModifier>  
 <SetAttribute ID="lblSwitchToDesignModeTrue" Caption="Create" />  
</TemplateModifier>

You can set the attributes for any number of elements in this file;
examine the ReportAuthorTemplate.lgx file to learn the ID and Caption
attributes available. Other template files exist in the same folder for the Settings panels.

The template modifier file can be in any folder
accessible to the application; if a fully-qualified file path is not
provided in the Template Modifier File attribute value, then the
application expects it to be in its \_SupportFiles folder.

More detailed information about template modifier files can be found in [Template Modifier Files](https://devnet.logianalytics.com/hc/en-us/articles/4406817877655-Template-Modifier-Files).
