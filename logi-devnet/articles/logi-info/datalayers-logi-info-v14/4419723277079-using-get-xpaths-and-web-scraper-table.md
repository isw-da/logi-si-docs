---
title: "Using \"Get XPaths\" and Web Scraper Table"
id: 4419723277079
section: "Datalayers - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723277079-Using-Get-XPaths-and-Web-Scraper-Table
updated_at: 2022-07-17T01:30:38Z
---

# Using "Get XPaths" and Web Scraper Table

# Using "Get XPaths" and Web Scraper Table

The DataLayer.Web Scraper element has an attribute named
**Get XPaths**. During development, when this attribute is used, the
target HTML page is read and transformed into XML, then a
**reference document** is created that lists all of the XPath
identifiers and their values. Looking through this topic, the developer
can quickly see, for example, the XPath tag name for a table with the
desired data.

![](https://devnet.logianalytics.com/hc/article_attachments/4419707158423/webpgscraper_01_754x392.png)

The example above shows part of the U.S. State Department web site page
that publishes per diem rates. The following example shows how to use
DataLayer.Web Scraper to get the XPath tags needed to parse this page.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699976855/webpgscraper_02.png)

As shown above, add a **Data Table** element with a
**DataLayer.Web Scraper** child element the report definition. Set the
datalayer's **Web Scraper URL** attribute value to the URL of the
target web page:

http://aoprals.state.gov/web920/per\_diem\_action.asp?MenuHide=1&CountryCode=1089  

and set its **Get XPaths** attribute to *All*, which causes the
development reference document to be created.

![](https://devnet.logianalytics.com/hc/article_attachments/4419707158679/webpgscraper_03.png)

Preview the report in Studio, and examine the XML nodes reference
document, shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699977111/webpgscraper_04.png)

Locate the desired nodes by **filtering** out everything else, in this
case everything*except* tables. To do this, go back to viewing
the definition and enter
//table
into the **Get XPaths** attribute and then preview the definition
again. Look through the Values column: tables are identified by their
*headings*, not their row data, so the target table has to have
distinctive headings. The table we want is shown above highlighted.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714956183/webpgscraper_05.png)

Next find, select, and copy the table's entire**XPath by Tag Name** value, highlighted above.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699977367/webpgscraper_06.png)

Next, back in the definition, clear the datalayer's
**Get XPath** attribute value. Then add a
**Web Scraper Table** child element beneath the datalayer and paster
the XML tag copied from the reference document into its
**Web Scraper XPath** attribute, as shown above, right. The complete
value is:

/html/body/div/table/tr/td[3]/table/tr[2]/td/div/form/table[2]  

And also set the **Column Names In First Row** attribute value to
*True*.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714956439/webpgscraper_07.png)

Finally, as shown above, add **Data Table Column** and
**Label** elements to display the data:The **column names** in the
datalayer, for use with @Data tokens, are the names seen in the XPath
reference document values, with any embedded spaces removed. In this
example, that's CountryName, PostName, SeasonBegin, SeasonEnd, etc.

![](https://devnet.logianalytics.com/hc/article_attachments/4419707158935/webpgscraper_08.png)

When previewed, as shown above, the report display the table with the
desired data from the target web site.
