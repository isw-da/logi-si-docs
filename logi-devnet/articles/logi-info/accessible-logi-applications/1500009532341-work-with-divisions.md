---
title: "Work with Divisions"
id: 1500009532341
section: "Accessible Logi Applications"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009532341-Work-with-Divisions
updated_at: 2021-06-17T01:58:45Z
---

# Work with Divisions

# Work with Divisions

Developers can use the **Division** element in their Logi reporting applications to **contain** and **organize** groups of elements within a report. The Division element makes working with groups of element in Studio easier and provides the ability to dynamically apply style classes, or to show and hide report sections. This topic discusses the Division element and techniques for its use.

* About the Division Element
* [Ease Repetitive Development Tasks](#EaseDev)
* [Stretch the Element Rules](#Rules)
* [Hide/Show Report Sections Using Show Modes](#ShowModes)
* [Hide/Show Report Sections Using Conditions](#Conditions)
* [Hide/Show Report Sections Using Action.Refresh Element](#Refresh)
* [Hide/Show Report Sections Using Security Rights](#Rights)

## About the Division Element

In Studio, in a report definition's Element Tree, the **Division** element functions as a "container" for other elements. It's simply a parent element that can have a wide range of child elements. Yet, this simple element can be extremely useful.

As a container, a **style class** assigned to a Division element affects all of the child elements it contains. For example, a style class that **centers text** or sets a **font size** can be applied once, to a Division element, and all of its children will also use that alignment or font size (unless individually overridden).

Divisions can be also be used as an **organizing** entity. Report **sections**, containing dozens of elements or just a single Label, can be placed within a Division. Then the Division can be shown or hidden, using runtime criteria, and the section will dynamically appear or disappear in the report. This provides tremendous **flexibility** and can be used to **reduce** the number of report definitions that need to be developed and maintained. In this way, a report based on just
one report definition that uses Divisions can appear differently in different circumstances or to different users. One common usage is to have one report that can add, update, and delete records in a table; the forms and controls for each type of operation are all there, just in different Divisions, which are revealed or hidden as needed.

The presence of a Division element normally causes a set of **SPAN** tags to be generated in the HTML rendered when the report is run. However, the element has an attribute that allows **DIV** tags to be generated instead. Generally, the DIV tag is considered a "block" container and SPAN an "in-line" container. The most obvious difference between the two tags is that DIV produces a **line break** after it.

The Division element's other attributes, **Condition**, **Show Modes**, and **Security Right ID**, which can be used to show and hide the container, are discussed in later sections.

## Ease Repetitive Development Tasks

Logi Studio allows developers to **copy** and **paste** elements in a report definition's Element Tree, which is very useful in situations where the same element is used repeatedly but with varying attributes. The Division element **extends** this by allowing groups of elements to be copied and pasted.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778435479/divisions_01.gif)

For example, the image above shows a part of the definition for one of DevNet's pages, Developer Library 1. On this page there are a lot of entries for documents and each entry consists of the same **five elements**, highlighted above in yellow. As you can see, these five elements have been placed beneath a **Division** element ("divIntroDataLayers"). The other, unexpanded Division elements also contain these five elements, too.

Suppose now that we need to change the **order** of the entries. This is easily done by selecting a Division element and moving it up or down in the Element Tree; its five child elements will move with it. If we need to **delete** an entry, we simply delete its Division. If we need to **add** a new entry, we copy one of the existing Divisions, paste it in place, and then modify the attributes of its child elements.

Similarly, Divisions and all of their children can be copied between **report definitions** or **applications** in one operation.

This is a very effective method of dealing with situations which entail repetitive use of multiple elements. As you can see, **grouping** elements beneath a Division element makes manipulating them easy.

## Stretch the Element Rules

The parent-child element **relationships** in Logi Studio are controlled by a set of "element rules". These ensure that developers can't inadvertently create bizarre and unworkable relationships, such as a **Dashboard** as the child of a **Label** element. However, occasionally developers may need to "stretch" the rules and the Division element can help.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778435735/divisions_02.gif)  ![](https://logianalytics.zendesk.com/hc/article_attachments/4402778435991/divisions_02a.gif)

In the example above, left, a **PopupPanel** element has been used in the definition. However, in the Element Toolbox, the **Image** element is not available for use beneath it; the Element Rules do not allow it. However, as shown in the example on the right, by adding a **Division** element beneath the PopupPanel, an Image element can then be used.

The Division element, as an "invisible" container, can be used in this way to achieve the desired results.

## Hide/Show Report Sections Using Show Modes

Another benefit of the Division element is the ability to use its **Show Modes** attribute to set its visibility (and the visibility of its child elements).  As discussed earlier, circumstances may dictate that only certain parts of a report be visible to a user. 

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771513495/divisions_03.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771513751/divisions_03a.gif)

This can be achieved by placing elements beneath a Division element, then setting the Division element's **Show Modes** attribute accordingly, as shown above.

There are built-in show mode values available which can be very useful. For example, using the *rdBrowser* value will cause the division to be seen only when the report is displayed as HTML in a browser; using *rdExportPdf* will cause the division to be visible only when the report is exported as a PDF. For more information about using Show Modes, see [Show Modes](https://devnet.logianalytics.com/hc/en-us/articles/1500009532461-Show-Modes).

## Hide/Show Report Sections Using Conditions

The Division element also has a **Condition** attribute, which can also be used to set its visibility (and the visibility of its child elements).  As discussed earlier, circumstances may dictate that only certain parts of a report be visible to a user. 

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771514007/divisions_04.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778436375/divisions_04a.gif)

This can be achieved by placing elements beneath a Division element, then setting the Division element's **Condition** attribute accordingly, as shown above. If the Condition evaluates to *True*, then the Division and its child elements will be made visible; otherwise they'll be hidden. For more information, see [Work with Conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500009529921-Work-with-Conditions).

## Hide/Show Report Sections Using Action.Refresh Element

The **Action.Refresh Element** element, using AJAX technology, allows you to refresh a portion of a report page instead of the entire report. It can be used, for example, to refresh Division elements and, when used with a **Link Parameters** element, can pass parameters that can cause divisions to be shown or hidden.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778436631/greencheck.gif) To get the refresh to work properly, you must place the Division element(s) to be refreshed *beneath* a parent Division element and then make that parent element the target of your Action.Refresh Element element. Do not target the child Division element(s).

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778436887/divisions_06.png)

In the example shown above, two Division elements have their Condition attributes set so they're displayed based on a Request parameter value. They're both children of the "divParent" element. Clicking the link "lblTest" will refresh "divParent" and pass a parameter value. The two child Division elements will be shown or hidden based on that parameter value.

## Hide/Show Report Sections Using Security Rights

Finally, the Division element also has a **Security Right ID** attribute, which can also be used to set its visibility (and the visibility of its child elements). As discussed earlier, circumstances may dictate that only certain parts of a report be visible to a user. 

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778437143/divisions_05.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771514263/divisions_05a.gif)

This can be achieved by placing elements beneath a Division element, then setting the Division element's **Security Right ID** attribute accordingly, as shown above. If Logi Security is enabled and a user's **security role** has the security right identified in this attribute, then the Division and its child elements will be made visible; otherwise they'll be hidden. For more information, see [Introduction to Logi Security 10](https://devnet.logianalytics.com/hc/en-us/articles/1500009515502-Introduction-to-Logi-Security-10).
