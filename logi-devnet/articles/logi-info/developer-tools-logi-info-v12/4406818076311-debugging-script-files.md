---
title: "Debugging Script Files"
id: 4406818076311
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406818076311-Debugging-Script-Files
updated_at: 2022-04-06T06:10:02Z
---

# Debugging Script Files

# Debugging Script Files

You can also cause debugging to extend to scripts. When enabled, a special link willbe included in the standard Debugger Trace page:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575447575/scripting_15.png)

To enable this, configure the **General** element's **Script Source Debugger Style** attribute.

Its *None* value is the default, or you can set it to *OnError*, in which case the View Script File link shown above appears in the Debugger Trace Page when an error occurs. This link displays the script as generated when the report was run. If the script is a simple, single line of script, the actual error may appear here instead of a link.

A third value option, *Always*, causes the link
to appear in the trace page at all times. *The routine use of Always is discouraged as it will incur a significant performance hit.*
