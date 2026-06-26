---
title: "Using Embedded Mode"
id: 4419708005015
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419708005015-Using-Embedded-Mode
updated_at: 2022-07-17T02:22:44Z
---

# Using Embedded Mode

# Using Embedded Mode

When the SubReport element's **SubReport Mode** attribute is set to *Embedded*, the subreport *must* be a Logi report definition.

![](https://devnet.logianalytics.com/hc/article_attachments/7522730737815/subreports_03.png)

In the example above, the SubReport element has been added and its **SubReport Mode** attribute value has been set to *Embedded*. With this mode setting, the attributes that have been covered with a shaded block are *ignored* and a **Target.Report** child element *must* be used to specify the Logi report definition to be embedded. Other types of Target elements may not be used.

![](https://devnet.logianalytics.com/hc/article_attachments/7522716993431/subreports_04.png)

When the Logi Server Engine renders the page, it will render the embedded report *first* and then *merge* its HTML code right into the HTML code for the main report as it generates it, surrounding it with <DIV> tags. The page resulting from the sample code looks like the above.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) Keep these restrictions in mind when using this mode:

* Do not embed report definitions containing super-elements, such as the **Analysis Grid**, using this mode. Internal component naming and session variable conflicts will arise and the super-element will not work correctly.
* Do not embed report definitions that use the **Wait Panel** element when using this mode.
* Any **Sort** elements used beneath individual Data Table columns and **Interactive Paging** elements in the subreport definition will be *ignored* and will not be rendered.
* You can add a **Style** element to the subreport but it may be overridden by the main report's style.
* Drilling down using subreports in this mode is limited to two levels. In other words, you cannot drill down through one report to a subreport, which itself embeds another subreport, then drill down again using links in the second embedded subreport. Those links will not work correctly.
