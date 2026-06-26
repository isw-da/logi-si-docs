---
title: "Using the Dashboard Element "
id: 4406817728791
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817728791-Using-the-Dashboard-Element
updated_at: 2022-04-06T06:07:51Z
---

# Using the Dashboard Element 

# Using the Dashboard Element

Only one Dashboard element is allowed per
report definition. Four child elements, discussed in other topics, are used with the Dashboard element. *We do not recommend that you use this element within an embedded sub-report*.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583797655/introdash_15.png)

Let's examine the Dashboard element's attributes:

| Attribute | Description |
| --- | --- |
| ID | (Required) Specifies a unique identifier for this element. |
| Save File | (Required) Specifies the fully-qualified file path and name of an XML file where dashboard changes users make at runtime are saved.  This value is *not* required and you *must* leave it blank if you're using the Auto Bookmark child element with the dashboard, see [Bookmarks](https://devnet.logianalytics.com/hc/en-us/articles/4406822405143-Bookmarks). Tokens may be used in this attribute, however, @Request tokens are *not* recommended as they're not persistent. If the file doesn't exist it will be created at first use; however its containing folder *will not* be automatically created. If Logi Security has been used in the project to control access, the user's name will appear in the @Function.UserName~ token. This can be embedded into the Save File attribute to provide separate files for individual users. For example, the attribute value might be: @Function.AppPhysicalPath~\DashSaveFiles\@Function.UserName~.xml  which might translate to: C:\inetpub\wwwroot\MyDashboardApp\DashSaveFiles\BillGates.xmlSave files can also be stored in a database, see [Storing Bookmark, Gallery, and Save Files in a Database](https://devnet.logianalytics.com/hc/en-us/articles/4406817598487-Storing-Bookmark-Gallery-and-Save-Files-in-a-Database). |
| Allow Free-form Layout | Specifies whether Free-form Layout mode is enabled. This layout mode allows dashboard panels to be placed wherever desired by the user, instead of fitting into a columnar arrangement. When disabled, users must arrange panels in pre-defined columns. When this attribute is *True*, the Dashboard Columns attribute must be *0*. Default: *False* |
| Auto Global Filters | Specifies whether dashboard panels with Analysis Filters, and/or those generated from an Analysis Grid that uses the Active Query Builder element, will have global filters created automatically. Default: *False* |
| Auto Panel Filters | Specifies whether dashboard panels generated from an Analysis Grid that uses the Active Query Builder element will have panel filters created automatically, based on its metadata. Default: *False* |
| Dashboard Adjustable | Determines if the user is allowed to add, remove and manage tabs and panels. Set this attribute to *False* for a static dashboard that users cannot change. When set to *True*, the user's dashboard changes are saved to the location specified in the Save File attribute.  When set to *False*, the user cannot save changes, but the Save File is still used to control the dashboard appearance. Therefore, set this to *True* during the development process so that you, the developer, can make desired changes. Then, if a static dashboard is desired, set it back to *False*. Finally, be sure to deploy the actual .xml Save file with the reporting application to the production server. Default: *True* |
| Dashboard Columns | Specifies the number of vertical columns (1- 8) the dashboard should be divided into. Columns are automatically sized to fit the available space. When Allow Free-form Layout is *True*, this attribute must be *0*. Default: *3* |
| Dashboard Tabs | When *True*, allows the user to put dashboard panels into different tabs. The user can create, rename, reposition and remove tabs. The initial tab is created automatically. |
| Disable Gallery Updates | Specifies whether users can delete panels at runtime from the gallery specified below in the Gallery File attribute. The default value is *True*. |
| Disable Global Filters from Panels | When Auto Global Filters attribute set to *True*, the user is able to click certain types of visualizations, such as charts, to add or update a global filter. Setting the attributes to *True* will prevent those clicks from adding dashboard global filters. |
| Gallery Caption | Specifies a caption for the gallery specified below in the Gallery File attribute. This caption appears in the list of galleries in the Add Panels pop-up panel. |
| Gallery File | Specifies the fully-qualified file path and name of an XML file where charts and tables created by users at runtime using an Analysis Grid can be accessed for use in the dashboard. This file is independent of the dashboard's Save File, allowing the visualizations to be shared and used by multiple dashboards. For example, the attribute value might be: @Function.AppPhysicalPath~\GalleryFiles\Gallery.xml  When a Gallery File is specified here, *do not* add Panel child elements under the Dashboard element. A Gallery File is created by using an Analysis Grid with a Custom Dashboard Panels element. The latter element's Dashboard Save File attribute is set to the name of an XML file that becomes the Gallery File. This file will be created and updated as the user adds visualizations in the Analysis Grid. Gallery files can also be stored in a database, see [Storing Bookmark, Gallery, and Save Files in a Database](https://devnet.logianalytics.com/hc/en-us/articles/4406817598487-Storing-Bookmark-Gallery-and-Save-Files-in-a-Database). |
| Save File Starter | Specifies a file to be used as the initial Save File in cases when the Save File does not exist yet. For example, when the Save File is different for each user, the Save File Starter file can include a set of default tabs and panels. See [Creating a Default Panel Arrangement](https://devnet.logianalytics.com/hc/en-us/articles/4406817722519-Creating-a-Default-Panel-Arrangement-) for more information. |
| Template Modifier File | The name of the template modifier file, if any. See [Customizing Dashboard Appearance](https://devnet.logianalytics.com/hc/en-us/articles/4406817723543-Customizing-Dashboard-Appearance-) for more information about template modifiers. The template modifier file can be in any folder accessible to the web application; if a fully-qualified file path is not provided in this attribute value, then the application expects it to be is your project's \_SupportFiles folder. |
