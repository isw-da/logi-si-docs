---
title: "Add Patched JAR Files to an Apache Phoenix Connector's Classpath"
id: 4402955474455
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402955474455-Add-Patched-JAR-Files-to-an-Apache-Phoenix-Connector-s-Classpath
updated_at: 2021-08-07T17:29:52Z
---

# Add Patched JAR Files to an Apache Phoenix Connector's Classpath

# Add Patched JAR Files to an Apache Phoenix Connector's Classpath

If your Apache Phoenix/HBase servers use patched `.jar` files, you might need to add the patched `.jar` files to the Apache Connector's classpath. If you do not, Apache Phoenix may produce an error indicating that you have outdated `.jar` files.

To add the patched `.jar` files to the Apache Phoenix connector's classpath:

1. Add the patched `.jar` files to a directory that is accessible to the connector. For example:

   ```
   /usr/local/share/java/zoomdata/phoenix
   ```
2. Add or modify the following property in the `/etc/zoomdata/edc-phoenix-4.7.properties` file to specify the path to your `.jar` files as a comma-separated list in `datasource.driver-config.jar-path` property. Be sure to put the path to your `.jar` files first so you do not corrupt entries already present in this property. For example:

   ```
   datasource.driver-config.jar-path=/usr/local/share/java/zoomdata/phoenix,lib/edc-phoenix-4.7/phoenix-core-4.7.0-HBase-1.1.jar
   ```
