---
title: "Export to Adobe PDF"
id: 4406817419799
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817419799-Export-to-Adobe-PDF
updated_at: 2022-04-06T06:06:00Z
---

# Export to Adobe PDF

# Export to Adobe PDF

The Adobe Portable Document Format (**PDF**) is a well-established file format standard and a widely-accepted method of distributing reports.

The following topics discuss how to export Logi reports to Adobe PDF:

* [Exporting a Report Manually](https://devnet.logianalytics.com/hc/en-us/articles/4406817424407-PDF-Exporting-a-Report-Manually#Manually)
* [Exporting a Report Automatically](https://devnet.logianalytics.com/hc/en-us/articles/4406822315927-PDF-Exporting-a-Report-Automatically#Automatically)
* [Adding Exported Headers and Footers](https://devnet.logianalytics.com/hc/en-us/articles/4406817416599-PDF-Adding-Exported-Headers-and-Footers#Footers)
* [Forcing Page Breaks in Exports](https://devnet.logianalytics.com/hc/en-us/articles/4406817425687-PDF-Forcing-Page-Breaks-in-Exports#ForcePgBrk)
* [Special Considerations for Java Apps](https://devnet.logianalytics.com/hc/en-us/articles/4406822317847-PDF-Special-Considerations-for-Java-Apps#JavaFonts)
* [Hiding Elements When Exporting](https://devnet.logianalytics.com/hc/en-us/articles/4406822316951-PDF-Hiding-Elements-when-Exporting#Hiding)
* [Exporting More Info Rows](https://devnet.logianalytics.com/hc/en-us/articles/4406817423255-PDF-Exporting-More-Info-Rows#MoreInfo)
* [Cascading Style Sheet Support](https://devnet.logianalytics.com/hc/en-us/articles/4406817417623-PDF-Cascading-Style-Sheet-Support#CSSSupport)
* [Debugging Exports](https://devnet.logianalytics.com/hc/en-us/articles/4406817418647-PDF-Debugging-Exports#Debugging)
* [Export Considerations](https://devnet.logianalytics.com/hc/en-us/articles/4406817421079-PDF-Export-Considerations#Considerations)
* [Export Errors](https://devnet.logianalytics.com/hc/en-us/articles/4406817422231-PDF-Export-Errors#Errors)

## About Exporting Reports to PDF

The PDF format is useful because of its ability to faithfully reproduce the appearance of a **document**, including graphics, images, and text, so that it can be easily viewed using the **Adobe Reader** program or browser plug-in. Notice the emphasis on "document" - PDF was *not* initially designed as a format for reproducing browser content and it doesn't always do so very well. Even though PDFs can be viewed within a browser, the two technologies are quite different.

For example, recent browser versions and Logi products support **doctype declarations**, which serve to tell the browser how to handle content layout, how to apply style, and more. Report pages can look quite different with different doctype selections. However, the PDF format *does not* support doctype declarations, and therefore can't represent everything exactly as the browser does. So, exported report pages may not look exactly like they do in the browser if a doctype has been applied.

What does this mean? It means developers and users should be realistic in their expectations about just how faithfully a Logi report can be reproduced when exported as a PDF document.

Chart Canvas charts are exported as SVG objects rather than
as images. This results in Chart Canvas charts exported to PDF having extremely
high resolution - they can be zoomed or printed with high-quality at any
resolution.

Logi Studio provides the **Action.Export PDF** element so that Logi reports can be exported to PDF files.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563309207/exportpdf_01.png)

Developers can give users the ability to export a report in two ways: **manually** (to a PDF viewed in their own browser) or **automatically** (to a PDF file) based on an event or schedule. Manual exports are configured within *report definitions* and automated exports are configured within *process definitions*.

The PDF export engine usesthe Gecko-based rendering technology developed by Mozilla and found in the Firefox browser, resulting in Chart Canvas charts beingexported as SVG objects rather than as images. This means that Chart Canvas charts exported to PDF have extremely high resolution - they can be zoomed or printed with high quality at any resolution.

### Exporting Links

By default, links in reports are *not* enabled when they're exported to PDF. However, "live links", which are those that do not use Action.Link, *can* be enabled in the PDF output. To enable them, set the **Target.PDF** element's **Show Links** attribute to *True*.

Live links are created by using a **Label** element, with its **Format** attribute set to *HTML*, and adding <a> tags around the text in
its **Caption**. Here's an example of a valid Caption attribute value for this purpose:

<a href="https://www.logianalytics.com">Visit the Logi Analytics web site</a>

A *complete* URL must be specified, as shown, not a *relative* URL.

### Specifying a Custom Temp File Location

![](https://devnet.logianalytics.com/hc/article_attachments/4417575435927/notev12.7base.png)In .NET Info applications, the PDF rendering engine used during exports writes temporary files to the C:\Windows\Temp folder by default. However, some anti-virus tools will flag multiple file-writing operations to this folder as potentially dangerous behavior and block them. Developers who encounter this situation can tell the
PDF rendering engine
to write temporary files elsewhere by adding a section to the Info application's web.config file:

<configSections>  
<section name="ABCpdf9.Section" type="WebSupergoo.ABCpdf9.ConfigSection, ABCpdf" allowLocation="true" allowDefinition="Everywhere" allowExeDefinition="MachineToLocalUser" overrideModeDefault="Allow"   
restartOnExternalChanges="true" requirePermission="true" />  
</configSections>  
  
<ABCpdf9.Section>  
<Preferences>  
 <clear />  
 <add Key="TempDirectory" Value="C:\my\_PDF\_Temp\_Folder" />  
</Preferences>  
</ABCpdf9.Section>

Add the code above that starts with <ABCpdf9.Section> just after the </configSections> section closing tag, as shown. Provide your own custom folder value for the TempDirectory key.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) Ensure that your custom temp folder already exists - the rendering engine will not create it.
