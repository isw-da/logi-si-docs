---
title: "SubscriptionPagedRequest"
id: 4415492887831
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415492887831-SubscriptionPagedRequest
updated_at: 2021-12-10T03:09:50Z
---

# SubscriptionPagedRequest

# SubscriptionPagedRequest

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **reportId**  string (GUID) | Y | The id of the report if available |  |
| **dashboardId**  string (GUID) | Y | The id of the dashboard if available |  |
| **isSubscription**  boolean |  | Used internally: is this a subscription request |  |
| **isReportingOwner**  boolean |  | Used internally: is current user the report/dashboard owner |  |
| **createdById**  string (GUID) | Y | Used internally |  |
| **subscriptions**  array of objects |  | An array of subscriptions, should be populated in case modifications are not yet saved to database |  |

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

**SubscriptionPagedRequest Sample**:

```
{"dashboardId":"a496ad94-fe92-48d5-a285-e45be738921f","isSubscription":true,"tenantId":null,"criteria":[{"key":"All","value":"","operation":1}],"pageIndex":1,"pageSize":10,"sortOrders":[{"key":"name","descending":true}]}
```
