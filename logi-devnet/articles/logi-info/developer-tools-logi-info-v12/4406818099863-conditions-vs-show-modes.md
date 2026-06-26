---
title: "Conditions vs. Show Modes"
id: 4406818099863
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406818099863-Conditions-vs-Show-Modes
updated_at: 2022-04-06T06:10:10Z
---

# Conditions vs. Show Modes

# Conditions vs. Show Modes

It may appear that the
**Show Modes** and the **Condition** attributes do the same thing:
show and hide elements.
However, Show Modes processing occurs in the *client* (the browser),
whereas Conditions are processed in the *server.* This means Show
Modes are more browser-dependent and may not always behave exactly as
expected with different browsers, making Conditions a better choice in
many situations.

Whereas Show Modes simply hide page parts in the browser, Condition
actually keeps them from being generated at all. For example, a data table
column hidden using a Condition never has its data rendered; it's never
sent by the server to the browser. However, if Show Modes are used for the
same purpose, then the data column *is* rendered and *is* sent
to the browser, where it's then hidden (but might be seen by viewing the
page's HTML source code). So, using the Condition in this case is more
secure, in that it ensures that data is not sent to the browser at all.

However, Show Modes do not require a roundtrip to the server to make
dynamic changes, as Conditions do, so there may be performance
implications involved in deciding which mechanism to use.

Condition attributes may also have a performance impact: If an element
isn't rendered then, obviously, its child elements aren't rendered either.
Child datalayers that aren't rendered, won't run to retrieve data. So
Conditions can be used in some cases to determine when, or if, datalayers
run.

When exporting, Show Modes include built-in values that make hiding or
showing elements very easy, so they may be a better choice for that
purpose.

For more information about Show Modes, see
[Show Modes](https://devnet.logianalytics.com/hc/en-us/articles/4406818147095-Show-Modes).
