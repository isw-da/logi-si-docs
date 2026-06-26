---
title: "Working with User Input Elements"
id: 4406818159767
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406818159767-Working-with-User-Input-Elements
updated_at: 2022-04-06T06:10:34Z
---

# Working with User Input Elements

# Working with User Input Elements

**User Input** elements allow users to interact with applications, most often to provide reporting criteria.

The following topics discuss a variety techniques for working with these elements:

* [Working with Change Flags](https://devnet.logianalytics.com/hc/en-us/articles/4406822668823-Working-with-Change-Flags#Flags)
* [Aligning Input Elements](https://devnet.logianalytics.com/hc/en-us/articles/4406818153623-Aligning-Input-Elements)
* [Using AutoComplete](https://devnet.logianalytics.com/hc/en-us/articles/4406822665879-Using-AutoComplete#Complete)
* [Wrapping in a Fieldset Box](https://devnet.logianalytics.com/hc/en-us/articles/4406818160791-Wrapping-in-a-Fieldset-Box#FieldsetBox)
* [Inclusion in Data Tables](https://devnet.logianalytics.com/hc/en-us/articles/4406822663959-Inclusion-in-Data-Tables#Tables)
* [Populating Input Element Collections](https://devnet.logianalytics.com/hc/en-us/articles/4406818154775-Populating-Input-Element-Collections#Populating)
* [Setting Default Values](https://devnet.logianalytics.com/hc/en-us/articles/4406818155927-Setting-Default-Values#DefaultValues)
* [Re-displaying Entered Values](https://devnet.logianalytics.com/hc/en-us/articles/4406822664983-Re-displaying-Entered-Values#Entered)
* [Validating Input](https://devnet.logianalytics.com/hc/en-us/articles/4406822667927-Validating-Input#ValidInput)
* [Using Validation Elements](https://devnet.logianalytics.com/hc/en-us/articles/4406822667031-Using-Validation-Elements#ValidationElements)
* [Using Event Handlers](https://devnet.logianalytics.com/hc/en-us/articles/4406818158359-Using-Event-Handlers#EventHandlers)
* [Using Event Handlers with JavaScript](https://devnet.logianalytics.com/hc/en-us/articles/4406818157335-Using-Event-Handlers-with-Javascript#Javascript)

## When Are Input Values Available?

Logi reports use the basic HTML FORM-submission mechanism for posting input control values. This means that a page *has to be submitted* before any of the values in its Input elements will be available for use in the next or reloaded page. Attempts to access @Data tokens for those values in the page *before* it's submitted will not work.
A common technique is to display a page, let the user enter values and submit the page, and then re-display the same page with dynamic content displayed based on the input values.
Another common technique is to display a page, let the user enter values and submit the page, run a Process task that does something with the entered values, and then re-display the original page.
Some script-based techniques can be used to initiate local actions on the input values, without submitting the page. For example, if text is entered in an input control, itcan be capitalized when the mouse leaves the control.
