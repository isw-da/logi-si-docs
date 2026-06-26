---
title: "Themes and Style Sheets"
id: 4419715632791
section: "Manage - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715632791-Themes-and-Style-Sheets
updated_at: 2022-07-17T01:25:36Z
---

# Themes and Style Sheets

# Themes and Style Sheets

When a theme is selected for a definition or application, it automatically applies a specific appearance to super-elements, like the Analysis Grid. In addition, the theme makes available a standard set of **style****classes** that developers can apply to regular elements. This can save a lot of time and helps to create a consistent appearance.

![](https://devnet.logianalytics.com/hc/article_attachments/4419715021207/workthemes_06.png)

In the example shown above, we see a definition that has had a theme applied to it. A **Division** element has been selected and one of the theme-supplied style classes is being assigned to it. As you can see, all of the theme-supplied classes begin with the letters "Theme" and they address alignment, font sizes, borders, and other useful styles.

Themes do not set the style class for *every* element; for example, Label and Rows, Row, and Column Cells (HTML tables) are not affected. You can set the **Class** attribute for these elements independently of the theme.

You can specify both a style sheet *and* a theme in a Global Style or Style element. If you have a style sheet and a theme assigned, the available classes from both will appear in the drop-down class list.

## Interaction with Other Style Sheets

You may already have a style sheet that you like to work with when developing reports. How will that **interact** with a theme when it's applied to your report?

If you have assigned a style class to an element and the theme also applies a style class to that same element, the theme's style will be applied first, then yours. This means both styles will be applied but your style will "win" when there's a direct conflict. When there's no conflict, the effect will be *additive*.

## Themes and Exports

Theme effects will also be applied to exports, which may or may not be desirable, and there is no way to block or undo the effects of a theme that has been assigned using the Global Style element. So if you plan to export reports to a format where appearance is important, such as PDF, you may want to assign themes using individual Style elements in each report, instead of the Global Style element.
