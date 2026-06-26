---
title: "Filtering and Calculations in SQL Queries"
id: 4406817170967
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817170967-Filtering-and-Calculations-in-SQL-Queries
updated_at: 2022-04-06T06:04:26Z
---

# Filtering and Calculations in SQL Queries

# Filtering and Calculations in SQL Queries

As we saw in [Find Out What's Taking So Long](https://devnet.logianalytics.com/hc/en-us/articles/4406822183063-Find-Out-What-s-Taking-So-Long), it took a lot longer to use an element
to filter data compared to using a WHERE clause in the SQL query. This is
generally true: if the datasource is SQL-based or accepts queries, you
should do all the filtering and calculations that you can
*in the query*. The database server is going to process them much
more quickly than the Logi application on the web server can.

However, many datasources do not accept queries and that's one of the
reasons we have data filtering and manipulation elements.
