---
title: "Configuring SecureKey in a Logi Application"
id: 4419715418135
section: "Manage - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715418135-Configuring-SecureKey-in-a-Logi-Application
updated_at: 2022-07-17T02:23:50Z
---

# Configuring SecureKey in a Logi Application

# Configuring SecureKey in a Logi Application

Implementing SecureKey Authentication in a Logi application builds upon existing techniques for implementing **Logi Security**.

![](https://devnet.logianalytics.com/hc/article_attachments/7522807408279/securekey_06_614x339.png)

In the example shown above, a **Security** element has been added to the application's \_Settings definition and configured with typical settings for a SecureKey implementation. The relevant attributes are:

| Attribute | Description |
| --- | --- |
| Authentication Source | (Required) Select *SecureKey* from the drop-down list of available values. |
| Authentication Client Addresses | Specifies the **IP address** of the web/application *server* making the SecureKey requests (*not* the end-user's IP address), identified as the "Parent App Server" in the first four images above. This value can be determined by "pinging" the application server from the web server hosting your Logi applications. If one computer serves both purposes and the Logi apps are being called using *localhost* in the URL, enter 127.0.0.1 for this value (or ::1 in IPv6). If multiple servers will be making SecureKey requests, multiple IP addresses can be entered here, separated by commas. Computer names may be used, and IP addresses with wildcard masks. To use wildcards, specify an IP address, the space character, then the wildcard mask.  For example, to allow all addresses in the range of 172.16.\*.\*, specify: 172.16.0.0 0.0.255.255  We do not recommend using partial wildcard masks; however, if this set up is absolutely required, you can provide a partial mask as long as the mask value is larger than the IP value. See below for an example. Generic information is available about [defining IP address wildcard masks](http://en.wikipedia.org/wiki/Wildcard_mask). SecureKey requests from servers with IP addresses *not* in this Authentication Client Addresses list are *rejected*. |
| Cache Roles and Rights | When Authentication Source is set to *SecureKey* and this value is left blank, the setting defaults to *Session*; SecureKey will not work if it's set to *False*. |
| Restart Session | When set to *True*, all security-related session variables are cleared with each new login attempt. This prevents session variables that were established during one user's session from being used during a subsequent user's session. |
| SecureKey Database Connection ID | Specifies a database Connection element ID, enabling the temporary storage of SecureKey tokens in a relational database rather than in the file system. The temporary values are stored in a database table named *rdSecureKey*, which is automatically created the first time a SecureKey is used. See [this section](#DBStorage) below for more information. |
| SecureKey Shared Folder | As discussed earlier, this attribute allows SecureKey to be used with **clustered server configurations** in web farms and web gardens by saving information in commonly-accessible files. The account used by (or impersonated by) the Logi application must have network access rights to read, write, and delete files in this folder. Set the SecureKey Shared Folder value to a network path, such as: //mySharedServer/SecureKeyFolder. Files in the SecureKey shared folder are automatically deleted over time, so do not use this folder to also store other files. If using this attribute for development diagnostics, enter a fully-qualified path on the web server. You can use the @Function.AppPhysicalPath~ token here as part of the path. |
| Security Enabled | Must be set to *True* to enable security. |

## About IP Addresses

Due to the stateless nature of browser interactions, IP addresses play an important role in ensuring security. Developers are occasionally confused about the two IP addresses used with SecureKey authentication, so here's some additional explanation:

## Authentication Client Address

This address ensures that the Parent application and the Logi application are allowed to talk to one another. It's the IP address of the *server* hosting the Parent application. It is *not* the IP address of the end-user computer used to request reports through the Parent application.

Computer names may be used, and IP addresses with wildcard masks. To use
wildcards, specify an IP address, the space character, then the
wildcard mask. For example, to allow all addresses in the range of
172.16.\*.\*, specify: 172.16.0.0 0.0.255.255.

This address is *never* passed in a URL when requesting a SecureKey from the Logi application. Instead, the Logi application automatically determines the address of incoming SecureKey requests from the Parent application and, if it matches one of the IP addresses specified in the Security element's Authentication Client Address attribute, then the Logi application will accept and begin processing the SecureKey request.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) We do not recommend using partial wildcard masks; however, if this set up is absolutely required, you can provide a partial mask as long as the mask value is larger than the IP value. For example:

10.158.48.128 0.0.0.218 will work, but

10.158.48.128 0.0.0.105 will not work.

## Client Browser Address

This address is used to verify that each report request to the Logi application is coming from a source that has been authenticated by the Parent application. It's the IP address of the *end-user computer* used to request reports through the Parent application. It is *not* the IP address of the *server* hosting the Parent application.

This address *is* passed in the URL of every request for a SecureKey. It should *not* be specified in the Security element's Authentication Client Address attribute. The Logi application automatically determines the address of incoming report requests and, if it matches the IP addresses associated with the specified SecureKey, access to the Logi application is allowed.

This query string value is no longer required.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) During development, it's not at all unusual for the Parent application to be hosted by a web server that's on the same machine as the browser used to make test requests. In this case, the Authentication Client Address and the Client Browser Address are very likely going to be the *same*, such as 127.0.0.1 or ::1. This can contribute to the confusion over these two addresses, and perhaps
produce
a rude surprise when the applications are deployed and the addresses change. We highly recommend testing SecureKey implementations using a separate machine to represent the
"end-user machine"
in order to avoid this confusion.

## Storing SecureKeys in a Database

In clustered environments, the SecureKey Shared Folder is usually used to store 
SecureKeys so that all computers in the cluster are aware of
them. It's also possible to store them instead in a database table, for additional security and to get the file system out of the process. The Security element's **SecureKey Database Connection ID** attribute is used to enable the feature and to provide a connection to the database, which must be on one of these supported database servers:

* MS SQL Server
* MySQL
* Oracle
* PostgreSQL

The table, *rdSecureKey*, is automatically created in the database when the feature is enabled and the first SecureKey request is received. SQL scripts for creating the table are also available in *<applicationFolder>*\rdTemplate\rdSecureKey. Temporary SecureKey records, like the temporary files in the file system, are automatically deleted from the table after they expire.

Do not set the **SecureKey Sessionless** attribute to *True* when enabling this feature; an error will result.
