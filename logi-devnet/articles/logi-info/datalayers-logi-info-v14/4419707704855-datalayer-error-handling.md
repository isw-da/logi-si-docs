---
title: "Datalayer Error Handling"
id: 4419707704855
section: "Datalayers - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707704855-Datalayer-Error-Handling
updated_at: 2022-07-17T02:24:02Z
---

# Datalayer Error Handling

# Datalayer Error Handling

The **If Data Error** element allows developers to handle errors, such as a failure to find or connect to data sources, or missing or corrupt data files, that may occur while retrieving data into a datalayer. In this way, errors are trapped and processing can be switched to alternate data sources, instead of displaying the system error page.

![](https://devnet.logianalytics.com/hc/article_attachments/7522839238039/introdl_06a.png)

Consider the example shown above. A Data Table normally uses a Web Service to retrieve the latest currency conversion information. However, if there is some problem with the web service and an error occurs, the If Data Element allows the datasource to switch to an XML data file. In this way, data is still presented and an error page is not displayed.

![](https://devnet.logianalytics.com/hc/article_attachments/7522812159383/introdl_06b.png)

What about any data manipulation elements that may exist? As shown above, when an error occurs, the alternate datalayer replaces the original datalayer as the data retrieval mechanism and applies its own data manipulation elements. Then the application will process any data manipulation elements for the original datalayer.

You may use multiple, nested 'If Data Error' elements. The Debugger Trace page will include an entry containing the actual error message and any details generated each time an If Data Error element is processed. The @Function.ErrorDataLayerID~ token can be used to determine the element ID of the datalayer that encountered the error.

![](https://devnet.logianalytics.com/hc/article_attachments/7522745474327/_newplus.jpg) New for 14.1 You can also retrieve Data Table and Data Chart error messages using the 'If Data Error' element and capture all of the error information in the new token element, @DataLayerError.

To utilize this feature, add the 'If Data Error' element to your datalayer and configure the @DataLayerError token using your datalayer ID:

![](https://devnet.logianalytics.com/hc/article_attachments/7522804940823/image-20220118-194520_1152x533.png)

Depending on the information you want to display on the page, you can choose from the following tokens:

* ErrorMessage~
* Restful data source only: rdHttpResponseBodyContent~
* Restful data source only: rdHttpResponseBodyCode~
* Restful data source only: rdHttpResponseDescription~

As a result, your error page will resemble the following:

![](https://devnet.logianalytics.com/hc/article_attachments/7522768952471/image-20220118-195952_1599x128.png)

![](https://devnet.logianalytics.com/hc/article_attachments/7522755629847/noteicon.jpg)Use divisions to customize the error message to include images, buttons, and links.
