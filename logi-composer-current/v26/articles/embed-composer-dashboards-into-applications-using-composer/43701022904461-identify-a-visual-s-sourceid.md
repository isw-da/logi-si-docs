---
title: "Identify a Visual's sourceID"
id: 43701022904461
section: "Embed Composer Dashboards Into Applications Using Composer"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701022904461-Identify-a-Visual-s-sourceID
updated_at: 2026-05-29T14:11:39Z
---

# Identify a Visual's sourceID

# Identify a Visual's `sourceID`

You can identify a Composer visual's `sourceID` while working with it. For example, to programmatically identify a visual's default settings using a REST API call, it is easiest to use the `sourceID` in the call to look at its source configuration.

**To identify the `sourceID` of a visual's source:**

1. Open the visual in its dashboard.
2. Find the number at the end of the URL in the address bar of your browser. The `sourceID` is the section of the number before the plus sign (+).

   ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242759704461)

After you have identified the `sourceID` of a visual, you can use it in other steps such as calling REST API methods.
