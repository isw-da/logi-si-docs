---
title: "Add and Remove Supervisors"
id: 4405859123479
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859123479-Add-and-Remove-Supervisors
updated_at: 2021-09-21T01:26:34Z
---

# Add and Remove Supervisors

# Add and Remove Supervisors

More than one Composer supervisor user can be defined for your Composer instance.

## Add a Supervisor

To add a supervisor:

1. Log into Composer as a supervisor (make sure you have selected the superaccount). The Manage Users page appears, listing all the user definitions in the Composer instance. If you move from this page, you can always access it by selecting **Users** on the [supervisor menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859441687-The-Composer-Supervisor-Menu) (![](https://devnet.logianalytics.com/hc/article_attachments/4406743720343/hamburger.png)).
2. On the left side of the page, select the name of the user definition that you would like to make a supervisor. The user definition appears on the right side of the page.

   Alternatively, define a new user to be a supervisor. See [*Add User Definitions*](https://devnet.logianalytics.com/hc/en-us/articles/4405850861463-Add-User-Definitions).
3. Select the **Account(s)** tab of the user definition. This tab lists all the accounts to which the user is assigned and the number of groups to which the user is assigned in each account.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747457175/accounts-tab_480x313.png)
4. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743937559/add-accts-btn.png). The Select Account(s) dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743937815/acct-select_197x211.png)
5. Select (check) the *superaccount*.

   Users assigned to the *superaccount* have full access to the Composer supervisor UI and its supervisory functions. See [*About the Supplied Composer Accounts*](https://devnet.logianalytics.com/hc/en-us/articles/4405859102999-About-the-Supplied-Composer-Accounts).
6. Select **Apply** when finished. The list of accounts on the **Account(s)** tab adjusts to show your selections.
7. Optionally, in the **Current Account** field, select the account that should be used the next time the user logs in. See [*Set the Current Account for a User*](https://devnet.logianalytics.com/hc/en-us/articles/4405850859927-Set-the-Current-Account-for-a-User).
8. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743938583/save-blue-supervisor-btn_62x21.png) to save the user definition.

The user is now a supervisor.

## Remove a Supervisor

You can remove a supervisor by removing them from the *superaccount* or by simply deleting the user definition of the supervisor. See [*Delete User Definitions*](https://devnet.logianalytics.com/hc/en-us/articles/4405850863255-Delete-User-Definitions) to learn about deleting user definitions.

To remove a supervisor from the *superaccount*:

1. Log into Composer as a supervisor. The Manage Users page appears, listing all the user definitions in the Composer instance. If you move from this page, you can always access it by selecting **Users** on the [supervisor menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859441687-The-Composer-Supervisor-Menu) (![](https://devnet.logianalytics.com/hc/article_attachments/4406743720343/hamburger.png)).
2. On the left side of the page, select the name of the user defined as a supervisor. The user definition appears on the right side of the page.
3. Select the **Account(s)** tab of the user definition. This tab lists all the accounts to which the user is assigned and the number of groups to which the user is assigned in each account.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747457175/accounts-tab_480x313.png)
4. Remove the user from the *superaccount* in one of two ways.

   * In the list of accounts on the Account(s) dialog, select the ![](https://devnet.logianalytics.com/hc/article_attachments/4406743776663/delete-grey.png) icon associated with the *superaccount*. When you do, a small ![](https://devnet.logianalytics.com/hc/article_attachments/4406743778071/delete-btn.png) button appears. Select this button to remove the user from the *superaccount*.
   * Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743937559/add-accts-btn.png) to view the Select Account(s) dialog. Clear (uncheck) the checkbox associated with the *superaccount* and select **Apply**.

   The list of accounts on the Account(s) tab adjusts to show your selections.
5. Select **Apply** when finished. The list of accounts on the **Account(s)** tab adjusts to show your selections.
6. Optionally, in the **Current Account** field, select the account that should be used the next time the user logs in. See [*Set the Current Account for a User*](https://devnet.logianalytics.com/hc/en-us/articles/4405850859927-Set-the-Current-Account-for-a-User).
7. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406747457559/save-blue-supervisor-btn_78x27.png) to save the user definition.
