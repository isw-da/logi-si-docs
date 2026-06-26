---
title: "Action Elements Example: Link to Another Report"
id: 4419722996247
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722996247-Action-Elements-Example-Link-to-Another-Report
updated_at: 2022-07-17T01:45:29Z
---

# Action Elements Example: Link to Another Report

# Action Elements Example: Link to Another Report

This example shows a simple link that launches another Logi report in the same application:

![](https://devnet.logianalytics.com/hc/article_attachments/4419699786263/introacts_01.png)

1. Add a **Label** element to your report and set its **Caption** attribute value as desired.
2. Beneath it, add an **Action.Report** element. Its default attribute settings are used for this example.
3. Beneath it, add a **Target.Report** element. Set its **Report Definition File** attribute to the definition file of the desired report.   
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4419706599319/criticalicon.png) In order to reload the current report definition, DO NOT set this attribute value to *CurrentReport* if you want Input element values or Link Parameters to be passed, or the data to be refreshed. Enter the actual report definition name instead.

The Label caption will appear on the page as an HTML link; when clicked, the second report will be displayed. Action.Report can be used as a child of a number of elements, including Button, Image, Charts, and more.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699786519/introacts_02.png)

At runtime, links generated using Action.Report, by default, use internal JavaScript to link to other definitions. However, these links may go unnoticed by search robots and may cause unwanted browser behavior. For example, as shown above top, the default Action.Report settings produce the context menu shown when *right-clicked* in the browser.
If you want users to be able to open the link target in a new browser tab or window, be sure to set the Action.Report element's **Crawler Friendly** attribute to *True*, as shown in the bottom example. This ensures that a standard HTML <a> tag set is generated for the link. Also use this value when you want search robots to find the link.
The appearance of the link can be controlled by the usual style classes associated with Anchors.
For a discussion of methods of passing data to the next report when the link is clicked, see [Pass Information](https://devnet.logianalytics.com/hc/en-us/articles/4419723105815-Pass-Information).
