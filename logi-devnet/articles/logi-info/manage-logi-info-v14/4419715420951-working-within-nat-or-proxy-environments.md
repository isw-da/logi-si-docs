---
title: "Working within NAT or Proxy Environments"
id: 4419715420951
section: "Manage - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715420951-Working-within-NAT-or-Proxy-Environments
updated_at: 2022-07-17T02:06:49Z
---

# Working within NAT or Proxy Environments

# Working within NAT or Proxy Environments

If a company has set up a firewall with NAT'd addresses or another form of network proxy that sends all traffic to the Logi application through a single IP address or a range of IP addresses, then client IP address checking in SecureKey needs to be suppressed because individual user locations will not be unique.
This can be achieved by modifying the Parent application's request to the Logi application so that it passes a Client Browser Address value of 0.0.0.0. For example:

http://*myServer*/*myLogiApp*/rdTemplate/rdGetSecureKey.aspx?Username=*bob*&Roles=*Worker,Manager* &ClientBrowserAddress=*0.0.0.0*

When using this approach, security can be further enhanced by limiting requests to those from certain parts of the network by using an IP address mask in the web server's security configuration. For IIS, this is accomplished in the IIS Manager's Directory Security tab; for Tomcat this is accomplished by adjusting some of its XML configuration files.
The ClientBrowserAddress query string value is no longer required.
