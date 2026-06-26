---
title: "ReportDashboardSearchCriteria"
id: 4415492849559
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415492849559-ReportDashboardSearchCriteria
updated_at: 2021-12-10T03:09:15Z
---

# ReportDashboardSearchCriteria

# ReportDashboardSearchCriteria

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **criterias**  array of objects |  | An array of [SearchCriteria](https://devnet.logianalytics.com/hc/en-us/articles/4415512052759-SearchCriteria) objects |  |
| **sortCriteria**  object |  | A [SortOrder](https://devnet.logianalytics.com/hc/en-us/articles/4415512056215-SortOrder) object |  |
| **copyGlobal**  boolean |  | Searches copy global report or not |  |
| **type**  integer |  | The type   * 0 = Report * 1 = Template * 2 = Dashboard |  |
| **isUncategorized**  boolean |  | Searches uncategorized rows or not |  |
| **visibleCategoryIds**  array of strings (GUID) |  | List of visible category ids |  |
| **visibleSubCategoryIds**  array of strings (GUID) |  | List of visible sub-category ids |  |
| **visibleLocalUncategorized**  boolean |  | Whether local Uncategorized is visible |  |
| **visibleGlobalUncategorized**  boolean |  | Whether global Uncategorized is visible |  |
| **defaultChecked**  boolean |  | Default checked setting |  |
| **includeHascode**  boolean |  | Whether to compute hashcode |  |
| **timestampOffset**  real number |  | The timestamp offset |  |
| **includeGlobalCategory**  boolean |  | Whether to include global category |  |
| **isGlobal**  boolean | Y | Whether this instance is global |  |
| **includeUncategory**  boolean |  | Whether to include Uncategorized |  |

Deprecated since version 2.0.0: tenantId field is removed

**Sample**:

```
{"tenantId":null,"isUncategorized":false,"criterias":[{"key":"CategoryId"}]}
```
