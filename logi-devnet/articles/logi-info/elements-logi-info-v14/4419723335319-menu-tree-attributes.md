---
title: "Menu Tree  Attributes"
id: 4419723335319
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723335319-Menu-Tree-Attributes
updated_at: 2022-07-17T02:05:20Z
---

# Menu Tree  Attributes

# Menu Tree Attributes

The Menu Tree element is the container for the entire menu. It has the following attributes:

| Attribute | Description |
| --- | --- |
| ID | (Required) Specifies a unique element ID. |
| Branch Collapsed Image | When a vertical menu mode is used, specifies an image that appears beside a menu branch that's collapsed. If located in \_SupportFiles, then only the file name is required. Otherwise provide a complete file path. If left blank, a default image is used. |
| Branch Expanded Image | When a vertical menu mode is used, specifies an image that appears beside a menu branch that's expanded. If located in \_SupportFiles, then only the file name is required. Otherwise provide a complete file path. If left blank, a default image is used. |
| Class | Specifies one or more CSS classes to be used by the element. When set, this class will also be used by all child elements that don't have their own class. May be used with or without a theme. |
| Disable Remember  Expansion | Specifies whether the expanded/collapsed state of the menu branches is stored in the browser's Local Storage and re-applied at the next viewing. The default value is *False*, so specify *True* to disable this feature. |
| Horizontal Menu Spacing | Specifies the number of spaces displayed between menu branches when the Menu Mode is *HorizontalPopup*. The default is *5* spaces. |
| Level Indent | Specifies the amount of indentation, in pixels, used to offset successive menu leaf levels in a hierarchy when using a vertical menu mode. The default value is *10* pixels. |
| Menu Mode | Specifies the type of menu to be displayed: *HorizontalPopup*, *Vertical*, or *VerticalPopup*. See the About the Menu Tree section of [Menu Tree Menus](https://devnet.logianalytics.com/hc/en-us/articles/4419723336215-Menu-Tree-Menus) for a visual example of each mode. |
| Security Right ID | When using Logi Security, specifies one or more Security Right IDs, separated by commas. Users with these Security Right IDs will be able to see the menu, users without them will not. |
