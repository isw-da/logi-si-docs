---
title: "Data Definitions"
id: 4406822229527
section: "Connect to Data - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822229527-Data-Definitions
updated_at: 2022-04-06T06:04:56Z
---

# Data Definitions

# Data Definitions

**Data Definitions** allow developers to leverage Logi Info's ability to connect to a variety of datasources in order to create a powerful JSON and XML data provider for Logi applications, non-Logi applications, and client browsers.

The following topics introduce the data definitions used to retrieve data:

* [Data Definition Basics](https://devnet.logianalytics.com/hc/en-us/articles/4406817248919-Data-Definition-Basics#Basics)
* [Creating a JSON Data Definition](https://devnet.logianalytics.com/hc/en-us/articles/4406817246871-Creating-a-JSON-Data-Definition#JSONDef)
* [Creating an XML Data Definition](https://devnet.logianalytics.com/hc/en-us/articles/4406817247895-Creating-an-XML-Data-Definition#XMLDef)
* [Retrieving Data](https://devnet.logianalytics.com/hc/en-us/articles/4406817253271-Retrieving-Data#Retrieving)
* [Example: Getting Data for aLogi Application](https://devnet.logianalytics.com/hc/en-us/articles/4406817250071-Retrieving-Data-Example-Getting-Data-for-a-Logi-Application#LogiAppSimple)
* [Example: Using Parameters for Dynamic Data](https://devnet.logianalytics.com/hc/en-us/articles/4406817251223-Retrieving-Data-Example-Using-Parameters-for-Dynamic-Data#Parameters)
* [Example: Using 3rd-Party APIs](https://devnet.logianalytics.com/hc/en-us/articles/4406817252247-Retrieving-Data-Example-Using-3rd-Party-APIs#APIs)

## About Data Definitions

Logi Info applications are capable of connecting to, and retrieving data from, a wide range of datasources. They also allow retrieval from multiple datasources simultaneously and can provide SQL-like JOINs between non-SQL datasets.

Data definitions allow the developer to retrieve data from these sources, manipulate it, and then make it available as a JSON data stream to a variety of data consumers.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584052631/usingdatadefs_01.png)

The diagram shown above illustrates this concept. Creating a Logi data definition is simple and uses the same elements and techniques used in Logi report definitions. Writing code that consumes the JSON data is also easy and a variety of examples are provided in the later sections of this topic.

The JSON data produced can be accessed by Logi apps, directly from browsers, and by any application written in a programming language that supports HTTP requests.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575435927/notev12.7base.png)Data definitions can also create both JSON and XML data.

### Browsers and Cross-Origin Resource Sharing

When the client accessing the Logi data definition is a browser that's *not* on the same domain, you'll need to use the **Cross-Origin Resource Sharing** (CORS) mechanism to guarantee access. The CORS standard describes HTTP headers which provide browsers with a way to request remote URLs when they have permission. CORS is supported by most modern browsers.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) CORS is *not* necessary when *web server applications* are consuming the data.

CORS is implemented for Logi data definitions by configuring your web server's HTTP Response Header.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575793047/usingdatadefs_01a.png)

The example above shows this being done for IIS, using the IIS Manager application. It can also be done by modifying the web.config file directly.

<filter>  
<filter-name>CorsFilter</filter-name>  
<filter-class>org.apache.catalina.filters.CorsFilter</filter-class>  
</filter>  
<filter-mapping>  
<filter-name>CorsFilter</filter-name>  
<url-pattern>/\*</url-pattern>  
</filter-mapping>

For Apache Tomcat (starting with v7.0.41), the code shown above can be added to `$CATALINA_BASE/conf/web.xml` or `WEB-INF/web.xml`. Other Linux-UNIX web servers can be configured similarly. Refer to your server's documentation.

This external site, [Enable CORS](http://enable-cors.org/index.html), provides a lot of useful information about CORS and has server configuration examples.
