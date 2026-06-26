---
title: "Working with Change Flags"
id: 4419723352471
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723352471-Working-with-Change-Flags
updated_at: 2022-07-17T01:25:54Z
---

# Working with Change Flags

# Working with Change Flags

You may find it useful to know, after a page with User Input elements has been submitted, whether or not any changes were made to their default values - did the user make any changes? This, for example, might let your code decide whether or not to take some action, such as updating a database record. Logi Info provides a "change flag" mechanism to let you make this determination.
A "change flag" is simply a Request variable with a *True* or *False* value; an Input Hidden element is added to a Report definition to generate that value. Other User Input elements specify the Input Hidden element's ID in their **Change Flag Element ID** attributes. When the page is submitted, in the next Report definition or Process task, the request variable associated with the Input Hidden element will have a value of *True* if any changes
to Input elements occurred.
This change flag functionality relies on the DHTML "onChange" event supported by all browser. Prior to Logi Info v12.1, this event was used to the exclusion of other events, so you could not also use your own onChange event handler with elements implementing a Change Flag Element ID.  
  
Support for multiple events is now available. When using a change flag, you may also add Event Handlers to User Input elements and they will be processed *after* the onChange events associated with setting the Input element change flags.
