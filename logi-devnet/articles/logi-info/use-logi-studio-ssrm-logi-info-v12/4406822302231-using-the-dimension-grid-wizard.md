---
title: "Using the Dimension Grid Wizard"
id: 4406822302231
section: "Use Logi Studio/SSRM - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822302231-Using-the-Dimension-Grid-Wizard
updated_at: 2022-04-06T06:05:49Z
---

# Using the Dimension Grid Wizard

# Using the Dimension Grid Wizard

The following examples walk you through using the Dimension Grid
wizard.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575727895/dgwizard_01.png)

1. Start the wizard by right-clicking the grid's parent and selecting
   **Element Wizards**![](https://devnet.logianalytics.com/hc/article_attachments/4417575446295/menuarrow.gif)**Add a Dimension Grid**, as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563322519/dgwizard_03.png)

2. **Datalayer Type** - Select the appropriate datalayer type for your
   datasource. Click **Next**.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575728407/dgwizard_04.png)

3. **Connection ID** - Select the desired connection from the list of
   connections defined in the \_Settings definition. Click
   **Next.**

![](https://devnet.logianalytics.com/hc/article_attachments/4417563322775/dgwizard_05.png)

4. **SQL Query** - If you 're using a SQL datasource, enter the query
   (or use the query wizard to build one) and click **Next**. This
   example uses the following T-SQL query:

SELECT [Order Details Extended].UnitPrice, [Order Details
Extended].Quantity, [Order Details Extended].ExtendedPrice,
Categories.CategoryName, Products.ProductName, Orders.OrderDate,
Customers.CompanyName, Customers.Country, Customers.Region,
Customers.City, Employees.LastName, Employees.FirstName   
 FROM [Order Details Extended]   
 INNER JOIN Orders ON [Order Details Extended].OrderID =
Orders.OrderID   
 INNER JOIN Products ON [Order Details Extended].ProductID =
Products.ProductID   
 INNER JOIN Categories ON Categories.CategoryID = Products.CategoryID
  
 INNER JOIN Customers ON Customers.CustomerID = Orders.CustomerID
  
 INNER JOIN Employees ON Employees.EmployeeID =
Orders.EmployeeID

![](https://devnet.logianalytics.com/hc/article_attachments/4417563323415/dgwizard_06.png)

5. **Xolap Cube Wizard** - Click **Next** to start the cube
   wizard.  
     
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417563323799/dgwizard_07.png)

6. **Create Dimensions** - Add dimensions by entering the arbitrary
   Dimension Name in the text box and clicking **Add**.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563324695/dgwizard_08.png)

7. **Add Levels** - Select a data column for a hierarchical level from
   the list and click the green arrow icon, as
   shown above.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417583969047/dgwizard_08a.png)  
    If you select a Date type column, the wizard will prompt you, as shown
   above, to add time period columns to the data that parse out the Year,
   Quarter, Month, or Day values, as shown above.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417575729943/dgwizard_09.png)  
    The column you selected will be added to the lower list of Dimension
   Levels. **Repeat** to add as many levels as desired. To remove a
   level, select it and click the red X icon. Refer to the end of the topic if you're creating levels
   using Date-type columns.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417575730199/dgwizard_10.png)

8. **Add More Dimensions and Levels** - Repeat the process of adding
   dimensions and levels until all dimensions have been configured. Use the
   Rename and Delete buttons to affect dimensions you've already
   configured. When all dimensions and levels have been configured, click
   **Next**.  
     
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417563325463/dgwizard_12.png)

9. **Create Measures** - Select a data column to be aggregated from the
   list and click the green arrow icon, as
   shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563325591/dgwizard_13.png)

The selected measure will appear below. Enter an arbitrary
**Measure Name** and select the aggregation or summarization function
to be applied to it. To remove a measure, click the adjacent
red X icon.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575730455/dgwizard_14.png)

10. **Add More Measures** - Repeat the process until all measures have
    been configured, then click **Next**.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583969687/dgwizard_15.png)

13. **Done** - Click **Finish** to close the wizard.

The wizard has added all the appropriate elements to your report
definition. Save the definition and run it.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583969815/dgwizard_16.png)

When it appears, select dimensions, measures, and values from the
Dimension Grid and view your data.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) You may need to manually set the Format of Date type columns.
