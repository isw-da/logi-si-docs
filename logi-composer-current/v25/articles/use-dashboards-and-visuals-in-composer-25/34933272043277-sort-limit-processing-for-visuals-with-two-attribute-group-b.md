---
title: "Sort &\u00a0Limit Processing for Visuals With Two Attribute Group-By Fields"
id: 34933272043277
section: "Use Dashboards and Visuals in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933272043277-Sort-Limit-Processing-for-Visuals-With-Two-Attribute-Group-By-Fields
updated_at: 2026-05-26T22:08:35Z
---

# Sort & Limit Processing for Visuals With Two Attribute Group-By Fields

# Sort & Limit Processing for Visuals With Two Attribute Group-By Fields

The logic used for sort and limit processing for visuals that use two attribute group-by fields (such as heat maps or floating bubble charts) requires additional explanation. The sort and limit logic used in Composer are linked to each other and are not global. Thus, the unique entries available for group 2 sort and limit processing depend on the number of unique entries produced by group 1 sort and limit processing.

## Limit Processing

In general, when two attribute group-by fields are used in a visual, the limit for group 1 affects the maximum number of elements available to be limited by group 2. So the limit for group 1 is applied first and the limit for group 2 is applied to the results of the limit for group 1. This limits the maximum number of subgroup elements within each group element.

### Heat Map Examples

In heat maps, you can apply a limit for both group 1 and group 2. The limit for group 2 depends on the results of the group 1 limit. The results from a group 1 limit should always match the limit set, but the results from a group 2 limit might match, but also might be less than the limit set. For example, if the limit for group 1 is 10, there should be 10 rows and columns in the result passed to the group 2 limit processing. So, if the limit for group 2 is also 10, fewer than 10 rows and columns may result from the group 2 limit processing.

Here is another heat map example. Suppose your heat map has:

* A group 1 limit of 10 and a group 2 limit of 5.
* From an absolute perspective, there are 100 unique group 1 values and 10 unique group 2 values.

Based on the first 10 unique group 1 values shown on the heat map, there might only actually be 4 corresponding unique group 2 values and thus, 4 will show for group 2 even though it has a limit of 5.

Now assume that the group 1 limit is increased to 25, but the group 2 limit is still 5. The first 25 unique group 1 values might have 5 or more unique group 2 values, in which case only 5 will show for group 2 because that is its limit. However, if the first 25 unique group 1 values still only have 4 corresponding unique group 2 values, group 2 will only have 4 rows and columns on the heat map.

Now assume that the group 1 limit is increased to 100 and the group 2 limit is increased to 10. As all the group 1 values are shown (there are only 100 unique group 1 values), all 10 unique group 2 values should show on the heat map, unless there is not enough space to render the full heat map. If this happens, the number of rows and columns for group 1 and group 2 respectively might be smaller.

## Sort Processing

In general, when two attribute group-by fields are used in a visual, the sort for group 1 sorts all the data and the sort applied by group 2 sorts the subgroup (group 2 elements) within each group 1 element. To verify that sorting has happened correctly, compare the aggregate results of each group 1 element using whatever metric function or calculation logic applied, but compare the group 2 subgroup elements within the same group 1 element to make sure group 2 sorting is correct. Do not rely on the individual results shown on the tooltip when hovering over a data point -- but look at the aggregate values for each group 1 element when verifying the sort logic.

For example, assume you have a heat map where group 1 refers to rows and group 2 refers to columns. In one row (we'll call it A) has one column with a really large value. however, if another row (B) has multiple columns that sum up to a larger value than the value in A), the B row will sort higher than the A row (assuming you are sorting in descending order by Sum). Here's an extreme heat map example. Suppose row A has a single column point with a value of 1,000,000 and row B has 12 column points (subgroup elements) with values of 100,000 each. If you are sorting in descending order by this same metric on group 1, row B will sort higher than row A. Thus there might be a data point in the middle of the heat map that appears with a much higher individual metric value, but the chart is still sorted correctly.

### Floating Bubble Sort Processing

Floating bubble charts have two groups and two metrics. The first group-by attribute represents data along the X-axis and the second group-by attribute is reflected along the Y-axis. Composer determines the correct place on a chart for a data point based on the first metric (on the Y axis). The second metric affects the size of the bubbles only. Consequently, when you sort by the first group-by attribute (X-axis), it affects the representation of data long the X-axis and when you sort by the second group-by attribute (Y-axis), it affects the representation along the Y-axis.

**Note:** 
Sort and limit processing in scatter plot visuals sort and limit the data returned to the scatter plot and **not** the way the scatter plot is rendered on the screen.
