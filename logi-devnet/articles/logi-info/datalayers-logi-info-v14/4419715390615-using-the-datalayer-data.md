---
title: "Using the Datalayer Data"
id: 4419715390615
section: "Datalayers - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715390615-Using-the-Datalayer-Data
updated_at: 2022-07-17T01:43:30Z
---

# Using the Datalayer Data

# Using the Datalayer Data

The following example shows how the data in a Data Table corresponds with the XML data retrieved using DataLayer.SQL to query the Northwind database:

![](https://devnet.logianalytics.com/hc/article_attachments/4419714846231/introdl_13.png)

The SQL query used was:

SELECT EmployeeID, LastName, FirstName, Title FROM Employees

The Logi Engine converts data retrieved from any datasource into XML. Each row from the datasource is equivalent to one XML element and each column is equivalent to one XML attribute. For example, the Data Table shown above contains four columns and nine rows, which is equivalent to nine XML elements, each with four attributes.

Data retrieved by a datalayer is cached in memory and/or on the web server's file system. The latter is discussed in [The Logi Server Engine](https://devnet.logianalytics.com/hc/en-us/articles/4419715421975-The-Logi-Server-Engine) and may be of interest to developers working with extremely large datasets or large numbers of concurrent users.

Data retrieved by the DataLayer.XML and DataLayer.Web Service elements may need to be reformatted for use, and the **XslTransform** element is available for this purpose.

Use of "bracketed" column names, such as "[Order Date]", is supported. The brackets allow column names to include spaces, special characters, or SQL reserved words.

The data retrieved with a datalayer is available using **@Data** tokens, in the format @Data.*ColumnName*~. The spelling of the column name is **case-sensitive**.

For example, @Data.LastName~ retrieves all values, in all rows, for the *LastName* column. This might sound as if you get all the data in one place in your report but you don't. When the reporting engine generates the report, it **iterates** through each row in the datalayer; the @Data token at any point in time represents the value in a column for the *current* row in the iteration.

## Data Scope

The scope, or availability, of data is generally limited to the element (Data Table, Chart, etc.) which is the parent element of the datalayer element used to retrieve the data. The following example illustrates the use of multiple datalayers and the availability of their data.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699826583/introdl_05.png)  

1. The Data Table element within the *div1* division can only use data from *DataLayer\_1* datalayer.
2. The chart's Series.Area element within the *div2* division can only use data from the *DataLayer\_2* datalayer.
3. The Data Table element within the *div3* division can also use the data from *DataLayer\_1* by virtue of the two elements, Data Layer Link and DataLayer.Linked, which link it to the datalayer's cached data.

Linking datalayers is a very useful practice, allowing the data retrieved into one datalayer to be available for re-use in another. This eliminates extra datasource queries and improves performance. For more information, see [Link Datalayers](https://devnet.logianalytics.com/hc/en-us/articles/4419715407255-Link-Datalayers).
