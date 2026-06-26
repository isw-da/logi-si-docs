---
title: "RoleVirtualNode"
id: 4415504790167
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415504790167-RoleVirtualNode
updated_at: 2021-12-10T03:09:42Z
---

# RoleVirtualNode

# RoleVirtualNode

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **isLastPage**  boolean |  | Is the last page or not |  |
| **name**  string |  | The role name or user name |  |
| **childNodes**  an array of object |  | An array of [RoleVirtualNode](#) |  |
| **numOfChilds**  integer |  | The number of children |  |
| **checked**  boolean |  | Whether this instance is selected |  |
| **indeterminate**  boolean |  | * true if 0 < numOfCheckedChilds < numOfChilds * false if not |  |
| **numOfCheckedChilds**  integer |  | The number of selected children |  |
| **totalItems**  integer |  | The total of items |  |
| **id**  string(GUID) |  | The id of role or user |  |
