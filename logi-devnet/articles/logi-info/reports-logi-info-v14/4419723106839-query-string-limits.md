---
title: "Query String Limits"
id: 4419723106839
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723106839-Query-String-Limits
updated_at: 2023-07-06T15:16:28Z
---

# Query String Limits

# Query String Limits

There *are* limits on the amount of data you can pass in a query string. The first limit is **length**: browsers do not accept an unlimited number of characters in a URL. Moreover, the limit varies by browser, as follows:

| Browser | Max URL Bytes |
| --- | --- |
| Microsoft IE | 2,048 |
| Microsoft Edge | ~80K |
| Firefox | 65K |
| Chrome & Safari | 80K |
| Opera | 190K |

Trying to pass very large amounts of data in the query string is generally *not* a good idea. For example, instead of querying data in Report 1 and then passing *all* of it to Report 2 in the query string, you might instead pass only the key data and re-execute the database query in Report 2. If it's not feasible to run the database query twice, another approach is to use linked datalayers that span the two reports, sharing the query results.

The second limit is in the Logi Server Engine itself. It uses a fixed-size **array** with **100****rows** to process request parameters. If you try to pass 101 parameters in your query string, an "index out of range" error will occur.

In summary, when passing data in query strings, don't exceed the length limit of the target browsers and don't pass more than 100 items as request parameters.
