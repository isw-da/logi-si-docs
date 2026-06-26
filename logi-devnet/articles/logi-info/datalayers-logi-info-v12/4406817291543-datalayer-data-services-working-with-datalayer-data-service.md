---
title: "DataLayer.Data Services - Working with DataLayer.Data Service"
id: 4406817291543
section: "Datalayers - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817291543-DataLayer-Data-Services-Working-with-DataLayer-Data-Service
updated_at: 2022-04-06T06:05:13Z
---

# DataLayer.Data Services - Working with DataLayer.Data Service

# DataLayer.Data Services - Working with DataLayer.Data Service

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) The data-related elements discussed here are available in Logi Info v12.5 but have been deprecated in later Info versions; consult the [Release Notes](https://clm.logianalytics.com/rdPage.aspx?rdReport=RelNotesINF) for specific details.

Like other datalayers, DataLayer.Data Services has a few standard child elements that can be used to shape the retrieved data. In addition, it has some special "Ds" child elements (discussed below) that developers can use to augment the Dataview when it's executed. However, other child elements for linking datalayers and formatting or transforming the data are not available.

The data retrieved is available using @Data tokens, in the format @Data.*ColumnName*~. The spelling of the column name is *case-sensitive*. The data is only available within the scope of its parent element, not throughout the entire report definition.

The data retrieved into the datalayer can be viewed by turning on debugging in Logi Studio and using the resulting link at the bottom of your report page to view the Debugger Trace page, see [Debug Reports](https://devnet.logianalytics.com/hc/en-us/articles/4406817355543-Debug-Reports). You'll be able to see the XML data retrieved.
