---
title: "Configure User Delegation for the Apache Solr Connector"
id: 34932719394061
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932719394061-Configure-User-Delegation-for-the-Apache-Solr-Connector
updated_at: 2026-05-26T22:06:28Z
---

# Configure User Delegation for the Apache Solr Connector

# Configure User Delegation for the Apache Solr Connector

User delegation is supported by Composer Apache Solr connectors.

## Prerequisites

A Solr Cloud cluster, version 6.4 or later, with Kerberos authentication must be available.

## Configuration Steps

User delegation configuration for Solr is performed in two steps:

1. Enable Kerberos delegation tokens.

   To enable Kerberos delegation tokens, set the Solr configuration parameter `solr.kerberos.delegation.token.enabled` to `true` (see [Using Delegation Tokens in the Kerberos Authentication Plugin](https://lucene.apache.org/solr/guide/8_1/kerberos-authentication-plugin.html) documentation) in the `solr.in.sh` file on each Solr node.
2. Configure proxy users and delegates.

   Configuration of proxy users and delegates is performed using these parameters in the `solr.in.sh` file on each Solr node:

   * solr.kerberos.impersonator.user.<USER>.users
   * solr.kerberos.impersonator.user.<USER>.groups
   * solr.kerberos.impersonator.user.<USER>.hosts.

   Consider the following example:

   solr.kerberos.impersonator.user.proxy\_user.groups=finance,marketing  
   solr.kerberos.impersonator.user.proxy\_user.hosts=\*

   In this configuration, user `proxy_user` can impersonate users belonging to groups `finance` or `marketing` when connecting to a Solr instance from any host.

   all these parameters should be stored in file `solr.in.sh` on each Solr node.
