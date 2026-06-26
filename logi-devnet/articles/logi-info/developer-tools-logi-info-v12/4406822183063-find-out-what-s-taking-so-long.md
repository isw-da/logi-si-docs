---
title: "Find Out What's Taking So Long"
id: 4406822183063
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822183063-Find-Out-What-s-Taking-So-Long
updated_at: 2022-04-06T06:04:27Z
---

# Find Out What's Taking So Long

# Find Out What's Taking So Long

In Studio, you can turn on debugging
and view the Debugger Trace Report after a report definition runs, see [Debug Reports](https://devnet.logianalytics.com/hc/en-us/articles/4406817355543-Debug-Reports). It
provides detailed information about every step in the report execution.
Here's an example portion of the Debugger report and how you can use it to
see how long processing takes:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563461399/performance_02.png)

In the right-most column, you can see the execution times, with an
embedded chart, for each step. It took until 1.672 seconds into report
execution to retrieve that data and have it ready for analysis, based on a
SQL query without a WHERE clause. The report instead uses a
**Condition Filter** element to filter the datalayer after the query
returns the data.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575834519/performance_01.png)

The example above shows a similar query, however this one includes a WHERE
clause and a filter element is *not* used. We can see that it only
took until 0.325 seconds into report execution, more than
*five times* faster than the first example, to have the data ready
for analysis. Clearly, this is the faster approach.

You can use the Debugger Trace Page to find out where processing takes the
longest and to see how different code changes and element combinations
affect performance.
