---
title: "Connecting to Twitter"
id: 4406818150295
section: "Logi Info v12 & Other Products"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406818150295-Connecting-to-Twitter
updated_at: 2022-04-06T06:10:29Z
---

# Connecting to Twitter

# Connecting to Twitter

You will need a Twitter regular account, of course, and you'll also need a Twitter "developer account". Then you'll have to register your Logi application, which is a complicated and time-consuming exercise. At the end of the process, you'll get *four values* from Twitter that you'll use when configuring your connection: Access Token, Access Token Secret, Consumer Key, and Consumer Secret.

Once that's done, you can begin to work in your \_Settings definition with the **Connection.Twitter** element, which manages authentication with, and connection to, Twitter for posting or retrieving data.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583596567/twitter_02.png)

As shown above, the Connection.Twitter element is added beneath the Connections element in the \_Settings definition and its attributes are configured using the four values generated when you registered your application with Twitter.
