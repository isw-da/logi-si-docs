---
title: "Analysis Grid Developers - Configuring for Report Author Galleries"
id: 4419707276183
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707276183-Analysis-Grid-Developers-Configuring-for-Report-Author-Galleries
updated_at: 2022-07-17T02:09:26Z
---

# Analysis Grid Developers - Configuring for Report Author Galleries

# Analysis Grid Developers - Configuring for Report Author Galleries

The [Report Author](https://devnet.logianalytics.com/hc/en-us/articles/4419715450135-Report-Author) element, available in the Self-Service Reporting Module (SSRM) add-on, v12+, provides users with the ability to construct reports using a drag-n-drop interface. Visualizations for use with the Report Author are created using the Analysis Grid's "Add to Dashboard" feature.

To do this, the Custom Dashboard Panels element is used with an Analysis Grid, just as described in [Analysis Grid Developers - Configuring Add-to-Dashboard](https://devnet.logianalytics.com/hc/en-us/articles/4419715051671-Analysis-Grid-Developers-Configuring-Add-to-Dashboard). However, for this purpose, its **Dashboard Save File** attribute value does *not* point to an existing Dashboard Save file. Instead, it identifies a separate Save file that will be used later by the Report Author as its "Gallery" file.

If Logi Security has been and will be used, the current user's name will be available in the @Function.UserName~ token. This can be embedded into this attribute to provide separate Gallery files for individual users. For example, the attribute value might be:

@Function.AppPhysicalPath~\GalleryFiles\@Function.UserName~.xml

which might translate to:

C:\inetpub\wwwroot\MyReportApp\GalleryFiles\BGates.xml

This file can be created, renamed, and copied as necessary to make it available to report definitions using the Report Author element.
