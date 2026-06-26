---
title: "Logi Info - Font Options with Canvas Charts"
id: 360049268093
section: "FAQs"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/360049268093-Logi-Info-Font-Options-with-Canvas-Charts
updated_at: 2021-12-06T13:13:40Z
---

# Logi Info - Font Options with Canvas Charts

**Question:**

How can the font styling be modified for Canvas Charts?

**Answer:**

There are several options available within Logi Info to customize Chart Canvas Fonts and Font Sizes.  Note each of these examples purposefully uses a different Google-hosted Google Font which is specified using a Style element.

**Using Chart Canvas Child Elements**

The most specific way to modify the font displayed within a canvas chart is to specify these properties on each child element of the Canvas Chart definition.  This solution provides very targeted control of the font for a Canvas Chart.

![2.jpg](https://devnet.logianalytics.com/hc/article_attachments/360073152633/2.jpg)![1.jpg](https://devnet.logianalytics.com/hc/article_attachments/360071918754/1.jpg)

**Using Modifier Files**

The way that Logi provides default property values applied to elements is through a Modifier XML file.  There are three different types of Modifier XML files (Template, Definition and Theme).  The Template modifier only applies to Logi Super Elements such as a Dashboard or Analysis Grid.

Template Modifier Files:  <https://documentation.logianalytics.com/logiinfov12/content/template-modifier-files.htm?Highlight=template>

Definition Modifier Files:  <https://documentation.logianalytics.com/logiinfov12/content/definition-modifier-files.htm?Highlight=modifier>

Working with Themes:  <https://documentation.logianalytics.com/logiinfov12/content/working-with-themes.htm?Highlight=theme%20modifier>

If you want the Font properties to be provided by default to all Chart Canvas elements within a definition, you could use a definition modifier file to modify the definition’s XML prior to rendering.

For example, the following solution will set the Chart Caption Style on all Canvas Charts.

Definition Modifier XML:

```
<Sample>  
  
 <UpdateOrAppendChildElement XPath=".//ChartCanvas" >  
 <NewElement>  
 <ChartCaptionStyle FontFamily="Inconsolata" FontWeight="Normal" FontColor="#000000" FontSize="24" AlignmentHorizontal="Center"/>  
 </NewElement>  
 </UpdateOrAppendChildElement>  
  
</Sample>
```

![3.jpg](https://devnet.logianalytics.com/hc/article_attachments/360073152673/3.jpg)![4.jpg](https://devnet.logianalytics.com/hc/article_attachments/360073152653/4.jpg)

You could also add or modify this XML to your Theme Modifier file and instead of this change being provided on a per definition basis, this change would be provided Theme-wide.

**Using Generalized CSS**

The easiest and most generic means of modifying the ChartCanvas Font is through CSS

 The following CSS targets all ChartCanvas elements, over-riding specified Font specifications.

```
.rdChartCanvas * {  
  font-family:  'Raleway', sans-serif !important;  
  font-size: 24px !important;  
  font-weight: bold !important;  
}
```

This CSS can be applied at the Theme.css level, within a custom CSS stylesheet or inline using an IncludeHTML element within your definition.
