---
title: "Action.Show Element"
id: 4419707912215
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707912215-Action-Show-Element
updated_at: 2022-07-17T01:32:12Z
---

# Action.Show Element

# Action.Show Element

The Action.Show element is used in Logi reports to *show* and *hide* sections of a report or elements within it. Using DHTML techniques, this element lets you give the end-user dynamic control over page content, which is very useful.

The following topics provide examples for using the Action.Show element:

* [Usage Example: Show/Hide Divisions](https://devnet.logianalytics.com/hc/en-us/articles/4419715545239-Action-Show-Element-Example-Show-Hide-Divisions#Examples)
* [Usage Example: Show/Hide a More Info Row](https://devnet.logianalytics.com/hc/en-us/articles/4419715546135-Action-Show-Element-Example-Show-Hide-a-More-Info-Row#MoreInfo)

## About Action.Show Element

Like most Action elements, Action.Show element is the child of a parent element such as **Label**, **Image**, or **Button** element, and is activated when its parent element is clicked.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699947415/showelement_01.png)  

In the example shown above, clicking the "A - E" link on the left results in the Index panel expanding to reveal links for the documents in that category. Clicking it again will collapse the panel back to its original state.

This is accomplished by placing the document links within a **Division** element; clicking the A-E link activates an Action.Show Element element that alternately shows or hides the division. The background images are applied using style and automatically expand or collapse to fill the space that the text requires.

The Action.Show Element element's **Element ID** attribute determines which element (the "target" element) will be affected when the Action.Show Element is activated. Action.Show Element works by overriding the **Show Modes** attributes of the target element. Multiple target elements can be specified in a comma-separated list and you can independently assign the desired action (show or hide) to each element in the listby adding :Show or :Hide after the element ID.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599575/noteicon.png) These terms
are *case-sensitive*; you must use ":Show", for example, not ":show". In addition, if these explicit actions are specified, the usual "toggle" effect will not work. In other words, clicking on a link that calls Action.Show element with <ElementID>:Show will show the element, but another click on the same link will not hide it.

Action.Show Element's **Display** attribute determines whether a target element will be visible or invisible; there are three values that can be selected: *Show* (visible), *Hide* (invisible), or the default*Toggle* (opposite of current state).

The **Show Element Effect** attribute can be set to *FadeIn* and the target element will be shown with a brief transparency effect, so it appears to "fade-in".

Unlike other actions, Action.Show Element does not have a specific **Target** child element. No links can be made to another report definition and only elements within the same definition can be controlled.
