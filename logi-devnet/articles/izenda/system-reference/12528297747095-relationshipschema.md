---
title: "RelationshipSchema"
id: 12528297747095
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528297747095-RelationshipSchema
updated_at: 2023-02-23T16:40:43Z
---

# RelationshipSchema

RelationshipSchema

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **joinQuerySourceId** string (GUID) |  | The id of the query source containing the relationship |  |
| **foreignQuerySourceId** string (GUID) |  | The id of the query source referenced by the relationship |  |
| **twoWays** boolean |  | Is this a two-way relationship | “Inner”, “Full” and “Cross” join types are two-way while “Left” and “Right” are not |
