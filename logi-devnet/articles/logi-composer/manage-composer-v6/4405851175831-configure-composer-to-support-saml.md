---
title: "Configure Composer to Support SAML"
id: 4405851175831
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851175831-Configure-Composer-to-Support-SAML
updated_at: 2021-09-21T01:29:35Z
---

# Configure Composer to Support SAML

# Configure Composer to Support SAML

This topic walks you through the steps to configure SAML settings in Composer for SAML Just-in-time (JIT) provisioning. When enabled and configured, the SAML directory can be used as a source for importing and autoprovisioning users in Composer.

1. Obtain the XML metadata file from your organization's SAML Identity Provider (IDP).
2. Create a Key File using the [Key Tool Generator](https://docs.oracle.com/javase/6/docs/technotes/tools/solaris/keytool.html) program.
3. Log into Composer as the supervisor and configure the SAML settings in the Security tab.
4. Configure the service provider details in your IDP account that you want accessible by Composer.
5. Upload Identity Provider Metadata and add key files to Composer.
6. Configure the SAML mappings in Composer.

In addition, there are optional configurations you can set up:

* [*Customize the Composer Entity ID*](#entityID)
* [*Configure the Auto-Redirect to the IDP*](#autoredirect)
* [*Use the Network Time Protocol to Synchronize Time*](https://devnet.logianalytics.com/hc/en-us/articles/4405859386519-Use-the-Network-Time-Protocol-to-Synchronize-Time) (avoids potential failure by the identity provider to authenticate SAML users)
* [*Implement Single Sign-On (SSO) via SAML*](https://devnet.logianalytics.com/hc/en-us/articles/4405851176727-Implement-Single-Sign-On-SSO-via-SAML)

## Prerequisites

### Obtain Identity Provider Metadata File

To enable Composer to support your organization's identity provider, first obtain the metadata content from your IDP and upload into Composer. Your Security Administrator responsible for managing IDPs can provide this file. Save this metadata file to your local hard drive for uploading into Composer. Refer to the configuration instructions provided below.

**ACTION:** Obtain the XML metadata file from your organization’s IDP.

### Generate a Key File and Configuring SAML with SSL

The key file helps you manage a keystore of cryptographic keys and trusted certificates. Generate the key file using the
[keytool program](https://docs.oracle.com/javase/6/docs/technotes/tools/solaris/keytool.html)
available from Oracle. After generating a key file, you are able to import your SSL certificate into the keystore.
Private keys that are used to digitally sign SAML messages along with any SSL/TLS certificates need to be imported into this keystore.

After installing the keytool program, take the following steps:

1. Run the following command to generate your key:

   ```
   keytool -genkey -alias <localhost> -keyalg RSA -keystore <mykeystore> .jks -keysize 2048 -validity 7000
   ```

   * Replace `<localhost>` with a unique alias (or name) for your key. This name is used (in the **Key** box) when you set up SAML in Composer.
   * Replace `<mykeystore>` with a unique name for your keystore file. This is the file that is uploaded into Composer.
   * The validity flag sets the expiration for the certificate for this key. This value can be changed accordingly based on how long your key is valid before expiring.
2. At the prompt, create the keystore password (`<yourKeyStorePassword>`) and press **Enter**.
3. For the next prompt, create a key password (`<yourKeyPassword)>`) and press **Enter**.
4. Enter the following command to import your SSL certificate (valid x.509) into the keystore:

   ```
   keytool -import -trustcacerts -alias <yourAliasName> -file <yourcertr.cer> -keystore <mykeystore>.jks
   ```

   * Replace `<yourAliasName>` with a unique name for your certificate.
   * Replace `<yourcertr.cer>` with the name of your SSL certificate.
   * Replace `<mykeystore>` with the keystore filename that you created in Step 1 above.

The key file is saved to your local hard drive. You will upload the key file into Composer in the configuration instructions provided below.

## Step-By-Step Configuration Instructions

Access Composer and take the following steps to configure SAML Settings:

1. Log in as the supervisor.
2. Select **Supervisor** and then **Security**. On the **Security Services** tab, make sure that the SAML SSO service is running. Otherwise, enable it, save your changes, and restart Composer for the changes to take effect. For more information, see
   [*Enable or Disable a Security Service*](https://devnet.logianalytics.com/hc/en-us/articles/4405851177751-Enable-or-Disable-a-Security-Service).
3. Select the **SAML Settings** tab.
4. In the General Settings section enable SAML.
5. Select **Upload Identity Provider Metadata** to upload the identity provider's (IDP) metadata file into Composer.
6. Specify the base URL to your Composer Server that users will be logging into via SSO. It must be in the following format:

   ```
   <scheme:>//<server>:<port>/composer
   ```

   If the base URL is changed after saving these SAML settings, update this value and then reboot Composer before downloading the metadata file.
7. Select **Add Key File** to upload the key file (that you generated from the Keytool program).
8. Enter the following information in the screen boxes:

   * **Key** (alias): the unique alias you created for the Key (for example, we used `localhost`)
   * **Key Pass** (word): your `(yourKeyPassword)`
   * **Key Store Pass** (word): your `(yourKeyStorePassword)`
9. Return to your IDP account and configure the service provider information to allow Composer access to the following attributes:

   * Required attribute in Composer: Username
   * Optional Attributes: Groups, Account, Active account, Email, Full Name

   After you have configured the SAML attributes in your IDP account, you can update the Composer SAML mappings.
10. In the **Default Account** list, select the default account to which new users should be added if no account mapping attribute is specified.
11. In the **Account Mapping** box, specify the SAML attribute that contains the comma separated list of Composer accounts associated with the user to be imported into Composer.
12. In the **Active Account Mapping** box, specify the SAML attribute that contains the name of the default Composer account for the user.
13. In the **Login Name Mapping** box, specify the name of the attribute that contains user logins (as established in your IDP account). This value is required so that users can be imported into and given access to Composer. The imported values will be used as login names for Composer users.
14. In the **Full Name Mapping** box, specify the name of the SAML attribute containing users' full names.
15. In the **Email Mapping** box, specify the name of the SAML attribute containing users' emails.
16. In the **Group Mapping** box, specify the name of the SAML attribute containing the multivalue list of group names identifying user memberships.
17. If you want Composer to automatically create groups for users if they don't exist in your environment yet, turn the **Auto Create Groups** on (slide the switch to the right).

    By default, groups created in Composer via SAML do not have any permissions or access to data sources. The Composer Administrator must manually assign privileges to the group.

    ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) If using ADFS, make sure to add this attribute specified in the
    **Username Mapping** box as a claim rule name in ADFS. Otherwise, this attribute is not sent by the identity provider and causes the SAML login to fail. For more information, refer to Issue #4 in our
    [commonly reported SAML issues](https://devnet.logianalytics.com/hc/en-us/articles/4405851198871-Basic-SAML-Troubleshooting).

    The Group, Email, Account, Active Account, and Full Name Mapping values are optional. Use these values if you are looking to automate the setup of user and group attributes in Composer. For information about the mapping options, see [*Implement Single Sign-On (SSO) via SAML*](https://devnet.logianalytics.com/hc/en-us/articles/4405851176727-Implement-Single-Sign-On-SSO-via-SAML).
18. Select **Save**.
19. After you have set up all the necessary information on the Composer SAML Settings page and saved the configuration, the last step is to have Composer generate the metadata file that is imported into your organization's IDP.

    Download the metadata file by selecting the corresponding button. The metadata file is an XML file that you upload to your IDP. Successfully enabling SSO in Composer results in a change to the login screen.
20. If you've already configured the SAML configuration and have made changes to the keystore, restart the Composer server for these changes to take effect.

You still have the option to log into Composer without using single sign-on. Selecting the
**Show Composer Authentication** option lets you log in using your Composer credentials. The first time that users log into Composer via SAML, Composer automatically creates the user profile in the
**Users and Groups** administrative page. In addition, if the user is a member of one or more groups, the Group(s) are also created (as long as the Group Mapping was provided during setup).

### Mapping to Custom User Attribute

You can store additional attribute mappings that may be available in your IDP's SAML Assertions file (for example, Address, City, State and Zip Code). To add a custom user attribute, select the corresponding button. Specify the custom user attribute and SAML attribute in the corresponding boxes.

* SAML Attribute- the name of the user attribute in the SAML provider
* Custom User Attribute - the name of the attribute Composer displays
* Usage - how the name appears to the user
* Secure - if you want to encrypt specific custom attribute mappings, select this checkbox

If you want to encrypt specific custom attribute mappings, select the
**Secure** checkbox for the required attributes pairs.

## Optional Configurations

See also [*Implement Single Sign-On (SSO) via SAML*](https://devnet.logianalytics.com/hc/en-us/articles/4405851176727-Implement-Single-Sign-On-SSO-via-SAML).

### Configure SAML Behind a Load Balancer

You need to configure the settings to work with Composer using SAML if there is unencrypted communication between the proxy and back-end servers and the load balancer is configured to use SSL.

The default configuration parameters are as follows:

```
saml.lb.enabled=false
saml.lb.scheme=https
saml.lb.serverName=<www.myserver.com>
```

For example, for the following front-end URL `https://<myserver.com>/composer`, configure the settings in the `zoomdata.properties` file as described below:

```
saml.lb.enabled=true
saml.lb.serverName=<myserver>.com
```

### Customize the Composer Entity ID

If your identity provider already contains a service provider using the entity ID 'zoomdata', you can create a unique entity ID for Composer. Also, this is applicable if you have two or more separate Composer instances and your IDP requires unique instance identifiers. To do this, you create an alias in the
`zoomdata.properties` file using:

```
saml.entityId=<aliasName>
```

Make sure that the base URL you specified while configuring SAML settings is the same as was used for generating the metadata file with the corresponding
**entityId**.

For help on accessing and editing the `zoomdata.properties` file, see [*Configuration Property Files*](https://devnet.logianalytics.com/hc/en-us/articles/4405850888599-Configuration-Property-Files).

### Configure the Auto-Redirect to the IDP

SAML can be configured to automatically redirect to the identity provider without prompting you with the Composer login. To configure this, edit the `zoomdata.properties` file and add the following parameter:

```
login.page=/saml/login/**
```

You can still log into Composer using credentials by navigating your browser to
`<your_URL>/composer/login`.

For guidance on accessing and editing the `zoomdata.properties` file, see [*Configuration Property Files*](https://devnet.logianalytics.com/hc/en-us/articles/4405850888599-Configuration-Property-Files).

## Troubleshooting

For basic SAML troubleshooting, see [*Basic SAML Troubleshooting*](https://devnet.logianalytics.com/hc/en-us/articles/4405851198871-Basic-SAML-Troubleshooting). If additional assistance is needed, reach out to our [Technical Support](https://devnet.logianalytics.com/hc/en-us/articles/4405859363351-Contact-Technical-Support) team.
