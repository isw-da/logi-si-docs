---
title: "Hello World! Tutorial"
id: 1500009530861
section: "Hello World! Tutorial"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009530861-Hello-World-Tutorial
updated_at: 2021-06-17T01:58:23Z
---

# Hello World! Tutorial

# Hello World! Tutorial

This topic is for new Logi developers. It guides you through the process of building a simple Logi application.

**Requirements**: This tutorial assumes that you have:

* Microsoft IIS web server and .NET Framework 4.x installed, - OR -
* A supported Java web server and Sun JDK 1.6 1.7, or 1.8, or JRockit, installed;
* And an un-expired trial license or a regular or OEM license file installed in   
  C:\Program Files\LogiXML IES Dev\LogiStudio.

Begin by launching **Logi Studio**, using its desktop icon or Start![](https://logianalytics.zendesk.com/hc/article_attachments/4402771511575/menuarrowrt.png)All Programs![](https://logianalytics.zendesk.com/hc/article_attachments/4402771511575/menuarrowrt.png)Logi Info![](https://logianalytics.zendesk.com/hc/article_attachments/4402771511575/menuarrowrt.png)Studio.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778621719/helloworld_01.png)

1. In Logi Studio, close the Getting Started dialog box and click **New** **Application** in the Welcome Panel, as shown above.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771759127/helloworld_02.png)

2. Logi Studio is capable of producing both .NET and Java web applications. For this tutorial, we'll select the **.NET** option, as shown above; however, comments are included in the following steps for Java applications.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778621975/helloworld_03.png)

3. Provide an application name: *HelloWorld*  - DO NOT insert a space between the two words and be sure to use the exact capitalization shown!   
     
   Choose the location for the new HelloWorld application folder. If you're using the IIS web server, for simplicity, use the default, C:\Inetpub\wwwroot, and the wizard will create the new Logi application folder there.   
     
   If you're using a Java-based web server, browse to its standard web application location. For example, for a default
   installation of Tomcat 7 this would be: C:\Program Files\Apache Software Foundation\Tomcat 7.0\webapps.  
   Port *8080* will be used by default in the application's URL.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778622231/helloworld_03a.png)

For a JBOSS server, and other Java servers that use auto-deploy, append a ".war" extension to the application folder name, as shown above.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778622615/helloworld_04.png)

Click **OK** to create the application. The progress indicator, shown above, will appear and required sub-folders and files will be created in your HelloWorld folder. Java web servers may complain as the wizard adds files to the folders; this is normal behavior.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778622871/helloworld_05.png)

4. The **Prepare a New Application Wizard**, shown above, will start. The next step is to configure the basic application settings and register it with your web server. Click **Next**.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778623255/helloworld_07.png)

5. The wizard will now run the web server diagnostics and configure your application, described in the dialog box shown above. Click **Next**.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778623511/helloworld_06.png)

The results of the diagnostic tests will displayed, as shown above. If all test results are "OK", click **Next.**

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif)  The failure of any test indicates that something is wrong with your web server environment's ability to run the new application. This could be caused by a number of things, such as failing to install the new Logi version as an Administrator, or having incorrect file permissions on the application folder, or failing to have the correct version of .NET installed. Contact Logi Support for assistance.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771761303/helloworld_08.png)

6. Next, you'll be asked to select a **Theme** for your application. Use the default, *Signal,* and click **Next**.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771761687/helloworld_09.png)

7. Next, enter a caption for the application, and click **Next**.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771762071/helloworld_10a.png)

8. When the wizard prompts you to create a Data Visualization, click **Cancel**.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771762327/helloworld_11.png)

9. In Studio's **Application Panel** (at the upper-left), find and double-click the **Default** report definition. It will open in the center of the screen, in the Workspace Panel.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778624279/helloworld_12.png)

10. In the Default definition, *right-click* the **Body** element and navigate the pop-up menus as shown above, finally clicking on the Label menu item. A **Label** element will be added to the definition.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771762583/helloworld_13.png)

11. Click the **Label** element and, in the **Attributes Panel**, enter the text "Hello World!" in the **Caption** attribute, as shown above. Then, in the Class attribute, select *ThemeTextLargest* from its pull-down list of style class options.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771762967/helloworld_14.png)

12. Finally, click the **Preview** tab at the bottom of the Workspace Panel to save your definition and run the Default report. Your "Hello World" message should be displayed, as shown above.

Congratulations on completing your first Logi report!
