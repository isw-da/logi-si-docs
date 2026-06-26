---
title: "Displaying Tokens Adjacent to One Another"
id: 4406817181719
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817181719-Displaying-Tokens-Adjacent-to-One-Another
updated_at: 2022-04-06T06:04:29Z
---

# Displaying Tokens Adjacent to One Another

# Displaying Tokens Adjacent to One Another

One of the simplest way to concatenate text is simply to include their @Data tokens **adjacent** to one another. If we use the SQL query from the previous example, so that two columns are returned,
but choose *not* to use a Calculated Column element, we can achieve the same results with this method.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575831959/combinetext_04.png)

As shown above, this time the **Caption** attribute of the **Label** element is set to both @Data tokens with a space between them. When tokens are resolved, the two names will be displayed along with the separating space.

As you may know, browsers will usually render *one* space within text, but will ignore any other consecutive spaces. So don't bother inserting multiple spaces in a Caption within text or around tokens; all of them after the first one will be ignored by the browser.
