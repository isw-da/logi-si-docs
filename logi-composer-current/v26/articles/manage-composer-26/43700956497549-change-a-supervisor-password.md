---
title: "Change a Supervisor Password"
id: 43700956497549
section: "Manage Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700956497549-Change-a-Supervisor-Password
updated_at: 2026-05-29T14:07:05Z
---

# Change a Supervisor Password

# Change a Supervisor Password

**Note:** 
The default **supervisor** user is no longer installed with Logi Composer v23.4 and later: add users to the **Supervisors** group instead. If you upgrade to Logi Composer from an earlier version, the Supervisor user becomes a member of the Supervisors group in the *Visual Data Discovery* (formerly *superaccount*) tenant.

After upgrading to Logi Composer v23.4 and later, members of the Supervisors group can change their own passwords, or force a password change at next log in. See [Change Passwords](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005569933-Change-Passwords). A system administrator or users who are members of a group with [user management privileges](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference) can change a password or force a password change for a member of the Supervisors group.

## Change a Password for Supervisor Group Members

**Note:** 
Only a system administrator or users who are members of a group with [user management privileges](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference) can change a password or force a password change for a member of the Supervisors group.

**Change or reset password for Supervisors group members**

1. Log in as user who has been assigned to a group with [user management privileges](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference).
2. Select **Users and Groups** from the [UI menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701160499853-The-Composer-UI-Menu). A work area opens you can use to add and manage users. Select the **Users** tab if both the **Users** and **Groups** tabs are visible.
3. Select the user from the list of users whose password you want to reset. The account details for that user appear on the right side of the page.
4. On the **Info** tab, select **Change Password**.
5. Type the new password in the **Password** and **Confirm Password** boxes.

   **Note:** 
   Optionally, change the **Require password change** switch from the default **No** to **Yes**. If you change this to **Yes**, the user is prompted (and forced) to change their password when they next attempt to log in.
6. Select **Save** to save your changes.
7. The next time the user logs in, they can use the new password you set. They are prompted to change this password if **Require password change** was set to **Yes**.

## Change a Supervisor Password in Earlier Versions of Logi Composer

**Note:** 
Only a Composer supervisor user can change or reset their own supervisor password. They cannot change the passwords for other supervisors.

**To** **change or reset the supervisor password:**

1. Log in as the supervisor user. Supervisor users are users assigned to the *superaccount*. The Manage Users page appears.
2. In the list on the left of the page, select the supervisor user name. The account details for the supervisor user appear on the right side of the page.
3. On the **Info** tab, select **Change Password**. The Info tab expands to show boxes that allow you to change the password.
4. Type the new password in the **Password** and **Confirm Password** boxes.
5. Optionally, change the **Require password change** switch. When this switch is set to **Yes**, the supervisor is prompted (and forced) to change their password on the next log in. When this switch is set to **No**, the supervisor is not prompted to change their password. The default setting for this switch is **No**.
6. Select **Save** to save the new password. As soon as you do this, the supervisor user can log into Composer using the new password.
