---
title: "Session Authentication for Single Sign On"
id: 360047844853
section: "Tactics"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/360047844853-Session-Authentication-for-Single-Sign-On
updated_at: 2023-08-22T15:33:55Z
---

# Session Authentication for Single Sign On

**What is Session Authentication?**

Session authentication provides a Single Sign-on(SSO) method, which allows for custom handling of authentication logic.

**Session authentication is used when:**

1. A developer wants to reuse existing OAuth, SAML, or other existing token-based authentication from the Parent application
2. Logi Securekey does not work in the environment due to
   * IP range limitation
   * Distributed, cloud-based architecture
3. Complex management of user state. e.g. to synchronize access permissions with parent application's access permissions on every report load

**How Does it work:**

Before a session starts, custom code processes authentication logic and provides an intrinsically trusted session parameter "rdUsername" to start the Info session.

Add front-facing logic (e.g. myLogin.aspx) that sets up rdUsername as a session parameter before passing to the Info application’s entry-point (rdPage.aspx).![mceclip0.png](https://devnet.logianalytics.com/hc/article_attachments/360069831613/mceclip0.png)

Additional information (e.g. UserRoles, UserRights, TenantID, etc.) can be set to session parameters in front-facing logic. This can be accessed in the application as Session tokens, e.g. @Session.TenantID~.

More information: <https://devnet.logianalytics.com/rdPage.aspx?rdReport=Article&dnDocID=2165&dnProd=2#Session>

**Implementation**

1. Create a front-end authentication solution.

Sample myLogin.jsp with in-line scriptlet:![mceclip2.png](https://devnet.logianalytics.com/hc/article_attachments/360069835353/mceclip2.png)2. Set the Security Authentication attribute of the Security element in the Logi Info application to 'AuthSession'.

3. Set the Logon Page attribute to the front-facing authentication page

4. Set the Logon Fail Page to redirect to a friendly error page or a page that handles failed authentication

```
  <Security  
 AuthenticationSource="AuthSession"  
 LogonFailPage="https://parentapp.com/login"  
 LogonPage="myLogin.jsp"  
 SecurityEnabled="True"  
 />
```
