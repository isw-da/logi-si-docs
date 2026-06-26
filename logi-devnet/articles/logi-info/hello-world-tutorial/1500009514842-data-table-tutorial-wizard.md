---
title: "Data Table Tutorial - Wizard"
id: 1500009514842
section: "Hello World! Tutorial"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009514842-Data-Table-Tutorial-Wizard
updated_at: 2021-06-17T01:58:16Z
---

# Data Table Tutorial - Wizard

# Data Table Tutorial - Wizard

This topic is for new Logi developers. It guides you through the process of building a Logi report that presents data from your SQL database in a table. It uses Studio's wizards to create the report.

**Requirements**: This tutorial assumes that you have:

* Microsoft IIS web server and .NET Framework 4.x installed, - OR -
* A supported Java web server and Sun JDK 1.6 1.7, or 1.8, or JRockit, installed;
* An un-expired trial license or a regular or OEM license file installed in   
  C:\Program Files\LogiXML IES Dev\LogiStudio;
* A working connection to a SQL database server;
* Credentials for accessing a table on the database server.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif)This tutorial builds on the [Hello World! Tutorial](https://devnet.logianalytics.com/hc/en-us/articles/1500009530861-Hello-World-Tutorial). Please complete that tutorial before proceeding with this one.

We also offer a more comprehensive tutorial, [Data Table Tutorial - Manual](https://devnet.logianalytics.com/hc/en-us/articles/1500009530481-Data-Table-Tutorial-Manual), which does not use Studio Wizards and provides more "behind-the-scenes" insight into report creation.

Begin by launching **Logi Studio**, using its desktop icon or Start![](https://logianalytics.zendesk.com/hc/article_attachments/4402771511575/menuarrowrt.png)All Programs![](https://logianalytics.zendesk.com/hc/article_attachments/4402771511575/menuarrowrt.png)Logi Info![](https://logianalytics.zendesk.com/hc/article_attachments/4402771511575/menuarrowrt.png)Studio.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771833751/datatablewiz_01.png)

1. In Logi Studio, close the Getting Started dialog box and re-open the **HelloWorld** application from the Welcome Panel, as shown above.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771834007/datatablewiz_02.png)

2. Click the **New File** menu item, and select *Report* from its drop-down list of options, as shown above.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771834263/datatablewiz_03.png)

Studio will add a new report definition, named "newReport" in the Application Panel, and put it into rename mode. Just start typing a new name - such as "**MyDataTable1**" - and press Enter to rename it.

If something happens, like you click elsewhere, and it exits rename mode, just select the newReport definition and press F2, or right-click and select *Rename*, to rename it.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771834519/datatablewiz_04.png)

3. You probably noticed that the new definition was opened in the Workspace editor. Select its **Body** element and the **Wizards** tab will appear in the main menu. In the Wizards tab, click the **Data Table** menu item to start the Add a Data Table wizard.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778677271/datatablewiz_05.png)

4. The wizard will first ask you to specify the datalayer type. Datalayers retrieve data for use in reports. Use the default *SQL* datalayer type and click **Next**.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771834775/datatablewiz_06.png)

5. Data for this report is coming from a database server, so you need to establish a **connection** to it. Select *Create New* to create a new connection and click **Next**.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771835031/datatablewiz_07.png)

6. The wizard will prompt you, in separate dialog boxes, for all of the information shown above. To save space, we've grouped them into *one* wizard image. You'll provide information as necessary and click **Next** to proceed each time.   
     
   The prompts shown above are for Microsoft SQL Server, but they'll vary depending on the Connection Type you select.  
     
   After you provide the requested information, the wizard will test the connection and present its status. If there's a problem, you can click **Previous** to go back and review or change your entries. Click **Next** again as needed to re-test the connection.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771835287/datatablewiz_08.png)

7. Once the connection is successful, you're ready to enter a SQL query. Skip using the SQL Query Builder this time and just type-in a simple query, like the one shown above, that will return some columns from your database. The click **Next** to continue.

8. As shown above, the next dialog box displays the names of all of the columns your query returned. Select the columns you'd like in your data table. The *Uncheck All* link can be helpful if you don't want the default "all columns" selection. Click **Next** to continue.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771835543/datatablewiz_10.png)

9. The wizard will prompt you, in separate dialog boxes, for all of the information shown above. To save space, we've grouped them into *one* wizard image. You'll provide information as necessary and click **Next** to proceed each time.

10. Click **Finish**. You probably noticed that the wizard has been inserting elements into the report definition as you've gone along.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778677527/datatablewiz_11.png)

11. Click the **Preview** tab at the bottom of the Workspace editor to save your work and preview the report in Studio. It should look something like the example shown above.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771835799/datatablewiz_12.png)

If you'd like to view it in your default browser, select and right-click the report definition, as shown above, and select *Run in Browser* from its context menu.

Well done! We recommend that you take some time to examine the elements the wizard added to your Default and \_Settings definitions. In the Default definition, in particular, notice the **Label** element added beneath each **Data Column** element. Look at its attributes and notice the **@Data** "token" used to represent the data from the datalayer.

You can **rearrange** the order of the table columns by selecting the **Data Table Column** elements and moving them up or down in the element tree in the Default definition. You can drag them (with their child elements) to a new position, or use the Move Up / Move Down items in the Home tab of Studio's main menu. Move a few and preview the report again to see the results.

Congratulations on completing this tutorial.
