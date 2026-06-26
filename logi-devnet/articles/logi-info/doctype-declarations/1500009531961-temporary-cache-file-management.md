---
title: "Temporary Cache File Management"
id: 1500009531961
section: "Doctype Declarations"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009531961-Temporary-Cache-File-Management
updated_at: 2021-12-21T18:02:10Z
---

# Temporary Cache File Management

# Temporary Cache File Management

A Logi application consists of a file system folder that contains a number of standard sub-folders and files. Many of these sub-folders have specific purposes; two of the most interesting standard sub-folders are **rdDataCache** and **rdDownload**. These folders hold temporary files for caching data and other purposes; they are managed automatically and are discussed here.

* About Temporary Cache Files
* [The rdDataCache Folder](#The_rdDataCache_Folder)
* [The rdDownload Folder](#rdDownload_Folder)
* [Temporary File Clean Up](#Temporary_File_Clean_Up_)

## About Temporary Cache Files

As you may know, physically a Logi application consists of a single folder that contains a number of standard sub-folders and files. Many of these sub-folders have specific purposes. For example, .css files placed in the \_SupportFiles folder will appear in Logi Studio automatically and will be included in selection lists for assigning style sheets. Two of the most interesting standard sub-folders are rdDataCache and rdDownload; they have a little-known mechanism associated with them that makes development and server storage maintenance much easier.

![](https://devnet.logianalytics.com/hc/article_attachments/4402771606551/tempcache_01.png)

For example, when data is returned from a datasource, the Logi data engine may cache it in server memory or in temporary XML files or both. When Animated Charts are used, temporary code fragment files are generated. These and other temporary files are created by the system in the **rdDataCache** folder.

The **rdDownload** folder is the home of a number of other temporary files. For example, when debugging links are turned on and trace pages are created, the XML debug files are placed in it. Uploaded files, oddly enough, temporarily reside here, too, before being relocated, and exports also use this folder.

Of course, developers who need to store data in temporary files are free to use these folders, too (traditionally, rdDownload). And it's a very good idea to do so. The server account under which Logi applications run typically has been granted Write permissions to these folders, so files can be written there.

## The rdDataCache Folder

When data is returned from a data source, the Logi Server Engine may cache it in server memory or in temporary XML files or in both. When certain charts are used, temporary code fragment files are generated. These and other temporary files are created by the system in the rdDataCache folder.

![](../../Logi%20Info%20v12.7/Content/Resources/sharedImages/greencheck.gif)  When data is cached in this folder it makes easier to "page" through the data and to retrieve it quickly. However, if a new data query is executed, then the data cached here is replaced. The two exceptions to this are when **DataLayer.Cached** is used and when a super-element such as the **Analysis Grid**, which is designed to work with cached data, are used. Both of these exceptions have specific mechanisms for refreshing their data.

The default name and location of the rdDataCache folder works very well for most implementations but they can be changed in [*The \_Settings Definition*](https://devnet.logianalytics.com/rdPage.aspx?rdReport=Article&dnDocID=2031#General). This might be helpful when very large data sets and large numbers of user raise concerns about temporary files consuming all of the free disk space, or in clustered server environments where sharing is required. These are unusual situations, however, and the default is appropriate for most use-cases.

(missing or bad snippet)

## The rdDownload Folder

The rdDownload folder is the home of a number of other temporary files. For example, when debugging links are turned on and trace pages are created, the XML debug files are stored here. *Uploaded* files, oddly enough, temporarily reside here, too, before being relocated, and exports also use this folder for temporary files.

There is no way to rename or relocate this folder.

Developers who need to store data in temporary files are free to use these folders, too (traditionally, rdDownload). And it's a very good idea to do so. The server account under which Logi applications run typically has been granted Write permissions to these folders, so files can be written there.

### Securing rdDownload

When reports or data are exported from Report definitions, the rdDownload folder temporarily contains exported PDF, Excel, etc. files in order to make them available for download by the user who created them. By default, these files have names based on GUIDs, so directly accessing them without permission by guessing their names *is* possible but unlikely. However, if you'd like to further secure these files, you can engage two special features.

* The first feature requires that the Session ID of the user requesting an export file download match that of the user who created the export file, otherwise an HTTP 403 error is returned.

* The second feature ensures that supporting files used in the process of creating an export, and saved in rdDownload, are deleted once the export file is created but before it's streamed back to the requesting user.

To enable these features, you must manually alter the Logi application's web.config file, in the application's root folder. The file already contains the code required and all you have to do is uncomment it to enable it. Here's the code:

<!-- Uncomment the following rdDownloadSecPageHandler verb in the httpHandlers section to enable the automatic deletion of export files in the rdDownload directory. This also enables additional security for these files.  -->  
<system.web>  
<!--  
    <httpHandlers>  
            <add verb="\*" path="rdDownload/\*" type="rdServer.rdDownloadSecPageHandler,rdServer"/>        
    </httpHandlers>  
-->   
</system.web>  
<!--  Uncomment the  rdDownloadSecPageHandler in the system.webServer section to enable rdDownload directory Security   -->  
<system.webServer>  
<!--  
      <validation validateIntegratedModeConfiguration="false"/>  
          <handlers>  
             <add  verb="\*" path="rdDownload/\*" name="rdDownloadSecPageHandler" type="rdServer.rdDownloadSecPageHandler,rdServer" resourceType="Unspecified"/>  
        </handlers>  
-->  
</system.webServer>

These features *do not* apply to exports created using Process Tasks.

Without these feature, these files are cleaned up periodically - see the following section.

## Temporary File Clean Up

When you create temporary files, you run the risk of consuming all of your hard disk storage space. To manage this, Info includes an automatic mechanism that "cleans up" files in temporary file folders by deleting them.

* Temporary file clean up runs on the very first application page request.
* With each subsequent request, Logi Info checks to see if it's been 5 minutes (default value, configurable--see below) since the last clean up. If so, then clean up is run again.
* When clean up runs, Info deletes any files older than 60 minutes (default value, configurable--see below) that are found in the rdDataCache and rdDownload folders, and the SecureKey Shared Folder, if that type of Logi Security is being used.
* When clean up runs, a message is added to the debug log.

In addition, when the web server is shut down cleanly, Info deletes all the files in rdDataCache and rdDownload automatically.

### Configure the Time Intervals

The two time intervals mentioned above are the default values but they can be configured differently.

![](https://devnet.logianalytics.com/hc/article_attachments/4406816680855/tempcache_02.png)  
 As shown above, two constants can be added to the \_Settings definition to configure the clean up mechanism.

* rdTempFileCleanupInterval - The time, in minutes, between clean ups. If this value is -1, clean up will not run at all; if the value is 0, clean up will run with *every* page request. Default value: *5 minutes*.
* rdTempFileLifespan - The minimum file age, in minutes, before a file qualifies to be deleted when the clean up runs. Default value: *60 minutes*. Note that your web server's **Session Timeout** setting should *not* be configured to be *less* than the value assigned to rdTempFileCleanupInterval or its default value of 5 minutes.

For information about these and other constants settings, see [Special Constants and Reserved Words](https://devnet.logianalytics.com/hc/en-us/articles/1500009531861-Special-Constants-and-Reserved-Words).
