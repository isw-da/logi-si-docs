---
title: "Changing .NET Application Versions"
id: 4419723189015
section: "Install, Upgrade, & Remove - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723189015-Changing-NET-Application-Versions
updated_at: 2022-07-17T01:36:28Z
---

# Changing .NET Application Versions

# Changing .NET Application Versions

In order to use all of the features in the latest Logi Info release, after you install it you will need to change the application version on all of your Logi applications. There are two methods for changing an application version:

![](https://devnet.logianalytics.com/hc/article_attachments/4419699913879/upgrstudio_04.png)

**1. Using Logi Studio** - When you open an application, Studio will display a warning in its Application tab, as shown above, if the application's version does not match the version of the Logi product being used. Click the **Change Version...** link to replace your Logi application's version-specific binary files with the files for a version that you select from a list of installed versions. *This will not affect any definitions or support files*.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714905367/upgrstudio_04a.png)

A progress indicator, like the one shown above, will be displayed.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714905623/upgrstudio_04b.png)

Changing an application version will also trigger some web server diagnostics to run after the upgrade and you'll see some information about that process. Once the tests end, you'll the results, as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599319/criticalicon.png) The failure of any test indicates that something is wrong with your web server environment's ability to run the upgraded application. This could be caused by a number of things, such as failing to install the new Logi version as an Administrator, or having incorrect file permissions on the application folder, or failing to have the correct version of .NET installed. Contact Logi Support for assistance.

**2. Using Server Manager** - You can also change application versions using Server Manager, which is installed with Studio and is available via Studio's Tools menu or the Start Menu. It's a tool that allows you to examine all of the Logi applications on the web server and manage them individually or in a batch.

![](https://devnet.logianalytics.com/hc/article_attachments/4419707084823/upgrstudio_05.png)

Server Manager, shown above, only works with .NET applications, using the IIS or Cassini web servers; if neither of these servers is installed, Server Manager will prompt you to install
them.
The Server Manager dialog box displays a table showing each application installed on the local web server and a list of all the Logi product versions installed on the machine. To change an application's version, check one or more applications, select the version desired, and click **Change Version**. The process usually takes less than a minute for each application selected. Versions can be upgraded or downgraded.
