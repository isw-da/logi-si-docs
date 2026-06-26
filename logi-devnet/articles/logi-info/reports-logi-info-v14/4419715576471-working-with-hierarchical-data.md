---
title: "Working with Hierarchical Data"
id: 4419715576471
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715576471-Working-with-Hierarchical-Data
updated_at: 2022-07-17T01:30:24Z
---

# Working with Hierarchical Data

# Working with Hierarchical Data

The Logi Engine also supports *hierarchical datasets* within
Word templates. You can use elements such as **Group Filters**  to
shape the data appropriately before assigning columns to Word Form Field
elements.
The Logi server engine *does not* dynamically copy or add fields to
the template based on the data returned in datalayer; at runtime, there
must be one form field in the template for every possible data column.
Developers must anticipate the maximum number of fields that could be
required by the data and provide them, or otherwise apply limits in their
queries.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714957847/fillwordtemp_06_636x161.png)

When working with hierarchical data, only one Word Form Field element is
required to fill repeating fields in a Word template. In the example
above, the Word Form Field element "fldUnits" provides the data
(from successive rows in the dataset) for all of the fields named Units\_01
thru Units\_06. You do not need one element for each form field.
