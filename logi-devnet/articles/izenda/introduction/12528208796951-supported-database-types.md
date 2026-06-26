---
title: "Supported Database Types"
id: 12528208796951
section: "Introduction"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528208796951-Supported-Database-Types
updated_at: 2023-02-19T08:35:46Z
---

# Supported Database Types

[Skip To Main Content](#)

Account

Settings

---

Logout

* placeholder

Account

Settings

---

Logout

Filter: 

* All Files

Submit Search

# Supported Database Types

## Supported Databases

Izenda fully supports the following database servers:

> * Microsoft SQL Server 2008 or later
> * Microsoft Azure
> * Oracle 10.2 or later
> * MySQL (For optimal performance MySQL 5.7+ is suggested. MySQL 5.7 includes major performance enhancements to derived tables/subqueries which are used throughout Izenda.)
> * PostgreSQL 9.3+
> * AWS Redshift (Izenda supports Redshift as a reporting database only (not a configuration database)) **New in version 2.7.0**
> * Elasticsearch (Izenda supports Elastic as a reporting database only (not a configuration database)) **New in version 2.18.0**
> * MongoDB (Izenda supports Mongo as a reporting database only (not a configuration database)) **New in version 3.1.0**

## Cubes Support

> SSAS (SQL Server Analysis Services) cubes cannot be used directly as
> data sources; however, an MDX (Multidimensional Expression) query
> can be written to flatten the cube which Izenda can then report
> against.

## Connection String Setup

Connection string setup is outlined in our Installation and Maintenance
Guide as well as our Administrator Guide.

* Refer to the [System DB and License](https://devnet.logianalytics.com/hc/en-us/articles/12528284579991-System-DB-and-License)
  section and the Connection String section
  for more information.
