---
title: "Setting Java Options"
id: 4406817686551
section: "Install, Upgrade, & Remove - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817686551-Setting-Java-Options
updated_at: 2022-04-06T06:07:36Z
---

# Setting Java Options

# Setting Java Options

In general, the following JVM flags should be added to the Java options settings that are used to tune/monitor the JVM.

The **Performance Settings** are *strongly recommended* for the Oracle JDK, whereas the **JConsole** and **Tracing Settings** are optional but recommended, at least during initial implementation.

## Typical Performance Settings

-server (JDK)  
-Xmx4096m (JDK)  
-XX:MaxPermSize=256m (JDK)  
-XX:-DisableExplicitGC (JDK)  
-XX:CompileThreshold=8000 (JDK)  
-Djava.awt.headless=true (JDK)  
-Djava.net.preferIPv4Stack=true (needed if sending email and using Java 1.7+)  
 -d64 (JDK - for 64-bit JVMs only)

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) The Java heap space setting, -Xmx4096m, shown above and in individual sections below is sufficient for a *minimal* development system, *not* for a production system. A setting more appropriate for a 64-bit production server would be something
like -Xmx8192m. Consult your production server administrator.

64-bit JVMs require the -d64 flag in the Performance Settings to force the JVM to use 64-bit addressing.

## JConsole Settings (optional, for monitoring)

-Dcom.sun.management.jmxremote  
 -Djava.rmi.server.hostname=*<your host ip addr>*  
 -Dcom.sun.management.jmxremote.port=1099  
 -Dcom.sun.management.jmxremote.authenticate=false  
 -Dcom.sun.management.jmxremote.ssl=false  
 -Dnashorn.args="--no-deprecation-warning" (for JDK 11/12 only, to reduce console noise)

The JDK includes the Java Monitoring and Management Console (**JConsole**) tool. It uses the extensive instrumentation of the Java virtual machine to provide information on the performance and resource consumption of applications running on the Java platform using Java Management Extension (JMX) technology. For more information about JConsole, see [this article](http://java.sun.com/javase/7/docs/technotes/guides/management/jconsole.html).

## Tracing Settings (optional, for testing)

-verbose:gc  
 -Xprof  
 -XX:-CITime  
 -XX:-PrintCompilation  
-Xloggc:$CATALINA\_HOME/logs/gc.log  
 -XX:+PrintGCDetails  
 -XX:+PrintGCTimeStamps

The $CATALINA\_HOME environment variable in the example refers to the folder into which Apache-Tomcat has been installed; for other web servers substitute the appropriate variable.

## About the Performance Settings

What do the Performance Settings recommended above actually do? Here's an explanation:

| Setting | Description |
| --- | --- |
| -server | This option instructs the launcher to run the Java JVM in Server Mode. The JVM can optimize a number of things for server environments, improving performance. |
| -Xmx | This option sets the maximum amount of memory that can be allocated to the JVM heap, improving performance. Minimum requiredment is 4096 MB (4GB). |
| -XX:MaxPermSize | This option sets the maximum amount of memory that can be used for the permanent generation, or "PermGen", Java's fixed block of memory for loading class files. Failure to set this to at least 128m will cause errors to occur and a setting of 256m is recommended. |
| -XX:-DisableExplicitGC | This option disables calls to the function System.gc(), which is often run explicitly by many classes. When it runs, it triggers a full garbage collection process, which consumes a lot of execution time and results in inefficient heap usage. When it's disabled, the JVM still performs garbage collection nonetheless, whenever necessary. |
| -XX:CompileThreshold | This option sets the number of method invocations/branches before compiling. The JVM usually waits for a method to be executed a certain number of times before it's compiled. Not compiling every method helps startup time and reduces RAM footprint. This option allows you to control that threshold. |
| -Djava.awt.headless | This option, when set to *true*, prevents graphics rendering code from assuming that a graphics console exists, avoiding any chance of encountering an obscure Java bug related to X-servers and graphics rendering. |

## "Hot Deployment" Caution

Be aware that Tomcat, JBOSS, WebLogic, and other servers that offer "Hot" or "Auto" deployment may produce errors when using Logi Studio wizards. If this deployment feature is enabled, the changes the wizard makes may be deployed before the wizard completes all of its steps, causing an error.

Typically, "Hello World"-type Logi apps will work fine in this environment but use of Studio wizards to build more complex apps will not.

To avoid this problem, either disable the hot or auto deployment feature (technique varies by server) or increase the "scan interval" used by the feature substantially.
