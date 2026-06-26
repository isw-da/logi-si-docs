---
title: "Authentication - Who is the User?"
id: 4406817634071
section: "Manage - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817634071-Authentication-Who-is-the-User
updated_at: 2022-04-06T06:07:20Z
---

# Authentication - Who is the User?

# Authentication - Who is the User?

*Authentication* is the process of identifying the current user,
usually the "login" or "logon" process that typically
associates a user record with a password. For Logi applications, this can
be accomplished by relying on operating system security features, by
building a custom Logi-based authentication system, or by letting a parent
application handle it. These three authentication methods are discussed in
this topic.

Once a user is authenticated, a Logi application has access to an internal
username that uniquely identifies the current user and drives the
authorization process discussed later.

## Operating System Authentication

This type of authentication is more commonly used in intranet/extranet
environments where web server or domain administrators can easily maintain
the list of valid users.

When using Windows OS-based authentication, the IIS web server manages
access to a Logi application. IIS determines the user's identity and that
identity gets passed into the Logi application.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575614871/intrologisec_01.png)

IIS has a number of authentication options, configurable in the IIS
Manager tool (part of which is shown above). Microsoft provides more
detailed instructions for using IIS security, but generally you disable
**Anonymous** **Authentication** and enable**Windows Authentication**, which validates the user with an account established either on the web
server or elsewhere in the network domain. When necessary, the browser
displays a login dialog box.

When using Java-based web servers on non-Windows operating systems, the
availability of authentication via the web server can be similar but will
vary by OS and web server.

## Custom Authentication Systems

Custom authentication systems generally provide their own user database
that can be queried to authenticate users. Logi Security provides a
default login page (rdLogon.aspx
for .NET,
rdLogon.jsp
for Java) that can be used with custom authentication systems. If
authentication succeeds, custom systems must pass at least a username into
the Logi application.

Custom authentication may work best when operating system-based accounts
cannot be easily managed, such as when using a 3rd-party web hosting
provider.

## Parent Application Authentication

Non-Logi applications that call a Logi report or embed Logi components may
do initial user authentication and establish a "single sign-on"
relationship with the Logi resources using
Logi SecureKey
authentication. This technology allows the "parent" application
to identify authenticated users to the Logi application/components by
passing a security token. This is very useful for developers who want to
extend their own applications by integrating Logi analytics and
visualization technology into them.

Once we know *who* the user is, we need to know what he's allowed to
do.
For more information on Logi SecureKey, see [SecureKey Coding Examples](https://devnet.logianalytics.com/hc/en-us/articles/4406822502167-SecureKey-Coding-Examples).
