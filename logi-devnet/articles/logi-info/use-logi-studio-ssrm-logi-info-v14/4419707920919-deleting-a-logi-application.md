---
title: "Deleting a Logi Application"
id: 4419707920919
section: "Use Logi Studio/SSRM - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707920919-Deleting-a-Logi-Application
updated_at: 2022-07-17T01:31:51Z
---

# Deleting a Logi Application

# Deleting a Logi Application

If you want to **delete** an entire Logi application, you can do so by using your file system tools, such as Windows Explorer, to delete the entire application folder.

First, in IIS Manager or other web server management tool, delete the virtual directory or web application entry for the app.

Then, delete the application folder. On a typical Windows server platform, for example, you would delete:

C:\inetpub\wwwroot\*yourAppFolder*

and all its subfolders and files.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599575/noteicon.png) Your web server may hold some application files open to improve performance and you may receive an "Access Denied" type error when you try the folder deletion. If this happens, try stopping and restarting the web server. For IIS, this can be done very easily by running iisreset.exe from the Start Menu ![](https://devnet.logianalytics.com/hc/article_attachments/4419706652439/menuarrow.gif) Run option or
from a
command line window. Once the web server is restarted, try deleting the application folder again.

Afterwards, in Studio, your application will still appear in the **Recent Applications** panel of the Welcome tab. Click its entry, as if to open it, and Studio will display a warning that it no longer exists and remove it from its list of recent applications.
