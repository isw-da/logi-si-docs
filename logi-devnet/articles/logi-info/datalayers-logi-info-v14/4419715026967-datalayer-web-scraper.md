---
title: "DataLayer.Web Scraper"
id: 4419715026967
section: "Datalayers - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715026967-DataLayer-Web-Scraper
updated_at: 2022-07-17T02:03:40Z
---

# DataLayer.Web Scraper

# DataLayer.Web Scraper

The **DataLayer.Web Scraper** element "scrapes", or retrieves, content from *within* web pages and organizes it into the row-column datasets usually found in datalayers. This topic discusses this datalayer.

The following sections are covered in this topic:

* Attributes
* [Working with DataLayer.Web Scraper](#Working)

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599319/criticalicon.png) The DataLayer.Web Scraper element is *not* available in Logi Java applications.
More information about this interesting element can be found in [Web Page Screen Scraping](https://devnet.logianalytics.com/hc/en-us/articles/4419707943703-Web-Page-Screen-Scraping).

## Attributes

The **DataLayer.Web Scraper** element has the following attributes:

| Attribute | Description |
| --- | --- |
| ID | Specifies an optional element ID. Recommended for easier identification when debugging. |
| Web Scraper URL | (Required) Specifies the address of the web page from which data will be retrieved; can be either an Internet HTTP address or a fully-qualified file path and name. A wide variety of file types are valid, including .htm, .html, .xhtml, and .mht, among others. |
| Get XPaths | (Development only) When this attribute is used, a document of the XML nodes on the target web page is created, for use as a reference during development, but data is not returned into the datalayer in an accessible form. If the attribute value is set to *All*, the document that's created lists all XML nodes in the target web page and includes the XPath strings that can be used to access each node. If set to a specific *XPath string*, the document that's created lists only the XML nodes in the web page that match that string. If left *blank*, no nodes document is created and data is returned into the datalayer; however either a **Web Scraper Rows** or **Web Scraper Table** element is required as a child of the datalayer for proper operation. |

  

## Working with DataLayer.Web Scraper

In most respects, **DataLayer.Web Scraper** functions exactly as other datalayer elements do and its data can be filtered and conditioned using appropriate elements. However, there is no need to use a Connection element in the \_Settings definition with this element*.* The DataLayer.Web Scraper element directly accesses the Internet or file system to read the specified web page or file.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706606743/dlwebscraper_01.png)

As shown above, a **DataLayer.Web Scraper** element is added as a child element to a Data Table or other data container element. Its attributes are set so that it accesses the desired web page or file.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599319/criticalicon.png) A **Web Scraper Rows** or **Web Scraper Table** (shown) child element must be used with this datalayer.

When using **Web Scraper Rows**, the rows of text identified will be retrieved into the datalayer and its columns will be named based on the element IDs of its child **Web Scraper Column** elements, which are used to identify individual nodes in the text rows.

When using **Web Scraper Table**, the rows of the table identified will be retrieved in the datalayer and the columns will be named based on the table column headers.

The datalayer reads and caches the data from the site or file. You can add child elements beneath the datalayer to affect its contents, including:

* **Filtering**: Sort, group, or restrict the data
* **Extending**: Add virtual columns to the datalayer that contain
  aggregated, calculated, or totaled data values
* **Securing**: Limit access to the data using Logi security
* **Linking**: Make the results reusable elsewhere in your report
  definitions

Data retrieved into the datalayer is cached in **XML** format, in memory and/or on the web server's file system. The latter is discussed in [The Logi Server Engine](https://devnet.logianalytics.com/hc/en-us/articles/4419715421975-The-Logi-Server-Engine) and may be of interest to developers working with extremely large datasets or large numbers of concurrent users.

The data read with the datalayer is available using **@Data****tokens**,
in the format @Data.*ColumnName*~. The spelling of the column name is
*case-sensitive*. The data is only available within the scope of the
parent element of the datalayer, not throughout the entire report
definition. The **DataLayer.Linked** element can be used to make the data reusable
in another datalayer outside this scope.

The following three paragraphs *do not apply* if you're using the **Get XPaths** attribute to create a XML nodes reference document:
The [Auto Columns](https://devnet.logianalytics.com/hc/en-us/articles/4419700048023-Auto-Columns)
element can be used to quickly display in your report all the data in a
datalayer.
The data retrieved into the datalayer can be viewed by turning on the
Debugger Link in your \_settings definition (General element) and using
the resulting iconat the bottom of your report page to view the Debugger Trace Page. A link on the trace page will display the retrieved data.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699507735/dlwebscraper_02.png)

Studio includes a wizard that will add elements for the columns in the datalayer to your definition. You can select the desired columns before the operation begins. With the datalayer's parent **Data Table** or similar element selected in the Definition Editor, click the wizard link, shown above, in the Element Toolbox.
