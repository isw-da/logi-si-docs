---
title: "Debugging Datalayers"
id: 4419715385495
section: "Datalayers - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715385495-Debugging-Datalayers
updated_at: 2022-07-17T01:43:36Z
---

# Debugging Datalayers

# Debugging Datalayers

Datalayer results and performance can be viewed during development using the Debugger Trace Report:

![](https://devnet.logianalytics.com/hc/article_attachments/4419714841623/introdl_14.png)

The debug information for a typical DataLayer.SQL run is shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599575/noteicon.png) This is *very* useful in determining the exact query (especially if tokens are being used) and the execution time required. The actual data retrieved can also be viewed using the Memory Stream Data link. If multiple datalayers run concurrently, they'll be shown here with individual links to their details.

Element IDs for datalayers are optional. However, we suggest you *always* provide a unique datalayer element ID, for ease in understanding the definition and, significantly, so that the datalayers are easily identified in the Debugger Trace page.

More information about use of the debugger can be found in [Debug Reports](https://devnet.logianalytics.com/hc/en-us/articles/4419715245463-Debug-Reports).
