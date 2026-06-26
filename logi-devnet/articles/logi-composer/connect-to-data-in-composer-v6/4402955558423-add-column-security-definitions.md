---
title: "Add Column Security Definitions"
id: 4402955558423
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402955558423-Add-Column-Security-Definitions
updated_at: 2021-08-07T17:30:52Z
---

# Add Column Security Definitions

# Add Column Security Definitions

To add column security to restrict the data source fields that can be viewed or used by the group:

1. Log into Composer as a Composer administrator, a user in a group that has been granted the **Can Administer Sources**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4402955416087-Group-Privilege-Reference), or a user in a group that has been granted the **Can Manage Source Permissions**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4402955416087-Group-Privilege-Reference)*and* who also has **read**[permission](https://devnet.logianalytics.com/hc/en-us/articles/4402955557783-About-Data-Source-Permissions) for the data source.

   If the user name you log in with is also associated with other Composer accounts, verify that the correct account is selected. See [*Switch Accounts*](https://devnet.logianalytics.com/hc/en-us/articles/4402955425175-Switch-Accounts).
2. Select **Sources** on the [top-level navigation banner](https://devnet.logianalytics.com/hc/en-us/articles/4402963039639-The-Top-Level-Navigation-Banner) or in the [UI menu](https://devnet.logianalytics.com/hc/en-us/articles/4402963040407-The-Composer-UI-Menu) (![](https://devnet.logianalytics.com/hc/article_attachments/4404952783767/hamburger.png)). The Sources page appears.
3. Locate the data source for which you want to restrict field access and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404952869271/security-col.png) in the **Column** column for the data source. The Column Security dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404952869783/col-security-empty_384x258.png)
4. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404952870039/add-filter-white_92x22.png). The Column Security dialog fills with information about the data source you selected.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404959543831/col-security-start_384x279.png)
5. Specify a name for the column security definition in the **Name** field. This name will be used to distinguish one column security definition from another in the Column Security dialog.
6. Optionally, use the **Description** field to supply a description for the column security definition.
7. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404959544087/add-groups_80x23.png) to select one or more groups to which the column security definition applies. The Add Groups dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404952870295/col-security-add-groups_384x280.png)
8. Select one or more groups for the column security filter. You can search for group names using the search box at the top of the dialog. When you have finished selecting groups, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404952794519/apply-btn.png).

   The groups appear under **Assignees** on the Column Security dialog. If you want to remove a group from the filter, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404959489559/delete-open.png) next to the group name in the **Assignees** section.
9. Select fields in the **Fields** list to be visible to the members of the selected groups. By default **Select All** is selected. To restrict the fields visible to group members, clear (uncheck) **Select All** and manually select fields in the list (**Select ALL** is automatically unselected when you clear (uncheck) a field in the list). Use the Search bar to search for fields in the list.

   To see only the fields you have selected in the list, select **Show selected fields only**. To see all fields in the list (including fields you have not selected), clear (uncheck) **Show selected fields only**.
10. When you are finished selecting data source fields that can be visible to the groups, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404959543447/save-blue-btn_43x23.png) to save the column security definition.
11. Repeat Steps 4-9 to add more column security definitions.
12. When all column security definition modifications have been made, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404959539863/close-btn_92x21.png) to close the Column Security dialog.
