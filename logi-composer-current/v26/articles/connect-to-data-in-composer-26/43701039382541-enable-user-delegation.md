---
title: "Enable User Delegation"
id: 43701039382541
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701039382541-Enable-User-Delegation
updated_at: 2026-05-29T14:11:30Z
---

# Enable User Delegation

# Enable User Delegation

You can use user delegation to run queries on behalf of users using a single set of credentials for a number of connectors. This allows you to share a single connection configuration among all users. User delegation can be established on a per-user or a per-group basis.

User delegation is currently supported by the following connectors: Apache Drill, Cloudera Impala, Cloudera Search, and Hive. The Oracle connector supports user delegation only via user credential pass-through.

**Note:** The Composer supervisor group members enables user delegation via a custom user attribute.Composer administrators [enable](#) and [apply user delegation](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701039356557-Apply-User-Delegation-to-a-Connection) to the data connection definition for a data source.

**Enable user delegation**

1. Log in as a system [admin](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701036219149-Supplied-Users-and-User-Groups#The2) or a member of the Supervisors group.

   **Note:** 
   The default **supervisor** user is no longer installed; add users to the **Supervisors** group instead.
2. Select **Security** from the menu. The security tabs display.

   ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242735287437)
3. Select the **LDAP Settings** tab. The LDAP Settings tab has five sections: **General Settings**, **LDAP Server**, **User Provisioning**, **Mappings**, and **Mappings to Custom User Attributes**.

   **Note:** 
   If the LDAP tab cannot be selected, verify that the LDAP security service is enabled. See [Use Lightweight Directory Access Protocol (LDAP)](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701162285837-Use-Lightweight-Directory-Access-Protocol-LDAP).
4. In the **Mapping to Custom User Attributes** section, select **Add Custom User Attribute**.
5. Type any meaningful name for the custom attribute name.
6. Match the new attribute to any LDAP attribute (for example, cn, sAMAccountName, name). This should be provided by an Impala administrator. The only requirement is that this attribute match the configuration in Sentry.
7. Select **Save** to save the attribute.

   The custom user attribute is referenced by its name, prefaced by the word `User`. For example, if your custom user attribute is named `XXXUserName`, you would reference it as `User.XXXUserName`. This reference name is shown in the **Usage** column.
8. Select **Connectors** on the supervisor menu. The Manage Connector Services page appears. This page has two tables: one for Connector Servers and one for Connectors.
9. Scroll down to the Connectors table and select the appropriate connector from the list. The connector settings page displays.

   ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242752436365)
10. Scroll down to the Connector Parameters and verify that the checkbox in the **User Attribute** column for the **DO\_AS\_USER** parameter is selected. This ensures that the **DO\_AS\_USER** parameter is visible and can be set in your Impala connection.
11. Select **Save**.

To apply user delegation to a data source connection definition, see [Apply User Delegation to a Connection](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701039356557-Apply-User-Delegation-to-a-Connection).
