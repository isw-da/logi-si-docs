---
title: "DataLayer.Data Services - Attributes"
id: 4406822247575
section: "Datalayers - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822247575-DataLayer-Data-Services-Attributes
updated_at: 2022-04-06T06:05:09Z
---

# DataLayer.Data Services - Attributes

# DataLayer.Data Services - Attributes

The DataLayer.Data Services element has the following attributes:

| Attribute | Description |
| --- | --- |
| Dataview ID | (Required) Specifies the ID of a Dataview definition, stored at the Logi Application Server, to be used to provide data for the datalayer. Once a Logi Application Service ID has been specified in the next attribute, the browse button in this attribute's value can be used to browse for available Dataviews. |
| Logi Application Service ID | (Required) Specifies the element ID of a **Connection.Logi Application Services** element in the \_Settings definition. |
| ID | Specifies a unique element ID. Providing a value here is *highly recommended* for easier identification of data when debugging. |
| Maximum Rows | The maximum number of rows to retrieve from the datasource, per request.  Default: *200 rows* or, if pagination is being used, *10 pages*, whichever is greater. |
