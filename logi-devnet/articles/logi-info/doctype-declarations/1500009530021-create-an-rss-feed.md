---
title: "Create an RSS Feed"
id: 1500009530021
section: "Doctype Declarations"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009530021-Create-an-RSS-Feed
updated_at: 2021-06-17T01:58:08Z
---

# Create an RSS Feed

# Create an RSS Feed

If you report on data that's constantly changing, an **RSS feed** might be the perfect solution for keeping your report consumers informed. This topic provides guidance for creating an RSS ("Really Simple Syndication") feed within Logi reporting products.

* About RSS Feeds
* [Prepare Your Information](#Preparing)
* [RSS Feed File Format](#FileFormat)
* [Create Your Feed File](#Creating)

## About RSS Feeds

An RSS feed is an **XML text file** on your web server that contains a list of headlines or topics, each with a description and link to the complete document or report. To see this in action, take a look a the following RSS feeds:

[Logi Analytics Discussion Forum feed](https://devnet.logianalytics.com/rdPage.aspx?rdReport=ForumThreads&FID=1)    
[Yahoo! News Top Stories](http://rss.news.yahoo.com/rss/topstories)

Users can subscribe to a feed and their browser will periodically check for new content and, optionally, alert them when it's found.
Because the "feed file" on your web server is just an XML text file, it's easy to regenerate it periodically without any human intervention.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771875607/rss_02.png)This can be very useful, for example, if you want to monitor a discussion forum or blog and be alerted when new information is posted. Many Logi Analytics product users monitor our Discussion Forum in this way.

Another possible use of feeds is to let users subscribe to reports that are **published multiple times** per day.

The image at the left identifies elements common to all feeds: (1) a **title** or subject, which is also a **link** to the complete content; (2) a **timestamp** indicating when the content was published; and (3) a brief **description** of the content. The photo is optional.

Though RSS is widely used, another feed variety called **Atom** exists. This topic only deals with RSS feeds.

Popular browsers such as Internet Explorer, Firefox, and Chrome have a full set of features for **working with feeds**. This image ![](https://logianalytics.zendesk.com/hc/article_attachments/4402778709527/rss_03.png) has been widely accepted as the **standard icon** for feeds and appears in the browsers themselves
to identify feeds and their features.

What do you need to do to establish your own feed?

1. You need to identify the **information** that you want to publish by using links in a feed
2. You need to place those links in an **XML file** on your web server, using the correct RSS format and XML elements
3. You need to schedule the **periodic generation** of your feed file

Logi reporting products make this fairly easy to do and each step is discussed below.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif)  The scheduling of feed generation (or any report to run) requires using a process definition,
available only in Logi Info.

There are other aspects of RSS feeds, including the use of 3rd-party "feed aggregator" web sites and feed validation that are not typically relevant to reporting with Logi products and are therefore not covered here. You can find out more about these and other RSS topics [here](https://www.w3schools.com/xml/xml_rss.asp).

## **Prepare Your Information**

The first step in the process is to create a new, or identify an existing, **report definition** that will produce the information that you want to have appear on your feed page. This could be in an existing Logi reporting application or in a separate application created just for this purpose. At a minimum, the application will need one **report definition** and one **process****task**.

If you're creating a new report definition just for this purpose, don't worry about its **appearance**; no one is going to see it. Don't bother with stylesheets, other formatting, or report headers or footers.

Your report definition can contain anything from a static set of Label elements to a table of data from a database. You want to be sure this report will contain the minimum information you'll need to create your feed page: a **title**, a **URL** to the content it describes, a **timestamp**, and a brief **description.** for each item in the feed list.

Feed pages are usually **time-oriented**; users get them because they want to know the **latest information**. In addition, the best feed pages provide a sane number of entries - the top ten (most recent) stories, for example - rather than a great long list of links. If you're getting the data from a database, you might want to retrieve the data sorted by timestamp and limited to a small number of records.

Once you've built your report, preview it and ensure that all of the desired data is there before proceeding.

## RSS Feed File Format

There are several versions of RSS in use; the version discussed here conforms to one of the latest, **RSS 2.0**. The syntax rules of RSS 2.0 are very simple but very strict. There are basically two sections, one that describes the feed itself and one that contains the descriptions of the articles, reports, or items in the feed.

|  |  |
| --- | --- |
|  | <rss version="**2.0**">     <channel>         <title>**Logi Analytics Support Discussion Forum**</title>         <link>**https://devnet.logianalytics.com/rdPage.aspx?rdReport=DiscussionForum**</link>         <description>**Logi Analytics Support Discussion Forum**</description>         <item>             <title>**Window Size**</title>             <link>http:**//devnet.logianalytics.com/rdPage.aspx?rdReport=ForumThreadPosts&ThreadID=71102**</link>             <description>**How can I determine the Window size?>**</description>             <author>**John Doe**</author>             <pubDate>**Thu, 12 Apr 2007 3:12:01 EDT**</pubDate>         </item>     </channel> </rss version> |

In the example above, first line in the document is the **XML declaration** which defines the XML version and the character encoding used in the document. The next line is the **RSS declaration** which identifies that this is an RSS document (in this case, RSS version 2.0). Note that elements are **case-sensitive**.

The next line contains the required **<channel>** element, which is used to
describe the RSS feed. It has three required child elements:

* **<title>** - Defines the title of the channel (e.g. Logi Analytics Support Discussion Forum)
* **<link>** - Defines the hyperlink to the channel (e.g.
  https://devnet.logianalytics.com/rdPage.aspx?rdReport=DiscussionForum)
* **<description>** - Describes the channel (e.g. Logi Analytics Support Discussion Forum)

Each <channel> element can have one or more **<item>** elements, each of which defines an article or report in the RSS feed. The <item> element has three required child elements:

* **<title>** - Defines the title of the item (e.g. "Window Size")
* **<link>** - Defines the hyperlink to the item (e.g. https://devnet.logianalytics.com/rdPage.aspx?rdReport=ForumThreadPosts&ThreadID=71102 )
* **<description>** - Describes the item (e.g. "How can I determine the Window size?")

Not required, but widely used, are two additional child elements for each <item> element: **<author>** and **<pubdate>**. Finally, the last two lines close the <channel> and <rss>
elements.

The syntax for writing **comments** in RSS is similar to that of HTML:  <!-- This is my RSS comment -->

There are other RSS elements that we won't use, including images; you can find out more here about [RSS](https://www.w3schools.com/xml/xml_rss.asp).

## Create Your Feed File

Now that you know what goes into your feed file, you need to provide a link to it from your application or web site. We recommend that you use the **feed icon**. The icon's hyperlink is going to be similar to:

http://myWebServer/myRss/myFeedFile.xml where "myRss" is a folder containing your feed file.

**Free**, **standardized** feed icons are available in a variety of sizes and graphic types [here](http://www.feedicons.com/).

Determine the physical location for your feed file before proceeding and ensure that the local ASPNET (IIS 5.x) or NETWORK SERVICE (IIS 6.x) account has Write permission to that folder.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778710039/rss_04.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771875863/rss_04a.png)

To generate your feed file:

1. Create a **Process definition** (or use an existing Process definition).
2. Add a new **Task** element to it ("taskCreateFeedFile" in the example above).
3. To the task, add a **Procedure.Export XML** element. Set its **Filename** attribute to the full file system path and filename for your feed file. This is an excellent place to make use of the @Function.AppPhysicalPath~ token. Be sure that your filename ends with ".xml".

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771876119/rss_05.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778710423/rss_05a.png)

4. Add a **Target.XML** element, as shown above, beneath the Procedure.Export XML element and set its **Report Definition File** attribute to the report definition that will provide your feed data.

One way to put the data from your report into the correct format and syntax for the feed file is to apply an **XSL Transform** to the raw XML that comes from the Export XML procedure. To do this you'll need to create a transform (.xsl) file and place it in the \_DataXMLs folder in your application project folder.

### What the Transform Does

A full explanation of **XPath** and **XSL Transforms** is beyond the scope of this topic. However, the following should give you a preliminary understanding and help you create your transform file. XPath allows you to **navigate** through the raw XML data and the transform outputs it in the proper **format**.

As an example of how a transform works, follow what happens when the Logi Analytics DevNet Discussion Forum feed is created. Here's one record of the data returned by the SQL query in our feed report definition:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771876375/rss_06.png)

Six columns of data were returned and in the report definition (but not shown here) **Calculated Column elements** were added. These appended extra columns to the datalayer: one named "msgDate" contains a formatted version of the CreateAt date, one named "rssDate" contains a formatted version of today's date, and one named "URL" combines the TID column value with this URL:

https://devnet.logianalytics.com/rdPage.aspx?rdReport=ForumThreadPosts&

|  |  |
| --- | --- |
|  | <rdData>    <MyDataTableSubject="**Window Size**" Message="**How can I determine the Window size?"**      CreatedAt="**2007-04-12T15:12:01.0370000-04:00**" UserName="**John Doe**" ForumTitle="**Managed Reporting**"    msgDate="**Thursday, April 12 2007 3:12:01 PM**" rssDate="**Mon, 16 Apr 2007 14:05:00 EDT**"     URL="**https://devnet.logianalytics.com/rdPage.aspx?rdReport=ForumThreadPosts&****ThreadID=71102**" /> </rdData> |

When the **taskCreateFeedFile** task executes, it runs the report, gets the data discussed earlier, and outputs it using the Export XML procedure to a file. In its raw form, before we apply the transform, the XML data for our one record would look like the example above.

|  |  |
| --- | --- |
|  | <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">     <!-- Results will be XML -->     <xsl:output method="**xml**" />      <xsl:template match="**rdData**">       <xsl:text></xsl:text>        <rss version="**2.0**">          <xsl:text></xsl:text>          <channel>              <xsl:text></xsl:text>               <title>**Logi Analytics DevNet Discussion Forum**</title>               <xsl:text></xsl:text>              <link>**https://devnet.logianalytics.com/rdPage.aspx?rdReport=DiscussionForum**</link>             <xsl:text></xsl:text>               <description>**Logi Analytics DevNet Discussion Forum**</description>               <xsl:text></xsl:text>               <language>**en-us**</language>               <xsl:text></xsl:text>               <webMaster>**DevNet@LogiAnalytics.com**</webMaster>               <xsl:text></xsl:text>               <pubDate>                 <xsl:value-of select="**@rssDate**" />               </pubDate>              <xsl:for-each select="**MyDataTable**">                 <xsl:text></xsl:text>                 <item>                   <xsl:text></xsl:text>                     <title>                        <xsl:value-of select="**@Subject**" />                     </title>                    <xsl:text></xsl:text>                    <link>                         <xsl:value-of select="**@URL**" />                    </link>                    <xsl:text></xsl:text>                   <description>                       <xsl:value-of select="**@Message**" />                   </description>                    <xsl:text></xsl:text>                   <author>                       <xsl:value-of select="**@UserName**" />                    </author>                    <xsl:text></xsl:text>                   <pubDate>                       <xsl:value-of select="**@msgDate**" />                     </pubDate>                    <xsl:text></xsl:text>                 </item>              </xsl:for-each> <xsl:text></xsl:text>           </channel>           <xsl:text></xsl:text>         </rss>     </xsl:template> </xsl:stylesheet> |

The **XLS Transform** used to iterate through and format the raw XML data into a feed file is shown above. Notice that it has a section at the top (starting with **<channel>** that describes the feed, and another (starting with **<xsl: for-each>**) the describes the repeating items (data rows), just as the RSS 2.0 standard requires.

Notice that, in the transform file, the "select" attribute for the <xsl:for-each> element is "MyDataTable". This is the name of the datatable in the feed report definition.

|  |  |
| --- | --- |
|  | <rss version="**2.0**">     <channel>      <title>**Logi Analytics Support Discussion Forum**</title>       <link>**https://devnet.logianalytics.com/rdPage.aspx?rdReport=DiscussionForum**</link>       <description>**Logi Analytics Support Discussion Forum**</description>       <language>**en-us**</language>       <webMaster>**DevNet@LogiAnalytics.com**</webMaster>       <pubDate>**Mon, 16 Apr 2007 14:05:00 EDT**</pubDate>       <item>         <title>**Window Size**</title>          <link>**https://devnet.logianalytics.com/rdPage.aspx?rdReport=ForumThreadPosts&ThreadID=71102**</link>           <description>**How can I determine the Window size?**</description>          <author>**John Doe**</author>           <pubDate>**Thursday, April 12 2007 3:12:01 PM**</pubDate>       </item>    </channel> </rss> |

And, finally, the example above shows the data in the feed file, after the transform has been applied.

These links will lead you to more information about [XPath](https://www.w3schools.com/xml/xpath_intro.asp) and [XSLT Transforms](https://www.w3schools.com/xml/xsl_intro.asp).

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771876631/rss_07.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771876887/rss_07a.png)

To apply your transform:

1. Create your transform file and, in Studio, add it to the **\_DataXMLs** folder in your project folder.
2. In your process definition, add an **XSL Transform** element beneath your Target.XML element, as shown above, and set its **XSL Transform File** attribute to the name of your transform file.

Test your task to ensure that it's writing your feed file in the correct *format* and to the correct *location*.

Finally, put your feed icon, with its link to your feed file, in place and you're all set to allow users to get your feed. Work with your browser to see what happens when you access a feed and how your browser deals with subscriptions to it.

### Schedule Generation of Your Feed File

To update your feed file on a regular basis, you can schedule your taskCreateFeedFile task to run periodically using **Logi Server Manager**. It will overwrite the feed file each time it runs. For complete information about scheduling tasks, see [Schedule Reports with Server Manager](https://devnet.logianalytics.com/hc/en-us/articles/1500009515862-Schedule-Reports-with-Server-Manager).
