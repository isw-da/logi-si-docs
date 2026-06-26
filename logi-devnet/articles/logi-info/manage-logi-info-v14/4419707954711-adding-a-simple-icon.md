---
title: "Adding a Simple Icon"
id: 4419707954711
section: "Manage - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707954711-Adding-a-Simple-Icon
updated_at: 2022-07-17T01:30:11Z
---

# Adding a Simple Icon

# Adding a Simple Icon

One of the simplest ways to add an icon to a report is to use a **Label** element.

![](https://devnet.logianalytics.com/hc/article_attachments/4419707171479/fa_02_635x215.png)

The basic procedure is to go to the [FA Icons](https://fortawesome.github.io/Font-Awesome/icons/) web page where all the available icons are displayed, find the icon you want to use, and click it. You'll be taken to a detail page for that icon and you'll see the HTML for implementing it, which looks similar to this:

<i class="fa fa-plus-square"></i>

Select and copy the class attribute from that code (highlighted in yellow) and paste it into your definition, in the Label element's **Class** attribute value, as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599319/criticalicon.png) Class names are *case-sensitive*!
In order to size the icon (relative to its container), you can use one of these additional classes, in combination with the icon class:

fa-lg, fa-2x, fa-3x, fa-4x, fa-5x

Classes for sizing and other usage details are discussed in the [FA Examples](https://fortawesome.github.io/Font-Awesome/examples/) web page.
We've exaggerated the spacing in the Class attribute value in the image above to make things a little clearer. One space between classes is all you need. And the resulting icon looks like this:

Give it a try and experiment with different sizes.
