---
title: "Granting File Permissions Under Windows"
id: 4406817455383
section: "Manage - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817455383-Granting-File-Permissions-Under-Windows
updated_at: 2022-04-06T06:06:11Z
---

# Granting File Permissions Under Windows

# Granting File Permissions Under Windows

Depending on your OS, you'll use **File Explorer** or
**My Computer** to set file permissions.  

![](https://devnet.logianalytics.com/hc/article_attachments/4417563291031/fileperm_01.png)

1. On the web server, navigate into your Logi application's folder and
   select the *rdDataCache* folder.
2. Right-click the folder and select **Properties** from the pop-up
   menu, as shown above, left.
3. In the Properties dialog box, click the **Security** tab, as shown
   above, right. Click **Edit...***No Security tab visible? See section below.*![](https://devnet.logianalytics.com/hc/article_attachments/4417575699991/fileperm_02.png)

4. If we're assigning permissions to the NETWORK SERVICE account, click
   Add... and then enter the account name in the subsequent dialog box, as
   shown above. Click **OK**.
![](https://devnet.logianalytics.com/hc/article_attachments/4417575700119/fileperm_04.png)  

5. Back in the Security dialog box, ensure that the NETWORK SERVICE account
   is selected and click the *Full Control* check box, as shown above.
   Then click **OK**.

Repeat this process for the
rdDownload
folder and for any other folders that you'll be writing data to.

## IIS 6 And Later - Application Pools

In IIS 6 and later, in addition to setting the permissions shown earlier,
you may also need to give permissions to the "Application Pool".
Logi Info applications are generally run by IIS within an application
pool, which provides isolation and performance improvements for web apps
that may use different versions of .NET. To assign file access permissions
to an application pool:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563291415/fileperm_06.png)

1. Open the IIS Manager utility, locate your Logi application and
   determine, by examining its properties, which application pool it's
   assigned to. Note the name of the pool ("DefaultAppPool" in
   the example).

![](https://devnet.logianalytics.com/hc/article_attachments/4417575700631/fileperm_07.png)

2. In the example above, we're setting permissions for the sub-folder
   "SavedFiles". Use File Explorer to navigate to your Logi app
   folder, then select and right-click the sub-folder in question, and
   select **Properties**.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583939735/fileperm_08.png)

3. In the Properties dialog box, click the **Security** tab, and then
   the **Edit** button.
4. In the Permissions dialog box, click **Add**.
5. In the Select Users or Groups dialog box, enter "IIS
   APPPOOL\<the app pool name>" as shown above.
6. Click **OK**, to close the dialog box and return to the Permissions
   dialog box.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575701015/fileperm_09.png)

Finally, select the application pool in the names list, and set its
permissions, as shown above. Then click **OK**.

## No Security Tab Visible?

In order to make the **Security** tab visible in the Properties dialog
box, you must turn off **Simple File Sharing**. This is usually an
issue only on stand-alone computers.

1. Open **Control Panel** and locate the **Folder Options** link. In
   Windows XP, this is through the **Appearance and Themes** link. Or,
   instead, you can access Folder Options through the **Tools** menu
   item in My Computer.
2. In the Folder Options dialog box, select the **View** tab.
3. At the very bottom of the list of **Advanced****settings**,
   un-check the "Use simple file sharing" option. Click
   **OK**.

The security tab should now appear when you select a file or folder's
properties.
