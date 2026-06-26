---
title: "ReportDashboardSearchCriteria"
id: 12528297833495
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528297833495-ReportDashboardSearchCriteria
updated_at: 2023-02-19T08:37:05Z
---

# ReportDashboardSearchCriteria

[Skip To Main Content](#)

Account

Settings

---

Logout

* placeholder

Account

Settings

---

Logout

Filter: 

* All Files

Submit Search

# ReportDashboardSearchCriteria

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **criterias**  array of objects |  | An array of [SearchCriteria](https://devnet.logianalytics.com/hc/en-us/articles/12528283106455-SearchCriteria) objects |  |
| **sortCriteria**  object |  | A [SortOrder](https://devnet.logianalytics.com/hc/en-us/articles/12528298506903-SortOrder) object |  |
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
