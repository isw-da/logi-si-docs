---
title: "Popup Panel Attributes"
id: 4419723110295
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723110295-Popup-Panel-Attributes
updated_at: 2022-07-17T02:06:44Z
---

# Popup Panel Attributes

# Popup Panel Attributes

The Popup Panel element has the following attributes:

| Attribute | Description |
| --- | --- |
| ID | (Required) Specifies a unique element identifier. |
| Caption | Specifies the text that will appear in the panel's Title Bar. You must provide a value here in order to display the Close button. |
| Class | Specifies the CSS class to be used by the element. When set, this class will also be used by all child elements that don't have their own class. |
| Close Button Caption | Specifies the "Close Button" text, which by default is an "X". This attribute allows you to specify different text instead, such as "Done". You must enter a value in the Caption attribute in order to display the Close button. |
| Close Button Class | Specifies an alternate class for the Close Button. |
| Height | Specifies the height of panel. If left blank, panel will automatically size to its contents. |
| Height Scale | Specifies the measurement units for the previous attribute: *Percent* or *Pixels*. |
| Hide Close Button | Specifies whether or not the Close Button will be displayed.  Default: *False* |
| Keep Other Popups | Specifies behavior when one popup is already being shown and then a second popup is shown. The default behavior is to close the first popup. When this attribute is set to *True*, the first popup will remain open and subsequent popups will be layered in above it. |
| Popup Modal | Specifies if the panel will be shown in a Modal state, disabling the rest of the report page and shading it with a transparent gray overlay.  Default: *False* |
| Popup Movable | Specifies whether the panel to be dragged and repositioned, using the mouse.   Default: *False*. |
| Popup Panel Location | Specifies the location at which the panel will be shown. Choices include: *Mouse* - panel will appear below and to the right of the cursor position.  *Center* - panel will appear at the center of page. *200,150* - panel will appear at these X,Y coordinates, relative to the upper left corner of the screen.   Default: *Mouse* |
| Security Right ID | When using Logi Security, specifies one or more Security Right IDs, separated by commas. Users with these Security Right IDs will be able to view the Analysis Grid, users without them will not. |
| Show On Page Load | Specifies whether the panel will be automatically displayed when the report page is first loaded. Default: *False* |
| Width | Specifies the width of the panel. If left blank, panel will automatically size to its contents. |
| Width Scale | Specifies the measurement units applied to previous attribute: *Percent* or *Pixels*. |
