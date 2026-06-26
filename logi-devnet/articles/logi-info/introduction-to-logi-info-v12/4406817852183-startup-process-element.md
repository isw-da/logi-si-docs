---
title: "Startup Process Element"
id: 4406817852183
section: "Introduction to Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817852183-Startup-Process-Element
updated_at: 2022-04-06T06:08:38Z
---

# Startup Process Element

# Startup Process Element

The **Startup Process** element lets you run a task *automatically* when a user session begins
(i.e., when the application is browsed by a user for the first time).
This allows you to set variables, run procedures, and accomplish any
other "startup" work you might want to do, and then redirect the browser
to a report definition.

*Multiple* Startup Process elements can be used; they'll be processed in the order in which they're listed in the definition.

When the Startup Process element's **First Session Only** attribute equals *True*, the Processes Task runs only for the server's first session. This enables startup processing to occur when the application starts, rather than when any subsequent session starts.

Any Request variables in the query string used to call the application will automatically be available as Request tokens in the process task called with this element. For example, @Request.rdReport~ will contain the name of the report definition.

The startup task runs *before* Connection elements are processed. This can be especially useful if you want to set session variables based on user identity or security parameters in the task, then use them as @Session tokens in Connection element attributes to create dynamic connections.

Unlike most process tasks, you *do not* need to use a **Response** element at the end of this task. Once the startup task is finished, the complete original URL will be sent to the browser again, automatically, so you don' t need to worry about specifying a report definition or forwarding request parameters. It couldn't be easier.

Of course, if you *want* to do some evaluation in the task, with Procedure.If, for example, and then redirect to some *other* report definition, you can use Response and Target elements to do that.

More information about Process tasks can be found in [Process Tasks](https://devnet.logianalytics.com/hc/en-us/articles/4406817796375-Process-Tasks).
