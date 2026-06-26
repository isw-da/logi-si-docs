---
title: "Using @Session Variables"
id: 4406818141335
section: "Manage - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406818141335-Using-Session-Variables
updated_at: 2022-04-06T06:10:26Z
---

# Using @Session Variables

# Using @Session Variables

We've already seen some examples of Session variables in use. @Session
tokens can be employed in a lot of places in your definitions. Here are
some more usage examples:

## Navigation Persistence

Because Session variables are persistent across pages, they can be
particularly useful in preserving values just before a Process task call.
For example, suppose you have a task for user login that users can call
from any page in your application. After the login task completes, you
want to return the user to the page he was viewing. Here's one technique
for doing this in a parameterized manner:

1. At the top of each report definition, use elements to create a Session
   variable ("Caller") with a value of
   @Request.rdReport~. This is the definition name of the report.
2. Each report definition, of course, has a link to the Login task.
3. At the end of the Login task, use Response.Report and Target.Report
   elements. In the Target.Report element's Report Definition File
   attribute, enter the
   @Session.Caller~
   token. This ensures the user will go back to the page he was viewing
   before calling the task.

## Dynamic Connections

@Session tokens can be used in the attributes of
**Connection** elements, allowing you to create dynamic connections.
Typically, this is done by using a **Startup Process** element in
\_Settings to run a Process task.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575416599/sessionvars_07.png)

As shown above, the task uses **Procedure.If** and
**Procedure.Set Session Vars** elements to set appropriate Session
variables based on variable criteria.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562946711/sessionvars_08.png)

When the task completes, the Connection elements in \_Settings will be
processed, using @Session tokens, as shown above.

## Dynamic JavaScript Code

Like all tokens, @Session tokens can be used in JavaScript code to make it
dynamic:

if ( '@Session.UserID~' == '' ) alert('Your session has expired.');   
if ( '@Session.UserID~' != '' )
SubmitForm('rdProcess.aspx?rdProcess=someTaskID&UserID=@Session.UserID~',
   '\_self','true','',null);

The code above embeds @Session tokens to determine if a user ID is present
and calls a Process task if it is.
