---
title: "Get Started with Composer v6"
id: 4405851075991
section: "Get Started with Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851075991-Get-Started-with-Composer-v6
updated_at: 2021-09-21T01:28:43Z
---

# Get Started with Composer v6

# Get Started with Composer v6

The following steps guide you through the process of installing and configuring the Composer platform and provides an overview of developing embeddable content. In addition, read [*Composer Personas*](https://devnet.logianalytics.com/hc/en-us/articles/4405859416983-Composer-Personas) for a descriptions of the different job skills that contribute to the successful implementation and use of Composer.

Some of the setup work described below requires use of the Composer API. API documentation is provided with your Composer installation at this link: `https://<composer-URL>/composer/swagger-ui.html`.

1. Product Installation

1. Verify you have a server available that meets the sizing requirements of Composer. See [*Server Size Guidelines*](https://devnet.logianalytics.com/hc/en-us/articles/4405851099543-Server-Size-Guidelines) and [*System Requirements*](https://devnet.logianalytics.com/hc/en-us/articles/4405859384727-System-Requirements) and [*Installation Prerequisites*](https://devnet.logianalytics.com/hc/en-us/articles/4405851087895-Installation-Prerequisites).This video demonstrates the use of common commands to show your server's CPU, memory, and disk space availability: <https://vimeo.com/548076115>
2. Install Composer using the supplied bootstrap script. See [*Installation Steps*](https://devnet.logianalytics.com/hc/en-us/articles/4405851088791-Installation-Steps). Optionally, install the product and its metadata store manually (see [*Install Composer Manually*](https://devnet.logianalytics.com/hc/en-us/articles/4405851085207-Install-Composer-Manually)). The following two videos can help you.

   * The first video downloads the bootstrap installation script and runs it: <https://vimeo.com/548076448>
   * The second video demonstrates the rest of the installation after the bootstrap installation script has completed: <https://vimeo.com/548076528>
3. Optionally, configure Composer servers in a distributed environment (either a load balanced environment or a high availability environment). See [*Configure a Composer Distributed Environment*](https://devnet.logianalytics.com/hc/en-us/articles/4405851080471-Configure-a-Composer-Distributed-Environment).
4. License the product, if a new license is required. See [*Request and Apply a New License Key*](https://devnet.logianalytics.com/hc/en-us/articles/4405851108247-Request-and-Apply-a-New-License-Key).

2. Product Security and Authorization

1. Integrate with your security software (LDAP, SAML, OAuth, Kerberos, or X 509). See [*Supported Authentication Tools*](https://devnet.logianalytics.com/hc/en-us/articles/4405851167639-Supported-Authentication-Tools).
2. Set up Composer accounts, user definitions, and groups, with appropriate privileges. See [*Authorize Composer Access*](https://devnet.logianalytics.com/hc/en-us/articles/4405850851607-Authorize-Composer-Access).
3. Define custom attributes, as needed, for each user. Custom attributes provide a way for administrators to create variables in user definitions. These variables can be interpolated in other fields elsewhere in the product. See [*Specify Custom User Attributes*](https://devnet.logianalytics.com/hc/en-us/articles/4405850862359-Specify-Custom-User-Attributes).

3. Data Store Connector and Connection Configuration

1. Log in as a supervisor and set up the Composer connectors needed to support the data stores your organization uses and that you will want to use for Composer data source configurations. See [*Manage Connectors and Connector Servers*](https://devnet.logianalytics.com/hc/en-us/articles/4405859186199-Manage-Connectors-and-Connector-Servers).
2. Log in as an administrator and define the connection strings necessary for the Composer connectors to access your data stores. See [*Manage Data Store Connections*](https://devnet.logianalytics.com/hc/en-us/articles/4405850909079-Manage-Data-Store-Connections).

4. Product Configuration

1. Activate logging. (regular -- Fluentd optional) See [*Activity Logging*](https://devnet.logianalytics.com/hc/en-us/articles/4405851110039-Activity-Logging), [*Manage Activity Logs*](https://devnet.logianalytics.com/hc/en-us/articles/4405851111959-Manage-Activity-Logs), and [*Set Up Unified Logging Using Fluentd*](https://devnet.logianalytics.com/hc/en-us/articles/4405859397655-Set-Up-Unified-Logging-Using-Fluentd).
2. Optionally, create custom charts needed by your organization. [*Manage Custom Charts*](https://devnet.logianalytics.com/hc/en-us/articles/4405859248279-Manage-Custom-Charts).
3. Optionally, create admin-defined functions needed for your environment. [*Admin-Defined Functions*](https://devnet.logianalytics.com/hc/en-us/articles/4405850995991-Admin-Defined-Functions).
4. Optionally, configure a different theme for the Composer UI. See [*Manage UI Themes*](https://devnet.logianalytics.com/hc/en-us/articles/4405859480983-Manage-UI-Themes).
5. Optionally, customize the Composer UI for your organization. See [*Customize the Composer User Interface*](https://devnet.logianalytics.com/hc/en-us/articles/4405850900887-Customize-the-Composer-User-Interface).

5. Data Authoring

1. Identify the data you need to use from your data stores to perform the data analytics you want.
2. Define data source configurations that collect the data you need. Data source configurations use the data store connections previously defined. See [*Manage Data Source Configurations*](https://devnet.logianalytics.com/hc/en-us/articles/4405851027479-Manage-Data-Source-Configurations).
3. Optionally, configure row and column security for your data sources. See [*Restrict Access to Data Using Row Security*](https://devnet.logianalytics.com/hc/en-us/articles/4405859333655-Restrict-Access-to-Data-Using-Row-Security) and [*Restrict Access to Fields Using Column Security*](https://devnet.logianalytics.com/hc/en-us/articles/4405851034007-Restrict-Access-to-Fields-Using-Column-Security).
4. Optionally, configure permissions for each data source. See [*About Data Source Permissions*](https://devnet.logianalytics.com/hc/en-us/articles/4405859328535-About-Data-Source-Permissions).

6. Dashboard and Visual Creation

1. Configure the dashboards and visuals needed to analyze your data. See [*Manage Dashboards*](https://devnet.logianalytics.com/hc/en-us/articles/4405850985623-Manage-Dashboards) and [*Manage Visuals*](https://devnet.logianalytics.com/hc/en-us/articles/4405851259671-Manage-Visuals)
2. Optionally, configure permissions for each dashboard. See [*About Dashboard Permissions*](https://devnet.logianalytics.com/hc/en-us/articles/4405859259159-About-Dashboard-Permissions).
3. Optionally, specify how each visual can be interacted with when embedded. See [*Control How Users Interact With a Visual*](https://devnet.logianalytics.com/hc/en-us/articles/4405859573143-Control-How-Users-Interact-With-a-Visual).
4. Optionally, share dashboards with other Composer users in your account. See [*Share a Dashboard with Users Inside Your Account*](https://devnet.logianalytics.com/hc/en-us/articles/4405859272471-Share-a-Dashboard-with-Users-Inside-Your-Account).
5. Optionally, export a dashboard. See [*Export a Dashboard*](https://devnet.logianalytics.com/hc/en-us/articles/4405850982935-Export-a-Dashboard).
6. Optionally, schedule a dashboard report. See [*About Scheduled Dashboard Reports*](https://devnet.logianalytics.com/hc/en-us/articles/4405850989335-About-Scheduled-Dashboard-Reports).

7. Dashboard Embedding

1. Set up Trusted Access and register your application as a client. See [*Trusted Access*](https://devnet.logianalytics.com/hc/en-us/articles/4405851181463-Trusted-Access).
2. Embed Composer dashboards in your applications. See [*Embed Composer Components Into Your Application*](https://devnet.logianalytics.com/hc/en-us/articles/4405859263895-Embed-Composer-Components-Into-Your-Application).
3. Optionally, enable embedded dashboard access from other sites using cross-origin sharing (CORS). See [*Enable Composer Component Access From Other Sites Using Cross-Origin Resource Sharing (CORS)*](https://devnet.logianalytics.com/hc/en-us/articles/4405850901783-Enable-Composer-Component-Access-From-Other-Sites-Using-Cross-Origin-Resource-Sharing-CORS-).

The following additional topics may also be helpful.

* [*Access Composer*](https://devnet.logianalytics.com/hc/en-us/articles/4405850867223-Access-Composer)
* [*Log Into the Composer UI*](https://devnet.logianalytics.com/hc/en-us/articles/4405850868119-Log-Into-the-Composer-UI)
* [*Switch Accounts*](https://devnet.logianalytics.com/hc/en-us/articles/4405850869015-Switch-Accounts)
* [*Home Page*](https://devnet.logianalytics.com/hc/en-us/articles/4405851121559-Home-Page)
* [*About Dialog*](https://devnet.logianalytics.com/hc/en-us/articles/4405851114903-About-Dialog)
