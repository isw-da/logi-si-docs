---
title: "Using the Meta Names Element"
id: 4406817518359
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817518359-Using-the-Meta-Names-Element
updated_at: 2022-04-06T06:06:35Z
---

# Using the Meta Names Element

# Using the Meta Names Element

The HTML <META> tag provides metadata about a Logi report. Metadata is
not displayed on the page, but is "machine parsable" and is typically used to specify page description, keywords,
modification dates, and other details. The <META> tag always goes between the <HEAD> tagsand can be used by browsers (to tell them how to display content or to reload page),
search engines (keywords), and other web services.

Logi products provide the **Meta Names** element, which allows developers to set some of the more common <META> tag variations directly, without the use of an external HTML file and the Include HTML File element. The Meta Names element is child of the report's root element.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583902231/inclhtml_03.png)

The example above shows a Meta Names element with every one of its attributes configured (they're all optional),

<META name="Description" content="Great document about including HTML" />  
 <META name="Generator" content="LogiInfo" />  
 <META name="Keywords" content="Logi Analytics, HTML, Reports" />  
 <META name="Robots" content="noindex" />  
 <META http-equiv="refresh" content="60" />

and the resulting <META> tag that each attribute generates in the report page are shown above. The element's attributes are described below:

| Attribute | Description |
| --- | --- |
| Meta Description | Specifies a description of the web page. Some search engines use this to provide the user with a document summary in the result of a search. |
| Meta Generator | Specifies the name of the application used to create the document. The default value is *LGXReporting*. |
| Meta Keywords | Specifies a comma-separated list of words that describe the document. Some search engines use this for keyword searches. |
| Meta Robots | Specifies whether the containing document should be indexed by search engines |
| Refresh | Specifies an interval, in seconds, for periodically refreshing the report. |
