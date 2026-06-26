---
title: "Using the Panel and Panel Content Elements"
id: 4419707745559
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707745559-Using-the-Panel-and-Panel-Content-Elements
updated_at: 2022-07-17T02:23:52Z
---

# Using the Panel and Panel Content Elements

# Using the Panel and Panel Content Elements

The Dashboard **Panel** element is simply a required container for the other child elements and multiple panel elements are generally used to create a Dashboard.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) If specifying a Gallery File in the Dashboard element attributes *do not* use Panel elements. See the Attributes table in [Using the Dashboard Element](https://devnet.logianalytics.com/hc/en-us/articles/4419707744535-Using-the-Dashboard-Element-) for more information.

![](https://devnet.logianalytics.com/hc/article_attachments/7522821699991/introdash_16.png)

The presence of Panel elements means simply that the panels are available, but they will not be displayed in the Dashboard unless configured through the Dashboard configuration page to be visible.
The Panel element has these attributes:

| Attribute | Description |
| --- | --- |
| Caption | (Required) Specifies the text displayed in the panel's title bar, and used as a title in the Dashboard configuration page. |
| ID | (Required) Specifies a unique identifier for this element. |
| Allow Caption Rename | Specifies if the user is allowed to change the Dashboard panel caption. When *True*, the "Rename" item appears in the panel Settings menu. When selected, the caption can be edited in place then saved by pressing Enter or clicking outside of the text box. The default value is *True*. |
| Image | Specifies the file name of a thumbnail image that will appear on the left side of the Add Panels panel. For the best appearance, images should be less than 200 pixels wide. The image name can come from an image in the \_SupportFiles folder or from a relative URL within the same Logi application. |
| Minimum Height | When the Dashboard has been configured for Free-form Layout, specifies the minimum height, in pixels, to which a panel can be resized. The default value, if left blank, is *100* pixels. |
| Minimum Width | When the Dashboard has been configured for Free-form Layout, specifies the minimum width, in pixels, to which a panel can be resized. The default value, if left blank, is *100* pixels. |
| Multiple Instances | Specifies whether multiple instances of a panel can be added to a Dashboard. When set to *True*, the Dashboard panel can be added multiple times to the same Dashboard or tab. This is especially useful for panels that have input parameters because the user can show different versions of the same panel with different parameters in the same Dashboard or tab. |
| Panel Description | Specifies the descriptive text for this panel that appears in the Add Panels panel. |
| Security Right ID | If entered, controls access to this element via Logi security. Supply the ID of a Right defined in the application's settings/security section. Only users that have a Role referenced in the Right will be able to see the element. (Be careful - when the Right is not defined in the settings, the element is visible.) Multiple Right IDs, separated by commas may be entered. In this case, the user will see the element if he has access to any one of the Rights. |
| Tooltip | Text that appears in a small balloon when the user hovers his mouse pointer over the panel's Title Bar. |

The **Panel Content** element is the first child element of a Dashboard panel. This element is a container for the actual content to be displayed. Its only attribute, **Height**, is optional and used to set a fixed panel height. When left blank, the height is resized automatically to fit the contents. If a fixed height is set, a vertical scroll-bar appears when necessary if the content's height is greater than the fixed height specified.

![](https://devnet.logianalytics.com/hc/article_attachments/7522821714199/introdash_17.png)

As shown above, left, content can be **included as a sub-report**, or be included directly in the Panel Content element or, as shown above, right.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) Inclusion of content **as a sub-report**, especially if there are many panels, is a *very desirable approach*: it keeps the main definition containing the Dashboard from becoming overly long and complex and allows panel content to be developed and tested independently before being integrated into the Dashboard. In addition, if you plan to *export* panel content, we highly recommend
that you
use sub-reports.

Dashboard panels are processed in separate threads at the web server, resulting in improved performance, especially for Dashboards with large numbers of panels.
Each Panel Content element is an individual reporting environment and, as such, can have its own Default Request Parameters element, Local Data element, etc. If necessary, panels can be identified with the token @Function.InstanceID~.
The **Load Panels Plugin Call** element allows developers to use a plug-in to access the underlying definition code for a Dashboard panel.
