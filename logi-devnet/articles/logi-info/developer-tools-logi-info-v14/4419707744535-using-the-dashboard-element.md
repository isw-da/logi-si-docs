---
title: "Using the Dashboard Element "
id: 4419707744535
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707744535-Using-the-Dashboard-Element
updated_at: 2022-07-17T02:23:52Z
---

# Using the Dashboard Element 

# Using the Dashboard Element

Only one Dashboard element is allowed per
report definition. Four child elements, discussed in other topics, are used with the Dashboard element. *We do not recommend that you use this element within an embedded sub-report*.

![](https://devnet.logianalytics.com/hc/article_attachments/7522807525911/introdash_15.png)![](https://devnet.logianalytics.com/hc/article_attachments/7522807534103/image-20220516-130924_1116x427.png)

Let's examine the Dashboard element's attributes:

| Attribute | Description |
| --- | --- |
| Allow Free-form Layout | Specifies whether Free-form Layout mode is enabled. This layout mode allows Dashboard panels to be placed wherever desired by the user, instead of fitting into a columnar arrangement. When disabled, users must arrange panels in pre-defined columns. When this attribute is *True*, the Dashboard Columns attribute must be *0*. Default: *False.* |
| Auto Global Filters | Specifies whether Dashboard panels with Analysis Filters, and/or those generated from an Analysis Grid that uses the Active Query Builder element, will have global filters created automatically. Default: *False.* |
| Auto Panel Filters | Specifies whether Dashboard panels generated from an Analysis Grid that uses the Active Query Builder element will have panel filters created automatically, based on its metadata. Default: *False.* |
| Dashboard Adjustable | Determines if the user is allowed to add, remove and manage tabs and panels. Set this attribute to *False* for a static Dashboard that users cannot change. When set to **True,** the user's Dashboard changes are saved to the location specified in the Save File attribute.  When set to *False*, the user cannot save changes, but the Save File is still used to control the Dashboard appearance. Therefore, set this to *True* during the development process so that you, the developer, can make desired changes. Then, if a static Dashboard is desired, set it back to *False*. Finally, be sure to deploy the actual .xml Save file with the reporting application to the production server. Default: *True* |
| Dashboard Columns | Specifies the number of vertical columns (1- 8) the Dashboard should be divided into. Columns are automatically sized to fit the available space. When Allow Free-form Layout is *True*, this attribute must be *0*. Default: *3.* |
| Dashboard Tabs | When *True*, allows the user to put Dashboard panels into different tabs. The user can create, rename, reposition and remove tabs. The initial tab is created automatically. |
| Disable Gallery Updates | Specifies whether users can delete panels at runtime from the gallery specified below in the Gallery File attribute. Default: *True*. |
| Disable Global Filters from Panels | When Auto Global Filters attribute set to *True*, the user is able to click certain types of visualizations, such as charts, to add or update a global filter. Setting the attributes to *True* will prevent those clicks from adding Dashboard global filters. |
| Gallery Bookmark Collection | Specifies a separate file/location to store the gallery items as bookmarks. The default (and recommended) value is the default bookmark collection of the application. |
| Gallery Caption | Specifies a caption for the gallery specified below in the Gallery File attribute. This caption appears in the list of galleries in the Add Panels pop-up panel. |
| Gallery File | Specifies the fully-qualified file path and name of an XML file where charts and tables created by users at runtime using an Analysis Grid can be accessed for use in the Dashboard. This file is independent of the Dashboard's Save File, allowing the visualizations to be shared and used by multiple Dashboards. For example, the attribute value might be: @Function.AppPhysicalPath~\GalleryFiles\Gallery.xml  When a Gallery File is specified here, *do not* add Panel child elements under the Dashboard element. A Gallery File is created by using an Analysis Grid with a Custom Dashboard Panels element. The latter element's Dashboard Save File attribute is set to the name of an XML file that becomes the Gallery File. This file will be created and updated as the user adds visualizations in the Analysis Grid. Gallery files can also be stored in a database, see [Storing Bookmark, Gallery, and Save Files in a Database](https://devnet.logianalytics.com/hc/en-us/articles/4419707679255-Storing-Bookmark-Gallery-and-Save-Files-in-a-Database). |
| ID | (Required) Specifies a unique identifier for this element. |
| New for 14.2Maximum Panel Count | Specifies the number of panels that can display in a Dashboard. If there is no constant, or its value is empty, this function is disabled. |
| New for 14.2Maximum Panels Per Tab | Specifies the number of panels per Dashboard tab. If there is no constant, or its value is empty, this function is disabled. |
| Save File Starter | Specifies a file to be used as the initial Save File in cases when the Save File does not exist yet. For example, when the Save File is different for each user, the Save File Starter file can include a set of default tabs and panels. See [Creating a Default Panel Arrangement](https://devnet.logianalytics.com/hc/en-us/articles/4419707741335-Creating-a-Default-Panel-Arrangement-) for more information. |
| Template Modifier File | The name of the template modifier file, if any. See [Customizing Dashboard Appearance](https://devnet.logianalytics.com/hc/en-us/articles/4419707742231-Customizing-Dashboard-Appearance-) for more information about template modifiers. The template modifier file can be in any folder accessible to the web application; if a fully-qualified file path is not provided in this attribute value, then the application expects it to be is your project's \_SupportFiles folder. |
