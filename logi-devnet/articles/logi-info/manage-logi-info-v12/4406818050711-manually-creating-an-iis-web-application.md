---
title: "Manually Creating an IIS Web Application"
id: 4406818050711
section: "Manage - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406818050711-Manually-Creating-an-IIS-Web-Application
updated_at: 2022-04-06T06:09:52Z
---

# Manually Creating an IIS Web Application

# Manually Creating an IIS Web Application

In some circumstances you may need to, or want to, create an IIS web
application manually. To do so, open the IIS Manager tool and examine the
list of folders and applications beneath the Default Web Site. If you find
it, right-click it and select *Convert to Application* from the
pop-up context menu.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583639191/iisreg_04.png)

As shown above, fill-in an **Alias** (this will be used in the URL to
run this application) and select an **Application Pool** (use the
*DefaultAppPool* selection shown unless you've created a special pool
for this application). The enter, paste, or browse to the correct Physical
Path for you Logi app's root folder. Click OK. Ensure that the new entry
was added to the list of applications beneath the correct web site.

You may want to create a separate Application Pool if you want to isolate
this application from others being run on the same web site. That can be
useful if you have to stop/restart your application but want to do so
without kicking all other users off the web site. More information about
Application Pools is available
[from Microsoft](https://docs.microsoft.com/en-us/iis/configuration/system.applicationhost/applicationpools/).

![](https://devnet.logianalytics.com/hc/article_attachments/4417562987799/iisreg_05.png)

The icon for your new web application will have changed from a folder to
an app icon. Select your new application in the list and, from the
**ASP.NET** options section in the center of the screen, double-click
**.NET Trust Levels** icon, shown circled above. Ensure that the Trust
Levels setting is **Full (internal)** and, if you had to make a
changed, click **Apply** in the right hand Actions panel.
