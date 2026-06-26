---
title: "Sorting Dimensions by Dates"
id: 4406817385495
section: "Use Logi Studio/SSRM - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817385495-Sorting-Dimensions-by-Dates
updated_at: 2022-04-06T06:05:46Z
---

# Sorting Dimensions by Dates

# Sorting Dimensions by Dates

Dates in dimension values are sorted as strings, which can be confusing.
To make a date-type dimension appear in sorted order across the Dimension
Grid, ensure that its data is returned into the datalayer as a DateTime
value in ISO 8601 format (yyyy-mm-dd). To sort the dimension by Month and
display the month number, you will need to **manually** setits
Xolap Level element's **Format** attribute to *MM* once the wizard
is finished. To sort it by Year and display the year number instead, set
this attribute to *yyyy*.
