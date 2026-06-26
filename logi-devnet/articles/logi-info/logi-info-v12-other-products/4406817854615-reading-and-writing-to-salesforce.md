---
title: "Reading and Writing to Salesforce"
id: 4406817854615
section: "Logi Info v12 & Other Products"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817854615-Reading-and-Writing-to-Salesforce
updated_at: 2022-04-06T06:08:39Z
---

# Reading and Writing to Salesforce

# Reading and Writing to Salesforce

Beginning with Logi Info v12.2 SP5, it's possible to use Salesforce's REST API to "write back" (Insert, Update, Delete) data to your Salesforce instance. This is a complex development task, however, and requires in-depth knowledge of both Logi Info and Salesforce.

The following discussion of operations using the Salesforce REST API assumes a security model in which a single Salesforce account (the "service" account) will be used to access Salesforce on behalf of all users of your Logi application. This account will require a standard Salesforce User License and should be restricted to limit its interactions to just the Salesforce objects to be modified. *Do not use an Administrator account for this*. You'll need to know the account's Salesforce password
and security token value. Salesforce uses OAuth 2 security, which includes a [Username-Password authentication flow](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_understanding_username_password_oauth_flow.htm) mode, which will be used in this example.

The general steps for developing a Logi application that uses the API are:

1. Register your Logi application as a "Connected App" in Salesforce, and get its "Consumer Key" and "Consumer Secret" values. See [this Salesforce document](https://help.salesforce.com/articleView?id=connected_app_create.htm&language=en_US).&type=0) for more information.
2. You may need to create a Salesforce *Custom Profile* and *Permission Set* for the service account, in order to ensure access to the Salesforce objects you want your Logi application to interact with.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417575544087/connsf_11.png)
3. As shown above, a **Connection.REST** element is used in the \_Settings definition to connect to Salesforce in order to login. ![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) No login credentials are configured in this element.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417563091991/connsf_12.png)
4. In your application's Default report definition, add a **Local Data** element and **DataLayer.REST** to perform the login. Set the Local Data element's Condition attribute to "@Session.SF\_AccessToken~" = ""to ensure that the access token will only be requested once per session (it has a default 4-hour lifetime).   
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417583739031/connsf_13.png)  
     
   An **Http Body** element is used to pass parameters during the login. The **Http Body Params** name-value pairs that need to be passed are shown above. The client\_id and client\_secret parameter values are, respectively, the Consumer Key and Consumer Secret values you noted when you created the Salesforce Connected App. The grant\_type value must be *password*. The password parameter value is the Salesforce service account's password, concatenated with its security token. The username is the account's
   Salesforce login ID.
5. Finally a **Flattener** element, with no attributes set, is used to make the returned values usable as @Local tokens.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417583739159/connsf_14.png)
6. Next, add a **Set Session Variables** element and configure its parameters as shown above. This makes the values returned from a successful login available for later use as session variables.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417563092375/connsf_15.png)
7. Back in the \_Settings definition, add another Connection.REST element, to be used when making requests using the Salesforce REST API. Configure is as shown above, with one of the session variables created in the previous step.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417575544727/connsf_16.png)
8. Add a **Request Header** element beneath the Connection element, as shown above, and configure it as shown, using the second session variable.

## Making Salesforce API Queries

Now we're ready to make a call to the Salesforce REST API, using **DataLayer.REST**, as shown below:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575544983/connsf_17.png)

The Accept Type value is *application/json* once again, and the Http Method this time is *GET*. The Url Path attribute contains the Salesforce Object Query Language (SOQL) query and here's an example:

/services/data/v38.0/query?q=SELECT Id, FirstName, LastName, Email, SuperUser FROM SelfServiceUser WHERE ContactId = '@Request.someID~'

You'll recall that, at execution, the datalayer's Url Path attribute value will be appended to the Connection element's Url Host value to make a complete URL.

Once again, we'll need a **Flattener** element to shape the returned JSON data. In the case of SOQL queries, most of the time we need to tell the Flattener where to begin, by using its Top Level XPath attribute:

![](https://devnet.logianalytics.com/hc/article_attachments/4417583739543/connsf_18.png)

And in most cases, the *records* node, as shown above, is the correct one.

## Writing to Salesforce via the API

Writing to Salesforce is somewhat similar to making queries, in that the same Connection.REST element is used and important information is placed in the URL Path attribute. However, there are some significant differences. The suggested approach is to use Process tasks, and you might think to use the **Procedure.REST** element to call the API.

However, when you make an API call you may want to use data it returns, but the Procedure.REST element is *not* a parent of the Flattener element, so you can't get the returned data into the proper format. The solution to this is to use a **Procedure.Run DataLayer Rows** element with a child DataLayer.REST element.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575545239/connsf_19.png)

As shown above, the configured datalayer's attribute values are similar to those provided in the earlier Query example, except the Http Method is now *POST*. The Url Path is not a SOQL query but a direct reference to a Salesforce object endpoint, in this example, the Case object. This is the way the API expects to receive a command to insert that object.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583739671/connsf_20.png)  

In addition, an **Http Body** child element, configured as shown above, is used to pass the values to be inserted. Here's an example of the JSON data array in the Http Body Content attribute:

{   
"AccountId" : "@Request.Acct\_ID~",  
"Description" : "@Request!Json.hdnDesc~",  
"Product\_\_c" : "Logi Info",  
"Product\_Version\_\_c" : "@Request.inpVersion~",  
"Service\_Pack\_Version\_\_c" : "@Request.inpSPNo~",  
"Subject" : "@Request!Json.inpSubject~"  
}

Note the use of literal and @Request token values. Also, notice the use of the highlighted !Json token modifier. It's used when the data is free-form text and it encodes any special characters, such as double-quotes and line-feeds, so that Salesforce won't reject the Json data stream as invalid.

Once again, a Flattener is used to shape the returned data in the example but, in this case, no Top Level XPath attribute needs to be specified.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) Please remember that the Salesforce API may not enforce referential integrity and therefore it may be up to you to ensure that all related tables are updated and other appropriate actions aretaken for each operation, in order to ensure a complete transaction.
