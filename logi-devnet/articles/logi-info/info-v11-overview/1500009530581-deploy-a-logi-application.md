---
title: "Deploy a Logi Application"
id: 1500009530581
section: "Info v11 Overview"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009530581-Deploy-a-Logi-Application
updated_at: 2023-01-02T13:54:11Z
---

# Deploy a Logi Application

# Deploy a Logi Application

You've developed and tested your Logi application and it's **working perfectly** running on the "localhost" server in your development computer. Now you're ready to deploy it onto your production server; this topic helps you get the details right.

* Production Server Checklist
* [Using Studio's Application Deployment Tool](#AppDepTool)
* [Alternate Method: Manually Copying Your Logi Application](#Copying)
* [Post-Deployment Server Configuration](#PostDeploy)

## Production Server Checklist

Before deploying your Logi application, review the following to ensure that your production server is ready to accept it:

* Do you have the necessary **administrative privileges** to work on the production server? Some of the following tasks may require it.
* Is the **web server** installed and tested? If not, install and test it.
* On a development machine you generally install both **Logi Studio** and **Logi Server**. You may also install both of them on a production server but it's not required. Just install Logi Server, which will make our **Server Manager** tool available on the production server as well.
* Is the appropriate **.NET Framework** for Windows (for Logi apps prior to v11.0.127: .NET 2.0 or 3.x; for v11.0.127 or later: .NET 4.x) or the official Sun JDK 1.6, 1.7, or 1.8 or **JRockit** installed on the production server?
* Does the production server have connectivity with your **production database****server** or other datasources?
* Do you know the appropriate **credentials** for accessing the production datasources? These may have to be changed in your \_Settings definition.
* Are there any **conventions** for file or folder locations on the production server that you need to observe (such as, "all applications must be installed on the D: drive, not the C: drive")?
* Are you allowed to **remotely access** the production server using remote desktop, Citrix, Terminal Services, or some other method? (This can be extremely useful when you need to run the web server's management tool or other tools.)
* If deploying with Studio's Deployment tool over a network, by copying or via a form of FTP, do you have the necessary **security****credentials** to access the destination?
* If deploying by manually copying files, can you map a **network drive** that's been "shared" on the production server?

Once these items have been reviewed and addressed as necessary, you're ready to proceed with deploying your Logi application.

## Using Studio's Application Deployment Tool

Logi Studio's **Application Deployment****Tool** is easy to use and allows you to set up reusable deployment operations. The tool provides a great deal of flexibility, allowing you to develop, for example, on a 32-bit platform and deploy to a 64-bit platform, or to develop on a Windows platform and deploy to a Java platform.

The Deployment tool is capable of copying all or part of your application to the production server, using either file system commands (to local or shared network folders) or one of three flavors of **FTP** (standard, SSL, or SSH). In Studio, the details of each operation are called a "deployment
target" and
they can be saved for later reuse.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771826071/deployapp_01.png)

The Application Deployment tool is opened in Studio by clicking its menu item, in the main menu's **Tools** tab, shown above.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771827863/deployapp_02.png)

If no deployments have been defined, the dialog box shown above appears. Click the link or **New...** to define your first deployment target.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778669847/deployapp_03.png)

The Add/Edit Deployment Target dialog box contains the following:

1. An arbitrary **name** you give the deployment, for future reference.  *Note:* This is also used as the Deployment Log File name, so it has to adhere to the OS *file naming standards*. For example, in Windows, these characters are invalid in a file name: \* | / \ : " < > ? and should not be used here.
2. The **transfer method**: Copy to Local or Network drive, FTP, FTP (SSL), or FTP (SSH).
3. If the "Local/Network" transfer method is selected, enter a UNC **file path** to a destination app folder on the production server. For example:  
     
   \\myWebServer\myLogiApp  
     
   If the destination app folder is not on the local machine, it must be *shared* on the network.  
     
   If one of the FTP transfer methods is selected, enter an FTP protocol **URL** to the destination app folder and arguments. Examples of these include:  
     
   FTP & FTP SSL: ftp://myWebServer/myLogiApp, ftp://myWebServer.com:8082/projects/myLogiApp  
   FTP SSH: sftp://myApp@myServer.com/myLogiApp  
      
   If necessary, you'll be prompted to supply a user ID and a password; do not include them in the URL.
4. The **Test** button can be used to ensure connectivity to destination.
5. Check which types of **files** are to be deployed. *Files are overwritten at destination without warning!*
6. If "Server Engine" has been selected above, the **server type** options for the deployment are shown (scroll down to see additional types, such as Java). Select the server type.
7. If "Server Engine" has been selected, the **available****versions** installed on the development machine are listed. An effective way to perform an application upgrade, when a new release of your Logi product comes out, is to select only the Server Engine.

If the destination requires a user ID and password in order to access it, when you click the **Test**
button, you'll be prompted for login credentials. If the credentials
are successfully authenticated, the user ID will automatically be saved
with the deployment target details and, optionally, the password as
well.

Once a deployment target has been defined, it appears in a list:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771828119/deployapp_04.png)

Once a deployment target has been defined, it appears in a list, as shown above, where they can be managed and edited. To run a deployment, check its checkbox and click the **Deploy** button. If multiple deployments are selected, they'll run consecutively.

The connection with the destination server will be established and then the files will be deployed to it.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778670103/deployapp_05.png)

The Deployment dialog box will expand to display the results of the process, as shown above. Text log files, stored in the rdDeployment folder beneath each Logi application folder, are accessible through the **View Logs** link, and document each deployment.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778670359/deployapp_06.png)

Finally, the deployment will be complete, and the link to the log file will be displayed.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif)  It's very important that you understand that copying the files, using the Deployment Tool, *does not register the application* with a web server on the target machine. So, after the first deployment, this has to be done by the developer using Studio, Server Manager, or the web server's tools.

### Controlling Which Files Are Deployed

The Add/Edit Target dialog box allows you to select the files to be deployed by category:

|  |  |
| --- | --- |
| **Category** | **Description** |
| Application Definition and Support | Copies all files in all folders with names beginning with an underscore, such as \_Definition, \_Script, \_Support Files, etc. This includes folders like \_Images and \_Stylesheets, which are from the old app folder scheme. Identical files will be skipped. |
| Application Settings | Copies \_Settings.lgx only. Identical files will be skipped. |
| Server Engine (.NET app) | Copies the rdTemplate and bin folders - identical files will be skipped. Also copies any .aspx, .asax, and .config files if they do not already exist; does not overwrite them if they do exist. |
| Server Engine (Java app) | Copies rdTemplate, Assemblies, and WEB-INF folders - identical files will be skipped. Also copies any .aspx, .asax, and .config files if they do not already exist; does not overwrite them if they do exist. |

Why not deploy *all* of the categories *all* of the time? You'll want to do so for your first deployment but, generally, you won't want to for subsequent deployments in order to avoid overwriting files that may have been **customized** for the production server, such as \_Settings.lgx. And, unless you're changing engine versions, deploying the engine files with every deployment is unnecessary and a waste of time. So the tool offers you the opportunity to tailor your deployments as needed.

The Deployment tool will *not* copy *every* file in your application folder:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778670615/deployapp_07.png)

The image above illustrates which folders and files are copied. Files are compared during the process and identical files will be skipped. Of special note is the fact that **custom folders** you may add to the application, for example to hold Dashboard Save files, *are not copied* and you will need to create these during your first deployment manually. Other files you may create in the application folder that are not stored in folders will *not* be copied, as well.

However, developers may want to *exclude* specific application definition and support files from a deployment, and Studio provides an easy way to do that:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778670871/deployapp_08.png)

By default, all files in Studio's Application Panel are included in deployments. However, if you wish to *exclude* a file, select it in the Application Panel, right-click it, and click the **Include in Deployments** item in the popup menu, as shown above.

You can also exclude an entire *folder* in the Application Panel in the same way. Suppose you want to deploy just 1 or 2 report definitions. This can be done by first selecting the **\_Reports folder**, right-clicking it and clicking the checked Include in Deployments item, which unselects *all* report definitions. Then select and right-click the 1 or 2 report definitions you want to deploy, and click their Include... items to include them in the deployment. Then run the Deployment
Wizard.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778671127/deployapp_09.png)

If files have been excluded, the **View Excluded Files** link, shown above, will be displayed to alert you to this situation when you add or edit a deployment target in the Deployment tool. Clicking the link will display a list of the excluded files.

### License Files

License files are *never included* in deployments, so you will have to manually deploy your license file the first time you deploy your application, or configure it to use a centralized license file. For more information about license files, see [Product Licensing](https://devnet.logianalytics.com/hc/en-us/articles/1500009531601-Product-Licensing).

### After a First-Time Deployment

After an application is deployed for the first time, you must make some configuration changes to ensure it will run. See the **Post-Deployment** section below for details.

For subsequent deployments, you need only run the Deployment tool to update the files on the target server.

[![](https://logianalytics.zendesk.com/hc/article_attachments/4402778391063/totop.gif)](#)  [Back to the top](#)

## Alternate Method: Manually Copying Your Logi Application

If you don't have a version of Studio that includes the Application Deployment Tool, you can use another deployment approach that works well if you can map a shared network drive on the server: just **copy** your entire Logi **application folder** to the production server.

From an operational perspective, for .NET applications, it doesn't really matter where you put the folder on the server but other company-specific considerations (storage location conventions, security, space limits, etc.) may apply. For Java applications, depending on your specific web server, you may be required to place your app folder in a specific folder (for example, beneath the webapps folder for Apache/Tomcat).

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771828375/deployapp_10.png)

Just be sure that your copy operation gets *all* of the files and folders inside your application folder to the production server.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif) Caution: If you develop your application on a **32-bit** machine and copy it to a **64-bit** production machine, *do not* copy the entire application folder, as some Logi Server Engine files in your app will be 32-bit-specific. Instead, either use the Deployment Tool and ensure that you deploy 64-bit engine files, or install Studio on your production server, use the New Application Wizard to create
an empty 64-bit application, then copy only your definition and support files over from your development machine.

If you're distributing your application to a remote site, you can use a compression utility like **WinZip** to package your entire Logi application project folder into a single .ZIP file.

Note that this approach copies *all* of the Logi Server Engine files as well as the application files, so the version of the production application will be the same as that of the development application. This approach will also copy any v10 or 11 **license file** in the application root folder to the production server, where it may not be viable.

Naturally, if you don't have a network connection to the production server, you can also use other methods, such as burning the entire application folder to a DVD or copying it to a USB "thumb drive" in order to move it to the production server.

## Post-Deployment Server Configuration

Once you have physically deployed your application to the production server for the first time, you need to configure it to run in the new environment.

##### When Using Windows IIS Web Server

1. Provide a **license file** for the application, unless you're using a centralized v11 license file.
2. **Register** the application with IIS. You can do this using Studio (if you've installed it on the production server), Server Manager, or the IIS Manager tool.

3. Ensure that the datasource connection strings or parameters, constants, and other server-specific attributes are correct in your application's \_Settings definition. This can be done using **Notepad** if Studio is not installed.
4. If your application writes any output to the **file system**, ensure that the account the application runs under is granted **Write permissions** to the relevant folders. These accounts are the local ASP.NET (IIS 5.x) or NETWORK SERVICE (IIS 6.0) accounts.

### When Using a Java Server

1. Provide a **license file** for the application, unless you're using a centralized v11 license file.
2. Provide any additional configurations required for your server. See [Java Server Configurations](https://devnet.logianalytics.com/hc/en-us/articles/1500009515622-Java-Server-Configurations) for specific information.

3. Ensure that the datasource connection strings or parameters, constants, and other server-specific attributes are correct in your application's \_Settings definition. This can be done using any text editor.
4. If your application writes any output to the **file system**, ensure that the identity the application runs under has appropriate file access permissions for the relevant directories.

Subsequent deployments for the purpose of updating report definitions, images, XML data, etc. should not require you to do any of the steps discussed above, unless you're changing folder locations or \_Settings attributes. This means Logi Server Engine files and \_Settings.lgx can be left out of future deployments undertaken for simple update purposes.
