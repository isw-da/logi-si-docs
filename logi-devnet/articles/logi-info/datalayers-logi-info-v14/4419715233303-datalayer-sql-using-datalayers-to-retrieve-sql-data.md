---
title: "DataLayer.SQL - Using Datalayers to Retrieve SQL Data"
id: 4419715233303
section: "Datalayers - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715233303-DataLayer-SQL-Using-Datalayers-to-Retrieve-SQL-Data
updated_at: 2022-07-17T02:24:38Z
---

# DataLayer.SQL - Using Datalayers to Retrieve SQL Data

# DataLayer.SQL - Using Datalayers to Retrieve SQL Data

DataLayer.SQL runs a SQL query to retrieve data from a SQL datasource. The element's **Source** attribute value is the actual SQL statement, and any valid SQL statement (or statements) will be run.

![](https://devnet.logianalytics.com/hc/article_attachments/7522826246423/introdl_01.png)

The example above shows a simple SQL query that returns data to a simple Data Table.

![](https://devnet.logianalytics.com/hc/article_attachments/7522845615639/introdl_02.png)

However, as shown in the example above, the Source attribute value (opened in the Attribute Zoom Window) can consist of *multiple* SQL statements. They will all be executed, as long as the syntax is correct, and any results will be returned to the datalayer. The Attribute Zoom window is opened for any attribute by double-clicking the attribute name.

All valid SQL statements can be executed. The **Handle Quotes Inside Tokens** attribute handles tokens that might have embedded single quotes, such as the text *Trail's Head*. When set to *True*, token values in the SQL Command will be wrapped in single-quotes, "doubling" them so the syntax will be valid. The default is *False*.

Tokens for string values should be wrapped in quotes to conform to your database SQL syntax. For example, if you'd use a query with a WHERE clause including quotes, like this:

...WHERE user\_lastname = 'Smith'

Then with tokens it would be:

...WHERE user\_lastname = '@Request.UserName~'

The **If Data Error** element can be used beneath DataLayer.SQL to handle errors that may occur, by switching to an alternate datalayer. While the multi-statement capability makes it easy to use them, your best performance for complex SQL queries and best security will be found by using stored procedures and the **DataLayer.SP** element.

![](https://devnet.logianalytics.com/hc/article_attachments/7522745474327/_newplus.jpg) New for 14.1 Or, use the token element @DataLayerError in conjunction with the **If Data Error** element to capture all of the error information.

![](https://devnet.logianalytics.com/hc/article_attachments/7522804940823/image-20220118-194520_1152x533.png)

Depending on the information you want to display on the page, you can choose from the following tokens:

* ErrorMessage~
* Restful data source only: rdHttpResponseBodyContent~
* Restful data source only: rdHttpResponseBodyCode~
* Restful data source only: rdHttpResponseDescription~

![](https://devnet.logianalytics.com/hc/article_attachments/7522755629847/noteicon.jpg)Use divisions to customize the error message to include images, buttons, and links.

See [Datalayer Error Handling](https://devnet.logianalytics.com/hc/en-us/articles/4419707704855-Datalayer-Error-Handling) for more information.
