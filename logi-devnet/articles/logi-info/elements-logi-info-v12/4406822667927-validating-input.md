---
title: "Validating Input"
id: 4406822667927
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822667927-Validating-Input
updated_at: 2022-04-06T06:10:32Z
---

# Validating Input

# Validating Input

When it comes to validating data entered by users, we *highly recommend* it! It takes some additional development work up front, but can save so many heartaches (and time) later. Validating data is one of the most important tasks associated with processing user input.
The browser environment presents some validation challenges and there are generally three opportunities to do validation. The first is related to events and occurs when the focus changes from one Input element to another element or when the Input element contents change. Validation in this case is accomplished using Event Handlers.
The second opportunity occurs when the page is submitted. If the validation fails, then the submission is aborted. Logi Studio provides a variety of **Validation** elements for this purpose.
This topic concerns itself with these first two validation opportunities but there is a third: it occurs in the *next* Report page or Process task, *after* submission has completed. That falls outside the scope of this topic but is highly encouraged, especially if you're updating a database.
The **Action.Pre-Action Javascript** element, a child of many Action elements, can be used to validate input and control whether its parent Action element executes. For more information, see [Scripting](https://devnet.logianalytics.com/hc/en-us/articles/4406818083479-Scripting).
