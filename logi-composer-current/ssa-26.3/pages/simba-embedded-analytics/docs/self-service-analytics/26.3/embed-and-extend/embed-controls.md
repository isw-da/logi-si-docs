> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Embedded Self-Service Analytics Component Controls

When Self-Service Analytics components are embedded in your applications, the way in which a user can interact with them is determined by settings established by the dashboard, the dashboard visuals, the user's Self-Service Analytics user definition, and the groups and tenants to which that user belongs.

Specifically:

* Control whether your users can interact with a dashboard using [dashboard interactivity](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-interactivity) and [visual interactivity](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-interactivity) settings. If a user is only allowed to view the dashboard, they cannot interact with the dashboard at all. See [Embeddable Component Snippets](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/embed/dash-embed-gencode-dashboard) and [Embedded Dashboard Properties and Objects](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/embed/embed-javascript-embedmanager-methods#embedded-dashboard-properties-and-objects).

* In embedded environments, you can filter which dashboards are available by the tags applied to your dashboards. See [Embed Components Using JavaScript and Trusted Access](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/embed/embed-javascript).

* The dashboard permissions for the dashboard determine whether a dashboard is even visible for a user, a group, or a tenant. They also control the permitted level (read, write, or delete) at which the user, group, or account can use the dashboard. See [About Dashboard and Self Service Report Permissions](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-auth-permissions#about-dashboard-and-self-service-report-permissions).

* Data source permissions can restrict the use of data sources by Self-Service Analytics users, groups, or accounts. They also control the permitted level (read, write, or delete) at which the user, group, or account can use the data source. For example, if a dashboard is embedded that the user has permissions to read, write, and delete, but the user does not have permission to use the data source used by a visual on the dashboard, an error appears for the visual for that user when the dashboard is embedded. See [About Source Permissions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/ds-permissions).

* Data source row security can be used to filter the data in the data source used for a dashboard. Row security is applied to specific users, groups, or accounts. If row security is in place, you users will only see the data source data that meets the requirements of the row security filters. For example, your dashboard might show sales for many product categories, but the row security filter for the data source might limit the sales a given user can see to jewelry sales only. See [Restrict Access to Data Using Row and Column Security](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/ds-security-row).

* Data source column security can restrict the fields within a data source visible to a given group of users. For example, if the group to which a user is assigned does not have access to the actual sales figures provided in the **Actual Sales** field of a sales dashboard, that field will not be visible on the dashboard for that user group when the dashboard is embedded. See [Restrict Access to Fields Using Column Security](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/ds-security-row#restrict-access-to-fields-using-column-security).

* The interactivity settings of the visuals in the embedded dashboard control many aspects concerning how a visual can be used, including controls for what appears on the [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu). For example, you can restrict the ability of your end users to use the context menu for a specific visual on a dashboard. A complete list of the controls available using visual interactivity settings is provided in [Control How Users Interact With a Visual](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-interactivity).

* The interactivity settings of the embedded dashboard control many aspects concerning how the dashboard and all of its visuals can be used, including controls for what appears on the [dashboard icon bar](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-layout#use-the-dashboard-icons). For example you can restrict the ability of your end users to add or remove visuals from the dashboard. A complete list of the controls available using dashboard interactivity settings is provided in [Control How Users Interact With a Dashboard](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-interactivity).

* [Cross-visual filters](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/pubsub-ov) can be published or subscribed to. Use them to control how filters interact in a dashboard.

  <Note>
    When more than one dashboard is embedded in application, the cross-visual filters that are published for a visual on one of the dashboards can be subscribed to by any visual on any of the embedded dashboards. However, this is not true unless the dashboards are embedded in the same application. Visuals in a dashboard open in one window or tab cannot subscribe to cross-visual filters published by visuals in a different window or tab.
  </Note>
