---
title: "Create an RSS Feed"
id: 4406822214039
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822214039-Create-an-RSS-Feed
updated_at: 2022-04-06T06:04:44Z
---

# Create an RSS Feed

# Create an RSS Feed

If you report on data that's constantly changing, an **RSS feed** might be the perfect solution for keeping your report consumers informed.

The following topics provide guidance for creating an RSS ("Really Simple Syndication") feed within Logi Info:

* [Preparing Your Information](https://devnet.logianalytics.com/hc/en-us/articles/4406817224599-Preparing-Your-Information#Preparing)
* [RSS Feed File Format](https://devnet.logianalytics.com/hc/en-us/articles/4406817226007-RSS-Feed-File-Format#FileFormat)
* [Creating Your Feed File](https://devnet.logianalytics.com/hc/en-us/articles/4406822213143-Creating-Your-Feed-File#Creating)

## About RSS Feeds

An RSS feed is an XML text file on your web server that contains a list of headlines or topics, each with a description and link to the complete document or report. To see this in action, take a look a the following RSS feed:

[Yahoo! News Top Stories](http://rss.news.yahoo.com/rss/topstories)

Users can subscribe to a feed and their browser will periodically check for new content and, optionally, alert them when it's found.
Because the "feed file" on your web server is just an XML text file, it's easy to regenerate it periodically without any human intervention.

This can be very useful, for example, if you want to monitor a discussion forum or blog and be alerted when new information is posted. Many Logi Analytics product users monitor our Discussion Forum in this way.
Another possible use of feeds is to let users subscribe to reports that are published multiple times per day.
The image at the left identifies elements common to all feeds: (1) a *title* or subject, which is also a link to the complete content; (2) a *timestamp* indicating when the content was published; and (3) a brief *description* of the content. The photo is optional.
Though RSS is widely used, another feed variety, called **Atom**, also exists. This topic only deals with RSS feeds.
Popular browsers such as Internet Explorer, Firefox, and Chrome have a full set of features for working with feeds. This image ![](https://devnet.logianalytics.com/hc/article_attachments/4417563432983/rss_03.png) has been widely accepted as the standard icon for feeds and appears in the browsers themselves
to identify feeds and their features.  
What do you need to do to establish your own feed?

1. You need to identify the information that you want to publish by using links in a feed
2. You need to place those links in an **XML file** on your web server, using the correct RSS format and XML elements
3. You need to schedule the periodic generation of your feed file

Logi Info makes this fairly easy to do and each step is discussed below.
There are other aspects of RSS feeds, including the use of 3rd-party "feed aggregator" web sites and feed validation that are not typically relevant to reporting with Logi products and are therefore not covered here. You can find out more about these and other RSS topics [here](http://www.w3schools.com/xml/xml_rss.asp).
