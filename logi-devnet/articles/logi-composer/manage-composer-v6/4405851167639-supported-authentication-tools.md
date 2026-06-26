---
title: "Supported Authentication Tools"
id: 4405851167639
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851167639-Supported-Authentication-Tools
updated_at: 2021-09-21T01:29:30Z
---

# Supported Authentication Tools

# Supported Authentication Tools

Composer supports several approaches to authenticating users. Your organization must choose the best approach given your existing constraints and objectives.

* Composer provides basic login access to the Composer application. See [*Authorize Composer Access*](https://devnet.logianalytics.com/hc/en-us/articles/4405850851607-Authorize-Composer-Access).
* X.509 client certificate authentication can be used to provide single sign-on capabilities, although it does not support auto-provisioning of user accounts. See [*Configure Client Certificate Authentication*](https://devnet.logianalytics.com/hc/en-us/articles/4405851168535-Configure-Client-Certificate-Authentication).
* SAML (Security Assertion Markup Language) can be used to provide single sign-on capabilities. See [*Configure Composer to Support SAML*](https://devnet.logianalytics.com/hc/en-us/articles/4405851175831-Configure-Composer-to-Support-SAML).
* Kerberos can be used to provide single sign-on capabilities. See [*Configure Kerberos Single Sign-On (SSO) Settings*](https://devnet.logianalytics.com/hc/en-us/articles/4405859461271-Configure-Kerberos-Single-Sign-On-SSO-Settings).
* Trusted Access can be used to allow for machine-to-machine authorization of Composer resources when embedded in your application. It allows users to log in once to the parent application and yet have their security information propagated to Logi Composer, creating a seamless and secure user experience. See [*Trusted Access*](https://devnet.logianalytics.com/hc/en-us/articles/4405851181463-Trusted-Access).

  ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg)Logi Analytics recommends using [Trusted Access](https://devnet.logianalytics.com/hc/en-us/articles/4405851181463-Trusted-Access) for all embed-related workflows.
* The OAuth 2.0 protocol as well as the OAuth 2.0 Implicit Flow can be used for authentication and authorization.
  See [*Use OAuth 2.0 to Access Composer*](https://devnet.logianalytics.com/hc/en-us/articles/4405851174807-Use-OAuth-2-0-to-Access-Composer).
* LDAP (Lightweight Directory Access Protocol) can be used to enable directory-based access to Composer. Composer can connect to an organization’s Active Directory (AD) and OpenLDAP directory services using configured LDAP settings. See [*Use Lightweight Directory Access Protocol (LDAP) With Composer*](https://devnet.logianalytics.com/hc/en-us/articles/4405859462551-Use-Lightweight-Directory-Access-Protocol-LDAP-With-Composer).

Composer[supervisors](https://devnet.logianalytics.com/hc/en-us/articles/4405859125911-Supplied-User-Definitions) can enable or disable Composer's authentication services as required. The available services are listed on the Security Services tab:

1. Log into Composer as a supervisor.
2. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743720343/hamburger.png) to access the [supervisor menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859441687-The-Composer-Supervisor-Menu) and then select **Security**.

   The Security page appears. It consists of four tabs: **Security Services**, **SAML Settings**, **LDAP Settings**, and **Kerberos Settings**. The Security Services tab is selected. Note that the SAML Settings, LDAP Settings, and Kerberos Settings tabs are accessible only when the corresponding service is enabled on the Security Services tab.

Settings for x.509, Kerberos SSO, and OAuth authentication are handled using the
[`zoomdata.properties`](https://devnet.logianalytics.com/hc/en-us/articles/4405850907159-zoomdata-properties-Properties) file.

Enabling or disabling any of these security services requires a restart of the Composer service. Basically, any time you switch a security feature, the Composer service needs to be restarted before the change takes effect. The following switch status may appear for each of the authentication services:
**Started**, **Stopped**, **Will start or stop on next restart**. See [*Enable or Disable a Security Service*](https://devnet.logianalytics.com/hc/en-us/articles/4405851177751-Enable-or-Disable-a-Security-Service).

When working with security authentication services, bear in mind that you cannot use them all at the same time. If you switch a particular security service on, others will become disabled. If you want to use a security service that is disabled, you must switch the running services off and then start the service you want. The following table describes the compatibility of the security services.

| Security Service | Can Be Used With |
| --- | --- |
| SAML | OAuth |
| LDAP | Kerberos, x509, OAuth |
| Kerberos | LDAP, OAuth |
| x509 | LDAP, OAuth |
| OAuth | SAML, LDAP, Kerberos, x509 |
