> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Supported Authentication Tools

Self-Service Analytics supports several approaches to authenticating users. Your organization must choose the best approach given your existing constraints and objectives.

* Self-Service Analytics provides basic login access to the Self-Service Analytics application. See [Authorize Self-Service Analytics Access for Users in Groups](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov).

* X.509 client certificate authentication can be used to provide single sign-on capabilities, although it does not support auto-provisioning of user accounts. See [Configure Client Certificate Authentication](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/kerberos-sso#configure-client-certificate-authentication).

* SAML (Security Assertion Markup Language) can be used to provide single sign-on capabilities. See [Configure Self-Service Analytics to Support SAML](#configure-self-service-analytics-to-support-saml).

* Kerberos can be used to provide single sign-on capabilities. See [Configure Kerberos Single Sign-On (SSO) Settings](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/kerberos-sso).

* Trusted Access can be used to allow for machine-to-machine authorization of Self-Service Analytics resources when embedded in your application. It allows users to log in once to the parent application and yet have their security information propagated to Self-Service Analytics, creating a seamless and secure user experience. See [Trusted Access](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/trusted-access-ov).

  <Note>
    insightsoftware recommends using [Trusted Access](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/trusted-access-ov) for all embed-related workflows.
  </Note>

* LDAP (Lightweight Directory Access Protocol) can be used to enable directory-based access to Self-Service Analytics. Self-Service Analytics can connect to an organization’s Active Directory (AD) and OpenLDAP directory services using configured LDAP settings. See [Use Lightweight Directory Access Protocol (LDAP)](#use-lightweight-directory-access-protocol-ldap).

Self-Service Analytics system administrators can enable or disable Self-Service Analytics's authentication services as required. The available services are listed on the Security Services tab.

**View and edit security options**

1. Log in as a system [admin](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#admin-user) or a member of the Supervisors group.

   <Note>
     The default **supervisor** user is no longer installed; add users to the **Supervisors** group instead.
   </Note>

2. Select **Tools > Security** from the Administration menu.

   The Security page appears. It consists of several sections: **Security Services**, **SAML Settings**, **LDAP Settings**, and **Kerberos Settings**. The Security Services tab is selected. Other tabs shown are accessible only when the corresponding service is enabled on the Security Services tab.

Settings for x.509 and Kerberos SSO authentication are handled using the [`zoomdata.properties`](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/properties-reference) file.

Enabling or disabling any of these security services requires a restart of the Self-Service Analytics service. Basically, any time you switch a security feature, the Self-Service Analytics service needs to be restarted before the change takes effect. The following switch status may appear for each of the authentication services: **Started**, **Stopped**, **Will start or stop on next restart**. See [Enable or Disable a Security Service](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/changing-encryption-mode#enable-or-disable-a-security-service).

When working with security authentication services, bear in mind that you cannot use them all at the same time. If you switch a particular security service on, others will become disabled. If you want to use a security service that is disabled, you must switch the running services off and then start the service you want.

**Security services compatibility**

| Security Service | Can Be Used With |
| - | - |
| x.509 | LDAP, Trusted Access |
| SAML SSO | Trusted Access |
| Kerberos | LDAP, Trusted Access |
| Trusted Access | SAML, LDAP, Kerberos, x.509 |
| LDAP | Kerberos, x.509, Trusted Access |

<h2 id="use-lightweight-directory-access-protocol-ldap">
  Use Lightweight Directory Access Protocol (LDAP)
</h2>

Lightweight Directory Access Protocol (LDAP) is an application protocol used over an IP network to manage and access directory information contained in an organization’s secured network. Self-Service Analytics has been tested and can be used with Active Directory and OpenLDAP directory services. The Self-Service Analytics server can be configured to use one of these LDAP services to authenticate users. When LDAP is enabled, users can log into Self-Service Analytics using their familiar LDAP identity and credentials.

<Note>
  LDAP configuration management tasks can be performed by a system [admin](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#admin-user) or a member of the Supervisors group.
</Note>

<Note>
  User attributes set in regular Self-Service Analytics user definitions via the UI or in LDAP user definitions are encrypted when stored in metadata. To specify the encryption mode, see [Encryption](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/changing-encryption-mode).
</Note>

Connecting Self-Service Analytics to an LDAP directory requires coordination between the authorized LDAP administrator and the Self-Service Analytics administrator. After enabling LDAP authentication in Self-Service Analytics, you can import users in the LDAP directory of your organization. All user information will be maintained in LDAP, not in your Self-Service Analytics user accounts.

The following LDAP configuration information is needed to configure LDAP in Self-Service Analytics:

<table>
  <thead>
    <tr>
      <th scope="col">Screen Box</th>
      <th scope="col">Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>URL</td>

      <td>
        The LDAP connection string for connecting to the LDAP repository. Connection string is of the following format:

        <br />

        ```
        ldap://<ldap-server>:<ldap-port>
        ```

        <br />

        * Replace `<ldap-server>` with the DNS name or IP address of the LDAP repository server
        * Replace `<ldap-port>` with the port number where the LDAP service is listening on `<ldap-server>` (typically port 389)
      </td>
    </tr>

    <tr>
      <td>Bind user</td>
      <td>User name credential of the service account that (at minimum) has read access to the LDAP repository.</td>
    </tr>

    <tr>
      <td>Bind password</td>
      <td>Password credential for the Bind user (LDAP service account).</td>
    </tr>

    <tr>
      <td>Search base</td>
      <td>Identifies the Distinguished Name (DN) - the location in the LDAP directory tree where to begin queries for registered users in the LDAP directory.</td>
    </tr>

    <tr>
      <td>Query</td>
      <td>LDAP query that will resolve a specific set of users group found in the search base to be imported into Self-Service Analytics.</td>
    </tr>

    <tr>
      <td>User ID attribute</td>
      <td>Identifier attribute for users in LDAP implementation of your organization. The following user ID attributes are supported: **UID**, **CN**, **sAMAccountname**, and **userPrincipalName**. This attribute will determine how user names will be represented in Self-Service Analytics.</td>
    </tr>
  </tbody>
</table>

<Note>
  In this release, when your admin enables the Enhanced Experience user interface, you will see changes to workflows you may have used in previous releases. If you are running an earlier release or your admin has not enabled the new interface, see [Use Lightweight Directory Access Protocol (LDAP)](#use-lightweight-directory-access-protocol-ldap).
</Note>

### Configure LDAP

**Configure LDAP**

1. Log in as a system [admin](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#admin-user) or a member of the Supervisors group.

2. Select **Tools > Security** from the Administration menu. The security work area opens.

   <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/configuration/security-26-2.jpg?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=82a8cdde20b900379f3f8427dcd680a0" alt="configure your authentication settings here" width="1308" height="691" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/configuration/security-26-2.jpg" />

3. On the Security Services tab, make sure that the [LDAP security service is on](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/changing-encryption-mode). If it is not running, turn it on.

4. Select the **LDAP Settings** tab. The LDAP Settings tab has five sections: **General Settings**, **LDAP Server**, **User Provisioning**, **Mappings**, and **Mappings to Custom User Attributes**.

5. In the **General Settings** section, switch the **Enable LDAP** option on (slide it to the right).

6. Enter the LDAP connection URL (DNS or IP address) where the LDAP directory resides.

7. Enter the Bind User and Bind Password credentials. The authorized LDAP administrator needs to provide these credentials.

8. Specify the Search Base which is the DN or location in the LDAP directory tree where a search for registered users can begin. An example entry is provided in the text field: `OU=people,DC=zoomdata,DC=local`, where:

   * OU means organizational unit
   * DC means domain controller

9. Provide a query string that can run to identify user nodes under the Search Base. An example is provided in the text field: `(objectclass=person`). Keep in mind that you can only import individual users into Self-Service Analytics. As a result, your query should be limited to objects that are designated as a “person” or “user.” Use a search engine to look up 'common LDAP query strings'.

10. Optionally [enable user provisioning](#enable-user-provisioning), configure [mappings](#configure-mappings) and [mappings to custom user attributes](#manage-mappings-to-custom-user-attributes).

11. Manually import users from the LDAP directory. See [Manually Importing Users from the LDAP Directory](#manually-import-users-from-the-ldap-directory).

12. To use the secure LDAP connection, import the certificate to your local `jre` key store. See [Using the Secure LDAP Connection](#use-the-secure-ldap-connection).

<h3 id="enable-user-provisioning">
  Enable User Provisioning
</h3>

Use the **User Provisioning** section to enable user provisioning. User provisioning allows you to verify the identity of users that log into Self-Service Analytics against the LDAP directory and automatically create new users in Self-Service Analytics if the user's credentials have been validated against the LDAP directory.

If disabled, you must manually import the users in order to allow them to log into Self-Service Analytics. See [Manually Importing Users from the LDAP Directory](#manually-import-users-from-the-ldap-directory).

When you have enabled the auto provisioning feature, you can select the default account for the provisioned users to be added.

The **Default Account** list contains all the account names, that are available within your Self-Service Analytics instance. If you want the users to be added to one of them, select the corresponding account. Otherwise, select the **User Account Mapping** option to configure the mappings with LDAP attributes for your users.

<h3 id="configure-mappings">
  Configure Mappings
</h3>

Use the **Mappings** subtab to define mappings that bind the user attributes from LDAP and Self-Service Analytics.

1. Select **Login Name Mapping** attribute from the list that will be used as a user login. There are four User ID Attributes supported: UID, CN, sAMAccountname, and userPrincipalName.

2. Account Mapping - select the account to which the user should be added. Account names are case-sensitive.

3. Active Account Mapping - select the account to which the user will log in for the first time

4. Full Name Mapping

5. Email mapping

6. If you want to import users and the groups which they are assigned to, in the **Group mapping attribute** box, type the name of the corresponding column in LDAP.

7. If you want Self-Service Analytics to automatically create groups for users if they do not exist in your environment yet, turn on **Auto Create Groups** (slide the switch to the right).

   After the credentials are verified, the user groups will be created in Self-Service Analytics and each user will be assigned to the corresponding group.

<h3 id="manage-mappings-to-custom-user-attributes">
  Manage Mappings to Custom User Attributes
</h3>

You can associate custom user attributes with a Self-Service Analytics user on the **Mappings to Custom User Attributes** subtab. Custom user attributes can to store values used for credential pass through. This means that if users have access to a particular data source that has been connected to Self-Service Analytics, their credentials can be saved on this page so that their access privileges are maintained for that source within Self-Service Analytics.

<h3 id="manually-import-users-from-the-ldap-directory">
  Manually Import Users from the LDAP Directory
</h3>

**Manually import users from the LDAP directory to Self-Service Analytics**

1. Log in as a system [admin](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#admin-user) or a member of the Supervisors group.

   <Note>
     The default **supervisor** user is no longer installed; add users to the **Supervisors** group instead.
   </Note>

2. Navigate to the Users work area.

3. Select **Import Users**. A list of users in the LDAP directory is displayed.

4. To import specific users, select them from the list. To import all users, select **Select All**.

5. Select **Import**.

If needed, delete imported users using the **Users** list in the left pane.

After users have been imported into Self-Service Analytics, they can be assigned groups and permissions. For an overview of how Self-Service Analytics manages users and groups and how to assign groups and permissions, see [Authorize Self-Service Analytics Access for Users in Groups](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov).

<Note>
  When a user is imported from Active Directory or if user provisioning is enabled and a new Active Directory user is added, the corresponding Self-Service Analytics user definition is automatically added. However, when a user is removed from Active Directory, the corresponding Self-Service Analytics user definition is not automatically removed. Self-Service Analytics authentication does not occur for the removed user, but you will need to manually remove the Self-Service Analytics user definition. See [Delete Users](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#delete-users) .
</Note>

<h3 id="use-the-secure-ldap-connection">
  Use the Secure LDAP Connection
</h3>

To use the secure LDAP connection, you need to import the certificate to your local `jre` key store.

1. Run the following command:

   ```bash theme={null}
   sudo keytool -import -file <ca_file_name>.pem -keystore /opt/zoomdata/jre/lib/security/cacerts
   ```

2. Restart Self-Service Analytics after importing the certificate:

   ```bash theme={null}
   sudo service zoomdata restart
   ```

Now when using a secure connection to LDAP, the URL must be as follows:

```
ldaps://<ldap_server>:636
```

<h2 id="configure-self-service-analytics-to-support-saml">
  Configure Self-Service Analytics to Support SAML
</h2>

This topic walks you through the steps to configure SAML settings in Self-Service Analytics for SAML Just-in-time (JIT) provisioning. When enabled and configured, the SAML directory can be used as a source for importing and autoprovisioning users in Self-Service Analytics.

1. Obtain the XML metadata file from your organization's SAML Identity Provider (IDP).
2. Create a Key File using the program.
3. Log in as an administrator or member of the Supervisors group and configure the SAML settings in the Security tab.
4. Configure the service provider details in your IDP account that you want accessible by Self-Service Analytics.
5. Upload Identity Provider Metadata and add key files to Self-Service Analytics.
6. Configure the SAML mappings in Self-Service Analytics.

In addition, there are optional configurations you can set up:

* [Customize the Self-Service Analytics Entity ID](#customize-the-self-service-analytics-entity-id)
* [Configure the Auto-Redirect to the IDP](#configure-the-auto-redirect-to-the-idp)
* [Use the Network Time Protocol to Synchronize Time](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-ov#use-the-network-time-protocol-to-synchronize-time) (avoids potential failure by the identity provider to authenticate SAML users)
* [Implement Single Sign-On (SSO) via SAML](#implement-single-sign-on-sso-via-saml)

### Prerequisites

#### Obtain Identity Provider Metadata File

To enable Self-Service Analytics to support your organization's identity provider, first obtain the metadata content from your IDP and upload into Self-Service Analytics. Your Security Administrator responsible for managing IDPs can provide this file. Save this metadata file to your local hard drive for uploading into Self-Service Analytics. Refer to the configuration instructions provided below.

**ACTION:** Obtain the XML metadata file from your organization’s IDP.

<img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/connectors/saml-idp2.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=e8100adc98e4973a4a5b4a83ab85670d" alt="" width="875" height="207" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/connectors/saml-idp2.png" />

#### Generate a Key File and Configuring SAML with SSL

The key file helps you manage a keystore of cryptographic keys and trusted certificates. Generate the key file using the [keytool program](https://docs.oracle.com/javase/6/docs/technotes/tools/solaris/keytool.html) available from Oracle. After generating a key file, you are able to import your SSL certificate into the keystore. Private keys that are used to digitally sign SAML messages along with any SSL/TLS certificates need to be imported into this keystore.

After installing the keytool program, take the following steps:

1. Run the following command to generate your key:

   ```bash theme={null}
   keytool -genkey -alias <localhost> -keyalg RSA -keystore <mykeystore> .jks -keysize 2048 -validity 7000
   ```

   * Replace `<localhost>` with a unique alias (or name) for your key. This name is used (in the **Key** box) when you set up SAML in Self-Service Analytics.
   * Replace `<mykeystore>` with a unique name for your keystore file. This is the file that is uploaded into Self-Service Analytics.
   * The validity flag sets the expiration for the certificate for this key. This value can be changed accordingly based on how long your key is valid before expiring.

2. At the prompt, create the keystore password (`<yourKeyStorePassword>`) and press **Enter**.

3. For the next prompt, create a key password (`<yourKeyPassword)>`) and press **Enter**.

4. Enter the following command to import your SSL certificate (valid x.509) into the keystore:

   ```bash theme={null}
   keytool -import -trustcacerts -alias <yourAliasName> -file <yourcertr.cer> -keystore <mykeystore>.jks
   ```

   * Replace `<yourAliasName>` with a unique name for your certificate.
   * Replace `<yourcertr.cer>` with the name of your SSL certificate.
   * Replace `<mykeystore>` with the keystore filename that you created in Step 1 above.

The key file is saved to your local hard drive. You will upload the key file into Self-Service Analytics in the configuration instructions provided below.

<h3 id="step-by-step-configuration-instructions">
  Step-By-Step Configuration Instructions
</h3>

Access Self-Service Analytics and take the following steps to configure SAML Settings:

1. Log in as an administrator or a member of the Supervisors group.

2. Select **Tools > Security** from the Administration menu. On the **Security Services** tab, make sure that the SAML SSO service is running. Otherwise, enable it, save your changes, and restart Self-Service Analytics for the changes to take effect. For more information, see [Enable or Disable a Security Service](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/changing-encryption-mode#enable-or-disable-a-security-service).

3. Select the **SAML Settings** tab.

4. In the General Settings section enable SAML.

5. Select **Upload Identity Provider Metadata** to upload the identity provider's (IDP) metadata file into Self-Service Analytics.

6. Specify the base URL to your Self-Service Analytics Server that users will be logging into via SSO. It must be in the following format:

   ```xml theme={null}
   <scheme:>//<server>:<port>/composer
   ```

   If the base URL is changed after saving these SAML settings, update this value and then reboot Self-Service Analytics before downloading the metadata file.

7. Select **Add Key File** to upload the key file (that you generated from the Keytool program).

8. Enter the following information in the screen boxes:

   * **Key** (alias): the unique alias you created for the Key (for example, we used `localhost`)
   * **Key Pass** (word): your `(yourKeyPassword)`
   * **Key Store Pass** (word): your `(yourKeyStorePassword)`

9. Return to your IDP account and configure the service provider information to allow Self-Service Analytics access to the following attributes:

   * Required attribute: Username
   * Optional Attributes: Groups, Account, Active account, Email, Full Name

   After you have configured the SAML attributes in your IDP account, you can update the Self-Service Analytics SAML mappings.

10. In the **Default Account** list, select the default account to which new users should be added if no account mapping attribute is specified.

11. In the **Account Mapping** box, specify the SAML attribute that contains the comma separated list of Self-Service Analytics accounts associated with the user to be imported into Self-Service Analytics.

12. In the **Active Account Mapping** box, specify the SAML attribute that contains the name of the default Self-Service Analytics account for the user.

13. In the **Login Name Mapping** box, specify the name of the attribute that contains user logins (as established in your IDP account). This value is required so that users can be imported into and given access to Self-Service Analytics. The imported values will be used as login names for Self-Service Analytics users.

14. In the **Full Name Mapping** box, specify the name of the SAML attribute containing users' full names.

15. In the **Email Mapping** box, specify the name of the SAML attribute containing users' emails.

16. In the **Group Mapping** box, specify the name of the SAML attribute containing the multivalue list of group names identifying user memberships.

17. If you want Self-Service Analytics to automatically create groups for users if they do not exist in your environment yet, turn the **Auto Create Groups** on (slide the switch to the right).

    By default, groups created in Self-Service Analytics via SAML do not have any permissions or access to data sources. The Self-Service Analytics Administrator must manually assign privileges to the group.

    <Note>
      If using ADFS, make sure to add this attribute specified in the **Username Mapping** box as a claim rule name in ADFS. Otherwise, this attribute is not sent by the identity provider and causes the SAML login to fail. For more information, refer to Issue #4 in our [commonly reported SAML issues](#implement-single-sign-on-sso-via-saml).
    </Note>

    The Group, Email, Account, Active Account, and Full Name Mapping values are optional. Use these values if you are looking to automate the setup of user and group attributes in Self-Service Analytics. For information about the mapping options, see [Implement Single Sign-On (SSO) via SAML](#implement-single-sign-on-sso-via-saml).

18. Select **Save**.

19. After you have set up all the necessary information on the Self-Service Analytics SAML Settings page and saved the configuration, the last step is to have Self-Service Analytics generate the metadata file that is imported into your organization's IDP.

    Download the metadata file by selecting the corresponding button. The metadata file is an XML file that you upload to your IDP. Successfully enabling SSO in Self-Service Analytics results in a change to the login screen.

20. If you have already configured the SAML configuration and have made changes to the keystore, restart the Self-Service Analytics server for these changes to take effect.

You still have the option to log into Self-Service Analytics without using single sign-on. Selecting the **Show Self-Service Analytics Authentication** option lets you log in using your Self-Service Analytics credentials. The first time that users log into Self-Service Analytics via SAML, Self-Service Analytics automatically creates the user profile in the **Users** (formerly *Users and Groups*) administrative page. In addition, if the user is a member of one or more groups, the Group(s) are also created (as long as the Group Mapping was provided during setup).

#### Mapping to Custom User Attribute

You can store additional attribute mappings that may be available in your IDP's SAML Assertions file (for example, Address, City, State and Zip Code). To add a custom user attribute, select the corresponding button. Specify the custom user attribute and SAML attribute in the corresponding boxes.

* SAML Attribute- the name of the user attribute in the SAML provider
* Custom User Attribute - the name of the attribute Self-Service Analytics displays
* Usage - how the name appears to the user
* Secure - if you want to encrypt specific custom attribute mappings, select this checkbox

If you want to encrypt specific custom attribute mappings, select the **Secure** checkbox for the required attributes pairs.

### Optional Configurations

See also [Implement Single Sign-On (SSO) via SAML](#implement-single-sign-on-sso-via-saml).

#### Configure SAML Behind a Load Balancer

You need to configure the settings to work with Self-Service Analytics using SAML if there is unencrypted communication between the proxy and back-end servers and the load balancer is configured to use SSL.

The default configuration parameters are as follows:

```properties theme={null}
saml.lb.enabled=false saml.lb.scheme=https saml.lb.serverName=<www.myserver.com>
```

For example, for the following front-end URL `https://<myserver.com>/composer`, configure the settings in the `zoomdata.properties` file as described below:

```properties theme={null}
saml.lb.enabled=true saml.lb.serverName=<myserver>.com
```

<h4 id="customize-the-self-service-analytics-entity-id">
  Customize the Self-Service Analytics Entity ID
</h4>

If your identity provider already contains a service provider using the entity ID 'zoomdata', you can create a unique entity ID for Self-Service Analytics. Also, this is applicable if you have two or more separate Self-Service Analytics instances and your IDP requires unique instance identifiers. To do this, you create an alias in the `zoomdata.properties` file using:

```properties theme={null}
saml.entityId=<aliasName>
```

Make sure that the base URL you specified while configuring SAML settings is the same as was used for generating the metadata file with the corresponding **entityId**.

For help on accessing and editing the `zoomdata.properties` file, see [Configuration Property Files](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#configuration-property-files).

<h4 id="configure-the-auto-redirect-to-the-idp">
  Configure the Auto-Redirect to the IDP
</h4>

SAML can be configured to automatically redirect to the identity provider without prompting you with the Self-Service Analytics login. To configure this, edit the `zoomdata.properties` file and add the following parameter:

```properties theme={null}
login.page=/saml/login/**
```

You can still log into Self-Service Analytics using credentials by navigating your browser to `<your_URL>/composer/login`.

For guidance on accessing and editing the `zoomdata.properties` file, see [Configuration Property Files](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#configuration-property-files).

### Troubleshooting

For basic SAML troubleshooting, see [Implement Single Sign-On (SSO) via SAML](#implement-single-sign-on-sso-via-saml). If additional assistance is needed, reach out to our [Technical Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support) team.

<h2 id="implement-single-sign-on-sso-via-saml">
  Implement Single Sign-On (SSO) via SAML
</h2>

Self-Service Analytics supports single sign-on (SSO) using the Security Assertion Markup Language (SAML), a secure, XML-based communication standard for authenticating identities between organizations. SAML eliminates the need for a user to create and maintain multiple authentication credentials (that is, passwords) for different websites. Instead, by leveraging SAML, a user authenticates one time using a secure site (known as the 'Identity Provider' or 'IDP') that then authorizes access to different applications and services that is linked to the user.

Key points to implementing SAML SSO in an organization’s operating environment:

* Service Providers must subscribe to an IDP service (or implement one internally) and complete a set up process. Since there are many IDPs options, service providers may subscribe to more than one service for the convenience of their users.
* Users need to complete a registration process to be added to your organization’s secured directory including the selection of authentication methods offered by your organization.
* New applications and programs (such as Self-Service Analytics) must be integrated into your organization’s existing security protocols.
* Authentication approval from the IDP is limited to a single use and there is a time limit for access.

<h3 id="prepare-to-integrate-self-service-analytics-into-your-saml">
  Prepare to Integrate Self-Service Analytics into Your SAML-Enabled Network
</h3>

If your organization already has SAML SSO integrated into the operating environment, Self-Service Analytics can be added to your list of secured applications and programs. This software supports the SAML 2.0 security protocol, and provides the following security functionality using SAML: (1) user authentication, (2) group mappings, and (3) account level synchronization of users and groups in Self-Service Analytics. Your organization’s Security Administrator or IT Manager responsible for network security may need to be involved if your Self-Service Analytics Administrator does not have account access to your IDP.

<Note>
  Self-Service Analytics can only support one IDP account. If your organization uses multiple IDP accounts, select one to connect with Self-Service Analytics.
</Note>

Prior to set up, Self-Service Analytics recommends checking to ensure that Network Time Protocol service is used to synchronize your network with accurate time servers. NTP helps to avoid potential failure by the identity provider to authenticate SAML users. See [Use the Network Time Protocol to Synchronize Time](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-ov#use-the-network-time-protocol-to-synchronize-time)

Self-Service Analytics’s SAML Settings provide mappings for the Group, Email, Account, Active account, and Full Name attributes that allow the Self-Service Analytics Administrator to import these settings directly into Self-Service Analytics’s Users and Groups administrative function.

Self-Service Analytics also supports an SSL connection to SAML. In order to setup using secured SAML, a keystore needs to be generated and saved in the Self-Service Analytics SAML configuration page. The SSL Certificate needs to be uploaded into the keystore file so that Self-Service Analytics can validate the SSL connection. See [Configure Self-Service Analytics to Support SAML](#configure-self-service-analytics-to-support-saml) for the setup instructions.

The organization’s IDP account needs to be imported into Self-Service Analytics as a Service Provider. This entails importing the IDP’s metadata file when configuring SAML in Self-Service Analytics. After completing all configuration steps, you need to generate Self-Service Analytics’s metadata file so that it can be added to your IDP’s account. Again, if your organization has a dedicated security administrator, contact them to assist in this setup procedure.

<Note>
  Self-Service Analytics supplies two default users you can use to log into Self-Service Analytics: admin and supervisor. You must log in as the supervisor to access the SAML configuration page. See [Supplied Users and User Groups](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#supplied-users-and-user-groups).
</Note>

Keep in mind the following SAML requirements that Self-Service Analytics supports:

* IDP account should support SAML 2.0: Your organization’s IDP needs to support SAML 2.0 in order to successfully add Self-Service Analytics.

* Default Account section: users can be auto-provisioned to a specific account.

* Importing users and groups from the IDP into Self-Service Analytics: there are two scenarios to consider for importing users and groups:

  * If the user or group profile does not already exist in Self-Service Analytics, they are created the first time that a user logs into Self-Service Analytics. In this case, the profile contains no access privileges and the Self-Service Analytics Administrator needs to set up these profiles.
  * If the user or group profile already exist in Self-Service Analytics, the names must be ***<u> an exact match </u>*** in order for the IDP profile information to populate the corresponding Self-Service Analytics accounts. For example, if the username “johndoe” is stored in the IDP, the exact same username should be in Self-Service Analytics.

After you have successfully configured and enabled SAML, users and groups imported in this manner can be managed from Self-Service Analytics’s Users and Groups functions. For guidance to import and setup these accounts, see [Manage Users](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage).

See [Configure Self-Service Analytics to Support SAML](#configure-self-service-analytics-to-support-saml) for instructions to setup SAML in Self-Service Analytics.

## Basic SAML Troubleshooting

When troubleshooting SAML configuration or login issues, be sure to enable DEBUG mode for the SAML module. DEBUG mode allows for additional logging and more detailed error messages to be captured in the `zoomdata.log` file (located in `/opt/zoomdata/logs` ) that is useful for troubleshooting purposes. To enable DEBUG mode, enter the following cURL command:

```bash theme={null}
curl -u <admin>:<password> -X "POST" "http://<hostname>:<port>/composer/actuator/loggers/org.springframework.security.saml" \
-H "Content-Type: application/json; charset=utf-8" -d $'{ "configuredLevel": "DEBUG" }'
```

Replace the `<admin>` and `<password>` with the credentials for the Self-Service Analytics admin user. Similarly, please make sure that your URL contains the appropriate `<hostname>` (or IP address) and `<port>` of your Self-Service Analytics environment. This should be similar to the hostname (or IP address) and port specified in your browser.

### Commonly Reported Issues

<h4 id="issue-1-warning-message-during-idp-redirection">
  Issue #1: Warning Message During IDP Redirection
</h4>

Summary:

User sees the following warning message during redirection to the IDP (Identity Provider):

```
HTTP Status 401 - Authentication Failed: Response issue time is either too old or with date in the future
```

Root Cause:

This error is likely being thrown as a result of mistiming between the Self-Service Analytics server and IDP server.

Resolution:

Check that the NTP service is running on both machines. if not - start it and check that time is the same.

<h4 id="issue-2-connection-error">
  Issue #2: Connection Error
</h4>

Summary:

User is encountering an error connecting to SAML And notices the following error message in the Self-Service Analytics log files:

```
2015-09-28 07:25:39,138 ERROR [o.s.s.s.u.SAMLUtil] Could not find any artifact resolution services in metadata.
2015-09-28 07:25:39,138 DEBUG [o.s.s.s.w.WebSSOProfileImpl] Could not decode artifact response message.
org.opensaml.ws.message.decoder.MessageDecodingException: Could not find any artifact resolution services in metadata.
```

Root Cause:

There is a missing artifact resolution service in the metadata, which is required by Self-Service Analytics.

Resolution:

Add the following property string to the *zoomdata.properties* file (located in `/etc/zoomdata` directory):

```properties theme={null}
saml.artifactBindingDefault=false
```

Restart Self-Service Analytics after making this change.

<h4 id="issue-3-error-validating-saml-message-on-self-service-analytics">
  Issue #3: Error Validating SAML Message on Self-Service Analytics Home Page
</h4>

Summary:

After following the steps to configure SAML in Self-Service Analytics and successfully connecting to the SAML IDP (e.g. ADFS) login page, the user may still encounter a "Error validating SAML message" error message on the Self-Service Analytics Home page after logging in via SAML.

When looking in the zoomdata.log/zoomdata-error.log files, the user might see the following error messages:

```
2015-09-28 13:19:13,336 ERROR [o.o.x.e.Decrypter] Error decrypting the encrypted data element
org.apache.xml.security.encryption.XMLEncryptionException: Illegal key size
Caused by: java.security.InvalidKeyException: Illegal key size
```

**Root Cause:**

Encryption better than AES-128 which is not allowed by the default cryptographic jurisdiction policy files that are shipped with the Java JDK.

Resolution:

To address this issue, download the appropriate [JCE extension for unlimited strength encryption](https://www.oracle.com/java/technologies/javase-jce8-downloads.html) for your current Java version and install the unlimited strength policy files with the JDK that is shipped with Self-Service Analytics. In order to install this JCE extension, you need to copy the two .jar files contained in the JCE downloaded archive to the */opt/zoomdata/jre/lib/security* directory of your Self-Service Analytics server and replace the existing limited JCE files in this location.

<Warning>
  Make a backup of the original JCE files in case you need to restore these files for some reason. Keep in mind that during upgrade or installation, these files will be overwritten.
</Warning>

Afterward, try following the steps to configure SAML in Self-Service Analytics again and this issue should no longer occur.

<h4 id="issue-4-error-validating-saml-message-continued">
  Issue #4: Error Validating SAML Message (continued)
</h4>

Summary:

User continues to encounter the "Error Validating SAML message" error after entering credentials through their ADFS login page. They also see the following error messages in the zoomdata.log file:

```
2015-09-29 09:05:08,796 INFO [o.s.s.s.l.SAMLDefaultLogger]
AuthNResponse;FAILURE;204.17.231.100org.opensaml.common.SAMLException: NameID element must be present as part
of the Subject in the Response message, please enable it in the IDP configuration

2015-09-29 09:05:08,796 DEBUG [o.s.s.s.SAMLProcessingFilter] Authentication request failed:
org.springframework.security.authentication.AuthenticationServiceException: Error validating SAML message
```

Root Cause:

The attribute, specified in the "Username Mapping" of Self-Service Analytics's SAML settings (under the Security tab logged in as the system admin), is not being sent by ADFS. In this example, the error message indicates that ADFS is not sending the "NameID" attribute.

Resolution:

Configure ADFS to add this attribute by following the below steps (we will continue to use "NameID" attribute in this example):

1. Add NameID as a "Claim rule name".

2. Choose "Active Directory" as the Attribute store.

3. Choose "SAMAccount-Name" as the LDAP attribute and "Name ID" as "Outgoing claim type".

4. Finish the wizard and confirm the claim rules window.

5. Verify that the Self-Service Analytics SAML settings on the **Security** tab when logged in as a member of the Supervisors group, have this attribute (in this example, NameID) specified correctly under the "Username Mapping" parameter.

   <Note>
     In ADFS 3.0, you may need to configure this attribute (e.g. "NameID") as a "Pass Through claim."
   </Note>
