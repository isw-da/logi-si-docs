---
title: "The Database Browser"
id: 4406822589335
section: "Use Logi Studio/SSRM - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822589335-The-Database-Browser
updated_at: 2022-04-06T06:09:37Z
---

# The Database Browser

# The Database Browser

The **Database Browser** tool allows developers to view the **objects** and **data** in connected databases. The objects available include Tables, Columns, Views, and Stored Procedures. The database browser *does**not* work with datasources that do not
return a *schema* when queried, such as XML data files.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583668503/usingstudio_53.png)

The Database Browser is launched from the main menu's Tools tab, as shown above. Select a database from the list of connections that have been configured in the \_Settings definition for this application.

If you select a Connection element in the \_Settings definition and click the Database Browser menu item, it will open the database immediately. If no Connection element is selected, then a list of databases like the one shown above will be displayed so you can select one.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563020311/usingstudio_54.png)

The Database Browser, shown above, provides the following features:

1. A list of the **Tables** available in the database is presented, as shown above.
2. Each table icon can be expanded to display its **Columns**.
3. The database's **Views** and **Stored Procedures**, if any, are also available.
4. The **Query Builder** tool can be launched from here with this button.
5. The **Details** tab provides table or column properties, the **Source** tab allows Stored Procedure code to be viewed (but not edited), and the **Data** tab displays the table's actual data, limited to 10,000 rows.
6. Rows of data displayed in the Data tab can be right-clicked and **edited** or **deleted**.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) The Database Browser *will* work with the databases for which we provide "native" Connection elements, such as Oracle, MS SQL Server, and MySQL. It *may* work with other databases that use a connection that mimics that of a database for which we provide a native connection. It is *not**guaranteed* to work with *every* database and, in that
case,
we recommend
that you use tools provided with the database to examine and manipulate it outside of Studio.

The Database Browser may not support all of the functions and views
available in Microsoft Access databases.

By default, the Database Browser will only return 10,000 rows of data. You can turn this limit off in Studio in Tools ![](https://devnet.logianalytics.com/hc/article_attachments/4417575446295/menuarrow.gif) Options. The Database Browser is a **non-modal dialog box** and can remain open, for reference, while you work elsewhere in Studio.
