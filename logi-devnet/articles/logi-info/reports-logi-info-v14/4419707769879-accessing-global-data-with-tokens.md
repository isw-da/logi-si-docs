---
title: "Accessing Global Data with Tokens"
id: 4419707769879
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707769879-Accessing-Global-Data-with-Tokens
updated_at: 2022-07-17T01:40:36Z
---

# Accessing Global Data with Tokens

# Accessing Global Data with Tokens

In a Logi application there are two sources of data that can be considered "global" in scope: **Session** variables and **Cookies**. These are values that, once set, are available to *all* report and process definitions in an application. As such, they're an unrestricted method of "passing" information between report and process definitions.

Logi application Session variables and Cookies can be set in both report and process definitions. They can also be set by entities *outside* a Logi application and used in the Logi application. In the case of a Logi application for Java, there are special circumstances for Session variable sharing with external Java applications, see [About Logi Apps and Java](https://devnet.logianalytics.com/hc/en-us/articles/4419715039639-About-Logi-Apps-and-Java-).

Session variable and Cookie values can be read in a Logi app using the @Session and @Cookie tokens. For example, if a process task creates a session variable called UserName, it can be accessed in any report definition with the token @Session.UserName~.

## Cookie Limitations

While we don't recommend that you use cookies to manage large amounts of data, they are very useful, so you should understand their limitations. Modern browsers adhere to the cookie limits described in **RFC 2965**. They will manage:

* At least 300 cookies total
* At least 20 cookies per unique host or domain name
* At least 4,096 per cookie (name and value text)

Popular browsers extend the maximum number of cookies allowed per unique host or domain name as follows:

| Browser | Max Cookies | Max Byte/Cookie |
| --- | --- | --- |
| IE 7\*, 8, 9, 10, 11 | 50 | 4,096 |
| Firefox | 50 | 4,097 |
| Chrome & Safari | no limit | 4,097 |
| Opera 9 | 30 | 4,096 |

\* after system patch. Without patch, limit is 20 cookies. See this [MS Knowledgebase article](http://support.microsoft.com/kb/941495).

Generally, if the you attempt to set a domain cookie that exceeds the number of cookies allowed, the oldest cookie is deleted and the new cookie is accepted.
