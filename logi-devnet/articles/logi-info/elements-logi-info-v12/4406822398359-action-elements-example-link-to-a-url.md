---
title: "Action Elements Example: Link to a URL"
id: 4406822398359
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822398359-Action-Elements-Example-Link-to-a-URL
updated_at: 2022-04-06T06:06:59Z
---

# Action Elements Example: Link to a URL

# Action Elements Example: Link to a URL

This example shows a simple link that opens another web page, in a new browser window:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563217687/introacts_03.png)

1. Add a **Label** element to your report and set its **Caption** attribute value as desired.
2. Beneath it, add an **Action.Link** element. Its default attribute settings are used for this example.
3. Beneath it, add a **Target.Link** element. Set its **URL** attribute to the URL of the target web site or page (include the "http://" prefix).  
     
   Other Target.Link attributes control aspects of the target, such as whether it's modal or will include scrollbars. The **Frame ID** attribute determines if the web page will open in the same browser window or tab (the default) or in other windows or tabs. If the latter, some of the behavior (window vs. tab) may be governed by your browser settings.

The Label caption will appear on the page as an HTML link; when clicked, the second web page or file will be displayed. Action.Link can be used as a child of a number of elements, including Button, Image, Charts, and more.

## Opening a File

If the URL ends in a file name and extension, such as http://devnet.logianalytics.com/downloads/StudioKeybdShortcuts.pdf, the browser will attempt to download and open the file for display. In some cases, you may be prompted to either Save or Open the file. If the file type is unusual (for example, it does not have not a common extension like .pdf, .docx, .txt, etc.) you may need to add the file type to your Logi
application's supported MIME Types in your web server. For IIS, this is accomplished using the IIS Manager application and is [described here](https://docs.microsoft.com/en-us/iis/configuration/system.webserver/staticcontent/mimemap#how-to). MIME types tell the browser how to handle the file when it downloads it.
