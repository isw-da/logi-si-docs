---
title: "Managing Session Timeout "
id: 4419715459991
section: "Manage - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715459991-Managing-Session-Timeout
updated_at: 2022-07-17T01:38:36Z
---

# Managing Session Timeout 

# Managing Session Timeout

The Session Timeout element makes it easy to prevent errors caused by session timeouts.

The following topics discuss use of the Session Timeout element:

* [Session Timeout Attributes](https://devnet.logianalytics.com/hc/en-us/articles/4419715458967-Session-Timeout-Attributes#Attributes)
* [Using the Session Timeout Element](https://devnet.logianalytics.com/hc/en-us/articles/4419707814039-Using-the-Session-Timeout-Element#Using)

## About the Session Timeout Element

When a user's working with a Logi Info application and leaves the browser session
inactive for some time, the server-side session may expire and end. This can
cause problems with pages that need the session state to be live. The
**Session Timeout** element makes it easy to prevent errors caused by session
timeouts.

The element operates in two modes, depending on the value of its **Session Auto Keep Alive** attribute. When
set to *True*, the session remains alive for as long as the browser is open. This is
accomplished by automatically "pinging" the server from the browser, thus informing the
server that the browser is still open. Once the browser closes, the server-side
session times-out after its expiration period.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714893591/sessiontimeout_01.png)

If the **Session Auto Keep Alive** attribute is set to *False*
(the default), the user will be prompted with a pop-up panel in the browser, which asks if the
session should be kept alive. This prompt appears some minutes before the timeout occurs.
If the user confirms the prompt, the session is kept alive and the user may
continue working. If the pop-up is ignored for some minutes, the browser session
is redirected to another web page, such as a login page.

### Web Server Session Expiration Setting

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599319/criticalicon.png) The Session Timeout element *does not* control or affect the web server's session expiration setting. That depends entirely on the web server's configuration.

![](https://devnet.logianalytics.com/hc/article_attachments/4419707061271/sessiontimeout_02_400x562.png)

For
Windows IIS, the default expiration setting is 20 minutes and can be set using either the IIS Management Console
(under the Logi application virtual directory![](https://devnet.logianalytics.com/hc/article_attachments/4419714617623/menuarrowrt.png)Session State (a typical configuration for IIS 7.5 is shown above) or in the application's Web.config file. Exact settings will vary depending on which Session State mode is being used. Refer to Microsoft's documentation on the subject for more information.
For Linux/UNIX servers, timeout configuration locations vary; consult the documentation. For example, for Apache Tomcat 7 servers, the value can be found in:

C:\Program Files\Apache Software Foundation\Tomcat 7.0\webapps\*yourLogiApp*\WEB-INF\web.xml

as this code:

<session-config>  
<session-timeout>20</session-timeout>  
</session-config>

where the value is in minutes.
