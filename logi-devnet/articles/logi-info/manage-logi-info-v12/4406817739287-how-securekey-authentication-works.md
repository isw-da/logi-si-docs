---
title: "How SecureKey Authentication Works"
id: 4406817739287
section: "Manage - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817739287-How-SecureKey-Authentication-Works
updated_at: 2022-04-06T06:07:54Z
---

# How SecureKey Authentication Works

# How SecureKey Authentication Works

Generally, there are four steps involved in the typical SecureKey Authentication transaction. In the following example scenario, a Logi application is embedded in an iFrame within its Parent application.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563143575/securekey_01_525x196.png)

1. The Parent application initially authenticates the user (the "single sign-on"), as shown above. The user successfully logs into the Parent application; the exact method it uses to determine that a user is valid is irrelevant to this process, except that user Roles and/or Rights, if applicable, should be retrieved as part of the authentication.  
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417563143703/securekey_02_521x254.png)

2. After the Parent application authenticates the user, the page that includes the embedded Logi application loads, as shown above. The Parent application sends the Logi application a request for a SecureKey token. The request includes the user ID, any user Roles and/or Rights, and (pre-v12.1.188) the user's machine IP address (the "client browser IP address").  
     
   When it receives the request for a SecureKey token, the Logi application first verifies that the request came from a valid source. This is done by automatically determining the Parent app's *server* IP address and ensuring that it's in a pre-configured list of approved addresses. If so, the Logi application stores the user information from the request and returns a unique SecureKey token to the Parent application.   
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417563143959/securekey_03_526x275.png)
3. The Parent application then sends the original report request to the Logi application, appending the SecureKey token.   
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417563144215/securekey_04_496x238.png)
4. Upon receiving the request, the Logi application automatically determines the client browser IP address and uses it, along with the SecureKey token, to authenticate the request. If authenticated, a session is started for the user and any Roles and Rights (stored in Step #2) associated with the token are used to authorize access to the correct reports, data, and other resources. The requested report is then generated and returned into the iFrame.

When the Logi application session is started for the user, *the SecureKey token**expires* and cannot be used again. Any subsequent reports requested from within the context of the Logi application will use the user's session to control access to reports, data, and resources. The user is then communicating directly from his or her browser to the Logi application for reports and the Parent application is no longer involved, as long as the Logi app session persists.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png)Developers need to ensure that the Parent application *does not* try to reuse the expired SecureKey token!

If the user's Logi application session ends, and he or she subsequently wants to access reports again, then the process of requesting and using a new SecureKey token will have to be repeated.

Once a SecureKey token is used, it cannot be used again in a different session, and "sharing" tokens across clients isn't possible, as the client browser IP address is referenced within
the key when it's created, making it valid *only* for the client that made the initial request.

## SecureKey Information Storage

Normally, the information associated with a SecureKey token (User Name, Roles, Rights, browser IP address, etc.) is stored as a web server "application scope" variable.

However, if you're using a clustered server configuration, you can specify a physical folder for temporary storage of SecureKey information as XML files. Using a shared network folder for this purpose allows common access to the SecureKey information by the clustered servers. This shared folder is specified in the **SecureKey Shared Folder** attribute of the Security element, in the Logi application's \_Settings definition. The SecureKey files created by this option are deleted whenever the automatic "temporary
cache file clean-up" occurs (which is configurable - see [Temporary Cache File Management](https://devnet.logianalytics.com/hc/en-us/articles/4406817871127-Temporary-Cache-File-Management)).
