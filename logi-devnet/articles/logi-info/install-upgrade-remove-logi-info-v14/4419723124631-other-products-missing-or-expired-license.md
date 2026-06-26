---
title: "Other Products: Missing or Expired License"
id: 4419723124631
section: "Install, Upgrade, & Remove - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723124631-Other-Products-Missing-or-Expired-License
updated_at: 2022-07-17T02:23:42Z
---

# Other Products: Missing or Expired License

# Other Products: Missing or Expired License

Other licensed Logi products, including the Discovery Module and DataHub, react differently when their licenses expire. A product or feature that requires a login, such as Dataview Authoring, will display an error message when a login is attempted:

![](https://devnet.logianalytics.com/hc/article_attachments/7522820631703/licenses_10.png)

Some products will allow you to view data but you cannot save visualizations or changes if the license has expired.
Other products will cause the Logi Info applications they work with to throw an error, with a descriptive error message in the usual format.

## Replacing Expired License Files

If your license for Discovery prior to Version 3.2 or DataHub 3.0+ expires, you'll need to replace it.
The very first time one of these products runs, the trial license file contents are automatically copied into the Platform Database (PDB) and used directly from there. Afterwards, the actual trial license file and any other license files subsequently placed in the folder, will be *ignored*. You'll need to perform the following to "replace" your trial license with an extended-trial or regular license.

WINDOWS: The license file record can be deleted from the PDB, and another one inserted to replace it, using [DeleteLicenseDB.txt](https://clm.logianalytics.com/downloads/Discovery/DeleteLicenseDB.txt) and [InsertLicenseDB.txt](https://clm.logianalytics.com/downloads/Discovery/InsertLicenseDB.txt), as follows:

1. Place the new license file in the same folder as the old license file, typically C:\LogiAnalytics\Discovery.
2. Download and save the two files above to your desktop.
3. Edit each file to include the correct Discovery Admin password, license file name, and license file path (if not the default). ![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) When editing DeleteLicenseDB.txt, you specify only the license file name, without its extension. For example, to delete the standard trial license, you specify "license-id=logiTrial03" (no quotes).
4. Rename the downloaded file extensions to ".bat".
5. Using *Run As Administrator*, execute the DeleteLicenseDB.bat file and allow it to fully complete.
6. Using *Run As Administrator*, execute the InsertLicenseDB.bat file and allow it to fully complete.

Information about this process is logged to: C:\LogiAnalytics\Discovery\platform\logs\licenseImport.log

## LINUX/UNIX:

These steps assume Discovery was installed in /opt/Discovery - adjust as necessary for your installation location.

1. Place the new license file in the same folder as the old license file, typically /opt/Discovery.
2. Download and save the two files above to your desktop.
3. Manually stop the Logi Application Server and Logi Data Service daemons.
4. Manually run /opt/Discovery/platform/bin/licenseTool.sh, editing and using the arguments found in the DeleteLicenseDB file.
5. Manually run licenseTool.sh again, editing and using the arguments found in the InsertLicenseDB file.
6. Manually start the Logi Data Service daemon.
7. Wait 20 seconds, manually start the Logi Application Server daemon

Information about this process is logged to: /opt/Discovery/platform/logs/licenseImport.log  

![](https://devnet.logianalytics.com/hc/article_attachments/7522806338455/licenses_11.png)
