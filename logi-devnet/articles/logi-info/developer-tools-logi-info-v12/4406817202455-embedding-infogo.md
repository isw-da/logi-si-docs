---
title: "Embedding InfoGo"
id: 4406817202455
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817202455-Embedding-InfoGo
updated_at: 2022-04-06T06:04:36Z
---

# Embedding InfoGo

# Embedding InfoGo

The InfoGo application can be embedded into other Logi applications or into non-Logi HTML pages.

## Using InfoGo as the Base Application

One of the simplest ways to embed InfoGo is to use it as the base application, then add your own definitions and supporting files to it. This lets you "build out" the application with your own code and refer to InfoGo definitions directly.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563445655/cfginfogo125_21.png)

In the example above, Studio's **Application Panel** shows an additional folder ("CRM") and definitions that have been added to InfoGo in order to use this approach. It has the advantage of a single code base, does not use an iFrame, and the security scheme in InfoGo can be used by the rest of the application.

## Embedding in an iFrame without SecureKey

The following example shows one way to embed InfoGo into another Logi application using an iFrame, but without using Logi Secure Key.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575823511/cfginfogo125_22.png)

As shown above, an **Include HTML** element is added to the report definition. Width control is exercised by placing it inside a container, like an HTML table Column Cell or a Division, whose width can be set. Here's the HTML code to include:

<script language="javascript" type="text/javascript">  
function resizeIframe(obj) {  
 obj.style.height = obj.contentWindow.document.body.scrollHeight + 'px';  
 }  
 </script>  
  
<iframe src='http://yourServer/InfoGo' style="width: 100%; min-height: 1200px;   
 frameborder: false;" frameborder='0' onload='javascript:resizeIframe(this);' "  
 scrolling="no">  
</iframe>

The same code can be used to embed InfoGo into a non-Logi application.

## Embedding in an iFrame with SecureKey

If you want to embed InfoGo using an iFrame and make use of Logi SecureKey authentication, you first have to get the SecureKey value from the InfoGo application.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563446167/cfginfogo125_23.png)

One way to do this is shown above. Under a Local Data element, **DataLayer.CSV** is used to retrieve the key value. This datalayer type is used because it can use a URL to retrieve the data. Its **CSV File** attribute value will be similar to:

http://yourServer/InfoGo/rdTemplate/rdGetSecureKey.aspx?UserName=@Function.UserName~&UserID=@Function.UserID~&Roles=@Function.UserRoles~

That retrieves one row into Local Data, with a column named SKey, containing the SecureKey value. Then, using the same embedded script from the previous example:

<script language="javascript" type="text/javascript">  
function resizeIframe(obj) {  
 obj.style.height = obj.contentWindow.document.body.scrollHeight + 'px';  
 }  
 </script>  
  
<iframe src='http://yourServer/InfoGo/**?rdSecureKey=@Local.SKey~**' style="width: 100%;  
 min-height: 1200px; frameborder: false;" frameborder='0'   
 onload='javascript:resizeIframe(this);' "scrolling="no">  
</iframe>

Add the rdSecureKey parameter and Local Data token, shown in blue above, to the iFrame source URL to complete the authentication process when embedding the InfoGo application.
