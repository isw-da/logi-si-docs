---
title: "Adding a Button using HTML"
id: 4406822615319
section: "Manage - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822615319-Adding-a-Button-using-HTML
updated_at: 2022-04-06T06:09:57Z
---

# Adding a Button using HTML

# Adding a Button using HTML

Of course, if you want to, or need to, add icons using the actual HTML, it can be done by using the **Include HTML** element.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562979351/fa_03_636x149.png)

In the example shown above, an Include HTML element has been added and its HTML code is set to:

<button type="button" onclick="window.location.href='http://www.google.com'">  
 <i class="fa fa-chevron-circle-up fa-2x"></i>  
</button>
which uses the *onClick* event to trigger an action when the button icon is clicked.

And the resulting icon is shown above.
