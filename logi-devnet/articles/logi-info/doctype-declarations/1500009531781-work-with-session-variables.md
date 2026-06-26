---
title: "Work with Session Variables"
id: 1500009531781
section: "Doctype Declarations"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009531781-Work-with-Session-Variables
updated_at: 2021-06-17T01:58:37Z
---

# Work with Session Variables

# Work with Session Variables

Session variables are values that are global in scope and persistent for the life of a user session. They're very useful in Logi applications for retaining and passing data. This topic discusses the elements and techniques associated with Session variables in a Logi application.

* About Session Variables
* [Set Session Variables](#Setting)
* [Use @Session Tokens](#Tokens)
* [Java Session Variable Copying](#Java)
* [View Session Variables in Debugger](#Debugger)

## About Session Variables

Session variables provide a useful way to store values that can be used anywhere in a Logi application and provide the best approximation of a real programming *variable* you'll find in stateless web applications.

Logi application Session variables can be set in both Report
and Process definitions using the **Set Session Variables** and **Procedure.Set Session Vars** elements, respectively. They can also be set by other, non-Logi applications and used in an integrated Logi application (see the Java Session Copying section for special considerations that apply to Java applications).

Session variables, of course, only exist as long as the user session lasts. The Session Timeout element, introduced in v11.4.046, can be used to manage the user session lifetime. For more information, see [Manage Session Timeout](https://devnet.logianalytics.com/hc/en-us/articles/1500009515942-Manage-Session-Timeout).

When using Logi SecureKey authentication, the **Security** element in \_Settings includes a **Restart Session** attribute that can be set to clear out all Session variables right before an attempted login. This
ensures that Session variables established during a previous user's session
are not re-used for the next user's session. For more information, see [Use Logi SecureKey Authentication](https://devnet.logianalytics.com/hc/en-us/articles/1500009515922-Use-Logi-SecureKey-Authentication).

### Restrictions

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif)  Session variables are of the *variant* data type, meaning they can be anything - strings, numbers, arrays, etc. - of any size, and that opens the door to potential abuse. It's possible to put huge amounts of data into Session variables but it's poor practice to do so, because that will negatively affect server performance. Our recommendation is that you use Session variables for *small
amounts of
data only*.

The **Repeat Elements** element is one of the very first things processed when a
page goes through the Logi Engine. Some values, including @Session tokens set with the two Set Session elements mentioned earlier,
aren't processed until *later* so @Session tokens should *not* be used with Repeat Elements.

## Set Session Variables

Setting Session variables in a Report definition is very easy:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778515095/sessionvars_01.png)

First, the **Set Session Variables** element is added to the definition, as shown above. Its optional attributes are also shown and can be very useful. The **Condition** attribute lets you specify a formula which has to evaluate to *True* for the Session variables to be set.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771449623/notev11.4.png)The **Set First Time Only** attribute, if set to *True*, causes the Session variables to be set the first time the definition is processed but does not reset them if the report is reloaded during the current user session. The default value is *False*.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778515351/sessionvars_02.png)

Next, a **Session Parameters** child element is added. This element lets you enter a list of Session variable names and their values.

As shown above, the values can be numbers, strings, tokens, or even formulae. A formula can be particularly useful here, especially if you want to make the Session variable value dynamic in order to, for example, increment a counter or a date each time the report is reloaded. This is one of the few opportunities you have to make a web application variable behave
like a normal
programming variable.

### Set Session Variables in a Process Task

In the next example, we'll examine a similar operation in a Process definition (only available in Logi Info).

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778515735/sessionvars_03.png)

In a task shown above, a **Procedure.Set Session Vars** element has been added, with a child **Session Parameters** element.

A Session variable, "PhoneNo", has been created, with a value that uses a formula to remove any non-numeric characters from a Request variable passed to the task.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771616279/sessionvars_04.png)

Later in the task, we can see how the @Session token is used to provide the "cleaned up" phone number value as a parameter for a SQL Stored Procedure.

As we've seen, Session variables can be used in Report and Process definitions to produce very dynamic, global values.

### Set Session Variables in Global.asax

In a .NET Logi application, you can also set Session variables in the application's Global.asax file by adding code like this:

<% Session("webpath") = Request.ServerVariables("URL") %>

This code takes advantage of ASP.NET objects to assign the URL of the application to the "webpath" Session variable. In the application, the value can be accessed using the @Session.webpath~ token.

## Use @Session Tokens

We've already seen some examples of Session variables in use. @Session tokens can be employed in a lot of places in your definitions. Here are some more usage examples:

### Navigation Persistence

Because Session variables are persistent across pages, they can be particularly useful in preserving values just before a Process task call. For example, suppose you have a task for user login that users can call from any page in your application. After the login task completes, you want to return the user to the page he was viewing. Here's one technique for doing this in a parameterized manner:

1. At the top of each report definition, use elements to create a Session variable ("Caller") with a value of @Request.rdReport~. This is the definition name of the report.
2. Each report definition, of course, has a link to the Login task.
3. At the end of the Login task, use Response.Report and Target.Report elements. In the Target.Report element's Report Definition File attribute, enter the @Session.Caller~ token. This ensures the user will go back to the page he was viewing before calling the task.

### Dynamic Connections

@Session tokens can be used in the attributes of **Connection** elements, allowing you to create dynamic connections. Typically, this is done by using a **Startup Process** element in \_Settings to run a Process task.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771616535/sessionvars_07.png)

As shown above, the task uses **Procedure.If** and **Procedure.Set Session Vars** elements to set appropriate Session variables based on variable criteria.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771616791/sessionvars_08.png)

When the task completes, the Connection elements in \_Settings will be processed, using @Session tokens, as shown above.

### Dynamic JavaScript Code

Like all tokens, @Session tokens can be used in JavaScript code to make it dynamic:

|  |  |
| --- | --- |
|  | if ( '@Session.UserID~' == '' ) alert('Your session has expired.');     if ( '@Session.UserID~' != '' ) SubmitForm('rdProcess.aspx?rdProcess=        someTaskID&UserID=@Session.UserID~','\_self','true','',null); |

The code above embeds @Session tokens to determine if a user ID is present and calls a Process task if it is.

## Java Session Variable Copying

Java-based Logi applications and non-Logi Java applications may maintain their Session
variables in different ways. When these two kinds of applications are integrated, they may need to
"copy" Session variables so they can be shared between them. Logi Session variables are
accessed via @Session tokens, while standard Java application Session variables are accessed via JSP or, in
a Java program, via javax.servlet.http.HttpSession.

The
**Java Session Copying** element, which is ignored in .NET Logi
applications, can be added to the \_Settings definition to enable Session variable copying between the two kinds of
Java applications. It has four attributes that let you control which
variables are copied, which optimizes performance. The "Include"
attributes are processed first, then the "Exclude" attributes. The
attributes include:

| Attribute | Description |
| --- | --- |
| Copy From Java Exclude | Specifies a comma-separated list of regular expressions that identify the Java application session variables that *will not* be copied to the Logi Info application session space. Do not use session variable names that contain spaces. |
| Copy From Java Include | Specifies a comma-separated list of regular expressions that identify the Java application session variables that *will* be copied to the Logi Info application session space. Do not use session variable names that contain spaces. |
| Copy To Java Exclude | Specifies a comma-separated list of regular expressions that identify the Logi Info application session variables that *will not* be copied to the Java application session space. Do not use session variable names that contain spaces. |
| Copy From Java Include | Specifies a comma-separated list of regular expressions that identify the Logi Info application session variables that *will* be copied to the Java application session space. Do not use session variable names that contain spaces. |

In Logi Info versions prior to v11.0.115, almost all session variables
were
automatically copied, which didn't always produce the best performance.
However, if you want to restore this behavior, you can copy the
following element source code and paste it into your \_Settings
definition:

<JavaSessionCopying CopyToJavaInclude="^"
CopyToJavaExclude="DebugFile,-bUsesSort$,-tra$,-xmlDef$,-Xsl$,-rdDef$"
CopyFromJavaInclude="^"   
CopyFromJavaExclude="^rd,^dt" />

## View Session Variables in the Debugger

The Logi **Debugger Trace Page** is very useful for identifying
problems and includes helpful information, such as the values of all
Request variables. However, it doesn't usually display Session
variables. However, for .NET applications, you can enable a *full trace page* that will show you the Session variables and much more.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771617047/sessionvars_05.png)

To turn on full tracing:

1. Locate your Logi application's **rdPage.aspx** file in the application folder, as shown above.
2. Use a text editor, such as Notepad, to edit the file to include **Trace="True"**, as shown above.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771617303/sessionvars_06.png)

The full trace page, similar to the one shown above, will now appear at the bottom of every report page and you can see the Session State section, highlighted, showing all the Session variables. You'll see quite a few that start with "rd" - these are created by the Logi Engine.
