---
title: "DataLayer.LDAP - Use with Logi Security"
id: 4419722829719
section: "Datalayers - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722829719-DataLayer-LDAP-Use-with-Logi-Security
updated_at: 2022-07-17T02:24:39Z
---

# DataLayer.LDAP - Use with Logi Security

# DataLayer.LDAP - Use with Logi Security

In order to authenticate users against an LDAP server, use the [DataLayer.LDAP - DataLayer.LDAP Authentication](https://devnet.logianalytics.com/hc/en-us/articles/4419707245463-DataLayer-LDAP-DataLayer-LDAP-Authentication) element.

When Logi Security is being used, DataLayer.LDAP can be used retrieve user rights from an LDAP server:

![](https://devnet.logianalytics.com/hc/article_attachments/7522826374679/dlldap_01.png)![](https://devnet.logianalytics.com/hc/article_attachments/7522843004695/dlldap_01a.png)  

As shown above, DataLayer.LDAP is added as a child of the **Rights From DataLayer** element, and its attributes configured as shown. The syntax for the **Source** attribute value follows the rules described in the next sections, and includes the token containing the identifying value for the current user, for example:

SELECT cn FROM 'dc=example,dc=com' WHERE objectClass ='group' AND member = '@Function.UserName~'
