---
title: "Metadata Repository"
id: 4402537836311
section: "Logi Composer v5 Overview"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402537836311-Metadata-Repository
updated_at: 2021-09-15T02:22:10Z
---

# Metadata Repository

# Metadata Repository

Metadata is any data that is used for the configuration and runtime operation of the Composer application, with the exception of customer-managed data stores. The metadata repository is simply the relational database instance containing the Composer schemas. The primary metadata schema includes configurations for:

* dashboards, visuals, and filters
* data store connectivity
* data source configurations and statistics
* enterprise authentication, accounts, users, groups, and permissions.

The metadata repository also contains separate schemas for storing raw data, which supports upload and keyset functionality. Note that the metadata schema definitions and the stored data are internal to the Composer application; they are not intended for direct manipulation.

Composer uses relational database technology for metadata storage, and ships with an open-source PostgreSQL 12 database. Composer strongly recommends using this instance due to the specific configuration and version employed. If you would like to use another PostgreSQL instance, contact [Technical Support](https://devnet.logianalytics.com/hc/en-us/articles/4402552854679-Contact-Technical-Support) for further guidance.

Internally, industry-standard technologies are used for database connectivity, object-relational mapping, and schema changes that are executed during Composer software upgrades. The database administrator can use well-known tools and procedures for backing up and restoring the entire metadata repository. The administrator is responsible for setting up authenticated access from the Composer server to the database.
