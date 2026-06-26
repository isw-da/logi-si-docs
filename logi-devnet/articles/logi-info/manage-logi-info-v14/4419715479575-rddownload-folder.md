---
title: "rdDownload Folder"
id: 4419715479575
section: "Manage - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715479575-rdDownload-Folder
updated_at: 2022-07-17T01:37:38Z
---

# rdDownload Folder

# rdDownload Folder

The rdDownload folder is the home of a number of other temporary files.
For example, when debugging links are turned on and trace pages are
created, the XML debug files are stored here. *Uploaded* files, oddly
enough, temporarily reside here, too, before being relocated, and exports
also use this folder for temporary files.

There is no way to rename or relocate this folder.

Developers who need to store data in temporary files are free to use these
folders, too (traditionally, rdDownload). And it's a very good idea to do
so. The server account under which Logi applications run typically has
been granted Write permissions to these folders, so files can be written
there.

## Securing rdDownload

When reports or data are exported from Report definitions, the
rdDownload folder temporarily contains exported PDF, Excel, etc. files in
order to make them available for download by the user who created them. By
default, these files have names based on GUIDs, so directly accessing them
without permission by guessing their names *is* possible but
unlikely. However, if you'd like to further secure these files, you can
engage two special features.

* The first feature requires that the Session ID of the user requesting an
  export file download match that of the user who created the export file,
  otherwise an HTTP 403 error is returned.

* The second feature ensures that supporting files used in the process of
  creating an export, and saved in rdDownload, are deleted once the export
  file is created but before it's streamed back to the requesting user.

To enable these features, you must manually alter the Logi application's
web.config
file, in the application's root folder. The file already contains the code
required and all you have to do is uncomment it to enable it. Here's the
code:

<!-- Uncomment the following rdDownloadSecPageHandler verb in the
httpHandlers section to enable the automatic deletion of export files in
the rdDownload directory. This also enables additional security for these
files.  -->  
 <system.web>  
<!--  
     <httpHandlers>  
             <add
verb="\*" path="rdDownload/\*"
type="rdServer.rdDownloadSecPageHandler,rdServer"/>
       
     </httpHandlers>  
-->   
 </system.web>  
 <!--  Uncomment the  rdDownloadSecPageHandler in the
system.webServer section to enable rdDownload directory Security
  -->  
 <system.webServer>  
<!--  
       <validation
validateIntegratedModeConfiguration="false"/>  
           <handlers>  
         
    <add  verb="\*"
path="rdDownload/\*" name="rdDownloadSecPageHandler"
type="rdServer.rdDownloadSecPageHandler,rdServer"
resourceType="Unspecified"/>  
         </handlers>  
-->  
 </system.webServer>

These features *do not* apply to exports created using Process Tasks.

Without these feature, these files are cleaned up periodically - see [Temporary File Clean Up](https://devnet.logianalytics.com/hc/en-us/articles/4419707839895-Temporary-File-Clean-Up).
