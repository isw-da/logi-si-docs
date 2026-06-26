---
title: "Paginate Data and Print Reports"
id: 4419715427223
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715427223-Paginate-Data-and-Print-Reports
updated_at: 2022-07-17T02:23:47Z
---

# Paginate Data and Print Reports

# Paginate Data and Print Reports

The volume of data retrieved into Logi reports often requires that tables be presented as a series of pages; in addition, developers often need to offer the ability to print hard copy versions of reports with suitable headers.

The following topics introduce developers to techniques for satisfying both of these requirements:

* [Interactive Paging Element Attributes](https://devnet.logianalytics.com/hc/en-us/articles/4419707768855-Interactive-Paging-Element-Attributes#Attributes)
* [Pagination Usage Examples](https://devnet.logianalytics.com/hc/en-us/articles/4419715428119-Pagination-Usage-Examples#Examples)
* [Page Navigation using URL](https://devnet.logianalytics.com/hc/en-us/articles/4419723104279-Page-Navigation-Using-URL#URL)
* [Creating Printable Reports](https://devnet.logianalytics.com/hc/en-us/articles/4419707767831-Creating-Printable-Reports#Printable)

## About Pagination

Large Data Tables, with hundreds of rows of data, are cumbersome to interact with in a browser-based environment. The concept of navigating through a lot of data using "pages", each with a small number of rows, is familiar to anyone who's used an Internet search engine and looked through the search results. Logi reporting tools include the **Interactive Paging** element which provides this functionality for Data Tables in Logi applications.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) We *do not* recommend using Interactive Paging with tables that contain user input elements in each row.

The examples below show four different styles and locations for page navigation links, all of which are created using the Interactive Paging element. The left two examples use Text-type links and the right two use Image-type links:

![](https://devnet.logianalytics.com/hc/article_attachments/7522806928663/paginate_01_789x339.png)

Studio includes a wizard that will add an Interactive Paging element to a report definition and configure it, using the Image-type links shown in the upper-right hand corner of the previous examples.

To use it, select the desired **Data Table element**, right-click it and select **Element Wizards.** Then, select **Add Interactive Paging Controls**, as shown below:

![](https://devnet.logianalytics.com/hc/article_attachments/7522792046999/paginate_02_729x527.png)

The Interactive Paging element can, of course, be added and configured manually as well.

![](https://devnet.logianalytics.com/hc/article_attachments/7522821196823/paginate_03_858x276.png)

The resulting element is inserted beneath the selected Data Table, as shown above, with its attributes configured by the wizard.
For more information, see [Paginate Data and Print Reports](#).
