---
title: "Display All Unique Elements for a Selected Filter Panel Attribute"
id: 4402955687447
section: "Composer v6 Troubleshooting"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402955687447-Display-All-Unique-Elements-for-a-Selected-Filter-Panel-Attribute
updated_at: 2021-08-07T17:32:10Z
---

# Display All Unique Elements for a Selected Filter Panel Attribute

# Display All Unique Elements for a Selected Filter Panel Attribute

## Resolution

The reason that only some, and not all, of the available attribute elements are showing on the filter panel is due to how Composer samples the data by default during the initial source creation. To have the filter panel populate with all the field elements, please refresh the field from within the data source so all the data is sampled. To do this:

1. Ensure you are logged into Composer as an administrator.
2. Select **Sources** on the UI menu (![](https://devnet.logianalytics.com/hc/article_attachments/4404952783767/hamburger.png)). The [Data Sources](https://devnet.logianalytics.com/hc/en-us/articles/4402962976663-Sources-Page) page appears.
3. Scroll down the list of connected data sources, select the target source and navigate to the
   **Fields** page.
4. Scroll to the field on which the filter is being applied.
5. Under the
   **Statistics** column, select the
   **Refresh** button.
     
    This ensures that all the values for that specific field will appear on the filter panel of the visuals.
