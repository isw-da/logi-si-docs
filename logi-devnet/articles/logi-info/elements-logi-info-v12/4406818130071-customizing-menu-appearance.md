---
title: "Customizing Menu Appearance"
id: 4406818130071
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406818130071-Customizing-Menu-Appearance
updated_at: 2022-04-06T06:10:22Z
---

# Customizing Menu Appearance

# Customizing Menu Appearance

An easy way to customize the appearance of Menu Tree menus is by customizing the theme used with the report or application, [Using the Theme Editor](https://devnet.logianalytics.com/hc/en-us/articles/4406818044055-Using-the-Theme-Editor). Menu border, background, and item colors can be set in the Colors category, Menus section of a custom theme.
You can also apply styling using CSS classes directly to the Menu Tree, Menu Branch, and Menu Leaf elements. For example, to make the menu item fonts larger, select a class like *ThemeTextLarger* to an element's **Class** attribute. If you're using your own style sheet, assign a class from it that specifies a larger font size to the attribute.
You can also use Conditional Class elements beneath any of the Menu Tree Menu elements in order to apply classes dynamically.
For more information about Conditional Class elements, see [Using Style Sheets](https://devnet.logianalytics.com/hc/en-us/articles/4406822553367-Using-Style-Sheets). Here's an example of how to use CSS to change the appearance of the Menu Tree pop-up panel:

![](https://devnet.logianalytics.com/hc/article_attachments/4417562950295/menutree_07.png)

The pop-up panels shown above have these qualities: they have no border, they appear just below the header, and they're a little transparent.
To achieve that, you'll need to override an existing theme class by adding it to your own style sheet:

.rdPopupMenu { border: 0px; opacity: 0.8; top: 39px !important; }

You'll need to adjust the "top" attribute to align it correctly with the bottom of your header.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) This change may affect *all* pop-up panels in your application.

## Adding a "Separator" Menu Item

When using vertical menus, sometimes it's desirable to provide some kind of visual separator between menu items:

![](https://devnet.logianalytics.com/hc/article_attachments/4417583602327/menutree_06.png)

In the example shown above, a "separator" item provides visual separation between one category of menu items and another. This is easily created by adding a **Menu Leaf** element that has no action associated with it (so it's not a link) and has a Caption that provides the desired visual. In the example above, several of the Unicode characters "Horizontal Bar" (U+2015) were used.
