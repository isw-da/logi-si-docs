---
title: "How Composer Validates an Environment's Java Version"
id: 43701135097613
section: "Install, Upgrade, and Remove Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701135097613-How-Composer-Validates-an-Environment-s-Java-Version
updated_at: 2026-05-29T14:08:47Z
---

# How Composer Validates an Environment's Java Version

# How Composer Validates an Environment's Java Version

Composer determines which Java is being used in your environment while the microservices are starting. It evaluates your environment in the following sequence. The first Java executable in this sequence that meets minimum requirements is used and validation stops.

1. The directory in the $JAVA\_HOME environment variable path is evaluated to verify that it points to JRE/JDK and its `$JAVA_HOME/bin/java` path contains a valid Java executable that meets the minimum requirements.
2. The `/etc/environment` file is parsed for its JAVA\_HOME variable identifying the Java installation directory. This Java installation directory is then evaluated for a valid Java executable that meets the minimum requirements.
3. The `<install-path>/jre` folder is evaluated for a valid Java executable that meets the minimum requirements.
4. The directories listed in the $PATH environment variable are evaluated for a valid Java executable that meets the minimum requirements.

If a Java executable that meets the minimum requirements is not found in this process, an exception occurs and Composer is not started. To install a valid version of OpenJDK, see [Manually Install OpenJDK](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701120437773-Manually-Install-OpenJDK).
