---
title: "Dashboard Smart Loading"
id: 34932824866829
section: "Use Dashboards and Visuals in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932824866829-Dashboard-Smart-Loading
updated_at: 2026-05-26T22:06:55Z
---

# Dashboard Smart Loading

# Dashboard Smart Loading

Composer uses smart loading to load visuals on a dashboard. Smart loading improves the performance for loading visuals on a dashboard, especially for dashboards containing many visuals.

Without smart loading, visuals cannot be used until all the visuals in a dashboard are loaded. With smart loading, an initial maximum number of visuals are loaded simultaneously. The rest of the visuals are put on hold. After one or more initial visuals are loaded, other visuals in the dashboard are taken off hold and loaded, but only up to the set maximum. As visuals are loaded, they can be used immediately, without waiting for all the dashboard visuals to load.

Visuals are loaded from the top down. The immediately viewable visuals (the ones at the top of the dashboard) are loaded first, up to the set maximum. If you scroll down through a dashboard, a visual that is on hold and is placed farther from the top of the dashboard is started at a higher priority than other visuals on the dashboard.

For information on managing smart loading, including changing the maximum number of visuals that are loaded simultaneously (the default is eight visuals), contact insightsoftware [Technical Support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932980712461-Contact-Technical-Support).
