---
title: "Logi Security: Standard Authentication "
id: 4419723143447
section: "Manage - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723143447-Logi-Security-Standard-Authentication
updated_at: 2023-07-19T04:21:03Z
---

# Logi Security: Standard Authentication 

# Logi Security: Standard Authentication

In this scenario, user data is stored in your own custom database and your Logi application validates the user against it.

![](https://devnet.logianalytics.com/hc/article_attachments/7522784606999/logisecsen_08_254x153.png)

Logi Info includes a default login page that includes the login form shown above (its appearance will vary slightly depending on the Theme used). This is the file rdLogon.aspx, in your Logi application root folder. You can substitute your own custom login page, as long as you submit user input controls with the *same names* as those in the default page.

After the login page is submitted, your Logi application handles validating the user against your security database. If the user is authenticated, the query should return one row of data and processing continues; if the user is not authenticated, no data should be returned and an error page will be displayed. A default "Access Denied" page is supplied but you can customize that, too, if desired.

To use this type of authentication with IIS, your application's Authentication feature should be configured for *Anonymous Authentication*. Then, to configure your Logi Application for this type of authentication:

![](https://devnet.logianalytics.com/hc/article_attachments/7522768041751/logisecsen_09_598x325.png)

1. In your Logi application's \_Settings definition, add a **Security** element, as shown above.
2. Set the **Authentication Source** attribute value to *Standard.*
3. Set the **Security Enabled** attribute to *True*.

The following sections discuss the subsequent steps you'll need to take when using SQL and LDAP authentication methods.

## Authenticating Using a SQL Database

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) Given the potential for a "SQL injection" attack, we highly recommend that you use a *Stored Procedure* to authenticate the submitted credentials.

![](https://devnet.logianalytics.com/hc/article_attachments/7522804073495/logisecsen_10_635x194.png)

4. Add an **Authentication** element beneath the Security element, as shown above.
5. Add a **DataLayer.SP** element beneath it and configure it appropriately.
6. Add an **SP Parameters** and an **SP Parameter** element, as shown above, beneath the datalayer. Set the SP Parameter's attributes as shown. The "dt-200" type designation is for VarChar, other types are available in an option list in the attribute. The @Request.rdUsername~ token contains the username value entered in the standard Login page. Custom login pages should take care to preserve the input control IDs
   in their forms.
7. Add a second **SP Parameter** element (not shown) and set it similarly for the password, using @Request.rdPassword~. Remember: tokens are *case-sensitive*!
8. Your authenticating Stored Procedure should be similar to:  
     
   @username varchar(20),  
   @passwordvarchar(16)  
   SELECT User\_Name, User\_ID FROM UsersTable  
   WHERE User\_LoginID = LTRIM(RTRIM(@username)) AND User\_Password = LTRIM(RTRIM(@password))  
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) Parameters are passed to the SP in the *top-to-bottom order* of the SP Parameter elements and do not take the parameter IDs into account. Your SP should "receive" and define the parameters in the same order.

9. Add other Roles and Rights elements as may be necessary (not shown).

If the SP returns *no* data, then the user is *not* authenticated. A successful authentication will return at least one value, which will be automatically assigned internally to the token @Function.UserName~. If a second value is returned, it will be assigned to @Function.UserID~.

## Authenticating Using an LDAP Server

![](https://devnet.logianalytics.com/hc/article_attachments/7522776402583/logisecsen_11_638x160.png)

4. Add an **Authentication** element beneath the Security element, as shown above.
5. Add a **DataLayer.LDAP Authentication** element beneath the Authentication element.
6. Set its **Connection ID** attribute value to the ID of a previously configured Connection.LDAP element.
7. Set its **Password** attribute to the appropriate @Request token from the Login page.
8. Set its **User DN Source** attribute to an LDAP query that includes the appropriate @Request token and any other LDAP objects and names appropriate to your LDAP server configuration, such as:   
     
   (.NET and Standard LDAP Server)  
    SELECT ADsPath FROM 'OU=Staff, DC=example, DC=com' WHERE uid='@Request.rdUserame~' AND objectClass='InetOrgPerson'  
     
   (.NET and Active Directory Server)  
   SELECT ADsPath FROM 'DC=myCompanyDomain, DC=local' WHERE   
   SamAccountName= '@Request.rdUserame~' AND objectClass='organizationalPerson'  
     
   (Java and Standard LDAP Server)  
    SELECT DN FROM subTreeScope;   
   WHERE uid='@Request.rdUserame~' AND objectClass= 'InetOrgPerson'   
     
   (Java and Active Directory Server)  
   SELECT CN FROM DC=myCompanyDomain, DC=local WHERE   
   SamAccountName='@Request.rdUserame~' AND objectClass='organizationalPerson'

9. Add other Roles and Rights elements as may be necessary (not shown).

The two @Request tokens mentioned above are passed from the Login page to the application, and any custom logon page substituted for the standard logon page must do the same, using the reserved words "rdUsername" and "rdPassword".

If the query returns *no* data, then the user is *not* authenticated. A successful authentication will return at least one value: the first one will be automatically assigned internally to the token @Function.UserName~ and, if there's a second one, it will be assigned to @Function.UserID~.
