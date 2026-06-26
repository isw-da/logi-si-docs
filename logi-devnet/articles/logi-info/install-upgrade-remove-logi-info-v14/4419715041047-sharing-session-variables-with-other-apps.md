---
title: "Sharing Session Variables with Other Apps"
id: 4419715041047
section: "Install, Upgrade, & Remove - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715041047-Sharing-Session-Variables-with-Other-Apps
updated_at: 2022-07-17T02:02:45Z
---

# Sharing Session Variables with Other Apps

# Sharing Session Variables with Other Apps

On a web server, Logi applications for Java and regular (non-Logi) Java applications
maintain their session variables in different ways. And, typically, you access Logi application session variables using @Session tokens, while Java application session variables are accessed via JSP or by using the javax.servlet.http.HttpSession object.
This topic describes these attributes.

If a Logi application for Java is to be integrated with a Java application, then how can their session variables be shared? The **Java Session Copying** element, available in the \_Settings definition, provides a selective method for session variable copying between the two applications.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599319/criticalicon.png) In order to use this feature, you must not use session variable names that contain *spaces* in your Logi application, and there's a small performance penalty for this process, so it's best to minimize the number of variables copied. It may be necessary to restart your web server if you edit the lists in the attributes described below.

The element has four attributes, consisting of Regular Expressions, which control which session variables are copied. As it can be difficult to write Regular Expressions which both include *and* exclude strings, we've provided two attributes ("include") which are processed first, followed by two other attributes ("exclude") which are processed second, making it easier to accomplish both types of operations.

| Attribute | Description |
| --- | --- |
| Copy From Java Exclude | Specifies, as a comma-separated list of Regular Expressions, the Java application session variables that will *not* be copied to the Logi application session variable space. This attribute is processed *after* Copy From Java Include, removing variables from that list. |
| Copy From Java Include | Specifies, as a comma-separated list of Regular Expressions, the Java application session variables that *will* be copied to the Logi application session variable space. |
| Copy To Java Exclude | Specifies, as a comma-separated list of Regular Expressions, the Logi application session variables that will *not* be copied to the Java application session variable space. This attribute is processed *after* Copy To Java Include, removing variables from that list. |
| Copy To Java Include | Specifies, as a comma-separated list of Regular Expressions, the Logi application session variables that *will* be copied to the Java application session variable space. |
