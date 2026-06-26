---
title: "Using the Label Element with HTML Format"
id: 4419707623319
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707623319-Using-the-Label-Element-with-HTML-Format
updated_at: 2022-07-17T02:24:15Z
---

# Using the Label Element with HTML Format

# Using the Label Element with HTML Format

The **Label** element can be used to insert HTML into your report. This is done by setting its **Format** attribute to *HTML* and entering the desired HTML code in its Caption attribute.

Because the code is embedded within an existing HTML page when the report is generated, you *do not* need to include <HTML> or <BODY> tags in the Caption.

Any valid HTML can be entered in the Caption and this is often a simple way to add **Bold** or *Italic* effects to text without the need for a style class. The HTML must be "well-formed";
that is, you need to ensure that you have entered all of the matching opening and closing HTML tags required.

For example, have you ever needed to call a Logi report and then automatically scroll to some specific location within it? In HTML, this is done using an **Anchor** tag (<A>) with a named bookmark in the destination page. Here's how to do it using a Label element:

![](https://devnet.logianalytics.com/hc/article_attachments/7522823987863/inclhtml_04.png)  

1. In the *destination* report, use a **Label** element to create an HTML bookmark, as shown above. The Label element won't be visible, so include it in the appropriate location in your report (the location that the browser will scroll to when the report is displayed). Set its **Format** attribute to *HTML* and, in its **Caption** attribute, enter the HTML code for an anchor, with the anchor name ("Security" in the example).

![](https://devnet.logianalytics.com/hc/article_attachments/7522794452503/inclhtml_05.png)  

2. In the *calling* report, in the **Target.Report** element used to identify the destination Logi report, add a hash mark (#) and the anchor name after the report definition name, as shown above.

Now, when the link, image, etc. that calls the report definition is clicked, the browser will scroll to bring the Label element from Step 1 into view. The URL generated looks like this:

http://myServer/myLogiApp/rdPage.aspx?rdReport=newReport3#Security

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) For the anchor to work correctly, it has to be the very *last* thing in the query string. This means, for example, that you cannot use this technique with **Link Parameters** or the **Wait Page** element, as they will add items to the query string *after* the anchor name.

Label elements include "HTML Attribute Params", enabling you to apply your application to work with other frameworks or libraries easier. With the HTML Attribute Params, you have the option to include "Id", "type", and "value" parameters:

![](https://devnet.logianalytics.com/hc/article_attachments/7522798805271/label_attributes_873x354.png)

After the HTML Attribute Params are applied:

![](https://devnet.logianalytics.com/hc/article_attachments/7522813179415/label_attributes_applied.png)

If an attribute was set in both Element and HTML attribute params, the one set in the HTML attribute params will be ignored.
