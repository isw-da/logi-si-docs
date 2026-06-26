---
title: "Passing Parameters to a Popup Panel"
id: 4419707776791
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707776791-Passing-Parameters-to-a-Popup-Panel
updated_at: 2022-07-17T01:40:21Z
---

# Passing Parameters to a Popup Panel

# Passing Parameters to a Popup Panel

As shown in previous examples, a common use of the Popup Panel is to
provide drill-down into the details of data that's presented in a Data Table. Placing a Popup Panel element in a Data Table column will result in
a pop-up being generated for *every* table row, which could have a
negative performance impact.

An alternate approach is to place the Popup Panel *outside* of the
Data Table and pass parameters to it, so that it can do its own lookup and
then present detail data. We'll use two Event Handlers again and make use
of the fact that, even though the hidden pop-up panel has been generated
(once when the report is first shown), we can use AJAX technology to
"re-draw" the hidden pop-up when a link in the Data Table is
clicked. The fact the panel isn't visible at the time doesn't matter and,
right after it's re-drawn, we'll show it.

An important detail is that the DHTML Events scheme recognizes the
pressing of a mouse button (*MouseDown*) as distinct from when the
button bottoms out (*Click*). It also recognizes the button coming
back up after a click (*MouseUp*) but we don't need to use that event
right now.

![](https://devnet.logianalytics.com/hc/article_attachments/4419707021207/poppanel_11.png)

Consider the example above. A Popup Panel has been added to a report, but
this time it's *not* under a Data Table column. The first child
element of the panel is a **Division**, and below it a **Label**. In
this example, the label is just a way to verify that the parameter we'll
pass has been received; the parameter will be available as a normal
@Request token. The Division has no attributes set other than its unique
element **ID** (which *is* important).

![](https://devnet.logianalytics.com/hc/article_attachments/4419699860631/poppanel_12.png)

Now, as shown above, an **Event Handler** element has been added
beneath the **Label** ("lblContactName") used to display data
in a Data Table column. Its **DHTML Event** attribute value is set to
*onMouseDown*.

Beneath it, an **Action.Refresh Element** element has been added, and
its attributes have been set as shown. When the mouse button is pressed
down, the division in the hidden panel will be refreshed, using AJAX.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599575/noteicon.png) The Action.Refresh Element element can have a
**Link Parameters** child element; its values are "received"
in the pop-up as @Request tokens when the pop-up panel is refreshed. If we
use an @Data token as the parameter value, we can pass data specific to
the row containing the link into the pop-up. In a scenario where you want
to show detail data in the pop-up, the Link Param can send identifying
data (like an OrderID) into it. Then elements in the pop-up might use that
OrderID to look up and display detail data in the pop-up.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714872855/poppanel_13.png)

Finally, we've added a second Event Handler element, as shown above,
beneath the Label in the Data Table column. Its DHTML Event attribute
value is set to *onClick*.

Beneath it, an **Action.Show Element** element has been added, and its
attributes have been set as shown. This element will cause the popup panel
to be shown.

So, to review: the Label element that users will click has
*two* Event Handlers beneath it. The first one will pass a request
variable to the pop-up panel and refresh it; the second one will cause the
refreshed pop-up panel to be shown.
