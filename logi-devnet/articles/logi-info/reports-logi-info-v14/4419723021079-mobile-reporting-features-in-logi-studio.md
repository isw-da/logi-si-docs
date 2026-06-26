---
title: "Mobile Reporting Features in Logi Studio"
id: 4419723021079
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723021079-Mobile-Reporting-Features-in-Logi-Studio
updated_at: 2022-07-17T01:44:31Z
---

# Mobile Reporting Features in Logi Studio

# Mobile Reporting Features in Logi Studio

Logi Studio includes a number of unique features for Mobile Report definitions, beginning with a special type of report definition:

![](https://devnet.logianalytics.com/hc/article_attachments/4419714829207/intromobile_04.png)

The Application panel includes a folder, **Mobile Reports**, as shown above. This folder can be right-clicked to create a new Mobile Report definition. When working with a Mobile Report definition, special elements will become available for use and certain other elements, which are not suitable for mobile reports, will be unavailable.

## Preview Masks

In order to allow developers to see their work in the proper context, Studio includes a special preview mode for mobile reports:

![](https://devnet.logianalytics.com/hc/article_attachments/4419714829463/intromobile_05.png)

As shown above, when the Preview button is pressed, a Mobile Report definition will be displayed in the Workspace panel within a mask that approximates the size of the target mobile device, using the appropriate browser for that device. The mask can be rotated to landscape orientation by clicking the white arrow on the mask frame.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699803927/intromobile_06.png)

Different device preview masks can be selected from a list (click the button next to the Preview URL); selecting a different mask immediately changes the displayed report preview. Standard masks are provided and developers can add custom masks as well.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699804183/intromobile_07.png)

These preview masks are only geographic simulators; they show you how your report will look in the available space. As shown above, they do not display any onscreen buttons or status bars that may normally appear above and below the space on the device screen. The real device OS is not being loaded, so Logi user input elements are not bound to OS controls; recalling the example in the previous section, this means no "Picker" control will appear if you click the Input Select List in the preview.

Full-fledged mobile device emulators are not included because they would present some operational problems, not the least of which would be the relatively long amount of time it would take to load and start them when the Preview button was clicked.
