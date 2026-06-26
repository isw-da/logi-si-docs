---
title: "Deploying Logi Applications"
id: 4406818007319
section: "Use Logi Studio/SSRM - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406818007319-Deploying-Logi-Applications
updated_at: 2022-04-06T06:09:37Z
---

# Deploying Logi Applications

# Deploying Logi Applications

After you've developed your Logi application on your development machine, it's time to deploy it to your production server. There are several ways to this, and they're all discussed in [Deploy a Logi Application](https://devnet.logianalytics.com/hc/en-us/articles/4406817366039-Deploy-a-Logi-Application).

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) If your application uses Discovery 3.0+ and you wish to preserve the Dataviews, visualizations, and other objects created during development, or if you're moving your application to another server and want to preserve the same objects, you'll also need to migratethe Platform Database. For more information, see [Deploy a Logi Application](https://devnet.logianalytics.com/hc/en-us/articles/4406817366039-Deploy-a-Logi-Application).

The easiest of these methods is to use Studio's **Application Deployment** tool. Before you use it, however, ensure that:

1. Logi Server is installed on your production server. On a development machine you generally install both **Logi Studio** and **Logi Server** and you may wish to install them both on a production server, but it's not required and most developers only install Logi Server there.
2. The .NET framework, or Oracle JDK orOpenJDK 8, 11, or 12, 13, or 14 has been installed on the production server.   
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) Oracle has changed its Java usage policies - see [Java Usage Policy](https://devnet.logianalytics.com/hc/en-us/articles/4406817692055-Java-Usage-Policy) for important information.
3. You have an appropriate **Logi license** for the production server.
4. You have the appropriate **security credentials** for writing to the production server.
5. The production server has connectivity to the database server or other datasources needed by your application, and you know the security credentials they require.
6. You know any **storage conventions** for folder locations on the production
   server that you need to observe (such as, "all applications must be installed on
   the D: drive, not the C: drive")?

Studio's Application Deployment tool is capable of *copying* all or part of your application to the production server, using either file system copy commands to local or shared network drives, or one of three flavors of **FTP** (standard, SSL, or SSH). In Studio, the details of each operation are called a "deployment target" and they can be saved for later reuse.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563018903/usingstudio_39.png)

The Application Deployment tool is started in Studio by selecting it from the Main Menu **Tools** tab, as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563019287/usingstudio_40.png)

If no deployments have been defined, the dialog box shown above appears. Click the link or **New...** to define your first deployment target.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583667607/usingstudio_41.png)

The Add/Edit Deployment Target dialog box contains the following:

1. **Caption**: Enter an arbitrary name for the deployment, for easy future reference.
2. **Transfer Method**: Select copy to Local or Network drive, FTP, FTP (SSL), or FTP (SSH).
3. **Path**: If Local/Network was selected in #2, enter the UNC file path to the destination app folder on the production server. For example:  
     
   \\myWebServer\myLogiApp  
     
   If an FTP variant was selected in #2, enter the FTP protocol **URL** to the destination app folder and arguments. Examples:  
     
   For FTP & FTP SSL: ftp://myWebServer/myLogiApp, ftp://myWebServer.com:8082/projects/myLogiApp  
     
   For FTP SSH: sftp://test.myServer.local//opt/tomcat/webapps/myLogiApp  
   Note use of *two* forward slashes after server name. Also you'll have to create the target application folder and grant permissions, as described in [Logi Java Application Folder Permissions](https://devnet.logianalytics.com/hc/en-us/articles/4406818009751-Logi-Java-Application-Folder-Permissions), because the application is not being deployed to a user's home directory.  
     
   If necessary, you'll be prompted to supply a user ID and a password when the tool run; do not include them in the URL.
4. **Test**: This button can be used to ensure connectivity to the destination.
5. **File Types**: Select the file types that are to be deployed. *Files are overwritten at the destination without warning!*
6. **Server Type**: If "Server Engine" was selected in #5, these options are shown. Select the appropriate server type.
7. **Available****Versions**: If "Server Engine" was selected in #5, available server engine versions are shown. Select the appropriate version.

If the destination requires a user ID and password in order to access it, when you click the **Test** button, you'll be prompted for login credentials. If the credentials are successfully authenticated, the user ID will automatically be saved with the deployment target details and, optionally, the password as well.

Once a deployment target has been defined, it appears in a list...

![](https://devnet.logianalytics.com/hc/article_attachments/4417583667735/usingstudio_42.png)

...as shown above, where it can be managed and edited. To run a deployment, check its check box and click the **Deploy** button. If multiple deployments are selected, they'll run consecutively.

The connection with the destination server will be established and then the files will be deployed to it.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583667991/usingstudio_43.png)

The Deployment dialog box will expand to display the results of the process, as shown above. The running log indicates which files are added, replaced, or skipped. Deployment process logs are created in the rdDeployment folder beneath each Logi application folder as text files and are accessible through the **View Logs** link.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583668247/usingstudio_44.png)

Finally, the deployment will complete and a direct link to its log file will be displayed.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) It's very important that you understand that copying the files, using the Deployment tool, *does not register the application* with a web server on the target machine. So, after a first-time deployment is run, you must complete this registration on the target machine using Logi Studio, Server Manager (for .NET applications only), or the web server's management tools.
