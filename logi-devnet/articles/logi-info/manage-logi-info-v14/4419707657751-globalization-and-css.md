---
title: "Globalization and CSS  "
id: 4419707657751
section: "Manage - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707657751-Globalization-and-CSS
updated_at: 2022-07-17T01:45:40Z
---

# Globalization and CSS  

# Globalization and CSS

In Logi reports, stylesheets and their classes can be used to control changes such as fonts, font sizes,
line heights, and reading direction when language changes are necessary. This can be
particularly useful when dealing with languages like Chinese,
where users tend to prefer different fonts,
and can also be useful to better harmonize the look of
mixed, script-specific fonts, such as when mixing Arabic and Latin fonts.
In general, the use of CSS selectors such as text-align, position, background-position, float, and clear, which often use absolute positioning, need to be reviewed when
globalizing
an application. CSS also offers the lang selector, which can be used in a variety of ways to affect the display of text in different languages.
In addition, CSS file encoding can be set by use of the @charset command at the top of the file, for example:

@charset "iso-8859-1"

The standard themes provided with Logi reporting tools include stylesheets and developers may need to create their own custom globalized themes, duplicating all but the stylesheet files, if themes are being used. The stylesheet files would then be customized for globalization. For more information about creating custom themes, see [Themes](https://devnet.logianalytics.com/hc/en-us/articles/4419723357847-Themes).
