---
title: "Viewing Session Variables in Debugger"
id: 4419723340695
section: "Manage - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723340695-Viewing-Session-Variables-in-Debugger
updated_at: 2022-07-17T02:22:46Z
---

# Viewing Session Variables in Debugger

# Viewing Session Variables in Debugger

The Logi **Debugger Trace Page** is very useful for identifying
problems and includes helpful information, such as the values of all
Request variables. However, it doesn't usually display SessionVariables.
However, for .NET applications, you can enable a
*full trace page* that will show you the Session Variables and much
more.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725373335/sessionvars_05_538x275.png)

To turn on full tracing:

1. Locate your Logi application's
   rdPage.aspx
   file in the application folder, as shown above.
2. Use a text editor, such as Notepad, to edit the file to include
   Trace="True", as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725381783/sessionvars_06_610x517.png)

The full trace page, similar to the one shown above, will now appear at
the bottom of every report page and you can see the Session State section,
highlighted, showing all the Session Variables. You'll see quite a few
that start with "rd" - these are created by the Logi Engine.
