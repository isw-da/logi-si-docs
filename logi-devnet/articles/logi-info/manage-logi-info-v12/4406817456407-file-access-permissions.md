---
title: "File Access Permissions"
id: 4406817456407
section: "Manage - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817456407-File-Access-Permissions
updated_at: 2022-04-06T06:06:14Z
---

# File Access Permissions

# File Access Permissions

A Logi Info application resides within an *application folder* on
the web server.

The following topics discuss additional details for granting file access permissions:

* [Which Accounts?](https://devnet.logianalytics.com/hc/en-us/articles/4406817457943-Which-Accounts-#Accounts)
* [Which Application Sub-Folders?](https://devnet.logianalytics.com/hc/en-us/articles/4406817458967-Which-Application-Sub-Folders-#Folders)
* [Granting File Permissions Under Windows](https://devnet.logianalytics.com/hc/en-us/articles/4406817455383-Granting-File-Permissions-Under-Windows#Permissions)

## About File Access Permissions

A Logi Info application, on your web server, consists of an
*application folder* with a set of sub-folders and files. The
application will need to write data into some of those sub-folders; for
example, data caching, temporary file creation, and exports are a few of
the operations that do that.

However, the **security settings** for these folders may prohibit file
writing by accounts normally used to run web applications like a Logi
application.

Applications created using the New Application wizard in Logi Studio
generally set these file permissions for you on your development machine,
as discussed below. However, if you manually create or copy an
application, they may not be set correctly, so you may need to explicitly
grant file access permissions to the application folders (which are
identified below).

### Tell-Tale Errors

If you receive these or similar errors when trying to preview or browse
your report:

There was a problem running a DataLayer. The error was: The web
application is unable to write to a folder.

Unable to save to the data cache. The file was: <application file
path>\rdDataCache\???.xml. Access to the path is denied.

Access to the path 'C:\inetpub\wwwroot\HelloWorld\MyData' is
denied.
then it is most likely that you need to grant Write permissions to the
*rdDataCache*, *rdDownload*, and/or other folders.

### .NET Application? Let The New App Wizard Do It

If you use the New Application Wizard in Studio (File![](https://devnet.logianalytics.com/hc/article_attachments/4417583616279/menuarrowrt.png)New Application...) to create a Logi .NET application, it will set the
appropriate file permissions for you. It actually provides a pretty
wide-open security setting, granting all rights to everyone, and you may
care to set more restrictive rights manually. You may, nonetheless, need
to manually grant rights when you deploy your application to a production
server.

Generally, if your application does anything more than put simple text on
a page, granting file permissions will be required and you'll need to do
this for each Logi application you develop and deploy.

### Java Application? Usually Done for You
