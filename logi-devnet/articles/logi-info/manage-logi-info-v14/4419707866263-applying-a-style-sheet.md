---
title: "Applying a Style Sheet"
id: 4419707866263
section: "Manage - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707866263-Applying-a-Style-Sheet
updated_at: 2022-07-17T01:36:11Z
---

# Applying a Style Sheet

# Applying a Style Sheet

Once a style sheet file has been added to an application's \_SupportFiles folder, it's available for use with any of the definitions within that application.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699916311/usingcss_01.png)  

1. To apply a style sheet to a specific definition, open the definition in the Workspace, as shown above.
2. Add a **Style** element, if necessary,
3. The Style element's **Style Sheet** attribute will provide a pull-down list of the style sheet files in the \_SupportFiles folder. Select the appropriate style sheet for use with this definition.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599575/noteicon.png) Once a style sheet has been selected, it can be edited in an external style sheet editor (if you have installed one) by clicking the Open File... link (shown circled above) at the top of the Attributes panel. This will launch the application associated in the file system with the .css file extension and open the file in it.

You can assign multiple style sheets but adding multiple Style elements in your definition. If two style sheets contain a class with the same name, then the last one (identified in the Style element further down the element tree) will "win" any conflict, overriding earlier classes.
