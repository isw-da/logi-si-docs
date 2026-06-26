---
title: "Debugging an Application"
id: 4419707854999
section: "Manage - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707854999-Debugging-an-Application
updated_at: 2022-07-17T01:36:51Z
---

# Debugging an Application

# Debugging an Application

Logi Studio also provides **debugging** features for an application, but
they have to be enabled to work. They are *not* enabled by default. You
can turn on debugging for all your definitions by clicking the
**Debug** icon in Studio's main menu and selecting
*DebuggerLinks* from the selection list.

Clicking the icon sets an
attribute value in
[The \_Settings Definition](https://devnet.logianalytics.com/hc/en-us/articles/4419723151767-The-Settings-Definition), General element, and you can also turn debugging on by setting that value
directly.

When the application is run, each page will display a debug
icon in the bottom-right corner of the browser window. The Debug Trace page
this link leads to contains detailed information about the page execution,
including account names, request variables, database query results, error
messages, etc. and is a very good way to identify errors. Each chart on a
page will also have its own debug icon and trace page.

More detailed
information about Logi application debugging techniques can be found in
[Debug Reports](https://devnet.logianalytics.com/hc/en-us/articles/4419715245463-Debug-Reports).
