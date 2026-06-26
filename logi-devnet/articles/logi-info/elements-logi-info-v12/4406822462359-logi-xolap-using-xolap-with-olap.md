---
title: "Logi XOLAP - Using XOLAP with OLAP"
id: 4406822462359
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822462359-Logi-XOLAP-Using-XOLAP-with-OLAP
updated_at: 2022-04-06T06:07:58Z
---

# Logi XOLAP - Using XOLAP with OLAP

# Logi XOLAP - Using XOLAP with OLAP

The XOLAP Cube element, and its child elements, which support the
Dimension Grid, can be also used with the **OLAP Grid** and
**OLAP Table** elements. This provides alternate datasources for the
OLAP elements and the ability to use the more flexible OLAP Grid with that
data.

What are the differences between the Dimension Grid and the OLAP Grid? The
Dimension Grid is designed to be less complicated to use and doesn't
support some features, such as multi-dimension sorting and multiple
dimensions on both axes, that are found in the OLAP Grid. So the OLAP Grid
allows more complex analysis of the XOLAP data.

The Dimension Grid, however, only displays data contained in Logi XOLAP
cubes; it's not able to connect to a OLAP cube, nor do we offer a
mechanism for building a XOLAP cube by querying an OLAP cube. Therefore,
you must use the OLAP Grid element, not a Dimension Grid, to display OLAP
data.
