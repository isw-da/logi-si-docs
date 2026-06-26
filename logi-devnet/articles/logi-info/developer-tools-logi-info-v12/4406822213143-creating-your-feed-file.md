---
title: "Creating Your Feed File"
id: 4406822213143
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822213143-Creating-Your-Feed-File
updated_at: 2022-04-06T06:04:45Z
---

# Creating Your Feed File

# Creating Your Feed File

Now that you know what goes into your feed file, you need to provide a link to it from your application or web site. We recommend that you use the feed icon. The icon's hyperlink is going to be similar to:

http://myWebServer/myRss/myFeedFile.xml where "myRss" is a folder containing your feed file.

Free, standardized feed icons are available in a variety of sizes and graphic types at [this web site](http://www.feedicons.com/).

![](https://devnet.logianalytics.com/hc/article_attachments/4417584071191/rss_04.png)

To generate your feed file:

1. Create a Process definition (or use an existing Process definition).
2. Add a new **Task** element to it ("taskCreateFeedFile" in the example above).
3. To the task, add a **Procedure.Export XML** element. Set its **Filename** attribute to the full file system path and filename for your feed file. This is an excellent place to make use of the @Function.AppPhysicalPath~ token. Be sure that your filename ends with ".xml".

![](https://devnet.logianalytics.com/hc/article_attachments/4417563433879/rss_05.png)  

4. Add a **Target.XML** element, as shown above, beneath the Procedure.Export XML element and set its **Report Definition File** attribute to the report definition that will provide your feed data.

One way to put the data from your report into the correct format and syntax for the feed file is to apply an **XSL Transform** to the raw XML that comes from the Export XML procedure. To do this you'll need to create a transform (.xsl) file and place it in the \_SupportFiles folder in your application project folder.

## What the Transform Does

A full explanation of **XPath** and **XSL Transforms** is beyond the scope of this topic. However, the following should give you a preliminary understanding and help you create your transform file. XPath allows you to navigate through the raw XML data and the transform outputs it in the proper format.
As an example of how a transform works, follow what happens when a hypotheticalLogi Analytics DevNet Discussion Forum feed is created. Here's one record of the data returned by the SQL query in our feed report definition:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575814935/rss_06_855x66.png)

Six columns of data are returned and, in the report definition (but not shown here), other elements are used to add three extra columns to the datalayer: "msgDate" containing a formatted version of the CreateAt date, "rssDate" containing a formatted version of today's date, and "URL" combining the TID column value with this URL:

https://devnet.logianalytics.com/rdPage.aspx?rdReport=ForumThreadPosts&  

When the **taskCreateFeedFile** task created earlier executes, it runs the report, gets the data discussed earlier, and outputs it using the Export XML procedure to a file.

<?xml version="1.0" encoding="ISO-8859-1" ?>  
<rdData>  
 <MyDataTable Subject="Setting W**indow Size"** Message="H**ow can I get the size of a browser windows at runtime?"**   
 CreatedAt="**2015-11-12T15:12:01.0370000-05:00**" UserName="**John Doe**" ForumTitle="Logi Info" msgDate="**Thursday, November12, 2015 3:12:01 PM**" rssDate="**Mon, 16Nov 2015 14:05:00**"  
 URL="**https://devnet.logianalytics.com/rdPage.aspx?rdReport=ForumThreadPosts&****ThreadID=71102**"/>  
</rdData>

In its raw form, before we apply the transform, the XML data for our one record would look like the example shown above.

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">  
 <!-- Results will be XML -->  
 <xsl:output method="**xml**" />   
 <xsl:template match="**rdData**">  
<xsl:text></xsl:text>  
 <rss version="**2.0**">  
<xsl:text></xsl:text>  
<channel>  
 <xsl:text></xsl:text>   
 <title>**Logi Analytics DevNet Discussion Forum**</title>   
 <xsl:text></xsl:text>  
 <link>**https://devnet.logianalytics.com/rdPage.aspx?rdReport=DiscussionForum**</link> <xsl:text></xsl:text>   
 <description>**Logi Analytics DevNet Discussion Forum**</description>   
 <xsl:text></xsl:text>   
 <language>**en-us**</language>   
 <xsl:text></xsl:text>   
 <webMaster>**DevNet@LogiAnalytics.com**</webMaster>   
 <xsl:text></xsl:text>   
 <pubDate>  
 <xsl:value-of select="**@rssDate**" />   
 </pubDate>  
 <xsl:for-each select="**MyDataTable**">  
 <xsl:text></xsl:text>   
 <item>  
<xsl:text></xsl:text>   
 <title>  
 <xsl:value-of select="**@Subject**" />   
 </title>  
 <xsl:text></xsl:text>  
 <link>  
 <xsl:value-of select="**@URL**" />  
 </link>  
 <xsl:text></xsl:text>  
<description>  
 <xsl:value-of select="**@Message**" />  
</description>  
 <xsl:text></xsl:text>  
<author>  
 <xsl:value-of select="**@UserName**" />   
</author>  
 <xsl:text></xsl:text>  
<pubDate>  
 <xsl:value-of select="**@msgDate**" />   
 </pubDate>  
 <xsl:text></xsl:text>  
 </item>  
 </xsl:for-each><xsl:text></xsl:text>  
 </channel>  
 <xsl:text></xsl:text>   
 </rss>  
 </xsl:template>  
</xsl:stylesheet>

The **XLS Transform** used to iterate through and format the raw XML data into a feed file is shown above. Notice that it has a section at the top (starting with <channel> that describes the feed, and another (starting with <xsl: for-each>) the describes the repeating items (data rows), just as the RSS 2.0 standard requires.

Notice that, in the transform file, the "select" attribute for the<xsl:for-each>element is "MyDataTable". This is the name of the data table in the feed report definition.

<?xml version="1.0" encoding="ISO-8859-1" ?>  
<rss version="**2.0**">  
 <channel>  
<title>**Logi Analytics Support Discussion Forum**</title>   
<link>**https://devnet.logianalytics.com/rdPage.aspx?rdReport=DiscussionForum**</link>   
<description>**Logi Analytics Support Discussion Forum**</description>   
<language>**en-us**</language>   
<webMaster>**DevNet@LogiAnalytics.com**</webMaster>   
<pubDate>**Mon, 16Nov 2015 14:05:00**</pubDate>   
<item>  
<title>**Window Size**</title>   
<link>**https://devnet.logianalytics.com/rdPage.aspx?rdReport=ForumThreadPosts&ThreadID=71102**</link>   
 <description>H**ow can I get the size of a browser windows at runtime?**</description>   
<author>**John Doe**</author>   
 <pubDate>**Thursday, November12, 2015 3:12:01 PM**</pubDate>   
</item>  
</channel>  
</rss>

And, finally, the example above shows the data in the feed file, after the transform has been applied.
These links will lead you to more information about [XPath](http://www.w3schools.com/xml/xml_xpath.asp) and [XSL
Transforms](http://www.w3schools.com/xml/xml_xsl.asp).

![](https://devnet.logianalytics.com/hc/article_attachments/4417575815447/rss_07.png)  

To apply your transform:

1. Create your transform file and, in Studio, add it to the \_SupportFiles folder in your project folder.
2. In your process definition, add an **XSL Transform** element beneath your Target.XML element, as shown above, and set its **XSL Transform File** attribute to the name of your transform file.

Test your task to ensure that it's writing your feed file in the correct *format* and to the correct *location*.

Finally, put your feed icon, with its link to your feed file, in place and you're all set to allow users to get your feed. Work with your browser to see what happens when you access a feed and how your browser deals with subscriptions to it.

## Scheduling Generation of Your Feed File

To update your feed file on a regular basis, you can schedule your taskCreateFeedFile task to run periodically using **Logi Scheduler**. It will overwrite the feed file each time it runs. For complete information about scheduling tasks, see [Logi Scheduler](https://devnet.logianalytics.com/hc/en-us/articles/4406822420503-Logi-Scheduler).
