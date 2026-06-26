---
title: "Logi OLAP - Re-using the MDX Query"
id: 4419715376151
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715376151-Logi-OLAP-Re-using-the-MDX-Query
updated_at: 2022-07-17T01:44:20Z
---

# Logi OLAP - Re-using the MDX Query

# Logi OLAP - Re-using the MDX Query

Many of Logi's other data visualization components are capable of
"2-D" representation of OLAP cube data, using MDX queries. So it
may be useful to be able to access the MDX query used in an OLAP Grid in
one report for use with non-OLAP elements in another report.
Each time the OLAP Grid is manipulated during runtime, a session variable
is updated to reflect the resulting MDX query. This session variable,
rdOlapLastMdxQuery, is available to other reports, Logi or otherwise. In a
Logi report, it would be accessed using the token
@Session.rdOlapLastMdxQuery~.
