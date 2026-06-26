---
title: "Load Balancing Configuration"
id: 1500009531401
section: "Upgrade Logi Products and Apps"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009531401-Load-Balancing-Configuration
updated_at: 2021-06-17T01:58:31Z
---

# Load Balancing Configuration

# Load Balancing Configuration

**Load balancing** is a technique used to distribute workload evenly across two or more web servers in order to optimize resource utilization, maximize throughput, minimize response time, and avoid overload. This topic discusses the configuration requirements for using Logi applications in a load-balanced .NET environment.

* About Load Balancing
* [Manage Session State](#Session)
* [Additional Centralization of Application Resources](#Application)
* [Use SecureKey Security](#SecureKey)
* [Centralize the Data Cache](#Cache)

## About Load Balancing

**Load balancing** is a technique used to distribute workload evenly across two or more web servers in order to optimize resource utilization, maximize throughput, minimize response time, and avoid overload. Load balancing can also be used
to increase reliability through redundancy.

Multiple web servers used in a load-balanced environment, sometimes called a "server
farm" or "clustered servers", are often controlled by load balancing management software. This software, monitors the port where external client browsers connect to access
services and distributes requests among the available servers. Replies may be routed back through the management software, hiding the existence of multiple servers. This prevents clients from contacting managed servers directly, which can have security benefits.

Alternate methods of load balancing exist, but the basic goal is the same: to distribute requests equitably across multiple servers.

### Sticky and Non-Sticky Sessions

In a standard environment, with one server, session is established with the first HTTP request and all subsequent requests, for the life of the session, will be handled by that same server.

However, in a load-balanced or clustered environment, there are two possibilities for handling requests, "sticky" sessions (sometimes called *session affinity*) and "non-sticky" sessions.

In a **sticky** session configuration, a session is established with the first HTTP request and a specific server is "assigned" to process all subsequent requests, for the life of the session.

In a **non-sticky** session configuration, each request is independent of previous requests and may be routed to any of the servers in the pool for processing.

In both sticky and non-sticky session configurations, centralizing the location of any shared resources and managing session state is very important. A centralized, shared location for cached data (caches with expirations longer than active sessions - typically the rdDataCache folder), saved Bookmark files, and saved Dashboard files *must* be accessible to all servers in the cluster.

## Managing Session State

A "session" is defined as the period of time in which a unique user interacts with a particular web application.

HTTP is a "stateless" protocol, in the sense that a web server is concerned only with the current HTTP request for any given web page. The web server retains no knowledge of previous requests and the stateless nature of HTTP requests presents unique challenges when writing web applications.

In clustered environments, where non-sticky sessions are desired, session state needs to be replicated to all members of the cluster.

### State Replication for ASP.NET and IIS

ASP.NET applications require session state to be maintained using one of these three session management options:

* **InProc** - Session state is stored locally on the web server and is managed in the same worker process as the ASP.NET application.
* **StateServer** - Session state is managed by the ASP.NET state service, which runs outside of the ASP.NET worker process. The service can run on a different server to support web farms.
* **SQLServer** - Session state is managed outside of the ASP.NET worker process and is stored in a SQL Server database. Like the StateServer option, this method can support web farms.

Note that additional considerations, other than load balancing, may affect the choice of session state management options.

IIS is configured by default to manage session information using the "InProc" option. For both standalone and load-balanced, sticky environments, this option allows a single server to manage the session information for the life of the session.

For non-sticky, load-balanced configurations, session state needs to be managed centrally. Since requests can be processed by any of the available servers, the servers need to be able to access session information from a common location. Therefore, either the StateServer or SQLServer management options should be used in this circumstance.

Actual configuration of session management options is accomplished using the IIS Management Tool, in the ASP.NET configuration tab or dialog box; however, the details are beyond the scope of this topic. Refer to your IIS documentation.

### State Replication for Apache Tomcat

Use this link for [detailed instructions](http://tomcat.apache.org/tomcat-8.0-doc/cluster-howto.html) about creating clustered implementations of Apache Tomcat.

The following describes how to configure Tomcat for in-memory state replication across all members of a cluster (some of the information presented here is drawn from the clustering instructions at the link above).

1. Modify your server.xml file by adding the following in either the <Engine> or <Host> sections:

<Cluster className="org.apache.catalina.ha.tcp.SimpleTcpCluster"/>

2. In *<LogiAppFolder>*/WEB\_INF/web.xml, ensure that the <distributable/> tag is included.
3. In Java EE, the location of session state storage is a vendor-specific decision. For example, servers may choose to store session state in memory and temporarily dump the memory to disk under heavy memory consumption. As a result, all of the session objects must be serialized, according to the Java EE specification. For more information, read the server-specific documentation about session persistency/replication. To facilitate session management in your Logi application, we've provided a context
   parameter, **EnableSessionPersistency**, in *<LogiAppFolder>*/WEB\_INF/web.xml. To enable session persistency, set this parameter to *True*, and remember to serialize all your session objects. Objects that are not serialized can cause unexpected exceptions. Prior to Logi Info v11.3, the default for this parameter is *False*, in v11.3+ the default is *True*.  
     
   Here's a partial file example, with both additions highlighted:  
     
         
       <!DOCTYPE web-app PUBLIC "-//Sun Microsystems, Inc.//DTD Web Application 2.3//EN"  
           "http://java.sun.com/dtd/web-app\_2\_3.dtd"[]>  
       <web-app id="WebApp\_ID">  
       <display-name>Logi Server for Java 11.2.040-SP2</display-name>  
       <description>Logi Server for Java 11.2.040-SP2</description>  
       <distributable/>  
       <context-param>  
        <param-name>EnableSessionPersistency</param-name>  
         <param-value>True</param-value>  
       </context-param>  
           ...
4. In your Logi application's \_Settings definition, add a **Java Session Copying** element:  
     
     
    ![](https://logianalytics.zendesk.com/hc/article_attachments/4402778540823/loadbal_06.png)

Be sure to set the **Copy to Java Include** attribute value, using a caret symbol "^".

## Additional Centralization of Application Resources

In a load-balanced environment, each web server must have Logi Server installed and properly licensed, and must have its own copy of the Logi application with its folder structure, system files, etc. This includes everything in the \_SupportFiles folder such as images, stylesheets, XML data files, etc., any custom themes, and any HTML or script files.

Some application files *should* be centralized, which also allows for easier configuration management. These files include:

**Definitions** - Copies of report, process, widget, template, and any other necessary definitions (except \_Settings) can be installed on each web server as part of the application, or, centralized definitions may be used, if desired, for easier maintenance.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778541079/loadbal_01.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771651863/loadbal_01a.png)

The location of definitions is configured in \_Settings definition, using the **Path** element's **Alternative Definition Folder** attribute, as shown above. This should be set to the UNC path to a shared network location accessible by all web servers, and the attribute value should include the \_Definitions folder. Physically, within that folder, you should create the folders \_Reports,
\_Processes, \_Widgets, and \_Templates as necessary. Do not include the \_Settings definition in any alternate
location; it must remain in the application folder on the web server as usual.

**"Save" Files** - Many super-elements, such as the **Dashboard** and **Analysis Grid**, allow the user to save the current configuration to a file for later reuse. The locations of these files are specified in attributes of the elements.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771652119/loadbal_02.png)

As shown in the Dashboard example above, the **Save File** attribute value should be the UNC path to a shared network location (with file name, if applicable) accessible by all web servers.

**Bookmarks** - If used in an application, the location of these files should also be centralized:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771652375/loadbal_03.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778541335/loadbal_03a.png)

As shown above, in the \_Settings definition, configure the **General** element's **Bookmark Location** attribute, with a UNC path to a shared network folder accessible by all web servers.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif)  In general, when you specify a network folder or file to centralize a resource, you need to change the identity that the web server uses (usually "ASPNET" or "NETWORK SERVICE"), or impersonates, to run the application to a network domain account that has Full Control access permissions for the specified folder.

## Use SecureKey Security

If you're using Logi SecureKey security in a load-balanced environment, you need to configure security to share requests.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771652631/loadbal_04.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771652887/loadbal_04a.png)

In the \_Settings definition, set the **Security** element's **SecureKey Shared Folder** attribute to a network path, as shown above. Files in the SecureKey folder are automatically deleted over time, so do not
use this folder to store other files.

## Centralize the Data Cache

The data cache repository is, by default, the rdDataCache folder in a Logi application's root folder. In a standalone environment, where all the requests are processed by the same server, this default cache configuration is sufficient.

In a load-balanced environment, centralizing the data cache repository is required.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771653143/loadbal_05.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778541719/loadbal_05a.png)

This is accomplished in Studio by editing a Logi application's \_Settings definition, as shown above. The **General** element's **Data Cache Location** attribute value should be set to the UNC path of a shared network location accessible by all web servers. This change should be made in the \_Settings definition for each instance of the Logi application (i.e. on each web server).

When you specify a network folder for the data cache, you need to change the identity that the web server uses (usually "ASPNET" or "NETWORK SERVICE"), or impersonates, to run the application to a network domain account that has Full Control access permissions for the specified folder.

In v11.0.127, this attribute was enhanced to support relative path notation, such as two periods ".." used to indicate a parent folder. For example,

@Function.AppPhysicalPath~\..\..\..\..\OurDataCache

Keywords: clustering, cluster
