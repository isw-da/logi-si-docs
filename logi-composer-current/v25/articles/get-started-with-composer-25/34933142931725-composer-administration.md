---
title: "Composer Administration"
id: 34933142931725
section: "Get Started With Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933142931725-Composer-Administration
updated_at: 2026-05-26T22:08:02Z
---

# Composer Administration

# Composer Administration

Composer makes visual analytics easy for end users. Composer administrators are a big part of that. This docs portal will help you install, configure, maintain, and upgrade Composer.

## How Do I Administer Composer?

Composer is much like any installed software in that the administrator manages the software's life-cycle. Some tasks need to be done only when you start out or want to upgrade Composer.

* Read the [Composer overview](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933090408205-Introduction-to-Composer-25).
* [Install Composer](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933011559565-Install-Composer).
* [Configure Composer](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932670123533-Configuration-Property-Files).
* [Upgrade Composer](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933226897037-Upgrade-Composer) to a new version.
* [Manage Composer](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/35385540487565-About-Microservices) microservices.

**Important:** Composer uses a packaged PostgreSQL database instance to store its metadata. Use the provided instance due to the specific configuration and version combination:

* Logi Composer v24.2 and earlier: PostgreSQL 12
* Composer v24.3 and later: PostgreSQL 16

If you would like to use another PostgreSQL instance, contact [Technical Support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932980712461-Contact-Technical-Support) for further guidance.

**Note:** New installations of Logi Composer (v24.3 and later) use PostgreSQL 16. If you are upgrading your environment to v24.3 or later, you can retain your existing PostgreSQL version.

You do other tasks only as needed.

* Configure a [high availability](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933027142285-Configure-a-High-Availability-Environment) environment.
* [Manage connectors](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932741363981-Manage-Connectors-and-Connector-Servers) and [data source configurations](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932941009037-Manage-Data-Sources).
* [Create custom metrics and derived fields](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932836147341--Maintain-Custom-Metrics).
* Manage [tenants](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932649111693-Manage-Composer-Tenants), [groups](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932593467277-Manage-User-Groups),and [users](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932578960909-Manage-Users).
* Manage [activity logging](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933086348813-Activity-Logging).
* [Start](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/35385540487565-About-Microservices#Start) and [stop](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/35385540487565-About-Microservices#Stop) the Composer microservices.
* [Uninstall Composer.](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933015054989-Uninstall-Composer)

You'll need to do some maintenance tasks at regular intervals.

* [Review activity logs](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933069110925-Manage-Activity-Logs).
