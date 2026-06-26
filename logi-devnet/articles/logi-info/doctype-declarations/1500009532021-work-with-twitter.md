---
title: "Work with Twitter"
id: 1500009532021
section: "Doctype Declarations"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009532021-Work-with-Twitter
updated_at: 2021-06-17T01:58:40Z
---

# Work with Twitter

# Work with Twitter

The social networking site **Twitter.com** allows its members to post brief public messages, called "Tweets", and private email-like messages, called "Direct Messages". Elements available in Logi Info allow developers to interact with Twitter in their reports and applications. This topic discusses these interactions
with Twitter.

* About the Twitter API
* [Connect to Twitter](#Connecting)
* [Search for and Retrieving Twitter Posts](#Searching)
* [Post Tweets and Messages](#Posting)

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif)  Twitter updated its API to v1.1 and Logi Info applications built with a version earlier than 11.4.046 will no longer be able to connect to Twitter. You must upgrade in order to restore connectivity.

## About the Twitter API

Logi Info's Twitter-related elements make use of the Twitter v1.1 **REST API**. This is a collection of web service methods that allow the developer to interact with Twitter at a programmatic level. There is no fee or license required to use the API; all that's needed are the credentials for a valid Twitter account and application registration.

The Twitter API is maintained by Twitter and is subject to change. This may affect Logi applications if a new version of the API does not maintain backward-compatibility with earlier versions. For example, this might cause a problem if the names of the data columns returned to a Logi application change. Developers who use the Logi's Twitter-related elements are encouraged to keep abreast of API updates.

Information about the Twitter v1.1 API can be found in Twitter's *[REST APIs Documentation](https://dev.twitter.com/rest/public)*.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif)  In order to manage their resources effectively, Twitter imposes limits on the number and frequency of queries from custom applications. These are described in their *[Rate Limiting](https://dev.twitter.com/rest/public/rate-limiting)* document. Refer to this document to see how these limits may affect you.

## Connect to Twitter

The first thing you need to do is register your application with Twitter at <http://dev.twitter.com/apps>.You need to have a Twitter account to do this, of course, and you'll have to provide some basic information about your application. At the end of the process, you'll get *four values* from Twitter that you'll use when configuring your connection.

Once that's done, you can begin to work in your \_Settings definition with the **Connection.Twitter** element, which manages authentication with, and connection to, Twitter for posting or retrieving data.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771599255/twitter_02.png)

As shown above, the Connection.Twitter element is added beneath the Connections element in the \_Settings definition and its attributes are configured using the four values generated when you registered your application with Twitter.

## Search for and Retrieve Twitter Posts

Once the connection has been configured, interaction with Twitter can occur. First, let's examine how posts can be located and retrieved for use in a Logi application.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771599639/twitter_03.png)

In the example above, a typical report definition is shown, including a data table. A **DataLayer.Twitter** element has been added beneath the table. Its attributes are configured as follows:

1. **Connection ID** - (Required) The ID of the Connection.Twitter element configured in the \_Settings definition.
2. **Search Type** - (Required) This attribute controls which subset of data will be searched. The related pull-down list of options includes: *User's Statuses*, *Friend's Statuses*, *User's Inbox*, *User's Sent Items*, and *Keyword Search*. Keyword Search searches through statuses only, but for *all* users on Twitter, not just the account specified in the connection element.
3. **ID** - A unique element ID.
4. **Keyword** - The word or phrase to be used when Keyword Search has been selected as the Search Type. This value can be parameterized by using a token here, such as @Request.Keyword~. The valid formats and operators that can be used in the keyword are documented in the *[The Twitter Search API](https://dev.twitter.com/rest/public/search)* document.
5. **Maximum Rows** - This attribute limits the number of rows in the result set returned to the datalayer. If left blank, defaults to 100 rows. Any value between 1-100 may be used, but above 100, the values must be in increments of 100.

The number and names of the columns returned into the datalayer will vary depending on the Search Type selected. The API documentation mentioned earlier provides detailed information about this.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771600023/twitter_04.png)

You can, of course, add columns to the data table manually, but this is an excellent opportunity to use the **Add Data Columns Wizard**. To do so, select the Data Table element and click the main menu Wizards tab. Then click the Data Columns icon, as shown above.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778500631/twitter_05.png)

As shown above, the wizard will connect to Twitter and then display a complete list of the result columns available for the specified Search Type, and you'll be able to exclude those you're not interested in seeing.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771600535/twitter_06.png)

The example above shows five of the 30+ columns returned for the Search Type "KeywordSearch".

Once the data has been retrieved into the datalayer, you are then free to manipulate it in any of the usual ways, such as applying filters, conditions, aggregations, etc. or even joining it with other data.

## Post Tweets and Messages

Posting *to* Twitter involves the use of a **Task** in a Process definition:  
![](https://logianalytics.zendesk.com/hc/article_attachments/4402778500887/twitter_07.png)

As shown above, a **Procedure.SendTweet** element is added beneath a **Task** element in the Process definition. Its attributes are set as follows:

1. **Connection ID** - (Required) The ID of the Connection.Twitter element configured in the \_Settings definition.
2. **ID** - (Required) A unique element ID.
3. **Text** - (Required) The actual text to be posted; limited to 140 characters. This value can be parameterized using a token, such as @Request.myText~.
4. **Tweet Type** - (Required) The type of post: either *Tweet* or *Direct Message*.
5. **Screen Name** - The name of the recipient. This attribute is unnecessary when the Tweet Type attribute is set to *Tweet*, but is required when it's set to *Direct Message*. This value can be parameterized using a token, such as @Request.ScreenName~.

Running this task will cause the message to be posted directly to Twitter.com.

The **If Error** element can be used beneath Procedure.SendTweet to capture error messages and send them as a request parameter to a report definition for display.
