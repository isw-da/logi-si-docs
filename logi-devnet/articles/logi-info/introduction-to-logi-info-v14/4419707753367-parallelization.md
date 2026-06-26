---
title: "Parallelization"
id: 4419707753367
section: "Introduction to Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707753367-Parallelization
updated_at: 2022-07-17T02:23:49Z
---

# Parallelization

# Parallelization

Logi v12 includes advances in "parallelization", the ability to execute multiple actions simultaneously. This translates into improved performance for the user. This technology improvement has been applied to the way the Logi Engine handles datalayers and Dashboard and tab panels.

## Datalayers

Data retrieval through datalayer elements is bounded by the longest performing query, rather than the *number* of queries. Multiple threads are launched at the web server to satisfy multiple requests and execute in parallel.

![](https://devnet.logianalytics.com/hc/article_attachments/7522807310359/serverengine_02.png)

These threads, and their execution times, are shown in the standard Debug Trace page, as shown above. This improves performance in pages with input elements, Data Tables, and data lists.

## Dashboard and Tab Panels

Dashboard and tabbed panel loading benefits greatly from parallelization.   
![](https://devnet.logianalytics.com/hc/article_attachments/7522807332375/serverengine_03.png)  
Dedicated threads for each panel allow parallel processing of panels, which improves performance, particularly when each panel has local parameters.
Testing of complex reports and Dashboards has shown up to a 4x performance improvement when upgraded to v12 to take advantage of Logi parallelization technology.
