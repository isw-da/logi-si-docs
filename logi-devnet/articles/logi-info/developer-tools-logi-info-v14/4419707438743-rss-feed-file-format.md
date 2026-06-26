---
title: "RSS Feed File Format"
id: 4419707438743
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707438743-RSS-Feed-File-Format
updated_at: 2022-07-17T01:55:45Z
---

# RSS Feed File Format

# RSS Feed File Format

There are several versions of RSS in use; the version discussed here conforms to one of the latest, **RSS 2.0**. The syntax rules of RSS 2.0 are very simple but very strict. There are basically two sections, one that describes the feed itself and one that contains the descriptions of the articles, reports, or items in the feed.

<?xml version="1.0" encoding="ISO-8859-1" ?>  
<rss version="**2.0**">  
<channel>  
<title>**Logi Analytics Support Discussion Forum**</title>  
<link>**https://devnet.logianalytics.com/rdPage.aspx?rdReport=DiscussionForum**</link>  
<description>**Logi Analytics Support Discussion Forum**</description>  
<item>  
<title>**Window Size****ThreadID=71102&https://devnet.logianalytics.com/rdPage.aspx?rdReport=ForumThreadPosts>link<
  
>/title<**</link>  
<description>**How can I determine the Window size?>**</description>  
<author>**John Doe**</author>  
<pubDate>**Thu, 12 Apr 2007 3:12:01 EDT**</pubDate>  
</item>  
</channel>  
</rss version>

In the example above, first line in the document is the XML declaration which defines the XML version and the character encoding used in the document.

The next line is the RSS declaration which identifies that this is an RSS document (in this case, RSS version 2.0).

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599319/criticalicon.png) Elements are *case-sensitive*.

The next line contains the required <channel> element, which is used to
describe the RSS feed. It has three required child elements:

* <title> - Defines the title of the channel (e.g. Logi Analytics Support Discussion Forum)
* <link> - Defines the hyperlink to the channel (e.g.
  https://devnet.logianalytics.com/rdPage.aspx?rdReport=Forum)
* <description> - Describes the channel (e.g. Logi Analytics Support Discussion Forum)

Each <channel> element can have one or more <item> elements, each of which defines an article or report in the RSS feed. The <item> element has three required child elements:

* <title> - Defines the title of the item (e.g. "Window Size")
* <link> - Defines the hyperlink to the item (e.g. https://devnet.logianalytics.com/rdPage.aspx?rdReport=Posts&ID=71102)
* <description> - Describes the item (e.g. "How can I determine the Window size?")

Not required, but widely used, are two additional child elements for each <item> element: <author> and <pubdate>. Finally, the last two lines close the <channel> and <rss>
elements.
The syntax for writing comments in RSS is similar to that of HTML: <!-- This is my RSS comment -->
There are other RSS elements that we won't use, including images; you can find out more here about [RSS syntax](http://www.w3schools.com/xml/xml_syntax.asp).
