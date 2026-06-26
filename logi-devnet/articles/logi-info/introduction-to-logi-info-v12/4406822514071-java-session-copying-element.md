---
title: "Java Session Copying Element"
id: 4406822514071
section: "Introduction to Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822514071-Java-Session-Copying-Element
updated_at: 2022-04-06T06:08:36Z
---

# Java Session Copying Element

# Java Session Copying Element

Java-based Logi applications and non-Logi Java applications may maintain their session
variables in different ways. When these two kinds of applications are integrated, they may need to
"copy" session variables so they can be shared between them. Logi session variables are
accessed via @Session tokens, while standard Java application session variables are accessed via JSP or, in
a Java program, via javax.servlet.http.HttpSession.

The
**Java Session Copying** element, which is ignored in .NET Logi applications, enables session variable copying between the two kinds of Java applications. It has four attributes that let you control which variables are copied, which optimizes performance. The "Include" attributes are processed first, then the "Exclude" attributes. The attributes include:

| Attribute | Description |
| --- | --- |
| Copy From Java Exclude | Specifies a comma-separated list of regular expressions that identify the Java application session variables that *will not* be copied to the Logi Info application session space. Do not use session variable names that contain spaces. |
| Copy From Java Include | Specifies a comma-separated list of regular expressions that identify the Java application session variables that *will* be copied to the Logi Info application session space. Do not use session variable names that contain spaces. |
| Copy To Java Exclude | Specifies a comma-separated list of regular expressions that identify the Logi Info application session variables that *will not* be copied to the Java application session space. Do not use session variable names that contain spaces. |
| Copy From Java Exclude | Specifies a comma-separated list of regular expressions that identify the Logi Info application session variables that *will* be copied to the Java application session space. Do not use session variable names that contain spaces. |

In Logi Info versions prior to v11.0.115, almost all session variables were
automatically copied, which didn't always produce the best performance. However, if you want to restore this behavior, you can copy the following element source code and paste it into your \_Settings definition:

<JavaSessionCopying CopyToJavaInclude="^"
CopyToJavaExclude="DebugFile,-bUsesSort$,-tra$,-xmlDef$,-Xsl$,-rdDef$"
CopyFromJavaInclude="^"   
CopyFromJavaExclude="^rd,^dt" />
