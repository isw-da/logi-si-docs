---
title: "Identify a Visual's sourceID"
id: 4405850878231
section: "Embed Composer Dashboards Into Applications using Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850878231-Identify-a-Visual-s-sourceID
updated_at: 2021-09-21T01:26:42Z
---

# Identify a Visual's sourceID

# Identify a Visual's `sourceID`

You can identify a Composer visual's `sourceID` while working with it. For example, to programmatically identify a visual's default settings using a REST API call, it is easiest to use the `sourceID` in the call to look at its source configuration.

**To identify the `sourceID` of a visual's source:**

1. Open the visual in its dashboard.
2. Find the number at the end of the URL in the address bar of your browser. The `sourceID` is the section of the number before the plus sign (+).

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743932823/source-id_576x334.png)

After you have identified the `sourceID` of a visual, you can use it in other steps such as calling REST API methods.
