---
title: "Initial Kerberized Impala Troubleshooting Steps"
id: 34933205203853
section: "Composer 25 Troubleshooting"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933205203853-Initial-Kerberized-Impala-Troubleshooting-Steps
updated_at: 2026-05-26T22:08:26Z
---

# Initial Kerberized Impala Troubleshooting Steps

# Initial Kerberized Impala Troubleshooting Steps

After configuring Composer to connect to a kerberized Impala data source per [Connect to a Kerberized CDH Cluster](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932727396493-Connect-to-a-Kerberized-CDH-Cluster), Composer may still fail to connect when the user attempts to create a new Impala data source to this kerberized CDH cluster. In these situations, we recommend you to check the following first before opening a support ticket for further assistance:

* Verify that the time is synchronized between the Kerberos and Composer servers. Kerberos is very sensitive to time differences that exist. If possible, consider configuring a Network Time Protocol (e.g. ntpd) to synchronize the time on your servers.
* Double-check the configuration parameters, JDBC URL, and that the correct user is specified in the
  `zoomdata.jvm` file for Kerberos. For example, an unintended space when copying parameters can cause the connection to fail.
* Check if you are using AES-256 encryption level in your Active Directory. By default, Java
  *does not* support AES-256 encryption. In case your environment is using AES-256 encryption, make sure to do the following whenever you install Composer on a new server or you are upgrading Composer to a new major version:

  1. Navigate to the [Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files 8 download page](https://www.oracle.com/java/technologies/javase-jce8-downloads.html "Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files 8 download page").
  2. Download the archive `jce_policy-8.zip`.
  3. Extract the `jce/local_policy.jar` and `jce/US_export_policy.jar` files from the archive to the appropriate directory. Overwrite the files already present in the directory.

     + Linux: `/opt/zoomdata/jre/lib/security/`
     + Windows: `<install-path>/jre/lib/security/`
  4. Restart Composer.
