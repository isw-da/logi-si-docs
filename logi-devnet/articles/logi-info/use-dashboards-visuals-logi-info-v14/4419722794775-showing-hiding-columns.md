---
title: "Showing/Hiding Columns"
id: 4419722794775
section: "Use Dashboards & Visuals - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722794775-Showing-Hiding-Columns
updated_at: 2022-07-17T02:08:20Z
---

# Showing/Hiding Columns

# Showing/Hiding Columns

The Data Table Column element's **Condition** attribute can be used to dynamically *show* or *hide* the column at runtime, and you may want to do this based on the table's data. However, there's an important restriction on this attribute: an expression used as its value *cannot* include @Data tokens. This is because any tokens used here must be available to be resolved when the table structure is being built but, because the table's datalayer doesn't run until later, there are no @Data tokens
available at that time.

One solution is to use Local Data, then @Local tokens would be available when the table structure is being built and could be used in the Condition attribute. Other types of tokens, of course, can be used in Condition attribute expressions.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) We *do not* recommend using **Show Modes** for this purpose. The attribute was removed in v12.1.188 but you may encounter it in earlier versions. Use the Condition attribute instead.
