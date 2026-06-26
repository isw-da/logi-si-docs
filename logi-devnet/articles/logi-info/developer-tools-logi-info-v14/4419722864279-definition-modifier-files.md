---
title: "Definition Modifier Files"
id: 4419722864279
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722864279-Definition-Modifier-Files
updated_at: 2022-07-17T01:51:46Z
---

# Definition Modifier Files

# Definition Modifier Files

**Definition Modifier Files** (DMFs) allow you to modify any of the
elements and attributes in a report definition, based on conditional
criteria, at runtime.

The following topics discuss the use of these files:

* [The Definition Modifier File Element](https://devnet.logianalytics.com/hc/en-us/articles/4419707522583-The-Definition-Modifier-File-Element#Element)
* [The Definition Modifier File](https://devnet.logianalytics.com/hc/en-us/articles/4419722863383-The-Definition-Modifier-File#File)

## About Definition Modifier Files

A DMF is an XML file that contains instructions to modify a definition
file's elements and their attributes at runtime. It's a separate file
that's processed *before* the Logi Server Engine starts to render a
report definition. At that time, elements may be conditionally inserted or
removed, and attributes may be set or unset.

This makes it possible to set culture- or customer-specific values based,
for example, on locale or security roles, at run-time. This means that
each user can potentially receive a different report because the
definition used to generate their report has been customized for them, on
the fly.

DMFs are similar to
[Template Modifier Files](https://devnet.logianalytics.com/hc/en-us/articles/4419715482903-Template-Modifier-Files) (which only affect super-elements and themes) and they're also
conceptually similar to a plug-in that executes on the
"LoadDefinition" event. In this context, you might think of them
as the "poor man's plug-in": they can provide similar
functionality but don't require additional development tools (Visual
Studio, etc.) to write and compile a plug-in .dll or .jar file.

Here are two examples of how DMFs might be used.

* Language Translation: you can use **XPath** notation in a DMF to find
  and replace specific strings of text anywhere in a report definition, in
  order to translate them into another language on the fly. You could even
  have a different DMF for each language supported and tokenize the DMF
  name in your report definition so that you can support multiple
  languages on the fly.

* Insert Additional Elements: you can use a DMF to add custom reporting
  content (headers, footers, and data) based, for example, on the user
  type, company, or other criteria.

DMFs can even insert nested DMFs.

When debugging links are turned on and DMFs are used, special entries
will appear in the
Debugger Trace report:

![](https://devnet.logianalytics.com/hc/article_attachments/4419699684375/usingdmf_03.png)

As shown above, these entries will follow those for the DMF applied by a
Logi Theme. Click them to view the DMF log and the source code of the
modified definition.
For more information, see [Debug Reports](https://devnet.logianalytics.com/hc/en-us/articles/4419715245463-Debug-Reports).
