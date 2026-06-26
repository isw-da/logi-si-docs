---
title: "What Is This Unsupported Class Error?"
id: 4402955696407
section: "Composer v6 Troubleshooting"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402955696407-What-Is-This-Unsupported-Class-Error
updated_at: 2021-08-07T17:32:14Z
---

# What Is This Unsupported Class Error?

# What Is This Unsupported Class Error?

The `UnsupportedClassVersionError: Main : Unsupported major.minor version 52.0` error typically occurs when the Java version with which the plug-in is compiled differs from the Java version that the Composer server is using. Composer and its related plug-ins are compiled using Java 8 (1.8.0\_131 or later). However, for example, if an older Composer server you have installed is running Java 7, it may not be able to read the Java 8 format class files in the corresponding plug-in (e.g. Phoenix connector, etc.) and will thus error out. If this is the case, upgrading to the latest Java version should resolve the issue.

Use the `java -version` command on Linux to determine the Java version.
