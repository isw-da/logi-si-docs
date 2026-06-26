---
title: "Datalayer Problems"
id: 4406822540311
section: "Manage - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822540311-Datalayer-Problems
updated_at: 2022-04-06T06:08:57Z
---

# Datalayer Problems

# Datalayer Problems

This topic introduces the different types of datalayer problems you could run into when developing Logi Studio, as well as possible solutions.

Problems Displaying Query Results:

* To display query results, use the token
  @Data.column\_name~ to access the data in
  each column returned. Token names are *case-sensitive*, so ensure
  that the case of the token matches the column name returned in the
  datalayer.
* Data returned into a datalayer can be examined using links on the
  Debugger Trace Report; turn on debugging links to view this page.

Joining Datalayers:

* Relationships between datalayers in a report can be created using a
  Join element, see [Join Datalayers](https://devnet.logianalytics.com/hc/en-us/articles/4406816923031-Join-Datalayers). This can be used to produce SQL-like joins of data from SQL and
  non-SQL datasources.
