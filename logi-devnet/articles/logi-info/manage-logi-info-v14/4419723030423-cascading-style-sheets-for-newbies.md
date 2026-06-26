---
title: "Cascading Style Sheets for Newbies"
id: 4419723030423
section: "Manage - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723030423-Cascading-Style-Sheets-for-Newbies
updated_at: 2022-07-17T01:43:56Z
---

# Cascading Style Sheets for Newbies

# Cascading Style Sheets for Newbies

If you're a developer with web design experience, you should already be familiar with style sheets and you can skip this topic.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599319/criticalicon.png)Logi Info includes a feature called **Themes** which can instantly apply pre-built styling to your application. A number of stock themes are included with Logi Info and you can also create your own. For more information about themes, see [Themes](https://devnet.logianalytics.com/hc/en-us/articles/4419723357847-Themes).

Cascading Style Sheets (CSS) is a technology that allows the presentation aspects of web pages to be separated from the page content. It can be used to add "styling" (e.g. apply fonts, colors, alignment, spacing, and more) to web pages. It's a mature standard, fully supported by the W3C. All modern browsers (Chrome, IE, Edge, Firefox, Safari) support CSS3 and earlier standards.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599319/criticalicon.png) IE has lagged behind Firefox and Chrome in supporting new CSS standards. Not only does this introduce compatibility issues you may have to deal with but, because Logi Studio uses the Windows operating system's IE components, Studio's Preview function may be affected. Issues of this nature tend to arise especially if you integrate third party libraries that make heavy use of HTML5 and CSS3 into
your
Logi
application.

As used with Logi applications, style sheets are independent text files that define style *classes*; with property settings. For example, the definition for the class "font9ptBold", shown below, contains *selectors* that cause text to appear in an 8-point, bold font:

.font9ptBold {  
 font-size: 8pt;  
 font-weight: bold;  
}

Classes are assigned to elements within a Logi application in order to control their appearance. For example, we might assign the font9ptBold class to a Label element so that its caption will appear on the web page in an 8-point, bold font. CSS includes a wide variety of selectors that can affect everything from font weight, size, and color to the positioning of images on the page.

Use of style sheets creates slightly more complexity for the developer than having appearance properties directly associated (as attributes) with elements in Logi Studio. The trade-off, however, is that they offer far more flexibility and browser-version compatibility.

Logi Info is CSS standards-compliant and, to help you work with style classes, Logi Studio includes a style sheet editor.
Logi Info allows you to set a "doctype declaration" for your application, which gives the browser some guidance about how to render the page. This is discussed in [Doctype Declarations](https://devnet.logianalytics.com/hc/en-us/articles/4419723241623-Doctype-Declarations) and can help sort out some the behavioral differences between browsers.

The "cascading" part of the technology's name refers to the way in which the effects of classes permeate *downward* through hierarchical structures of elements in web pages. The effects start at the top and, unless superceded by other classes, continues downward within the container, structure, or child elements.

You can develop your own "standard" style sheet file with a .css file extension, and then *re-use it* or parts of it with different Logi applications. This saves development time and promotes a consistent look for your applications, if desired. You may care to develop and share a "company style sheet" so that all of your Logi application developers produce pages with the same appearance.

Style classes can be applied in a number of ways, including "inline" or embedded directly into HTML. However, it's beyond the scope of this topic to provide a complete explanation of Cascading Style Sheets; [excellent resources](http://www.w3schools.com/css/css_intro.asp) can be found online.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599319/criticalicon.png) Logi products include a feature called **Themes** which can instantly apply style and other presentation touches to your report. A number of stock themes are included with the products and you can also create your own. For more information about themes, see [Themes](https://devnet.logianalytics.com/hc/en-us/articles/4419723357847-Themes).

## Create an Example Style Sheet

Select and copy the following text, paste it into Notepad or a similar text editor, and save it to your desktop (or any other location you prefer) as CSSExample.css:

/\* CSSExample.css: our example style sheet \*/  
.myTable {  
 padding: 5px;  
border-width: 2px;   
border-style: solid;   
border-color: Silver;  
border-collapse: collapse;  
background-color: White;  
font-family: Verdana, Arial; /\* if Verdana font not found, will use Arial \*/  
font-size: 9pt;  
font-weight: normal;  
color: Black; /\* this is the font color \*/  
}  
  
.myTable TH {/\* TH: automatically applied to table header \*/  
padding: 5px;  
border-style: solid;  
border-color: Silver;  
background-color: #F0F0F0; /\* colors can also be specified using hex \*/  
font-size: 10pt;  
color: Maroon;  
}  
  
.myTable TD {/\* TD: automatically applied to table cells \*/  
border: 2px solid Silver; /\* combines three border selectors into one \*/  
padding-left: 5px;  
padding-right: 5px;  
text-align: center;  
}  
  
.fontBold {  
 font-weight: bold;  
}  
  
If you're wondering what those "TH" and "TD" designations are, they relate to the tags that make up an HTML table: TH = Table Header, and TD = Table Data. By including them as shown above, their classes will be automatically applied to any Data Table that uses the myTable class. This is a bit of CSS shorthand that saves you time and effort.
The next two sections discuss how to include this style sheet in your application, and how to edit it within Studio.

If you're wondering what those "TH" and "TD" designations are, they relate to the tags that make up an HTML table: TH = Table Header, and TD = Table Data. By including them as shown above, their classes will be automatically applied to any Data Table that uses the myTable class. This is a bit of CSS shorthand that saves you time and effort.
