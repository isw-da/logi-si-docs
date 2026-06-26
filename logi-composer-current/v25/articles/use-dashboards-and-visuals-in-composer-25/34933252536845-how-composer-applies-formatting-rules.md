---
title: "How Composer Applies Formatting Rules"
id: 34933252536845
section: "Use Dashboards and Visuals in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933252536845-How-Composer-Applies-Formatting-Rules
updated_at: 2026-05-26T22:09:04Z
---

# How Composer Applies Formatting Rules

# How Composer Applies Formatting Rules

You can apply formatting rules to data affected by multiple conditions. The formatting rules are applied sequentially, and can cancel out a previously applied rule.

For example, if you define the background row color for orders from Florida to appear green, but define the background row color for orders that fall within a certain threshold to appear blue, the final result will depend on the order in which you organize your format rules.

![The blue background rule overrides the green background rule](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46166963153421 "Conditional Formatting example")

In the above example, formatting based on the **State** condition is applied first, then formatting based on the **Actualsales** condition overrides that rule.

![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167007067021)

In the above example, formatting based on the **Actualsales** condition is applied first, then formatting based on the **State** condition overrides that rule.

Mix and match rules as needed to achieve the look and feel you want.
