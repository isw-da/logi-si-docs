---
title: "What Should I Check for if Live Mode Is Configured But My Dashboard Data Isn't Updating?"
id: 34933208947853
section: "Composer 25 Troubleshooting"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933208947853-What-Should-I-Check-for-if-Live-Mode-Is-Configured-But-My-Dashboard-Data-Isn-t-Updating
updated_at: 2026-05-26T22:08:24Z
---

# What Should I Check for if Live Mode Is Configured But My Dashboard Data Isn't Updating?

# What Should I Check for if Live Mode Is Configured But My Dashboard Data Isn't Updating?

Before opening a support ticket with Composer [Technical Support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932980712461-Contact-Technical-Support), please check the following first:

* Data might be added in real time but not for "now" depending on the time field that Composer is using to play on. Since live mode only queries for any new data that comes in since the query was last executed, any "new but historical" data will not be captured until the dashboard is refreshed and the full query is executed.
* Verify that the time is in sync between the database server and Composer server.
* Verify that the database server and Composer server is using the same time zone.
* Try enabling Delay Mode
  *(with a significant delay)*
  to see if that makes any difference.
