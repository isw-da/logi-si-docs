---
title: "Creating a Default Panel Arrangement "
id: 4419707741335
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707741335-Creating-a-Default-Panel-Arrangement
updated_at: 2022-07-17T02:23:55Z
---

# Creating a Default Panel Arrangement 

# Creating a Default Panel Arrangement

You may want all of your users to start using the Dashboard with the exact same, pre-defined tab and panel arrangement. A default tab and panel arrangement can be saved for later use by working with the Dashboard element attributes **Save File** and **Save File Starter**.
As mentioned earlier, the "Save" file specified in the **Save File** attribute value is created automatically the first time the user changes the Dashboard configuration. It records any configuration changes a user makes to the Dashboard, such as which panels are included, panel arrangement, and tabs. When the user returns to use the Dashboard in a subsequent session, this file is used to automatically configure the Dashboard. As mentioned earlier, this file can be identified on a per-user basis,
providing each
user with their own
personal arrangement every time they use the Dashboard.
If a file is specified in the **Save File****Starter** attribute, and no Save File has been created yet (because this is the first time the user is using the Dashboard), then the Save File Starter file will provide the initial Dashboard configuration. This allows each user to begin with a standard initial Dashboard configuration.
Follow these steps to create a default panel and tab arrangement:

1. Create your Dashboard and panels in Logi Studio, as usual.  
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/7522792713239/introdash_27.png)
2. Configure the Dashboard element's **Save File** attribute with a value that will create a separate file for each user, as discussed earlier and shown above. The example above demonstrates the use of tokens in the value and assumes Logi Security is in use.
3. Run the application and, in your browser, create and arrange the tabs, panels, and panel parameters (if any) desired for your default arrangement. Close your browser.
4. In the file system, find the Save file that was just created during your session, and copy it to the \_SupportFiles folder. Rename the copy using an arbitrary but meaningful name, such as DashDefaultLayout.xml.  
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/7522792719127/introdash_28.png)
5. Back in Studio, configure the Dashboard element's **Save File Starter** attribute with the complete path and file name of your renamed Save file copy, as shown above.

All first-time users will now see the default Dashboard arrangement, and any customizations they're allowed to make will be saved for their next session.
