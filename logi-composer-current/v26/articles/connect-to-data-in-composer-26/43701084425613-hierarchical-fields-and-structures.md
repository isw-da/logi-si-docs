---
title: "Hierarchical Fields and Structures"
id: 43701084425613
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701084425613-Hierarchical-Fields-and-Structures
updated_at: 2026-05-29T14:08:22Z
---

# Hierarchical Fields and Structures

# Hierarchical Fields and Structures

**Note:** 
Hierarchical fields are enabled by default at the server level. Work with [Technical Support](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072313613-Contact-Technical-Support) to disable.

Logi Composer now supports common hierarchical structures you can use to visualize and organize your data. Hierarchies create parent-child tree-based, and field-level hierarchical structures using your source data.

When you organize your data in Logi Composer in hierarchies, it's easier to access for analytical processing, for data traversal, and keyword searching. To view your data in a hierarchical format, create a data source that defines a hierarchy using data in an adjacency list structure, add one or more hierarchy fields to your source, and use the hierarchical field in the context of a group or filter on pivot table visuals or other visuals.

See the following topics for more information:

* [Define a Hierarchical Source](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701100433165-Define-a-Hierarchical-Source)
* [Edit a Hierarchical Source](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701096930061-Edit-a-Hierarchical-Source)
* [Define a Hierarchy Field for Your Source](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701079796493-Define-a-Hierarchy-Field-for-Your-Source)
* [Filter by Hierarchy Field](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701118747917-Filter-by-Hierarchy-Field)
* [Apply Hierarchical Groups](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701032076813-Apply-Hierarchical-Groups)
* [Apply Hierarchical Filters to a Pivot Table Visual](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701096655501-Apply-Hierarchical-Filters-to-a-Pivot-Table-Visual)
* [Apply Hierarchical Filters to Visuals](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701068080653-Apply-Hierarchical-Filters-to-Visuals)
* [Sunburst](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701214045197-Sunburst)

## Limitations

* Cycles in hierarchies are not supported.
* Hierarchical groups are available in the Pivot Table visual as a single hierarchical group in rows.
* Hierarchical groups are available as multiple groups in the Sunburst visual.
* When you use a hierarchical group, simple metrics are calculated for all hierarchy levels by default. Specify **Use Rollup** to roll data up to parent levels as needed in pivot tables.
* Data sharpening and viewing data changes using the time bar are not available.
* By default, simple metrics are included; enable **Use Rollup** to roll data up to the parent levels in pivot tables.
* Aggregate filters are not available.
* Pagination is not supported in pivot table visuals that use hierarchical groups. To view your entire hierarchy, adjust the rows per page limit to accommodate all items of the hierarchy.
