---
title: "Enable Composer  Component Access From Other Sites Using Cross-Origin Resource Sharing (CORS)"
id: 34932686402701
section: "Manage Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932686402701-Enable-Composer-Component-Access-From-Other-Sites-Using-Cross-Origin-Resource-Sharing-CORS
updated_at: 2026-05-26T22:06:18Z
---

# Enable Composer  Component Access From Other Sites Using Cross-Origin Resource Sharing (CORS)

# Enable Composer Component Access From Other Sites Using Cross-Origin Resource Sharing (CORS)

Cross-origin resource sharing (CORS) is a standard introduced in HTML 5 that allows web applications to use HTTP headers to specify which origins are permitted to request resources on the server. Cross-origin resource sharing provides a web application access to selected resources running at a different location. Modern web browsers will consult the Access-Control-Allow-Origin header on how to relax the same origin policy for a given page. By default, this setting was disabled starting version 1.5.0SR1 due to security vulnerability concerns. However, CORS can be enabled for certain or all domains by editing the `zoomdata.properties` file (located in `/etc/zoomdata`).
For more information about CORS, see <https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS>.

**Modify CORS request permissions**

1. From your terminal, open a command line session.
2. Connect to your Composer server via a command prompt.
3. Use the following command to access and open the `zoomdata.properties` file:

   vi /etc/zoomdata/zoomdata.properties
4. Add the following variables to the file on new lines:

   http.response.header.content-security-policy.frame-ancestors=<source1> <source2>  
   access.control.allow.origin=<origin1>,<origin2>

   Replace `<source>` with the actual sources that may embed resources. The default is an asterisk (`*`), or all sources. For more information about the Content-Security-Policy (CSP) frame-ancestors directive, see <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/frame-ancestors>.

   Replace `<origin1>` and `<origin2>` with your specific URI including `http` or `https` as appropriate. Use `*` as a wildcard instead of a specific origin, thereby allowing any origin to access the resource, keeping in mind that this is a potential security vulnerability and may not work with all browsers. Refer to your Tomcat documentation to verify the appropriate syntax to use.
5. Save the document using standard `vi` commands.
6. Restart Composer microservices after making this change and also make sure to clear your browser cache. See  [Restart Microservices](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/35385540487565-About-Microservices#Restart).
