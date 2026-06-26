---
title: "SecureKey Coding Examples"
id: 4406822502167
section: "Manage - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822502167-SecureKey-Coding-Examples
updated_at: 2022-04-06T06:08:28Z
---

# SecureKey Coding Examples

# SecureKey Coding Examples

This topic helps developers who are writing applications that will call a Logi application using Logi SecureKey Authentication.

Language examples include:

* [C# (.NET)](https://devnet.logianalytics.com/hc/en-us/articles/4406817822999-C-Net-#CSharp)
* [Visual Basic (.NET)](https://devnet.logianalytics.com/hc/en-us/articles/4406817829015-Visual-Basic-NET-#VB)
* [Java](https://devnet.logianalytics.com/hc/en-us/articles/4406817824023-Java#Java)
* [Node](https://devnet.logianalytics.com/hc/en-us/articles/4406822499863-Node#Node)
* [Perl](https://devnet.logianalytics.com/hc/en-us/articles/4406817825431-Perl#Perl)
* [PHP](https://devnet.logianalytics.com/hc/en-us/articles/4406817826455-PHP#PHP)
* [Python](https://devnet.logianalytics.com/hc/en-us/articles/4406822501271-Python#Python)
* [Ruby](https://devnet.logianalytics.com/hc/en-us/articles/4406817827863-Ruby#Ruby)

## About Logi SecureKey Authentication

Logi **SecureKey Authentication** is a technology we offer for use in "single sign-on" scenarios, where a non-Logi application (the "Parent" application), which conducts the initial user authentication, is integrated with a Logi application. SecureKey Authentication provides a method of securely accessing the integrated Logi app, and is discussed in detail in [Logi SecureKey Authentication](https://devnet.logianalytics.com/hc/en-us/articles/4406822454807-Logi-SecureKey-Authentication).
This topic provides examples of the Parent application code required to establish the flow of secure exchanges with a Logi application using SecureKey.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) The examples, in several languages, are very generic and are only intended to provide the basic, necessary code. They're provided with the assumption that developers who undertake using them and extending their functionality have in-depth skills with the language selected. Other languages can also be used and success with them will, again, depend on the developer's
skills.
The ClientBrowserAddress query string value is no longer required.
