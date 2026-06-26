---
title: "Position May Matter"
id: 4419723194519
section: "Manage - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723194519-Position-May-Matter
updated_at: 2022-07-17T01:36:06Z
---

# Position May Matter

# Position May Matter

Because of the way that the HTML is generated when a Logi application is run, the *position* of a local **Style**  element in the Element Tree may be significant. It may affect its ability to override classes in other style sheets, especially for individual elements such as Dashboards and Analysis Grids.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714907671/usingcss_06.png)

Due to the variety involved in this, it's difficult to provide definite rules here. However, if you're attempting to override other classes and find it's not working, and have checked all other variables such as correct spelling, etc., try repositioning the Style element *lower down* in the element tree so that it's below the element you're trying to affect.
