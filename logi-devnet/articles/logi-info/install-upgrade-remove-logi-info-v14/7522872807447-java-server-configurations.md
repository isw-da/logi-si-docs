---
title: "Java Server Configurations"
id: 7522872807447
section: "Install, Upgrade, & Remove - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/7522872807447-Java-Server-Configurations
updated_at: 2022-07-17T02:04:57Z
---

# Java Server Configurations

# Java Server Configurations

Logi products work with a variety of Java-based web servers, which often require
specific configurations to work correctly and for optimum performance.

The following topics provide the details of these configurations for each server, including:

* [Setting Java Options](https://devnet.logianalytics.com/hc/en-us/articles/4419723050903-Setting-Java-Options#Options)
* [Apache-Tomcat 5.5 / 6 / 7 / 8](https://devnet.logianalytics.com/hc/en-us/articles/4419723046935-Apache-Tomcat-5-5-6-7-8-9#Apache)/ 9
* [JBoss 7.1](https://devnet.logianalytics.com/hc/en-us/articles/4419707723031-JBoss-7-1#JBoss7)
* [JBoss 5.1](https://devnet.logianalytics.com/hc/en-us/articles/4419723049879-JBoss-5-1#JBoss51)
* [JBoss 4](https://devnet.logianalytics.com/hc/en-us/articles/4419707722007-JBoss-4#JBoss4)
* [Glassfish 4.1](https://devnet.logianalytics.com/hc/en-us/articles/4419723048855-Glassfish-4-1-#GF41)
* [Glassfish 3.0 / 3.1/ 4.0](https://devnet.logianalytics.com/hc/en-us/articles/4419715396887-Glassfish-3-0-3-1-4-0#GF3)
* [Glassfish 2.1](https://devnet.logianalytics.com/hc/en-us/articles/4419723047959-Glassfish-2-1#GF21)
* [WebLogic 12c](https://devnet.logianalytics.com/hc/en-us/articles/4419715399191-WebLogic-12c#WebLogi12c)
* [WebLogic 10](https://devnet.logianalytics.com/hc/en-us/articles/4419715398295-WebLogic-10#WebLogi10)
* [Websphere 7 / 8.5](https://devnet.logianalytics.com/hc/en-us/articles/4419715400087-Websphere-7-8-5#Websphere)
* [WildFly 8 / 9 / 10](https://devnet.logianalytics.com/hc/en-us/articles/4419715401111-WildFly-8-9-10#WildFly)

Please note the following important information:

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) Oracle has changed its Java usage policies - see [Java Usage Policy](https://devnet.logianalytics.com/hc/en-us/articles/4419723053335-Java-Usage-Policy) for important information.

* The Oracle JDK or OpenJDK 7, 8, 11, 12, 13, or 14 is *required* for non-Apple platforms, or as noted in individual configuration topics linked above. JDK 7 is *required* for Apple platforms. The JRE is not sufficient.
* It's *possible* to use Logi products on systems that use symbolic links or the Filesystem Hierarchy Standard (FHS), but it makes configuration much more complicated and *we don't recommend it*.
* When Logi Studio creates a new application, it's deployed in exploded format within a single "Logi application folder", not as a WAR file. WAR deployments by Studio are not supported at this time.
* We no longer distribute the ojdbc6.jar. Info Java includes hardcoded references to certain Oracle datatypes, which are referenced in the Oracle JDBC driver. To allow Info Java to compile we included LogiSTUB.jar. This jar replaces ojdbc6.jar, but only to allow Info to run; it does not allow Oracle data to actually be retrieved. To retrieve Oracle data, download ojdbc8.jar and delete LogiSTUB.jar.

JDK/OpenJDK 11 is supported starting with this version but its use requires these configuration steps:

1. In JVM options, set --illegal-access=permit
2. In the server's server.xml file, set relaxedQueryChars="[]"
3. Copy *<LogiAppFolder>*/rdTemplate/Java11/jaxb-api-2.4.0-b180830.0359.jar to *<LogiAppFolder>*/WEB-INF/lib.

JDK/OpenJDK 11 and higher are supported starting with Info v12.7 but its use requires these configuration steps:

1. In JVM options, set --illegal-access=permit and -Dnashorn.args="--no-deprecation-warning"
2. In the server's server.xml file, set relaxedQueryChars="[]{}|" in the connector elements.
3. Copy <LogiAppFolder>/rdTemplate/Java11/jaxb-api-2.4.0-b180830.0359.jar to <LogiAppFolder>/WEB-INF/lib
4. Copy <LogiAppFolder>/rdTemplate/Java11/javax.activation-1.2.0.jar to <LogiAppFolder>/WEB-INF/lib

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) PhantomJS in Linux, as we distribute, is complete. There is no requirement to install Qt, WebKit, or any other libraries. However, it still relies on Fontconfig (the package Fontconfig or Libfontconfig, depending on the distribution). Normally, this is present; however, if you run PhantomjJS and receive a 127 error you need to complete another step. Navigate to the application root/WEB-INF/lib directory and enter "ldd phantomjs". All the referenced libraries appear. If a version of Fontconfig does not appear then it must be installed. FontConfig installation instructions for various distros vary. The Ubuntu instructions are included here:

sudo apt-get update -y

sudo apt-get install -y fontconfig-config

For more information, see <https://phantomjs.org/download> and <https://www.freedesktop.org/wiki/Software/fontconfig/>.
