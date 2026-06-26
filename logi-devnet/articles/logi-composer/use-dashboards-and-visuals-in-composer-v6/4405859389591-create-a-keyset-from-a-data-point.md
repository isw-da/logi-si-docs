---
title: "Create a Keyset From a Data Point"
id: 4405859389591
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859389591-Create-a-Keyset-From-a-Data-Point
updated_at: 2021-09-21T01:28:58Z
---

# Create a Keyset From a Data Point

# Create a Keyset From a Data Point

You can create a keyset from a data point in a visual using the radial menu. The result set used for the keyset is automatically filtered by the data point you select.

To create a keyset from a data point:

1. Create a visual.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743784727/airports-by-state_576x253.png)
2. Select a data point in the visual. For example, you might select the bar representing Virginia. The radial menu appears:

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743785111/airports-by-state-radial_576x254.png)
3. Select **Keyset** on the radial menu. The Save Keyset dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743785367/save-keyset2_192x190.png)
4. Enter a name for the keyset in the **Name** box. Because the keyset will be shared by all users of the Composer instance, be sure to enter a unique name.
5. Optionally, enter a description for the keyset in the **Description** box.
6. In the **Select a Field as Key** box, enter the field that should be used as the key for the keyset. This should be the field by which the original visual was grouped. A list of keyset values for the field you selected appears on the Save Keyset dialog. These values can include an empty value.
7. Select **Save** to save the keyset.
