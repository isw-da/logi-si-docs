---
title: "License Management"
id: 4419715444887
section: "Install, Upgrade, & Remove - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715444887-License-Management
updated_at: 2022-07-17T02:23:43Z
---

# License Management

# License Management

DevNet includes a **License Management** page where you can manage your product licenses and download license files. In order to manage your licenses, you must be a DevNet member and login to the DevNet site. Once you are logged in, go to **Support**![](https://devnet.logianalytics.com/hc/article_attachments/7522803222807/menuarrowrt.png)**License Manager**.

![](https://devnet.logianalytics.com/hc/article_attachments/7522759984663/image__7__1169x573.png)

The details of the License Management page are shown above and explained below:

1. **Products, Status, Search** - These controls let you filter the table of license keys, by product type and status, and search based on License Key name.
2. **Export** - Use these icons to export your license key list to Excel or PDF.
3. **License Key Name** - The license key we created for you when you purchased the product appears here.
4. **Type & Expires** - The license type and expiration date appear here.
5. **License** - License actions: click the "Create" link in this column to assign your license to a specific machine. Once done, the machine name will appear in the next column and the link will change to "Download". Click the link again to download and save your license file. You may download the file as many times as necessary but it's only valid on the assigned machine.
6. **Assigned To** - The name of the machine a license has been assigned to. The ![](https://devnet.logianalytics.com/hc/article_attachments/7522820701079/btnlicdel.gif) icon allows you to "un-assign" the license - when this is done, the License link will revert back to "Create", and you may assign the license to another machine.
7. **Note** - This column displays optional text you enter to help you more easily identify the computer. Click the ![](https://devnet.logianalytics.com/hc/article_attachments/7522795463063/btnlicedit.gif) icon to add or edit this text.
8. **Log** - Click the ![](https://devnet.logianalytics.com/hc/article_attachments/7522795467159/btnliclog.gif) icon to display the history of assignments for this license.

Here are the details of the process of creating and downloading a license file:

![](https://devnet.logianalytics.com/hc/article_attachments/7522820734359/licenses_03.png)

If the link in the Licenses column of the table shown earlier says "Create", clicking it will display the **Create License File** pop-up panel, shown above. You use it to assign the license to a specific machine, by entering the computer name. The Optional Note input is for your use if you want to further identify the machine and its text appears in the table of licenses shown earlier.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) The machine name "LogiOEM" (or any case variation thereof) is not a valid machine name.

If the computer on which this license is to be used runs a **Windows** OS, then the computer name value is what's known in Windows parlance as the "machine name". You can open a Command Prompt window on the machine and enter "hostname", then press Enter to have the name displayed. If a multi-part name is displayed, such as "myPC.myCompany.local", use just the first part, "myPC".

If the computer on which this license is to be used runs a **Linux or other UNIX-derivative** OS, then the "computer name" value is the computer's "hostname". You can go to a command line and enter "#hostname", then press Enter to have the name displayed. Use the *full* hostname value, exactly as it's displayed, for your computer name value entry.

Click **OK** to generate the license file for the designated computer.

![](https://devnet.logianalytics.com/hc/article_attachments/7522806448279/licenses_04.png)

Once the license file has been generated, the link in the Licenses column will change to "Download". Click this link to display the Download License File pop-up panel, shown above. Click **Download** to download and save the license file.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) Some browsers may add an .xml file extension to the downloaded file, which is *wrong*. A typical license filename looks like lgx120201.lic so don't let your browser add anything to it.
If the computer on which this license is to be used runs a **Windows** OS, then save the license file to

C:\Program Files\LogiXML IES Dev\LogiStudio

This will provide licensing for development work using Logi Studio, as well as for new Logi applications that are developed on the machine and run there using any web server. If you're upgrading any older Logi applications, you'll also need to copy the license file into their application folder.

If the computer on which this license is to be used runs a **Linux or other UNIX-derivative** OS, then the license file location will depend on how you start the web server. If you start it from the bin folder, then save the license file there. If you start it elsewhere, for example, by running a script, then save it to the folder that you run the script from.
