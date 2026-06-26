---
title: "Creating Application Pools in IIS 6"
id: 4406822546711
section: "Install, Upgrade, & Remove - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822546711-Creating-Application-Pools-in-IIS-6
updated_at: 2022-04-06T06:09:02Z
---

# Creating Application Pools in IIS 6

# Creating Application Pools in IIS 6

Microsoft IIS 6 introduced **Application Pools** as a method of isolating different applications within the server, in order to provide improved reliability. The "Default Application Pool" is created by default at installation and all virtual directory applications, when created, are assigned to this default pool.

However, applications using different .NET versions can't be run at the same time in the same pool. If they are, error messages will appear for whichever application is started last. The
recommended
practice
is
to create a new application pool and assign all applications that use the same .NET version to it.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583717783/upgrstudio_06.png)

To create a new application pool:

1. Open the IIS Manager (see All Programs![](https://devnet.logianalytics.com/hc/article_attachments/4417583616279/menuarrowrt.png)Administrative Tools )
2. Select and right-click the **Applications Pools** item in the list on the left. Select **New Application Pool...** from the pop-up menu.
3. Enter the new name of your choice as the Application Pool ID and leave the default pool settings selected. Click **OK**
4. Expand the Application Pools item in the list on the left to see your new pool.
  

![](https://devnet.logianalytics.com/hc/article_attachments/4417563071255/upgrstudio_07.png)

To assign an application to the new Application Pool:

1. Expand the **Web Sites** item in the list on the left.
2. Select and right-click the virtual directory representing your application. Select **Properties** from the popup menu.
3. Select the new application pool you just created from the list of Application Pools in the Properties dialog box.
4. Click **OK**

If you have any doubt about which version of .NET your application is set to use:

![](https://devnet.logianalytics.com/hc/article_attachments/4417583718551/upgrstudio_08.png)

Click
the **ASP.NET** tab on the Properties dialog box and inspect the ASP.NET version selection.
