---
title: "Insert HTML into Reports"
id: 4406822359191
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822359191-Insert-HTML-into-Reports
updated_at: 2022-04-06T06:06:32Z
---

# Insert HTML into Reports

# Insert HTML into Reports

The Logi Server Engine generates HTML and JavaScript when it processes a Logi definition, but you may find that you need to insert your own HTML code directly into a Logi report.

The following topics discuss the elements available to insert HTML:

* [Using the HTML Tag Element](https://devnet.logianalytics.com/hc/en-us/articles/4406817515543-Using-the-HTML-Tag-Element#HTMLTag)
* [Using the Include HTML Element](https://devnet.logianalytics.com/hc/en-us/articles/4406822360087-Using-the-Include-HTML-Element#InclHTML)
* [Using the Include HTML File Element](https://devnet.logianalytics.com/hc/en-us/articles/4406817516823-Using-the-Include-HTML-File-Element#UsingElement)
* [Using the Meta Names Element](https://devnet.logianalytics.com/hc/en-us/articles/4406817518359-Using-the-Meta-Names-Element#Meta)
* [Inserting <Meta> and Other Tags Using JavaScript](https://devnet.logianalytics.com/hc/en-us/articles/4406817513367-Inserting-Meta-and-Other-Tags-Using-Javascript#JavaScript)
* [Using the Label Element with HTML Format](https://devnet.logianalytics.com/hc/en-us/articles/4406822361111-Using-the-Label-Element-with-HTML-Format#Label)
* [Using the Label Element's HTML Tag Attribute](https://devnet.logianalytics.com/hc/en-us/articles/4406822362007-Using-the-Label-Element-s-HTML-Tag-Attribute#Attribute)
* [Invalid XHTML Characters](https://devnet.logianalytics.com/hc/en-us/articles/4406817514519-Invalid-HTML-Characters#XHTML)

## About Inserting HTML

The "source code" of a Logi definition is an XML document, which is processed by the Logi Server Engine, and output as HTML. However, you may want to insert your own HTML code directly into a Logi report. There are many reasons for wanting to do this, including adding <META> information, adding <SCRIPT> content, and embedding external HTML documents into your report page.
For example, the topic you're reading right now is actually a separate, external HTML file that has been embedded into the DevNet site page.

### Requirements

HTML that's included into a Logi definition must be have properly-formed tag structures, and include all closing tags. For example,

<p><strong>My Title</strong></p>

If a complete HTML page is embedded, it may include <HTML> and <BODY> tags, but they aren't required.
