---
title: "Changing Java Application Versions"
id: 4419715499543
section: "Install, Upgrade, & Remove - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715499543-Changing-Java-Application-Versions
updated_at: 2022-07-17T01:36:27Z
---

# Changing Java Application Versions

# Changing Java Application Versions

In order to use all of the features in the latest Logi Info release, after you install it you will need to change the application version on all of your Logi applications.

The process for upgrading a Logi Java application on your development machine is the same as it is for .NET apps: use the **Change Version** link in Studio as discussed in [Changing .NET Application Versions](https://devnet.logianalytics.com/hc/en-us/articles/4419723189015-Changing-NET-Application-Versions).

The Server Manager tool discussed in [Changing .NET Application Versions](https://devnet.logianalytics.com/hc/en-us/articles/4419723189015-Changing-NET-Application-Versions) is intended for use *only* with .NET applications, and expects to work with the IIS or Cassini web servers. You cannot use Server Manager for Java applications.

Changing your Java application version on a Linux/Unix production server (which won't have Logi Studio or Server Manager installed as they are Windows apps) is a little more complicated. You could just copy the application files and folders from the development machine to the production machine but that will likely result in an undesirable proliferation of .jar files over time. Instead, we recommend the following:

1. Change the version of your Logi app on your development machine using Studio or Server Manager.
2. On the production server, create a new folder which will become your new Logi app folder.
3. Copy *everything* from the app folder on your development machine (which is the new version) to this new folder.
4. Copy any files specific to the production app, such as \_Settings.lgx, which might have different connection settings, from the original Logi app folder on the production server to the new app folder on the production server.
5. Rename the old and new app folders, or adjust any references so the new app folder is now the recognized location for your Logi app.
6. You may need to change the General element's Application Path attribute in \_Settings.lgx if the path or folder name have changed.
7. Test your application.
8. Archive or delete the old app folder on the production server.
