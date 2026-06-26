---
title: "Application Configuration and Settings"
id: 4406817451671
section: "Introduction to Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817451671-Application-Configuration-and-Settings
updated_at: 2022-04-06T06:06:10Z
---

# Application Configuration and Settings

# Application Configuration and Settings

This topic provides answers to frequently-asked questions about application configuration and settings:

1. [In Studio, the Application page shows a "Warning: Version
   Mismatch" message. What does this mean?](#VerMismatch)
2. [How do I turn on debugging?](#Debugging)
3. [How can I use switch between VBScript and JavaScript?](#ScriptLang)
4. [Is there some way to assign a style sheet to an entire Logi
   application?](#GlobalCSS)
5. [I'd like to create a mailto: link in several reports. Is there a way
   to define the email address as a constant?](#Constants)
6. [What happens when you "register this application" using the
   Studio wizard?](#RegisterIIS)
7. [How can I browse my report from within Studio? Whenever I try to do
   it, the Default report is displayed.](#DefaultRpt)
8. [I noticed the Team Development element in \_Settings. What does that
   do?](#TeamDev)
9. [Is it possible to use Logi report definitions that are stored in a
   database table?](#ExtDef)
10. [When I ran my report I received an "Access denied" error
    message.](#FilePerm)
11. [Can I configure my Logi application's document type declaration
    (doctype)?](#doctype)

## 1. In Studio, the Application page shows a "Warning: Version Mismatch" message. What does this mean?

This warning means that the application
was created with a version of the Logi product that is older than the
version of Studio currently installed on your computer. As a result, some
application features available in the newer product may not be available.
To upgrade your application to a different Logi product version, click the
Change Version... link on Studio's Application page, or use the Server
Manager utility, available on the Studio Tools menu. For more information, see [Logi Product Upgrades](https://devnet.logianalytics.com/hc/en-us/articles/4406817922839-Logi-Product-Upgrades).

## 2. How do I turn on debugging?

You can turn on debugging in Logi Studio for all your report definitions
by clicking the **Debug** icon on the menu or toolbar and selecting
*DebuggerLinks* from the selection list. Clicking the icon sets an
attribute value in the \_Settings definition, General element, and you can
also turn debugging on by setting that value directly.

## 3. How can I switch between JavaScript and VBScript?

Support for VBScript has been deprecated - it continues to be supported
but JavaScript is the recommended scripting language. JavaScript is the
default scripting language. The choice of scripting language is set in the
\_Settings definition, using the **General** element's
**Scripting Language** attribute. When creating a Logi app for Java,
JavaScript is the only scripting language choice.

## 4. Is there some way to assign a style sheet to an entire Logi application?

Yes. If you prefer to do that, rather than assign style sheets in each
individual report definition, you can do so in the \_Settings definition.
Just add a **Global Style** element and assign the style sheet file to
it, and it will then apply to every report definition.

## 5. I'd like to create a mailto: link in several reports. Is there a way to define the email address as a constant?

Yes. Constants can be defined in the \_Settings definition and referred to
from report definitions. This allows the value of the constant, in your
case the email address, to change, if necessary, without requiring a
change in every report definition. Constants are referred to using the
@Constant token.

## 6. What happens when you "register this application" using the Studio wizard?

When using IIS as your web server, the registration wizard creates an IIS
Virtual Directory for your web application. You must be logged-in with an
account that has administrator privileges in order for the wizard to
create and configure IIS virtual directories. You can also do this
manually, if you prefer, using the IIS Management tool provided with
Windows.

## 7. How can I browse my report from within Studio? Whenever I try to do it, the Default report is displayed.

In the \_Settings definition, the **Application** element has an
attribute that selects which report is considered the "default"
report and is displayed when you select Browse from Studio's toolbar. You
can quickly change this selection by selecting and right-clicking a report
definition in Studio's Application panel, then selecting "Set As
Default" from the pop-up menu that appears. You can also browse any
individual report definition by selecting and right-clicking it and
selecting "Run in Browser".

## 8. I noticed the Team Development element in \_Settings. What does that do?

Team Development is a simple source code control system. It was designed
to be used in an environment where there are multiple developers working
on the same application and it's useful to control access to definitions
and support files. When Team Development is enabled, application files are
locked and developers must check them in and out to work on them. This
prevents overlapping editing of the same file and creates an audit trail
of who worked on which files. File History can also be enabled so that
revisions can be rolled-back and undone. More information is available in
[Using Logi 12 Studio](https://devnet.logianalytics.com/hc/en-us/articles/4406822594327-Using-Logi-12-Studio).

## 9. Is it possible to use Logi report definitions that are stored in a database table?

Yes. Logi report definitions are XML files and these can be stored in a
table column. The **External Definitions** element can be used in the
\_Settings definition with a datalayer element to retrieve the stored
report definitions and make them available to the application

## 10. When I ran my report I received an "Access denied" error message.

In order to allow the account used by the web server to run Logi
applications to write temporary cache files to the server's hard drive,
you must give it permissions to do so. This is described in detail in
[File Access Permissions](https://devnet.logianalytics.com/hc/en-us/articles/4406817456407-File-Access-Permissions).

## 11. Can I configure my Logi application's document type declaration (doctype)?

Yes, the \_Settings definition's **General** element includes a
**Doctype Declaration** attribute, that can be set to *Html5*,
*Xhtml Strict*, *Xhtml Transitional*, *Xhtml Frameset*, or
*None*. If left blank, the default is *Html5*.
