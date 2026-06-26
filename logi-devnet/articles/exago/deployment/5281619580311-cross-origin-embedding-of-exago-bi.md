---
title: "Cross-Origin Embedding of Exago BI"
id: 5281619580311
section: "Deployment"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281619580311-Cross-Origin-Embedding-of-Exago-BI
updated_at: 2022-05-03T22:08:43Z
---

# Cross-Origin Embedding of Exago BI

# Cross-Origin Embedding of Exago BI

When a user enters Exago BI, the application creates a session in order to preserve the user’s working state and environment while they engage with it. The session information is stored on the web application server or state server (depending on the network configuration).

Whenever requests are made the user’s browser sends a unique, randomly generated ID to the web server in order to authenticate the user and preserve the connection between user and session.

By default, this session ID is stored as a browser cookie. However, when embedding Exago BI in a cross-origin environment (where the Exago BI server and host application are referred to by different protocols, domains or ports) cookies are considered a potential attack vector for cross-site scripting. Most modern web browsers prevent embedded content from separate origins from using cookies without additional configuration to explicitly allow this behavior safely.

Consider these three scenarios for embedding Exago BI in a host application:

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Critical")
>
> In the cases below and a state server is in use, make sure to set `cookieless="false"` as the use of cookieless sessions with a state server is not supported.

* Exago BI and Host Application are referenced by the same origin (not covered by this topic)
* Exago BI and Host Application are referenced by different origins, using [Cross-Origin Resource Sharing (CORS) with Cookies](#Cross-Or) (recommended)
* Exago BI and Host Application are referenced by different origins, using [Cookieless Sessions](#Cookiele) (not recommended)

## Cross-Origin Resource Sharing (CORS) with Cookies

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> When using cookies, Exago BI must be accessed via **HTTPS** in a CORS environment.

If the Exago BI application is being accessed over a network, the Exago BI web server must be configured to allow **cross-origin requests** from the embedding host application.

By default, a web application making a request for content that originates from a remote server sends a cross-origin HTTP request. For security reasons, browsers restrict these types of requests when they originate from scripts.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> When using the JavaScript API with versions prior to *v2019.1.23*, *v2019.2.9*and *v2020.1.0* in a CORS environment, [Cookieless Sessions](#Cookiele) must be used.

To permit content to be accessed by white listed resources, you can configure the Exago BI web server to send a *Access-Control-Allow-Origin* and *Access-Control-Allow-Credentials* headers to the calling server.

### *v2019.2.29+, v2020.1.13+, v2021.1.1+*

As of the version numbers listed above, two new [Application Settings](https://devnet.logianalytics.com/hc/en-us/articles/5281615366423-Application-Settings) elements, **AccessControlAllowCredentials** and **CorsAllowedOrigins** have been added to the Web Application’s `appSettings.config` file. These new nodes are the only supported way of adding *Access-Control-Allow-Origin* and *Access-Control-Allow-Credentials* for new installations.

Setting the headers in the web server’s configuration is no longer recommended. However, that method will continue to function for existing clients upgrading from previous versions.

Review the Web Application appSettings.config section of [Application Settings](https://devnet.logianalytics.com/hc/en-us/articles/5281615366423-Application-Settings) for full details on setting these headers.

### *pre-v2019.2.29, v2020.1.13, v2021.1.1*

*Access-Control-Allow-Origin* should be set to a single domain that matches the domain of the page in which Exago BI is embedded. For example:

```
Access-Control-Allow-Origin: hostapp.server.com
Access-Control-Allow-Credentials: true
```

In **IIS**, this is either set in the **HTTP Response Headers** or added manually to the `web.config` file.

In **Apache**, the following lines should be added to all relevant `.conf` files:

```
Header set Access-Control-Allow-Origin "hostapp.server.com"
Header set Access-Control-Allow-Credentials: "true"
```

In **NGINX**, the following line should be added inside the location /Exago/ {…} section of the “exago” NGINX site configuration file:

```
add_header 'Access-Control-Allow-Origin' 'hostapp.server.com';
add_header 'Access-Control-Allow-Credentials' 'true'
```

## Cookieless Sessions

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> As of Exago BI*v2019.1.23+*, *v2019.2.9+*and *v2020.1.0+* the use of cookieless sessions is not recommended when Exago BI is hosted over a secure connection (HTTPS). Use [Cross-Origin Resource Sharing (CORS) with Cookies](#Cross-Or) instead.

### Enable Cookieless Sessions

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This topic references `<WebApp>/`,
> `<WebSvc>/` and `<Sched>/`as a placeholder
> for the Web Application, Web Service API and Scheduler Service's install
> location respectively. The default install location is
> `C:\Program Files\Exago\ExagoWeb\` (`/opt/Exago/` on Linux),
> `C:\Program Files\Exago\ExagoWebApi\` ( `/opt/Exago/WebServiceApi/` on Linux) or
> `C:\Program Files\Exago\ExagoScheduler\` (`/opt/Exago/Scheduler/` on Linux); however, these directories
> can be changed during installation.

To enable cookieless sessions, locate the following line in the `<WebApp>\web.config` file and set the `cookieless` attribute to *true*:

```
<sessionState mode="InProc" cookieless="true" timeout="20" />
```

Cookieless sessions work to preserve state by appending the session ID to the URL string itself, which is used to connect to the web server. For example, a standard application URL generated by the server API after creating a session looks similar to the following:

```
//ExagoBI/ExagoHome.aspx?sn=0
```

With cookieless sessions enabled, the session ID is added to the URL, for example:

```
//ExagoBI/(S(rim43x0e3cz2hf4sjw24ezdk))/ExagoHome.aspx?sn=0
```

This has no direct implications for the embedding process into the host application.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> In Linux environments, a patched `System.Web.dll` Mono library is necessary when using cookieless sessions. This patched DLL is installed when the Exago BI Linux Installer is executed, or it can be installed using our [patch script](https://devnet.logianalytics.com/hc/article_attachments/5432173608983/exago_mono_patch.tgz). Exago BI only supports specific versions of Mono, review [Installing Exago on Linux](https://devnet.logianalytics.com/hc/en-us/articles/5281601243031-Installing-Exago-on-Linux) for details.

### Secured Authentication

When the Web Application server is exposed to the internet or any insecure public network or intranet, enable secured authentication to prevent unauthorized access.

Because the session ID is passed as a part of the URL, it can be used by malicious third parties to send unauthorized requests to the web server. Secured authentication causes the web server to require a secondary security token in order to authenticate the session. This does not require any additional effort on the part of the end-user.

To enable secured authentication, edit the `<WebApp>\appSettings.config` file and add the following line:

```
<add key="useSecurityToken" value="True" />
```

The server API generates a security token with the session and embeds it into the page markup. It is sent with every client request as a part of the payload. When using a secured connection, the payload is encrypted, thus making it nearly impossible for a malicious party to derive the token.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> Unsecured connections will compromise any security intended by the use of secured authentication. If the payload is unencrypted, the token can be easily intercepted by a third party. The web server must enforce HTTPS in order for secured authentication to function properly.

## Additional Resources

Review these third-party resources for additional background information on the topics presented in this topic.

* [Mozilla Developer Network: Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
* [IBM: Prevent a cross-site scripting attack](https://www.ibm.com/developerworks/ibm/library/wa-secxss/)
