---
title: "Working with Support Files"
id: 4419722914839
section: "Introduction to Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722914839-Working-with-Support-Files
updated_at: 2022-07-17T02:07:46Z
---

# Working with Support Files

# Working with Support Files

This topic provides answers to frequently-asked questions about working with support files:

1. [I tried to add an Excel template to my application and received an
   "Access denied" error message.](#AddFile)
2. [I tried to save data in an XML data file and received an "Access
   denied" error message.](#XMLFile)
3. [Where did the files I saved in rdDownload go? They've been deleted](#rdDownload).
4. [What kinds of image files can I use with Logi applications?](#ImgTypes)
5. [Can #ID type class definitions be used in style sheets with Logi
   applications?](#ClassSelectors)
6. [Can external HTML files be embedded within Logi reports?](#HTMLFile)
7. [Does Logi Studio include some kind of style sheet editor or do I need
   to get one of my own?](#ExtCSS)
8. [How can I organize my support files in the \_SupportFiles folder into
   sub-folders?](#SuppFiles)
9. [Can I use URLs or tokens to refer to external images with the Image
   element?](#ImageURLs)
10. [What happened to the \_Images folder? I don't see it anymore in new
    applications.](#ImagesFolder)
11. [How can I organize files within the \_SupportFiles folder?](#OrganizeFiles)

## 1. I tried to add an Excel template to my application and received an "Access denied" error message.

This can occur if you still have the template file open in Excel
while trying to add it to your application's Support Files. Close the file
in Excel before trying to add it to your project.

## 2. I tried to save data in an XML data file and received an "Access denied" error message.

In order to allow the account used by the web server to run Logi
applications to write to the server's hard drive, you must give it
permission to do so. This is described in detail in
[File Access Permissions](https://devnet.logianalytics.com/hc/en-us/articles/4419707587351-File-Access-Permissions).

## 3. Where did the files I saved in rdDownload go? They've been deleted.

Two folders, rdDataCache and rdDownload, in your Logi application folder
are used by the server engine to store *temporary* files. Any files
in these folders are automatically "cleaned up" (deleted)
periodically. If you want to write data out to files or export reports and
retain them, we recommend you create a new folder in the application
folder and place them there.

## 4. What kinds of image files can I use with Logi applications?

Logi apps will work with image files in these formats: .gif, .jpg, .jpeg,
.png, .bmp, .wmf, .xbm, .art

## 5. Can #ID type class definitions be used in style sheets with Logi applications?

Yes. For complete information about the class definitions that can be used
with Logi apps, see [Using Style Sheets](https://devnet.logianalytics.com/hc/en-us/articles/4419715511703-Using-Style-Sheets).

## 6. Can external HTML files be embedded within Logi reports?

Yes. The **Include HTML** and **HTML File** elements can be used to
embed HTML code and external HTML files, respectively, into Logi reports.
For more information, see [Insert HTML into Reports](https://devnet.logianalytics.com/hc/en-us/articles/4419722951831-Insert-HTML-into-Reports).

## 7. Does Logi Studio include some kind of style sheet editor or do I need to get one of my own?

Logi Studio provides two ways to edit styles sheets. It includes a
content-specific, internal style sheet editor, which opens in a tab inside
the Studio Workspace panel, and the Class Selector tool which allows class
editing and previewing within Studio. Menu options within Studio can also
launch whatever external CSS editor you may own that's associated with the
.css file extension. Logi applications also [Themes](https://devnet.logianalytics.com/hc/en-us/articles/4419723357847-Themes), some of which are provided, and Studio includes a Theme Editor tool so
you can create customized themes.

## 8. How can I organize my support files in the \_SupportFiles folder into sub-folders?

If you create a new sub-folder, such as "images", under Support
Files in Studio's Application panel, and give your support files names
that begin with the sub-folder name, such as "images.logo.png",
they will appear in Studio's Application panel organized into virtual
sub-folders, for example, as "logo.png" beneath the
"images" folder. You can also drag files into the folders and
have Studio rename them automatically (see #11 below).

## 9. Can I use URLs or tokens to refer to external images with the Image element?

Yes. Generally, if you just supply a file name in the Image element's
Caption attribute, it assumes your image file to be in the \_SupportFiles
folders. If you supply a complete URL
("http://somesite/myImage.gif") instead, this assumption is
overridden. However, using a token in the Caption to supply a URL can be
problematic, due to the timing of token evaluation. The solution is to
force the Caption to be considered as a URL, by entering
"http://" and then the token, like this:
"http://@Data.myURLToken~". Naturally, your token must not
contain the (now redundant) "http://" itself.

## 10. What happened to the \_Images folder? I don't see it anymore in new applications.

After the release of Logi Info v10, files formerly stored in individual
folders named \_Images, \_Stylesheets, \_IncHtmls, \_DataXMLs, and \_Scripts
were consolidated into the \_SupportFiles folder, with backward
compatibility provided (as long as file paths are not specified using
tokens).

## 11. How can I organize files within the \_SupportFiles folder?

Files can be organized within the \_SupportFiles folder by adding
sub-folders *from within**Studio's Application panel* (right-click the SupportFiles folder)
and dragging files into them. This automatically adds a prefix to the file
name. For example, if you created a sub-folder in Studio called
"images", a file named "myLogo.png" dragged into it
would be renamed "images.myLogo.png".

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) Using external
OS file system tools to create a sub-folder under \_Support files
*will not work* correctly; the sub-folder must be created within
Studio. After that, you can add files to \_SupportFiles externally,
manually including the prefix in the name, if desired. When working with
these organized files you must provide the complete file name; for
example, an Image element's Caption attribute value would be
"images.myLogo.png".
