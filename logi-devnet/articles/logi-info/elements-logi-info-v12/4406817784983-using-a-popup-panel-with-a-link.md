---
title: "Using a Popup Panel with a Link"
id: 4406817784983
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817784983-Using-a-Popup-Panel-with-a-Link
updated_at: 2022-04-06T06:08:10Z
---

# Using a Popup Panel with a Link

# Using a Popup Panel with a Link

Adding a Popup Panel to your report definition is simple and
straightforward:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575571735/poppanel_03.png)

In the example above, a **Popup Panel** element (named
"pnlPhoto1") has been added to the definition in a data table
column. Its attributes have been set to control its behavior. ![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png)
The panel's caption will display data from the datalayer, through the use
of @Data tokens, which is why the Popup Pane has been placed as a
child-element beneath a Data Table Column element. Otherwise it could have
been placed anywhere in the definition.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583771799/poppanel_04.png)

Next, below the Popup Panel element, an **Image** element has been
added, as shown above, and its **Caption** attribute set to data
returned from the datalayer that specifies the image filename.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563122583/poppanel_05.png)

Finally, a link has been created, which shows or hides the Popup Panel, by
adding an **Action.Show Element** element to the **Label** element
that displays the data in the report's Property Number column. Its
attributes are set to make it act upon the Popup Panel
("pnlPhoto1") and to cause the panel's visibility to
*toggle*, or alternate, between shown and hidden.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563124631/poppanel_06.png)

The examples above show the data table and what happens when one of the
Property Number links is clicked. The report is disabled when the panel is
displayed and the background is "grayed" out because the Popup
Panel has been set to *Modal*.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png)
When you place a popup panel in a data table column, an
instance of the panel will be generated for *every* row in the data
table. This could have performance implications when using large data
sets. Another technique, placing the Popup Panel element *outside* of
the data table, is discussed in [Passing Parameters to a Popup Panel](https://devnet.logianalytics.com/hc/en-us/articles/4406817781783-Passing-Parameters-to-a-Popup-Panel).
