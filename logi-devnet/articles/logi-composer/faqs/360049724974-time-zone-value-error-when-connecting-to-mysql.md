---
title: "Time Zone Value Error When Connecting to MySQL"
id: 360049724974
section: "FAQs"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/360049724974-Time-Zone-Value-Error-When-Connecting-to-MySQL
updated_at: 2023-03-30T12:30:05Z
---

# Time Zone Value Error When Connecting to MySQL

**Issue:**

When attempting to connect to a MySQL database, the following error occurs:

```
Failed to establish connection. Cannot create PoolableConnectionFactory   
(The server time zone value 'EDT' is unrecognized or represents more than   
one time zone. You must configure either the server or JDBC driver (via   
the serverTimezone configuration property) to use a more specific time   
zone value if you want to utilize time zone support.)
```

**Answer:**

This issue is due to the server time zone configuration, which is set to a non-UTC time zone. In order to avoid this issue, please add

```
serverTimezone=UTC
```

as part of your JDBC connection string parameter, preceding with **?** if it's the only parameter, or **&** if there are multiple parameters in the string.

**Further Reading**

StackOverflow article: <https://stackoverflow.com/questions/26515700/mysql-jdbc-driver-5-1-33-time-zone-issue>
