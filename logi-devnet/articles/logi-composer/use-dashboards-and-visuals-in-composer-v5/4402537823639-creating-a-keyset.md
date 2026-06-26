---
title: "Creating a Keyset"
id: 4402537823639
section: "Use Dashboards and Visuals in Composer v5"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402537823639-Creating-a-Keyset
updated_at: 2021-09-15T02:22:00Z
---

# Creating a Keyset

# Creating a Keyset

You can create a keyset from the result set of a visual or from a data point in a visual using the radial menu. Keysets are shared by all users of the Composer instance. The instructions in the following sections create the same keyset, using the two different methods.

* [*Creating a Keyset from the Visual Result Set*](#Creating)
* [*Creating a Keyset from a Data Point*](#Creating2)

![](https://devnet.logianalytics.com/hc/article_attachments/4406753437463/noteicon.jpg) If you change the field type from Number or Integer to Attribute for a field that is used in a keyset, errors will result when the keyset is applied as a filter. To resolve this problem, create an Attribute derived field from the original field (for example, using the `num_to_text` function) and use it when you create the keyset, instead of the original field.

To control whether keysets can be created or managed from a visual, use the interactivity sidebar. See [*Controlling How Users Interact With a Visual*](https://devnet.logianalytics.com/hc/en-us/articles/4402537944215-Controlling-How-Users-Interact-With-a-Visual).

## Creating a Keyset from the Visual Result Set

You can create a keyset from the result set of a visual. Filtering the visual data before creating the keyset will limit the unique data values included in the keyset.

To create a keyset from a visual result set:

1. Create a visual and filter it as desired.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406753464215/va-airports_362x147.png)
2. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406763902743/three-dots-menu_19x11.png) and then **Create Keyset** from the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537941655-Using-the-Visual-Menu). The Save Keyset dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406763957015/save-keyset2_192x190.png)
3. Enter a name for the keyset in the **Name** box. Because the keyset will be shared by all users of the Composer instance, be sure to enter a unique name.
4. Optionally, enter a description for the keyset in the **Description** box.
5. In the **Select a Field as Key** box, enter the field that should be used as the key for the keyset. A list of keyset values for the field you selected appears on the Save Keyset dialog. These values can include an empty value.
6. Select **Save** to save the keyset.

## Creating a Keyset from a Data Point

You can create a keyset from a data point in a visual using the radial menu. In this case, the result set used for the keyset is automatically filtered by the data point you select.

To create a keyset from a data point:

1. Create a visual.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406763957527/airports-by-state_576x253.png)
2. Select a data point in the visual. For example, you might select the bar representing Virginia. The radial menu appears:

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406763958039/airports-by-state-radial_576x254.png)
3. Select **Keyset** on the radial menu. The Save Keyset dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406763957015/save-keyset2_192x190.png)
4. Enter a name for the keyset in the **Name** box. Because the keyset will be shared by all users of the Composer instance, be sure to enter a unique name.
5. Optionally, enter a description for the keyset in the **Description** box.
6. In the **Select a Field as Key** box, enter the field that should be used as the key for the keyset. This should be the field by which the original visual was grouped. A list of keyset values for the field you selected appears on the Save Keyset dialog. These values can include an empty value.
7. Select **Save** to save the keyset.
