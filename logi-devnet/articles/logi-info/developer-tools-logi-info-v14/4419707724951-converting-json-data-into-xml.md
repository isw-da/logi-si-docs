---
title: "Converting JSON Data into XML"
id: 4419707724951
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707724951-Converting-JSON-Data-into-XML
updated_at: 2022-07-17T01:42:42Z
---

# Converting JSON Data into XML

# Converting JSON Data into XML

[Converting XML into JSON Data](https://devnet.logianalytics.com/hc/en-us/articles/4419723055383-Converting-XML-into-JSON-Data) demonstrated how XML data retrieved into a datalayer could be converted into JSON data for use with jQuery components that work with that data. This topic describes the reverse: how to retrieve JSON data and turn it into XML data for use with Logi elements.

This example gets a weather forecast from Yahoo in JSON format, using a special datalayer, **DataLayer.JSON File**, and converts it to regular Logi XML data.

Start this example by setting the **Style** element to one of the standard Logi Analytics Themes, but don't use a style sheet. You won't need to include any script files, either.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714850327/jquery_16.png)

Add a **Data Table** element and set its attributes as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706970391/jquery_17.png)

Next, add a **DataLayer.JSON File** element beneath the Data Table, as shown above. Here's the complete value to use for its **Json File** attribute value:

http://query.yahooapis.com/v1/public/yql?q=select%20item%20from%20weather.forecast%20where%20location%3D%2222102%22&format=json

This may wrap in your browser, but it's all one line. ![](https://devnet.logianalytics.com/hc/article_attachments/4419706599575/noteicon.png) The highlighted bit is a U. S. postal Zip Code, which determines the forecast location.

The Json File attribute value can be either a fully-qualified file path and name or a URL. By default, the server will look in the app's
\_SupportFiles folder, in which case you can simply specify the filename (such as
mydata.js).

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599575/noteicon.png) We're also using XPATH to extract the data we want from the returned data. You may want to turn on debug and look at the data in the various stages of processing.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714850583/jquery_18.png)

Next, add a **Data Table Column** element and set its attributes as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714850839/jquery_19.png)

Followed by a **Label** element to display the data, as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699832855/jquery_20.png)

Finish by adding another Data Table Column and Label combination. Set the Data Table Column element's **Class** attribute to *ThemeAlignTop* as before but leave its **Width** and **Width Scale** attributes blank. Set the Label attributes as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699833239/jquery_21.png)

If you Preview the report now, you'll see the local forecast for the specified zip code, which might look like the example above.

In summary, we've seen how jQuery can be used in Logi report definitions, how XML data can be included as JSON data, and how JSON data can be converted to XML for use with Logi elements. A final, important reminder: jQuery, like all JavaScript, is *case-sensitive* and you can head off many errors by paying strict attention to case.
