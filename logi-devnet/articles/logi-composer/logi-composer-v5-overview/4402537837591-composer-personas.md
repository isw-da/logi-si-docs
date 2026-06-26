---
title: "Composer Personas"
id: 4402537837591
section: "Logi Composer v5 Overview"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402537837591-Composer-Personas
updated_at: 2021-09-15T02:22:12Z
---

# Composer Personas

# Composer Personas

The successful implementation and use of Composer requires the completion of tasks that require different job skills. Whether these tasks are performed by one person or by more than one person varies by organization. This topic describes the different skills needed.

* Somebody with the authorization and skills to install the Composer software as a standalone product, in a high availability environment, or behind a load balancer. This person must understand your server and database infrastructure. Typically, this is someone in Operations.
* Somebody who manages licensing of the product.
* One or more people to manage product security, including:

  + Your organization's authentication tools (X.509, SAML, Kerberos, OAuth, or LDAP) and their integration into Composer
  + The Composer accounts, users, and groups required by your organization.
* One or more people to manage configuration of the product. Among other things, configuration can include tasks such as setting up logging, creating and managing custom charts and admin-defined functions, or tailoring the theme and other features of the UI as needed by your organization. Typically, this would be a system developer.
* Somebody who manages the Composer connectors and connector server definitions needed by Composer for your data stores. This person would also create the Composer connection definitions needed to access those data stores. Typically, this is a database administrator.
* Somebody to define Composer data source configurations from the data available in your data stores. This person must understand the data in your data stores and how it will be used. They must also understand who should have access to the data in each data source and whether access should be controlled by column or row. This person may be referred to as a *data author*.
* One or more people who can create meaningful dashboards and visuals that help your organization analyze the data you've collected. These people need to be able to specify who should have access to the dashboard data and the dashboard functions available for end users to interact with after the dashboard is embedded in your application. This person may be referred to as a *content author*.
* One or more people to embed your dashboards into your applications. Typically, this is an application developer.
