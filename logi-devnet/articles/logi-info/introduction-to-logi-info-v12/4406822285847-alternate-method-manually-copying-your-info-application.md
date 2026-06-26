---
title: "Alternate Method: Manually Copying Your Info Application"
id: 4406822285847
section: "Introduction to Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822285847-Alternate-Method-Manually-Copying-Your-Info-Application
updated_at: 2022-04-06T06:05:37Z
---

# Alternate Method: Manually Copying Your Info Application

# Alternate Method: Manually Copying Your Info Application

If you don't have a version of Studio that includes the Application Deployment Tool, you can use another deployment approach that works well if you can map a shared network drive on the server: just *copy* your entire Logi application folder to the production server.

From an operational perspective, for .NET applications, it doesn't really matter where you put the folder on the server but other company-specific considerations (storage location conventions, security, space limits, etc.) may apply. For Java applications, depending on your specific web server, you may be required to place your app folder in a specific folder (for example, beneath the webapps folder for Apache/Tomcat).

![](https://devnet.logianalytics.com/hc/article_attachments/4417563341207/deployapp_10.png)

Just be sure that your copy operation gets *all* of the files and folders inside your application folder to the production server.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) If you develop your application on a 32-bit machine and copy it to a 64-bit production machine, *do not* copy the entire application folder, as some Logi Server Engine files in your app will be 32-bit-specific. Instead, either use the Deployment Tool and ensure that you deploy 64-bit engine files, or install Studio on your production server, use the New Application Wizard
to create
an empty 64-bit application, then copy only your definition and support files over from your development machine.

If you're distributing your application to a remote site, you can use a compression utility like **WinZip** to package your entire Logi application project folder into a single .ZIP file.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) This approach copies *all* of the Logi Server Engine files as well as the application files, so the version of the production application will be the same as that of the development application. This approach will also copy any license file in the application root folder to the production server, where it may not be viable.

Naturally, if you don't have a network connection to the production server, you can also use other methods, such as burning the entire application folder to a DVD or copying it to a USB "thumb drive" in order to move it to the production server.
