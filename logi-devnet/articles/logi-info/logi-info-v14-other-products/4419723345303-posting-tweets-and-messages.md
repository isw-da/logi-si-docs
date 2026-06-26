---
title: "Posting Tweets and Messages"
id: 4419723345303
section: "Logi Info v14 & Other Products"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723345303-Posting-Tweets-and-Messages
updated_at: 2022-07-17T01:26:11Z
---

# Posting Tweets and Messages

# Posting Tweets and Messages

Posting *to* Twitter involves the use of a **Task** in a Process definition:

![](https://devnet.logianalytics.com/hc/article_attachments/4419707215895/twitter_07.png)

As shown above, a **Procedure.SendTweet** element is added beneath a **Task** element in the Process definition. Its attributes are set as follows:

1. **Connection ID** - (Required) The ID of the Connection.Twitter element configured in the \_Settings definition.
2. **ID** - (Required) A unique element ID.
3. **Text** - (Required) The actual text to be posted; limited to 140 characters. This value can be parameterized using a token, such as @Request.myText~.
4. **Tweet Type** - (Required) The type of post: either *Tweet* or *Direct Message*.
5. **Screen Name** - The name of the recipient. This attribute is unnecessary when the Tweet Type attribute is set to *Tweet*, but is required when it's set to *Direct Message*. This value can be parameterized using a token, such as @Request.ScreenName~.

Running this task will cause the message to be posted directly to Twitter.com.

The **If Error** element can be used beneath Procedure.SendTweet to capture error messages and send them as a request parameter to a report definition for display.
