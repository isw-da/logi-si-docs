---
title: "Add and Remove Supervisors"
id: 43700990533901
section: "Manage Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700990533901-Add-and-Remove-Supervisors
updated_at: 2026-05-29T14:11:43Z
---

# Add and Remove Supervisors

# Add and Remove Supervisors

**Note:** 
The default **supervisor** user is no longer installed with Logi Composer v23.4 and later: add users to the **Supervisors** group instead. If you upgrade to Logi Composer from an earlier version, the Supervisor user becomes a member of the Supervisors group in the *Visual Data Discovery* (formerly *superaccount*) tenant.

After upgrading to Logi Composer v23.4 and later, the supplied [admin user](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701036219149-Supplied-Users-and-User-Groups#The2) (System Administrator) or a member of the Administrators group can add or remove users in the Supervisors group.

Add any number of users to this group to allow them to perform specific functions without giving them access to all tasks members of the Administrators group can perform in the *Visual Data Discovery* tenant.

## Add a User to the Supervisors Group

1. Log in as the supplied [admin user](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701036219149-Supplied-Users-and-User-Groups#The2) or a member of the Administrators group in *Visual Data Discovery*.
2. Select **Users and Groups** on the [UI menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701160499853-The-Composer-UI-Menu) (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243384539405)). A work area opens you can use to manage users. Select the **Users** tab.
3. Select the user from the list of users you want to add to the Supervisors group. The account details for that user appear on the right side of the page.
4. On the **Info** tab, select **Add Group(s)**. The Select Account(s) dialog appears.

   **Note:** 
   If the user is already a member of the Supervisors group, this option is not shown.
5. Select (check) the group or groups you want to add this user to. When you add a user to the Supervisors group, they have full access to the Composer supervisor UI and its supervisory functions. See [About the Supplied Composer Tenant](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701021083277-About-the-Supplied-Composer-Tenant).
6. Select **Apply** when finished.
7. Select **Save** to save the user.

The user is now a member of the Supervisors group.

## Remove a User from the Supervisors Group

You can remove a user from the Supervisors group by removing them from the Supervisors or by simply deleting their user account. See [Delete Users](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701021605645-Delete-Users) .

1. Log in as the supplied [admin user](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701036219149-Supplied-Users-and-User-Groups#The2) or a member of the Administrators group in *Visual Data Discovery*.
2. Select **Users and Groups** on the [UI menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701160499853-The-Composer-UI-Menu) (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243384539405)). A work area opens you can use to manage users. Select the **Groups** tab if both the **Users** and **Groups** tabs are visible.
3. Select the Supervisors group from the list of groups. The details for that group appear on the right side of the page.
4. Select the **Members** tab. This tab lists all members of the Supervisors group.
5. Remove the user from the group by selecting the remove icon (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243353146125)) next to the user's name. Confirm your deletion in the confirmation modal.
6. Select **Save** when finished. The list of users on the **Members** tab adjusts to show your changes.
