---
title: "Global versus Local Style Sheets"
id: 4419707868183
section: "Manage - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707868183-Global-versus-Local-Style-Sheets
updated_at: 2022-07-17T01:36:08Z
---

# Global versus Local Style Sheets

# Global versus Local Style Sheets

The presence of the **Style**  element in a report definition indicates a *local* style sheet, one that applies only to that definition. A Logi application may contain several report definitions, and each definition may use a separate style sheet. However, a *global* style sheet can be used instead, one that affects *all* report definitions in an application. The global style sheet is configured in the \_Settings definition.

![](https://devnet.logianalytics.com/hc/article_attachments/4419707086871/usingcss_05.png)

1. Double-click the \_Settings definition in the Application Panel, so that it opens for editing in the Workspace panel.
2. In the Element Toolbox panel, double-click the **Global Style** element to add it to the definition.
3. Select the Global Style element, as shown above, and select a style sheet from the pull-down list in its **Style Sheet** attribute.

Now all of the applications definitions will be able to use classes from the global style sheet and you need not assign a style sheet to each definition individually.

However, what happens if you assign *both* a local *and* a global style sheet, and each has a class with the same name but with a different class definition? As you might guess, the local style sheet's classes will override those of the same name in the global style sheet. This is discussed in more detail in [Position May Matter](https://devnet.logianalytics.com/hc/en-us/articles/4419723194519-Position-May-Matter).
