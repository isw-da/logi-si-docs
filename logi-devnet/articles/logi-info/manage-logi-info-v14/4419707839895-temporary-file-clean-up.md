---
title: "Temporary File Clean Up"
id: 4419707839895
section: "Manage - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707839895-Temporary-File-Clean-Up
updated_at: 2022-07-17T02:23:28Z
---

# Temporary File Clean Up

# Temporary File Clean Up

When you create temporary files, you run the risk of consuming all of your hard disk storage space. To manage this, Info includes an automatic mechanism that "cleans up" files in temporary file folders by deleting them.

* Temporary file clean up runs on the very first application page request.
* With each subsequent request, Logi Info checks to see if it's been 5 minutes (default value, configurable--see below) since the last clean up. If so, then clean up is run again.
* When clean up runs, Info deletes any files older than 60 minutes (default value, configurable--see below) that are found in the rdDataCache and rdDownload folders, and the SecureKey Shared Folder, if that type of Logi Security is being used.
* When clean up runs, a message is added to the debug log.

In addition, when the web server is shut down cleanly, Info deletes all the files in rdDataCache and rdDownload automatically.

## Configure the Time Intervals

The two time intervals mentioned above are the default values but they can be configured differently.  
![](https://devnet.logianalytics.com/hc/article_attachments/7522803799831/tempcache_02.png)

As shown above, two constants can be added to the \_Settings definition to configure the clean up mechanism.

* rdTempFileCleanupInterval - The time, in minutes, between clean ups. If this value is -1, clean up will not run at all; if the value is 0, clean up will run with *every* page request. Default value: *5 minutes*.
* rdTempFileLifespan - The minimum file age, in minutes, before a file qualifies to be deleted when the clean up runs. Default value: *60 minutes*. ![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) Your web server's **Session Timeout** setting should *not* be configured to be *less* than the value assigned to rdTempFileCleanupInterval or its default value of 5 minutes.

For information about these and other constants settings, see
[Special Constants](https://devnet.logianalytics.com/hc/en-us/articles/4419723160343-Special-Constants) and [Reserved Words](https://devnet.logianalytics.com/hc/en-us/articles/4419715473687-Reserved-Words).
