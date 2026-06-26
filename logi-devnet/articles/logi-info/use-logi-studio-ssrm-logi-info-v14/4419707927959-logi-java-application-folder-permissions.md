---
title: "Logi Java Application Folder Permissions"
id: 4419707927959
section: "Use Logi Studio/SSRM - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707927959-Logi-Java-Application-Folder-Permissions
updated_at: 2022-07-17T02:23:05Z
---

# Logi Java Application Folder Permissions

# Logi Java Application Folder Permissions

After deployment of a Logi Java application, you can elect to grant 775 (full access) permissions manually on the application root folder and all of its child folders and files. If you prefer a more selective approach, typical Logi application folders require these permissions:

| Folder | Permission |
| --- | --- |
| Logi app root | 440 |
| assemblies |  |
| rdDataCache | 660 |
| rdDownload | 660 |
| rdTemplate | 660 |
| WEB-INF |  |
| lib |  |
| PhantomJS (binary) | 550 |
| \_Definitions |  |
| \_SupportFiles |  |
| goBookmarks (InfoGo app only) | 660 |
| (your custom folders) | 660 |

## Controlling Which Files Are Deployed

The Add/Edit Target dialog box allows you to select the files to be deployed by category:

| Category | Description |
| --- | --- |
| Application Definition and Support | Copies all files in all folders with names beginning with an underscore, such as \_Definition, \_Script, \_Support Files, etc. This includes folders like \_Images and \_Stylesheets, which are from a legacy folder scheme. Identical files will be skipped. |
| Application Settings | Copies \_Settings.lgx only. Identical files will be skipped. |
| Server Engine (.NET app) | Copies the rdTemplate and bin folders - files are overwritten without warning. Also copies any .aspx, .asax, and .config files if they do not already exist; does not overwrite them if they do exist. |
| Server Engine (Java app) | Copies rdTemplate, Assemblies, and WEB-INF folders - files are overwritten without warning. Also copies any .aspx, .asax, and .config files if they do not already exist; does not overwrite them if they do exist. |

Why not just deploy *all* of the categories *all* of the time? You'll want to do so for your first deployment but, generally, you won't want to for subsequent deployments in order to avoid overwriting files that may have been *customized* for the production server, such as \_Settings.lgx. And, unless you're changing engine versions, deploying the engine files with every deployment is unnecessary and a waste of time. So the tool offers you the opportunity to tailor your deployments as needed.

However, developers may wantto *exclude* specific application definition and support files from a deployment, and Studio provides an easy way to do that:

![](https://devnet.logianalytics.com/hc/article_attachments/7522749154583/usingstudio_45.png)

By default, all files in Studio's Application panel are included in deployments. However, if you wish to *exclude* a file, select it in the Application panel, right-click it, and uncheck the **Include in Deployments** item in the popup menu, as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/7522779988887/usingstudio_46.png)

If files *have* been excluded in this manner, in the bottom section of the Add/Edit Deployment Target dialog box, a **View Excluded Files** link will be displayed, as shown above. Clicking the link will display a list of the excluded files.

## License Files

License files are *never included* in deployments, so you will have to manually deploy your license file the first time you deploy your application, or configure it to use a centralized license file. For more information about license files, see [Product Licensing](https://devnet.logianalytics.com/hc/en-us/articles/4419707792663-Product-Licensing).

## After a First-Time Deployment

After the first time an application is deployed, you must:

* Provide a license file for the application, unless you're using a centralized license file.
* Register the application with the web server.
* Ensure that the datasource connection strings or parameters, constants, and other server-specific settings are correct in the \_Settings definition.
* For a Java app, complete any special configurations required by your web server.

For subsequent deployments, you need only run the Deployment tool to update the files on the target server.

For more information, see [Deploy a Logi Application](https://devnet.logianalytics.com/hc/en-us/articles/4419707523735-Deploy-a-Logi-Application).
