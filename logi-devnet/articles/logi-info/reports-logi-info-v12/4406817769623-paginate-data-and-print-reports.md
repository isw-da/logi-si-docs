---
title: "Paginate Data and Print Reports"
id: 4406817769623
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817769623-Paginate-Data-and-Print-Reports
updated_at: 2022-04-06T06:08:04Z
---

# Paginate Data and Print Reports

# Paginate Data and Print Reports

The volume of data retrieved into Logi reports often requires that tables be presented as a series of **pages**; in addition, developers often need to offer the ability to **print** hard copy versions of reports with suitable headers.

The following topics introduce developers to techniques for satisfying both of these requirements:

* [Interactive Paging Element Attributes](https://devnet.logianalytics.com/hc/en-us/articles/4406822469399-Interactive-Paging-Element-Attributes#Attributes)
* [Pagination Usage Examples](https://devnet.logianalytics.com/hc/en-us/articles/4406817770647-Pagination-Usage-Examples#Examples)
* [Page Navigation using URL](https://devnet.logianalytics.com/hc/en-us/articles/4406822470295-Page-Navigation-Using-URL#URL)
* [Creating Printable Reports](https://devnet.logianalytics.com/hc/en-us/articles/4406817768087-Creating-Printable-Reports#Printable)

## About Pagination

Large data tables, with hundreds of rows of data, are cumbersome to interact with in a browser-based environment. The concept of navigating through a lot of data using "pages", each with a small number of rows, is familiar to anyone who's used an Internet search engine and looked through the search results. Logi reporting tools include the **Interactive Paging** element which provides this functionality for data tables in Logi applications.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) We *do not* recommend using Interactive Paging with tables that contain user input elements in each row.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583782167/paginate_01_558x240.png)

The examples above show four different styles and locations for page navigation links, all of which are created using the Interactive Paging element. The left two examples use Text-type links and the right two use Image-type links.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563131543/paginate_02_464x336.png)

Studio includes a wizard that will add an Interactive Paging element to a report definition and configure it, using the Image-type links shown in the upper-right hand corner of the previous examples. To use it, select the desired data table element, right-click it and select "Element Wizards", then select "Add Interactive Paging Controls", as shown above. The Interactive Paging element can, of course, be added and configured manually as well.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583782679/paginate_03_634x205.png)

The resulting element is inserted beneath the selected data table, as shown above, with its attributes configured by the wizard.
