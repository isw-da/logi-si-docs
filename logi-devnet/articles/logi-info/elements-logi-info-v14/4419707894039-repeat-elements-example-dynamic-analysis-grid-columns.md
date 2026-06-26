---
title: "Repeat Elements Example: Dynamic Analysis Grid Columns"
id: 4419707894039
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707894039-Repeat-Elements-Example-Dynamic-Analysis-Grid-Columns
updated_at: 2022-07-17T01:34:57Z
---

# Repeat Elements Example: Dynamic Analysis Grid Columns

# Repeat Elements Example: Dynamic Analysis Grid Columns

Repeat Elements can also be used with super-elements, such as the **Analysis Grid**. This allows you to present dynamic Analysis Grids and let the user select the datasource at run time.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714923927/repeatele_18.png)

1. We'll start by adding an **Analysis Grid** element, and its child datalayer, to the definition, as shown above. The datalayer query will retrieve all of the data from the table: SELECT \* FROM Orders

![](https://devnet.logianalytics.com/hc/article_attachments/4419714924183/repeatele_19_613x165.png)

2. Next, we add **Repeat Elements** element as a child of the Analysis Grid, with its own child datalayer, as shown above. This datalayer will retrieve the column information from the datasource. Once again, the syntax for querying the schema will vary by datasource and this example is for Microsoft SQL Server 2012. The SQL query is:

SELECT column\_name,  
CASE WHEN data\_type = 'nchar' THEN 'Text'  
WHEN data\_type = 'int' THEN 'Number'  
 WHEN data\_type = 'money' THEN 'Number'  
WHEN data\_type = 'datetime' THEN 'Date'   
END As column\_type  
FROM information\_schema.columns  
WHERE table\_name = 'Orders'  
AND ordinal\_position < 9 -- limits number of columns returned  
ORDER BY ordinal\_position

It's pretty straightforward, except for the CASE statement. We need to specify the column data types for the Analysis Grid columns and, to do that, we need to know the data type for each column. The CASE statement translates the data type name in the system schema table to one of the values used in the **Analysis Grid Column** element's **Data Type** attribute. Once again, the actual data types available to you for use in the CASE statement will depend on your datasource.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699936919/repeatele_20_596x173.png)

3. Finally, we add an **Analysis Grid Column** element, as shown above, and set is attributes using @Repeat tokens.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699937175/repeatele_21_596x211.png)

When the report is run, an Analysis Grid will be displayed that dynamically includes the available data columns. Data can be formatted and aligned using techniques from the previous example.
