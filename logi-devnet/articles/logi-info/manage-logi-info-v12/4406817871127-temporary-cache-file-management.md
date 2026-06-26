---
title: "Temporary Cache File Management"
id: 4406817871127
section: "Manage - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817871127-Temporary-Cache-File-Management
updated_at: 2022-04-06T06:08:46Z
---

# Temporary Cache File Management

# Temporary Cache File Management

The files that make up a Logi application are contained in a single
application root folder that has a number of standard sub-folders. Many of
these sub-folders have specific purposes; two of the most interesting
standard sub-folders are **rdDataCache** and **rdDownload**. These
folders hold temporary files for caching data and other purposes; they are
managed automatically.

The following topics discuss the temporary cache file management folders:

* [The rdDataCache Folder](https://devnet.logianalytics.com/hc/en-us/articles/4406817869975-The-rdDataCache-Folder#rdDataCache)
* [The rdDownload Folder](https://devnet.logianalytics.com/hc/en-us/articles/4406822530455-rdDownload-Folder#rdDownload)
* [Temporary File Clean Up](https://devnet.logianalytics.com/hc/en-us/articles/4406817872151-Temporary-File-Clean-Up#Cleaning)

## About Temporary Cache Files

As you may know, physically a Logi application consists of a single folder
that contains a number of standard sub-folders and files. Many of these
sub-folders have specific purposes. For example, .css files placed in the
*\_SupportFiles* folder will appear in Logi Studio automatically and
will be included in selection lists for assigning style sheets.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563087255/tempcache_01.png)

Two of the most interesting standard sub-folders are
*rdDataCache* and *rdDownload*; they have a mechanism associated
with them that makes web server storage maintenance much easier.
