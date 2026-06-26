---
title: "The Oracle Connection String"
id: 4419723102231
section: "Connect to Data - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723102231-The-Oracle-Connection-String
updated_at: 2022-07-17T01:40:49Z
---

# The Oracle Connection String

# The Oracle Connection String

The Connection String for an Oracle database requires a **special parameter** that you must code manually.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714867991/orapkgs_01.png)

Add the following parameter, highlighted above, to your Connection element's **Connection String** attribute:
PLSQLRSet=1
This informs the OLEDB provider that row sets can be returned (in the example above, an OLEDB provider supplied by Oracle has been installed and is used).
Check here to see examples of [Oracle connection strings](http://www.connectionstrings.com/?carrier=oracle) for a variety of configurations and circumstances. All must include the parameter shown above in order to return row sets.
