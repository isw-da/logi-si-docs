---
title: "Web Metadata Builder"
id: 4406817979799
section: "Connect to Data - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817979799-Web-Metadata-Builder
updated_at: 2022-04-06T06:09:24Z
---

# Web Metadata Builder

# Web Metadata Builder

The **Web Metadata Builder** is a tool used to create and manage "metadata files", which are used with elements that have been extended to use the Active Query Builder for data retrieval.

The following topics provide further instructions for using the tool:

* [Using the Web Metadata Builder](https://devnet.logianalytics.com/hc/en-us/articles/4406822571159-Using-the-Web-Metadata-Builder#Metadata)
* [Managing Data Source Connections](https://devnet.logianalytics.com/hc/en-us/articles/4406817977623-Managing-Data-Source-Connections#Connections)
* [Managing Metadata Definitions](https://devnet.logianalytics.com/hc/en-us/articles/4406817978647-Managing-Metadata-Definitions#Definitions)
* [Creating Multiple Metadata Files](https://devnet.logianalytics.com/hc/en-us/articles/4406822570135-Creating-Multiple-Metadata-Files#Multiple)

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) Prior to Logi Info v12.5, metadata builder functionality was available as a wizard built into Logi Studio. Beginning with v12.5, the Web Metadata Builder replaces that wizard and appears in a window
within Studio.

## About the Web Metadata Builder

The **Web Metadata Builder** (WMB) is a browser-based tool for building metadata. It's part of Logi Studio (v12.5+) and is also delivered with some Logi Info add-on modules.

The WMB creates and manages metadata files, which are utilized in a Logi Info application with the **Active Query Builder** and **Metadata** elements. These elements enable a UI that allows end-users to decide which data set to work with, by giving them a way to interactively select tables and joins, at runtime.

For example, an Analysis Grid (AG) is often configured with a SQL datalayer, which retrieves data based on a
SQL query hard-coded by the developer. The query determines the basic dataset that will be available to all AG users for analysis.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575503767/usingwmb_23.png)

However, when added as a child of an Analysis Grid, the Active Query Builder element causes a special "Data" tab to appear at the top of the
AG, as shown above. In it, users can select the tables and joins they want to work with. Intelligent assistance is provided to help users make reasonable joins and the SQL query is then created dynamically. This allows users to have a greater choice in the data they work with.

## Controlling the Metadata

You, as the developer or InfoGo data manager, still exercise control over what tables, views, columns, and relationships are available for use with the Active Query Builder. This is where the "metadata file", associated with a Connection element, comes in. It enumerates all of the database objects that will be available to users for selection in the Analysis Grid. The Active Query
Builder is then pointed
to one or more metadata files. Multiple metadata files can be associated with a Connection element.

The WMB is used during development or InfoGo data management to create and manage metadata files. It provides the same functionality as the wizard with the same name in Logi Studio but, as a web-based tool, without the need to run Studio.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563031319/usingwmb_01.png)

Using the WMB results in a Metadata element being inserted into the application's \_Settings definition, as a child of the specified Connection element, as shown above. The Metadata element is configured to use the metadata file created using the WMB. You can, of course, manually insert and configure the element.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575435927/notev12.7base.png)The [Definition Modifier Files](https://devnet.logianalytics.com/hc/en-us/articles/4406817363863-Definition-Modifier-Files) element is now available as a child of the Metadata element and is intended for use supporting translations and internationalization. *It should not be used in this context for other purposes, such as modifying tables or applying security.*

The Active Query Builder and Metadata elements installed with the SSRM work with these database servers:

* DB2
* Microsoft SQL Server 2005+
* MySQL
* Oracle
* Progress OpenEdge
* PostgreSQL
* Redshift (Amazon)
* Vertica (HP)

and any JDBC-accessible databases that use the same SQL syntax as one of the listed databases.

## Controlling Web Metadata Builder Access

If you're *not* using Logi Security, then access to the WMB is available to anyone.

However, access to the WMB can be disabled for *all* users by setting the **General** element's **Disable Metadata Builder** attribute equal to *True*, in your \_Settings definition.

If you *are* using Logi Security, then access to the WMB can be selectively controlled by the Security element's **Metadata Admin Security Right IDs** attribute, in your \_Settings definition. This attribute specifies a comma-separated list of Security Right IDs that will be granted access to the WMB. The default value is rdMetadataAdmin.
To grant access to the WMB, either give users the
rdMetadataAdmin security Right, or set this attribute to an existing
administrator security Right.
