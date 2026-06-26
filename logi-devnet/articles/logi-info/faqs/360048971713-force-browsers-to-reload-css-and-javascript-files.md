---
title: "Force browsers to reload CSS and Javascript files"
id: 360048971713
section: "FAQs"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/360048971713-Force-browsers-to-reload-CSS-and-Javascript-files
updated_at: 2023-07-18T19:31:42Z
---

# Force browsers to reload CSS and Javascript files

### Foreword:

Web servers and browsers attempt to efficiently load resources such as CSS and Javascript filles.  This is one of the main concepts behind using centrally hosted resources or CDN (Content Delivery Network) hosted files.  Instead of caching a file for a single website, browsers can cache a CDN referenced file for any number of websites.

There are cases when it is necessary that a user load the most recent version of a CSS or Javascript file.  If the file name remains the same, there is a good chance that the server or browser will serve the user a cached version of the file.

### Question:

Is there a way to force browsers to reload CSS and Javascript files for a Logi Info Application?

### Answer:

The most widely used solution to force servers and browsers to not cache files is to provide a unique parameter along with the request for the file.

For example, instead of requesting "Style.css", the request would become "Style.css?rnd=12345"

Typically within a Report Definition, Logi Info Studio developers use the "Style" and "IncludeScript" elements as a means to include CSS or Javascript files.  Unfortunately, these elements do not allow additional parameters to be passed into a request, and they are stripped out before being processed.

A work-around solution is to use an IncludeHTMLFile element instead.  The IncludeHTMLFile element allows a developer to utilize any valid HTML, including the <link> and <script> tags.  This provides the ability to append a version number, random GUID or SessionID to the end of the request, and apply that information to the HEAD of generated HTML.

For example, to only cache a stylesheet for a user's session:

```
<link rel="stylesheet" href="./_SupportFiles/Style.css?rnd=@Function.SessionID~">
```

To never cache a stylesheet for any user:

```
<link rel="stylesheet" href="./_SupportFiles/Style.css?rnd=@Function.GUID~">
```

A developer could even control the file caching based on a product release number stored as a constant.

```
<link rel="stylesheet" href="./_SupportFiles/Style.css?rnd=@Constant.VersionID~">
```

An example to control the caching of a script file based on a user's session:

```
<script language="JAVASCRIPT" src="./_SupportFiles/myscripts.js?rnd=@Function.SessionID~"></script>
```

 Initial Run:

![mceclip0.png](https://devnet.logianalytics.com/hc/article_attachments/360071122494/mceclip0.png)

Subsequent Session Reload:

![mceclip1.png](https://devnet.logianalytics.com/hc/article_attachments/360072284573/mceclip1.png)
