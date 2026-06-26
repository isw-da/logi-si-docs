---
title: "Copy the New Files"
id: 4419715495703
section: "Install, Upgrade, & Remove - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715495703-Copy-the-New-Files
updated_at: 2022-07-17T01:36:37Z
---

# Copy the New Files

# Copy the New Files

Start by copying files from the newly installed version to your working
InfoGo copy, as follows:

1. Copy all of the Report definition files with the
   InfoGo
   virtual folder prefix from the original
   \_Definitions\\_Reports
   folder to the target
   \_Definitions\\_Reports
   folder, overwriting the existing files:  
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4419707083031/upgrssrm_02.png)
2. Copy the
   InfoGo.goManageReports.lgx
   file from the original
   \_Definitions\\_Processes
   folder to the target
   \_Definitions\\_Processes
   folder, overwriting the existing file:  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4419699912855/upgrssrm_03.png)
3. Copy all files from the original
   \_SupportFiles
   folder, *except* those with the
   goCustomizations
   virtual folder prefix and
   InfoGo.DashboardModifier.xml and
   InfoGo.AnalysisGridModifier.xml, to the target
   \_SupportFiles
   folder, as shown below. ![](https://devnet.logianalytics.com/hc/article_attachments/4419706599575/noteicon.png) The image below does not show
   *all* of the selected files - there should be about 78 of them.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4419707083287/upgrssrm_04.png)
4. Copy the files in the original
   \_Plugins
   folder to the target
   \_Plugins
   folder. Verify that each
   .dll
   file has been upgraded by right-clicking it, selecting Properties, and
   checking its version in the Details tab, as shown below. If you
   encounter an error while copying or the version number is incorrect, you
   may need to stop and restart your web server to unload the .dlls before
   trying to copy them again.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4419714904727/upgrssrm_05.png)
5. Open the original and target InfoGo applications and examine their
   \_Settings definitions. Manually compare their Constants element
   parameters and add any new parameters from the original
   file to the target file.

![](https://devnet.logianalytics.com/hc/article_attachments/4419707083671/upgrssrm_06.png)
