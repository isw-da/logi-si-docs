---
title: "Hello World! Tutorial"
id: 4419700069271
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419700069271-Hello-World-Tutorial
updated_at: 2023-07-27T06:35:22Z
---

# Hello World! Tutorial

# Hello World! Tutorial

This topic is for new Logi developers. It guides you through the
process of building a simple Logi Info application.

## Requirements

This tutorial assumes that you have:

* Microsoft IIS web server and .NET Framework 4.x installed, - OR -
* A supported Java web server and the Oracle JDK or OpenJDK 8, 11,
  12, 13, or 14  
  ![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png)
  Oracle has changed its Java usage policies - see
  [Java Usage Policy](https://devnet.logianalytics.com/hc/en-us/articles/4419723053335-Java-Usage-Policy)
  for important information.
* And an un-expired trial license, or a regular or OEM license file,
  installed in the   
  *<Logi Info installation folder>*\LogiStudio folder,
  which defaults to:  
  C:\Program Files\LogiXML IES Dev\LogiStudio.

## Tutorial

Begin by launching **Logi Studio**, using its desktop icon or Start![](https://devnet.logianalytics.com/hc/article_attachments/7522803222807/menuarrowrt.png)All Programs![](https://devnet.logianalytics.com/hc/article_attachments/7522803222807/menuarrowrt.png)Logi Info![](https://devnet.logianalytics.com/hc/article_attachments/7522803222807/menuarrowrt.png)Studio.

![](https://devnet.logianalytics.com/hc/article_attachments/7522865916183/helloworld_01.png)

1. In Logi Studio, close the Getting Started dialog box and click
   **New** **Application** in the Welcome Panel, as shown
   above.

![](https://devnet.logianalytics.com/hc/article_attachments/7522870926487/helloworld_02.png)

2. Logi Studio is capable of producing both .NET and Java web applications.
   For this tutorial, we'll select the **.NET** option, as shown above;
   however, comments are included in the following steps for Java
   applications.

![](https://devnet.logianalytics.com/hc/article_attachments/7522865931671/helloworld_03.png)

3. Provide an application name: *HelloWorld*  - DO NOT insert a space
   between the two words and be sure to use the exact capitalization shown!
     
     
    Choose the location for the new HelloWorld application folder. If you're
   using the IIS web server, for simplicity, use the default,
   C:\Inetpub\wwwroot,
   and the wizard will create the new Logi application folder there.   
     
    If you're using a Java-based web server, browse to its standard web
   application location. For example, for a default installation of Tomcat
   7 this would be:
   C:\Program Files\Apache Software Foundation\Tomcat
   7.0\webapps.  
    Port *8080* will be used by default in the application's URL.

![](https://devnet.logianalytics.com/hc/article_attachments/7522835437975/helloworld_03a.png)
For a JBOSS server, and other Java servers that use auto-deploy, append
a ".war" extension to the application folder name, as shown
above.  
  

![](https://devnet.logianalytics.com/hc/article_attachments/7522835445783/helloworld_04.png)

Click **OK** to create the application. The progress
indicator, shown above, will appear and required sub-folders and files
will be created in your HelloWorld folder. Java web servers may complain
as the wizard adds files to the folders; this is normal behavior.

![](https://devnet.logianalytics.com/hc/article_attachments/7522857870743/helloworld_05.png)

4. The **Prepare a New Application Wizard**, shown above, will start.
   The next step is to configure the basic application settings and
   register it with your web server. Click **Next**.

![](https://devnet.logianalytics.com/hc/article_attachments/7522870970007/helloworld_07.png)  

5. The wizard will now run the web server diagnostics and configure your
   application, described in the dialog box shown above. Click
   **Next**.

![](https://devnet.logianalytics.com/hc/article_attachments/7522865968663/helloworld_06.png)
  
The results of the diagnostic tests will displayed, as shown above. If
all test results are "OK", click **Next.**  
![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png)
The failure of any test indicates that something is wrong with
your web server environment's ability to run the new application. This
could be caused by a number of things, such as failing to install the
new Logi version as an Administrator, or having incorrect file
permissions on the application folder, or failing to have the correct
version of .NET installed. Contact Logi Support for assistance.

![](https://devnet.logianalytics.com/hc/article_attachments/7522865975063/helloworld_08.png)

6. Next, you'll be asked to select a **Theme** for your application. Use
   the default, *Signal,* and click **Next**.

  
![](https://devnet.logianalytics.com/hc/article_attachments/7522857930775/helloworld_09.png)

7. Next, enter a caption for the application, and click **Next**.

![](https://devnet.logianalytics.com/hc/article_attachments/7522882735127/helloworld_10a.png)  

8. When the wizard prompts you to create a Data Visualization, click
   **Cancel**.

  
![](https://devnet.logianalytics.com/hc/article_attachments/7522857939479/helloworld_11.png)  

9. In Studio's **Application Panel** (at the upper-left), find and
   double-click the **Default** report definition. It will open in the
   center of the screen, in the Workspace Panel.

  
![](https://devnet.logianalytics.com/hc/article_attachments/7522866016279/helloworld_12.png)

10. In the Default definition, *right-click* the **Body** element
    and navigate the pop-up menus as shown above, finally clicking on the
    Label menu item. A **Label** element will be added to the
    definition.

  
![](https://devnet.logianalytics.com/hc/article_attachments/7522871042455/helloworld_13.png)

11. Click the **Label** element and, in the **Attributes Panel**,
    enter the text "Hello World!" in the **Caption** attribute,
    as shown above. Then, in the Class attribute, select
    *ThemeTextLargest* from its pull-down list of style class
    options.

  
  
![](https://devnet.logianalytics.com/hc/article_attachments/7522835603479/helloworld_14.png)

12. Finally, click the **Preview** tab at the bottom of the Workspace
    Panel to save your definition and run the Default report. Your
    "Hello World" message should be displayed, as shown above.

Congratulations on completing your first Logi report!

## Possible Errors

Did you receive an error when you tried to preview the report? Here's how
to proceed:
*Error: Please*  *specify a URL in "\_Settings/Path.AppPath"*  
It appears the wizard failed to fill-in the proper value for the
Application Path. Open the \_Settings definition, and select the
**Path** element. Fill-in the value for the
**Application Path** attribute with:

http://localhost/HelloWorld(.NET)  
 http://localhost:8080/HelloWorld(Java)

Save the definition and try previewing again.
