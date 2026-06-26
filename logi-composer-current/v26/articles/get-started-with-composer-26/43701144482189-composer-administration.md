---
title: "Composer Administration"
id: 43701144482189
section: "Get Started With Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701144482189-Composer-Administration
updated_at: 2026-05-29T14:09:14Z
---

# Composer Administration

# Composer Administration

Composer makes visual analytics easy for end users. Composer administrators are a big part of that. This docs portal will help you install, configure, maintain, and upgrade Composer.

## How Do I Administer Composer?

Composer is much like any installed software in that the administrator manages the software's life-cycle. Some tasks need to be done only when you start out or want to upgrade Composer.

* Read the [Composer overview](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701141809421-Introduction-to-Composer-26).
* [Install Composer](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072793997-Install-Composer).
* [Configure Composer](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700991919117-Configuration-Property-Files).
* [Upgrade Composer](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701165056525-Upgrade-Composer) to a new version.
* [Manage Composer](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701119873037-About-Microservices) microservices.

**Important:** Composer uses a packaged PostgreSQL database instance to store its metadata. Use the provided instance due to the specific configuration and version combination:

* Logi Composer v24.2 and earlier: PostgreSQL 12
* Composer v24.3 and later: PostgreSQL 16

If you would like to use another PostgreSQL instance, contact [Technical Support](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072313613-Contact-Technical-Support) for further guidance.

**Note:** New installations of Logi Composer (v24.3 and later) use PostgreSQL 16. If you are upgrading your environment to v24.3 or later, you can retain your existing PostgreSQL version.

You do other tasks only as needed.

* Configure a [high availability](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701105065613-Configure-a-High-Availability-Environment) environment.
* [Manage connectors](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701042404749-Manage-Connectors-and-Connector-Servers) and [data source configurations](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701068934669-Manage-Data-Sources).
* [Create custom metrics and derived fields](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701030223373--Maintain-Custom-Metrics).
* Manage [tenants](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700956182925-Manage-Composer-Tenants), [groups](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701035505293-Manage-User-Groups),and [users](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701051820941-Manage-Users).
* Manage [activity logging](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701106334605-Activity-Logging).
* [Start](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701119873037-About-Microservices#Start) and [stop](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701119873037-About-Microservices#Stop) the Composer microservices.
* [Uninstall Composer.](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701120892685-Uninstall-Composer)

You'll need to do some maintenance tasks at regular intervals.

* [Review activity logs](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701136219917-Manage-Activity-Logs).
