---
title: "Combining Icon and Text in a Label"
id: 4419715579543
section: "Manage - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715579543-Combining-Icon-and-Text-in-a-Label
updated_at: 2022-07-17T01:30:10Z
---

# Combining Icon and Text in a Label

# Combining Icon and Text in a Label

You can combine an icon with the caption of a **Label** element:

![](https://devnet.logianalytics.com/hc/article_attachments/4419707171863/fa_04_630x153.png)

As shown above, a Label element is given a **Caption** attribute value and set to the FA class for the desired icon.

![](https://devnet.logianalytics.com/hc/article_attachments/4419707172119/fa_05.png)

And the result is shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599575/noteicon.png)

* If you want to add more space between the icon and the text, add a space at the beginning of your Caption attribute (only *one* - any more than that will be ignored by the browser).
* The style of the caption *text* is controlled by the FA classes. You can't change it by adding more classes to the Class attribute.

  However, if you want to style the icon and the text separately, you can do this:

![](https://devnet.logianalytics.com/hc/article_attachments/4419699989271/fa_06_628x215.png)

In this example, separate Label elements are used for the icon and the accompanying text. The Label element for the icon is also placed in a separate Division, which allows the icon to be further styled, in this case by setting its Color using CSS in a separate style sheet.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699989527/fa_07.png)

By applying style to the Division element ("divStyleFA") that contains the icon, the icon color has been set to *Blue.* The second Label element's Class attribute has been set to change the font size of the text.
