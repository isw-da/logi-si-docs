---
title: "JavaScript API: Report and Dashboard Execution Timing"
id: 5281636421655
section: "JavaScript API"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281636421655-JavaScript-API-Report-and-Dashboard-Execution-Timing
updated_at: 2022-05-03T22:07:56Z
---

# JavaScript API: Report and Dashboard Execution Timing

# JavaScript API: Report and Dashboard Execution Timing

As of *v2019.1.3+*, Exago BI exposes a JavaScript API that may be invoked in the browser to execute reports and Dashboards and retrieve information about how long they take to run. This makes it easier to do benchmarking, especially for Dashboard executions where a test would need to wait until the last tile is finished loading.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> All report types and execution formats are supported in this API.

`wrWebReportsCtrl.ExecuteReport` now returns a `Promise` that resolves with the class that controls the given execution (one of `wrChainedExecuteClass`, `wrDashboardDesignCtrl`, `wrExecuteClass`, `wrExpressViewDesignCtrl`). Each of these classes exposes the `Timing` property, which is a `Promise` that resolves when execution timing information has finished being collected for the given execution.

```
const executor = await wrWebReportsCtrl.ExecuteReport("Reports\Report", "html");
await executor.Timing; // Evaluates to { load: 5243 }
```

The `Timing` property resolves with an object describing timing information about the report or Dashboard execution:

```
{
  load: 5243
}
```

Returns the time (in milliseconds) it took for the report or last Dashboard tile to finish loading.
