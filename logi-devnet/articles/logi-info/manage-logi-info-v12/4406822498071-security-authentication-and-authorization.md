---
title: "Security, Authentication, and Authorization"
id: 4406822498071
section: "Manage - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822498071-Security-Authentication-and-Authorization
updated_at: 2023-03-16T05:05:39Z
---

# Security, Authentication, and Authorization

# Security, Authentication, and Authorization

Logi Info provides a flexible mechanism, "Logi Security", for
implementing and enforcing security in Logi applications. It's capable of
authenticating users, enforcing roles, enabling different security
privileges for different users, and controlling web page component
visibility. It can also control data access, down to the row-, column-,
and cell levels. Logi Security is described in detail in
[Logi Security](https://devnet.logianalytics.com/hc/en-us/articles/4406822422295-Logi-Security).

Logi Info applications track every user's authentication status for each
web request made. The best practice is to employ the
**Security** element in the \_Settings definition; it provides proper
authentication and support for highly granular authorization to access
reports, functionality, and data. The Security element is described in [Working with Logi Security](https://devnet.logianalytics.com/hc/en-us/articles/4406818124567-Working-with-Logi-Security).

Logi **SecureKey** authentication technology provides integration for
applications requiring secure access to a Logi application or embedded
Logi components. It enables a "single sign-on" environment while
enhancing security: user authorization is established and requests are
made to Logi applications or embedded components using a special security
key. SecureKey is discussed in
[Logi SecureKey Authentication](https://devnet.logianalytics.com/hc/en-us/articles/4406822454807-Logi-SecureKey-Authentication).

Logi Security works with a variety of security scenarios. Specific
examples of application and web server configurations for seven different
scenarios is available in
[Logi Security Scenarios](https://devnet.logianalytics.com/hc/en-us/articles/4406817836055-Logi-Security-Scenarios-).
