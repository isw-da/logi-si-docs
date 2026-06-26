---
title: "The Security Element"
id: 4406818122519
section: "Manage - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406818122519-The-Security-Element
updated_at: 2022-04-06T06:10:19Z
---

# The Security Element

# The Security Element

Logi Security is built around the **Security** element, which is added into a Logi application's \_Settings definition. It's the container element for all other globally-configured security elements and handles both *authentication* and *authorization*.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562951959/worklogisec_01.png)

The Security element, shown in the example above, has a **Security Enabled** attribute, which enables and disables Logi Security. The element's other attributes include:

| Attribute | Description |
| --- | --- |
| Authentication Source | (Required) Specifies how the Logi Server gets its authentication information. Choices include: *AuthNT* - In Logi .NET applications, uses Windows OS security to get the information. This must also be enabled in the IIS web server by disabling "Anonymous Authentication" and enabling "Windows Authentication" for the application. Does not apply for Java applications. *AuthSession* - Uses a session variable, *rdUsername*, that's set in a custom logon process. *Standard* - Causes Logi application to display a form-based logon page. The supplied default logon page, *rdLogon.aspx*, or a custom page based on it, can be used. *SecureKey* - User information passed from another application, using a secure key token. For more information, see [Logi SecureKey Authentication](https://devnet.logianalytics.com/hc/en-us/articles/4406822454807-Logi-SecureKey-Authentication). |
| Access Denied Page | Specifies a custom page that users will be redirected to if they attempt to access a report that they're *not authorized* to access. If left blank, a standard error page distributed with Logi Info will be used. Custom error pages should be an .aspx file, placed in the Logi application folder. |
| Authentication Client Addresses | (Required if the Authentication Source is set to *SecureKey)* Specifies a comma-separated list of one or more IP addresses for approved external applications that will be requesting keys under Logi SecureKey Authentication. Computer names may be used, and IP addresses with wildcard masks. To use wildcards, specify an IP address, the space character, then the wildcard mask. For example, to allow all addresses in the range of 172.16.\*.\*,  specify: 172.16.0.0 0.0.255.255  Generic information is available about [defining IP wildcard masks](http://en.wikipedia.org/wiki/Wildcard_mask). |
| Cache Roles and Rights | Specifies *when* a user's Roles and Rights are retrieved. Selecting *Session* causes this to occur only once, at session start. If left blank or set to *False*, Roles and Rights are retrieved with *every* request. Must be set to *Session* if SecureKey authentication source is selected. |
| Development Client Addresses | *Provides special functionality for testing during development*. Specifies a comma-separated list of one or more IP addresses, with a default value of *127.0.0.1*. (IPv6 addresses, such as ::1, are also supported). If a user browses the application from one of the IP addresses in the list, then the internal security username is automatically set to the value of the Development Username attribute, and the "usual" security is bypassed. |
| Development Username | *Provides special functionality for testing during development*. Specifies a default user name value if a user browses the application from one of the IP addresses specified in the Development Client Addresses attribute. Let's developers avoid repetitive log-ins when testing. |
| Logon Fail Page | Specifies the page that users will be redirected to if logon fails. If left blank and a *Standard* authentication source is selected, a default page, *rdLogon.aspx* is used. A custom page named here should be an .aspx file, placed in the Logi application folder. |
| Logon Page | Specifies the page displayed at logon when a *Standard* authentication source is selected. If left blank, a default page, *rdLogon.aspx*, is used. Custom logon pages can be created by copying and renaming the default logon page and placing them in the Logi application folder. |
| Metadata Admin Security Right IDs | Specifies a comma-separated list of Security Right IDs that will be granted access to the Web Metadata Builder, see [Web Metadata Builder](https://devnet.logianalytics.com/hc/en-us/articles/4406817979799-Web-Metadata-Builder). The default value is *rdMetadataAdmin*. To grant access to the Web Metadata Builder, either give users the rdMetadataAdmin security Right, or set this attribute to an existing administrator security Right. |
| NT Authentication Domain | Specifies the Windows domain that will be authenticating users when an *AuthNT* authentication source is selected. The application will then *only* accept users authenticated in that domain. To authenticate users from multiple domains, leave this attribute value blank. |
| Restart Session | When using a *SecureKey* authentication source and set to *True*, this attribute causes almost all session variables to be cleared at the start of each attempted login (the exceptions are several Logi system variables). This feature allows a single browser instance to access the same Logi application and use different credentials and sessions from different browser tabs. Default value: *False.* |
| Scheduler Username | When using an *AuthSession* or *Standard* authentication source, specifies the name of the user account that will be used to run scheduled Logi processes. |
| SecureKey Database Connection ID | Specifies a database Connection element ID, enabling the temporary storage of SecureKeys in a relational database rather than in the file system. The temporary values are stored in a database table named *rdSecureKey*, which is automatically created the first time a SecureKey is used. Supported databases are:  * SQL Server * Oracle * MySQL * PostgreSQL |
| SecureKey Sessionless | When using a SecureKey authentication source and set to *True*, this attribute causes SecureKeys to be stored in the application data cache folder (by default, rdDataCache) instead of in Session state. These files expire and get cleaned-up automatically if no requests for them are made during the Session timeout period. Setting this attribute to True is especially important when securing access to Data definitions to retrieve JSON data because such requests are sessionless. |
| SecureKey Shared  Folder | This attribute is functional only when using a SecureKey authentication source and clustered web farm or web garden configurations. In a single-server configuration, SecureKey keeps SecureKey requests in Application state. With multiple servers, this information must be stored in files in the folder specified by this attribute, which is shared among the web servers. The account used by (or impersonated by) the web application must have network access rights to read, write and delete files from this folder. Set this attribute value to UNC network path, such as: //mySharedServer/SecureKeyFolder Older files in the SecureKeyFolder are automatically deleted over time, so do not use this folder to store other files. |
| Security Enabled | Enables or disables Logi Security. The default value is *False*. |

  

## Bypassing Security During Development

Adding security to a Logi application complicates the development process, as security will be applied when you Preview a report in Studio or run a wizard. In order to make life a little easier for developers, two special Security element attributes can be used to disable, or apply special, security settings while developing and testing an application. These are the **Development Client Address** and **Development Username** attributes, described in the table above.
