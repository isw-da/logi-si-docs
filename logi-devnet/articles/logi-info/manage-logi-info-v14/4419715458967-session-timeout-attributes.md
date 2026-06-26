---
title: "Session Timeout Attributes"
id: 4419715458967
section: "Manage - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715458967-Session-Timeout-Attributes
updated_at: 2022-07-17T02:06:21Z
---

# Session Timeout Attributes

# Session Timeout Attributes

The Session Timeout element has the following attributes:

| Attribute | Description |
| --- | --- |
| Session Auto Keep Alive | Specifies the operating mode. When set to *True*, the session remains alive for as long as the browser is open. Once the browser closes, the server-side session times-out after its expiration period.  If set to *False* (the default), the user will be asked, in a warning pop-up panel, if they want to continue the session. This prompt appears some minutes before the timeout occurs. If the user confirms the prompt, the session is kept alive. If the pop-up is ignored for some minutes, the browser session is redirected to another web page, such as a login page. |
| Session Ended URL | Specifies a URL that the browser will redirect to once the session ends. The default is the standard Logi logout page rdLogout.aspx. |
| Session Keep Alive Caption | Specifies the button caption in the warning pop-up panel. Clicking the button keeps the session alive. The default caption is "Continue the Session". |
| Session Keep Alive Caption Class | Specifies the class used to style the Session Keep Alive Caption text. |
| Session Warning Caption | Specifies the text displayed in the warning pop-up panel. The default value is "Your session will automatically end soon". |
| Session Warning Caption Class | Specifies the class used to style the Session Warning Caption text. |
| Session Warning Duration | Specifies the amount of time, in minutes, that the warning pop-up panel will be displayed before the browser is redirected to the Session Ended URL value. The default value is 3 minutes. This formula is used to determine when the warning pop-up panel will be displayed: Server session expiration - (Session Warning Duration + 2) . For example, if the server session expiration setting = 20 minutes and Session Warning Duration = 3 minutes, the warning pop-up will appear after 15 minutes of inactivity. |
| Template Modifier File | Specifies the name of an optional Template Modifier file. The template modifier file can be in any folder accessible to the application; if a fully-qualified file path is not provided then the application expects it to be in the \_SupportFiles folder. |
