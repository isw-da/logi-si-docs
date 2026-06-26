---
title: "Saving Dashboard Settings "
id: 4419723075735
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723075735-Saving-Dashboard-Settings
updated_at: 2022-07-17T02:23:54Z
---

# Saving Dashboard Settings 

# Saving Dashboard Settings

Given that users can potentially customize a Dashboard at runtime, it's useful to be able to save those customizations for future use. There are several ways to do this.

## Save Files

The **Save File** is an XML file that stores a record of the Dashboard changes users make at runtime. Its data is associated internally with IDs for the Dashboard and panels used to create it.

![](https://devnet.logianalytics.com/hc/article_attachments/7522807584535/introdash_11.png)

The Dashboard element's **Save File** attribute specifies a fully-qualified path and file name, as shown above, for the Save File. Tokens may be used in the path and file name. This creates the opportunity for reusing an individual user's configuration for their next session through the use of Logi Security, or a GUID-and-cookie scheme, tying the user name to the Safe File. For example:

C:\inetpub\wwwroot\myLogiApp\SavedDash\DashConfig.xml  
@Function.AppPhysicalPath~\SavedDash\DashConfig.xml  
@Function.AppPhysicalPath~\SavedDash\@Function.UserName~.xml

In the examples shown above, a special folder "SavedDash" has been created by the developer in the application folder to hold Dashboard Save Files and is shown
as part of the Save File path. (Extra spaces in the examples are just there for reading clarity).

## Gallery Files

A **Gallery File** contains the same data as a Save File and its attribute accepts the same values and tokens. However, unlike a Save File, it's not associated internally with a specific Dashboard and its panels. Instead, it's created using an Analysis Grid and can be copied, moved, and shared between Logi applications and users, providing an independent collection of visualizations as a resource.
The **Extra Gallery File** element, a child of the Dashboard element, allows you to specify additional gallery files. When multiple gallery files have been specified and the user is adding panels to a Dashboard, he'll be able to select them from different visual galleries.
![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) The general Logi Info development rule that elements requiring an element ID be given *unique* IDs is very important when dealing with Extra Gallery Files. For example, if a Dashboard and a gallery file both refer to Dashboard panels that have the same element ID, an "duplicate panel" error will occur.
How are extra gallery files useful? Imagine a scenario in which a gallery file of pre-configured "standard" panels is created and then shared with all users as an extra gallery file. They could then build Dashboards using panels from this standard gallery and/or from their personal gallery.

![](https://devnet.logianalytics.com/hc/article_attachments/7522838372247/introdash_12.png)

The Extra Gallery File element, shown above, requires a fully-qualified file path and name, with .xml extension, to the file. Other optional attributes allow you to specify whether users can modify the panels in the gallery (Disable Gallery Update) and specify the name
that will appear in the list of gallery choices (Gallery Caption) that will appear in the Add Panels pop-up panel.
The element also has a Security Right ID attribute, so access
to gallery files can be controlled using security rights. Multiple Extra Gallery File elements may be used.

## Using a Report Definition as an Extra Gallery File

There's also another interesting way to share gallery visualizations: the Extra Gallery File element's **Gallery File** attribute can be configured to point to a regular Logi report definition (.lgx) file. If that definition file includes a Dashboard element with child **Panel** elements containing visualizations, the application will locate those panels in the definition and also
make *them* available
in the Visual Gallery.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) Do not use definitions with Panels that get their data using *linked datalayers* as Extra Gallery Files. Linked datalayers used to create the content of Panel elements in this scenario are not recognized and the content will not be available. If possible, replace the linked datalayers with regular datalayers in order to make definitions work as Extra Gallery Files.

  

### Bookmarks

A Bookmark for a report page that includes a Dashboard, when created manually using **Action.Add Bookmark**, stores Request and Session variables and a *reference* to the Dashboard's Save File. It does not *contain* the Dashboard configuration data itself.
For more information, see [Bookmarks](https://devnet.logianalytics.com/hc/en-us/articles/4419707675287-Bookmarks).

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) Manual bookmarks can be created independently of updates to the Dashboard configuration (and, therefore, updates to the Save File). So running a bookmark for a page containing a Dashboard may not necessarily reproduce the Dashboard configuration that existed at the time the bookmark was created.
Automatic Bookmarks (see [Adding Automatic Bookmarks](https://devnet.logianalytics.com/hc/en-us/articles/4419715359511-Adding-Automatic-Bookmarks)), created using the **Auto Bookmark** element, on the other hand, will automatically create a bookmark *and* the bookmark equivalent of a Save File whenever the Dashboard configuration is changed, giving you the best of both worlds. Do not specify a Save File value when using this child element.

![](https://devnet.logianalytics.com/hc/article_attachments/7522838381847/introdash_13.png)

When Automatic Bookmarks are in use, Undo and Redo icons will appear beside the tabs, as shown above.
You can also store your Bookmarks, Save files, and Gallery files in a SQL database. See [Bookmarks](https://devnet.logianalytics.com/hc/en-us/articles/4419707675287-Bookmarks) for more information.
