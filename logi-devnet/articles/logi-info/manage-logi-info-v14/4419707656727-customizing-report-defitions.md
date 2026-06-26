---
title: "Customizing Report Defitions  "
id: 4419707656727
section: "Manage - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707656727-Customizing-Report-Defitions
updated_at: 2022-07-17T01:45:44Z
---

# Customizing Report Defitions  

# Customizing Report Defitions

Logi Info includes a technology called Definition Modifier Files (DMF). A DMF is an XML file that contains instructions to modify a definition file's
elements and their attributes at runtime. It's a separate file that's processed
*before* the Logi Server Engine starts to render a report definition. At
that time, elements may be conditionally inserted or removed, and attributes may
be set or unset.
This makes it possible to set culture- or customer-specific values based, for
example, on locale or security roles, at run-time. This means that each user can
potentially receive a different report because the definition used to generate
their report has been customized for them, on the fly.
DMFs are similar to the Template Modifier Files,
mentioned in [Customizing Super-Element Interfaces](https://devnet.logianalytics.com/hc/en-us/articles/4419722990103-Customizing-Super-Element-Interfaces-), and they're also conceptually similar to a plug-in
that executes on the "LoadDefinition" event. In this context, you might think of
them as the "poor man's plug-in": they can provide similar functionality but
don't require additional development tools (Visual Studio, etc.) to write and
compile a plug-in .dll or .jar file.
To assist with globalization, a DMF could be used, for example, to perform language translation. XPath notation can be used in a DMF to find and replace specific strings of text anywhere in a report definition, in order to translate them into another language on-the-fly. You could even have a different DMF for each language supported and tokenize the DMF name in your report definition so that you can support multiple languages automatically.
This subject is discussed in detail in [Template Modifier Files](https://devnet.logianalytics.com/hc/en-us/articles/4419715482903-Template-Modifier-Files).
