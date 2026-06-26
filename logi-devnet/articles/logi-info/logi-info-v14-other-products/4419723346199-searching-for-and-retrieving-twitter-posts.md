---
title: "Searching for and Retrieving Twitter Posts"
id: 4419723346199
section: "Logi Info v14 & Other Products"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723346199-Searching-for-and-Retrieving-Twitter-Posts
updated_at: 2022-07-17T02:22:45Z
---

# Searching for and Retrieving Twitter Posts

# Searching for and Retrieving Twitter Posts

Once the connection has been configured, interaction with Twitter can occur. First, let's examine how posts can be located and retrieved for use in a Logi application.

![](https://devnet.logianalytics.com/hc/article_attachments/7522730839319/twitter_03.png)

In the example above, a typical report definition is shown, including a Data Table. A **DataLayer.Twitter** element has been added beneath the table. Its attributes are configured as follows:

1. **Connection ID** - (Required) The ID of the Connection.Twitter element configured in the \_Settings definition.
2. **Search Type** - (Required) This attribute controls which subset of data will be searched. The related pull-down list of options includes: *User's Statuses*, *Friend's Statuses*, *User's Inbox*, *User's Sent Items*, and *Keyword Search*. Keyword Search searches through statuses only, but for *all* users on Twitter, not just the account specified in the connection element.
3. **ID** - A unique element ID.
4. **Keyword** - The word or phrase to be used when Keyword Search has been selected as the Search Type. This value can be parameterized by using a token here, such as @Request.Keyword~. The valid formats and operators that can be used in the keyword are documented in the Twitter *[Search Tweets API](https://developer.twitter.com/en/docs/tweets/search/overview)* document.
5. **Maximum Rows** - This attribute limits the number of rows in the result set returned to the datalayer. If left blank, defaults to 100 rows. Any value between 1-100 may be used, but above 100, the values must be in increments of 100.

The number and names of the columns returned into the datalayer will vary depending on the Search Type selected. The API documentation mentioned earlier provides detailed information about this.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725336855/twitter_04.png)

You can, of course, add columns to the Data Table manually, but this is an excellent opportunity to use the **Add Data Columns Wizard**. To do so, select the Data Table element and click the main menu Wizards tab. Then click the Data Columns icon, as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/7522717131799/twitter_05.png)

As shown above, the wizard will connect to Twitter and then display a complete list of the result columns available for the specified Search Type, and you'll be able to exclude those you're not interested in seeing.

![](https://devnet.logianalytics.com/hc/article_attachments/7522717139223/twitter_06.png)

The example above shows five of the 30+ columns returned for the Search Type "KeywordSearch".

Once the data has been retrieved into the datalayer, you are then free to manipulate it in any of the usual ways, such as applying filters, conditions, aggregations, etc. or even joining it with other data.
