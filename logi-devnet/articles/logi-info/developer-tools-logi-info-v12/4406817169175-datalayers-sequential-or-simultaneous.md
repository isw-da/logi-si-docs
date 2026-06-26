---
title: "Datalayers: Sequential or Simultaneous?"
id: 4406817169175
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817169175-Datalayers-Sequential-or-Simultaneous
updated_at: 2022-04-06T06:04:26Z
---

# Datalayers: Sequential or Simultaneous?

# Datalayers: Sequential or Simultaneous?

The Logi Server Engine will usually run multiple datalayers in the same
definition *simultaneously*, in separate server process threads, to
provide the best performance. You can see this happening by examining the
Debugger Trace Report: each datalayer running in its own thread will have
a "Thread for Datalayer ID" reference.

An exception to this is when datalayers are used under multiple
**Local Data** elements. The Local Data elements (and their datalayers)
are run *sequentially*, one after the other, in the top-to-bottom
order of the elements in the definition. This is done so that the data
from one datalayer can be used as criteria in a query in the next
datalayer. There is no way to avoid this other than planning your
application carefully to minimize the use of multiple Local Data elements,
if data retrieval performance becomes an issue.
