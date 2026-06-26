---
title: "Izenda Functions"
id: 12528280982167
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528280982167-Izenda-Functions
updated_at: 2023-02-23T15:58:09Z
---

# Izenda Functions

# Izenda Functions

## List of Built-in Functions

| Function | Description | Result Data Types | Examples |
| --- | --- | --- | --- |
| **AVG**  `AVG(expression)`  Numeric, Money | Returns the average of the values in a group. Null values are ignored. | Numeric, Money | `AVG([Retail].[dbo].[Orders].[Freight])` |
| **COUNT**  `COUNT(expression)`  Any data type except Image and Lob. | Returns the number of items in a group. | Numeric. | `COUNT([Retail].[dbo].[Orders].[OrderID])` |
| **MAX**  `MAX(expression)`  Any data type except Image and Lob. | Returns the maximum value in a group. | The same data type as expression. | `MAX([Retail].[dbo].[Orders].[Freight])` |
| **MIN**  `MIN(expression)`  Any data type except Image and Lob. | Returns the minimum value in a group. | The same data type as expression. | `MIN([Retail].[dbo].[Orders].[Freight])` |
| **SUM**  `SUM(expression)`  Numeric, Money. | Returns the sum of all the values in a group. Null values are ignored. | The same data type as expression. | `SUM([Retail].[dbo].[Orders].[Freight])` |
| **LEN**  `LEN(expression)`  Text. | Returns the number of characters of the given text expression, excluding trailing blanks. | Numeric. | `LEN([Retail].[dbo].[Orders].[ShipAddress])` |
| **ROUND**  `ROUND(expression)`  Numeric, Money. | Returns the expression rounded to the specified length or precision. | The same data type as expression. | `ROUND([Retail].[dbo].[Orders].[Freight],0)` |
| **CONCAT**  `CONCAT(expression,expression[,...])`  Text. | Returns the concatenation of all the parameters in that exact order. | Text. | `CONCAT('ab','cd',[SHIPCOUNTRY])` |
| **GETDATE**  `GETDATE()`  N/A. | Returns the current system date and time. | Datetime. | `GETDATE()` |
| **DATEADD**  `DATEADD(datepart,number,date)`  **datepart**: the part of the date. (See table [List of Dateparts and Abbreviations](#list-of-dateparts-and-abbreviations))   **number**: the value used to increment datepart.   **date**: an expression that returns a datetime value. | Returns a new datetime value based on adding an interval to the specified date. | Datetime. | `DATEADD(day,3,[DueDate])` |
| **DATEDIFF**  `DATEDIFF(datepart,startdate,enddate)`  **datepart**: the part of the date. (See table [List of Dateparts and Abbreviations](#list-of-dateparts-and-abbreviations))   **startdate**, **enddate**: expressions that return datetime values. | Returns the number of date and time boundaries crossed between two specified dates. | Numeric. | `DATEDIFF(day,[OrderDate],[ShipDate])` |
| **DATEPART**  `DATEPART(datepart,date)`  **datepart**: the part of the date. (See table [List of Dateparts and Abbreviations](#list-of-dateparts-and-abbreviations))   **date**: an expression that returns a datetime value. | Returns a number representing the specified datepart of the specified date. | Numeric. | `DATEPART(DAY,[Retail].[dbo].[Orders].[OrderDate])` |
| **CONVERT**  `CONVERT(data_type,expression)`  **data\_type**: any data type.   **expression**: any expression. | Explicitly converts an expression of one data type to another, similar to `CAST..AS`. | The same data type as data\_type. | `CONVERT(TEXT,[Retail].[dbo].[Orders].[OrderDate])` |
| **CAST..AS**  `CAST(expressionASdata_type)`  **data\_type**: any data type.   **expression**: any expression. | Explicitly converts an expression of one data type to another, similar to `CONVERT`. | The same data type as data\_type. | `CAST([Retail].[dbo].[Orders].[OrderID]ASTEXT)` |
| **ISNULL**  `ISNULL(check_expression,replacement_expression)`  **check\_expression** and **replacement\_expression**: any data type. | Returns the value of check\_expression if it is not NULL; otherwise, returns the value of replacement\_expression. | The same data type as expression. | `ISNULL([Retail].[dbo].[Orders].[ShipRegion],'NoRegion')` |
| **BETWEEN..AND**  `BETWEEN(expression,begin_expression,end_expression)`  Any data type except Image and Lob. | Returns TRUE if the value of test\_expression is greater than or equal to the value of begin\_expression and less than or equal to the value of end\_expression, otherwise returns FALSE. | Boolean. | `CASEWHEN(BETWEEN([Retail].[dbo].[Orders].[EmployeeID],1,3))THEN1000else[Retail].[dbo].[Orders].[EmployeeID]END` |
| **AND**  `boolean_expressionANDboolean_expression`  Boolean. | Returns TRUE when both expressions are TRUE, otherwise returns FALSE. | Boolean. | `CASEWHEN([Retail].[dbo].[Orders].[EmployeeID]=1AND[Retail].[dbo].[Orders].[CustomerID]='DELDG')THEN1000else[Retail].[dbo].[Orders].[EmployeeID]end` |
| **OR**  `boolean_expressionANDboolean_expression`  Boolean. | Returns TRUE when either expression is TRUE, otherwise returns FALSE. | Boolean. | `CASEWHEN([Retail].[dbo].[Orders].[EmployeeID]=1OR[Retail].[dbo].[Orders].[EmployeeID]=2)THEN1000else[Retail].[dbo].[Orders].[EmployeeID]end` |
| **DISTINCT**  `DISTINCT(expression)` or `DISTINCTexpression`  Any data type except Image and Lob. | Returns unique values. | The same data type as expression. | `COUNT(DISTINCT([Northwind].[dbo].[Orders].[ShipCity]))` |
| **IFF**  `IFF(boolean_expression,true_expression[,false_expression])`  **boolean\_expression**: Boolean.   **true\_expression**, **false\_expression**: any data type except Image and Lob. | Returns the value of true\_expression when boolean\_expression is TRUE, otherwise returns the value of false\_expression. | The highest precedence data type from data types of true\_expression and false\_expression. | `IIF([Retail].[dbo].[Orders].[EmployeeID]=2,200,[Retail].[dbo].[Orders].[EmployeeID])` |
| **IF..THEN..ELSE..END**  `IF(boolean_expression)THEN(true_expression)[ELSE(false_expression)]END`  **boolean\_expression**: Boolean.   **true\_expression**, **false\_expression**: any data type except Image and Lob. | Returns the value of true\_expression when boolean\_expression is TRUE, otherwise returns the value of false\_expression. | The highest precedence data type from data types of true\_expression and false\_expression. | `IF([northwind].[dbo].[Orders].[EmployeeID]<3)then'Less'else(IF(BETWEEN([northwind].[dbo].[Orders].[EmployeeID],3,6))then  'More'else'Most'END)END` |
| **CASE WHEN..THEN..ELSE..END**  `CASEWHEN(when_expression)THEN(result_expression)[…n][ELSE(else_result_expression)]END`  Any data type except Image and Lob. | Returns the value of result\_expression matching the first when\_expression with the value equal to input\_expression, otherwise return the value of else\_result\_expression. | The highest precedence data type from data types of all `result_expression` s and else\_result\_expression. | `Casewhen([northwind].[dbo].[Orders].[EmployeeID]=1)then'less'when([northwind].[dbo].[Orders].[EmployeeID]=3)then'mid'when([northwind].[dbo].[Orders].[EmployeeID]=4)  then'high'else'notevaluated'end` |
| **CASE..WHEN..THEN..ELSE..END**  `CASE(input_expression)WHEN(when_expression)THEN(result_expression)[…n][ELSE(else_result_expression)]END`  Any data type except Image and Lob. | Returns the value of result\_expression matching the first when\_expression with the value equal to input\_expression, otherwise return the value of else\_result\_expression. | The highest precedence data type from data types of all `result_expression` s and else\_result\_expression. | `CASE'USA'WHEN  [Retail].[dbo].[Orders].[ShipCountry]THEN1else[Retail].[dbo].[Orders].[OrderID]END` |
| [\*\*](#id1)CASE WHEN…THEN…ELSE…END   `CASEWHEN(when_expression)THEN(result_expression)[…n][ELSE(else_result_expression)]END`  Any data type except Image and Lob. | Returns the value of result\_expression matching the first when\_expression with the value equal to input\_expression, otherwise return the value of else\_result\_expression. | The highest precedence data type from data types of all `result_expression` s and else\_result\_expression. | `Casewhen([northwind].[dbo].[Orders].[EmployeeID]=1)then'less'when([northwind].[dbo].[Orders].[EmployeeID]=3)then'mid'when([northwind].[dbo].[Orders].[EmployeeID]=4)  then'high'else'notevaluated'end` |
| **RUNNINGSUM**  `RUNNINGSUM(expression)`  Numeric, Money. | Returns the sum of all the values of expression from the first row up to the current row. | The same data type as expression. | `RUNNINGSUM([Retail].[dbo].[Orders].[Freight])` |
| **RUNNINGAVG**  `RUNNINGAVG(expression)`  Numeric, Money. | Returns the average of all the values of expression from the first row up to the current row. | The same data type as expression. | `RUNNINGAVG([Retail].[dbo].[Orders].[Freight])` |
| **RUNNINGCOUNT**  `RUNNINGCOUNT(expression)`  Any data type except Image and Lob. | Returns the number of unique values of expression from the first row up to the current row. | Numeric. | `RUNNINGCOUNT([Retail].[dbo].[Orders].[OrderID])` |

## List of Dateparts and Abbreviations

|  |  |
| --- | --- |
| Datepart | Abbreviations |
| **year** | **yy**, **yyyy** |
| **quarter** | **qq**, **q** |
| **month** | **mm**, **m** |
| **dayofyear** | **dy**, **y** |
| **day** | **dd**, **d** |
| **week** | **ww**, **wk** |
| **weekday** | **dw** |
| **hour** | **hh** |
| **minute** | **mi**, **n** |
| **second** | **ss**, **s** |
| **millisecond** | **ms** |
