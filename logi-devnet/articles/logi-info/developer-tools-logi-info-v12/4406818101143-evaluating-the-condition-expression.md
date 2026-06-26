---
title: "Evaluating the Condition Expression"
id: 4406818101143
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406818101143-Evaluating-the-Condition-Expression
updated_at: 2022-04-06T06:10:11Z
---

# Evaluating the Condition Expression

# Evaluating the Condition Expression

In all instances, the Condition attribute's value is an
*expression* that evaluates to either *True* or *False*.
Leaving the attribute value blank equates to setting it to *True*.
Expressions should be in JavaScript or intrinsic function syntax.

Tokens of all kinds may be included in expressions.

Expressions used in Conditions *do not* require the leading
"=" sign which is typically used before formulae in other types
of attributes. Values are generally compared using a comparison operator
and, when expressions use string or ambiguous data types, both sides of
the equation should be enclosed in double-quotes. More complex expressions
can be created using logical operators and parentheses.

Here are some example expressions:

| Expression | Comment |
| --- | --- |
| "@Data.LastName~" = "Smith" | Both sides of the equation are known to be strings. |
| @Data.CustomerID~ <> 1234 | Both sides of the equation are known to be numbers. |
| 1 = 1 | This expression can be used to force a *True* value. |
| ("@Request.Page~" = "") Or ("@Request.Page~" = "1") | Logical operators can be used. |
| InStr("@Data.Categories~", "1") > 0 | Script functions are supported. |
| "@Cookie.UserCategory~" = "1" | Cookies are evaluated as **text**. |
| "@Data.City~" = "Toronto" | When used with the Condition Filter element, causes all datalayer rows where the City column value is not "Toronto" to be removed. |

Complete information about
[Built in Functions and Operators](https://devnet.logianalytics.com/hc/en-us/articles/4406817003543-Built-in-Functions-and-Operators)
is available for your reference.

Generally, if the expression contains an error of some kind, such as a
data type mismatch or a missing function argument, no error message is
displayed in the browser; instead, the Condition just doesn't work as
desired. However, an error message *will* usually be included in the
Debugger Trace Page (see [Debug Reports](https://devnet.logianalytics.com/hc/en-us/articles/4406817355543-Debug-Reports))
at the point at which the expression is evaluated. So, if your Condition
isn't working as you expected, check the Debugger page.
