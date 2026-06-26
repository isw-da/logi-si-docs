---
title: "Izenda Operators"
id: 12528296558359
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528296558359-Izenda-Operators
updated_at: 2023-02-23T15:58:02Z
---

# Izenda Operators

# Izenda Operators

## List of Operators

| Operator | Description | Result Data Types | Examples |
| --- | --- | --- | --- |
| **+ (Text Concatenation)**  `expression      +   expression`  Text + Text | Concatenates two text values in that exact order.   Not supported by Oracle and PostgreSQL. In cases where Oracle or PostgreSQL raises an error, please use the `CONCATfunction` instead. | Text | To return employee’s full name from [FirstName] and [LastName] columns:  `[FirstName]+''+[LastName]` |
| **+ Add**  `expression      +   expression`  Numeric/Money + Numeric/Money   Datetime + Numeric   Numeric + Datetime | Adds two numbers or two currency amount, or adds a number of days to a date. | The data type with the higher prededence. | Two and a half days from hire date:  `[HireDate]+2.5` |
| **- (Subtract)**  `expression      -   expression`  Numeric/Money - Numeric/Money   Datetime - Numeric | Subtracts two numbers or two currency amount, or subtracts a number of days from a date. | The data type with the higher prededence. | The number of products in stock after 10 have been taken out:  `UnitsInStock-10` |
| **\* (Multiply)**  `expression      *   expression`  Numeric/Money \* Numeric/Money | Multiplies two numbers, or a currency amount with a number. | Number | Price after 15% discount:  `UnitPrice*0.85` |
| **/ (Divide)**  `expression      /   expression`  Numeric/Money / Numeric/Money | Divides one number or currency amount by another. | Number | Price after 50% discount:  `UnitPrice/2` |
| **= (Equals)**  `expression      =   expression`  Any data type except Image and Lob. | Compares the equality in value of two expressions. The expression of the lower precedence data type is converted to the higher precedence data type in case data types are different. | Boolean | Employees named ‘John’:  `[FirstName]='John'` |
| **> (Greater Than)**  `expression      >   expression`  Any data type except Image and Lob. | Compares if the value of the first expression is higher than the second expression. The expression of the lower precedence data type is converted to the higher precedence data type in case data types are different. | Boolean | Products with more than 10 units in stock:  `UnitsInStock>10` |
| **< (Less Than)**  `expression      <   expression`  Any data type except Image and Lob. | Compares if the value of the first expression is lower than the second expression. The expression of the lower precedence data type is converted to the higher precedence data type in case data types are different. | Boolean | Products with less than 3 units in stock:  `UnitsInStock<3` |
| **>= (Greater Than or Equal To)**  `expression      >=  expression`  Any data type except Image and Lob. | Compares if the value of the first expression is higher than or equal to the second expression. The expression of the lower precedence data type is converted to the higher precedence data type in case data types are different. | Boolean |  |
| **<= (Less Than or Equal To)**  `expression      <=  expression`  Any data type except Image and Lob. | Compares if the value of the first expression is lower than or equal to the second expression. The expression of the lower precedence data type is converted to the higher precedence data type in case data types are different. | Boolean |  |
| **<> (Not Equal To)**  `expression      <>  expression`  Any data type except Image and Lob. | Compares if the value of the first expression is not equal to the second expression. The expression of the lower precedence data type is converted to the higher precedence data type in case data types are different. types are different. | Boolean | Products still available in stock:  `UnitsInStock<>0` |
