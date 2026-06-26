---
title: "DataLayer.Google App - Working with DataLayer.Google App"
id: 4419707487895
section: "Datalayers - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707487895-DataLayer-Google-App-Working-with-DataLayer-Google-App
updated_at: 2022-07-17T01:53:35Z
---

# DataLayer.Google App - Working with DataLayer.Google App

# DataLayer.Google App - Working with DataLayer.Google App

Detailed information about the Google App Engine referenced here can be found at the [Google App Engine](https://cloud.google.com/appengine/docs/whatisgoogleappengine?csw=1) web site.

Unlike most datalayers, **DataLayer.Google App**, does not require a separate connection with the Google web service. Therefore, there is no related Connection element that must be used.

The data retrieved with a datalayer is available using @Data **tokens**, in the format @Data.*ColumnName*~. The spelling of the column name is **case-sensitive**. The data is only available within the **scope** of the **parent** element of the datalayer, not throughout the entire report definition. The DataLayer.Linked element can be used to make the data reusable in another datalayer outside this scope.

The [Auto Columns](https://devnet.logianalytics.com/hc/en-us/articles/4419700048023-Auto-Columns) element can be used to quickly see which "column names" are being returned by the web service.

You can also view the data retrieved into the datalayer by turning on the **Debugging Link** in their \_settings definition (General element) and using the resulting link at the bottom of the report page to view the **Application Trace** page. A link on the Trace page will display the retrieved data.

*![](https://devnet.logianalytics.com/hc/article_attachments/4419706599319/criticalicon.png)Take appropriate security precautions and use the account facilities available in the Google App Engine service to ensure that your data is secured.*
