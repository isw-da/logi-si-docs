---
title: "Configuring Add-to-Dashboard or -Gallery"
id: 4406817372439
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817372439-Configuring-Add-to-Dashboard-or-Gallery
updated_at: 2022-04-06T06:05:42Z
---

# Configuring Add-to-Dashboard or -Gallery

# Configuring Add-to-Dashboard or -Gallery

The Thinkspace allows users
to generate a visualization, then add it as a new panel in an
existing dashboard or as a resource in a visualization gallery in another report. The [Logi Info Dashboard](https://devnet.logianalytics.com/hc/en-us/articles/4406817724567-Logi-Info-Dashboard-) and [Report Author](https://devnet.logianalytics.com/hc/en-us/articles/4406822491031-Report-Author) elements can make use of visualization galleries.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583974295/devdm31_13.png)

When properly configured, the Thinkspace visualization area will display a button like the one shown above. Its tooltip caption can be configured; by default it's "Add to Gallery".

![](https://devnet.logianalytics.com/hc/article_attachments/4417583974551/devdm31_14_780x421.png)

When configured for use with a Dashboard "Save File" and the button is clicked, the visualization is added immediately as a *new panel*
in the Dashboard, as shown above.

The Thinkspace writes the underlying XML for its visualization into the Dashboard's
configuration file. In the Dashboard, the chart is
inserted at the top of Column 1; if Dashboard tabs are being used, the
insertion occurs in the currently active tab.

Or, if so configured, the Thinkspace can write the underlying XML for its visualization into a Dashboard or Report Author's "Gallery File". The visualization is then available for use but no immediate insertion occurs.

Just before the visualization is saved, the user will be prompted for the **Panel Title** (with the chart title from the Thinkspace provided as a suggestion) and an optional description for display.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563330711/devdm31_15.png)

The new visualization thereafter appears in the Dashboard Configuration
Page or Visual Gallery, as shown above, just like any other resource, complete with a
thumbnail image. The visualization can be removed from the visible dashboard
panels and from the configuration page or gallery entirely, using the usual
controls.

The user can insert multiple visualizations into a Dashboard or Gallery using this technique.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575733399/devdm31_16.png)

In the report definition, the developer makes this functionality available by adding a **Custom Dashboard Panels** element, shown above, beneath a Thinkspace element. For use with a dashboard Save File, its **Dashboard Save File** attribute value should be set to match the target dashboard's **Save File** attribute value, as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563330967/devdm31_17.png)

For use with a Dashboard or Report Author's visualization gallery, the attributes should be configured as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) The Save File and Gallery File attribute example values shown above have been shortened for visual clarity. However, a *fully-qualified path and file name*, with .xml
extension, is required, so a realistic attribute value would be something like:

@Function.AppPhysicalPath~\DashFiles\DashbdSave.xml  
@Function.AppPhysicalPath~\Galleries\@Function.UserName~\_UserGallery.xml

Ensure that the account that runs the Logi application has **Write**
permissions to the "DashFiles" or "Galleries" folder. For experimentation purposes, you can use the rdDownload folder, for which appropriate permissions already exist (but its contents are periodically deleted, so don't use it for anything but experimentation).

If Logi Security is being used, Dashboard Save Files and Gallery Files can be personalized using the @Function.UserName~token.

The Custom Dashboard Panel element also has an attribute, **Add Caption**, which sets the caption for the button used to save the visualization. If left blank, the default caption is "Add to Gallery".

For more information about Dashboards, see [Logi Info Dashboard](https://devnet.logianalytics.com/hc/en-us/articles/4406817724567-Logi-Info-Dashboard-).
