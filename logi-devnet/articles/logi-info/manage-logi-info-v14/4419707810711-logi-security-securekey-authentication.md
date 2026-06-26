---
title: "Logi Security: SecureKey Authentication "
id: 4419707810711
section: "Manage - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707810711-Logi-Security-SecureKey-Authentication
updated_at: 2023-01-03T07:46:46Z
---

# Logi Security: SecureKey Authentication 

# Logi Security: SecureKey Authentication

This scenario is used when a Logi report or Logi components are integrated into another application. The other ("Parent") application will present the user with a login page or screen and authenticate the user. It then passes the authenticated credentials, and possibly Role and Rights information, to the Logi application. The key point is that the Parent application authenticates the user.

All that remains to be done is to ensure that a user requesting a Logi report is, in fact, the user who's already been authenticated by the Parent application and Logi SecureKey technology accomplishes this.

To use this type of authentication with IIS, your application's Authentication feature should be configured for *Anonymous Authentication*. Then, to configure your Logi Application for this type of authentication:

![](https://devnet.logianalytics.com/hc/article_attachments/7522784668823/logisecsen_12._591x305.png)

1. In your Logi application's \_Settings definition, add a **Security** element, as shown above.
2. Set the **Authentication Source** attribute value to *SecureKey*.
3. Set the **Authentication Client Addresses** attribute value to the IP address of the server hosting the parent application. If both the parent and the Logi applications are on the same server, enter 127.0.0.1 here. Multiple addresses can be entered as a comma-separated list, if necessary.  
     
    Computer names may be used, and IP addresses with wildcard masks. To use wildcards, specify an IP address, the space character, and then the wildcard mask. For example, to allow all addresses in the range of 172.16.\*.\*, specify: 172.16.0.0 0.0.255.255  
     
   Generic information is available about [defining IP wildcard masks](http://en.wikipedia.org/wiki/Wildcard_mask)..
4. Set the **Security Enabled** attribute to *True*.
5. Add other Roles and Rights elements as may be necessary (not shown).

Modify the parent application to interact with the Logi application: see [Configuring the Parent Application](https://devnet.logianalytics.com/hc/en-us/articles/4419723084951-Configuring-the-Parent-Application) for details.

The tokens @Function.UserName~, @Function.UserRoles~, and @Function.UserRights~ can be used to access the data passed from the parent program.

As a debug tool, it's very helpful when developing applications using SecureKey to view the information being sent between the parent application and the Logi application. Test applications, for use in a .NET application only, are available for download from DevNet and help by showing the information in a SecureKey exchange.
