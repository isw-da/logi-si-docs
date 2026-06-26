---
title: "Setting Session Variables"
id: 4419723339799
section: "Manage - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723339799-Setting-Session-Variables
updated_at: 2022-07-17T02:22:47Z
---

# Setting Session Variables

# Setting Session Variables

Setting Session Variables in a Report definition is very easy:

![](https://devnet.logianalytics.com/hc/article_attachments/7522730895127/sessionvars_01_623x110.png)

First, the **Set Session Variables** element is added to the
definition, as shown above. Its optional attributes are also shown and can
be very useful. The **Condition** attribute lets you specify a formula
which has to evaluate to *True* for the Session Variables to be set.
The **Set First Time Only** attribute, if set to *True*, causes
the Session Variables to be set the first time the definition is processed
but does not reset them if the report is reloaded during the current user
session. The default value is *False*.

![](https://devnet.logianalytics.com/hc/article_attachments/7522717210135/sessionvars_02_599x151.png)

Next, a **Session Parameters** child element is added. This element
lets you enter a list of Session Variable names and their values.
As shown above, the values can be numbers, strings, tokens, or even
formulae. A formula can be particularly useful here, especially if you
want to make the Session Variable value dynamic in order to, for example,
increment a counter or a date each time the report is reloaded. This is
one of the few opportunities you have to make a web application variable
behave like a normal programming variable.

## Setting Session Variables in a Process Task

In the next example, we'll examine a similar operation in a Process
definition (only available in Logi Info).

![](https://devnet.logianalytics.com/hc/article_attachments/7522744898327/sessionvars_03_633x113.png)

In a task shown above, a **Procedure.Set Session Vars** element has
been added, with a child **Session Parameters** element.
A Session variable, "PhoneNo", has been created, with a value
that uses a formula to remove any non-numeric characters from a Request
variable passed to the task.

![](https://devnet.logianalytics.com/hc/article_attachments/7522730976919/sessionvars_04_592x170.png)

Later in the task, we can see how the @Session token is used to provide
the "cleaned up" phone number value as a parameter for a SQL
Stored Procedure.
As we've seen, Session Variables can be used in Report and Process
definitions to produce very dynamic, global values.

## Setting Session Variables in Global.asax

In a .NET Logi application, you can also set Session Variables in the
application's
Global.asax
file by adding code like this:

<% Session("webpath") =
Request.ServerVariables("URL") %>

This code takes advantage of ASP.NET objects to assign the URL of the
application to the "webpath" Session variable. In the
application, the value can be accessed using the
@Session.webpath~
token.
