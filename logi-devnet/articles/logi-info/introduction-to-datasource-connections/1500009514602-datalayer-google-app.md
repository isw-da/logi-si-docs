---
title: "DataLayer.Google App"
id: 1500009514602
section: "Introduction to Datasource Connections"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009514602-DataLayer-Google-App
updated_at: 2021-06-17T01:58:10Z
---

# DataLayer.Google App

# DataLayer.Google App

The **Google App****Engine** lets developers run their web applications on Google's
infrastructure. App Engine applications are easy to build, easy to maintain, and
easy to scale as traffic and data storage needs grow. The Logi **DataLayer.Google App** datalayer enables connection to the datastore of a published application hosted by the Google App Engine. This topic discusses the datalayer.

* Attributes
* [Add Logi Python File to Your Google Application](#LogiPyFile)
* [Work with DataLayer.Google App](#WorkingWith)
* [A Simple Example](#Example)

## Attributes

The **DataLayer.Google App** element has the following attributes:

| Attribute | Description |
| --- | --- |
| ID | (Required through v10.1.46) A unique element ID. |
| Google App Entity | (Required): The name of the data entity (also called "kind" or "model") desired. This value is case-sensitive. |
| Google App Module | (Required): The name of the Python source code in the Google App which contains the class defining the data entity specified in Google App Entity. |
| Google App URL | (Required): The web address of the Google App.  Example: http://mydemoapp.appspot.com |
| Google App Filter | A filter that can be used to restrict the data that's returned. Examples:  State = 'Virginia' Level = 2 AND Country = 'France' Color IN ('red', 'blue') |
| Google App ID Field | The name of a data model property that is unique for each entity. This field is used to build a complete set of data from multiple queries when the datastore is too large for a single query. |
| Google App Limit | The maximum number of entities to request per query, up to 1000. Reducing this limit can help if a query times out. Default and maximum value: *1000*. |

## Add the Logi Python File to Your Google Application

In order to enable your Google App Engine application to provide the appropriate response to the Logi datalayer element, you must include a **special Python file** in your Google application. [Open this file](https://devnet.logianalytics.com/Downloads/logi.py.txt) and save it, using the file name "logi.py", to the root folder of your Google application. Your Logi application will call functions in this file, which run on Google, in order to retrieve data (the Logi Engine itself
does not run Python scripts).

## Work with DataLayer.Google App

Detailed information about the Google App Engine referenced here can be found at the [Google App Engine](http://code.google.com/appengine/docs/whatisgoogleappengine.html) web site.

Unlike most datalayers, **DataLayer.Google App**, does not require a separate connection with the Google web service. Therefore, there is no related Connection element that must be used.

The data retrieved with a datalayer is available using @Data **tokens**, in the format @Data.*ColumnName*~. The spelling of the column name is **case-sensitive**. The data is only available within the **scope** of the **parent** element of the datalayer, not throughout the entire report definition. The DataLayer.Linked element can be used to make the data reusable in another datalayer outside this scope.

Logi Info developers can make use of the **AutoColumns** element to quickly see which "column names" are being returned by the web service.

Developers can also view the data retrieved into the datalayer by turning on the **Debugging Link** in their \_settings definition (General element) and using the resulting link at the bottom of the report page to view the **Application Trace** page. A link on the Trace page will display the retrieved data.

*![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif)  Developers should be aware that they need to take appropriate security precautions and use the account facilities available in the Google App Engine service to ensure that their data is secured.*

## A Simple Example

The following example demonstrates how the **DataLayer.Google App** element can be used.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771867927/datalayergapp_01.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771868183/datalayergapp_01a.png)

The example definition shown above includes a **Data Table** and a **DataLayer.Google App** element. The datalayer's attributes are set as shown.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778703383/datalayergapp_02.png)

The screenshot of the resulting **Logi application table**, above, shows the data from the worksheet being used in the sample application.
