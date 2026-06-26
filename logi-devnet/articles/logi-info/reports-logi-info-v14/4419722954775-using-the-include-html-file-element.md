---
title: "Using the Include HTML File Element"
id: 4419722954775
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722954775-Using-the-Include-HTML-File-Element
updated_at: 2022-07-17T02:24:15Z
---

# Using the Include HTML File Element

# Using the Include HTML File Element

The **Include HTML File** element allows an HTML document to be included within your Logi report definition. HTML files stored in your application's \_SupportFiles folder will be available for selection in the element's attributes from a drop-down list.

The Include HTML File element can be placed in your definition beneath a number of elements, such as **Report Header**, **Body**, **Division**, **Data Table Column**, **Report Footer**, and others. When it's placed beneath any of these lower level elements, the HTML it references will be inserted between the <BODY> tags of the generated report page.

It can also be a child of the **Report** (root) element in your definition, which places the HTML between the report page's <HEAD> tags. This can be very useful for including scripts, instructing the browser where to
find external style sheets, providing meta information, and more.
See the [Element Reference](https://clm.logianalytics.com/rdPage.aspx?rdReport=ElementRefDetail&itemID=846&iName=IncludeHtmlFile&iType=Element&iLabel=Include+HTML+File&lnkpg=0) entry for this element for a complete list of parent elements.

![](https://devnet.logianalytics.com/hc/article_attachments/7522840542743/inclhtml_02.png)

If your HTML file has been added to the application in the \_SupportFiles folder, then, in the Include HTML File element's **Filename** attribute, you need only specify the actual file name (or select it from the drop-down list), as shown above. Otherwise, you'll need to specify a fully-qualified file path (on the web server), starting with a drive letter and the @Function.AppPhysicalPath~ can be used here for that purpose.

You can place script functions in an HTML file (with the proper <SCRIPT> tags) and use Include HTML File to include them in definitions; this can be useful if you want to include the same script functions in a number of Logi definitions but maintain them all in a single file. Or, you may want to use scripting in this manner to include an external JavaScript library.

<script type="text/javascript" src="\_Scripts/tiny\_mce/tiny\_mce.js"></script>

For example, the **TinyMCE editor** used in DevNet's forums is added into DevNet using an Include HTML File element and an HTML file containing the script shown above.

Here are some key points to remember when working with HTML files with *visible content* and the Include HTML File element:

## Caching Confusion

Files embedded with the Include HTML File element are *cached* at the web server. If you forget about this, it can cause great frustration when you edit the HTML content in your file and then it doesn't appear to change in the report page! To abandon the cached content, you will need to delete the value in the Filename attribute, save and browse the page again, then re-enter the filename and continue testing. Or, if it doesn't affect anyone else, you can reset the web server.

## Width Coordination

When embedding your HTML file in a report definition that you must pay close attention to *widths*. Possible parent elements, such as Column and Data Table Column, need to be wide enough to accommodate your HTML file; conversely, your HTML file may need to constrain its own width to fit inside the Logi report page. Coordination of widths is essential for a good result.

## No Scrolling

A file displayed using the Include HTML File element will be shown in its *entirety*; its full length will be displayed, "pushing" anything below it down the page. There is no option to show a portion of it within a scrolling window. (To create a scrolling area for HTML content within a report, you need to use the **Sub-Report** element).

## Style sheet Interaction

The effects of style classes referenced in your embedded HTML document will be *combined* with those of the Logi report page containing the document. They will interact and this can have unexpected consequences as different classes vie for precedence. There is no hard-and-fast rule to follow concerning the use of style in this situation, but be prepared for the possibility that a little experimentation may be necessary to get things looking right.
