---
title: "Action Elements Example: With an Event Handler"
id: 4419723000471
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723000471-Action-Elements-Example-With-an-Event-Handler
updated_at: 2022-07-17T01:45:25Z
---

# Action Elements Example: With an Event Handler

# Action Elements Example: With an Event Handler

Action elements can also be used with Event Handler elements, letting an event trigger an action.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699787543/introacts_12.png)

In the example shown above, an Input Select List element is the parent of an **Event Handler** element. Action and Target elements follow beneath. The Event Handler is set to fire when the DHTML *OnChange* event occurs, so the new report will be displayed when the selection in the list changes.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599575/noteicon.png) You can use *multiple* Event Handlers under a single parent element, each for a different event and each with its *own* Action element. For example, a link created by using a Label element can have an Event Handler for the *onMouseDown* event, and a second one for the *onClick* event. In this way, two Actions can be triggered when the link is clicked. The usefulness of this approach varies, however, based on the types of events the parent element supports and the order in which
they're fired.
For more specific information about using Event Handlers, see [Working with User Input Elements](https://devnet.logianalytics.com/hc/en-us/articles/4419715630487-Working-with-User-Input-Elements).
