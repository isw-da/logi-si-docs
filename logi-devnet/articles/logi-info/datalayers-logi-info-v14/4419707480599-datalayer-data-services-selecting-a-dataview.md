---
title: "DataLayer.Data Services - Selecting a Dataview"
id: 4419707480599
section: "Datalayers - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707480599-DataLayer-Data-Services-Selecting-a-Dataview
updated_at: 2022-07-17T01:53:51Z
---

# DataLayer.Data Services - Selecting a Dataview

# DataLayer.Data Services - Selecting a Dataview

The following assumes that you've already added and configured a Connection.Logi Application Services element in \_Settings and have used Logi Studio's Dataview Authoring tool to create at least one Dataview.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714716951/dlds_01.png)

As shown above, add a DataLayer.Data Services element beneath the table or visualization of your choice and configure the **Logi Application Service ID** with the ID of your Connection element. Click the browse button at the end of the **Dataview ID** attribute.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706744983/dlds_02.png)

The Dataview Selector dialog box will appear in Studio, displaying a searchable list of available Dataviews. Click the **Select** button of the desired Dataview.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714717207/dlds_03.png)

The dialog box will close and the GUID of the selected Dataview will be automatically copied into the datalayer's Dataview ID attribute, as shown above. To select a different Dataview, just repeat the process.
