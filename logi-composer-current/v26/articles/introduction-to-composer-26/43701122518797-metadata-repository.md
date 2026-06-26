---
title: "Metadata Repository"
id: 43701122518797
section: "Introduction to Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701122518797-Metadata-Repository
updated_at: 2026-05-29T14:09:06Z
---

# Metadata Repository

# Metadata Repository

Metadata is any data that is used for the configuration and runtime operation of the Composer application, with the exception of customer-managed data stores. The metadata repository is simply the relational database instance containing the Composer schemas. The primary metadata schema includes configurations for:

* dashboards, visuals, and filters
* data store connectivity
* data source configurations and statistics
* enterprise authentication, accounts, users, groups, and permissions.

The metadata repository also contains separate schemas for storing raw data, which supports upload and keyset functionality. Note that the metadata schema definitions and the stored data are internal to the Composer application; they are not intended for direct manipulation.

Composer uses relational database technology for metadata storage, and ships with an open-source PostgreSQL database.

**Important:** Composer uses a packaged PostgreSQL database instance to store its metadata. Use the provided instance due to the specific configuration and version combination:

If you would like to use another PostgreSQL instance, contact [Technical Support](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072313613-Contact-Technical-Support) for further guidance.

**Note:** New installations of Logi Composer (v24.3 and later) use PostgreSQL 16. If you are upgrading your environment to v24.3 or later, you can retain your existing PostgreSQL version.

Internally, industry-standard technologies are used for database connectivity, object-relational mapping, and schema changes that are executed during Composer software upgrades. The database administrator can use well-known tools and procedures for backing up and restoring the entire metadata repository. The administrator is responsible for setting up authenticated access from the Composer server to the database.
