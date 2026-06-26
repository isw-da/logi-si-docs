---
title: "Delete Data Store Connections"
id: 43701054466061
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701054466061-Delete-Data-Store-Connections
updated_at: 2026-05-29T14:11:35Z
---

# Delete Data Store Connections

# Delete Data Store Connections

A data store connection cannot be deleted if it is used by any data source configurations. You must first remove it from the data source configurations before you can delete it.

**Note:** 
You must be logged in as an administrator or as a user with the [group privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference) **Manage Connections** to maintain data store connection definitions.

**Delete a data store connection:**

1. Log in as an administrator or as a user with the [group privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference) **Manage Connections**.
2. Select **Connections** on the [top-level navigation banner](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701115577869-The-Top-Level-Navigation-Banner) or the [UI menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701160499853-The-Composer-UI-Menu) (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243300476941)) or select the **Connections** box on the [Home page](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701136935821-Home-Page). The [Connections page](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701008155149-Connections-Page) appears.

   The Connections page lists the data store connections you have defined and identifies how many data source configurations each connection uses.
3. Highlight (hover over) the row listing the data store connection you want to delete. You can search the list to locate the connection definition. See [Search and Filter Lists](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701008213517-Search-and-Filter-Lists).
4. Select the delete icon (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243317080333)) in the Actions column for the associated row.

   A warning dialog appears.
5. Select **Delete** on the warning dialog. The connection is deleted.

**Note:** 
If you try to delete a visual, filter snippet, dashboard, dashboard link, source, or source field, Composer displays an error message naming any objects dependent on the item you’re trying to delete. You can delete the item after you’ve removed the association from the dependent object.
See[Fields Usage](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701095792013-Fields-Usage).
