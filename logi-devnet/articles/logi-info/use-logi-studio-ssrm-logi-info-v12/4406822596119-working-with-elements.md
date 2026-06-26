---
title: "Working with Elements"
id: 4406822596119
section: "Use Logi Studio/SSRM - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822596119-Working-with-Elements
updated_at: 2022-04-06T06:09:41Z
---

# Working with Elements

# Working with Elements

The primary source code files for Logi applications are report definitions. These files contain XML-formatted text and Studio allows you to create and edit this text by graphically manipulating objects, called "elements". In Studio, elements are arranged in a tree structure that mirrors the top-to-bottom structure of a web page and some elements have names that are similar to HTML tags.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563003415/usingstudio_09.png)

The example above shows elements in the "Element Tree" in a report definition. An element can be the "parent" of another element, creating a **parent-child** relationship between them. In the example above, the **Label**, **New Line**, and **Image** elements are children of the **Body** element. These relationships are governed by *rules* which are enforced within Studio by restricting the availability of child elements for assignment to a parent element.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583654423/usingstudio_10.png)

Elements can be added to the element tree by first selecting the parent element and then double-clicking the child element in the **Element Toolbox** panel, or by dragging-and-dropping the element. The Element Toolbox, shown above, includes:

1. Elements are grouped by function, and groups can expanded or collapsed.
2. Elements can be double-clicked, or dragged-and-dropped, in order to add them to a definition.
3. Tabs to specify the relationship of the displayed elements to the element selected in the definition: **Child** or **Sibling**. Only elements which apply to the specified relationship type will be displayed.

You can also filter the elements shown in the toolbox:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563003799/usingstudio_10a.png)

Just enter letters into the Filter Elements box, shown above, and the elements in the toolbox will be filtered as you type. And, of course, only elements that appear in the toolbox because they have a relationship with the element selected in the Element Tree will be included in the filtered list.

Child and sibling elements can also be added to the definition by right-clicking an element in the tree and selecting them from the **context menu** that appears:

![](https://devnet.logianalytics.com/hc/article_attachments/4417583654935/usingstudio_11.png)

An element's context menu, shown above, includes several useful options for working with elements, such as moving, copying, cutting, or deleting them.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563004439/usingstudio_12.png)

You can also select *multiple* parent elements (hold down the "Ctrl" key while selecting them) and then add a child element beneath all of them at once. In the example above on the left, multiple **Data Table Column** elements have been selected, then the **Sort** element was chosen from the Element Toolbox. The result, on the right, shows a Sort element added beneath each selected Data Table Column element.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583655447/usingstudio_13.png)

Once in the tree, elements can be moved up or down by dragging them or by using the **Up** and **Down** tool bar arrows or similar items in their context menus. The example above shows a **New Line** element being dragged upward in the tree; note the circled green positioning dot that helps you determine where to drop it. When an element is moved in this way, all of its child elements move with it. Even groups of elements (peers, on the same level in the tree) can
be
selected and moved at the same time.

Elements can also be copied and pasted, individually or in groups, back into the same definition, into another definition, or even into another Logi application in order to reuse them. All of their child elements will be copied with them.

Even XML source code, copied from the Workspace panel's **Source** tab, can be pasted right into the element tree and will instantly appear there as the correct elements. This is a great way to share code via email or discussion forums.

Two special elements, **Shared Element** and **Include Shared Element**, can be used to make one instance of a group of elements re-usable throughout your application. Elements placed under a Shared Element element in one definition can be referenced using the Include Shared Element element in other definitions. This is particularly useful, for example, for managing **headers** and **footers** that appear on many reports within an application. More information about these useful elements
is available in
[Shared Elements](https://devnet.logianalytics.com/hc/en-us/articles/4406822603415-Shared-Elements).

### Element Positioning

By default, Logi definitions use *Flow Positioning* to arrange the elements on a report page. This is a very common scheme in web applications in which each element's location is dependent on the location of the elements preceding it. This is the most flexible scheme and works best across multiple browsers.

### Element Seeker

Logi Studio includes a feature, the **Element Seeker**, that lets you quickly locate an element in a definition file by selecting it in your preview or browser window. To use it, you must be working in Logi Studio v12.2 SP5+ and the Logi Server Engine version of your Logi application also has to be v12.2 SP5+. In addition, if you're using the Internet Explorer browser, you must be using IE 9 or
later. Here's how it works:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575478679/usingstudio_13a.png)

Enable the Element Seeker in Studio's Debug menu, as shown above. When you preview or browse a report page, you'll see the Seeker icon in the lower right-hand corner.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563004951/usingstudio_13b.png)

When you click the Seeker icon, it will turn green and enter selection mode. As you move your mouse cursor around the page, different regions will be framed in green, as shown above. Click a framed region...

![](https://devnet.logianalytics.com/hc/article_attachments/4417583655831/usingstudio_13c.png)

... and Logi Studio will open the correct report definition and select the element responsible for the chosen region, as shown above.

To turn *off* the Seeker's selection mode, you'll need to refresh your preview or browser page.
