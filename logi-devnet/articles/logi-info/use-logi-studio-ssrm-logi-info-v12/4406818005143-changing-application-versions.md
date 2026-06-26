---
title: "Changing Application Versions"
id: 4406818005143
section: "Use Logi Studio/SSRM - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406818005143-Changing-Application-Versions
updated_at: 2022-04-06T06:09:36Z
---

# Changing Application Versions

# Changing Application Versions

A Logi application includes files and settings installed on the web server and *version-specific* binary files included in each Logi application project folder. This allows each Logi application to maintain its own **version identity** and allows backward compatibility from new versions of Logi products.

Applications can be **upgraded** and **downgraded** to different versions and, when a new version of Logi Info is installed, applications must be upgraded before they'll have the benefits of the new version.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575495959/usingstudio_61.png)

When you open an application, Studio displays a **warning** in its Application tab, as shown above, if the application's version does not match the version of Studio being used. Applications will continue to run correctly with this mismatch but, as the warning says, the rules governing element relationships and attributes may be incorrect when editing definitions.

For existing Logi .NET and Java applications, Studio provides a quick and easy way to change versions:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575496343/usingstudio_62.png)

To change versions, click the **Change Version...** link, shown above. This will display a wizard with a list of the installed versions and, after you select one, will replace the application's version-specific binary files with the files of the selected version. The replacement may take several minutes. *This will not affect any definitions or support files you have created and you can revert the change*.

For .NET applications, the **Server Manager**, which can be launched from Studio's Tools menu, can also be used to change application versions. This is a tool that allows you to examine all of the .NET Logi applications on the local web server and manage them.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563021079/usingstudio_63.png)

The **Server Manager** dialog box, shown above, displays a list of the applications installed on the local web server. Select one or more applications (1) and the desired product versions (2), and click Change Version... (3). The process usually takes less than a minute for each application selected.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) Server Manager is intended for use *only* with .NET applications, using the IIS or Cassini web servers; if neither one of these servers is installed, Server Manager will prompt you to install them.

For additional important information about changing application versions, see [Logi Product Upgrades](https://devnet.logianalytics.com/hc/en-us/articles/4406817922839-Logi-Product-Upgrades).
