---
title: "Action Elements Example: Email Report as Attachment"
id: 4406817580055
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817580055-Action-Elements-Example-Email-Report-as-Attachment
updated_at: 2022-04-06T06:06:57Z
---

# Action Elements Example: Email Report as Attachment

# Action Elements Example: Email Report as Attachment

This example shows a link that uses **Action.Email Report** to send the current report as a PDF attachment.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563218711/introacts_06.png)

1. Add a **Label** element to your report and set its **Caption** attribute value as desired.
2. Beneath it, add an **Action.Email Report**  element. Set its **ID** and **Connection ID** attributes appropriately.
3. Beneath it, add **Action.PDF** and **Target.PDF** elements. By leaving Target.PDF's **Report Definition File** attribute blank, the default (the current report) will be attached. Other export formats are also supported.

When the report is run and the link is clicked, a modal pop-up panel will be displayed:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575645975/introacts_07.png)

Users can then enter email information. Multiple addresses can be entered in the "To" field by separating them with commas or semi-colons. If you provide values for other attributes, such as From Email Address, those values will appear in the pop-up panel as default values for the user input controls. When **Send Now** is clicked, the email(s) will sent out, with the exported report attached as a PDF.
If it's supported by your browser, the Action.Email Report element will use an **HTML5** feature called "local storage" to automatically store the email addresses you enter, preserve them between sessions, and provide them back to you in a list for selection in subsequent sessions. If your browser doesn't support this feature, or if it's turned off in your browser options, obviously the element won't be able to provide the list of addresses for re-use.
