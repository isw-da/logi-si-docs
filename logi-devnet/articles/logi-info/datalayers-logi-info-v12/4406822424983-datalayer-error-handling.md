---
title: "Datalayer Error Handling"
id: 4406822424983
section: "Datalayers - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822424983-Datalayer-Error-Handling
updated_at: 2022-10-28T16:20:04Z
---

# Datalayer Error Handling

# Datalayer Error Handling

The **If Data Error** element allows developers to handle errors, such as a failure to find or connect to data sources, or missing or corrupt data files, that may occur while retrieving data into a datalayer. In this way, errors are trapped and processing can be switched to alternate data sources, instead of displaying the system error page.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563171991/introdl_06a.png)

Consider the example shown above. A Data Table normally uses a Web Service to retrieve the latest currency conversion information. However, if there is some problem with the web service and an error occurs, the If Data Element allows the datasource to switch to an XML data file. In this way, data is still presented and an error page is not displayed.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583822999/introdl_06b.png)

What about any data manipulation elements that may exist? As shown above, when an error occurs, the alternate datalayer replaces the original datalayer as the data retrieval mechanism and applies its own data manipulation elements. Then the application will process any data manipulation elements for the original datalayer.

You may use multiple, nested If Data Error elements. The Debugger Trace page will include an entry containing the actual error message and any details generated each time an If Data Error element is processed. The @Function.ErrorDataLayerID~ token can be used to determine the element ID of the datalayer that encountered the error.
