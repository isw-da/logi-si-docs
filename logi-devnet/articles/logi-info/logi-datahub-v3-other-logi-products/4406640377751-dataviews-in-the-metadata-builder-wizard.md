---
title: "Dataviews in the Metadata Builder Wizard"
id: 4406640377751
section: "Logi DataHub v3 & Other Logi Products"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406640377751-Dataviews-in-the-Metadata-Builder-Wizard
updated_at: 2022-04-01T03:13:27Z
---

# Dataviews in the Metadata Builder Wizard

# Dataviews in the Metadata Builder Wizard

Logi Info installations that include the [Self-Service Reporting Module](https://devnet.logianalytics.com/hc/en-us/articles/1500009515322-Install-the-Self-Service-Reporting-Module) add-on enable the **Active Query Builder** and **Metadata** elements in Logi Studio.

The Active Query Builder allows Analysis Grid users
to determine what dataset to work with, by giving them a way to
interactively select
tables and joins, at runtime.

The tables, views, columns, and relationships are available for use with the Active Query Builder are determined by building a "metadata file", associated with a Connection
element, which enumerates all of the database objects that will be
available to users for selection in the Analysis Grid. The Metadata
element provides a tool, the [Metadata Builder](https://devnet.logianalytics.com/hc/en-us/articles/1500009516142-Use-the-Metadata-Builder-Wizard) wizard, which is used during development to create the file.

The Metadata Builder wizard can create metadata files for Logi DataHub v3 dataviews.

![](https://devnet.logianalytics.com/hc/article_attachments/5160421354903/withinfo_03.png)

To do this, the Metadata element is added as child of the Connection.Logi DataHub v3 element in \_Settings, as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/5160432700439/withinfo_04.png)

The Metadata Builder wizard is then used, as shown above, to create the metadata file for the Logi DataHub v3 dataview.

![](https://devnet.logianalytics.com/hc/article_attachments/5160453600279/withinfo_05.png)

The Active Query Builder is then able to use the Logi DataHub v3 metadata and display it in the Analysis Grid interface, as shown above.
