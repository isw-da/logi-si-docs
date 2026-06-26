---
title: "String Functions"
id: 4406817398167
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817398167-String-Functions
updated_at: 2022-04-06T06:05:53Z
---

# String Functions

# String Functions

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) The functions listed in the table below are for SQL queries and should not be used with inline scripts.

The following table lists the string functions used in Logi Info:

| Function | Description/Example |
| --- | --- |
| CONCATENATE(string1, string2, ...) | Returns a string that is the result from joining two or more string values. e.g. CONCATENATE('Hello ', 'World') returns 'Hello World' |
| FIND(string,substring, start) | Returns the starting position of substring in string. The first character is in position 1 and the function returns 0 if the substring is not found. The optional start parameter can be used to control the search start position. e.g. FIND('Hello World', 'ello',1) returns 2 |
| INSERT(string, start, length, substring) | Inserts a substring into string, at the specified position. The length determines how many of the original characters are overwritten by the new substring. E.g. INSERT('This is a test', 5, 4, ' really') returns 'This reallya test' and INSERT('This is a test', 5, 0, ' really') returns 'This really is a test' |
| LEFT(string, number) | Returns the specified number of characters from the left side of the string. e.g. LEFT('Hello World', 5) returns 'Hello' |
| LEN(string) | Returns number of characters in a text string. e.g. LEN('Hello World') returns 11 |
| LOWER(string) | Returns a string with all the letters in lowercase. e.g. LOWER('Hello World') returns 'hello world' |
| MID(string, start, length) | Returns the characters from the start position for the specified length. e.g. MID('Hello World', 4, 4) returns 'lo W' |
| RIGHT(string, number) | Returns the specified number of characters from the right side of the string. e.g. RIGHT('Hello World',5) returns 'World' |
| SQL\_FUNCTION(string) | (For Microsoft SQL Server only) Adds the provided string directly to the final T-SQL command sent to the database server, without any changes. In order to prevent SQL injection attacks, by default this function is disabled. Update the configuration in order to enable support. e.g. SQL\_FUNCTION('[Freight] + 5') would send [Freight] + 5 to the database. |
| TRIM(string) | Returns a string with any leading and trailing spaces removed. e.g. TRIM(' Hello World ') returns 'Hello World' |
| UPPER(string) | Returns a string with all the characters in uppercase. e.g. UPPER('Hello World') returns 'HELLO WORLD' |
