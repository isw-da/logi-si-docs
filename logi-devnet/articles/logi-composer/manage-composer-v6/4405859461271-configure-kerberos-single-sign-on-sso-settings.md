---
title: "Configure Kerberos Single Sign-On (SSO) Settings"
id: 4405859461271
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859461271-Configure-Kerberos-Single-Sign-On-SSO-Settings
updated_at: 2022-06-23T20:08:05Z
---

# Configure Kerberos Single Sign-On (SSO) Settings

# Configure Kerberos Single Sign-On (SSO) Settings

Kerberos is an enterprise authentication protocol that uses the concept of tickets and three-way authentication to enable users and computers to identify themselves and secure access to resources.

Composer supports Kerberos as a Single Sign On (SSO) mechanism. Using Kerberos SSO, users can seamlessly log into Composer and administrators can completely externalize and centrally manage users or group memberships using their existing Kerberos infrastructure. You can learn more about Kerberos [here](https://en.wikipedia.org/wiki/Kerberos_(protocol)).

## How It Works

When using Kerberos with Composer, the workflow is as follows:

1. A user logs in to his company domain (for example, logging into his windows workstation) and is authenticated with Kerberos. In the case of Windows environments, this is likely Active Directory.
2. In a browser window, a user visits the Composer application and Composer then leverages the user's Kerberos identity to automatically log them into Composer. If this is a users first visit to Composer, then Composer will auto-provision them as a new user in the Composer environment.
3. Kerberos authentication is often paired with LDAP to look up a user's authorization or group membership. Composer will look up the user's group membership. For more information, see the topic on [*Use Lightweight Directory Access Protocol (LDAP) With Composer*](https://devnet.logianalytics.com/hc/en-us/articles/4405859462551-Use-Lightweight-Directory-Access-Protocol-LDAP-With-Composer) .

![](https://devnet.logianalytics.com/hc/article_attachments/4406743753495/kerberos_450x212.png)

## Prerequisites

Before you start configuring settings for Composer to use Kerberos, you must:

* Create a Kerberos Principal. For more information on how to create a Kerberos Principal, refer to [Kerberos documentation](http://web.mit.edu/KERBEROS/krb5-1.5/krb5-1.5.4/doc/krb5-user/What-is-a-Kerberos-Principal_003f.html).
* Create the keytab file on the instance where KDC runs and upload it to Composer Server.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) If you have Kerberos enabled, you must use a static context path for the Composer login URL. Multiple or dynamic context paths are not supported at this time.

### How to Generate the Keytab File

To generate the `.keytab` file for existing AD users, run the following command on AD server:

```
ktpass     
-out <file_name>.keytab     
-princ <HTTP/zoomdata_host> @<realm>     
-mapUser <user_name>	  
–pass <user_password>	  
-crypto RC4-HMAC     
-pType KRB5_NT_PRINCIPAL
```

To generate the `.keytab` file for existing MIT LDAP user, run the following command on LDAP server side:

```
$kadmin     
kadmin: xst -e "rc4-hmac" -k <file_name>.keytab <HTTP/zoomdata_host> @<realm>
```

## Configure General Settings

To configure the Kerberos settings for Composer Server, complete the following steps:

1. Enable the Kerberos SSO service on the [Security Services](#) tab. Keep in mind, that if you have SAML or x509 authentication enabled, you will have to disable them first to use Kerberos.
2. Restart the Composer server by running the following command:

   ```
   sudo service zoomdata restart
   ```
3. Log in as a supervisor and select **Security**. Navigate to the **Kerberos Settings** tab.
4. Slide the **Enable Kerberos** switch on (to the right).
5. Specify the **Kerberos Service Principal**.
6. Select **Upload Kerberos Keytab File** and upload the `.keytab` file, that you have generated before.
7. Select the **Include Kerberos realm/domain name in auto provisioned Composer username** if you want to have the user name in the following format: `username@realm`.
8. Save your settings.

## Configure the Settings on the Client Side

Perform the steps listed below on the client instance that will connect to kerberized Composer.

1. Install the Kerberos command line tools:

   ```
   sudo yum install krb5-workstation     
   sudo yum install krb5-libs
   ```
2. Navigate to the `krb5.conf` file and specify the host on which Composer server runs:

   ```
   [libdefaults]     
   default_realm = ZOOMDATA.LOCAL     
   [realms]     
   ZOOMDATA.LOCAL = {     
   kdc = <composer_host>.local     
   admin_server = <composer_host>.local     
   }     
   [logging]    
   default = FILE:/var/log/krb5.log
   kdc = FILE:/var/log/krb5.log
   [domain_realm]    
   .zoomdata.local = ZOOMDATA.LOCAL   
   zoomdata.local = ZOOMDATA.LOCAL
   ```
3. List all the Kerberos tickets available on the current instance:

   ```
   klist
   ```
4. Remove all the Kerberos tickets (if there are any):

   ```
   kdestroy -A
   ```
5. Obtain a Kerberos ticket for a user (the realm is not required if there is a default one specified in krb5.conf):

   ```
   kinit user@ZOOMDATA.LOCAL
   ```
6. Configure your browser to support Kerberos SSO to Composer.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) To authenticate a user with a Kerberos ticket in Composer, you must either enable LDAP autoprovisioning or create a user with the same name in Composer.
