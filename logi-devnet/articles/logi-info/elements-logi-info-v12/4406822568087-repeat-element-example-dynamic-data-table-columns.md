---
title: "Repeat Element Example: Dynamic Data Table Columns"
id: 4406822568087
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822568087-Repeat-Element-Example-Dynamic-Data-Table-Columns
updated_at: 2022-04-06T06:09:20Z
---

# Repeat Element Example: Dynamic Data Table Columns

# Repeat Element Example: Dynamic Data Table Columns

Suppose you have a requirement to display a data table that may have a varying number of columns. You could use **Auto Columns** to display the table columns but you want more control over formatting and appearance. This is a perfect opportunity to use Repeat Elements, but assumes that your datasource can accept queries about the data schema. Here's how:

![](https://devnet.logianalytics.com/hc/article_attachments/4417583687447/repeatele_03.png)

1. Start by adding a **Data Table** element and a datalayer to your definition. Then, as a child of the data table, add a **Repeat Elements** element, as shown above.  
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417563040023/repeatele_04.png)
2. Next, add a datalayer beneath the Repeat Elements element. This datalayer is going to query the datasource, in this example a SQL server, for information about the table schema. You will need to know the specific syntax required to do this, which can vary widely from one datasource to another. This query is for Microsoft SQL Server 2012:

SELECT column\_name,  
CASE WHEN data\_type= 'nchar' THEN 'Text'  
WHEN data\_type = 'int' THEN 'Number'  
 WHEN data\_type = 'money' THEN 'Number'  
WHEN data\_type = 'datetime' THEN 'Date'   
END As column\_type  
FROM information\_schema.columns  
WHERE table\_name = 'Orders'  
AND ordinal\_position < 9 -- limits number of columns returned  
ORDER BY ordinal\_position

It's pretty straightforward, except for the CASE statement. We're going to add **Sort** elements to our data table columns later and, to do that, we need to know the *data type* for each column. The CASE statement translates the data type name in the database's system schema table to one of the values used in the Sort element's Data Type attribute. The actual data types available to you for use in the CASE statement will depend on your datasource.  
  
![](https://devnet.logianalytics.com/hc/article_attachments/4417583687703/repeatele_05.png)

1. Now we can add the **Data Table Column** element, as shown above. Its **Column Header** attribute makes use of the @Repeat token and the column name we retrieved in the query.   
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417583688087/repeatele_06.png)
2. To display data in the column, we add a **Label** element. Its **Caption** uses something you may not have seen before: "nested" tokens. Basically, this is a token within a token; the inner token gets evaluated first, then the outer token. If this was a mathematical expression, it might look like: @Data.(@Repeat.column\_name~)~ and the token in the parenthesis gets evaluated first.  
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417583688471/repeatele_07.png)
3. And, finally, we add the **Sort** element and set its attributes, using @Repeat tokens, as shown above.  
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417583688855/repeatele_08.png)

When the report is run, we get something like the table shown above. Obviously, additional formatting can be done as well. If the schema of the table changes, the report will handle it without any additional development.

### Special Crosstab Table Considerations

If you want to create dynamic **Crosstab Tables** using Repeat Elements and the techniques shown above, there are some special considerations:

When working with Crosstab Tables, you may decide to use **Extra Crosstab Value Column** elements, summaries, or individual column IDs, all of which use special column names consisting of an "rd" reserved word, a dash, and a column ID, such as rdCrosstabValue-OrderTotal.

However, these special column names won't work in nested tokens. For example, this nested token *won't* work:

@Data.rdCrosstabValue-@Repeat.column\_name~~

In order to use these special column names correctly in nested tokens, you need to concatenate the "rdCrosstab" reserved word and the dash with the column ID value in the column name data in the Repeat Element element's datalayer. You can do this in your SQL query, or with a Calculated Column element. The @Data.@Repeat.column\_name~~ nested token will then work correctly.
