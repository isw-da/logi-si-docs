---
title: "How Composer Validates an Environment's Java Version"
id: 4405859375767
section: "Install, Upgrade, and Remove Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859375767-How-Composer-Validates-an-Environment-s-Java-Version
updated_at: 2021-09-21T01:28:52Z
---

# How Composer Validates an Environment's Java Version

# How Composer Validates an Environment's Java Version

As of version 5.8, Composer requires Java 11.0.5. All supported Zoomdata versions and earlier versions of Composer 5 use Java 8.

Composer determines which Java is being used in your environment while the Composer microservices are starting. It evaluates your environment in the following sequence. The first Java executable in this sequence that meets Composer's minimum requirements is used and validation stops.

1. The directory in the $JAVA\_HOME environment variable path is evaluated to verify that it points to JRE/JDK and its `$JAVA_HOME/bin/java` path contains a valid Java executable that meets the minimum requirements.
2. The `/etc/environment` file is parsed for its JAVA\_HOME variable identifying the Java installation directory. This Java installation directory is then evaluated for a valid Java executable that meets the minimum requirements.
3. The `<composer-install-path>/jre` folder is evaluated for a valid Java executable that meets the minimum requirements.
4. The directories listed in the $PATH environment variable are evaluated for a valid Java executable that meets the minimum requirements.

If a Java executable that meets the minimum requirements is not found in this process, an exception occurs and Composer is not started. To install a valid version of OpenJDK, see [*Manually Install OpenJDK 11*](https://devnet.logianalytics.com/hc/en-us/articles/4405851089815-Manually-Install-OpenJDK-11).
