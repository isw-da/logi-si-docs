---
title: "JavaScript API: Proxy Incoming Requests"
id: 5281609005079
section: "JavaScript API"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281609005079-JavaScript-API-Proxy-Incoming-Requests
updated_at: 2022-05-03T22:07:54Z
---

# JavaScript API: Proxy Incoming Requests

# JavaScript API: Proxy Incoming Requests

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> As of *v2018.1*, this is no longer necessary. Use **[Cookieless Sessions](https://devnet.logianalytics.com/hc/en-us/articles/5281619580311-Cross-Origin-Embedding-of-Exago-BI#Cookiele)** instead.

It can be tricky to serve content from different domains as part of the same web page. To protect against malicious scripts, web browsers enforce a **same-origin policy** whereby scripts have permission to access only data from the same origin (domain and port number). Websites that violate the same-origin policy are said to be engaging in **cross-site scripting** (XSS). Such websites will not function properly in modern web browsers.

A common integration of Exago BI into a host application is to separate the installation of Exago onto its own web server. API calls between the host app and Exago are communicated via a **web service**.

When embedding Exago content into a host web page, iFrames work around the same-origin policy because the iFrame barrier effectively isolates the embedded page from the surrounding content. No scripts can cross the barrier in either direction.

However, when using the Exago [JavaScript API](https://devnet.logianalytics.com/hc/en-us/articles/5281628892055-JavaScript-API) to embed content directly in the host DOM, browsers will complain if the embedded content is thought to be coming from a different domain than the host. One way to work around this restriction is to use the host web server as a **proxy server**. The host can be configured as the entry point for requests to Exago, which it then redirects to the Exago server. This is known as a **reverse proxy**.

This setup can have some security advantages—all external calls are routed through the host server, thus preventing potential attackers from being able to access the Exago server directly. Exago can be hidden behind a firewall and requests filtered based on their content.

The following sections explain how you might set up this configuration.

## Configure the Host Server

The host server application should be configured as follows:

### IIS

First ensure that the [**Application Request Routing**](https://www.iis.net/downloads/microsoft/application-request-routing) extension is installed.

#### Enable Proxy

1. In IIS select the web server then open **Application Request Routing Cache**.
2. Click **Server Proxy Settings**
3. Select **Enable proxy** then click **Apply**.

#### Set up URL Rewrite

1. In IIS select the **Default Web Site**then open **URL Rewrite**.
2. For both the web application and web service do the following:
   1. Click **Add Rule(s)**
   2. Select **Reverse Proxy** then click OK.
   3. Enter the Exago BI server / web service address in the **Inbound Rule** field.
   4. Enter the Exago BI server / web service address in the **Outbound Rule – From:** field.
   5. Enter the host application address in the **Outbound Rule – To:** field.
   6. Click **OK**.

See **[Setup IIS with URL Rewrite as a reverse proxy for real world apps](https://blogs.msdn.microsoft.com/friis/2016/08/25/setup-iis-with-url-rewrite-as-a-reverse-proxy-for-real-world-apps/)** (MSDN) for more information.

### Apache

Add the following lines to **httpd.conf**

```
LoadModule proxy_module        modules/mod_proxy.so
LoadModule proxy_ajp_module    modules/mod_proxy_ajp.so
LoadModule proxy_http_module   modules/mod_proxy_http.so
ProxyPass /{EXAGO}             http://localhost/{EXAGO}
ProxyPass /{EXAGO_WEBSERVICE}  http://localhost/{EXAGO_WEBSERVICE}
```

See [**Running a Reverse Proxy with Apache**](http://www.apachetutor.org/admin/reverseproxies) for more information.

## Configure Exago BI

Exago BI should be configured as follows:

Add the following to the web service configuration file – Config**WebReportsApi.xml**:

```
<webreportsbaseurl>http:\{HOST_APP_ADDRESS}{EXAGO_PATH}</webreportsbaseurl>
```

Finally, make sure that any references in the host application to Exago BI (web application or web service) use the proxy URL.
