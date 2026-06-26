---
title: "Temporary Cache File Management"
id: 4419707838871
section: "Manage - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707838871-Temporary-Cache-File-Management
updated_at: 2023-03-19T10:18:57Z
---

# Temporary Cache File Management

# Temporary Cache File Management

The files that make up a Logi application are contained in a single application root folder that has a number of standard sub-folders. Many of these sub-folders have specific purposes; two of the most interesting standard sub-folders are **rdDataCache** and **rdDownload**. These folders hold temporary files for caching data and other purposes; they are managed automatically.

The following topics discuss the temporary cache file management folders:

* [The rdDataCache Folder](https://devnet.logianalytics.com/hc/en-us/articles/4419707837975-The-rdDataCache-Folder)
* [The rdDownload Folder](https://devnet.logianalytics.com/hc/en-us/articles/4402880007831)
* [Temporary File Clean Up](https://devnet.logianalytics.com/hc/en-us/articles/4419707839895-Temporary-File-Clean-Up)

## About Temporary Cache Files

As you may know, physically a Logi application consists of a single folder that contains a number of standard sub-folders and files. Many of these sub-folders have specific purposes. For example, .css files placed in the *\_SupportFiles* folder will appear in Logi Studio automatically and will be included in selection lists for assigning style sheets.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699900951/tempcache_01.png)

Two of the most interesting standard sub-folders are *rdDataCache* and *rdDownload*; they have a mechanism associated with them that makes web server storage maintenance much easier.
