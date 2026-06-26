---
title: "Conditions Example: Using the Procedure.If Element"
id: 4406822635927
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822635927-Conditions-Example-Using-the-Procedure-If-Element
updated_at: 2022-04-06T06:10:10Z
---

# Conditions Example: Using the Procedure.If Element

# Conditions Example: Using the Procedure.If Element

Tasks within Process Definitions can make use of the
**Procedure.If** element to provide conditional processing. This
element functions like a typical IF-THEN statement in procedural
programming:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575434007/usingcond_06.png)

In the process definition example above, the "taskExport" task
includes a **Procedure.If** element which has a conditional
**Expression** attribute. If this expression evaluates to *True*,
then all of the Procedure.If element's child elements will execute. If the
expression is *False*, then processing will continue with the
**next element** following the Procedure.If element's child elements.
So, as shown above, if the "doExport" Request parameter equals
*1*, then the yellow-highlighted elements will execute; otherwise
they'll be skipped.

Several other elements are available for use in controlling conditional
branching:

**Procedure.Else** - This element *must* be a sibling of, and
immediately follow, a Procedure.If element. It identifies a conditional
block of procedures that will be run if the Procedure.If element
immediately above it evaluates to *False*. If the Else block ran, the
token
@Procedure.myProcedureID.rdReturnValue~
returns *True,* otherwise it returns *False*.

**Procedure.Switch** - This element works with one or more child
**Procedure.Switch Case** elements to define conditional blocks of
procedures to be run when a specified value matches. Use it when there are
multiple conditional blocks defined and just one of them is to be run,
based on the value of a variable. You can also use a child
**Procedure.Switch Else** element, which runs its block of procedures
if *none* of the previous Switch Case elements match the specified
value.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575434263/usingcond_07.png)

The value to test against is specified in the Expression attribute and can
be literal value, a token, or even JavaScript that evaluates to a value.
The Data Type attribute ensures comparisons, especially of dates, are made
correctly.

Conditions give developers a useful tool, providing the ability to
dynamically change their reports and allowing great flexibility when
developing Logi applications.
