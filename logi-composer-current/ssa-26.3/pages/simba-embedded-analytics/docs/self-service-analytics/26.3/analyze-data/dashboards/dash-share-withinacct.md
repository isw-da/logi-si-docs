> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Share a Dashboard or Self Service Report with Users

Your users can share dashboards easily amongst themselves in a user-friendly manner. Allow them to grant and [revoke](#revoke-or-change-shared-dashboard-access) `VIEWER`, `COMMENTER`, or `EDITOR` access level to a dashboard for sharing. When a user shares a dashboard, the users who receive it can access the underlying visuals and sources used in the dashboard. See [Shared Access - Viewers](#shared-access-viewers).

Control the visibility of this feature in embedded mode by enabling or disabling **Share Dashboard** in the [dashboard interactivity settings](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-interactivity).

Share dashboards with:

* Existing users in a non-tenant environment.
* Existing users and groups within a tenant, and optionally with everyone in a tenant using the **Share with everyone** tab. You must [enable dashboard sharing](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#server-level-variables) in your tenant environment. See [Server-Level Variables](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#server-level-variables).
* As an administrator, you can filter users who can receive a dashboard using the recipient rules API. See [Configure Recipient Rules](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-schedule#configure-recipient-rules).

## Share a Dashboard or Self Service Report

1. Log in as a user who can share dashboards ([**Manage Dashboard Permissions** privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference)). Your user account must meet one of the following conditions:

   * Access as the `OWNER` of a dashboard or self service report - the user who created it and has `READ`, `WRITE`, and `DELETE` permissions for it.
   * Access as the `EDITOR` of a dashboard or self service report - the user who can edit and has `READ` and `WRITE` permissions for it.
   * In a group with the [**Administer Dashboards** privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference).

2. Open the dashboard or report you wish to share from the [list of available](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-manage#use-the-library-for-dashboards) dashboards or [reports](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/ssr-manage#use-the-self-service-reports-library).

3. Select Share Dashboard or Share Report icon. The **Share \[Name]** work area opens with a **Select Users** work area visible. In a multi-tenant environment, several tabbed work areas are shown: **Select Users**, **Select Groups**, and **Share with everyone**.

   <img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/share-dashboard-24-3.png?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=bd14bf74ebf723eecdca85a9a872b045" alt="Share Dashboards work area" width="752" height="668" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/share-dashboard-24-3.png" />

   Some columns in this work area can be resized or sorted as needed; select the column header break to resize, or select the column name to change the sort.

4. Select and add users using the work area.

5. Enter a full or partial user or group name in the search field to find and select existing users and groups.

   <Note>
     If you use the **Share with everyone** work area, you can skip this step.
   </Note>

6. Select an access level for the selected users, groups, or everyone in your tenant: **Viewer**, **Commenter**, or **Editor**.

   <Note>
     All users can see comments associated with widgets in your dashboard when comments are enabled. See [Widget Comments](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/widgets/widget-cmts-ov) for more information on working with comments.
   </Note>

7. Select **Add** to grant selected users and groups access to this dashboard or report.

   Dashboard and report owners and users with **Viewer**, **Commenter**, or **Editor** access to the dashboard or report are listed in the **Existing Access** list.

   <Note>
     If you use the **Share with everyone** work area, all users are given the access level you selected.
   </Note>

8. Select **Save** to save your changes. Any user or group on the Existing Access list retain their access until you [revoke their access](#revoke-or-change-shared-dashboard-access).

<Note>
  [Local visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-add-dash#add-local-visuals-to-a-dashboard) inherit a dashboard's access level. To share visuals from the Visual Gallery included in your dashboard, you need appropriate permissions or privileges, and `DATA ACCESS` permission for the sources of those visuals. See [Shared Access - Viewers](#shared-access-viewers), [Shared Access - Commenters](#shared-access-commenters),and [Shared Access - Editors](#shared-access-editors).
</Note>

<h2 id="shared-access-viewers">
  Shared Access - Viewers
</h2>

<table>
  <thead>
    <tr>
      <th>Sharing User or Group Access - Dashboards</th>
      <th>Sharing User or Group Access - Visuals</th>
      <th>Sharing User or Group Access - Sources</th>
      <th>Recipient Access</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Sharing user has dashboard access:

        <br />

        * `OWNER` or `EDITOR` of the dashboard
        * Has [**Administer Dashboards** privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference)
      </td>

      <td>No visuals access</td>
      <td>No source access</td>

      <td>
        Recipients are given access to:

        <br />

        * `VIEWER` access level to the dashboard
        * No visual access
        * No source access
      </td>
    </tr>

    <tr>
      <td>
        Sharing user has dashboard access:

        <br />

        * `OWNER` or `EDITOR` of the dashboard
        * Has [**Administer Dashboards** privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference)
      </td>

      <td>
        Sharing user has visual access:

        <br />

        * Owner of the visual
        * Has [**Manage Visuals** privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference), and `READ` permission for the visuals
        * Has [**Administer Visuals** privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference)
      </td>

      <td>No source access</td>

      <td>
        Recipients are given access to:

        <br />

        * `VIEWER` access level to the dashboard
        * `VIEWER` access level to the visuals
        * No source access
      </td>
    </tr>

    <tr>
      <td>
        Sharing user has dashboard access:

        <br />

        * `OWNER` or `EDITOR` of the dashboard
        * Has [**Administer Dashboards** privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference)
      </td>

      <td>
        Sharing user has visual access:

        <br />

        * Owner of the visual
        * Has [**Manage Visuals** privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference), and `READ` permission for the visuals
        * Has [**Administer Visuals** privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference)
      </td>

      <td>
        Sharing user has source access:

        <br />

        * Owner of the source
        * Has [**Manage Sources** privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference), and `DATA ACCESS` permission for the source
        * Has [**Administer Sources** privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference)
      </td>

      <td>
        Recipients are given access to:

        <br />

        * `VIEWER` access level to the dashboard
        * `VIEWER` access level to the visuals
        * `DATA ACCESS` permission to the source
      </td>
    </tr>
  </tbody>
</table>

<h2 id="shared-access-commenters">
  Shared Access - Commenters
</h2>

<table>
  <thead>
    <tr>
      <th>Sharing User or Group Access - Dashboards</th>
      <th>Sharing User or Group Access - Visuals</th>
      <th>Sharing User or Group Access - Sources</th>
      <th>Recipient Access</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Sharing user has dashboard access:

        <br />

        * `OWNER` or `EDITOR` of the dashboard
        * Has [**Administer Dashboards** privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference)
      </td>

      <td>No visuals access</td>
      <td>No source access</td>

      <td>
        Recipients are given access to:

        <br />

        * `COMMENTER` access level to the dashboard
        * No visual access
        * No source access
      </td>
    </tr>

    <tr>
      <td>
        Sharing user has dashboard access:

        <br />

        * `OWNER` or `EDITOR` of the dashboard
        * Has [**Administer Dashboards** privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference)
      </td>

      <td>
        Sharing user has visual access:

        <br />

        * Owner of the visual
        * Has [**Manage Visuals** privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference), and `READ` permission for the visuals
        * Has [**Administer Visuals** privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference)
      </td>

      <td>No source access</td>

      <td>
        Recipients are given access to:

        <br />

        * `COMMENTER` access level to the dashboard
        * `COMMENTER` access level to the visuals
        * No source access
      </td>
    </tr>

    <tr>
      <td>
        Sharing user has dashboard access:

        <br />

        * `OWNER` or `EDITOR` of the dashboard
        * Has [**Administer Dashboards** privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference)
      </td>

      <td>
        Sharing user has visual access:

        <br />

        * Owner of the visual
        * Has [**Manage Visuals** privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference), and `READ` permission for the visuals
        * Has [**Administer Visuals** privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference)
      </td>

      <td>
        Sharing user has source access:

        <br />

        * Owner of the source
        * Has [**Manage Sources** privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference), and `DATA ACCESS` permission for the source
        * Has [**Administer Sources** privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference)
      </td>

      <td>
        Recipients are given access to:

        <br />

        * `COMMENTER` access level to the dashboard
        * `COMMENTER` access level to the visuals
        * `DATA ACCESS` permission to the source
      </td>
    </tr>
  </tbody>
</table>

<h2 id="shared-access-editors">
  Shared Access - Editors
</h2>

<table>
  <thead>
    <tr>
      <th>Sharing User or Group Access - Dashboards</th>
      <th>Sharing User or Group Access - Visuals</th>
      <th>Sharing User or Group Access - Sources</th>
      <th>Recipient Access</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Sharing user has dashboard access:

        <br />

        * `OWNER`or `EDITOR` of the dashboard
        * Has [**Administer Dashboards** privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference)
      </td>

      <td>No visuals access</td>
      <td>No source access</td>

      <td>
        Recipients are given access to:

        <br />

        * `EDITOR` access level to the dashboard
        * No visual access
        * No source access
      </td>
    </tr>

    <tr>
      <td>
        Sharing user has dashboard access:

        <br />

        * `OWNER`or `EDITOR` of the dashboard
        * Has [**Administer Dashboards** privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference)
      </td>

      <td>
        Sharing user has visual access:

        <br />

        * `OWNER` or `EDITOR` of the visuals
        * Has [**Administer Visuals** privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference)
      </td>

      <td>No source access</td>

      <td>
        Recipients are given access to:

        <br />

        * `EDITOR` access level to the dashboard
        * `EDITOR` access level to the visuals
        * No source access
      </td>
    </tr>

    <tr>
      <td>
        Sharing user has dashboard access:

        <br />

        * `OWNER` or `EDITOR` of the dashboard
        * Has [**Administer Dashboards** privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference)
      </td>

      <td>
        Sharing user has visual access:

        <br />

        * `OWNER` or `EDITOR` of the visuals
        * Has [**Administer Visuals** privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference)
      </td>

      <td>
        Sharing user has source access:

        <br />

        * `OWNER` or `EDITOR` of the sources
        * Has [**Manage Sources** privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference), and `DATA ACCESS` permission for the source
        * Has [**Administer Sources** privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference)
      </td>

      <td>
        Recipients are given access to:

        <br />

        * `EDITOR` access level to the dashboard
        * `EDITOR` access level to the visuals
        * `DATA ACCESS` permission to the sources
      </td>
    </tr>
  </tbody>
</table>

<h2 id="revoke-or-change-shared-dashboard-access">
  Revoke or Change Shared Dashboard Access
</h2>

Users with appropriate access can revoke Viewer, Commenter, and Editor access from shared dashboards if needed.

If you or your users revoke a recipient's access to a dashboard, the recipient still has `READ` access to the visuals and `DATA ACCESS` to the source. See [Shared Access - Viewers](#shared-access-viewers).

**Revoke dashboard viewer, commenter, or editor access**

1. Log in as a user who can share dashboards. Your user account must meet one of the following conditions:

   To revoke an access level:

   * Access as the `OWNER` of a dashboard - the user who created it and has `READ`, `WRITE`, and `DELETE` permissions for it.
   * Access as the `EDITOR` of a dashboard - the user who can edit and has `READ` and `WRITE` permissions for it.
   * In a group with the [**Administer Dashboards** privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference).

2. Open the dashboard you need from the [list of available](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-manage#use-the-library-for-dashboards) dashboards.

3. Select Share Dashboard <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/share-dash-22-4.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=2845181af743f45892dc64f7fe42f0eb" alt="select to share a visual, dashboard, or report" width="25" height="25" noZoom data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/share-dash-22-4.png" />. The **Share \[Dashboard Name]** work area opens with several tabbed work areas: **Select Users**, **Select Groups**, and **Share with everyone** for tenants in your environment.

4. Use the **Search** box to find one or more users or groups in the **Existing Access** list in the **Select Users** work area, **Select Groups** work area, or **Share with everyone** work area (when you are working within a tenant).

5. Select the remove icon (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/delete-open.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=02c9cbe530b9f34bd9a73851fdf499e2" alt="" width="16" height="18" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '16px', height: '18px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/delete-open.png" />) next to the user name or group name to remove their access to the dashboard. Select the remove icon as appropriate in the **Share with everyone work** area.

6. Select **Save** to save your changes.

**Change dashboard access**

1. Log in as a user who can share dashboards. Your user account must meet one of the following conditions:

   To change a user's access level:

   * Access as the `OWNER` of a dashboard - the user who created it and has `READ`, `WRITE`, and `DELETE` permissions for it.
   * Access as the `EDITOR` of a dashboard - the user who can edit and has `READ` and `WRITE` permissions for it.
   * In a group with the [**Administer Dashboards** privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference).

2. Open the dashboard you need from the [list of available](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-manage#use-the-library-for-dashboards) dashboards.

3. Select Share Dashboard <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/share-dash-22-4.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=2845181af743f45892dc64f7fe42f0eb" alt="select to share a visual, dashboard, or report" width="25" height="25" noZoom data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/share-dash-22-4.png" />. The **Share \[Dashboard Name]** work area opens with several tabbed work areas: **Select Users**, **Select Groups**, and **Share with everyone** for tenants in your environment.

4. Use the **Search** box to find one or more users or groups in the **Existing Access** list in the **Select Users** work area, **Select Groups** work area, or **Share with everyone** work area (when you are working within a tenant).

   <Note>
     All users can see comments associated with widgets in your dashboard when comments are enabled. See [Widget Comments](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/widgets/widget-cmts-ov) for more information on working with comments.
   </Note>

5. Select **Save** to save your changes.

<Note>
  When you revoke access to a dashboard, they can no longer access the dashboard, but may still have access to shared visuals and sources.
</Note>
