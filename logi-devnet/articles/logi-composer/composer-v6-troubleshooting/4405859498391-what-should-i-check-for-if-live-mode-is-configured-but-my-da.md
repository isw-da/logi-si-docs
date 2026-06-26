---
title: "What Should I Check for if Live Mode Is Configured But My Dashboard Data Isn't Updating?"
id: 4405859498391
section: "Composer v6 Troubleshooting"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859498391-What-Should-I-Check-for-if-Live-Mode-Is-Configured-But-My-Dashboard-Data-Isn-t-Updating
updated_at: 2021-09-21T01:29:52Z
---

# What Should I Check for if Live Mode Is Configured But My Dashboard Data Isn't Updating?

# What Should I Check for if Live Mode Is Configured But My Dashboard Data Isn't Updating?

Before opening a support ticket with Composer [Technical Support](https://devnet.logianalytics.com/hc/en-us/articles/4405859363351-Contact-Technical-Support), please check the following first:

* Data might be added in real time but not for "now" depending on the time field that Composer is using to play on. Since live mode only queries for any new data that comes in since the query was last executed, any "new but historical" data will not be captured until the dashboard is refreshed and the full query is executed.
* Verify that the time is in sync between the database server and Composer server.
* Verify that the database server and Composer server is using the same time zone.
* Try enabling Delay Mode
  *(with a significant delay)*
  to see if that makes any difference.
