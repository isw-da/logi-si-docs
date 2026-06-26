---
title: "DataLayer.SQL - Using Studio's DataLayer Wizard"
id: 4406817328791
section: "Datalayers - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817328791-DataLayer-SQL-Using-Studio-s-DataLayer-Wizard
updated_at: 2022-04-06T06:05:26Z
---

# DataLayer.SQL - Using Studio's DataLayer Wizard

# DataLayer.SQL - Using Studio's DataLayer Wizard

Studio includes a wizard that can assist you in configuring DataLayer.SQL. The wizard assumes that you have already added an appropriate database **Connection** element in the \_Settings definition and configured it.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563378839/dlsql_01.png)

As shown above, the wizard can be started by selecting and then right-clicking the parent element under which you want to add the datalayer, and using the context menus to select "Add a SQL DataLayer". The wizard will open; use it as follows:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575768471/dlsql_02.png)

1. Select the ID of the Connection element from the drop-down list of available connections. Click **Next** to continue.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417575768599/dlsql_03.png)
2. Enter the SQL query that will be used to retrieve data, either by typing it in directly or by building it using the Query Builder tool (see [Using Logi 12 Studio](https://devnet.logianalytics.com/hc/en-us/articles/4406822594327-Using-Logi-12-Studio)). If you attempt to use the Query Builder and receive an error, type in a simple query instead and proceed with the wizard; you can adjust the query later. Click **Next** to continue.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417563379863/dlsql_04.png)
3. Click **Finish** to close the wizard.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417563379991/dlsql_05.png)![](https://devnet.logianalytics.com/hc/article_attachments/4417584019607/dlsql_05a.png)
4. The wizard has inserted the datalayer and configured its attributes, as shown above.
