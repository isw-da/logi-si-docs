---
title: "Scripting with Action.Pre-Action JavaScript"
id: 4419723298199
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723298199-Scripting-with-Action-Pre-Action-JavaScript
updated_at: 2022-07-17T02:22:55Z
---

# Scripting with Action.Pre-Action JavaScript

# Scripting with Action.Pre-Action JavaScript

The **Action.Pre-Action Javascript** element allows you to run code after a link, button, etc. has been clicked but before its Action element executes. This makes it much easier to do specialized input validation or to perform custom UI changes before the page is submitted.

![](https://devnet.logianalytics.com/hc/article_attachments/7522718430871/scripting_01a.png)

As shown above, Action.Pre-Action Javascript is available as a child element of most other Action elements. If the JavaScript it runs returns any value other than *false*, then the parent Action element will execute. If it returns *false*, the parent Action element will *not* execute. You may use multiple Action.Pre-Action Javascript elements beneath a parent Action element.

The JavaScript code can be inline, as shown above, or it can be a function in a separate script file, or a function included using an **Include Script** element. Here's a simple example of the latter:

function TestColor(inpColor) {  
if ( inpColor == 'red') {   
return true;   
}  
else {  
alert('You must enter red');  
return false;   
 }  
}

The code shown above is placed in an Include Script element in the report definition.

![](https://devnet.logianalytics.com/hc/article_attachments/7522746204695/scripting_01b.png)

The Action.Pre-Action Javascript element code, shown above, is:

return TestColor(document.getElementById('inpColor').value);

If the text "red" is entered in an Input Text element on the page with an ID of "inpColor" (not shown) and the "Save data" link is clicked then the next report *will* be shown. If any other text is entered and the link is clicked, a warning message will appear and navigation to the next report *will not* occur.
