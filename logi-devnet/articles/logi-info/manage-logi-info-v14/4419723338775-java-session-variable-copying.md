---
title: "Java Session Variable Copying"
id: 4419723338775
section: "Manage - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723338775-Java-Session-Variable-Copying
updated_at: 2022-07-17T02:05:18Z
---

# Java Session Variable Copying

# Java Session Variable Copying

Java-based Logi applications and non-Logi Java applications may maintain
their Session Variables in different ways. When these two kinds of
applications are integrated, they may need to "copy" Session
Variables so they can be shared between them. Logi Session Variables are
accessed via @Session tokens, while standard Java application Session
Variables are accessed via JSP or, in a Java program, via
javax.servlet.http.HttpSession.

The **Java Session Copying** element, which is ignored in .NET Logi
applications, can be added to the \_Settings definition to enable Session
Variable copying between the two kinds of Java applications. It has four
attributes that let you control which variables are copied, which
optimizes performance. The "Include" attributes are processed
first, then the "Exclude" attributes. The attributes include:

| Attribute | Description |
| --- | --- |
| Copy From Java Exclude | Specifies a comma-separated list of regular expressions that identify the Java application session variables that *will not* be copied to the Logi Info application session space. Do not use session variable names that contain spaces. |
| Copy From Java Include | Specifies a comma-separated list of regular expressions that identify the Java application session variables that *will* be copied to the Logi Info application session space. Do not use session variable names that contain spaces. |
| Copy To Java Exclude | Specifies a comma-separated list of regular expressions that identify the Logi Info application session variables that *will not* be copied to the Java application session space. Do not use session variable names that contain spaces. |
| Copy From Java Include | Specifies a comma-separated list of regular expressions that identify the Logi Info application session variables that *will* be copied to the Java application session space. Do not use session variable names that contain spaces. |

It is possible to have almost all session variables copied automatically,
but that typically doesn't produce the best performance. However, if you
want to use this behavior, create element source code like the example
below and paste it into your \_Settings definition XML code:

<JavaSessionCopying CopyToJavaInclude="myVar1, myVar2"
CopyFromJavaInclude="myVar3, myVar4" />
