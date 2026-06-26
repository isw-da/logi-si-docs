---
title: "Add Column Security Definitions"
id: 34932911585677
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932911585677-Add-Column-Security-Definitions
updated_at: 2026-05-26T22:09:50Z
---

# Add Column Security Definitions

# Add Column Security Definitions

Add column security to restrict the data source fields that can be viewed or used by the group.

1. Log into Composer as a user in a group that has been granted the **Administer Sources** [privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference), or a user in a group that has been granted the **Manage Source Permissions** [privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference)*and* who also has **read**  [permission](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932915596173-About-Source-Permissions) for the data source.

   If the user name you log in with is also associated with other Composer accounts, verify that the correct account is selected. See [Switch Tenants](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932611967885-Switch-Tenants).
2. Select **Sources** on the [top-level navigation banner](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933120256397-The-Top-Level-Navigation-Banner) or in the [UI menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933143886477-The-Composer-UI-Menu) (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167921323661)). The Sources page appears.
3. Locate the data source for which you want to restrict field access and select the icon in the **Column** column for the data source. The Fields Security dialog appears.
4. Select **Add Filter**. The Fields Security dialog fills with information about the data source you selected.

   ![add a column filter to the fields security work area here](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167291498765 "Fields Security Work Area")
5. Specify a name for the column security definition in the **Name** field. This name will be used to distinguish one column security definition from another here.
6. Optionally, use the **Description** field to supply a description for the column security definition.
7. Select **Add Groups** to select one or more groups to which the column security definition applies. The Add Groups dialog appears.
8. Select one or more groups for the column security filter. You can search for group names using the search box at the top of the dialog. When you have finished selecting groups, select **Apply**.

   The groups appear under **Assignees** on the Column Security dialog. If you want to remove a group from the filter, select ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167893175821) next to the group name in the **Assignees** section.
9. Select fields in the **Fields** list to be visible to the members of the selected groups. By default, all fields are selected, and all values are allowed (the **Allow values** option is selected).

   Check or clear (uncheck) fields, then optionally select **Forbid values** to forbid selected fields, or leave **Allow values** selected to allow your selected fields. Use the Search bar to search for fields in the list.

   To see only the fields you have selected in the list, select **Show selected fields only**. To see all fields in the list (including fields you have not selected), clear (uncheck) **Show selected fields only**.
10. When you are finished selecting data source fields that can be visible to the groups, select **Save** to save the column security definition.
11. Repeat Steps 4-9 to add more column security definitions.
12. When all column security definition modifications have been made, select **Close** to close the Column Security dialog.
