---
title: "XML - Saving Other Data as XML Data"
id: 4406817450519
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817450519-XML-Saving-Other-Data-as-XML-Data
updated_at: 2022-04-06T06:06:10Z
---

# XML - Saving Other Data as XML Data

# XML - Saving Other Data as XML Data

There are situations in which you may, during development, want to *capture data* from a SQL database or other data source and save it as XML data.
For example, it may be desirable to create an XML data file of country names, postal codes, or other static data to be used in an application. Or, it may be useful to work with XML data, without the need for a live database connection.
Logi reporting products make it very easy to do this, following these steps:

1. Turn on debugging, using the Debug icon in Studio's toolbar or by configuring your application's \_Settings definition, **General** element's **Debugger Style** attribute to *DebuggingLinks* and saving the definition.
2. Run the Logi report that retrieves the desired SQL data or data from another datasource.
3. Click the debug link or icon at the bottom of the report page.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563292311/exportxml_06.png)

4. As shown above, find the *View File Stream Data* link in the Debugger Trace Report page and click it. This should open the XML in the datalayer in your browser in a data table.
5. Click the *View raw XML* link to view the formatted XML data by itself.
6. Right-click in the browser and select *View Source*. This should open the data in **Notepad** or some other text editor.
7. Save the data in the text editor to a file with an .xml extension.

The data is now ready to be used with Logi applications and can be retrieved using DataLayer.XML.
