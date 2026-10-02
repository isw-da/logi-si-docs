> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Simba Self-Service Analytics Release Notes 26.3

This topic describes feature enhancements, resolved issues, and important information for Self-Service Analytics 26.3.

To purchase this product, contact [insightsoftware Sales](mailto:loginewbusinessteam@insightsoftware.com?subject=I%20am%20interested%20in%20purchasing%20this%20product,%20please%20contact%20me.).

* [Product Transitions](#product-transitions)
* [Beta Features in This Release](#beta-features-in-this-release)
* [Feature Enhancements](#feature-enhancements)
* [API Updates](#api-updates)
* [Bug Fixes](#bug-fixes)
* [Breaking Changes](#breaking-changes)
* [Known Issues](#known-issues)
* [Dependency Updates](#dependency-updates)
* [Operating System Platform Support](#operating-system-platform-support)

See also [Important Notices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/upgrading-server#important-notices), Product Transitions, and the Self-Service Analytics 26 Summary of Changes.

Simba Self-Service Analytics is offered on a quarterly release schedule, and our version numbering system reflects this. The current major release is v26.3.

<h2 id="product-transitions">
  Product Transitions
</h2>

Composer has been restructured to be Simba Self-Service Analytics, part of our Embedded Analytics offerings.

* Simba Agentic Intelligence is now fully integrated with Simba Self-Service Analytics.
* Your users can now access the Forgot Password workflow from the Self-Service Analytics Login.
* Licenses support the capabilities your organization needs: License Simba Self-Service Analytics and Simba Agentic Intelligence to work together, or Self-Service Analytics on its own.
* Content previously managed in Composer, Visual Data Discovery, or as embedded Visual Data Discovery content will be supported in Simba Self-Service Analytics 26.3 and later releases.
* Content previously managed in Dundas BI, or Managed Dashboards and Reports will be supported in Simba Custom Analytics 26.3 and later releases.

For more information on how to plan and work through this transition, reach out to [Technical Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support) for assistance.

For a brief overview of all environment and capability changes, see [Transitioning for Symphony and Composer Users](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/transition-sym).

<h2 id="beta-features-in-this-release">
  Beta Features in This Release
</h2>

This release may contain some features and enhancements in a beta test state so you can try them out in a non-production environment. Assess how they work in your environment, and provide feedback to insightsoftware as part of a formal beta testing process.

<Warning>
  Do not use beta features in a production environment or on mission-critical systems.
</Warning>

<h3 id="rn-folders">
  Create Folders
</h3>

**Beta Release: Self-Service Analytics 26.3**

When [enabled](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#server-level-variables), users with appropriate privileges can use the Self-Service Analytics API to create and manage folders and folder structures. Your users can organize their dashboards and reports in the folder structure you define. See [API updates](#api-updates).

<Warning>
  You must have the appropriate licensing from insightsoftware to use these features.
</Warning>

<Warning>
  This feature is considered to be released in beta for your testing purposes. Workflows and features may change before a production-ready version is released.
</Warning>

<h2 id="feature-enhancements">
  Feature Enhancements
</h2>

<h3 id="rn-wkspc">
  Workspaces
</h3>

In environments that are integrated with Simba Agentic Intelligence, you can now create and use workspaces to build and refine data sources in a private workspace before publishing them publicly to other users. Users with appropriate permissions can view your published workspaces. Import an existing source from the your organization's existing public inventory, or create one from scratch with a guided, conversational flow. Describe what you need, pick a connection, and choose the tables to include. This feature is available both in single and multiple tenant environments.

* Iterate freely: nothing in the workspace you create is visible to other users in your environment it until you publish.
* Describe what you need to a chatbot that walks you through creating a data source and keeps a running history of every step.
* Publish your selected data sources to tenant users as public inventory when ready. Publish as little as a subset at a time, and choose whether each subset creates a new source or updates an existing one.

<Note>
  Once you have published a workspace, you cannot make further changes to iterate that workspace. Create a new workspace and publish it with your preferred adjustments.
</Note>

<Warning>
  You must have the appropriate licensing from insightsoftware to see this option.
</Warning>

<h3 id="sai-26.3">
  Simba Agentic Intelligence Integration
</h3>

Manage two key elements of your Simba Agentic Intelligence integration directly in Self-Service Analytics.

* **LLM Configuration** (**Administration > Tools > LLM**): Set up and manage your LLM providers: credentials, parameters, and capabilities.
* **Agentic Rules** (**Profile > Agentic Rules**): Create, edit, and search plain-English rules, and assign them to your data sources.

You'll also find the Q\&A and visual-creation chatbot experience, including question suggestions, directly on the Self-Service Analytics home page.

<Warning>
  Visibility of these settings depends on your license.
</Warning>

Additionally, you can access the help options for the products you are licensed for from the main menu. If your license covers both Self-Service Analytics and Simba Agentic Intelligence, you can reach both help systems from the main menu.

<h3 id="radar-vis">
  Radar Visuals
</h3>

Compare multiple metrics across one or more entities at a glance with the new Radar visual. Each entity is plotted as a colored polygon on a shared radial grid, with one axis per metric — useful for side-by-side comparisons like performance scores, ratings, or benchmark results.

* Select 3 to 12 metrics and a Group By attribute; each group value becomes its own polygon (up to 10 by default).
* Hover a polygon to see the entity's values across every metric, and optionally select to filter or drill down in your data.
* You can apply visual filters and cross-filtering from other visuals on the same dashboard.
* Customize the grid shape, fill, line styling, and axis labels from the visual's settings panel.
* Exports as a PNG or as part of a PDF dashboard export.

<Note>
  Radar charts don't support the TimePlayer control or axis rulers.
</Note>

<h3 id="vis-imp">
  Visuals Improvements
</h3>

* Table visuals display a status bar that includes the total row count and the number of rows currently displayed.
* Pivot table visuals display a status bar that includes the total number of rows.
* View information about the total number of items you have access to and a count of items you have selected when you access your Data Sources, Visual Gallery, Dashboards Library, or Reports Library.

<h3 id="pwd-reset">
  Password Reset
</h3>

Your users can now start a password reset process from the login page. This is also available in multi-tenant environments: the reset applies to all tenants you are a member of.

Select **Forgot Password?**, then enter your username in the provided form. Self-Service Analytics sends a reset link to the email address linked to your username and associated with your user account. This link is valid for 60 minutes. After you reset your password, all of your current sessions are terminated.

<Note>
  This applies only to locally-managed Self-Service Analytics user accounts. Any SSO or other externally managed user account setups must reset their password in that environment.
</Note>

<h3 id="qy-perf">
  Query Performance
</h3>

Upgraded the underlying query engine to improve performance and reliability when running reports and dashboards.

<h2 id="api-updates">
  API Updates
</h2>

API documentation is provided in your environment at this link: `https://<self-service-analytics-URL>/composer/swagger-ui.html`.

**26.3.0**

<h3 id="api-folders">
  /api/folders
</h3>

Use these endpoints to create and manage folders and folder structures for your dashboards and reports. These endpoints are in beta: include the header `X-Enable-Preview: true` in every request. Responses include the header `X-API-Stability: experimental`.

<Note>
  Requires the **Administer Folders** privilege (`ROLE_ADMINISTER_FOLDERS`). To create a folder, you need the **Create Folders** privilege (`ROLE_CREATE_FOLDERS`). See [Group Privilege Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference).
</Note>

<Note>
  Folder requests return only the folders you have permission to see.
</Note>

#### POST

* `POST /api/folders`: Create a folder. Provide:

  * `folder_name`: The name of the folder. This cannot be blank when you create a folder, and is limited to 100 characters.
  * `description`: Optional. A description of the folder.
  * `parent_id`: Optional. The ID of the folder this folder is created in. If you don't provide one, the folder is placed at the root.
  * `inheritance_state`: Optional.
  * `content_type`: `DASHBOARDS` or `REPORTS`.

  The response returns the folder details, including `project_id`, `project_type`, `permissions`, and `visibility`. If you don't provide a parent, the system creates a shared library project for the folder. Otherwise, the folder inherits the project of its parent.

<Warning>
  The default maximum folder depth is six. Administrators can change this by configuring `folder.tree.max-depth`.
</Warning>

#### GET

Use these endpoints to view your existing folder structure: folder trees, children, folder contents, and breadcrumb paths.

* `GET /api/folders/{folderId}`: Get the details of a folder.
* `GET /api/folders/tree`: Returns your root folders for one content type. Provide `content_type` (`DASHBOARDS` or `REPORTS`).
* `GET /api/folders/{id}/children`: Returns a folder's direct subfolders, paginated with `page_size` (default 50, max 200) and `cursor`. The response includes `pageInfo` with `nextPageToken` and `previousPageToken`. If the folder has 100 or more child folders, the response includes the `X-Folder-Fanout-Warning` header.
* `GET /api/folders/{id}/contents`: Returns a paginated list of the dashboards and reports mapped directly into a folder, using `page_size` (default 50, max 200) and `cursor`.
* `GET /api/folders/{id}/path`: Returns the breadcrumb chain from the root to a folder.

<Note>
  Workspaces introduce an optional `X-Workspace-Id` request header (or an equivalent `workspaceId` query parameter; the header takes priority when both are sent). Existing endpoints that don't recognize this header ignore it and behave exactly as before. Currently only the source endpoints honor it, scoping results to a workspace instead of the account.
</Note>

#### PATCH

* `PATCH /api/folders/{folderId}`: Update a folder's metadata. Provide `name`, `description`, or both. A `name` is limited to 100 characters. Omit `name` to leave it unchanged.
* `PATCH /api/folders/dashboards/{id}/folder`: Place a dashboard in a folder. Provide `folder_id`.
* `PATCH /api/folders/reports/{id}/folder`: Place a report in a folder. Provide `folder_id`.

#### PUT

* `PUT /api/folders/tree-state`: Replaces the saved expanded state of your folder tree. Provide `folder_ids`, the folders to show expanded. The response returns the list of expanded folder IDs.

#### DELETE

* `DELETE /api/folders/{folderId}`: Permanently delete an empty folder. If the folder is not empty, the request returns `409 FOLDER_NOT_EMPTY`.

<Warning>
  You must have the appropriate licensing from insightsoftware to use these features.
</Warning>

<Warning>
  This feature is considered to be released in beta for your testing purposes. Workflows and features may change before a production-ready version is released.
</Warning>

<h3 id="api-json-datasets">
  /api/json-datasets
</h3>

Use these endpoints to create and manage JSON datasets that store shape data. Use `GeoJSON` or `TopoJSON` boundary data to overlay country borders, state outlines, sales territories, or custom regions on your maps.

By default, each dataset is limited to 5 MB and each account is limited to 100 datasets. You can set the dataset size limit and the maximum number of datasets for your environment or per tenant account by configuring `json.storage.max-size` and `json.storage.max-datasets-per-account`. See [zoomdata.properties Properties](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/properties-reference#json-dataset-properties).

<Note>
  Requests return `401 Unauthorized` if you aren't logged in, `400 Bad Request` for an invalid dataset ID or payload, `404 Not Found` if the dataset doesn't exist in your account, and `422 Unprocessable Entity` if the dataset can't be saved.
</Note>

#### POST

* `POST /api/json-datasets`: Creates a JSON dataset. Provide:

  * `name`: Required. Cannot be blank. Up to 255 characters. Must be unique in your account; names are case-sensitive.
  * `description`: Optional. Up to 512 characters.
  * `data`: Required. The shape data as a JSON object. It's stored as provided and isn't validated as `GeoJSON` or `TopoJSON`.

  Returns the full dataset record, including `id`, `accountId`, and the creation and modification details.

  <Note>
    Returns `409 Conflict` for a duplicate dataset name or if the account's dataset limit is reached, and `413 Payload Too Large` if the dataset exceeds the size limit.
  </Note>

#### GET

* `GET /api/json-datasets`: Returns the JSON datasets in your account. List results include metadata only: `id`, `name`, `description`, and timestamps. They exclude the dataset's `data` payload.
* `GET /api/json-datasets/{id}`: Returns the full details of a single JSON dataset, including its `data` payload.

#### PUT

* `PUT /api/json-datasets/{id}`: Updates a JSON dataset. Provide:

  * `name`: Required. Up to 255 characters. Must be unique in your account; names are case-sensitive.
  * `description`: Optional. Up to 512 characters. If you omit it, the existing description is kept. To clear it, send an empty value.
  * `data`: Required. The shape data as a JSON object. It's stored as provided and isn't validated as `GeoJSON` or `TopoJSON`.

  <Note>
    Returns `409 Conflict` for a duplicate dataset name and `413 Payload Too Large` if the updated dataset exceeds the size limit.
  </Note>

#### DELETE

* `DELETE /api/json-datasets/{id}`: Permanently deletes a JSON dataset.

<h3 id="api-trusted-access-sessions">
  /api/trusted-access/sessions
</h3>

Increased the maximum username length accepted by the trusted access session API from 40 to 255 characters.

<h2 id="bug-fixes">
  Bug Fixes
</h2>

<h3 id="tbl-ctx">
  Table Context Menu
</h3>

**26.3.0**

Corrected an issue where right-clicking a cell in the Pivot Table or Table visual didn't open the context menu as expected.

<h3 id="tbl-thm">
  Table Dark Theme Display
</h3>

**26.3.0**

Corrected an issue where some elements in table menus, tooltips, and pop-ups didn't display correctly when using the `dark` theme.

<h2 id="breaking-changes">
  Breaking Changes
</h2>

### System Users Menu Option

**26.3.0**

In environments where the [enhanced-experience](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#server-level-variables) toggle has been enabled, the menu option **System Users** has been removed from the main menu UI.

Users with appropriate privileges can instead access users using the **User** menu option, and groups using the **Groups** menu option.

<h3 id="helm-26.3">
  Helm Chart installController
</h3>

**26.3.0**

The helm chart for 26.3.0 has a breaking change: `ingress.installController` now defaults to `false`. The bundled `ingress-nginx` controller version this chart originally shipped has been retired.

Bring your own ingress controller or set `installController` back to `true` if you still rely on the bundled dependency.

<h2 id="known-issues">
  Known Issues
</h2>

<table>
  <thead>
    <tr>
      <th>Component or Feature</th>
      <th>Issue</th>
      <th>Work Around</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>Self-Service Report Microservice</td>

      <td>
        In this release, the Self-Service Report service is not included by default in the Self-Service Analytics installation bundle. Until you install this service, export requests will fail.

        <br />

        After you upgrade to Self-Service Analytics 26.3 or later, the service does not restart automatically. It reports a running state, but exports continue to fail until you restart it.
      </td>

      <td>
        Install the Self-Service Report microservice manually after you install Self-Service Analytics, and restart it manually after every upgrade. Confirm the result with a test export rather than relying on the service status.

        <br />

        For the commands for your platform, see [Install Self-Service Analytics - Linux](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-ov), [Upgrade Self-Service Analytics](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/upgrading-server), and [Install Self-Service Analytics - Windows](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-windows).
      </td>
    </tr>

    <tr>
      <td>OpenSearch Source Documentation Storage</td>

      <td>
        Raw data presentation will vary, depending on the source from which the raw field data is fetched. In particular, fused data sources may be affected where OpenSearch indices with different mappings are joined.

        <br />

        For example, when such indices are joined by an IP field and one of them allows data to be fetched from the original documents but another requires the data to be fetched from doc values.
      </td>

      <td>
        Ensure indices with similar or identical mappings are used in a fused data source. See Raw Data.

        <br />

        In an environment where Simba Agentic Intelligence is in use, define a workspace for the affected fields to bring them into cohesion before passing to Self-Service Analytics for processing. See Normalize Data Using Agentic Intelligence.
      </td>
    </tr>
  </tbody>
</table>

<h2 id="dependency-updates">
  Dependency Updates
</h2>

| Dependency | New Version | Previous Version |
| - | - | - |
| Java | Java 21 (Self-Service Analytics version 26.3 and later) | Java 17 (Composer version 26.2 and earlier) |
| Apache Calcite | 1.41 (Self-Service Analytics version 26.3 and later) | 1.38 (Composer version 26.2 and earlier) |
| PostgreSQL | 18 (chart-managed Self-Service Analytics version 26.3 and later) | Bitnami PostgreSQL 12 (Composer version 26.2 and earlier) |

<h2 id="operating-system-platform-support">
  Operating System Platform Support
</h2>

*List Updated: 30 June 2026*

<Warning>
  This information is provided to assist you in planning your future upgrade projects.
</Warning>

<Danger>
  Running an older, unsupported operating system in your environment is done so at your own risk. Plan and upgrade to a supported operating system for full support and functionality.
</Danger>

* RHEL 9 (Red Hat)

* CentOS Stream 9

* Ubuntu 22.04

  <Note>
    Older versions of Ubuntu are nearing end of life (EOL) support. Self-Service Analytics 26.3 and later will require an operating system upgrade before you upgrade your instance.
  </Note>

* Windows Server version and 2019 or higher.

For more information on previous, current, and future planned operating system support, see [Operating System Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/installation-prerequisites#operating-system-support).
