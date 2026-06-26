---
title: "Work with Twitter"
id: 4419707998487
section: "Logi Info v14 & Other Products"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707998487-Work-with-Twitter
updated_at: 2022-07-17T02:05:15Z
---

# Work with Twitter

# Work with Twitter

The social networking site **Twitter.com** allows its members to post brief public messages ("Tweets") and private email-like messages ("Direct Messages"). Elements available in Logi Info allow developers to interact with Twitter in their reports and applications.

The following topics discuss these interactions
with Twitter:

* [Connecting to Twitter](https://devnet.logianalytics.com/hc/en-us/articles/4419707997463-Connecting-to-Twitter#Connecting)
* [Searching for and Retrieving Twitter Posts](https://devnet.logianalytics.com/hc/en-us/articles/4419723346199-Searching-for-and-Retrieving-Twitter-Posts#Searching)
* [Posting Tweets and Messages](https://devnet.logianalytics.com/hc/en-us/articles/4419723345303-Posting-Tweets-and-Messages#Posting)

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) Twitter updated its API to v1.1 and Logi Info applications built with a version earlier than 11.4.046 will no longer be able to connect to Twitter. You must upgrade in order to restore connectivity.

## About the Twitter API

Logi Info's Twitter-related elements make use of the Twitter v1.1 REST API. This is a collection of web service methods that allow the developer to interact with Twitter at a programmatic level. There is no fee or license required to use the "Standard" API; all that's needed are the credentials for a valid Twitter account and application registration. More functionality is available, using other levels of the API, for a fee. There are also several different Twitter APIs available, depending on what
you want to do.

The Twitter API is maintained by Twitter and is subject to change. This may affect Logi applications if a new version of the API does not maintain backward-compatibility with earlier versions. For example, this might cause a problem if the names of the data columns returned to a Logi application change. Developers who use the Logi's Twitter-related elements are encouraged to keep abreast of API updates.

Information about the Twitter v1.1 API can be found in Twitter's *[API Documentation](https://dev.twitter.com/rest/public)*.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) In order to manage their resources effectively, Twitter imposes limits on the number and frequency of queries from custom applications, as described in *[Rate Limiting](https://dev.twitter.com/rest/public/rate-limiting)*. Refer to this document to see how these limits may affect you.
