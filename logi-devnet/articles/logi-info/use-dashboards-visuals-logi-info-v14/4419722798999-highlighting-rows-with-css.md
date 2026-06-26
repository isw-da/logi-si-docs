---
title: "Highlighting Rows with CSS"
id: 4419722798999
section: "Use Dashboards & Visuals - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722798999-Highlighting-Rows-with-CSS
updated_at: 2022-07-17T01:54:28Z
---

# Highlighting Rows with CSS

# Highlighting Rows with CSS

In order to increase the "readability" of tables, especially
wide tables, it's often useful to be able to highlight an entire row when
the cursor is hovering over it.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706737559/dtrows_05_627x219.png)

This effect is shown in the example above and can be created using a
simple style class. The CSS used to create the effect is:

#yourDataTableID TR:hover TD { background-color: AliceBlue; }

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599319/criticalicon.png) This may not work if your application doesn't have a
[Doctype Declarations](https://devnet.logianalytics.com/hc/en-us/articles/4419723241623-Doctype-Declarations) set (Logi apps default to the HTML5 doctype) or with some older browser
versions.
