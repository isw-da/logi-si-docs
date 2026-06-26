---
title: "Data Table Tutorial - Wizard"
id: 4406816906903
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406816906903-Data-Table-Tutorial-Wizard
updated_at: 2022-04-06T06:02:45Z
---

# Data Table Tutorial - Wizard

# Data Table Tutorial - Wizard

This topic is for new Logi developers. It guides you through the
process of building a Logi report that presents data from your SQL
database in a table. It uses Studio's wizards to create the report.

**Requirements**: This tutorial assumes that you have:

* Microsoft IIS web server and .NET Framework 4.x installed, - OR -
* A supported Java web server and Oracle JDK or OpenJDK 8, 11, 12, 13 (depending on your setup)  
  ![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png)
  Oracle has changed its Java usage policies - see [Java Usage Policy](https://devnet.logianalytics.com/hc/en-us/articles/4406817692055-Java-Usage-Policy)
  for important information.
* And an un-expired trial license, or a regular or OEM license file,
  installed in the   
  *<Logi Info installation folder>*\LogiStudio folder,
  which defaults to:  
    C:\Program Files\LogiXML IES Dev\LogiStudio;
* A working connection to a SQL database server;
* Credentials for accessing a table on the database server.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) This tutorial builds on the [Hello World! Tutorial](https://devnet.logianalytics.com/hc/en-us/articles/4406816920599-Hello-World-Tutorial). Please complete that tutorial before proceeding with this one.
We also offer a more comprehensive tutorial,
[Data Table Tutorial - Manual](https://devnet.logianalytics.com/hc/en-us/articles/4406822240407-Data-Table-Tutorial-Manual), which does not use Studio Wizards and provides more
"behind-the-scenes" insight into report creation.
 
Begin by launching **Logi Studio**, using its desktop icon or Start![](https://devnet.logianalytics.com/hc/article_attachments/4417583616279/menuarrowrt.png)All Programs![](https://devnet.logianalytics.com/hc/article_attachments/4417583616279/menuarrowrt.png)Logi Info![](https://devnet.logianalytics.com/hc/article_attachments/4417583616279/menuarrowrt.png)Studio.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575929751/datatablewiz_01.png)

1. In Logi Studio, close the Getting Started dialog box and re-open the
   **HelloWorld** application from the Welcome Panel, as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584241559/datatablewiz_02.png)

2. Click the **New File** menu item, and select *Report* from its
   drop-down list of options, as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4417592023447/datatablewiz_03.png)


Studio will add a new report definition, named "newReport" in
the Application Panel, and put it into rename mode. Just start typing a
new name - such as "**MyDataTable1**" - and press Enter to
rename it.

If something happens, like you click elsewhere, and it exits rename
mode, just select the newReport definition and press F2, or right-click
and select *Rename*, to rename it.
  

![](https://devnet.logianalytics.com/hc/article_attachments/4417584241815/datatablewiz_04.png)

3. You probably noticed that the new definition was opened in the Workspace
   editor. Select its **Body** element and the **Wizards** tab will
   appear in the main menu. In the Wizards tab, click the
   **Data Table** menu item to start the Add a Data Table wizard.

![](https://devnet.logianalytics.com/hc/article_attachments/4417592024599/datatablewiz_05.png)

4. The wizard will first ask you to specify the datalayer type. Datalayers
   retrieve data for use in reports. Use the default *SQL* datalayer
   type and click **Next**.

![](https://devnet.logianalytics.com/hc/article_attachments/4417592025111/datatablewiz_06.png)

5. Data for this report is coming from a database server, so you need to
   establish a **connection** to it. Select *Create New* to create
   a new connection and click **Next**.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575930391/datatablewiz_07.png)

6. The wizard will prompt you, in separate dialog boxes, for all of the
   information shown above. To save space, we've grouped them into
   *one* wizard image. You'll provide information as necessary and
   click **Next** to proceed each time.   
     
    The prompts shown above are for Microsoft SQL Server, but they'll vary
   depending on the Connection Type you select.  
     
    After you provide the requested information, the wizard will test the
   connection and present its status. If there's a problem, you can click
   **Previous** to go back and review or change your entries. Click
   **Next** again as needed to re-test the connection.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584242071/datatablewiz_08.png)

7. Once the connection is successful, you're ready to enter a SQL query.
   Skip using the SQL Query Builder this time and just type-in a simple
   query, like the one shown above, that will return some columns from your
   database. The click **Next** to continue.

  
![](https://devnet.logianalytics.com/hc/article_attachments/4417584242583/datatablewiz_09.png)  

8. The wizard will display an example data table in a dialog box, where you
   can make adjustments to it, if desired. If the table is just as you want
   it, click **Next** to exit the wizard. If not, you can continue
   making adjustments, using the features identified above:   
     
    1- Click these buttons to add calculated or "Formula" columns,
   and to Filter the data based on column values;   
    2- Click the Gear icon to display the table's Configuration Panel
   (discussed below);   
    3- Hover your cursor over a table column header and use the drag handles
   that appear to change the column width or rearrange column order. Click
   the header text to see a configuration menu for that column (discussed
   below);  
    4- Select the maximum number of rows to be retrieved.

### Table Configuration Panel

If you click the Gear icon, the table's Configuration Panel will be
displayed:



![](https://devnet.logianalytics.com/hc/article_attachments/4417592026775/datatablewiz_10.png)  
  
As shown above, the Configuration Panel includes these controls:

* **Columns** - Select the columns that will be displayed (displayed
  vs. retrieved in the data).
* **Sort** - Specify the sort order of the data after it's been
  retrieved.
* **Group** - Specify the grouping of the data after it's been
  retrieved.
* **Aggregate** - Add new columns for aggregations including
  *Sum, Average, Standard Deviation, Count, Distinct Count,
  Minimum,*
  and *Maximum*.
* **Paging** - Specify whether the table will use paging and, if
  so, how many rows will be shown per page.

  
 Click the Gear icon again to hide the Configuration Panel.  

### Column Configuration Menu

If you click a column's header text, a pop-up Configuration Menu for
that column will be displayed:  

![](https://devnet.logianalytics.com/hc/article_attachments/4417584242839/datatablewiz_10a.png)

Options on that menu allow you to do some of the same thing you can do
in the Configuration Panel but other options, like Format, work
specifically on the selected column. Changes in the example table will
take affect immediately. The wizard automatically gives each column
interactive sorting capabilities.  

9. When you're done, click **Next** and **Finish** and the Wizard
   will close. You may have noticed that the wizard was adding all of the
   elements for the data table to your definition as you went along.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) Only the elements for the data table itself will be added. The
wizard's configuration controls that you, as a developer, have been
working with are *not* part of the data table and do not appear at
runtime.



![](https://devnet.logianalytics.com/hc/article_attachments/4417575931031/datatablewiz_11.png)

10. Click the **Preview** tab at the bottom of the Workspace editor to
    save your work and preview the report in Studio. It should look
    something like the example shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575931415/datatablewiz_12.png)  

  

If you'd like to view it in your default browser, select and right-click
the report definition, as shown above, and select
*Run in Browser* from its context menu.

Well done! We recommend that you take some time to examine the elements
the wizard added to your report and \_Settings definitions. In the report
definition, in particular, notice the **Label** element added beneath
each **Data Column** element. Look at its attributes and notice the
**@Data** "token" used to represent the data from the
datalayer.
You can **rearrange** the order of the table columns by selecting the
**Data Table Column** elements and moving them up or down in the
element tree in the report definition. You can drag them (along with their
child elements) to a new position, or use the Move Up / Move Down items in
the Home tab of Studio's main menu. Move a few and preview the report
again to see the results.
Congratulations on completing this tutorial.
