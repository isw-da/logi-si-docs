---
title: "Label Elements Support Immediate IF"
id: 1500009531341
section: "Doctype Declarations"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009531341-Label-Elements-Support-Immediate-IF
updated_at: 2021-06-17T01:58:31Z
---

# Label Elements Support Immediate IF

# Label Elements Support Immediate IF

In Logi Studio, **Label** elements can make use of an intrinsic Immediate (or sometimes called "Inline") IF function. This allows you to do conditional processing in the label's Caption attribute value.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778542743/labelimmedif_01.png)

An example of this in action is shown above, where the general syntax for the IIF function is:

=IIF(statement to evaluate, true value, false value)  
 

When using this function in a Caption attribute remember that you must preface it with an equals ("=") sign and, in the statement to be evaluated, when comparing strings the values on both sides of the equals sign must be within double-quotes, as shown.

More information about intrinsic functions can be found in [Intrinsic Functions and Operators](https://devnet.logianalytics.com/hc/en-us/articles/1500009530801-Intrinsic-Functions-and-Operators).
