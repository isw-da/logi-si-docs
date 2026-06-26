---
title: "Using the Report Author"
id: 4419723131799
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723131799-Using-the-Report-Author
updated_at: 2022-07-17T02:23:35Z
---

# Using the Report Author

# Using the Report Author

Using the Report Author element is very easy:

![](https://devnet.logianalytics.com/hc/article_attachments/7522804334359/rptauthor_08.png)

As shown above, add the Report Author element to your report definition. Examples of the attribute values are:

* *Gallery File* = @Function.AppPhysicalPath~\GalleryFiles\RAGallery.xml
* *Save File* = @Function.AppPhysicalPath~\GalleryFiles\RASaveFile.xml
* *Uploaded File Folder* = @Function.AppPhysicalPath~\GalleryFiles\images

As described in [Report Author Attributes](https://devnet.logianalytics.com/hc/en-us/articles/4419707799959-Report-Author-Attributes), if Logi Security is in use, you could further differentiate the files and folders using the @Function.UserName~ token.

That's all you need to do. The Report Author element provides a huge amount of functionality with very little developer effort.

## Extra Gallery Files

The **Extra Gallery File** element,a child of the Report Author element, allows you to specify additional gallery
files. When multiple gallery files have been specified and the user is
adding visuals to a report, he'll be able to
select them from different visual galleries.

How are extra gallery files useful? Imagine a scenario in which a
gallery file of pre-configured "standard" visualizations is created and
then shared with all users as an extra gallery file. They could then
build reports using visualizations from this standard
gallery and/or from their personal gallery.

![](https://devnet.logianalytics.com/hc/article_attachments/7522789756695/rptauthor_09.png)

The Extra Gallery File element, shown above, requires a
fully-qualified file path and name, with .xml extension, to the file.
Other optional attributes allow you to specify whether users can modify
the visuals in the gallery (Disable Gallery Update) and specify the name
that will appear in the list of gallery choices (Gallery Caption). The
element also has a Security Right ID attribute, so access
to gallery files can be controlled using security rights. Multiple Extra Gallery File elements may be used.

There's also another interesting way to share gallery visualizations: the Extra Gallery File element's **Gallery File** attribute can be configured to point to a regular Logi report definition (.lgx) file. If that definition file includes a Dashboard element with child **Panel** elements containing visualizations, the application will locate those panels in the definition and also make *them*
available
in the Visual Gallery.

Gallery files can also be stored in a database, see [Storing Bookmark, Gallery, and Save Files in a Database](https://devnet.logianalytics.com/hc/en-us/articles/4419707679255-Storing-Bookmark-Gallery-and-Save-Files-in-a-Database).
