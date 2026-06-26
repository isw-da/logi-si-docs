---
title: "RelationshipSchema"
id: 4415492841111
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415492841111-RelationshipSchema
updated_at: 2021-12-10T03:09:12Z
---

# RelationshipSchema

# RelationshipSchema

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **joinQuerySourceId**  string (GUID) |  | The id of the query source containing the relationship |  |
| **foreignQuerySourceId**  string (GUID) |  | The id of the query source referenced by the relationship |  |
| **twoWays**  boolean |  | Is this a two-way relationship | “Inner”, “Full” and “Cross” join types are two-way while “Left” and “Right” are not |
