---
title: "Deploying a Logi Services Database"
id: 4406822284951
section: "Introduction to Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822284951-Deploying-a-Logi-Services-Database
updated_at: 2022-04-06T06:05:40Z
---

# Deploying a Logi Services Database

# Deploying a Logi Services Database

If your application uses **Logi Services** technology (i.e. includes the Discovery 3.0+ add-on module), you'll need to deploy a copy of the Platform Database (PDB) to your production server. The PDB contains a variety of objects, including security information, Dataviews, settings, licenses, and more.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) These deployment instructions *copy* the development PDB; they do not make *incremental updates* to the production PDB. Use caution if you're considering repeating these instructions at a later date; you want to avoid overwriting new records in the production PDB with "old" data from the development PDB.

Use these following steps to deploy the PDB. They assume a default installation location on both servers.

1. Stop the Logi Application Service and Logi Data Service services on both servers.
2. On the production server, create a backup folder and *move* the following folder (with all files and sub-folders) and files into it:  
     
   C:\LogiAnalytics\Discovery\platform\ldap  
     
   C:\LogiAnalytics\Discovery\platform\db\LogiDB.mv.db  
   C:\LogiAnalytics\Discovery\platform\bin\logiconfig.bat  
   C:\LogiAnalytics\Discovery\platform\settings\logiDataService.json
3. Copy the C:\LogiAnalytics\Discovery\platform\ldap folder (with all files and sub-folders) from the development server to the same location on the production server.
4. Copy these files from the development server to the same location on the production server:  
     
   C:\LogiAnalytics\Discovery\platform\db\LogiDB.mv.db  
   C:\LogiAnalytics\Discovery\platform\bin\logiconfig.bat  
   C:\LogiAnalytics\Discovery\platform\settings\logiDataService.json
5. Ensure that the copied folder and files have the same file access permissions as neighboring folders and files (or are unblocked) on the production server.
6. Restart the Logi Application Service and Logi Data Service services on both servers.
7. On the production server, test to see that the Admin user can access Dataviews stored in the PDB.
8. Delete the folder and files in the backup folder from Step 2 once you're sure the application is working correctly.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) The PDB contains the product license, which is machine-specific. Once you copy it to another machine, you will need to replace the license in the PDB (assigned to the development server) with one assigned to the product server. See [Product Licensing](https://devnet.logianalytics.com/hc/en-us/articles/4406817805207-Product-Licensing) for details.

There is a method of migrating the PDB to a production server *without* the security information. Alternate security information can then be inserted from an Excel spreadsheet. This is done using a script which is described in the platform documentation, in a topic entitled *Migrating the Platform Database*. To access this documentation from Logi Studio, run the Dataview Authoring tool, log into it, and click the Help icon in the upper right-hand corner near your user name.
