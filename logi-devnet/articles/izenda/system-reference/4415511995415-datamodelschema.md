---
title: "DataModelSchema"
id: 4415511995415
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415511995415-DataModelSchema
updated_at: 2021-12-10T03:08:37Z
---

# DataModelSchema

# DataModelSchema

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **querySources**  array of objects |  | An array of [QuerySourceSchema](https://devnet.logianalytics.com/hc/en-us/articles/4415492835479-QuerySourceSchema) objects |  |
| **relationships**  array of objects |  | An array of [RelationshipSchema](https://devnet.logianalytics.com/hc/en-us/articles/4415492841111-RelationshipSchema) objects |  |

**Sample**:

```
{"querySources":[{"id":"8aa52ba9-8324-4b8e-bf42-619a3f050aa5","name":"dbo.Customers","type":"Table","color":null,"connectionId":"8195a480-ddd8-4915-95a0-432e24fed0ad","modified":"2016-04-19T03:08:56.091528","fields":[{"name":"ContactName","properties":""},{"name":"CustomerID","properties":"{\"PrimaryKey\":true}"}]},{"id":"66dcf36e-e4b0-4c9b-9919-b9ba49377784","name":"dbo.Orders","type":"Table","color":null,"connectionId":"8195a480-ddd8-4915-95a0-432e24fed0ad","modified":"2016-12-19T03:08:56.091528","fields":[{"name":"CustomerID","properties":""},{"name":"OrderDate","properties":""},{"name":"OrderID","properties":"{\"PrimaryKey\":true}"}]},{"id":"26efbdf4-c724-4824-bd9c-6ae1e2dc7435","name":"dbo.Order Details","type":"Table","color":null,"connectionId":"8195a480-ddd8-4915-95a0-432e24fed0ad","modified":"2016-12-19T03:08:56.091528","fields":[{"name":"OrderID","properties":"{\"PrimaryKey\":true}"},{"name":"ProductID","properties":"{\"PrimaryKey\":true}"},{"name":"Quantity","properties":""},{"name":"UnitPrice","properties":""}]}],"relationships":[{"joinQuerySourceId":"8aa52ba9-8324-4b8e-bf42-619a3f050aa5","foreignQuerySourceId":"66dcf36e-e4b0-4c9b-9919-b9ba49377784","twoWays":false},{"joinQuerySourceId":"66dcf36e-e4b0-4c9b-9919-b9ba49377784","foreignQuerySourceId":"26efbdf4-c724-4824-bd9c-6ae1e2dc7435","twoWays":true}]}
```
