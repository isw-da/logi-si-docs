---
title: "DataLayer.LDAP - Attributes"
id: 4419707493015
section: "Datalayers - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707493015-DataLayer-LDAP-Attributes
updated_at: 2022-07-17T01:53:20Z
---

# DataLayer.LDAP - Attributes

# DataLayer.LDAP - Attributes

The DataLayer.LDAP element has the following attributes:

| Attribute | Description |
| --- | --- |
| ID | An optional element ID. Recommended for easier identification when debugging. |
| Source | (Required) Specifies a query statement using a SQL-like syntax that returns a rowset of LDAP records, such as users, rights, groups, devices and other collections available from the LDAP server. See the LDAP Query Syntax sections below for more information. |
| Connection ID | The ID of a **Connection.LDAP** element defined in the \_Settings definition. If this value is left blank, the datalayer will try to use the *first* connection element in the \_Settings definition. For clarity, developers are advised to enter an ID here in all cases. |
