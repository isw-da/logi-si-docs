---
title: "Non-sticky Session Load Balancing"
id: 4406817709847
section: "Manage - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817709847-Non-sticky-Session-Load-Balancing
updated_at: 2022-04-06T06:07:45Z
---

# Non-sticky Session Load Balancing

# Non-sticky Session Load Balancing

Non-sticky session configuration means that you do not route all the requests to the same server that handled the initial request. Subsequent requests can be routed to any of the servers in the pool for processing. Again, we recommend you use a sticky session load balancing environment with Logi Info because certain files need to be shared across servers, which can be slower in a network environment.

If you must use a non-sticky session configuration, you will face these challenges:

* Session replication can be contentious
* File access performance can impact app performance and in some cases can cause race-conditions, leading to errors
* Performance impact on distributed file systems, e.g. EFS, would be greater, especially for high file I/O requirements for rdDatacache folder
* Hosting on cloud (AWS, Azure, GCP, etc.) adds additional complexity to the above issues

To deploy a non-sticky environment, follow these steps:

1. Configure Load Balancer to be set to non-sticky
2. Prepare environment for centralization of resources (see [Application Resource Centralization](#Addition))
3. Centralize rdDataCache (see below)
4. Configure Logi Info application
5. Deploy application to all web servers

## Centralizing rdDataCache for Non-Sticky Sessions Only

The data cache repository is, by default, the rdDataCache folder in a Logi application's root folder. In a standalone environment, where all the requests are processed by the same server, this default cache configuration is sufficient.

In a non-sticky load-balanced environment, centralizing the data cache repository is required. This will pose additional challenges to customers who want to use a non-sticky load balanced environment. If you do insist on using this configuration, make sure you centralize the data cache in this way.  
 
![](https://devnet.logianalytics.com/hc/article_attachments/4417575596311/loadbal_05_786x197.png)

This is accomplished in Studio by editing a Logi application's \_Settings definition, as shown above. You need to set the **General** element's **Data Cache Location** attribute value to the UNC path of a shared network location accessible by all web servers. You need to make this change in the \_Settings definition for each instance of the Logi application (i.e. on each web server).
When you specify a network folder for the data cache, you need to change the identity that the web server uses to run the application (usually ASPNET or NETWORK SERVICE or the Application Pool), or impersonates, to a network domain account that has Full Control access permissions for the specified folder.

This attribute will support relative path notation, such as two periods ".." used to indicate a parent folder. For example,

@Function.AppPhysicalPath~\..\..\..\..\OurDataCache  
 

## Managing Session State for Non-Sticky Sessions

A "session" is defined as the period of time in which a unique user interacts with a particular web application.
HTTP is a "stateless" protocol, in the sense that a web server is concerned only with the current HTTP request for any given web page. The web server retains no knowledge of previous requests and the stateless nature of HTTP requests presents unique challenges when writing web applications.
In clustered environments, where non-sticky sessions are desired, session state needs to be replicated to all members of the cluster.

### State Replication for ASP.NET and IIS for Non-Sticky Session Environments

Your
ASP.NET applications require the session state to be maintained using one of these three session management options:

* **InProc** - Session state is stored locally on the web server and is managed in the same worker process as the ASP.NET application.
* **StateServer** - Session state is managed by the ASP.NET state service, which runs outside of the ASP.NET worker process. The service can run on a different server to support web farms.
* **SQLServer** - Session state is managed outside of the ASP.NET worker process and is stored in a SQL Server database. Like the StateServer option, this method can support web farms.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) Additional considerations, other than load balancing, may affect the choice of session state management options.
IIS is configured by default to manage session information using the "InProc" option. For both standalone and load-balanced, sticky environments, this option allows a single server to manage the session information for the life of the session.
For non-sticky, load-balanced configurations, session state needs to be managed centrally. Since requests can be processed by any of the available servers, the servers need to be able to access session information from a common location. Therefore, you should use either the StateServer or SQLServer management options in this circumstance.
Use your IIS Management Tool, in the ASP.NET configuration tab or dialog box, to actually configure your session management options; however, the details are beyond the scope of this document. Refer to your IIS documentation.

### State Replication for Java and Apache Tomcat for Non-Sticky Session Environments

Use this link for [detailed instructions](http://tomcat.apache.org/tomcat-8.0-doc/cluster-howto.html) about creating clustered implementations of Apache Tomcat.
This procedure describes how you configure Tomcat for in-memory (multicast) and database (persistent) session replication across all members of a cluster (some of the information presented here is drawn from the clustering instructions at the link above).
To configure *in-memory* session replication:

1. Modify your server.xml file by adding the following in either the <Engine> or <Host> sections:

<Cluster className="org.apache.catalina.ha.tcp.SimpleTcpCluster"/>

To configure use of a *database* for session replication, follow these steps:

1. Ensure that the <Cluster> element is disabled in your server.xml file to turn off in-memory replication.
2. Navigate to the root of your Logi app and, if it doesn't already exist, create a folder named META-INF.
3. In the META-INF folder create a file named context.xml and open it in a file editor.
4. In the file, define a root <Context> element, and then add the following <Manager> element to that section:

<Manager className="org.apache.catalina.session.PersistentManager" >

5. Determine what type of database you want to use for session persistence and copy the .JAR driver file for that database into the Tomcat lib folder.
6. Add the following <Store> element within the <Manager> section:

<Store className="org.apache.catalina.session.JDBCStore"  
   connectionURL="jdbc:<your\_jdbc\_connection\_url>"  
   driverName="<your\_jdbc\_driver\_classname>"  
   sessionIdCol="session\_id"  
   sessionValidCol="valid\_session"  
   sessionMaxInactiveCol="max\_inactive"  
   sessionLastAccessedCol="last\_active"  
   sessionTable="tomcat\_sessions"  
   sessionAppCol="app\_context"  
   sessionDataCol="session\_data"  
/>

7. Execute the following SQL command against the database specified in your JDBC connection URL:

create table tomcat\_sessions (  
   session\_id varchar(100) not null primary key,  
   valid\_session char(1) not null,  
   max\_inactive int not null,  
   last\_access bigint not null,  
   app\_context varchar(255),  
   session\_data mediumblob,  
   KEY kapp\_context (app\_context)  
);

## Configure Logi Info Application

Regardless of which replication method you chose above, complete the session configuration with these steps:

1. In *<LogiAppFolder>*/WEB\_INF/web.xml, ensure that the <distributable/> tag is included.

2. In <LogiAppFolder>/WEB\_INF/web.xml, set the **EnableSessionPersistency** context parameter to *True*. This parameter is present in all Logi apps by default.  
     
   Here's a partial file example, with both additions highlighted:.

<!DOCTYPE web-app PUBLIC "-//Sun Microsystems, Inc.//DTD Web Application 2.3//EN"  
        "http://java.sun.com/dtd/web-app\_2\_3.dtd"[]>  
    <web-app id="WebApp\_ID">  
    <display-name>Logi Server for Java 12.2.225-SP5</display-name>  
    <description>Logi Server for Java 12.2.225-SP5</description>  
    <distributable/>  
    <context-param>  
     <param-name>EnableSessionPersistency</param-name>  
      <param-value>True</param-value>  
    </context-param>  
        ...

3. In your Logi application's \_Settings definition, add a **Java Session Copying** element:  
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417583805335/loadbal_06_806x185.png)

Be sure to set the **Copy to Java Include** attribute value, using a caret symbol "^".
