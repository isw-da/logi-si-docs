---
title: "Share a  Dashboard with Users"
id: 34932824740749
section: "Use Dashboards and Visuals in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932824740749-Share-a-Dashboard-with-Users
updated_at: 2026-05-26T22:09:55Z
---

# Share a  Dashboard with Users

# Share a Dashboard with Users

Your users can share dashboards easily amongst themselves in a user-friendly manner. Allow them to grant and [revoke](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932831844109-Revoke-or-Change-Shared-Dashboard-Access) `VIEWER`, `COMMENTER`, or `EDITOR` access level to a dashboard for sharing. When a user shares a dashboard, the users who receive it can access the underlying visuals and sources used in the dashboard. See [Shared Access - Viewers](#SharedAcess).

Control the visibility of this feature in embedded mode by enabling or disabling **Share Dashboard** in the [dashboard interactivity settings](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932814650893-Control-How-Users-Interact-With-a-Dashboard).

Share dashboards with:

* Existing users in a non-tenant environment.
* Existing users and groups within a tenant, and optionally with everyone in a tenant using the **Share with everyone** tab. You must [enable dashboard sharing](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932636844045-Server-Level-Variables#share-dash-tnt) in your tenant environment. See [Server-Level Variables](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932636844045-Server-Level-Variables).
* As an administrator, you can filter users who can receive a dashboard using the recipient rules API. See [Configure Recipient Rules](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932843478029-Configure-Recipient-Rules).

## Share a Dashboard

1. Log into Composer in as a user who can share dashboards ([**Manage Dashboard Permissions** privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference)). Your user account must meet one of the following conditions:

   * Access as the `OWNER` of a dashboard - the user who created it and has `READ`, `WRITE`, and `DELETE` permissions for it.
   * Access as the `EDITOR` of a dashboard - the user who can edit and has `READ` and `WRITE` permissions for it.
   * In a group with the [**Administer Dashboards** privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference).
2. Open the dashboard you wish to share from the [list of available](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932842461581-Use-the-Library-for-Dashboards) dashboards.
3. Select Share Dashboard icon. The **Share [Dashboard Name]** work area opens with a **Select Users** work area visible. In a multi-tenant environment, several tabbed work areas are shown: **Select Users**, **Select Groups**, and **Share with everyone**.

   ![Share Dashboards work area](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167331255437 "Share Dashboards work area")
4. Select and add users using the work area.
5. Enter a full or partial user or group name in the search field to find and select existing users and groups.

   **Note:** If you use the **Share with everyone** work area, you can skip this step.
6. Select an access level for the selected users, groups, or everyone in your tenant: **Viewer**, **Commenter**, or **Editor**.

   **Note:** 
   All users can see comments associated with widgets in your dashboard when comments are enabled. See [Manage Widget Comments](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933318308877-Manage-Widget-Comments) for more information on working with comments.
7. Select **Add** to grant selected users and groups access to this dashboard.

   Dashboard owners and users with **Viewer**, **Commenter**, or **Editor** access to the dashboard are listed in the **Existing Access** list.

   **Note:** If you use the **Share with everyone** work area, all users are given the access level you selected.
8. Select **Save** to save your changes. Any user or group on the Existing Access list retain their access until you [revoke their access](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932831844109-Revoke-or-Change-Shared-Dashboard-Access).

**Note:** [Local visuals](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933273131405-Add-Local-Visuals-to-a-Dashboard) inherit a dashboard's access level. To share visuals from the Visual Gallery included in your dashboard, you need appropriate permissions or privileges, and `DATA ACCESS` permission for the sources of those visuals. See [Shared Access - Viewers](#SharedAcess), [Shared Access - Commenters](#SharedAcess3),and [Shared Access - Editors](#SharedAcess2).

## Shared Access - Viewers

| Sharing User or Group Access - Dashboards | Sharing User or Group Access - Visuals | Sharing User or Group Access - Sources | Recipient Access |
| --- | --- | --- | --- |
| Sharing user has dashboard access:   * `OWNER` or `EDITOR` of the dashboard * Has [**Administer Dashboards** privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference) | No visuals access | No source access | Recipients are given access to:   * `VIEWER` access level to the dashboard * No visual access * No source access |
| Sharing user has dashboard access:   * `OWNER` or `EDITOR` of the dashboard * Has [**Administer Dashboards** privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference) | Sharing user has visual access:   * Owner of the visual * Has [**Manage Visuals** privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference), and `READ` permission for the visuals * Has [**Administer Visuals** privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference) | No source access | Recipients are given access to:   * `VIEWER` access level to the dashboard * `VIEWER` access level to the visuals * No source access |
| Sharing user has dashboard access:   * `OWNER` or `EDITOR` of the dashboard * Has [**Administer Dashboards** privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference) | Sharing user has visual access:   * Owner of the visual * Has [**Manage Visuals** privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference), and `READ` permission for the visuals * Has [**Administer Visuals** privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference) | Sharing user has source access:   * Owner of the source * Has [**Manage Sources** privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference), and `DATA ACCESS` permission for the source * Has [**Administer Sources** privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference) | Recipients are given access to:   * `VIEWER` access level to the dashboard * `VIEWER` access level to the visuals * `DATA ACCESS` permission to the source |

## Shared Access - Commenters

| Sharing User or Group Access - Dashboards | Sharing User or Group Access - Visuals | Sharing User or Group Access - Sources | Recipient Access |
| --- | --- | --- | --- |
| Sharing user has dashboard access:   * `OWNER` or `EDITOR` of the dashboard * Has [**Administer Dashboards** privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference) | No visuals access | No source access | Recipients are given access to:   * `COMMENTER` access level to the dashboard * No visual access * No source access |
| Sharing user has dashboard access:   * `OWNER` or `EDITOR` of the dashboard * Has [**Administer Dashboards** privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference) | Sharing user has visual access:   * Owner of the visual * Has [**Manage Visuals** privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference), and `READ` permission for the visuals * Has [**Administer Visuals** privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference) | No source access | Recipients are given access to:   * `COMMENTER` access level to the dashboard * `COMMENTER` access level to the visuals * No source access |
| Sharing user has dashboard access:   * `OWNER` or `EDITOR` of the dashboard * Has [**Administer Dashboards** privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference) | Sharing user has visual access:   * Owner of the visual * Has [**Manage Visuals** privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference), and `READ` permission for the visuals * Has [**Administer Visuals** privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference) | Sharing user has source access:   * Owner of the source * Has [**Manage Sources** privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference), and `DATA ACCESS` permission for the source * Has [**Administer Sources** privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference) | Recipients are given access to:   * `COMMENTER` access level to the dashboard * `COMMENTER` access level to the visuals * `DATA ACCESS` permission to the source |

## Shared Access - Editors

| Sharing User or Group Access - Dashboards | Sharing User or Group Access - Visuals | Sharing User or Group Access - Sources | Recipient Access |
| --- | --- | --- | --- |
| Sharing user has dashboard access:   * `OWNER`or `EDITOR` of the dashboard * Has [**Administer Dashboards** privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference) | No visuals access | No source access | Recipients are given access to:   * `EDITOR` access level to the dashboard * No visual access * No source access |
| Sharing user has dashboard access:   * `OWNER`or `EDITOR` of the dashboard * Has [**Administer Dashboards** privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference) | Sharing user has visual access:   * `OWNER` or `EDITOR` of the visuals * Has [**Administer Visuals** privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference) | No source access | Recipients are given access to:   * `EDITOR` access level to the dashboard * `EDITOR` access level to the visuals * No source access |
| Sharing user has dashboard access:   * `OWNER` or `EDITOR` of the dashboard * Has [**Administer Dashboards** privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference) | Sharing user has visual access:   * `OWNER` or `EDITOR` of the visuals * Has [**Administer Visuals** privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference) | Sharing user has source access:   * `OWNER` or `EDITOR` of the sources * Has [**Manage Sources** privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference), and `DATA ACCESS` permission for the source * Has [**Administer Sources** privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference) | Recipients are given access to:   * `EDITOR` access level to the dashboard * `EDITOR` access level to the visuals * `DATA ACCESS` permission to the sources |
