---
title: "Events Created by Client"
id: 34933097007245
section: "Composer 25 Reference Information"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933097007245-Events-Created-by-Client
updated_at: 2026-05-26T22:07:53Z
---

# Events Created by Client

# Events Created by Client

## Thread Events

| Event | Description |
| --- | --- |
| thread:start | Thread is starting. |
| thread:stop | Thread is stopping. |
| thread:pause | Thread is pausing. Relevant only for time bar visuals. |
| thread:unpause | Thread is resuming. Relevant only for time bar visuals. |
| thread:updateSpeed | Thread's speed is updating. Relevant only for time bar visuals. |
| thread:message | Thread is sending data, which is returned as a packet by the listener to a callback function. |
| thread:error | An error occurred on the thread. The error message is included in the event, which is returned as a packet by the listener to a callback function. |
| thread:startVisDone | Thread has finished starting the visual. |
| thread:stopVisDone | Thread has finished stopping the visual. |
| thread:noData | Thread has found no data. |
| thread:dirtyData | Data is currently being read. Not fully sharpened yet. |
| thread:notDirtyData | All the data has been read and is fully sharpened. |
| thread:pauseDone | Thread has finished pausing. For time bar sources. |
| thread:unpauseDone | Thread has finished resuming. For time bar sources. |
| thread:pagination | Pagination for most visuals. |
| thread:pivotPaging | Separate paging event for Pivot Table visual. |
| thread:viewport | Viewport has updated. |
| thread:timeline | Reports time window currently being queried. |

## Visualization Events

| Event | Description |
| --- | --- |
| showReflinePopup | Show Reference Line pop-up. |
| interaction | Interaction with the visual. Includes event details. |
| actionList:open | Action list opened. |
| actionList:close | Action list closed. |
| tooltip:show | Display tooltip. |
| tooltip:update | Updating tooltip. |
| tooltip:move | Moving tooltip. |
| tooltip:hide | Hide tooltip. |
| filters:add | Add a filter. |
| filters:remove | Remove a filter. |
| showWarning | Show a warning. |
| releaseInteractiveElement | Released an interactive element you no longer want to be interactive. |
| registerInteractiveElement | Registered a new interactive element. |
| requestData | Requesting data. |
| axisLabels:create | Create axis labels for your visual. |
| axisLabel:create | Create an axis label for your visual. |
| axisLabels:remove | Remove all axis labels from visual. |
| stop | Visual is stopping. |
| request:pickAttribute | Visual has requested attribute picker. |
| request:pickMetric | Visual has requested metric picker. |
| request:registered | Visual queries whether some element is interactive. |
| request:getTicksStep | Visual is requesting the tick step. |
