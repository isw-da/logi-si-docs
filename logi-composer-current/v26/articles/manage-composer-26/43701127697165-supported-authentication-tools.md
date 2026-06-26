---
title: "Supported Authentication Tools"
id: 43701127697165
section: "Manage Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701127697165-Supported-Authentication-Tools
updated_at: 2026-05-29T14:09:22Z
---

# Supported Authentication Tools

# Supported Authentication Tools

Composer supports several approaches to authenticating users. Your organization must choose the best approach given your existing constraints and objectives.

* Composer provides basic login access to the Composer application. See [Authorize Composer Access](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701020778765-Authorize-Composer-Access).
* X.509 client certificate authentication can be used to provide single sign-on capabilities, although it does not support auto-provisioning of user accounts. See [Configure Client Certificate Authentication](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701193920781-Configure-Client-Certificate-Authentication).
* SAML (Security Assertion Markup Language) can be used to provide single sign-on capabilities. See [Configure Composer to Support SAML](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701162439437-Configure-Composer-to-Support-SAML).
* Kerberos can be used to provide single sign-on capabilities. See [Configure Kerberos Single Sign-On (SSO) Settings](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701208766477-Configure-Kerberos-Single-Sign-On-SSO-Settings).
* Trusted Access can be used to allow for machine-to-machine authorization of Composer resources when embedded in your application. It allows users to log in once to the parent application and yet have their security information propagated to Composer, creating a seamless and secure user experience. See [Trusted Access](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701128164493-Trusted-Access).

  **Note:** insightsoftware recommends using [Trusted Access](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701128164493-Trusted-Access) for all embed-related workflows.
* LDAP (Lightweight Directory Access Protocol) can be used to enable directory-based access to Composer. Composer can connect to an organization’s Active Directory (AD) and OpenLDAP directory services using configured LDAP settings. See [Use Lightweight Directory Access Protocol (LDAP)](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701162285837-Use-Lightweight-Directory-Access-Protocol-LDAP).

Composer system administrators can enable or disable Composer's authentication services as required. The available services are listed on the Security Services tab.

**View and edit security options**

1. Log in as a system [admin](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701036219149-Supplied-Users-and-User-Groups#The2) or a member of the Supervisors group.

   **Note:** 
   The default **supervisor** user is no longer installed; add users to the **Supervisors** group instead.
2. Select **Security** from the UI menu. .

   The Security page appears. It consists of several sections: **Security Services**, **SAML Settings**, **LDAP Settings**, and **Kerberos Settings**. The Security Services tab is selected. Other tabs shown are accessible only when the corresponding service is enabled on the Security Services tab.

Settings for x.509 and Kerberos SSO authentication are handled using the
[`zoomdata.properties`](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701054421133-zoomdata-properties-Properties) file.

Enabling or disabling any of these security services requires a restart of the Composer service. Basically, any time you switch a security feature, the Composer service needs to be restarted before the change takes effect. The following switch status may appear for each of the authentication services:
**Started**, **Stopped**, **Will start or stop on next restart**. See [Enable or Disable a Security Service](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701209060237-Enable-or-Disable-a-Security-Service).

When working with security authentication services, bear in mind that you cannot use them all at the same time. If you switch a particular security service on, others will become disabled. If you want to use a security service that is disabled, you must switch the running services off and then start the service you want.

**Security services compatibility**

| Security Service | Can Be Used With |
| --- | --- |
| x.509 | LDAP, Trusted Access |
| SAML SSO | Trusted Access |
| Kerberos | LDAP, Trusted Access |
| Trusted Access | SAML, LDAP, Kerberos, x.509 |
| LDAP | Kerberos, x.509, Trusted Access |
