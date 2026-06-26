---
title: "Use Compare Filters, Not Condition Filters"
id: 4406817168151
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817168151-Use-Compare-Filters-Not-Condition-Filters
updated_at: 2023-03-30T19:59:04Z
---

# Use Compare Filters, Not Condition Filters

# Use Compare Filters, Not Condition Filters

If you have to filter the data after it's been retrieved, use
**Compare Filter** elements, *not***Condition Filter** elements. Compare filters are implemented as a
native part of the Logi Engine whereas Condition Filters execute script
and that takes a lot longer to run. It's not unusual to see performance
improvements of 25-50% when Condition Filter elements are replaced with
Compare Filter elements.

##
