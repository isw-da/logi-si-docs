---
title: "SecureKey Coding Examples"
id: 4419707807383
section: "Manage - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707807383-SecureKey-Coding-Examples
updated_at: 2022-07-17T02:06:25Z
---

# SecureKey Coding Examples

# SecureKey Coding Examples

This topic helps developers who are writing applications that will call a Logi application using Logi SecureKey Authentication.

Language examples include:

* [C# (.NET)](https://devnet.logianalytics.com/hc/en-us/articles/4419723137687-C-Net-#CSharp)
* [Visual Basic (.NET)](https://devnet.logianalytics.com/hc/en-us/articles/4419723140375-Visual-Basic-NET-#VB)
* [Java](https://devnet.logianalytics.com/hc/en-us/articles/4419715455383-Java#Java)
* [Node](https://devnet.logianalytics.com/hc/en-us/articles/4419723138839-Node#Node)
* [Perl](https://devnet.logianalytics.com/hc/en-us/articles/4419707803543-Perl#Perl)
* [PHP](https://devnet.logianalytics.com/hc/en-us/articles/4419707804439-PHP#PHP)
* [Python](https://devnet.logianalytics.com/hc/en-us/articles/4419707805463-Python#Python)
* [Ruby](https://devnet.logianalytics.com/hc/en-us/articles/4419707806359-Ruby#Ruby)

## About Logi SecureKey Authentication

Logi **SecureKey Authentication** is a technology we offer for use in "single sign-on" scenarios, where a non-Logi application (the "Parent" application), which conducts the initial user authentication, is integrated with a Logi application. SecureKey Authentication provides a method of securely accessing the integrated Logi app, and is discussed in detail in [Logi SecureKey Authentication](https://devnet.logianalytics.com/hc/en-us/articles/4419723086999-Logi-SecureKey-Authentication).
This topic provides examples of the Parent application code required to establish the flow of secure exchanges with a Logi application using SecureKey.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) The examples, in several languages, are very generic and are only intended to provide the basic, necessary code. They're provided with the assumption that developers who undertake using them and extending their functionality have in-depth skills with the language selected. Other languages can also be used and success with them will, again, depend on the developer's
skills.
The ClientBrowserAddress query string value is no longer required.
