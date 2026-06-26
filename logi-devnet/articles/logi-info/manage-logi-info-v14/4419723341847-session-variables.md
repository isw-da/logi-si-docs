---
title: "Session Variables"
id: 4419723341847
section: "Manage - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723341847-Session-Variables
updated_at: 2022-07-17T02:05:16Z
---

# Session Variables

# Session Variables

Session Variables are values that are global in scope and persistent for
the life of a user session. They're very useful in Logi applications for
retaining and passing data. This topic discusses the elements and
techniques associated with Session Variables in a Logi application.

The following sections discuss working with Session Variables:

* [Setting Session Variables](https://devnet.logianalytics.com/hc/en-us/articles/4419723339799-Setting-Session-Variables#Setting)
* [Using @Session Tokens](https://devnet.logianalytics.com/hc/en-us/articles/4419707991703-Using-Session-Variables#Tokens)
* [Java Session Variable Copying](https://devnet.logianalytics.com/hc/en-us/articles/4419723338775-Java-Session-Variable-Copying#Java)
* [Viewing Session Variables in Debugger](https://devnet.logianalytics.com/hc/en-us/articles/4419723340695-Viewing-Session-Variables-in-Debugger#Debugger)

## About Session Variables

Session Variables provide a useful way to store values that can be used
anywhere in a Logi application and provide the best approximation of a
real programming *variable* you'll find in stateless web
applications.
Logi application Session Variables can be set in both Report and Process
definitions using the **Set Session Variables** and
**Procedure.Set Session Vars** elements, respectively. They can also be
set by other, non-Logi applications and used in an integrated Logi
application (see the Java Session Copying section for special
considerations that apply to Java applications).

Session Variables, of course, only exist as long as the user session
lasts. The
[Session Timeout](https://devnet.logianalytics.com/hc/en-us/articles/4419715459991-Managing-Session-Timeout-)
element can be used to manage the user session lifetime.
When using
[Logi SecureKey Authentication](https://devnet.logianalytics.com/hc/en-us/articles/4419723086999-Logi-SecureKey-Authentication), the **Security** element in \_Settings includes a
**Restart Session** attribute that can be set to clear out all Session
Variables right before an attempted login. This ensures that Session
Variables established during a previous user's session are not re-used for
the next user's session.

### Restrictions

Session Variables are of the *variant* data type, meaning they
can be anything - strings, numbers, arrays, etc. - of any size, and that
opens the door to potential abuse. It's possible to put huge amounts of
data into Session Variables but it's poor practice to do so, because that
will negatively affect server performance. Our recommendation is that you
use Session Variables for *small amounts of data only*.

The **Repeat Elements** element is one of the very first things
processed when a page goes through the Logi Engine. Some values, including
@Session tokens set with the two Set Session elements mentioned earlier,
aren't processed until *later* so @Session tokens should
*not* be used with Repeat Elements.
