---
title: "Link Datalayers"
id: 4419715407255
section: "Datalayers - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715407255-Link-Datalayers
updated_at: 2022-07-17T01:42:22Z
---

# Link Datalayers

# Link Datalayers

When datalayers run, they *retrieve* and *cache* data. Performance may be improved by minimizing the re-running of datalayers, especially if long-running queries are involved, by allowing a datalayer to *share* data that's already been cached by another datalayer.

Developers are always looking for ways to improve performance, particularly where database queries are concerned. You can improve the performance of your Logi applications by eliminating repeatedqueries of the same data, through use of a feature that allows data retrieved into one datalayer to be saved and re-used elsewhere within the application.
Two elements are used in this process: the first one, **Data Layer Link**, identifies the data to be saved and made available; and the second one, **DataLayer.Linked**, provides a way to access and re-use that data.

The following topics discuss the technique of linking datalayers:

* [Making a DataLayer Link Available](https://devnet.logianalytics.com/hc/en-us/articles/4419707732759-Making-a-DataLayer-Link-Available#Available)
* [Linking Within the Same Definition](https://devnet.logianalytics.com/hc/en-us/articles/4419723063831-Linking-Within-the-Same-Definition#SameDef)
* [Linking Across Different Definitions](#DifferentDefs)
