---
title: "Which Application Sub-Folders?"
id: 4419707589271
section: "Manage - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707589271-Which-Application-Sub-Folders
updated_at: 2022-07-17T01:49:03Z
---

# Which Application Sub-Folders?

# Which Application Sub-Folders?

Your web server account will, of course, have to be able to
*read* all of the files in your application folder.

The two sub-folders in your Logi application folder that will routinely
need to have *Write* permissions granted to them are
**rdDataCache** and **rdDownload**. The latter is often used as a
convenient place to hold temporary files and does not necessarily have
anything to with actual downloads.

If, in the course of your development work, you add your own new
sub-folders to hold data files or "save files" used with
elements like a Dashboard, or decide to write data to another folder, you
will need to grant *Write* and possibly even
*Full Control* permissions to them as well.

One approach that guarantees access is to give
*Full Control* permissions to the Logi application folder itself
(which is what Studio's New Application wizard does). All files and
folders within the app folder then inherit the permissions. However, this
is not necessary and, as mentioned earlier, may cause security concerns.
