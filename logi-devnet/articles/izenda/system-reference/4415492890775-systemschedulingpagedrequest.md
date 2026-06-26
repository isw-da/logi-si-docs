---
title: "SystemSchedulingPagedRequest"
id: 4415492890775
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415492890775-SystemSchedulingPagedRequest
updated_at: 2021-12-10T03:09:50Z
---

# SystemSchedulingPagedRequest

# SystemSchedulingPagedRequest

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **systemLevel**  boolean |  | Is the search at System level. |  |

Inherited fields:

## PagedRequest

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **tenantId**  string (GUID) | Y | The id of the tenant |  |
| **criteria**  array of objects |  | An array of [SearchCriteria](https://devnet.logianalytics.com/hc/en-us/articles/4415512052759-SearchCriteria) objects |  |
| **sortOrders**  array of objects |  | An array of [SortOrder](https://devnet.logianalytics.com/hc/en-us/articles/4415512056215-SortOrder) objects |  |
| **parentIds**  array of strings (GUIDs) |  | Ids of the parents |  |
| **pageIndex**  integer |  | The index of the page | Inherited from [PagingInfo](https://devnet.logianalytics.com/hc/en-us/articles/4415504741143-PagingInfo) |
| **pageSize**  integer |  | The size of the page | Inherited from [PagingInfo](https://devnet.logianalytics.com/hc/en-us/articles/4415504741143-PagingInfo) |
| **total**  integer |  | The total number of rows | Inherited from [PagingInfo](https://devnet.logianalytics.com/hc/en-us/articles/4415504741143-PagingInfo) |
| **skipItems**  integer |  | Skip items | Inherited from [PagingInfo](https://devnet.logianalytics.com/hc/en-us/articles/4415504741143-PagingInfo) |
| **isLastPage**  boolean |  | Whether this is the last page | Inherited from [PagingInfo](https://devnet.logianalytics.com/hc/en-us/articles/4415504741143-PagingInfo) |

**PagedRequest Sample**:

```
{"criteria":[{"key":"All","value":"","operation":1}],"pageIndex":1,"pageSize":10,"sortOrders":[{"key":"shareWith","descending":true}]}
```

**System SchedulingPagedRequest Sample**:

```
{"systemLevel":true,"tenantId":null,"pageIndex":1,"pageSize":10,"sortOrders":[{"key":"name","descending":true}],"criteria":[{"key":"ReportingType","value":""},{"key":"ReportDashboardName","value":""},{"key":"DeliveryType","value":""},{"key":"DeliveryMethod","value":""},{"key":"Recipients","value":""},{"key":"Type","value":""},{"key":"LastSuccessfulRun","value":""},{"key":"NextScheduledRun","value":""},{"key":"NextScheduledRunFrom","value":""},{"key":"NextScheduledRunTo","value":""},{"key":"LastSuccessfulRunFrom","value":""},{"key":"LastSuccessfulRunTo","value":""},{"key":"RecurrenceType","value":""},{"key":"ExportFileType","value":""},{"key":"CreatedBy","value":""}]}
```
