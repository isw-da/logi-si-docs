---
title: "Security Scenarios"
id: 1500009531741
section: "Doctype Declarations"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009531741-Security-Scenarios
updated_at: 2021-06-17T01:58:36Z
---

# Security Scenarios

# Security Scenarios

This topic provides examples of a number of representative security scenarios, from simple to complex, to assist you in understanding how to configure your web server and Logi applications. Scenarios include:

* IIS: Basic Authentication
* [IIS: Digest Authentication for Windows Domain Servers](#Digest)
* [IIS: Integrated Windows Authentication](#Integrated)
* [Logi Security: NT Authentication](#NTAuth)
* [Logi Security: Session Variable Authentication](#Session)
* [Logi Security: Standard Authentication](#Standard)
* [Logi Security: SecureKey Authentication](#SecureKey)

"Logi Security 10" in this topic refers to a modified set of security elements released with **v10.0.189** that make security easier to implement. For information about Logi Security 10, see [Introduction to Logi Security 10](https://devnet.logianalytics.com/hc/en-us/articles/1500009515502-Introduction-to-Logi-Security-10) and [Work with Logi Security 10](https://devnet.logianalytics.com/hc/en-us/articles/1500009516342-Work-with-Logi-Security-10).

"Logi Security 9" refers to the security elements available in earlier releases and, though deprecated in the Logi Security 10 system, they are still supported, for backward compatibility, in Logi v10 products. In Logi v11 products, Logi Security 9 is no longer available. Developers using Logi Security 9 and upgrading to v11 products will have to adopt Logi Security 10.

## IIS: Basic Authentication

This scenario simply configures the web server, IIS 6, to require valid credentials before allowing any access to the Logi application.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif)  User login credentials are sent to the web server in plain text, without any encryption. So anyone attempting to compromise your system security could intercept network messages and examine the unencrypted credentials. This security method is *not* recommended for public networks.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771618839/secscen_01.png)

1. Using the **IIS Manager** utility, select the Virtual Directory for your Logi application, right-click and select **Properties** from the popup menu.
2. Select the **Directory Security** tab.
3. Click the **Edit** button in the Anonymous access and authentication control section.
4. Uncheck the *Anonymous access* checkbox, as shown above.
5. Check the *Basic authentication* checkbox, as shown above, and provide domain and realm information.
6. Click **OK** and **OK** to save your settings and exit the Properties dialog box.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778516503/secscen_02.png)

Now, when the URL for your Logi application is browsed, users will see the dialog box shown above and will have to provide valid credentials for your network domain before seeing the Logi application.

## IIS: Digest Authentication for Windows Domain Servers

This scenario, shown with IIS 6, uses the credentials established in a **Windows Active Directory** domain and validates them before allowing access to the Logi application.

Digest authentication offers the same functionality as Basic authentication; however, Digest authentication provides enhanced security because login credentials are not sent in plain text. Digest authentication encrypts the credentials before sending them across the network.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771619095/secscen_03.png)

1. Using the **IIS Manage**r utility, select the Virtual Directory for your Logi application, right-click and select **Properties** from the popup menu.
2. Select the **Directory Security** tab.
3. Click the **Edit** button in the Anonymous access and authentication control section.
4. Uncheck the *Anonymous access* checkbox, as shown above.
5. Check the *Digest authentication for Windows domain servers* checkbox, as shown above
6. Click **OK** and **OK** to save your settings and exit the Properties dialog box.

Now, when the URL for your Logi application is browsed, users will see the dialog box shown above and will have to provide valid credentials for your network domain before seeing the Logi application.

## IIS: Integrated Windows Authentication

In this scenario, integrated Windows authentication automatically sends the credentials the user used to login to his Windows computer to the Logi application. Formerly called "NTLM" and also referred to as "Windows NT Challenge/Response" authentication, this is a secure form of authentication because the user name and password are hashed before being sent across the network.

To configure IIS 7.x:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771619351/secscen_03a.png)

1. Using the **IIS Manager** utility, select the Virtual Directory for your Logi application.
2. Double-click the Authentication item in the center Properties panel.
3. Select the "Anonymous Authentication" property and click *Disable* in the right-hand Action panel.
4. Select the "Windows Authentication" property and click *Enable* in the right-hand Action panel.

To configure IIS 6:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771619607/secscen_04.png)

1. Using the **IIS Manager** utility, select the Virtual Directory for your Logi application, right-click and select **Properties** from the popup menu.
2. Select the **Directory Security** tab.
3. Click the **Edit** button in the Anonymous access and authentication control section.
4. Uncheck the *Anonymous access* checkbox, as shown above.
5. Check the *Integrated Windows authentication* checkbox, as shown above
6. Click **OK** and **OK** to save your settings and exit the Properties dialog box.

Now, when the URL for your Logi application is browsed, authorized domain users will not see a login dialog box at all; instead they'll proceed directly into the Logi application. Users who are not authorized will be redirect to an error page.

## Logi Security: NT Authentication

"NT Authentication" uses the operating system security scheme as the source of user credentials. In Logi .NET applications using a Windows web server, this is often user data from an Active Directory domain. In Logi Java applications using a Linux/UNIX web server, the source is the Linux/UNIX accounts.

This configuration can also be used when user data comes from an LDAP directory, such as Novell's eDirectory. Special elements, DataLayer.LDAP and DataLayer.LDAP Authentication, were added in v10.0.366 to facilitate use of LDAP.

The following scenario describes configuration of a Windows IIS server:

First, configure your IIS web server to use *Integrated Windows authentication* as described in the previous section.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778516759/secscen_05.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771619863/secscen_05a.png)

1. In your Logi application's \_Settings definition, add a **Security** element, as shown above.
2. Set the **Authentication Source** attribute value to *AuthNT*.
3. Set the **NT Authentication Domain** attribute value to the name of your domain. This value is not case-sensitive and you should not enter any slashes, backslashes, or ".com" here. If authenticating across multiple domains, leave this value blank.
4. Set the **Security Enabled** attribute to *True*.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771620119/secscen_06.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778517015/secscen_06a.png)

5. If using Logi Security 9, add a **UserRoles.NT** element beneath the Security element, as shown above. This element will automatically retrieve the user's Roles (Group) information from the operating system.  
     
   In Logi Security 10, the **Security** element will automatically get the Roles (Group) from the domain, without the need for any other child elements.  
      
     
   ![](https://logianalytics.zendesk.com/hc/article_attachments/4402778517271/secscen_06b.png)

6. If you want to make use of user Rights, several elements are available for retrieving rights. The easiest way to do this when using Logi Security 10 is to add, beneath the Security element, a **User Rights** element and, beneath it, a **Rights From Roles** element, as shown above. This will cause the internal Roles list retrieved by the Security element to be copied to the internal Rights list, as well. For other ways to work with Rights, see [Work with Logi Security 10](https://devnet.logianalytics.com/hc/en-us/articles/1500009516342-Work-with-Logi-Security-10).

Save the application and browse the report. You should be able to access the report and, within the Logi application, work with the domain user login ID using @Function.UserName~, user Roles using @Function.UserRoles~, and user Rights using @Function.UserRights~.

## Logi Security: Session Variable Authentication

This scenario uses a session variable, "rdUsername" that you set in your own custom logon application or process, to hold the user login ID. Logi Security can then use it to authorize access to various Logi reports and data.

First, configure your IIS web server to use whatever authentication is appropriate for your custom logon application or process.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771620375/secscen_07.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771620631/secscen_07a.png)

1. In your Logi application's \_Settings definition, add a **Security** element, as shown above.
2. Set the **Authentication Source** attribute value to *AuthSession*.
3. Set the **Security Enabled** attribute to *True*.
4. Add additional security-related element (Roles, Rights, etc. - not shown) as necessary.

Save the application and browse the report. You should be able to access the report and also see the user's login ID using @Session.rdUsername~.

## Logi Security: Standard Authentication

This scenario presents a logon page when a user browses the Logi application:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771620887/secscen_08.png)

A default logon page, shown above, is provided with your Logi product (the file is rdLogon.aspx, in your Logi application root folder) but developers may substitute their own file. The credentials collected from this logon page can then be validated in the Logi application against your own security database.

If the user is authenticated, one row of data is returned and processing continues; if the user is not authenticated, no data is returned and an error page will be displayed. Developers can substitute their own custom "access denied" page, if desired.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771621143/secscen_09.png)

First, configure your IIS web server to allow *Anonymous access* and ensure that *no* "Authenticated access" options are checked, as shown above.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778517911/secscen_10.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771621399/secscen_10a.png)

1. In your Logi application's \_Settings definition, add a **Security** element, as shown above.
2. Set the **Authentication Source** attribute value to *Standard.*
3. Set the **Security Enabled** attribute to *True*.

### Authenticating Using a SQL Database with Logi Security 10:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif)  Given the potential for a "SQL injection" attack, we recommend that you use a *stored procedure* to authenticate the submitted credentials.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771621783/secscen_11b.png)

4. Add an **Authentication** element beneath the Security element, as shown above.
5. Add a **DataLayer.SP** element beneath it (DataLayer.SQL can be used, but will not be as secure).
6. Set its **Command** attribute value to the name of the stored procedure that will perform the authentication.
7. Set its **Connection ID** attribute value to the ID of a previously configured connection to your security database.  
     
     
   ![](https://logianalytics.zendesk.com/hc/article_attachments/4402771622039/secscen_11c.png)
8. Add an **SP Parameters** and an **SP Parameter** element, as shown above, beneath the datalayer. Set the SP Parameter's attributes as shown. The "dt-200" type designation is for VarChar, other types are available in an option list in the attribute. The @Request.rdUsername~ token contains the username value entered in the standard login page. Custom login pages should take care to preserve the input control IDs
   in their forms.
9. Add a second **SP Parameter** element (not shown) and set it similarly for the password, using @Request.rdPassword~. Remember: tokens are *case-sensitive*!
10. Your authenticating stored procedure should be similar to:

@username   varchar(20),  
@password   varchar(16)

SELECT User\_Name, User\_ID FROM UsersTable  
WHERE User\_LoginID = LTRIM(@username) AND User\_Password = LTRIM(@password)   
  
![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif)  Parameters are passed to the SP in the *top-to-bottom order* of the SP Parameter elements and do not take the parameter IDs into account. Your SP should "receive" and define the parameters in the same order.

If the SP returns *no* data, then the user is *not* authenticated. A successful authentication will return at least one value, which will be automatically assigned internally to the token @Function.UserName~. If a second value is returned, it will be assigned to @Function.UserID~.

### Authenticate Using a SQL Database with Logi Security 9:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771622295/secscen_11.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778518167/secscen_11a.png)

4. Add an **Authentication Rule.SQL** element beneath the Security element, as shown above.
5. Set its **Connection ID** attribute value to the ID of a previously configured connection to your security database.
6. Set its **Source** attribute to a SQL query that tests the login credentials entered, such as:
  

SELECT UserName, UserID FROM UsersTable   
WHERE UserName = 'Request.UserName~' AND (Password='@Request.rdPassword~' OR Password IS NULL)

### Authenticate Using an LDAP Server (v10.0.366+):

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778518423/secscen_13.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778518679/secscen_13a.png)

4. Add an **Authentication** element beneath the Security element, as shown above.
5. Add a **DataLayer.LDAP Authentication** element beneath the Authentication element.
6. Set its **Connection ID** attribute value to the ID of a previously configured Connection.LDAP element.
7. Set its **Password** attribute to the appropriate @Request token.
8. Set its **User DN Source** attribute to an LDAP query that includes the appropriate @Request token and any other LDAP objects and names appropriate to your LDAP server configuration, such as:   
     
   (.NET and Standard LDAP Server)  
    SELECT ADsPath FROM 'OU=Staff, DC=example, DC=com' WHERE uid='@Request.rdUserName~' AND objectClass='InetOrgPerson'  
     
   (.NET and Active Directory Server)  
   SELECT ADsPath FROM 'DC=myCompanyDomain, DC=local' WHERE   
   SamAccountName= '@Request.rdUserName~' AND objectClass='organizationalPerson'  
     
   (Java and Standard LDAP Server)  
    SELECT DN FROM subTreeScope;   
   WHERE uid='@Request.rdUserName~' AND objectClass= 'InetOrgPerson'   
     
   (Java and Active Directory Server)  
   SELECT CN FROM DC=myCompanyDomain, DC=local WHERE   
   SamAccountName='@Request.rdUserName~' AND objectClass='organizationalPerson'

The two @Request tokens shown above are passed from the logon page to the application (and any custom logon page substituted for the standard logon page must do the same, using the reserved words "rdUsername" and "rdPassword").

If the query returns *no* data, then the user is *not* authenticated. A successful authentication will return at least one value: the first one will be automatically assigned internally to the token @Function.UserName~ and, if there's a second one, it will be assigned to @Function.UserID~.

Add other **roles** and **rights** elements as may be necessary (not shown). Save the application and browse the report. Provide valid credentials and you should be able to access the report and also see the user ID using @Function.UserName~ .

## Logi Security: SecureKey Authentication

This scenario is used when Logi reporting is integrated into another application. The other ("parent") application will present the user with a logon page or screen and authenticate the user. It then passes the authenticated credentials, and possibly Role and Rights information, to the Logi application. The key point is that the parent application does the authentication of the user.

All that remains to be done is to ensure that a user requesting a Logi report is, in fact, the user who's already been authenticated by the parent application and the SecureKey mechanism accomplishes this.

First, configure your IIS web server to allow *Anonymous access* and ensure that no authenticated options are selected, as shown in the previous section.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778518935/secscen_12.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771622679/secscen_12a.png)

1. In your Logi application's \_Settings definition, add a **Security** element, as shown above.
2. Set the **Authentication Source** attribute value to *SecureKey*.
3. Set the **Authentication Client Addresses** attribute value to the IP address of the server hosting the parent application. If both the parent and the Logi applications are on the same server, enter 127.0.0.1 here. Multiple addresses can be entered as a comma-separated list, if necessary.
4. Set the **Security Enabled** attribute to *True*.

Modify the parent application to interact with the Logi application: see the section **Configuring a Parent Application** in [Use Logi SecureKey Authentication](https://devnet.logianalytics.com/hc/en-us/articles/1500009515922-Use-Logi-SecureKey-Authentication) for details.

Add other **roles** and **rights** elements as may be necessary (not shown). The tokens @Function.UserName~, @Function.UserRoles~, and @Function.UserRights~ can be used to access the data passed from the parent program.

As a debug tool, it's very helpful when developing applications using SecureKey to view the information being sent between the parent application and the Logi application. A test utility, for use in a .NET environment only, is available for download from DevNet; it displays the SecureKey information in a test exchange: <http://downloads.logianalytics.com/info/TestSecurekey.zip>
