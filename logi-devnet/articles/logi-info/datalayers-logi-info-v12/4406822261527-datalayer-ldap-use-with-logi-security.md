---
title: "DataLayer.LDAP - Use with Logi Security"
id: 4406822261527
section: "Datalayers - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822261527-DataLayer-LDAP-Use-with-Logi-Security
updated_at: 2022-04-06T06:05:19Z
---

# DataLayer.LDAP - Use with Logi Security

# DataLayer.LDAP - Use with Logi Security

In order to authenticate users against an LDAP server, use the [DataLayer.LDAP Authentication](https://devnet.logianalytics.com/hc/en-us/articles/4406816908439-DataLayer-LDAP-Authentication) element.

When Logi Security is being used, DataLayer.LDAP can be used retrieve user rights from an LDAP server:

![](https://devnet.logianalytics.com/hc/article_attachments/4417584026391/dlldap_01.png)![](https://devnet.logianalytics.com/hc/article_attachments/4417584026775/dlldap_01a.png)  

As shown above, DataLayer.LDAP is added as a child of the **Rights From DataLayer** element, and its attributes configured as shown. The syntax for the **Source** attribute value follows the rules described in the next sections, and includes the token containing the identifying value for the current user, for example:

SELECT cn FROM 'dc=example,dc=com' WHERE objectClass ='group' AND member = '@Function.UserName~'
