---
title: "Authenticating the User"
id: 4419723327383
section: "Manage - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723327383-Authenticating-the-User
updated_at: 2022-07-17T02:22:50Z
---

# Authenticating the User

# Authenticating the User

The first step in providing secure access to the Logi application is to authenticate the user, based on the login. The Security element's **Authentication Source** attribute value governs the behavior of some of the other security-related elements for this step.
When this attribute is set to *AuthNT* or *SecureKey*, the user is authenticated outside of the Logi application and the token @Function.UserName~ is set automatically.

![](https://devnet.logianalytics.com/hc/article_attachments/7522745432343/worklogisec_02.png)

When the attribute is set to *AuthSession* or *Standard*, it may be the Logi application's responsibility to authenticate the user by querying a datasource.
An **Authentication** element, with a child datalayer, as shown above, is used for this purpose. The example above uses a DataLayer.SP element and its child elements to call an SQL database Stored Procedure (SP). The first SP Parameter element is configured, as shown above, to pass the login user name, and the second is configured for the login password, using the token @Request.rdPassword~.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) The two case-sensitive token names, rdUsername and rdPassword, match the IDs of text input controls used in the standard Login page provided with each Logi application, and should also be used as the input control IDs in any *custom* Login page you might
create.
The authenticating stored procedure code should be similar to:

@username varchar(20),  
@passwordvarchar(16)  
SELECT User\_Name, User\_ID FROM UsersTable  
WHERE User\_LoginID = LTRIM(@username) AND User\_Password = LTRIM(@password)

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) Parameters are passed to the SP in the *top-to-bottom order* of the SP Parameter elements and do not take the parameter IDs into account. Your SP should "receive" and define the parameters in the same order.
If the SP returns *no* data, then the user is *not* authenticated. A successful authentication will return two values: the first one will be automatically assigned internally to the token @Function.UserName~ and the second to @Function.UserID~.
For additional flexibility, the Authentication element includes an attribute, **Username Data Column**, that lets you specify the name of the column in the result set that contains the user name.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) Different datalayer elements can be used with the Authentication element, so that users can be authenticated using a variety of datasources. However, we *do not* recommend using **DataLayer.SQL** with direct query text replacement using tokens; it's a possible avenue for "SQL Injection" attacks.
