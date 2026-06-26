---
title: "The File Column Example: Retrieving Dashboard Configuration Data"
id: 4406822332951
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822332951-The-File-Column-Example-Retrieving-Dashboard-Configuration-Data
updated_at: 2022-04-06T06:06:12Z
---

# The File Column Example: Retrieving Dashboard Configuration Data

# The File Column Example: Retrieving Dashboard Configuration Data

Here's an example scenario where the configuration data for a
super-element, the Dashboard, which is usually saved to an XML file, is
also saved to a database table and retrieved using the
**File Column** element.

## Requirements

* Your database server must be capable of saving a CLOB in a data column.
  This example uses Microsoft SQL Server 2008 R2, which has an
  "XML" data type (also available on MS SQL Server 2012).
* The database account used to connect to the server must have permissions
  for **Bulk** insert/update operations.
* A database table must exist that includes the following schema:  
    
  UserNameVARCHAR(50)-- a unique identifier for retrieving the record SaveFile XML

## Writing the Data

We'll use a Process task to write the data to the database. This
task can be called by a user action, such as clicking a "Save"
button or link, or logging out of the application, or by something more
automatic, such as the end of the session.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583938455/filecol_04_627x158.png)

An example of the task is shown above. Writing the data relies on a SQL
command that reads directly from a file:

INSERT INTO DashboardData   
 SELECT '@Function.UserName~', SaveFile  
 FROM (  
 SELECT \* FROM OPENROWSET (BULK
'@Function.AppPhysicalPath~\SavedDashboards\@Function.UserName~.xml',
SINGLE\_CLOB)   
 AS SaveFile) AS R(SaveFile)

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) The second SELECT statement line is wrapped on this page and
should be all one line.

This example assumes that the user name is available as a token, either
through Logi Security or another security scheme. The user name is then
used in the SQL command to provide a value for the unique identifier
column, and for the name of the dashboard save file. This syntax is
correct for MS SQL Server 2012 and 2008 R2 but may vary for other database
servers.

Naturally, the Dashboard will have to be used at least once so its
configuration is saved to its Save File before the data can be written to
the database.

## Reading the Data

When running the report, the data stored in the database needs to be read
once and saved to an XML data file on the web server that the Dashboard
element can use.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563290647/filecol_05_632x180.png)

We'll do this, as shown above, with a **Local Data** element. Its
**Condition** attribute can be set in some manner to ensure that it
only runs the first time the page is displayed (@Request token, cookie,
etc.). Data retrieval will take place using **DataLayer.SQL** using a
query similar to:

SELECT SaveFile FROM DashboardData WHERE UserName = 'Bob'

The use of Local Data allows important data to be available, using an
@Local token, anywhere in the rest of the definition.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575699863/filecol_06_600x210.png)

A shown above, a File Column element is used to extract the stored data
from the database column and save it as a file on the web server. The
complete Filename attribute would be something like:

@Function.AppPhysicalPath~\SavedDashboards\@Function.UserName~.xml

which you'll recognize as matching the file path and name used in the SQL
INSERT command in the previous section. File Column will overwrite any
existing file when it saves the XML data.

## Using the Data in the Dashboard

Finally, the Dashboard element needs to be configured to use the
newly-written data file:

![](https://devnet.logianalytics.com/hc/article_attachments/4417583938839/filecol_07.png)

When configuring the Dashboard element's **Save File** attribute, you
can use the
@Function.AppPhysicalPath~\...
string we used earlier, or you can use a combination of Local Data tokens
created by the File Column element, such as:

@Local.colFilePath~\@Local.colFileName~

if you aren't tying the Save File to individual users.
This approach, storing configuration data in an XML data type column in a
database table, is also applicable to other super-elements, such as the
Analysis Grid.
