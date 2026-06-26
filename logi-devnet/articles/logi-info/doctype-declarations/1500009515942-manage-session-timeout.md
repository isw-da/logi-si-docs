---
title: "Manage Session Timeout"
id: 1500009515942
section: "Doctype Declarations"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009515942-Manage-Session-Timeout
updated_at: 2023-09-13T11:05:47Z
---

# Manage Session Timeout

# Manage Session Timeout

This topic discusses use of the **Session Timeout** element, which makes it easy to prevent errors caused by session timeouts.

* About the Session Timeout Element
* [Attributes](#Attributes)
* [Use the Element](#Using)

## About the Session Timeout Element

When a user's working with a Logi Info application and leaves the browser session
inactive for some time, the server-side session may expire and end. This can
cause problems with pages that need the session state to be live. The
**Session Timeout** element, introduced in v11.4.046, makes it easy to prevent errors caused by session
timeouts.

There element operates in two modes, depending on the value of its **Session Auto Keep Alive** attribute. When
set to *True*, the session remains alive for as long as the browser is open. This is
accomplished by automatically "pinging" the server from the browser, thus informing the
server that the browser is still open. Once the browser closes, the server-side
session times-out after its expiration period.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771617559/sessiontimeout_01.png)

If the **Session Auto Keep Alive** attribute is set to *False*
(the default), the user will be prompted with a pop-up panel in the browser, which asks if the
session should be kept alive. This prompt appears some minutes before the timeout occurs.
If the user confirms the prompt, the session is kept alive and the user may
continue working. If the pop-up is ignored for some minutes, the browser session
is redirected to another web page, such as a login page.

### Web Server Session Expiration Setting

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif) The Session Timeout element *does not* control or affect the web server's session expiration setting. That depends entirely on the web server's configuration.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771617815/sessiontimeout_02.png)

For
Windows IIS, the default expiration setting is 20 minutes and can be set using either the IIS Management Console
(under the Logi application virtual directory![](https://logianalytics.zendesk.com/hc/article_attachments/4402771511575/menuarrowrt.png)Session State (a typical configuration for IIS 7.5 is shown above) or in the application's Web.config file. Exact settings will vary depending on which Session State mode is being used. Refer to Microsoft's documentation on the subject for more information.

For Linux/UNIX servers, timeout configuration locations vary; consult the documentation. For example, for Apache Tomcat 7 servers, the value can be found in:

C:\Program Files\Apache Software Foundation\Tomcat 7.0\webapps\*yourLogiApp*\WEB-INF\web.xml

as this code:

  <session-config>  
    <session-timeout>20</session-timeout>  
  </session-config>

where the value is in minutes.

## Attributes

The Session Timeout element has the following attributes:

| Attribute | Description |
| --- | --- |
| Session Auto Keep Alive | Specifies the operating mode. When set to *True*, the session remains alive for as long as the browser is open. Once the browser closes, the server-side session times-out after its expiration period.  If set to *False* (the default), the user will be asked, in a warning pop-up panel, if they want to continue the session. This prompt appears some minutes before the timeout occurs. If the user confirms the prompt, the session is kept alive. If the pop-up is ignored for some minutes, the browser session is redirected to another web page, such as a login page. |
| Session Ended URL | Specifies a URL that the browser will redirect to once the session ends. The default is the standard Logi logout page rdLogout.aspx. |
| Session Keep Alive  Caption | Specifies the button caption in the warning pop-up panel. Clicking the button keeps the session alive. The default caption is "Continue the Session". |
| Session Keep Alive Caption Class | Specifies the class used to style the Session Keep Alive Caption text. |
| Session Warning Caption | Specifies the text displayed in the warning pop-up panel. The default value is "Your session will automatically end soon". |
| Session Warning Caption Class | Specifies the class used to style the Session Warning Caption text. |
| Session Warning Duration | Specifies the amount of time, in minutes, that the warning pop-up panel will be displayed before the browser is redirected to the Session Ended URL value. The default value is 3 minutes.  This formula is used to determine when the warning pop-up panel will be displayed:  Server session expiration - (Session Warning Duration + 2)  For example, if the server session expiration setting = 20 minutes and Session Warning Duration = 3 minutes, the warning pop-up will appear after 15 minutes of inactivity. |
| Template Modifier File | Specifies the name of an optional Template Modifier file. The template modifier file can be in any folder accessible to the application; if a fully-qualified file path is not provided then the application expects it to be in the \_SupportFiles folder. |

## Use the Element

The **Session Timeout** element is easy to implement:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771618071/sessiontimeout_03.png)

Simply add the Session Timeout element in your \_Settings definition, as shown above, then set its optional attributes as desired.
