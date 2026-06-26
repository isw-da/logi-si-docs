---
title: "The File Column (BLOBs)"
id: 4419707590295
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707590295-The-File-Column-BLOBs
updated_at: 2022-07-17T01:49:00Z
---

# The File Column (BLOBs)

# The File Column (BLOBs)

Many database servers allow you to store Binary Large Objects
**(BLOBs**) or Character Large Objects (**CLOBs**) in a table
column. Logi Info developers can manipulate this kind of data using the
**File Column** element.

The following topics discuss the File Column element:

* [Preparing Data in a Datalayer](https://devnet.logianalytics.com/hc/en-us/articles/4419715299735-Preparing-Data-in-a-Datalayer#Datalayer)
* [Working with Retrieved Data](https://devnet.logianalytics.com/hc/en-us/articles/4419722920599-Working-with-the-Retrieved-Data-#WorkingData)
* [Example: Retrieving Dashboard Configuration Data](https://devnet.logianalytics.com/hc/en-us/articles/4419722919575-Example-Retrieving-Dashboard-Configuration-Data#DashbdData)

## About BLOBs and CLOBs

The ability of some database servers to store large amounts of data in
individual table columns provides a interesting challenge for data storage
and retrieval. A common BLOB implementation example is an HR table that
stores employee data and includes an actual *photo* of each employee
in one of its columns. Other examples of BLOBs include audio and
multimedia objects, and even executable code.

Other implementations may store large amounts of *text*, called
CLOBs, in the same manner. For example, the HTML for entire web pages
could be stored in a single table column as part of a content management
system. Other examples of CLOBs include XML data, documents, and logs.

BLOB and CLOB data may be stored as a collection of bytes right in the
database's standard storage area or they may reside outside it, in
auxiliary files, referenced by pointers in the table column record. The
size of a BLOB or CLOB can be quite large; for example, ODBC and JDBC
specs allow up to 4GB of data.

Let's see how this kind of data can be retrieved for use in a Logi
application.
