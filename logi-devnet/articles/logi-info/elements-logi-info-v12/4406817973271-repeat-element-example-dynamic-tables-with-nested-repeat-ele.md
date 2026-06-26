---
title: "Repeat Element Example: Dynamic Tables with Nested Repeat Elements"
id: 4406817973271
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817973271-Repeat-Element-Example-Dynamic-Tables-with-Nested-Repeat-Elements
updated_at: 2022-04-06T06:09:22Z
---

# Repeat Element Example: Dynamic Tables with Nested Repeat Elements

# Repeat Element Example: Dynamic Tables with Nested Repeat Elements

Let's expand on the previous example - this time we don't even have to know the table names. We can use nested **Repeat Elements** elements to gather all the information to we need to display the data for whatever tables are available. Let's also do a little more sophisticated formatting and aligning this time, and some summarizing.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575508759/repeatele_09.png)

1. This time we'll start by adding a **Repeat Elements** element to our definition, with a child datalayer, as shown above. Once again, the syntax for querying the schema will vary by datasource and this example is for Microsoft SQL Server 2012. The SQL query, which limits us to three tables for this example, is:

SELECT table\_name FROM information\_schema.tables  
WHERE table\_name IN ('Customers', 'Employees', 'Orders')  
ORDER BY table\_name

Think of this as the "outer loop" of the code, which allows us to iterate through each of the tables.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563038359/repeatele_10_582x168.png)

2. Now we'll add a **Data Table** element, and use @Repeat tokens from the datalayer to give each table its required unique ID and a caption, as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575509143/repeatele_11_625x184.png)

3. Add a **datalayer** beneath the data table, as shown above, and set its attributes as shown above, right. This query will retrieve that data for each table.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575509655/repeatele_12_608x136.png)

4. We want to summarize freight costs for the Orders table, so add an **Aggregate Column** element beneath the datalayer and set its attributes as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575510039/repeatele_13_244x145.png)

5. Now things begin to get interesting: add *another***Repeat Elements** element beneath the data table, as shown above, with its own datalayer. This is the "inner loop" of the code, which iterates the table columns. The SQL query for this datalayer is:

SELECT column\_name, data\_type,  
CASE WHEN data\_type = 'nchar' THEN ''  
WHEN data\_type = 'int' THEN '######'  
WHEN data\_type = 'datetime' THEN 'Short Date'   
 WHEN data\_type = 'money' THEN 'Currency'   
END As column\_format,  
CASE WHEN data\_type = 'nvarchar' THEN 'ThemeAlignLeft'  
WHEN data\_type = 'nchar' THEN 'ThemeAlignCenter'  
WHEN data\_type = 'int' THEN 'ThemeAlignRight'  
WHEN data\_type = 'datetime' THEN 'ThemeAlignCenter'   
WHEN data\_type = 'money' THEN 'ThemeAlignRight'   
END As column\_align  
FROM information\_schema.columns  
WHERE table\_name = '@Repeat.repeatTableNames.table\_name~'  
AND ordinal\_position < 9 -- limits number of columns returned  
ORDER BY ordinal\_position

As shown above, the query uses CASE statements to set formatting and alignment values based on the data type the column and, in the WHERE clause, uses an @Repeat token from the *first* Repeat Elements element (the "outer loop") to limit the result set to a specific table.

You can identify columns from the first Repeat Elements element more specifically using a token that includes its element ID: @Repeat.repeatTableNames.table\_name~.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563039383/repeatele_13a_553x145.png)
  
![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) When using nested Repeat Elements elements in any type of table, you cannot have more than one table hierarchy (Rows, Row, Column Cells) level between them. As shown above, the arrangement of rows and columns in the left and middle examples is correct. The right example is *invalid* and the second Repeat Elements element will not be processed.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575510295/repeatele_14_648x167.png)

6. At last we can add a **Data Table Column** element under the second Repeat Elements element, as shown above, and set its attributes using @Repeat tokens.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563039639/repeatele_15_648x175.png)

7. And then we can add a **Label** element to display the data, using nested tokens as before, in its attributes as shown. We'll also use an @Repeat token to set the format.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583687191/repeatele_16_330x317.png)

8. Finally, we can finish up by adding **Summary Row** (and its child elements) and **Interactive Paging** child elements beneath the Data Table and a **New Line** element beneath the first Repeat Elements element, as shown above. To ensure that the summary row only appears for the Orders table, set the Condition attribute of its three **Column** child elements to "@Repeat.table\_name~" = "Orders".

![](https://devnet.logianalytics.com/hc/article_attachments/4417583687319/repeatele_17_567x632.png)

When the report is run, three tables should be displayed, as shown above.
