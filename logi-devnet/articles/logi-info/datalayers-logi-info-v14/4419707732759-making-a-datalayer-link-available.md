---
title: "Making a DataLayer Link Available"
id: 4419707732759
section: "Datalayers - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707732759-Making-a-DataLayer-Link-Available
updated_at: 2022-09-02T15:56:10Z
---

# Making a DataLayer Link Available

# Making a DataLayer Link Available

The following example illustrates how to make the data in a datalayer re-usable:

![](https://devnet.logianalytics.com/hc/article_attachments/4419714858007/dllinked_01.png)

1. As shown above, the example definition contains an **Input Select List** and **DataLayer.SQL** elements. The datalayer uses a regular SQL query to retrieve data from the database to present as options in aselection list.
2. Beneath the datalayer, a **Data Layer Link** element has been added. The effect of the element is to "save" a copy of the data for future use. ![](https://devnet.logianalytics.com/hc/article_attachments/4419706599319/criticalicon.png) You *must* give the element a *unique* ID.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699840919/dllinked_02.png)

If you use elements to filter, sort, and otherwise manipulate the data in the datalayer, then the *position*of the Data Layer Link element in the element tree is significant. For example, above left, the *raw* data, as it was retrieved from the database, will be available for re-use. But, above right, because the link comes after (below) the other elements,
the *filtered* and *sorted* data will be available.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699841175/dllinked_03.png)

You can even use *multiple* Data Layer Link elements beneath a datalayer. In the example above, *both* the raw and the filtered, sorted data would be available for re-use, for different consumers.

The data in the datalayer is now available for re-use, saving us the performance load of running one or more queries later in our application.
