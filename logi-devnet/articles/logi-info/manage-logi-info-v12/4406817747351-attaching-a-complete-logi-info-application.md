---
title: "Attaching a Complete Logi Info Application"
id: 4406817747351
section: "Manage - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817747351-Attaching-a-Complete-Logi-Info-Application
updated_at: 2022-04-06T06:07:57Z
---

# Attaching a Complete Logi Info Application

# Attaching a Complete Logi Info Application

Your Support Engineer may ask you to attach your entire Logi Info application to your case. The application's files can be compressed and attached using the same techniques described earlier. Here's how to prepare your application before doing so:

The Sample Applications on DevNet include sample data in XML files, so connection details aren't necessary to run them. Assuming the connection is not part of the problem you need help with, you can do the same thing with your application's data using this technique:

1. Run the application and open its debugger report page.  
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417563142551/worksupport_09.png)  
   Find and click the link associated with the data returned from the source, before any other processing occurs, as shown above.
2. When the Data View page is displayed, click the *View raw XML* data link. The formatted XML data will appear in a new page.
3. *Right-click* anywhere in the XML data and select *View source* or *View page source* (varies by browser). The unformatted XML data will appear in a new page.
4. *Right-click* anywhere in the XML data and select *Save As...* to save the raw XML data in your application's \_SupportFiles folder, with an .xml extension.
5. Repeat to create XML data files for all of the data required.

If your application depends on a "parent" application, "untether" it by modifying your application so that it can run stand-alone.

If your application implements security, be sure to provide a set of login credentials to us. If there are any critical session variables required, tell us about them, too.

Make a "groomed" copy of your application folder by including only the minimum files necessary. Do not include files like *newReport.lgx,* obsolete definitions, unused images and style sheets, etc. Remove the application's *bin*, *rdTemplate*, *rdDownload*, or *rdDataCache* folders.

Compress the groomed application folder and it's ready to be attached to the case.
