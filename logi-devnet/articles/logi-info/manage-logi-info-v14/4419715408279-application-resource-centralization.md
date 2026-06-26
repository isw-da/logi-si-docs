---
title: "Application Resource Centralization"
id: 4419715408279
section: "Manage - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715408279-Application-Resource-Centralization
updated_at: 2022-07-17T02:23:56Z
---

# Application Resource Centralization

# Application Resource Centralization

You will use the same procedures as best practice for both sticky and non-sticky load balancing management. However, for sticky implementation, ensure rdDataCache directory is set to default configuration (under root of application directory).

## Centralizing Files

When using sticky sessions, you want to centralize certain files:

* Saved Bookmark files
* Saved Dashboard files
* SecureKey files
* Error Log files

You have options on how you can centralize the Bookmark, Dashboard, and SecureKey files in a database. For more information, see [File To Database Mapping Element](https://devnet.logianalytics.com/hc/en-us/articles/4419707819671-File-To-Database-Mapping-Element).

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) You will also want to centralize your Error log files, but you cannot put them in a database.

## Configuring Application

In addition to centralizing the files, as shown above, modify the \_Settings file to target the file locations.

 
**"Save" File** - Many super-elements, such as the **Dashboard** and **Analysis Grid**, allow the user to save the current configuration to a file for later reuse. The locations of these files are specified in attributes of the elements.   
 
 
![](https://devnet.logianalytics.com/hc/article_attachments/7522838674967/loadbal_02_422x182.png)

As shown in the Dashboard example above, the **Save File** attribute value should be the UNC path to a shared network location (with file name, if applicable) accessible by all web servers.

 
**Bookmarks** - If used in an application, the location of these files should also be centralized:  
 
![](https://devnet.logianalytics.com/hc/article_attachments/7522807895959/loadbal_03_823x167.png)

As shown above, in the \_Settings definition, configure the **General** element's **Bookmark Folder Location** attribute, with a UNC path to a shared network folder accessible by all web servers.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png)

* In general, when you specify a network folder or file to centralize a resource, you need to change the identity that the web server uses to run the application (usually ASPNET or NETWORK SERVICE or the Application Pool), or impersonates, to a network domain account that has Full Control access permissions for the specified folder.

* You can also store your Bookmarks and Save files in a SQL database. See [Bookmarks](https://devnet.logianalytics.com/hc/en-us/articles/4419707675287-Bookmarks) for more information.

* You also have options on how you can centralize the Bookmark, Dashboard, and SecureKey files in a database for non-sticky sessions; see [File To Database Mapping Element](https://devnet.logianalytics.com/hc/en-us/articles/4419707819671-File-To-Database-Mapping-Element).

If you're using Logi SecureKey security in a load-balanced environment, you need to configure security to share requests.  
 
![](https://devnet.logianalytics.com/hc/article_attachments/7522838698647/loadbal_04_816x228.png)

In the \_Settings definition, set the **Security** element's **SecureKey Shared Folder** attribute to a network path, as shown above. Files in the SecureKey folder are automatically deleted over time, so do not
use this folder to store other files.

Keywords: clustering, cluster, clustered
