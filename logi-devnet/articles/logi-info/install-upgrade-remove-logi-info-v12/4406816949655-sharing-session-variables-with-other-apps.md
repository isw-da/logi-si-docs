---
title: "Sharing Session Variables with Other Apps"
id: 4406816949655
section: "Install, Upgrade, & Remove - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406816949655-Sharing-Session-Variables-with-Other-Apps
updated_at: 2022-04-06T06:03:02Z
---

# Sharing Session Variables with Other Apps

# Sharing Session Variables with Other Apps

On a web server, Logi applications for Java and regular (non-Logi) Java applications
maintain their session variables in different ways. And, typically, you access Logi application session variables using @Session tokens, while Java application session variables are accessed via JSP or by using the javax.servlet.http.HttpSession object.
This topic describes these attributes.

If a Logi application for Java is to be integrated with a Java application, then how can their session variables be shared? The **Java Session Copying** element, available in the \_Settings definition, provides a selective method for session variable copying between the two applications.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) In order to use this feature, you must not use session variable names that contain *spaces* in your Logi application, and there's a small performance penalty for this process, so it's best to minimize the number of variables copied. It may be necessary to restart your web server if you edit the lists in the attributes described below.

The element has four attributes, consisting of Regular Expressions, which control which session variables are copied. As it can be difficult to write Regular Expressions which both include *and* exclude strings, we've provided two attributes ("include") which are processed first, followed by two other attributes ("exclude") which are processed second, making it easier to accomplish both types of operations.

| Attribute | Description |
| --- | --- |
| Copy From Java Exclude | Specifies, as a comma-separated list of Regular Expressions, the Java application session variables that will *not* be copied to the Logi application session variable space. This attribute is processed *after* Copy From Java Include, removing variables from that list. |
| Copy From Java Include | Specifies, as a comma-separated list of Regular Expressions, the Java application session variables that *will* be copied to the Logi application session variable space. |
| Copy To Java Exclude | Specifies, as a comma-separated list of Regular Expressions, the Logi application session variables that will *not* be copied to the Java application session variable space. This attribute is processed *after* Copy To Java Include, removing variables from that list. |
| Copy To Java Include | Specifies, as a comma-separated list of Regular Expressions, the Logi application session variables that *will* be copied to the Java application session variable space. |

Once copied, session variables are identified, in the Java app, using its session object's attribute ID and, in the Logi app, as the name used with a @ Session token. For example:
Java JSP:session.getAttribute("userEmail")  
Logi app:@Session.userEmail~
  
If circumstances demand it, it's possible to return to an earlier, "copy all" behavior by manually adding the following XML to your \_Settings definition source code, as a child of the <Setting> tag:  
<JavaSessionCopying
CopyToJavaInclude="^" CopyToJavaExclude="DebugFile,-bUsesSort$,-tra$,-xmlDef$,  
 -Xsl$,-rdDef$" CopyFromJavaInclude="^" CopyFromJavaExclude="^rd,^dt" />
