---
title: "Retrieving Data from HP Vertica"
id: 4419723324439
section: "Connect to Data - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723324439-Retrieving-Data-from-HP-Vertica
updated_at: 2022-07-17T01:28:46Z
---

# Retrieving Data from HP Vertica

# Retrieving Data from HP Vertica

You can use DataLayer.SQL to retrieve data from Vertica but, for best performance with very large datasets, we recommend the use of [DataLayer.ActiveSQL](https://devnet.logianalytics.com/hc/en-us/articles/4419722806807-DataLayer-ActiveSQL).

![](https://devnet.logianalytics.com/hc/article_attachments/4419707199127/workvertica_04.png)

Vertica uses **HP Vertica SQL** which is based on standard SQL syntax but has a number of very important differences that you should be aware of as you create your queries. Please refer to the [HP Vertica SQL Reference](https://www.vertica.com/docs/9.2.x/HTML/Content/Authoring/SQLReferenceManual/SQLReferenceManual.htm) for more information. After the data is retrieved, you may condition, filter, and shape it just as you would any other datalayer data.

## Using the Active Query Builder and Connection-Related Metadata

When using an Analysis Grid with the **Active Query Builder**, users can select the tables and Joins to be used for analyses at runtime. To facilitate this, developers need to create and specify the metadata files to be used. [Web Metadata Builder](https://devnet.logianalytics.com/hc/en-us/articles/4419723223063-Web-Metadata-Builder) provides information about creating these files.

![](https://devnet.logianalytics.com/hc/article_attachments/4419700012951/workvertica_05.png)

To specify the metadata files to be used with a Connection.Vertica element, add one or more child **Metadata** elements beneath it, as shown above. This element's attributes identify the metadata file and the name for it that will appear in the Active Query Builder interface.
