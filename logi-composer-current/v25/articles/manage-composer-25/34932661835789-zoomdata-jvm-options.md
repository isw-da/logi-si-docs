---
title: "zoomdata.jvm Options"
id: 34932661835789
section: "Manage Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932661835789-zoomdata-jvm-Options
updated_at: 2026-05-26T22:06:17Z
---

# zoomdata.jvm Options

# zoomdata.jvm Options

The `zoomdata.jvm` file contains JVM options (e.g. memory configuration) and Java system properties (e.g. timezone, temp directory, etc.) related to Composer. The table below describes the options you can adjust.

Situations where the `zoomdata.jvm` file needs to be edited include:

* [Configure Memory Settings](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932637063437-Configure-Memory-Settings)
* [Connect to a Kerberized CDH Cluster](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932727396493-Connect-to-a-Kerberized-CDH-Cluster)

For information on editing configuration files, see [Edit a Configuration File](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932669980557-Edit-a-Configuration-File).

| Option | Default Value | Description |
| --- | --- | --- |
| DEBUG\_ENABLED | 0/false | Toggle switch to enable or disable the Java debug capability. To enable, enter '1' or 'true'.  Example: `DEBUG_ENABLED=false` |
| DEBUG\_PORT | 9393 | The default port for the Java debug capability.  Example: `DEBUG_PORT=9393` |
| JAVA\_OPTS | -Xss256k -Xms2048m -Xmx8192m | Java-related options for JVM. Refer to Oracle's article on [Java HotSpot VM Options](https://www.oracle.com/java/technologies/javase/vmoptions-jsp.html) for information. |
| KERBEROS\_CONFIG | /etc/krb5.conf | Default location for the Kerberos configuration details. However, the path to the file may be different in your environment.  Refer to Oracle's article on [File Formats](https://docs.oracle.com/cd/E36784_01/html/E36882/krb5.conf-4.html) for information. |
| KERBEROS\_PRINCIPAL | hdfs@HADOOP.COM | Kerberos principal name. |
| KERBEROS\_KEYTAB | /etc/zoomdata/zoomdata.keytab | Kerberos keytab location. |
| PROXY\_HOST | user-defined | For cloud-based connectors (including Google Analytics and Salesforce) being used in a proxy configuration, this property specifies the server host to be returned for calls, and identifies the proxy host server that will provide internet access. |
| PROXY\_PORT | user-defined | For cloud-based connectors (including Google Analytics and Salesforce) being used in a proxy configuration, this property specifies the server port to be returned for calls, and identifies the proxy port server that will provide internet access. |
