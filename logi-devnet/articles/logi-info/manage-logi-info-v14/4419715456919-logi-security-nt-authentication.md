---
title: "Logi Security: NT Authentication "
id: 4419715456919
section: "Manage - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715456919-Logi-Security-NT-Authentication
updated_at: 2022-07-17T02:23:33Z
---

# Logi Security: NT Authentication 

# Logi Security: NT Authentication

The **Security** element in the \_Setting definition can be configured to use "NT Authentication" as its authentication source. This mode uses the Windows operating system's security scheme as the source of the user name and security rights and roles. This typically means the user will be authenticated in a Windows Active Directory domain but this mode can also be used when authenticating to other LDAP directories, using these special elements: **DataLayer.LDAP** and **DataLayer.LDAP
Authentication**.

Assuming that your IIS web server has been configured to use *Windows Authentication* as described in [IIS: ASP.NET Impersonation](https://devnet.logianalytics.com/hc/en-us/articles/4419723141399-IIS-ASP-NET-Impersonation-) , here's how to configure your Security element:

![](https://devnet.logianalytics.com/hc/article_attachments/7522768107031/logisecsen_05_536x292.png)

1. In your Logi application's \_Settings definition, add a **Security** element, as shown above.
2. Set the **Authentication Source** attribute value to *AuthNT*.
3. Set the **NT Authentication Domain** attribute value to the name of your domain. This value is not case-sensitive and you should not enter any slashes, backslashes, or ".com" here. If authenticating across multiple domains, leave this value blank.
4. Set the **Security Enabled** attribute to *True*.
  
![](https://devnet.logianalytics.com/hc/article_attachments/7522776452503/logisecsen_06_215x165.png)

5. The **Security** element will automatically get the Roles ("Group") information for the authenticated user from the domain, without the need for any other child elements.   
     
   If you want to make use of user Rights, several elements are available for retrieving rights. The easiest way to do this is to add, beneath the Security element, a **User Rights** element and, beneath it, a **Rights From Roles** element, as shown above. This will cause the internal Roles list retrieved by the Security element to be copied to the internal Rights list. For other ways to work with Rights, see [Working with Logi Security](https://devnet.logianalytics.com/hc/en-us/articles/4419715615255-Working-with-Logi-Security).

Save the application and browse the report. You should be able to access the report and, within the Logi application, work with the user information via tokens: the user login ID will be available as @Function.UserName~, user Roles as @Function.UserRoles~, and user Rights as [@Function.UserRights](mailto:@Function.UserRights)~.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) Windows and other security domains may allow usernames and passwords to contain special characters. However, many of the connection strings used to connect to datasources have reserved characters, usually single- and double-quotes, the equals sign, semi-colons, and commas. When a domain username or password containing these reserved characters is automatically combined into the
connection string, they break it. They can also affect queries, for the same reason. Therefore, domain usernames or passwords that include these reserved characters will cause a failure to connect or an outright error.
