---
title: "Copy the New Files"
id: 4406817910039
section: "Install, Upgrade, & Remove - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817910039-Copy-the-New-Files
updated_at: 2022-04-06T06:09:01Z
---

# Copy the New Files

# Copy the New Files

Start by copying files from the newly installed version to your working
InfoGo copy, as follows:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575533975/upgrssrm_02.png)

1. Copy all of the Report definition files with the
   InfoGo
   virtual folder prefix, shown selected above, from the original
   \_Definitions\\_Reports
   folder to the target
   \_Definitions\\_Reports
   folder, overwriting the existing files.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417563074967/upgrssrm_03.png)
2. Copy the
   InfoGo.goManageReports.lgx
   file, shown selected above, from the original
   \_Definitions\\_Processes
   folder to the target
   \_Definitions\\_Processes
   folder, overwriting the existing file.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417583722007/upgrssrm_04.png)
3. Copy all files from the original
   \_SupportFiles
   folder, *except* those with the
   goCustomizations
   virtual folder prefix and
   InfoGo.DashboardModifier.xml and
   InfoGo.AnalysisGridModifier.xml, to the target
   \_SupportFiles
   folder, as shown above. ![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) The image above does not show
   *all* of the selected files - there should be about 78 of them.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417583722519/upgrssrm_05.png)
4. Copy the files in the original
   \_Plugins
   folder to the target
   \_Plugins
   folder. Verify that each
   .dll
   file has been upgraded by right-clicking it, selecting Properties, and
   checking its version in the Details tab, as shown above. If you
   encounter an error while copying or the version number is incorrect, you
   may need to stop and restart your web server to unload the .dlls before
   trying to copy them again.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417583722903/upgrssrm_06.png)
5. Open the original and target InfoGo applications and examine their
   \_Settings definitions. Manually compare their Constants element
   parameters, as shown above, and add any new parameters from the original
   file to the target file.
