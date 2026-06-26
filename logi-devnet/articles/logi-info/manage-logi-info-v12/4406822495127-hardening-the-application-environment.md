---
title: "Hardening the Application Environment"
id: 4406822495127
section: "Manage - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822495127-Hardening-the-Application-Environment
updated_at: 2022-04-06T06:08:26Z
---

# Hardening the Application Environment

# Hardening the Application Environment

Many web application servers are attacked every day. The best defense
against such attacks is to ensure that server hardening is a
well-established practice within your organization. All devices and
software that are involved in deploying and supporting a web application,
such as servers, firewalls, databases and others, must be securely
configured.
Some common server hardening tips & tricks include:

* Avoid using insecure protocols that send your information or passwords
  in plain text.
* Minimize unnecessary software on your servers.
* Keep your operating system up to date, especially security patches.
* Do not use default accounts and passwords.
* User Accounts should have very strong passwords.
* Change passwords on a regular basis and do not reuse them.
* Lock accounts after too many login failures. Often these login failures
  are illegitimate attempts to gain access to your system.
* Do not permit empty passwords.
* Unnecessary services should be disabled, especially remote-access unless
  carefully configured to control client access.
* Minimize open network ports to be only what is needed for your specific
  circumstances.
* Configure the system firewall. Proper setup of a firewall itself can
  prevent many attacks.
* Maintain server logs; mirror logs to a separate log server
* Limit user accounts to accessing only what they need. Increased access
  should only be on an as-needed basis.
* Maintain proper backups.
* Don't forget about physical server security.

Please refer to information about securing your specific web server and
OS, which can generally be found online.
