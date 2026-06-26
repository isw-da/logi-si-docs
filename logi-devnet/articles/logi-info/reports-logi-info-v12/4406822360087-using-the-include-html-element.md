---
title: "Using the Include HTML Element"
id: 4406822360087
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822360087-Using-the-Include-HTML-Element
updated_at: 2022-04-06T06:06:34Z
---

# Using the Include HTML Element

# Using the Include HTML Element

The **Include HTML** element allows you to insert HTML at selected points within your report definition.

This element can be placed in your definition as the child of a number of elements, such as Report Header, Body, Division, Data Table Column, Report Footer, and others. See the [Element Reference](https://clm.logianalytics.com/rdPage.aspx?rdReport=ElementRefDetail&itemID=2223&iName=IncludeHtml&iType=Element&iLabel=Include+HTML&lnkpg=0) entry for this element for a complete list.

In the past, developers have used a **Label** element, set to **HTML** format, for this purpose. However, feedback from developers indicated that this was a somewhat obscure usage, so the Include HTML element is now recommended for this purpose instead.

![](https://devnet.logianalytics.com/hc/article_attachments/5263097959703/inclhtml_01.png)  

A simple example is shown above and the resulting HTML output looks like this:

<!DOCTYPE HTML>  
<HTML xmlns:msxsl="urn:schemas-microsoft-com:xslt" xmlns:rdXslExtension="urn:rdXslExtension">  
<HEAD>  
(... various standard tags not shown for clarity )  
</HEAD>  
<BODY onload="rdBodyLoad()">  
(... various standard tags not shown for clarity )  
<div id="rdMainBody">  
<SPAN><p>Here's my HTML</p></SPAN>  
</div>  
(... various standard tags not shown for clarity )  
</BODY>  
</HTML>

As you can, the HTML from the Include HTML element has been inserted between two <SPAN> tags in the code.

Scripts can be entered here in the same way, using <SCRIPT> tags. If you double-click the **HTML** attribute name and open the Attribute Zoom window, it's easy to enter multi-line scripts, like the following example:

<script type="text/javascript">  
NagMsgTimer = function() {  
setTimeout('ShowNagMsg()', 2\*60\*1000); /\* delay 2 mins, in milliseconds, \*/  
 }  
function ShowNagMsg() {  
alert('Register your product now!');  
setTimeout('ShowNagMsg()', 2\*60\*1000); /\* delay 2 mins, in milliseconds, \*/  
 }  
/\* cause function NagMsgTimer to run when page is loaded \*/   
 if (window.attachEvent) { /\* IE \*/  
window.attachEvent('onload', NagMsgTimer); /\* event name is case sensitive \*/  
 }  
 else { /\* Moz, Netscape, Firefox \*/  
window.addEventListener('load', NagMsgTimer, false);  
 }  
 </script>

This script will be included in the HTML and, because it attaches itself to the page load event, will begin to execute automatically when the page is loaded. To get the script inserted in the <HEAD> section, see the next part of this topic and use the **Include HTML File** element instead.
