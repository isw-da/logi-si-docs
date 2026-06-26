---
title: "Datasource Language "
id: 4419722991127
section: "Manage - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722991127-Datasource-Language
updated_at: 2022-07-17T01:45:41Z
---

# Datasource Language 

# Datasource Language

Data displayed in Logi reports is typically stored in datasources external to the Logi application and these datasources may have their own language- or culture-specific configuration possibilities. This is significant for the developer and may require coordination with IT system administrators to ensure proper configuration.
In particular, database servers often have language configuration options or are available in language-specific product versions. The specifics of these are beyond the scope of this topic, but system and database administrators involved with databases providing data for globalized Logi applications need to concern themselves with issues such as:

* Character encoding (Unicode, UTF8, etc.)
* Collation
* Case-sensitivity
* Accent-sensitivity

Database server vendors often have extensive information available about their products and globalization. Here are some vendor resources:
Microsoft - *[International Considerations for SQL Server 2008 R2](https://docs.microsoft.com/en-us/previous-versions/sql/sql-server-2008-r2/ms142795(v=sql.105)?redirectedfrom=MSDN)*  
Oracle - *[Database Globalization Support Guide for 11g](http://download.oracle.com/docs/cd/B28359_01/server.111/b28298/toc.htm)*
