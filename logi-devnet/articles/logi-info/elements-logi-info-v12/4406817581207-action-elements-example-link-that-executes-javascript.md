---
title: "Action Elements Example: Link that Executes JavaScript"
id: 4406817581207
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817581207-Action-Elements-Example-Link-that-Executes-JavaScript
updated_at: 2022-04-06T06:06:59Z
---

# Action Elements Example: Link that Executes JavaScript

# Action Elements Example: Link that Executes JavaScript

This example shows a simple link that executes some JavaScript:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563218327/introacts_04.png)

1. Add a **Label** element to your report and set its **Caption** attribute value as desired.
2. Beneath it, add an **Action.Javascript** element. Set its **Javascript** attribute to the code you wish to run. You may enter multi-line Javascript code, set off by curly brackets if necessary, and all the traditional functions are supported.  
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) Double-click the Javascript attribute name to open the Attribute Zoom window for easier code editing. For more information, see [Using Logi 12 Studio](https://devnet.logianalytics.com/hc/en-us/articles/4406822594327-Using-Logi-12-Studio).

The Label caption will appear on the page as an HTML link; when clicked, the embedded JavaScript will be executed on the browser. Action.Link and Action.JavaScript may be used as the child of a number of elements, including Label, Button, Image, Charts, and more.
The **Action.JavaScript** element provides the easiest way to enter JavaScript code. However, the same result can be achieved by using Action.Link and Target.Link elements. Enter the JavaScript code, prefaced with "javascript" followed by a colon, in the Target.Link element's **URL** attribute.
