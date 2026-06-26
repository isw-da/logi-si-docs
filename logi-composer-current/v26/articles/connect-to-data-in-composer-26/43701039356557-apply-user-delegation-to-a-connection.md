---
title: "Apply User Delegation to a Connection"
id: 43701039356557
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701039356557-Apply-User-Delegation-to-a-Connection
updated_at: 2026-05-29T14:11:30Z
---

# Apply User Delegation to a Connection

# Apply User Delegation to a Connection

Applying user delegation to a Composer data source connection definition involves setting the **Do As User** parameter in the connection definition and setting up proxy user features in your data store. Any authentication mechanism (Kerberos or LDAP) and group mapping (file system or LDAP-based) method can be used by the data store or Composer, as long as the user name assigned to the **Do As User** connector parameter is allowed appropriate authorizations (delegation) in the data store configuration.

**Note:** 
Supervisors group members [enables user delegation](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701039382541-Enable-User-Delegation) via a custom user attribute. Administrators [enable](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701039382541-Enable-User-Delegation) and apply user delegation to the data connection definition for a data source.

User delegation processing is depicted in the following diagram.

![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242756235405)

User delegation occurs in this manner:

1. The Composersupervisor group member or administrator assigns any LDAP attribute (for example, `cn`, `sAMAccountName`, `name`) to a custom user attribute. This should be provided by your data store administrator. The only requirement is that this attribute must match the configuration in Sentry. See [Enable User Delegation](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701039382541-Enable-User-Delegation).

   The Composer custom user attribute is referenced by its name, prefaced by the word `User`. For example, if your custom user attribute is named `XXXUserName`, you would reference it as `User.XXXUserName`.
2. The Composer administrator references the custom user attribute in the appropriate data source connection definition using the connection's **Do As User** box. For example:

   ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242725056397)
3. When a user submits a query using the data source, the Composer connector sends the user identified by the **Do As User** parameter (or as interpreted by the setting in that parameter) to the data store when it connects on behalf of the query.

   Assuming user proxy (user delegation) features are set up properly on the data store, the data store runs the query on behalf of the user. For information on setting up user proxy, user impersonation, or user delegation features in each data store, see the following links.

   | Data Store | User Proxy Setup Links |
   | --- | --- |
   | Apache Drill | * <https://drill.apache.org/docs/configuring-user-impersonation/> * <https://drill.apache.org/docs/configuring-inbound-impersonation/> |
   | Cloudera Impala | * <https://docs.cloudera.com/documentation/enterprise/latest/topics/impala_delegation.html> |
   | Cloudera Search | * <https://docs.cloudera.com/documentation/enterprise/latest/topics/impala_delegation.html> * <https://docs.cloudera.com/documentation/enterprise/5-12-x/topics/search_ha_proxy.html> * <https://docs.cloudera.com/documentation/enterprise/5-10-x/topics/admin_hdfs_proxy_users.html> |
   | Hive | * <https://community.cloudera.com/t5/Community-Articles/Enable-DoAs-option-Hive-to-allow-users-to-runs-queries-with/ta-p/247400> * <https://docs.cloudera.com/documentation/enterprise/5-8-x/topics/cdh_sg_hiveserver2_security.html#concept_vjq_c3x_nm> * <https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/Superusers.html> |
