---
title: "Setting the Same-site Cookie attribute for embedded Logi Info Apps"
id: 4410287590679
section: "Best Practices"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4410287590679-Setting-the-Same-site-Cookie-attribute-for-embedded-Logi-Info-Apps
updated_at: 2023-10-26T16:45:54Z
---

# Setting the Same-site Cookie attribute for embedded Logi Info Apps

**Background on sameSite Cookie attribute and Logi Info**  
  
The SameSite cookie attribute clarifies access rights for your application and its underlying cookies. More information regarding this attribute and cookies, in general, can be found in the following article: <https://web.dev/samesite-cookies-explained/>.

This attribute can cause an issue if an application is embedded in other web applications using an iframe, including the EmbeddedAPI, and the Logi application URL is from a different domain than the parent application.

In 2020 Microsoft began rolling out a change to the default SameSite cookie behavior under IIS. With this change, if the SameSite attribute has not been set, the attribute will be passed as ‘Lax’, instead of the previous default of ‘None’.

Depending on how the SameSite cookie attribute is set under the Logi web application, and how the web browser enforces policies for the SameSite cookie attribute, cookies may not persist in the browser for the Logi web application. Most notably, this can prevent the Session cookie, ASP.NET\_SessionId in a .Net application, from being retained in the browser, causing a loss of session state, including authentication for the embedded application.

If the Logi application is using SecureKey, then any request to the server may result in the following error:

***“Unable to authenticate the user. Missing rdSecureKey parameter.”***

If you are not using SecureKey authentication, your error message(s) may be different.

For current browser and server behavior regarding the SameSite cookie attribute, setting the Logi application cookies with **SameSite=”None”** will revert to the previous behavior. This change can be made in the web.config of the Logi Info application.

### Resolving Errors related to the sameSite cookie attribute

To set the SameSite attribute for the Session cookie, add the attribute **cookieSameSite="None"** on the sessionState element inside the <system.web></system.web> tag. If you are not currently using a sessionState element, we would recommend using one of the commented-out versions in the web.config file, like the one below.  The other attributes in the sessionState element should be configured for your deployment scenario.

```
<sessionState mode="InProc" cookieless="false" cookieSameSite="None" />
```

For all other cookies, add the attribute **sameSite="None"** on the httpCookies element. The Logi web.config may already have this element, if it does not, it can be added immediately after the sessionState element, inside the <system.web></system.web> tag.

```
<httpCookies sameSite="None" httpOnlyCookies="true" requireSSL="true"
```

If you experience these symptoms in your embedded application and changes to the web.config do not resolve the issue, please reach out to Logi Support so we may assist in further identifying the configuration for your specific implementation scenario.
