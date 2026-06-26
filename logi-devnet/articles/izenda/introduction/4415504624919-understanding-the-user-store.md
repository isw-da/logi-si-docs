---
title: "Understanding the User Store"
id: 4415504624919
section: "Introduction"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415504624919-Understanding-the-User-Store
updated_at: 2021-12-10T03:08:03Z
---

# Understanding the User Store

# Understanding the User Store

The User Store is one of the three tiers of Izenda’s Architecture and is
designed to manage all data interactions within Izenda. Within the User
Store, the Configuration Database stores all relevant reporting data.
The Configuration Database is set up during the [installation
process](https://devnet.logianalytics.com/hc/en-us/articles/4415511914903-Installation-Guide) and can be hosted on various [types
of databases.](https://devnet.logianalytics.com/hc/en-us/articles/4415492685975-Supported-Database-Types).

[![../_images/UserStore.jpg](https://devnet.logianalytics.com/hc/article_attachments/4415492448279/userstore_1184x546.jpg)](https://devnet.logianalytics.com/hc/article_attachments/4415492448023/userstore.jpg)

## What The Configuration Database Contains (High Level)

* Encrypted Database Connection Strings
* User identifier information
* Report Definitions
* Report Metadata (e.g. revision history previously saved versions)

## What The Configuration Database Does Not Contain (High Level)

* A backdoor to your data
* A backdoor to your user identities (Social Security numbers, spouse
  names, favorite colors)

## Connection to Izenda Servers

* In online mode, the User Store is used routinely to verify the
  license.
* Reports Definitions, User Definitions, and Connection Strings are not
  backed up on Izenda servers.
