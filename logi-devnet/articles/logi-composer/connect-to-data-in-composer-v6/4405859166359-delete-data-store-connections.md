---
title: "Delete Data Store Connections"
id: 4405859166359
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859166359-Delete-Data-Store-Connections
updated_at: 2021-09-21T01:27:01Z
---

# Delete Data Store Connections

# Delete Data Store Connections

A data store connection cannot be deleted if it is used by any data source configurations. You must first remove it from the data source configurations before you can delete it.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) You must be logged in as an administrator or as a user with the [group privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference)**Can Manage Connections** to maintain data store connection definitions.

To delete a data store connection:

1. Make sure you are logged into Composer as an administrator or as a user with the [group privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference)**Can Manage Connections**.
2. Select **Connections** on the [top-level navigation banner](https://devnet.logianalytics.com/hc/en-us/articles/4405851152407-The-Top-Level-Navigation-Banner) or the [UI menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859444119-The-Composer-UI-Menu) (![](https://devnet.logianalytics.com/hc/article_attachments/4406743720343/hamburger.png)) or select the **Connections** box on the [Home page](https://devnet.logianalytics.com/hc/en-us/articles/4405851121559-Home-Page). The [Connections page](https://devnet.logianalytics.com/hc/en-us/articles/4405850909975-Connections-Page) appears.

   The Connections page lists the data store connections you have defined and identifies how many data source configurations each connection uses.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743923351/connections-page1_768x131.png)
3. Highlight (hover over) the row listing the data store connection you want to delete. You can search the list to locate the connection definition. See [*Search for a Definition in a List*](https://devnet.logianalytics.com/hc/en-us/articles/4405850911127-Search-for-a-Definition-in-a-List).
4. Select the trashcan (![](https://devnet.logianalytics.com/hc/article_attachments/4406743722391/trashcan.png)) in the Actions column for the associated row.

   A warning dialog appears.
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406747430807/delete-blue1-btn_50x26.png) on the warning dialog.

   The connection is deleted.
