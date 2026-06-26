---
title: "Exporting to XML"
id: 4406817449367
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817449367-Exporting-to-XML
updated_at: 2022-04-06T06:06:08Z
---

# Exporting to XML

# Exporting to XML

Data stored in the Extensible Markup Language (XML) format allows information systems to share structured data and is a widely-accepted method of storing and transferring data. Logi products use XML files as temporary caches for a variety of purposes and can export Logi report data to XML files.

The following topics discuss techniques for exporting to XML:

* [Exporting Data Manually](https://devnet.logianalytics.com/hc/en-us/articles/4406822326679-XML-Exporting-Data-Manually#Manually)
* [Exporting Data Automatically](https://devnet.logianalytics.com/hc/en-us/articles/4406817447959-XML-Exporting-Data-Automatically#Automatically)
* [Saving Other Data as XML Data](https://devnet.logianalytics.com/hc/en-us/articles/4406817450519-XML-Saving-Other-Data-as-XML-Data#Saving)
* [Export to XML Considerations](https://devnet.logianalytics.com/hc/en-us/articles/4406822327575-XML-Export-to-XML-Considerations#Considerations)

## About Exporting Data to XML

The XML data format is useful because of its relative simplicity and general cross-platform accessibility. XML files are simple text files that can be used to store a variety of data. In the schema used by Logi Info for tabular data, an XML element set represents one data record, each column is identified by an XML attribute name, and its data is the attribute value.
Logi Studio provides **Export XML** elements that make it easy to export Logi report data into XML
files.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583940119/exportxml_01.png)

The example above shows report data that has been exported into an XML data file. Note the formatting of the highlighted DateTime data: it's in the **ISO 8601** format. Record 1 of the dataset is everything between the first <dtOrders and />.
You can give users the ability to export a data *manually* via user interaction at runtime or choose to *automate* the export process based on an event or schedule. Manual exports are configured within **Report** definitions and automated exports are configured within **Process** definitions.
