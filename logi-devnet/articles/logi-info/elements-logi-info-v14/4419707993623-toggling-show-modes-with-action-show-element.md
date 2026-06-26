---
title: "Toggling Show Modes with Action.Show Element"
id: 4419707993623
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707993623-Toggling-Show-Modes-with-Action-Show-Element
updated_at: 2022-07-17T01:26:20Z
---

# Toggling Show Modes with Action.Show Element

# Toggling Show Modes with Action.Show Element

You may have a need to allow the user, at runtime, to alternately show and hide ("toggle") a report section. Two elements, the **Division** and **Action.Show Element**, using Show Modes, make this easy to do.

![](https://devnet.logianalytics.com/hc/article_attachments/4419707214103/showmodes_05.png)

In the example above, a **Label** element has been placed in a report to be the link for showing and hiding instructions, which are in their own **Division**. The Division element's **Show Modes** attribute is set to an arbitrary value, *XYZ*, which causes it to be hidden initially.

![](https://devnet.logianalytics.com/hc/article_attachments/4419707214487/showmodes_06.png)

An **Action.Show Element** element has been added beneath the link Label and its attributes configured as shown above. Clicking the link will now result in the Show Modes of the Division element being manipulated, "toggling" it between being shown and being hidden.
