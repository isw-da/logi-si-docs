---
title: "Enable User Delegation"
id: 4405859193111
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859193111-Enable-User-Delegation
updated_at: 2021-09-21T01:27:14Z
---

# Enable User Delegation

# Enable User Delegation

You can use user delegation to run queries on behalf of Composer users using a single set of credentials for a number of Composer connectors. This allows you to share a single connection configuration among all users. User delegation can be established on a per-user or a per-group basis.

User delegation is currently supported by the following Composer connectors: Apache Drill, Cloudera Impala, Cloudera Search, and Hive. The Composer Oracle connector supports user delegation only via user credential pass-through.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) The Composer supervisor enables user delegation via a custom user attribute. Composer administrators [apply user delegation](https://devnet.logianalytics.com/hc/en-us/articles/4405850928919-Apply-User-Delegation-to-a-Connection) to the data connection definition for a data source.

To enable user delegation:

1. Log into the Composer server as a supervisor.
2. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743720343/hamburger.png) to see the [supervisor menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859441687-The-Composer-Supervisor-Menu).
3. Select **Security** on the supervisor menu. The security tabs display.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747450007/security-services_450x221.png)
4. Select the **LDAP Settings** tab. The LDAP Settings tab has five sections: **General Settings**, **LDAP Server**, **User Provisioning**, **Mappings**, and **Mappings to Custom User Attributes**.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) If the LDAP tab cannot be selected, verify that the LDAP security service is enabled. See [*Use Lightweight Directory Access Protocol (LDAP) With Composer*](https://devnet.logianalytics.com/hc/en-us/articles/4405859462551-Use-Lightweight-Directory-Access-Protocol-LDAP-With-Composer).
5. In the **Mapping to Custom User Attributes** section, select **Add Custom User Attribute**.
6. Type any meaningful name for the custom attribute name.
7. Match the new attribute to any LDAP attribute (for example, cn, sAMAccountName, name). This should be provided by an Impala administrator. The only requirement is that this attribute match the configuration in Sentry.
8. Select **Save** to save the attribute.

   The custom user attribute is referenced by its name, prefaced by the word `User`. For example, if your custom user attribute is named `XXXUserName`, you would reference it as `User.XXXUserName`. This reference name is shown in the **Usage** column.
9. Select **Connectors** on the supervisor menu. The Manage Connector Services page appears. This page has two tables: one for Connector Servers and one for Connectors.
10. Scroll down to the Connectors table and select the appropriate connector from the list. The connector settings page displays.

    ![](https://devnet.logianalytics.com/hc/article_attachments/4406747450263/impala-connector_421x310.png)
11. Scroll down to the Connector Parameters and verify that the checkbox in the **User Attribute** column for the **DO\_AS\_USER** parameter is selected. This ensures that the **DO\_AS\_USER** parameter is visible and can be set in your Impala connection.
12. Select **Save**.

To apply user delegation to a data source connection definition, see [*Apply User Delegation to a Connection*](https://devnet.logianalytics.com/hc/en-us/articles/4405850928919-Apply-User-Delegation-to-a-Connection).
