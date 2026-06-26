---
title: "Use Lightweight Directory Access Protocol (LDAP)"
id: 43701162285837
section: "Manage Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701162285837-Use-Lightweight-Directory-Access-Protocol-LDAP
updated_at: 2026-05-29T14:10:30Z
---

# Use Lightweight Directory Access Protocol (LDAP)

# Use Lightweight Directory Access Protocol (LDAP)

Lightweight Directory Access Protocol (LDAP) is an application protocol used over an IP network to manage and access directory information contained in an organization’s secured network. Composer has been tested and can be used with Active Directory and OpenLDAP directory services. The Composer server can be configured to use one of these LDAP services to authenticate users. When LDAP is enabled, users can log into Composer using their familiar LDAP identity and credentials.

**Note:** 
LDAP configuration management tasks can be performed by a system [admin](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701036219149-Supplied-Users-and-User-Groups#The2) or a member of the Supervisors group.

**Note:** 
User attributes set in regular Composer user definitions via the UI or in LDAP user definitions are encrypted when stored in metadata. To specify the encryption mode, see [Change the Encryption Mode](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701175423245-Change-the-Encryption-Mode).

Connecting Composer to an LDAP directory requires coordination between the authorized LDAP administrator and the Composer administrator.
After enabling LDAP authentication in Composer, you can import users in the LDAP directory of your organization. All user information will be maintained in LDAP, not in your Composer user accounts.

The following LDAP configuration information is needed to configure LDAP in Composer:

| Screen Box | Description |
| --- | --- |
| URL | The LDAP connection string for connecting to the LDAP repository. Connection string is of the following format:  ldap://<ldap-server>:<ldap-port>   * Replace `<ldap-server>` with the DNS name or IP address of the LDAP repository server * Replace `<ldap-port>` with the port number where the LDAP service is listening on `<ldap-server>` (typically port 389) |
| Bind user | User name credential of the service account that (at minimum) has read access to the LDAP repository. |
| Bind password | Password credential for the Bind user (LDAP service account). |
| Search base | Identifies the Distinguished Name (DN) - the location in the LDAP directory tree where to begin queries for registered users in the LDAP directory. |
| Query | LDAP query that will resolve a specific set of users group found in the search base to be imported into Composer. |
| User ID attribute | Identifier attribute for users in LDAP implementation of your organization. The following user ID attributes are supported: **UID**, **CN**, **sAMAccountname**, and **userPrincipalName**. This attribute will determine how user names will be represented in Composer. |

## Configure LDAP

**Configure LDAP**

1. Log in as a system [admin](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701036219149-Supplied-Users-and-User-Groups#The2) or a member of the Supervisors group.

   **Note:** 
   The default **supervisor** user is no longer installed; add users to the **Supervisors** group instead.
2. Select **Security** from the menu (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243179331725)). The security tabs display.

   ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243201234957)
3. On the Security Services tab, make sure that the [LDAP security service is on](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701209060237-Enable-or-Disable-a-Security-Service). If it is not running, turn it on.
4. Select the **LDAP Settings** tab. The LDAP Settings tab has five sections: **General Settings**, **LDAP Server**, **User Provisioning**, **Mappings**, and **Mappings to Custom User Attributes**.
5. In the **General Settings** section, switch the **Enable LDAP** option on (slide it to the right).
6. Enter the LDAP connection URL (DNS or IP address) where the LDAP directory resides.
7. Enter the Bind User and Bind Password credentials. The authorized LDAP administrator needs to provide these credentials.
8. Specify the Search Base which is the DN or location in the LDAP directory tree where a search for registered users can begin. An example entry is provided in the text field: `OU=people,DC=zoomdata,DC=local`, where:

   * OU means organizational unit
   * DC means domain controller
9. Provide a query string that can run to identify user nodes under the Search Base. An example is provided in the text field: `(objectclass=person`). Keep in mind that you can only import individual users into Composer. As a result, your query should be limited to objects that are designated as a “person” or “user.” Use a search engine to look up 'common LDAP query strings'.
10. Optionally [enable user provisioning](#userprov), configure [mappings](#mappings) and [mappings to custom user attributes](#customattr).
11. Manually import users from the LDAP directory. See [Manually Importing Users from the LDAP Directory](#import).
12. To use the secure LDAP connection, import the certificate to your local  `jre` key store. See [Using the Secure LDAP Connection](#secureconn).

## Enable User Provisioning

Use the **User Provisioning** section to enable user provisioning. User provisioning allows you to verify the identity of users that log into Composer against the LDAP directory and automatically create new users in Composer if the user's credentials have been validated against the LDAP directory.

If disabled, you must manually import the users in order to allow them to log into Composer.
See [Manually Importing Users from the LDAP Directory](#import).

When you have enabled the auto provisioning feature, you can select the default account for the provisioned users to be added.

The **Default Account** list contains all the account names, that are available within your Composer instance. If you want the users to be added to one of them, select the corresponding account.
Otherwise, select the **User Account Mapping** option to configure the mappings with LDAP attributes for your users.

## Configure Mappings

Use the **Mappings** subtab to define mappings that bind the user attributes from LDAP and Composer.

1. Select **Login Name Mapping** attribute from the list that will be used as a user login. There are four User ID Attributes supported: UID, CN, sAMAccountname, and userPrincipalName.
2. Account Mapping - select the account to which the user should be added. Account names are case-sensitive.
3. Active Account Mapping - select the account to which the user will log in for the first time
4. Full Name Mapping
5. Email mapping
6. If you want to import users and the groups which they are assigned to, in the **Group mapping attribute** box, type the name of the corresponding column in LDAP.
7. If you want Composer to automatically create groups for users if they don't exist in your environment yet, turn on **Auto Create Groups** (slide the switch to the right).

   After the credentials are verified, the user groups will be created in Composer and each user will be assigned to the corresponding group.

## Manage Mappings to Custom User Attributes

You can associate custom user attributes with a Composer user on the **Mappings to Custom User Attributes** subtab. Custom user attributes can to store values used for credential pass through. This means that if users have access to a particular data source that has been connected to Composer, their credentials can be saved on this page so that their access privileges are maintained for that source within Composer.

## Manually Import Users from the LDAP Directory

**Manually import users from the LDAP directory to** Composer

1. Log in as a system [admin](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701036219149-Supplied-Users-and-User-Groups#The2) or a member of the Supervisors group.

   **Note:** 
   The default **supervisor** user is no longer installed; add users to the **Supervisors** group instead.
2. Select **System Users** from the menu. The Manage Users work area opens.
3. On the **Users** tab, select **Import Users**. A list of users in the LDAP directory is displayed.
4. To import specific users, select them from the list. To import all users, select **Select All**.
5. Select **Import**.

If needed, you can delete imported users using the Users list in the left pane.

After users have been imported into Composer, they can be assigned groups and permissions. For an overview of how Composer manages users and groups and how to assign groups and permissions,
see [Authorize Composer Access](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701020778765-Authorize-Composer-Access).

**Note:** 
When a user is imported from Active Directory or if user provisioning is enabled and a new Active Directory user is added, the corresponding Composer user definition is automatically added. However, when a user is removed from Active Directory, the corresponding Composer user definition is not automatically removed. Composer authentication does not occur for the removed user, but you will need to manually remove the Composer user definition. See [Delete Users](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701021605645-Delete-Users) .

## Use the Secure LDAP Connection

To use the secure LDAP connection, you need to import the certificate to your local  `jre` key store.

1. Run the following command:

   sudo keytool -import -file <ca\_file\_name>.pem -keystore /opt/zoomdata/jre/lib/security/cacerts
2. Restart Composer after importing the certificate:

   sudo service zoomdata restart

Now when using a secure connection to LDAP, the URL must be as follows:

ldaps://<ldap\_server>:636
