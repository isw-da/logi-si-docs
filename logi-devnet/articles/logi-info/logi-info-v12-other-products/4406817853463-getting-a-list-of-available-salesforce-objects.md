---
title: "Getting a List of Available Salesforce Objects"
id: 4406817853463
section: "Logi Info v12 & Other Products"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817853463-Getting-a-List-of-Available-Salesforce-Objects
updated_at: 2022-04-06T06:08:38Z
---

# Getting a List of Available Salesforce Objects

# Getting a List of Available Salesforce Objects

How do you determine what objects, specifically tables and columns, Salesforce makes available?

To get a list of tables, you use a special SOQL query using the command **LIST TABLES**. This query will return a list of table names; these names, in turn, can be subsequently used with LIST to retrieve the columns for each table. Here are some examples of the code to put this in action:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575545623/connsf_05.png)

As shown above, a simple data table and DataLayer.SQL element are used to retrieve a list of tables from Salesforce. The special SQL query syntax "LIST TABLES" is used in the datalayer's Source attribute.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563093143/connsf_06.png)

The results returned from Salesforce can be accessed using the **special Data token** @Data.rdSalesforceTable~, as shown above,

![](https://devnet.logianalytics.com/hc/article_attachments/4417575546135/connsf_07.png)

and the output will look something like the example above.
Once the table names have been acquired, they can be used in a query to retrieve a list of the columns for a particular table.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575546775/connsf_08.png)

In the example above, a second data table is used to list the columns associated with one of the Salesforce tables. The SOQL query syntax is LIST <table name>, and in the example, a table name has been hard-coded into the query. A more sophisticated solution might use a table name selected from the displayed results of the previous (LIST TABLES) query to drive the second query, using a request token: LIST @Request.TableName~, for example.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583740439/connsf_09.png)

And finally, as shown above, another **special Data token** @Data.rdSalesforceField~ is used to display the Salesforce table column information the query retrieved.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563093783/connsf_10.png)

The output would be a list of columns, as shown above.   
By combining the techniques shown here, developers can access data stored on Salesforce and incorporate it in their Logi applications.
