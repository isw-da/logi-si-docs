---
title: "Creating Crosstab Tables Manually"
id: 4419707443735
section: "Use Dashboards & Visuals - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707443735-Creating-Crosstab-Tables-Manually
updated_at: 2022-07-17T02:24:48Z
---

# Creating Crosstab Tables Manually

# Creating Crosstab Tables Manually

You can create a Crosstab Table in Logi Studio manually by adding the appropriate elements to a report definition. Every Crosstab Table uses the following minimum components:

![](https://devnet.logianalytics.com/hc/article_attachments/7522831320215/xtabtable_05.png)

* One **Crosstab Table** element
* One or more **DataLayer** elements with a **Crosstab Filter** element to retrieve and shape the data
* One or more **Crosstab Table Label Column** elements to display the Label column data
* One or more **Crosstab Table Value Columns** element to display the Value column data

The elements above define the most basic Crosstab Table. Other elements, such as **Condition Filters**, **Sort Filters**, and **Calculated Columns**, can be used to manipulate the data in the datalayer in the same way they would be used for any Data Table or chart.

If you use a **Sort Filter** beneath your datalayer, its effect on the table display may be different depending on its placement *before* (above) or *after* (below) the Crosstab Filter element. This is particularly relevant if your data returns some zero values, and you may want to experiment with this element in different locations in your definition.

The Crosstab Table Label Column element includes the **Scope Row Header** attribute. When set to *True*, the HTML output for data cells will be modified to improve Section 508 accessibility, creating a column which includes header information for each row, changing the <TD> tags to <TH Scope="Row"> tags.

A number of elements that are available for use with regular Data Tables, such as **Header Row**, **Interactive Paging**, and **More Info Row**, can also be used with Crosstab Tables. For information about using these elements, see [Data Tables](https://devnet.logianalytics.com/hc/en-us/articles/4419707469719-Data-Tables).

![](https://devnet.logianalytics.com/hc/article_attachments/7522745474327/_newplus.jpg) New for 14.1 Adding "HTML Attribute Params" to your Crosstab Table enables you to apply your application to work with other frameworks or libraries easier. Depending on the type of HTML Attribute Params you add, there will be different parameters available to use, or you can define your own parameters. If an attribute was set in both Element and HTML Attribute Params, the one set in the HTML Attribute Params will be ignored.
