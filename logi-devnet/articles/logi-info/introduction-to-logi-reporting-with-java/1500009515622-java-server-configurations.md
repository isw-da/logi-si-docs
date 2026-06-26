---
title: "Java Server Configurations"
id: 1500009515622
section: "Introduction to Logi Reporting with Java"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009515622-Java-Server-Configurations
updated_at: 2021-08-19T21:51:23Z
---

# Java Server Configurations

# Java Server Configurations

Logi products work with a variety of Java-based web servers, which often require specific configurations to work correctly and for optimum performance.

**IMPORTANT**: If you wish to upgrade to JDK 8 release build 261 (1.8.0\_261), or any later build of JDK 8, you will need to replace the mscorlib.jar file in the application folder with the new one and restart your server. The mscorlib.jar file can be found on our [Product Download](https://clm.logianalytics.com/rdPage.aspx?rdReport=ProductDownloads "Select to access Product Dowload page") page. Please contact Support for additional assistance.

This topic provides the details of these configurations for each server, including:

* General Information
* [Apache Tomcat 5.5 / 6.0 / 7.0](#Apache)
* [JBoss 4](#JBoss4)
* [JBoss 5.1](#JBoss51)
* [JBoss 7.1](#JBoss7)
* [Sun Glassfish (SJSAS) 2.1](#SunGF21)
* [Sun Glassfish (SJSAS) 3.0, 3.1](#SunGF3x)
* [BEA WebLogic 10](#BEA10)
* [Oracle WebLogic 12c](#Oracle12c)
* [IBM Websphere 7, 8.5](#Websphere)

## General Information

* The official Sun JDK 1.6, 1.7, or 1.8 is *required* for non-Apple platforms. JDK 1.6 is *required* for Apple platforms. The JRE is not sufficient, but OpenJDK 1.7 and Oracle JRockit 1.6 or 1.7 may be used.
* It's possible to use Logi products on systems that use symbolic links or the Filesystem Hierarchy Standard (FHS), but it makes configuration much more complicated and we don't recommend it.
* When Logi Studio creates a new application, it's deployed in exploded format within a single "Logi application folder", not as a WAR file. WAR deployments by Studio are not supported at this time.

![](https://devnet.logianalytics.com/hc/article_attachments/4402778385687/attnicon.gif) PhantomJS in Linux, as we distribute, is complete. There is no requirement to install Qt, WebKit, or any other libraries. However, it still relies on Fontconfig (the package Fontconfig or Libfontconfig, depending on the distribution). Normally, this is present; however, if you run PhantomjJS and receive a 127 error you need to complete another step. Navigate to the application root/WEB-INF/lib directory and enter "ldd phatntomjs". All the referenced libraries appear. If a version of Fontconfig does not appear then it must be installed. FontConfig installation instructions for various distros vary. The Ubuntu instructions are included here:

sudo apt-get update -y

sudo apt-get install -y fontconfig-config

For more information, see https://phantomjs.org/download and https://www.freedesktop.org/wiki/Software/fontconfig/.

### Set Java Options

The following JVM flags should be added to the Java options settings that used to tune/monitor the JVM.

Tthe **Performance Settings** are *strongly recommended* for the Sun JDK, OpenJDK, and JRockit, whereas the **JConsole** and **Tracing Settings** are optional but recommended, at least during initial implementation.

|  |  |
| --- | --- |
| Typical Performance Settings (required) | "-server (JDK)  -Xmx1280m (JDK, JRockit)  -XX:MaxPermSize=256m (JDK)  -XX:-DisableExplicitGC (JDK)  -XX:CompileThreshold=8000 (JDK)  -Djava.awt.headless=true (JDK, JRockit) |
| JConsole Settings (optional, for monitoring) | -Dcom.sun.management.jmxremote  -Djava.rmi.server.hostname=*<your host ip addr>*  -Dcom.sun.management.jmxremote.port=1099  -Dcom.sun.management.jmxremote.authenticate=false  -Dcom.sun.management.jmxremote.ssl=false |
| Tracing Settings (optional, for testing) | -verbose:gc  -Xprof  -XX:-CITime  -XX:-PrintCompilation  -Xloggc:$CATALINA\_HOME/logs/gc.log  -XX:+PrintGCDetails  -XX:+PrintGCTimeStamps" |

![](https://devnet.logianalytics.com/hc/article_attachments/4402778385687/attnicon.gif)  The Java heap space setting, -Xmx1280m, shown above is sufficient only for a minimal 32-bit development system, *not* for a production system. A setting more appropriate for a 64-bit production server would be something like -Xmx8192m. Consult your production server administrator.

For 64-bit JVMs you need to add a -d64 flag in the Performance Settings to force the JVM to use 64-bit addressing (does not apply to JRockit).

The $CATALINA\_HOME environment variable in the example refers to the folder into which Apache Tomcat has been installed; for other web servers substitute the appropriate variable.

The JDK includes the Java Monitoring and Management Console (**JConsole**) tool. It uses the extensive instrumentation of the Java virtual machine to provide information on the performance and resource consumption of applications running on the Java platform using Java Management Extension (JMX) technology. For more information about JConsole, see [this article](http://java.sun.com/javase/6/docs/technotes/guides/management/jconsole.html).

### About the Performance Settings

What do the performance settings recommended above actually do? Here's an explanation:

|  |  |
| --- | --- |
| **Setting** | **Description** |
| -server | This option instructs the launcher to run the Java JVM in Server Mode. The JVM can optimize a number of things for server environments, improving performance. |
| -Xmx | This option sets the maximum amount of memory that can be allocated to the JVM heap, improving performance. |
| -XX:MaxPermSize | This option sets the maximum amount of memory that can be used for the permanent generation, or "PermGen", Java's fixed block of memory for loading class files. Failure to set this to at least 128m will cause errors to occur and a setting of 256m is recommended. |
| -XX:-DisableExplicitGC | This option disables calls to the function System.gc(), which is often run explicitly by many classes. When it runs, it triggers a full garbage collection process, which consumes a lot of execution time and results in inefficient heap usage. When it's disabled, the JVM still performs garbage collection nonetheless, whenever necessary. |
| -XX:CompileThreshold | This option sets the number of method invocations/branches before compiling. The JVM usually waits for a method to be executed a certain number of times before it's compiled. Not compiling every method helps startup time and reduces RAM footprint. This option allows you to control that threshold. |
| -Djava.awt.headless | This option, when set to *true*, prevents graphics rendering code from assuming that a graphics console exists, avoiding any chance of encountering an obscure Java bug related to X-servers and graphics rendering. |

### "Hot Deployment" Caution

Be aware that Tomcat, JBOSS, WebLogic, and other servers that offer "Hot" or "Auto" deployment may produce errors when using Logi Studio wizards. If this deployment feature is enabled, the changes the wizard makes may be deployed before the wizard completes all of its steps, causing an error.

Typically, "Hello World"-type Logi apps will work fine in this environment but use of Studio wizards to build more complex apps will not.

To avoid this problem, either disable the hot or auto deployment feature (technique varies by server) or increase the "scan interval" used by the feature substantially.

## Apache Tomcat 5.5 / 6.0 / 7.0

1. Logi application folders must be stored beneath the webapps folder.

2. Use the environment variable $CATALINA\_OPTS to pass in the JVM flags described above to the Tomcat start-up script. The $CATALINA\_HOME environment variable in the example refers to the folder into which Apache Tomcat has been installed.

Under Windows, when Tomcat is installed as an *application*, the JVM flags can be set by creating the file $CATALINA\_HOME\bin\setenv.bat and placing a line of text similar to this in it:

set "CATALINA\_OPTS = -server -d64 -Xmx1280m -XX:MaxPermSize=256m -XX:CompileThreshold=8000  
-XX:-DisableExplicitGC -Djava.awt.headless=true"

The -d64 flag assumes 64-bit software and note that the double-quotes enclose *everything* except the set command word.

Under Windows, when Tomcat is installed as a *service*, the JVM flags can be set by using the administrative tool installed with Tomcat (version number varies): $CATALINA\_HOME\bin\tomcat6w.exe:

![](https://devnet.logianalytics.com/hc/article_attachments/4402771656087/javaconfig_02.png)

In the administrative tool, select the Java tab and add the JVM flags to the Java Options, as shown above.

### Special Connection Pooling for Oracle in Connection-Intensive Environments

Logi applications may quickly open and close dozens of database connections and, in some connection-intensive environments, this may cause server resource problems. The following configuration changes for Tomcat implement connection pooling and have been tested with our Connection.JDBC and Connection.Oracle elements:

For server-wide connection pooling, change these files:

1. Add this to the file $CATALINA\_HOME/conf/web.xml:

<resource-ref>  
      <description> DB Connection Pooling</description>  
      <res-ref-name> jdbc/Oraclecp</res-ref-name>  
      <res-type> javax.sql.DataSource</res-type>  
      <res-auth> Container</res-auth>  
</resource-ref>

2. Create a new file $CATALINA\_HOME/conf/context.xml, containing the following:

<?xml version="1.0" encoding="UTF-8"?>  
<Context>  
  <Resource name="jdbc/Oraclecp" auth="Container"  
    type="javax.sql.DataSource" removeAbandoned="true"  
    logAbandoned="false"   
    maxActive="20" maxIdle="3" maxWait="10000"  
    removeAbandonedTimeout="30"   
    username= "*<yourUsername>*"  
    password="*<yourPassword>*"  
    factory="org.apache.tomcat.dbcp.dbcp.BasicDataSourceFactory"  
    driverClassName="oracle.jdbc.OracleDriver"  
    url="jdbc:oracle:thin:@*<yourServerName>*:1521:*<yourSID>*"/>  
</Context>

3. Copy the "ojdbc6.jar" file from *<LogiAppFolder>*/WEB-INF/lib to $CATALINA\_HOME/common/lib

4. Manually edit your Connection element attributes in \_Settings.lgx (using the Source tab in Studio's Workspace) to be:

Connection String = jndi-datasource-name=jdbc/Oraclecp

These links provide additional information about connection pooling:

<https://people.apache.org/~fhanik/jdbc-pool/jdbc-pool.html><https://tomcat.apache.org/tomcat-5.5-doc/jndi-datasource-examples-howto.html>

## JBoss 4

The following configuration details apply for JBoss 4:

1. Delete these files:  *<LogiAppFolder>/*WEB-INF/lib/log4j-1.2.8.jar *<LogiAppFolder>/*WEB-INF/classes/log4j.properties

2. Auto-deploy is used with this server so either manually or through Logi Studio's New Application wizard, give the root folder for your Logi application a .war file extension. Ensure that this folder is placed beneath whatever folder you've configured as your auto-deploy folder, for example: jboss/server/default/deploy/myLogiApp.war

See the *Hello World! Tutorial* for some examples of working with the New Application wizard.

3. The startup batch file "run.bat" may include the following line: set JAVA\_OPTS=%JAVA\_OPTS% -Xms128m -Xmx512m. This must be prevented from overriding our required Java Options environment settings (see the General section, above). Users can either modify the batch file or the environment variable.

4. Logi v10.0.114+ users: JBoss ships with a xerces library that conflicts with Logi's implementation of it, so remove the following .jar files from the *<LogiAppFolder>/*WEB-INF/libfolder prior to deploying:

xml-apis-1.3.04.jar  
xml-apis-ext-1.304.jar  
xercesImpl-2.7.1.jar

## JBoss 5.1

The following configuration details apply for JBoss 5.1:

1. Auto-deploy is used with this server so either manually or through Logi Studio's New Application wizard, give the root folder for your Logi application a .war file extension. Ensure that this folder is placed beneath whatever folder you've configured as your auto-deploy folder, for example: jboss/server/default/deploy/myLogiApp.war

See the *Hello World! Tutorial* for some examples of working with the New Application wizard.

2. Set the Java options by editing $JBOSS\_HOME/bin/run.confso that it includes:

-Xmx1280m  
-XX:CompileThreshold=8000  
-Djava.awt.headless=true

3. Edit *<LogiAppFolder>/*WEB-INF/web.xmland add the following:

<context-param>  
    <param-name>org.jboss.jbossfaces.WAR\_BUNDLES\_JSF\_IMPL</param-name>  
    <param-value>true</param-value>  
</context-param>

5. Logi v10.0.114+ users: JBoss ships with a xerces library that conflicts with Logi's implementation of it, so remove the following .jar files from the *<LogiAppFolder>/*WEB-INF/lib folder prior to deploying:

xml-apis-1.3.04.jar  
xml-apis-ext-1.304.jar  
xercesImpl-2.7.1.jar

## JBoss 7.1

The following configuration details apply for JBoss 7. *We do not recommend using JBoss 6.*

1. Auto-deploy is used with this server so either manually or through Logi Studio's New Application wizard, give the root folder for your Logi application a .war file extension. Ensure that this folder is placed beneath whatever folder you've configured as your auto-deploy folder, for example: jboss/server/default/deploy/myLogiApp.war

See the *Hello World! Tutorial* for some examples of working with the New Application wizard.

2. Set the Java options by editing $JBOSS\_HOME/bin/run.conf so that it includes:

-Xmx1280m  
-XX:CompileThreshold=8000  
-Djava.awt.headless=true

3. Edit *<LogiAppFolder>/*WEB-INF/web.xml and add the following:

<context-param>  
    <param-name>org.jboss.jbossfaces.WAR\_BUNDLES\_JSF\_IMPL</param-name>  
    <param-value>true</param-value>  
</context-param>

4. If your JBoss server isn't capable of dynamic deployment, or you're not sure about the server settings, restart your JBoss server, using bin/standalone.sh.

5. Use a specific port and parameter when browsing the Logi applications. For example:

http://localhost:port#/yourLogiApp/rdpage.aspx?rdReport=Default

    and be sure to use the correct case-sensitive spelling of the Logi report definition file name, e.g. Default vs default.

## Sun Glassfish (SJSAS) 2.1

1. Manually add a .war extension to the Logi application folder. Deploy your application manually using the Glassfish Admin Console.

2. Right-click this link [sun-web.xml](https://clm.logianalytics.com/downloads/info/java/glassfish3.0/sun-web.xml) and save our customized version of the file in *<LogiAppFolder>/*WEB-INF. Keep the included *<LogiAppFolder>*/WEB-INF/web.xml file, but replace the existing *<LogiAppFolder>*/WEB-INF/sun-web.xml file, if you have one.

## Sun Glassfish (SJSAS) 3.0, 3.1

1. Manually add a .war extension to the Logi application folder. Deploy your application manually using the Glassfish Admin Console.

2. In addition to the recommended Java Options listed in the General Information section above, set the -XX:MaxPermSize setting to a minimum of 300m.

3. Right-click this link [sun-web.xml](https://clm.logianalytics.com/downloads/info/java/glassfish3.0/sun-web.xml) and save our customized version of the file in *<LogiAppFolder>/*WEB-INF. Keep the included *<LogiAppFolder>*/WEB-INF/web.xml file, but replace the existing *<LogiAppFolder>*/WEB-INF/sun-web.xml file, if you have one.

4. Right-click this link [faces-config.xml](https://clm.logianalytics.com/downloads/info/java/glassfish3.0/faces-config.xml) and save our customized version of the file in *<LogiAppFolder>/*WEB-INF, replacing the standard file of the same name.

## BEA WebLogic 10

1. Auto-deploy is used with this server. Logi application folders must be manually given a .war file extension.

2. The JVM settings described above can be changed by editing them in

$WL\_HOME/user\_projects/domains/<Logi\_Domain>/bin/setDomainEnv.sh      (Linux/UNIX)

$WL\_HOME/user\_projects/domains/<Logi\_Domain>/bin/setDomainEnv.cmd     (Windows)

3. Right-click this link [weblogic.xml](https://clm.logianalytics.com/downloads/info/java/weblogic10/weblogic10.xml) and save the file in *<LogiAppFolder>/*WEB-INF

4. If using requests that return a large amount of data, performance can be improved by configuring the "TCP Chunk" parameters. You must pass -D weblogic.Chunksize=65535 for Logi to work properly under Weblogic. See the following information: *[Tune the Chunk Parameters](http://download.oracle.com/docs/cd/E13222_01/wls/docs100/perform/WLSTuning.html#wp1152088)*

## Oracle WebLogic 12c

1. Auto-deploy is used with this server. Logi application folders must be manually given a .war file extension.

2. The JVM settings described above can be changed by editing them in

$WL\_HOME/user\_projects/domains/<Logi\_Domain>/bin/setDomainEnv.sh      (Linux/UNIX)

$WL\_HOME/user\_projects/domains/<Logi\_Domain>/bin/setDomainEnv.cmd     (Windows)

3. Right-click this link [weblogic.xml](https://clm.logianalytics.com/downloads/info/java/weblogic12c/weblogic.xml) and save the file in *<LogiAppFolder>/*WEB-INF

4. If using requests that return a large amount of data, performance can be improved by configuring the "TCP Chunk" parameters. You must pass -D weblogic.Chunksize=65535 for Logi to work properly under Weblogic. See the following information: *[Tune the Chunk Parameters](http://download.oracle.com/docs/cd/E13222_01/wls/docs100/perform/WLSTuning.html#wp1152088)*

## IBM Websphere 7, 8.5

For best performance, Websphere 8.5 users should ensure that they're using SDK 7. Information about the SDK [can be found here](http://www-01.ibm.com/support/knowledgecenter/SS7K4U_8.5.5/com.ibm.websphere.installation.nd.doc/ae/tins_installation_jdk7_gui.html) and it can be downloaded using the from IBM Installation Manager [from here](https://www.ibm.com/support/knowledgecenter/SS7K4U_8.5.5/com.ibm.websphere.installation.nd.doc/ae/tins_installation_jdk7_gui.html).

![](https://devnet.logianalytics.com/hc/article_attachments/4402771656343/javaconfig_03.png)
