---
title: "DataLayer.Google App - Attributes"
id: 4419707485975
section: "Datalayers - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707485975-DataLayer-Google-App-Attributes
updated_at: 2022-07-17T01:53:38Z
---

# DataLayer.Google App - Attributes

# DataLayer.Google App - Attributes

The DataLayer.Google App element has the following attributes:

| Attribute | Description |
| --- | --- |
| Google App Entity | (Required): The name of the data entity (also called "kind" or "model") desired. This value is case-sensitive. |
| Google App Module | (Required): The name of the Python source code in the Google App which contains the class defining the data entity specified in Google App Entity. |
| Google App URL | (Required): The web address of the Google App.  Example: http://mydemoapp.appspot.com |
| Google App Filter | A filter that can be used to restrict the data that's returned. Examples:  State = 'Virginia' Level = 2 AND Country = 'France' Color IN ('red', 'blue') |
| Google App ID Field | The name of a data model property that is unique for each entity. This field is used to build a complete set of data from multiple queries when the datastore is too large for a single query. |
| Google App Limit | The maximum number of entities to request per query, up to 1000. Reducing this limit can help if a query times out. Default and maximum value: *1000*. |
| ID | An optional, unique element ID. Recommended for easier identification when debugging. |
