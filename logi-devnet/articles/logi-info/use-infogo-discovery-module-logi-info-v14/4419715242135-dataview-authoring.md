---
title: "Dataview Authoring"
id: 4419715242135
section: "Use InfoGo/Discovery Module - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715242135-Dataview-Authoring
updated_at: 2022-07-17T01:52:12Z
---

# Dataview Authoring

# Dataview Authoring

Logi Data Services technology, found in recent Discovery Module versions, uses Dataviews to define datasource
connections, queries, and data enrichment.

The following topics discuss
Dataviews and the tools for creating and managing them:

* [Launching the Dataview Authoring Tool](https://devnet.logianalytics.com/hc/en-us/articles/4419707518359-Launching-the-Dataview-Authoring-Tool#Launch)
* [Dataview Authoring Tool Menu](https://devnet.logianalytics.com/hc/en-us/articles/4419707516311-Dataview-Authoring-Tool-Menu#Menu)
* [Managing Your Profile](https://devnet.logianalytics.com/hc/en-us/articles/4419715244439-Managing-Your-Profile#Profile)
* [Connecting to Databases](https://devnet.logianalytics.com/hc/en-us/articles/4419707514135-Connecting-to-Databases#Databases)
* [Connecting to Data Files and Applications](https://devnet.logianalytics.com/hc/en-us/articles/4419722853399-Connecting-to-Data-Files-and-Applications#Applications)
* [Managing Data Sources](https://devnet.logianalytics.com/hc/en-us/articles/4419722855831-Managing-Data-Sources#ManageDS)
* [Creating a Dataview](https://devnet.logianalytics.com/hc/en-us/articles/4419715241111-Creating-a-Dataview#CreateDV)
* [Dataview Loading](https://devnet.logianalytics.com/hc/en-us/articles/4419715243031-Dataview-Loading)
* [Filtering Data](https://devnet.logianalytics.com/hc/en-us/articles/4419707517335-Filtering-Data#Filter)
* [Data Enrichment](https://devnet.logianalytics.com/hc/en-us/articles/4419722854551-Data-Enrichment#Enrichment)
* [Creating Data Relationships](https://devnet.logianalytics.com/hc/en-us/articles/4419707515031-Creating-Data-Relationships#Relationships)
* [Managing Dataviews](https://devnet.logianalytics.com/hc/en-us/articles/4419722856727-Managing-Dataviews#ManagingDVs)

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599575/noteicon.png) Advanced features discussed here work with Logi Info v12.5 and later. Earlier and later Info versions may not support them; consult the [Release Notes](https://clm.logianalytics.com/rdPage.aspx?rdReport=RelNotesINF) for specific details.

## About Dataviews

Logi Data Services technology provides you with an advanced means of data retrieval based on the "Dataview", a definition that specifies the connection information, query details,
and data enrichment details.

Dataviews are stored in a system database and can be used with the SuperWidget Authoring too. For more information, see [SuperWidgets](https://devnet.logianalytics.com/hc/en-us/articles/4419707702679-SuperWidgets). Dataviews can also be used in Logi Info reports using a special DataLayer element, and the data can be altered at runtime using special Data Service ("Ds") elements. When executed at the server, the Dataview retrieves the data and makes it available
in the standard datalayer format to other elements for analyses and visualizations. Some of the benefits of this include:

* Decoupling of developer and data architect duties
* Shared access to stored Dataviews by multiple users
* Better support for Self-Service analytics
* Excellent performance for very large datasets (250M+ rows)

Prior to working with Dataviews, a connection to Logi services must be configured. See [Get Started with the Discovery Module 3.2](https://devnet.logianalytics.com/hc/en-us/articles/4419707604759-Get-Started-with-the-Discovery-Module-3-2)
for more information.
Dataviews are created using tools like the Dataview Authoring tool accessible from Logi Studio. The Dataviews used with Logi Info can retrieve data from a number of databases.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599575/noteicon.png) If our **DataHub 3.0+** product is installed, then Dataviews can *also* retrieve and join file-, cloud-, and application-based data, such as Facebook, Google Analytics, and Marketo, and cache it in a separate data store.

The following sections describe how you can create and manage Dataviews using the browser-based tool in Logi Studio.
