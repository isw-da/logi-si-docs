---
title: "Working with Gallery Files"
id: 4406817206423
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817206423-Working-with-Gallery-Files
updated_at: 2022-04-06T06:04:38Z
---

# Working with Gallery Files

# Working with Gallery Files

![](https://devnet.logianalytics.com/hc/article_attachments/4417583690775/ssrmv12.7.png)InfoGo now stores visualizations as bookmarks, not in Gallery or Extra Gallery files. Information about migration of existing gallery items into bookmarks can be found in [Upgrade the Self-Service Reporting Module](https://devnet.logianalytics.com/hc/en-us/articles/4406817916311-Upgrade-the-Self-Service-Reporting-Module).

Users working with InfoGo versions prior to 12.7 can save the charts and other visualizations they create in a "Visual Gallery". By default this is each user's personal collection and, when they subsequently create Dashboards and Reports, they choose the panels and visualizations to include from this private gallery. The visual gallery data is stored in a personal gallery file based on the user's name and InfoGo is configured by default to access this file.

It's also possible to store Gallery and Save files in a SQL database. Logi Studio includes a migration tool and a special **File To Database Mapping** element that make it easy to transfer existing bookmark files into a database, and then use them from there. For more information about migrating these files, see [Storing Bookmark, Gallery, and Save Files in a Database](https://devnet.logianalytics.com/hc/en-us/articles/4406817598487-Storing-Bookmark-Gallery-and-Save-Files-in-a-Database).

## Extra Gallery Files

The **Extra Gallery File** element, a child of the Dashboard and Report Author elements, allows you to specify additional gallery files. When multiple gallery files have been specified and the user is adding panels or visuals to a Dashboard or Report, he'll be able to select them from different visual galleries.

Extra Gallery File elements are added and configured in the goExtraGalleryFiles definition, in the goCustomizations folder in Studio.

How are extra gallery files useful? Imagine a scenario in which a gallery file of pre-configured "standard" visualizations is created and then shared with all users as an extra gallery file. They could then build dashboards and reports using visualizations from this standard gallery and/or from their personal gallery.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563442967/cfginfogo125_18.png)

The Extra Gallery File element, shown above, requires a fully-qualified file path and name, with .xml extension, to the file. Other optional attributes allow you to specify whether users can modify the visuals in the gallery (Disable Gallery Update) and specify the name that will appear in the list of gallery choices (Gallery Caption). The element also has a Security Right ID attribute, so access
to gallery files can be controlled using security Rights.

Extra gallery files to be shared are typically created by a developer who temporarily manipulates the gallery file path and name in InfoGo manually, then creates and saves the desired visuals. That file path and name are specified in the goAnalysisGrid definition, in the **Custom Dashboard Panels** element's **Dashboard Save File** attribute value. Once the extra gallery has been created, the original file path and name are restored. The file path and name of the extra gallery file are then
used in the Extra Gallery File element.

There's also another interesting way to share gallery visualizations: the Extra Gallery File element's **Gallery File** attribute can be configured to point to a regular Logi report definition (.lgx) file. If that definition file includes a Dashboard element with child **Panel** elements containing visualizations, the application will locate those panels in the definition and also make *them* available in the Visual Gallery.

## Saving Other Visualizations

As delivered, InfoGo allows users to save visualizations made with its analysis tools to the visual gallery. However, as a developer, you may wish to add elements or definitions to the application which include coded visualizations *not* created with these tools, and you might want to save them to the gallery, too. Here are the steps to do this:

1. Ensure that you have an **Extra Gallery File** element configured in the goCustomizations.goExtraGalleryFiles definition. You can add an additional Extra Gallery Fileelement for this purpose, if you need to. Its Gallery File attribute should point to the Dashboard Save File used by the target dashboard.
2. In the definition with your visualization, add a Link, Button, or Image element with an **Action.Add Dashboard Panel** element
   beneath it. This will be the element clicked to save the visualization to the gallery.
3. In the Action element's **Add Panel Content Element ID** attribute, specify the element ID of the visualization to be saved.
4. In its **Dashboard Save File** attribute, specify the value from the Extra Gallery File element's **Gallery File** attribute.
5. In its **Image** attribute, specify name of a thumbnail image of your visualization, less than 200 pixels wide.

When the report is run and the Save link, image, or button is clicked, the user will prompted for a title and descriptive text and the visualization will be saved to the gallery. From there it will be available for use in a dashboard or report like any other visualization.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) Visualizations in a *different* Logi application cannot be saved in this way.

More information about the Action.Add Dashboard Panel element is available in [Logi Info Dashboard](https://devnet.logianalytics.com/hc/en-us/articles/4406817724567-Logi-Info-Dashboard-).
