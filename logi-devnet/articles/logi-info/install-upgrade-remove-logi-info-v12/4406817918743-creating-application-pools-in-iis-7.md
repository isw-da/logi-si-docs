---
title: "Creating Application Pools in IIS 7+"
id: 4406817918743
section: "Install, Upgrade, & Remove - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817918743-Creating-Application-Pools-in-IIS-7
updated_at: 2022-04-06T06:09:01Z
---

# Creating Application Pools in IIS 7+

# Creating Application Pools in IIS 7+

The **Application Pool** is a method of isolating different .NET applications within the web server, in order to provide improved reliability. The default application pool, "DefaultAppPool" is created at installation and all virtual directory applications, when created, are assigned to this default pool.

However, applications using different .NET versions can't be run at the same time in the same pool. If they are, error messages will appear for whichever application is started last. The
recommended
practice
is
to create a new application pool and assign all applications that use the same .NET version to it.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583717271/upgrstudio_09.png)

To create a new application pool:

1. Open the IIS Manager (see All Programs![](https://devnet.logianalytics.com/hc/article_attachments/4417583616279/menuarrowrt.png)Administrative Tools )
2. Select and right-click the **Applications Pools** item in the list on the left. Select **Add Application Pool...** from the pop-up menu.
3. Enter the new name of your choice as the Application Pool ID and leave the default pool settings selected. Click **OK**
4. Right-click the Application Pools item in the list on the left and click **Refresh** to see your new pool.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583717527/upgrstudio_10.png)

To assign an application to the new Application Pool:

1. Expand the **Sites** item in the list on the left, then expand the **Default Web Site** item below it.
2. Find and select your application in the list.
3. In the right-hand Actions Panel, click **Basic Settings...**
4. A dialog box like the one shown above will appear. Click **Select...** and choose your new Application Pool from the list.
5. Click **OK**.

Your application is now assigned to your new Application Pool.
