---
title: "Get Started With Composer 26"
id: 43701104724621
section: "Get Started With Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701104724621-Get-Started-With-Composer-26
updated_at: 2026-05-29T14:08:38Z
---

# Get Started With Composer 26

# Get Started With Composer 26

The following steps guide you through the process of installing and configuring the Composer platform and provides an overview of developing embeddable content. In addition, read [Composer Personas](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701122556941-Composer-Personas) for a descriptions of the different job skills that contribute to the successful implementation and use of Composer.

Some of the setup work described below requires use of the Composer API.

API documentation is provided in your environment at this link: `https://<composer-URL>/composer/swagger-ui.html`.

[1. Product Installation](#)

1. Verify you have a server available that meets the sizing requirements of Composer. See [Server Size Guidelines](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701073249037-Server-Size-Guidelines) and [System Requirements](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701105740685-System-Requirements) and [Installation Prerequisites](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701135037709-Installation-Prerequisites).
2. Install Composer using the supplied bootstrap script. See [Installation Steps](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701120422797-Installation-Steps). Optionally, install the product and its metadata store manually (see [Install Composer Manually](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701105134605-Install-Composer-Manually)).
3. Optionally, configure Composer servers in a distributed environment (either a load balanced environment or a high availability environment). See [Configure a Distributed Composer Environment](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701120036749-Configure-a-Distributed-Composer-Environment).
4. License the product, if a new license is required. See [Request and Apply a New License Key](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701121443341-Request-and-Apply-a-New-License-Key).

[2. Product Security and Authorization](#)

1. Integrate with your security software (LDAP, SAML, Kerberos, or X.509). See [Supported Authentication Tools](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701127697165-Supported-Authentication-Tools).
2. Set up tenants, users, and groups, with appropriate privileges. See [Authorize Composer Access](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701020778765-Authorize-Composer-Access).
3. Define custom attributes, as needed, for each user. Custom attributes provide a way for administrators to create variables in user definitions. These variables can be interpolated in other fields elsewhere in the product. See [Specify Custom User Attributes](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701051547533-Specify-Custom-User-Attributes).

[3. Data Store Connector and Connection Configuration](#)

1. Log in as the supplied [admin user](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701036219149-Supplied-Users-and-User-Groups#The2) (System Administrator) or a member of the Supervisors group and set up the connectors needed to support the data stores your organization uses and that you will want to use for data source configurations. See [Manage Connectors and Connector Servers](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701042404749-Manage-Connectors-and-Connector-Servers).
2. Log in as an administrator and define the connection strings necessary for the connectors to access your data stores. See [Manage Data Store Connections](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701038107149-Manage-Data-Store-Connections).

[4. Product Configuration](#)

1. Activate logging. (regular -- Fluentd optional) See [Activity Logging](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701106334605-Activity-Logging), [Manage Activity Logs](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701136219917-Manage-Activity-Logs), and [Set Up Unified Logging Using Fluentd](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701136195213-Set-Up-Unified-Logging-Using-Fluentd).
2. Optionally, create custom charts needed by your organization. [Manage Custom Charts](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701046331405-Manage-Custom-Charts).
3. Optionally, create admin-defined functions needed for your environment. [Admin-Defined Functions](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701029797901-Admin-Defined-Functions).
4. Optionally, configure a different theme for the your environment's UI. See [Manage UI Themes](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701163831053-Manage-UI-Themes).
5. Optionally, customize the UI for your environment. See [Customize the User Interface](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701054077581-Customize-the-User-Interface).

[5. Data Authoring](#)

1. Identify the data you need to use from your data stores to perform the data analytics you want.
2. Define data source configurations that collect the data you need. Data source configurations use the data store connections previously defined. See [Manage Data Sources](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701068934669-Manage-Data-Sources).
3. Optionally, configure row and column security for your data sources. See [Restrict Access to Data Using Row Security](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701069473293-Restrict-Access-to-Data-Using-Row-Security) and [Restrict Access to Fields Using Column Security](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701069320333-Restrict-Access-to-Fields-Using-Column-Security).
4. Optionally, configure permissions for each data source. See [About Source Permissions](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701101615373-About-Source-Permissions).

[6. Dashboard and Visual Creation](#)

1. Configure the dashboards and visuals needed to analyze your data. See [Manage Dashboards](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701029082893-Manage-Dashboards) and [Manage Visuals](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701171638925-Manage-Visuals).
2. Optionally, configure permissions for each dashboard. See [About Dashboard Permissions](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701076423437-About-Dashboard-Permissions).
3. Optionally, specify how each visual can be interacted with when embedded. See [Control How Users Interact With a Visual](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701185104653-Control-How-Users-Interact-With-a-Visual).
4. Optionally, share dashboards with other users in your tenant. See [Share a Dashboard with Users](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701077162637-Share-a-Dashboard-with-Users).
5. Optionally, export a dashboard. See [Export Dashboards](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701076601229-Export-Dashboards).
6. Optionally, schedule a dashboard report. See [About Scheduled Dashboard Reports](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700998266509-About-Scheduled-Dashboard-Reports).

[7. Dashboard Embedding](#)

1. Set up Trusted Access and register your application as a client. See [Trusted Access](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701128164493-Trusted-Access).
2. Embed dashboards in your applications. See [Embed Components Into Your Application](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701093407501-Embed-Components-Into-Your-Application).
3. Optionally, enable embedded dashboard access from other sites using cross-origin sharing (CORS). See [Enable Composer Component Access From Other Sites Using Cross-Origin Resource Sharing (CORS)](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701054098061-Enable-Composer-Component-Access-From-Other-Sites-Using-Cross-Origin-Resource-Sharing-CORS).

The following additional topics may also be helpful.

* [Access Logi Composer](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701052048397-Access-Logi-Composer)
* [Log Into the Logi Composer UI](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700988311437-Log-Into-the-Logi-Composer-UI)
* [Switch Tenants](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701052090125-Switch-Tenants)
* [Home Page](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701136935821-Home-Page)
* [About Dialog](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701106879757-About-Dialog)
