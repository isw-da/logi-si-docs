---
title: "Data Sources Page"
id: 43701081381901
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701081381901-Data-Sources-Page
updated_at: 2026-05-29T14:10:55Z
---

# Data Sources Page

# Data Sources Page

Use **Sources** to create, import, export, search, review, and maintain your data sources.

All users can view the **Sources** work area.

* If you log in as a user who has not been granted [permissions](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701101615373-About-Source-Permissions) for any data sources, the **Sources** work area displays a message indicating that no sources are available.
* If you log in as a user who only has **read** [permissions](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701101615373-About-Source-Permissions) for one or more data sources, they are shown here, but Connection information is not available for the sources.
* If you log in as a user who belongs to a group that is granted the **Create New Data Sources** or **Administer Sources** [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference), you can create, import, export, and maintain data source configurations using this work area.

![Use this work area to create, import, and edit data sources.](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242588195725 "Sources Work Area")

The Data Sources work area includes the following features:

1. **Create Source**: Select to create a new data source configuration. See [Define a Source](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701080450061-Define-a-Source).
2. **Import Source**: Select to import a new data source configuration and connection information. See [Import or Export Sources](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701098185613-Import-or-Export-Sources).
3. **Export Selected Items**: Export one or more data sources by selecting the checkbox for a source to export. The **Export Selected Items** button becomes active. Select to download the sources in JSON format.
4. **Embed Sources Inventory**: Select ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242555555341) to generate a code snippet to embed the sources inventory in your application. See [Generate a Sources Inventory HTML Snippet](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701117598861-Generate-a-Sources-Inventory-HTML-Snippet).
5. A table that lists the data sources you can see, sort, and favorite.
6. Options to modify source permissions, view and modify row and column security filters, refresh the cache, and manage Available Visual Types and Materialized Views.
7. A search bar at the top of the page you can use to search for a specific data source in the table.

**Access the Data Sources work area**

1. Log into Composer.
2. Select **Sources** on the [UI menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701160499853-The-Composer-UI-Menu) (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243248828429)) or the [top-level navigation menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701115577869-The-Top-Level-Navigation-Banner), or select the **Sources** box on the [Home page](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701136935821-Home-Page). The Sources work area appears.

Depending on your settings, you can edit and delete data sources listed in the table. You can also clear the cache for a data source. If there are many sources listed, you may need to search for the source you need.

## Search Field

You can use the search field to filter the sources in this work area by source Name, Description (if provided), Connection, or Author. For example, if you type a **C** in the search box, only sources that include the letter *C* in the selected field searched are shown in the working area. See [Search and Filter Lists](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701008213517-Search-and-Filter-Lists).

## Buttons

The buttons on the page allow easy access to saved data sources, as well as other data sources created by other users in your Composer environment that you have been granted access to see. Use the options shown to create new sources, filter the data sources shown, as well as import, export, or create sources.

| Button | Description |
| --- | --- |
| All | Removes any filters for the sources list and displays all sources available to you within your environment. |
|  | Displays only the sources that you have marked as favorites. |
|  | Displays only the sources that you created and saved. Sources created and saved by other users are hidden. |
|  | Displays only the sources that other users shared with you. |
|  | Select to generate an embeddable sources inventory link.  See [Generate a Sources Inventory HTML Snippet](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701117598861-Generate-a-Sources-Inventory-HTML-Snippet). |
| **Export Selected Items** | Allows you to export multiple selected items. |
| **Import Source** | Allows you to import a source.  See [Import or Export Sources](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701098185613-Import-or-Export-Sources). |
| **Create Source** | Allows you to create a new source.  See [Define a Source](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701080450061-Define-a-Source). |

## The Sources List

The sources list columns are described below. Several of these columns can be used to sort the list: select the column header to sort first to last and again to sort last to first. You can search for items by the contents of several columns. See [Search and Filter Lists](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701008213517-Search-and-Filter-Lists).

| Column | Description |
| --- | --- |
| Select (not labeled) | Select one or more items to perform bulk actions, such as export, for your resources. |
| Fav | Mark the source as a favorite. |
| Type | An icon identifying the data store type for the data source. |
| Name | The name assigned during data source creation. |
| Description (not labeled) | The description icon is visible if a description associated with a source. You can search for a source by the contents of this field. |
| Tags | Content tags applied to the source. Select the filter icon to open a drop down list and select tags to filter your list or to [narrow your search results](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701008213517-Search-and-Filter-Lists#Filter). If several tags are associated with an item, hover over the ellipsis to see all tags for this resource. |
| Filter icon | Select to filter the work area's contents by one or more content tags. |
| Connection | The display name of the [data store connection definition](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701038107149-Manage-Data-Store-Connections) connected to this data source. For flat files, you define a Display Name when you upload the file; this name is shown. |
| Author | The user name of the data source creator. |
| Modified Date | The time stamp when the data source configuration definition was last modified. |
| Permissions | Select the permissions icon for a data source to assign and manage its permissions. You can only define permissions for a data source if you are logged in as a user with the **Administer Sources** [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference), or as a user with the **Manage Source Permissions** privilege. |
| Row | Select the row security ( ) icon for a data source to define its row security for [authorization groups](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701035505293-Manage-User-Groups). You can only define row security for a data source if you are logged in as a user with the **Administer Sources** [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference), or as a user with the **Manage Source Permissions** privilege. |
| Column | Select the column security ( ) icon for a data source to define its column security for different [authorization groups](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701035505293-Manage-User-Groups). You can only define row security for a data source if you are logged in as a user with the **Administer Sources** [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference), or as a user with the **Manage Source Permissions** privilege. |
| Actions | Shows icons you can select to perform actions for the data source.   * Select the delete () icon to delete a data source configuration. Before you delete a data source configuration, you must delete all the dashboards and visuals that use it. See [Delete a Data Source Configuration](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701080355981-Delete-a-Data-Source-Configuration). You can only delete a data source if you are logged in as, a user with the **Administer Sources** [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference), or a user with **read** and **delete** [permission](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701101615373-About-Source-Permissions) for the data source. * Select the clear cache () icon to clear the data cache for a data source configuration. Select one or more cache options to clear:    + Data Cache: Clears the cached query results.   + Statistics Cache: Clears the cache of fields statistic metadata, such as min, max, and distinct values numbers. See [How Composer Caches Data](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701078034061-How-Composer-Caches-Data) and [Clear the Cache for a Data Source Configuration](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701080340493-Clear-the-Cache-for-a-Data-Source-Configuration). You can only clear the cache for a data source if you a user with the **Administer Sources** [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference), or a user with **write** [permission](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701101615373-About-Source-Permissions) for the data source.  **Note:**    If a [Custom Range](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116424973-Manage-Fields#Custom) has been defined for a field, the minimum and maximum fields used in filters remain unchanged when you refresh source data. These fields are shown with cache actions disabled on the [Cache tab](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701085337997-Cache-Tab). * Select the More menu () button to view the More menu for a data source configuration. Options include:    + Available Visual Types: Select to define what visuals are available for this data source configuration. See [Available Visual Types](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701177930509-Available-Visual-Types).   + Materialized Views: Select to define materialized view settings for the data source configuration. See [Use Materialized Views (Experimental)](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701111709069-Use-Materialized-Views-Experimental). Not visible if disabled.   + Export Source: Select to export the source information in JSON format. See [Import or Export Sources](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701098185613-Import-or-Export-Sources).   **Note:**  If you try to delete a visual, filter snippet, dashboard, dashboard link, source, or source field, Composer displays an error message naming any objects dependent on the item you’re trying to delete. You can delete the item after you’ve removed the association from the dependent object. See[Fields Usage](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701095792013-Fields-Usage). |
