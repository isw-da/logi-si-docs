---
title: "Session Variables"
id: 4406818143383
section: "Manage - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406818143383-Session-Variables
updated_at: 2022-04-06T06:10:26Z
---

# Session Variables

# Session Variables

Session variables are values that are global in scope and persistent for
the life of a user session. They're very useful in Logi applications for
retaining and passing data. This topic discusses the elements and
techniques associated with Session variables in a Logi application.

The following sections discuss working with Session Variables:

* [Setting Session Variables](https://devnet.logianalytics.com/hc/en-us/articles/4406822656663-Setting-Session-Variables#Setting)
* [Using @Session Tokens](https://devnet.logianalytics.com/hc/en-us/articles/4406818141335-Using-Session-Variables#Tokens)
* [Java Session Variable Copying](https://devnet.logianalytics.com/hc/en-us/articles/4406822655639-Java-Session-Variable-Copying#Java)
* [Viewing Session Variables in Debugger](https://devnet.logianalytics.com/hc/en-us/articles/4406818142359-Viewing-Session-Variables-in-Debugger#Debugger)

## About Session Variables

Session variables provide a useful way to store values that can be used
anywhere in a Logi application and provide the best approximation of a
real programming *variable* you'll find in stateless web
applications.
Logi application Session variables can be set in both Report and Process
definitions using the **Set Session Variables** and
**Procedure.Set Session Vars** elements, respectively. They can also be
set by other, non-Logi applications and used in an integrated Logi
application (see the Java Session Copying section for special
considerations that apply to Java applications).

Session variables, of course, only exist as long as the user session
lasts. The
[Session Timeout](https://devnet.logianalytics.com/hc/en-us/articles/4406817840407-Managing-Session-Timeout-)
element can be used to manage the user session lifetime.
When using
[Logi SecureKey authentication](https://devnet.logianalytics.com/hc/en-us/articles/4406822454807-Logi-SecureKey-Authentication), the **Security** element in \_Settings includes a
**Restart Session** attribute that can be set to clear out all Session
variables right before an attempted login. This ensures that Session
variables established during a previous user's session are not re-used for
the next user's session.

### Restrictions

Session variables are of the *variant* data type, meaning they
can be anything - strings, numbers, arrays, etc. - of any size, and that
opens the door to potential abuse. It's possible to put huge amounts of
data into Session variables but it's poor practice to do so, because that
will negatively affect server performance. Our recommendation is that you
use Session variables for *small amounts of data only*.

The **Repeat Elements** element is one of the very first things
processed when a page goes through the Logi Engine. Some values, including
@Session tokens set with the two Set Session elements mentioned earlier,
aren't processed until *later* so @Session tokens should
*not* be used with Repeat Elements.
