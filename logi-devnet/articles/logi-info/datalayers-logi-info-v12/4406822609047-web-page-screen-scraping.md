---
title: "Web Page Screen Scraping"
id: 4406822609047
section: "Datalayers - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822609047-Web-Page-Screen-Scraping
updated_at: 2022-04-06T06:09:51Z
---

# Web Page Screen Scraping

# Web Page Screen Scraping

The **DataLayer.Web Scraper** element "scrapes", or
retrieves, content from *within* web pages and organizes it into the
row/column datasets usually found in datalayers. This provides an easy way
for developers to automate the collection and use of data published on
other web sites or in HTML files.

The following topics discuss techniques for
using the datalayer:

* [Using "Get XPaths" and Web Scraper Table](#GetXPath)
* [Using Web Scraper Rows and Web Scraper Column](#Working)

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) The linked topics illustrate techniques by referring to public
websites. While we make an effort to stay aware of them, these sites
may change their coding from time to time without our knowledge,
invalidating the actual data and values depicted, so you may not be able
to achieve the identical results. The techniques themselves, however,
remain valid.

## About "Web Page Scraping"

"Screen scraping" has been around for a long time; it's the
process of **extracting** data from the text on a
**display** screen, usually based on fields or screen regions. A key
issue is that the data is intended to be *viewed* and is therefore
neither documented nor structured for convenient parsing. In the age of
the Internet, the term has also come to apply to the same process with web
pages. In many cases, complicated parsing code is required.

However, the Logi approach makes the process fairly easy. Generally, in a
Logi application, the target HTML web page is **read** (the entire
page, not just the portion displayed), **transformed** into XML, and
then parsed based on **XPath** identifiers. Data formatted into tables,
and even in less-structured blocks of text, can readily be parsed and
served up to the report developer in the standard Logi datalayer
row/column structure. The data can then be further processed (filtered,
grouped, aggregated, etc.) using all the usual datalayer child elements.
This is all done using the **DataLayer.Web Scraper** element and its
child elements.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png)
The DataLayer.Web Scraper element is *not* available in Logi Java
applications.

For purposes of convenience, this topic refers to "HTML
files" but file extensions are not really important; if the file will
render to a web page, the datalayer will use it. Pages with .htm, .html,
xhtml, .mht and other extensions are all valid.

One of the keys to this process is specifying the XPath **parsing****identifiers** and DataLayer.Web Scraper provides a mechanism for
assisting developers in selecting them, as discussed in [Using "Get XPaths" and Web Scraper Table](https://devnet.logianalytics.com/hc/en-us/articles/4406818048535-Using-Get-XPaths-and-Web-Scraper-Table).
