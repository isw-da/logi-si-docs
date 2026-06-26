---
title: "Styling the Home Page"
id: 5281612994711
section: "Extensibility"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281612994711-Styling-the-Home-Page
updated_at: 2022-05-03T22:09:01Z
---

# Styling the Home Page

# Styling the Home Page

Visually modifying and branding the user interface is a simple but effective step toward integrating Exago into a host application. For styling purposes Exago can be thought of as a control that sits within a div on an .aspx (html) page.

Aesthetic changes can be made for single users or groups of users by directing each user/group to different custom .aspx pages. However, we suggest using **[Application Themes](https://devnet.logianalytics.com/hc/en-us/articles/5281620572951-Application-Themes-Overview)** instead to encapsulate groups of changes, which can be selected dynamically in the API.

To visually integrate Exago, make a copy of the *ExagoHome.aspx* file and modify the elements surrounding the Exago control or override the CSS of the user interface itself.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> Do not make changes directly to *ExagoHome.aspx* as they will be overwritten during upgrades. Instead use the example below to create a custom .aspx page.

## Exago Control

The example below is the minimum code necessary to embed the Exago control.

```
<%@ Page Language="C#" EnableViewState="false" EnableEventValidation="false" %><%@ Register src="WebReportsCtrl.ascx" tagname="WebReportsCtrl" tagprefix="wr" %><!DOCTYPE html><html>  <head runat="server">    <title>Exago</title>  </head>  <body>    <form runat="server">      <wr:WebReportsCtrl ID="WebReportsCtrl" runat="server" />    </form>  </body></html>
```

### Exago Control Properties

Several properties can be set on the Exago Control to modify various settings and behaviors of Exago. The following properties can be set.

* **ConfigFile** — Loads a configuration file other than that created by the Admin Console (for example `ConfigFile="NorthwindConfig.xml"`).
  > ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
  >
  > If entering Exago through the API this parameter is ignored.
* **LanguageFile** — Specify which language files to use in place of the ‘Language File’ parameter of **Main Settings** in the configuration file. (for example `LanguageFile="es-mx, getting-started-custom"`).
* **ForceIECompatMode** — Setting to *True* will force certain JavaScript functions to working in ‘compatibility’ mode. This may be necessary if dragging a Data Field into a cell of the Report Designer does not work properly. (for example `ForceIECompatMode="true"`).
* **XUaCompat** — Controls whether to remove the meta u-ax-compatible tag when running reports to PDF in IE8. The default is *false* which removes the tag. If you are experiencing issues downloading PDF reports in IE8 setting this flag to True may resolve the issue. (for example `XUaCompat="true"`).
  > ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Critical")
  >
  > IE8 is no longer supported by Exago, as of *v2016.1*.

## Changing CSS and Images

All of the CSS and images used by Exago can be modified within the aspx page if desired. However we recommend using an **[Application Theme](https://devnet.logianalytics.com/hc/en-us/articles/5281620572951-Application-Themes-Overview)** instead.

Any icon in Exago can be changed on a per-company or per-user basis:

1. Create the custom images you would like to display.
2. Identify the Id of the image you want to change. See [Finding Image Ids](#Finding).
3. Create a language file that maps the Ids to the location of the custom images. See [Multi-Language Support](https://devnet.logianalytics.com/hc/en-us/articles/5281604247447-Multi-Language-Support).  

   ### Example

   ```
   <element id="ExportTypeMenuHtml" image= "ConfigImagesCustomHTMLExecutIconLarge.png"></element>
   ```

### Hovering Images

For icons that have hover effects there is a special naming convention.

To change custom icons with hover effects:

1. Follow the steps above to create the non-hover icon.
2. Create the custom icon with the hover effect. Save it to have the same name as the non-hover icon and append “\_h” to its name.

### Finding Image Ids

To find the Ids of icons in Exago:

1. Open Exago in a browser.
2. Use the browser’s developer tools to inspect the icon you want to change. For most browsers this can be done by pressing F12.
3. Look at the id property of the icon. There will be several words separated by underscores. Use the last element as the image Id (see example below).

![](https://devnet.logianalytics.com/hc/article_attachments/5432248879767/element.png)
