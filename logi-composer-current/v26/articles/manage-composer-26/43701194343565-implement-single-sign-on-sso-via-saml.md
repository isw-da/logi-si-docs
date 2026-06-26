---
title: "Implement Single Sign-On (SSO) via SAML"
id: 43701194343565
section: "Manage Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701194343565-Implement-Single-Sign-On-SSO-via-SAML
updated_at: 2026-05-29T14:09:24Z
---

# Implement Single Sign-On (SSO) via SAML

# Implement Single Sign-On (SSO) via SAML

Composer  supports single sign-on (SSO) using the Security Assertion Markup Language (SAML), a secure, XML-based communication standard for authenticating identities between organizations. SAML eliminates the need for a user to create and maintain multiple authentication credentials (that is, passwords) for different websites. Instead, by leveraging SAML, a user authenticates one time using a secure site (known as the 'Identity Provider' or 'IDP') that then authorizes access to different applications and services that is linked to the user.

Key points to implementing SAML SSO in an organization’s operating environment:

* Service Providers must subscribe to an IDP service (or implement one internally) and complete a set up process. Since there are many IDPs options, service providers may subscribe to more than one service for the convenience of their users.
* Users need to complete a registration process to be added to your organization’s secured directory including the selection of authentication methods offered by your organization.
* New applications and programs (such as Composer) must be integrated into your organization’s existing security protocols.
* Authentication approval from the IDP is limited to a single use and there is a time limit for access.

## Prepare to Integrate Composer  into Your SAML-Enabled Network

If your organization already has SAML SSO integrated into the operating environment, Composer can be added to your list of secured applications and programs. Composer supports the SAML 2.0 security protocol. Composer provides the following security functionality using SAML: (1) user authentication, (2) group mappings, and (3) account level synchronization of users and groups in Composer. Your organization’s Security Administrator or IT Manager responsible for network security may need to be involved if the Composer Administrator does not have account access to your IDP.

**Note:** Composer can only support one IDP account. If your organization uses multiple IDP accounts, select one that will connect with Composer.

Prior to set up, Composer recommends checking to ensure that Network Time Protocol service is used to synchronize your network with accurate time servers. NTP helps to avoid potential failure by the identity provider to authenticate SAML users.

For more information, see [Using the Network Time Protocol](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701073403021-Use-the-Network-Time-Protocol-to-Synchronize-Time).

Composer’s SAML Settings provide mappings for the Group, Email, Account, Active account, and Full Name attributes that allow the Composer Administrator to import these settings directly into Composer’s Users and Groups administrative function.

Composer also supports an SSL connection to SAML. In order to setup using secured SAML, a keystore needs to be generated and saved in the Composer SAML configuration page. The SSL Certificate needs to be uploaded into the keystore file so that Composer can validate the SSL connection. See [Configure Composer to Support SAML](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701162439437-Configure-Composer-to-Support-SAML)
for the setup instructions.

The organization’s IDP account needs to be imported into Composer as a Service Provider. This entails importing the IDP’s metadata file when configuring SAML in Composer. After completing all configuration steps, you need to generate Composer’s metadata file so that it can be added to your IDP’s account. Again, if your organization has a dedicated security administrator, contact them to assist in this setup procedure.

**Note:** Composer supplies two default users you can use to log into Composer: admin and supervisor. You must log in as the supervisor to access the SAML configuration page. See [Supplied Users and User Groups](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701036219149-Supplied-Users-and-User-Groups).

Keep in mind the following SAML requirements that Composer supports:

* IDP account should support SAML 2.0: Your organization’s IDP needs to support SAML 2.0 in order to successfully add Composer.
* Default Account section: users can be auto-provisioned to a specific account.
* Importing users and groups from the IDP into Composer: there are two scenarios to consider for importing users and groups:

  + If the user or group profile does not already exist in Composer, they are created the first time that a user logs into Composer. In this case, the profile contains no access privileges and the Composer Administrator needs to set up these profiles.
  + If the user or group profile already exist in Composer, the names must be
    ***an exact match*** in order for the IDP profile information to populate the corresponding Composer accounts. For example, if the username “johndoe” is stored in the IDP, the exact same username should be in Composer.

After you have successfully configured and enabled SAML, users and groups imported in this manner can be managed from Composer’s Users and Groups function. For guidance to import and setup these accounts, see
[Manage Users](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701051820941-Manage-Users).

See [Configure Composer to Support SAML](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701162439437-Configure-Composer-to-Support-SAML) for instructions to setup SAML in Composer.
