---
title: "Preparing to Run the Dimension Grid Wizard"
id: 4406817384471
section: "Use Logi Studio/SSRM - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817384471-Preparing-to-Run-the-Dimension-Grid-Wizard
updated_at: 2022-04-06T06:05:46Z
---

# Preparing to Run the Dimension Grid Wizard

# Preparing to Run the Dimension Grid Wizard

Prior to running the Dimension Grid wizard:

* Become familiar with the data you'll be working with. Identify the data
  columns that will become *dimensions* and *measures*, what
  *values* (aggregations) you need, and how you might want to
  *filter* the data.
* Ensure that you have a valid **Connection** configured in \_settings
  and can connect to your datasource.
* If you're using a SQL data source, you may care to experiment a bit in
  the Query Builder to develop the query that you'll need.
* You should also keep an eye on the number of result rows your query is
  likely to return. While Logi XOLAP can process tens of thousands of data
  rows into an XML cube very quickly, millions of result rows may produce
  unacceptable delays.

Now, launch Studio and open your report definition.
