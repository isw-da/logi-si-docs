---
title: "DataLayer.LDAP Authentication"
id: 4406816908439
section: "Datalayers - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406816908439-DataLayer-LDAP-Authentication
updated_at: 2022-04-06T06:02:47Z
---

# DataLayer.LDAP Authentication

# DataLayer.LDAP Authentication

The Lightweight Directory Access Protocol (LDAP) is an application protocol for reading and editing hierarchical sets of records over a network. Common implementations include user information and directory services. This topic introduces the developer to the **DataLayer.LDAP Authentication** element, which can be used to authenticate a user against an LDAP server.

The following sections are covered in this topic:

* Attributes
* [Working with DataLayer.LDAP Authentication](#sec1)

## Attributes

The DataLayer.LDAP Authentication element has the following attributes:

| Attribute | Description |
| --- | --- |
| ID | An optional element ID. Recommended for easier identification when debugging. |
| Connection ID | (Required) The ID of a **Connection.LDAP** element defined in the \_Settings definition. If this value is left blank, the datalayer will try to use the *first* connection element in the \_Settings definition. For clarity, developers are advised to enter an ID here in all cases. |
| Password | (Required) Specifies the password for an LDAP distinguished name (DN). Usually as a token with the value of the password passed from the standard or customized logon page: @Request.rdPassword~. |
| User DN Source | (Required) Specifies an LDAP query that returns the LDAP User Distinguished Name (DN). The returned DN will be used with the Password attribute to authenticate the current user. The query usually includes LDAP objects and names appropriate to your LDAP server and a token with the value of the user name passed from the standard or customized logon page, @Request.rdUsername~. Example LDAP queries: (.NET and Standard LDAP Server)  SELECT ADsPath FROM 'OU=Staff, DC=example, DC=com' WHERE uid='@Request.rdUserName~' AND objectClass='InetOrgPerson'(.NET and Active Directory Server) SELECT ADsPath FROM 'DC=myCompanyDomain, DC=local' WHERE  SamAccountName= '@Request.rdUserName~' AND objectClass='organizationalPerson'(Java and Standard LDAP Server)  SELECT DN FROM subTreeScope;  WHERE uid='@Request.rdUserName~' AND objectClass= 'InetOrgPerson' (Java and Active Directory Server) SELECT CN FROM DC=myCompanyDomain, DC=local WHERE  SamAccountName='@Request.rdUserName~' AND objectClass='organizationalPerson'  Prior to v10.0.503, this attribute was named "User DN". |

## Working with DataLayer.LDAP Authentication

This datalayer can only be used as a child of the Authentication element in the \_Settings definition.

Unlike other datalayers, DataLayer.LDAP Authentication retrieves only a single record, if authentication succeeds, containing the **Common Name** attribute associated with the supplied user identifier. If authentication fails, nothing is returned. This datalayer does not have any child elements for filtering, joining, or extending its data.

The data retrieved into the datalayer can be viewed by turning on the **Debugging Link** in your \_Settings definition (General element) and using the resulting link at the bottom of your report page to view the **Debugger Trace** page. A link on the Trace page will display the retrieved data.
