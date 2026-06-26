---
title: "Filtering Data on Load"
id: 4406640366871
section: "Using DataHub v2.2 With Logi Info"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406640366871-Filtering-Data-on-Load
updated_at: 2022-04-01T03:13:24Z
---

# Filtering Data on Load

# Filtering Data on Load

Logi DataHub lets you filter data loaded into Dataviews by specifying filtering criteria for data sources. This topic discusses the filtering criteria configuration.

* [About Filters and Data Caching](#About)
* [Create a Filter Expression](#Expression)
* [Filter Syntax Usage Notes](#Notes)

## About Filters and Data Caching

When using filtering, questions sometimes arise about the load times and statuses indicated in DataHub. Here's an explanation of the data caching scheme and how filtering affects it:

When a Dataview ("A") is created, the data necessary for it is downloaded and cached by DataHub. If another Dataview ("B") is created that happens to use the exact same data, then it's pointed to the existing, cached data downloaded for "A". This improves performance and saves storage space.

However, when a Dataview ("C") is subsequently created with a filter, the filtered data is downloaded and cached separately because it does not exactly match the existing cached data for "A". Then if another Dataview is created that uses filtering identical to that of "C", it will use the cached, filtered data download for "C".

## Create a Filter Expression

Filtering essentially adds a standard ANSI SQL-92 "WHERE" clause to the query used to download data. Therefore, filtering is only available for the supported database and Salesforce data providers.

Access to the filtering options is available on a Dataview's page, in its Dataview Configuration tab:

![](https://devnet.logianalytics.com/hc/article_attachments/5160463787671/filterload_01.png)

Click the Filter icon, shown circled above, to specify the filter criteria for that
Object. If a filter already exists for an object, the filter icon will appear "filled in", as shown above for the Orders object. If there is no icon, then filtering is not supported.

Clicking the icon will display the Filter Criteria dialog box:

![](https://devnet.logianalytics.com/hc/article_attachments/5160434255511/filterload_02.png)

If the filter already exists, its filter expression will be loaded into the dialog box, as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/5160463023255/criticalicon.png) Do not surround your expression with double-quotes, as suggested by the example in the dialog box.

If you try to modify the filter expression for an object that's already been used in a Dataview, a warning message will be displayed.

## Filter Syntax Usage Notes

The Filter Criteria dialog box lets you specify the expression that will be part of the WHERE clause in the query DataHub issues to the data source.

![](https://devnet.logianalytics.com/hc/article_attachments/5160463023255/criticalicon.png) Do not include the SQL reserved word "WHERE" in your filter expression.

The query syntax conforms to ANSI-92 PostgreSQL syntax. There are numerous references on the Internet for PostgreSQL-style WHERE clauses. Here's the general syntax for the WHERE clause issued by DataHub:

WHERE *exp* AND|OR *exp* AND|OR *exp*...

where *exp* can be one of the following:

[column] = value  
[column] = value OR [column] = value  
[column] = 'stringValue'  
[column] = 'dateValue'  
[column] > value   
[column] >= value   
[column] < value   
[column] <= value   
[column] BETWEEN value1 AND value2   
[column] IN (value1,value2,...)   
[column] NOT IN (value1,value2,...)   
[column] LIKE value   
[column] NOT LIKE value   
[column] IS NULL/IS NOT NULL

and

* Column names must be enclosed in square brackets, e.g., [OrderDate].
* Column names are case-sensitive.
* Column names can only reference a column in the current data object.
* Column names can be either the
  "friendly" name found in the Columns panel or the actual column name in the data source.
* Conditions may be nested.
* String and date values must be enclosed in *single* quotes.
* Numeric values must not be enclosed in quotes.

![](https://devnet.logianalytics.com/hc/article_attachments/5160446913687/noteicon.png) The filter expression only applies to the associated data object. In a typical Dataview, data objects are often related via Left Outer Joins and this may result in Null values for filtered information. Furthermore, it's possible to create a filter on a data object to remove Null values but, due to the behavior of a Left Outer Join, continue to see Null values in the resulting
Dataview.
