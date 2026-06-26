---
title: "DataLayer.SP - Attributes"
id: 4406817318295
section: "Datalayers - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817318295-DataLayer-SP-Attributes
updated_at: 2022-04-06T06:05:23Z
---

# DataLayer.SP - Attributes

# DataLayer.SP - Attributes

The DataLayer.SP element has the following attributes:

| Attribute | Description |
| --- | --- |
| Command | (Required) Specifies the **name** of the stored procedure (i.e. the name called to execute it). |
| Connection ID | Specifies the ID of a Connection element defined in the \_Settings definition. If left *blank*, the datalayer will use the first connection in the \_Settings definition. For clarity, developers are advised to enter an ID here in all cases. |
| ID | Specifies a unique element ID. Providing a value here is *highly recommended* for easier identification of data when debugging. |
| Maximum Rows | Specifies the maximum number of results rows to retrieve. Default: *no limit*. |
