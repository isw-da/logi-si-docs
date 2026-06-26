---
title: "Action Elements Example: Link that Executes JavaScript"
id: 4419715353495
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715353495-Action-Elements-Example-Link-that-Executes-JavaScript
updated_at: 2022-07-17T02:24:10Z
---

# Action Elements Example: Link that Executes JavaScript

# Action Elements Example: Link that Executes JavaScript

This example shows a simple link that executes some JavaScript:

![](https://devnet.logianalytics.com/hc/article_attachments/7522839978135/introacts_04.png)

1. Add a **Label** element to your report and set its **Caption** attribute value as desired.
2. Beneath it, add an **Action.Javascript** element. Set its **JavaScript** attribute to the code you wish to run. You may enter multi-line JavaScript code, set off by curly brackets if necessary, and all the traditional functions are supported.  
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) Double-click the JavaScript attribute name to open the Attribute Zoom window for easier code editing. For more information, see [Using Logi Studio](https://devnet.logianalytics.com/hc/en-us/articles/4419707934103-Using-Logi-Studio).

The Label caption will appear on the page as an HTML link; when clicked, the embedded JavaScript will be executed on the browser. Action.Link and Action.JavaScript may be used as the child of a number of elements, including Label, Button, Image, Charts, and more.
The **Action.JavaScript** element provides the easiest way to enter JavaScript code. However, the same result can be achieved by using Action.Link and Target.Link elements. Enter the JavaScript code, prefaced with "javascript" followed by a colon, in the Target.Link element's **URL** attribute.
