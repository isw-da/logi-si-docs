---
title: "Display All Unique Elements for a Selected Filter Panel Attribute"
id: 43701167210637
section: "Composer 26 Troubleshooting"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701167210637-Display-All-Unique-Elements-for-a-Selected-Filter-Panel-Attribute
updated_at: 2026-05-29T14:10:23Z
---

# Display All Unique Elements for a Selected Filter Panel Attribute

# Display All Unique Elements for a Selected Filter Panel Attribute

## Resolution

The reason that only some, and not all, of the available attribute elements are showing on the filter panel is due to how Composer samples the data by default during the initial source creation. To have the filter panel populate with all the field elements, please refresh the field from within the data source so all the data is sampled. To do this:

1. Ensure you are logged into Composer as an administrator.
2. Select **Sources** on the UI menu (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243137973261)). The [Sources](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701081381901-Data-Sources-Page) page appears.
3. Scroll down the list of connected data sources, select the target source and navigate to the
   **Fields** page.
4. Scroll to the field on which the filter is being applied.
5. Under the
   **Statistics** column, select the
   **Refresh** button.

   This ensures that all the values for that specific field will appear on the filter panel of the visuals or filter snippet.
