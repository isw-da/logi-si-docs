---
title: "Statement on Log4j and Log4Net Vulnerabilities"
id: 4415781801751
section: "Announcements"
category: "General"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415781801751-Statement-on-Log4j-and-Log4Net-Vulnerabilities
updated_at: 2022-11-09T03:59:20Z
---

# Statement on Log4j and Log4Net Vulnerabilities

### Summary

In the second week of December, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability.

## Timeline

### 12/28/2021 Log4j2 Versions 2.0 - 2.17.0 Vulnerability Update (CVE-2021-44832)

We are currently investigating the latest CVE announcement, and will provide mitigation steps as soon as they are available. Read more about this update by selecting the following link: [CVE - CVE-2021-44832.](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44832)

### 12/19/2021 10:00 PM EST Log4Net Vulnerability Update (CVE-2018-1285)

This update does affect some Izenda and Exago customers.

### 12/17/2021 .NET Impacts of Log4Net Discovered (CVE-2018-1285)

We are assessing the impact of this discovery. Read more about this update by selecting the following link: [NVD - CVE-2018-1285](https://nvd.nist.gov/vuln/detail/CVE-2018-1285).

### 12/16/2021 17:00 PM EST: Log4j 1.x Vulnerability Announced

It has been discovered that older versions of Log4j are also vulnerable to CVE-2021-4104. Read more about this update by selecting the following link: [CVE - CVE-2021-4104](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-4104).

See product specific sections for mitigation steps.

### 12/15/2021 13:00 PM EST: Additional Vulnerability (CVE-2021-45046) Identified

This vulnerability renders obsolete some of the mitigation approaches that were previously recommended, for some non-standard configurations. Notably, setting the system property "**log4j2.noFormatMsgLookup**" to "**true**" does NOT mitigate CVE-2021-45046. To learn more, please select the following link: [CVE - CVE-2021-45046](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-45046).

We have modified our product specific recommendations below.

### 12/13/2021 09:53 AM EST: Initial Remediation

We are working to fix the [Log4j vulnerability issue](https://blogs.apache.org/foundation/entry/apache-log4j-cves)[.](https://msrc-blog.microsoft.com/2021/12/11/microsofts-response-to-cve-2021-44228-apache-log4j2/ "https://msrc-blog.microsoft.com/2021/12/11/microsofts-response-to-cve-2021-44228-apache-log4j2/") Please open a support case if you have specific concerns, but you can use the information below to get started with your mitigation efforts:

* [Microsoft’s Response to CVE-2021-44228 Apache Log4j 2 – Microsoft Security Response Center](https://msrc-blog.microsoft.com/2021/12/11/microsofts-response-to-cve-2021-44228-apache-log4j2/ "https://msrc-blog.microsoft.com/2021/12/11/microsofts-response-to-cve-2021-44228-apache-log4j2/")
* [Log4Shell: critical vulnerability in Apache Log4j | Kaspersky official blog](https://www.kaspersky.com/blog/log4shell-critical-vulnerability-in-apache-log4j/43124/ "https://www.kaspersky.com/blog/log4shell-critical-vulnerability-in-apache-log4j/43124/")
* [Log4j – Apache Log4j Security Vulnerabilities](https://logging.apache.org/log4j/2.x/security.html "https://logging.apache.org/log4j/2.x/security.html")

## Logi Report Customers:

### 10/31/2022

Logi Report now provides a more robust and flexible logging system that implements the SLF4J (Simple Logging Facade for Java) solution, enabling you to plug in the logging framework you want to use easily. For more information, see [Configuring the Logging System](https://devnet.logianalytics.com/hc/en-us/articles/5735516331543-Configuring-the-Logging-System).

### 2/20/2022 2:00 PM EST: Update for CVE-2021-4104

Log4j 1.x has reached end of life, see: <https://logging.apache.org/log4j/1.2/> customers using Report versions below v14.5 should upgrade to version 15.5 or higher to resolve this log4j vulnerability.

To mitigate this issue while staying on the same version, you should remove the class JMSAppender from log4j jars: zip -q -d log4j-\*.jar org/apache/log4j/net/JMSSink.class

Read more about this update by selecting the following link: <https://www.cvedetails.com/cve/CVE-2021-4104/>.

### 2/20/2022 2:00 PM EST: Update for CVE-2022-23302

Log4j 1.x has reached end of life, see: <https://logging.apache.org/log4j/1.2/> customers using Report versions below v14.5 should upgrade to version 15.5 or higher to resolve this log4j vulnerability.

To mitigate this issue while staying on the same version, you should perform the following steps:

1. Comment or remove JMSSink in your log4j configuration.
2. Remove the class JMSSink from log4j jars : zip -q -d log4j-\*.jar org/apache/log4j/net/JMSSink.class
3. Restrict the access of system users to the application platform to prevent attackers from modifying the configuration of log4j.

Read more about this update by selecting the following link: <https://www.cvedetails.com/cve-details.php?t=1&cve_id=CVE-2022-23302>.

### 2/20/2022 2:00 PM EST: Update for CVE-2022-23305

Log4j 1.x has reached end of life, see: <https://logging.apache.org/log4j/1.2/> customers using Report versions below v14.5 should upgrade to version 15.5 or higher to resolve this log4j vulnerability.

To mitigate this issue while staying on the same version, you should remove the use of JDBCAppender from your log4j configuration file.

Read more about this update by selecting the following link: <https://www.cvedetails.com/cve-details.php?t=1&cve_id=CVE-2022-23305>.

### 2/20/2022 2:00 PM EST: Update for CVE-2022-23307

Log4j 1.x has reached end of life, see: <https://logging.apache.org/log4j/1.2/> customers using Report versions below v14.5 should upgrade to version 15.5 or higher to resolve this log4j vulnerability.

To mitigate this issue while staying on the same version, you should not configure chainsaw to read serialized log events. Other receivers can be used, such as xmlsocketreceiver.

Read more about this update by selecting the following link: <https://www.cvedetails.com/cve-details.php?t=1&cve_id=CVE-2022-23307>.

### 12/29/2021 23:00 PM EST: Update for CVE-2021-44832

Read more about this update by selecting the following link: [CVE - CVE-2021-44832.](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44832)

If you are using Logi Report version >= v15.5 (log4j 2.9.1), you can swap out your older version of Log4j jars with the latest one, released by Apache (v2.17.1) to mitigate this vulnerability.

We will be including Log4j v2.17.1 in the next Service Pack release for Logi Report, as well as Logi Report v18.3, scheduled for the end of January, 2022.

### 12/22/2021 23:00 PM EST: Update for CVE-2021-45105

Read more about this update by selecting the following link: [CVE - CVE-2021-45105.](https://logging.apache.org/log4j/2.x/security.html#CVE-2021-45105)

You can mitigate this vulnerability as follows:

* If you are using Logi Report version >= v15.5 (log4j 2.9.1), the recommended fix for this vulnerability is swapping out your older version of Log4j jars with the latest one, released by Apache (v2.17.1). Alternatively, you can mitigate this infinite recursion issue in configuration:
  + In PatternLayout in the logging configuration, replace Context Lookups like ${ctx:loginId} or $${ctx:loginId} with Thread Context Map patterns (%X, %mdc, or %MDC).
  + Otherwise, in the configuration, remove references to Context Lookups like ${ctx:loginId} or $${ctx:loginId} where they originate from sources external to the application such as HTTP headers or user input.
* If you are using Logi Report version >=14.5 and <15.5 (log4j 2.7), you can mitigate this infinite recursion issue in configuration by taking either of the preceding methods.
* If you are using Logi Report version <14.5 (log4j 1.2.8), you are not impacted.

### 12/16/2021 17:00 PM EST: Log4j 1.x Vulnerability Announced. Affect on Report Customers

The latest vulnerability update announced today might affect Logi Report customers using Log4j 1.x versions. Read more about this update by selecting the following link: [CVE - CVE-2021-4104](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-4104).

### 12/13/2021 09:53 AM EST: Initial Remediation for Report Customers

We will issue fixes for CVE-2021-44228 and CVE-2021-45046 in upcoming Service Packs. If you are one of the customers that might be affected by these vulnerabilities, before applying a Service Pack that contains the fix, you can mitigate CVE-2021-44228 and CVE-2021-45046 as follows:

* If you are using Logi Report version >= v15.5 (log4j 2.9.1), you can:  
  + Swap out your older version of Log4j jars with the latest one, released by Apache (v2.17.1). This is the preferred solution.
  + Remove the JndiLookup class from the classpath (example: zip -q -d log4j-core-\*.jar org/apache/logging/log4j/core/lookup/JndiLookup.class).

* If you are using Logi Report version >=14.5 and <15.5 (log4j 2.7), you can remove the JndiLookup class from the classpath (example: zip -q -d log4j-core-\*.jar org/apache/logging/log4j/core/lookup/JndiLookup.class).
* If you are using Logi Report version <14.5 (log4j 1.2.8), you are not impacted.

## Logi Info Customers:

Customers on the latest version of Logi Info (14.1) are not affected since it ships with Log4j v 2.17.1.  
Only Logi Info JAVA customers on earlier versions of Info who are using Log4j for logging debug messages will be potentially affected by the Log4j related issues.

### 12/20/2021 13:00 PM EST CVE-2021-45105 Log4j Update: Affect for Logi Info

We will issue fixes for CVE-2021-45105, along with previously listed vulnerabilities, by replacing older Log4j implementations with Log4j v2.17.0. You also have the option to swap out your older version of Log4j jars with the latest one, released by Apache (v2.17.0). Swapping out the jars is the best immediate solution. This specifically addresses the issue where Apache Log4j  versions 2.0-alpha1 through 2.16.0 (excluding 2.12.3) did not protect from uncontrolled recursion from self-referential lookups. Using these older versions of Log4j allows an persons with control over Thread Context Map data to cause a denial of service attack when a crafted string is interpreted.

### 12/17/2021 13:00 PM EST CVE-2018-1285 Log4Net Update: Affect for Logi Info

CVE-2018-1285 does not seem to be an issue in Logi Info since the Studio developer sets the location of this config file and edits the contents. This file is not available to end users (and potential attackers) to modify.

Logi Info versions earlier than 12.8 do not contain Log4Net.

### 12/16/2021 17:00 PM EST: Log4j 1.x Vulnerability Announced, Should not Affect Info Customers

The latest vulnerability update announced today does not affect Logi Info customers using Log4j 1.x versions. Read more about this update by selecting the following link: [CVE - CVE-2021-4104](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-4104).

### 12/13/2021 09:53 AM EST: Initial Remediation for Info Users

Note that we only started shipping Log4j v2.x with Info version 12.8, so if you are on a previous version of Info you should not be impacted since Log4j 1.x is not affected by this.

We will issue fixes for CVE-2021-44228 and CVE-2021-45046 in upcoming Service Packs. If you are one of the customers that might be affected by these vulnerabilities, before applying a Service Pack that contains the fix you can mitigate CVE-2021-44228 and CVE-2021-45046 by either:

* Swapping out your older version of Log4j jars with the latest one, released by Apache (v2.17.0) (this is the preferred solution), or
* Removing the JndiLookup class from the classpath (example: zip -q -d log4j-core-\*.jar org/apache/logging/log4j/core/lookup/JndiLookup.class).

## LPS and Discovery Customers:

### 1/06/2022 4:00 PM EST LPS and Discovery CVE-2021-4104

We did an inspection for the Log4j usage.  For Logi Platform Services 3.3 and Discovery 3.2 (SSM): Log4j 1.2.17 (inside the uberjar dataservice-1.0.0.jar), the flaw highlights Log4j versions 2.x, **not** version 1.x, which is past its end of life. In the cases listed above, we did not find the problem class 'JndiLookup'.

Discovery and LPS did not use JMSAppender in DataServices. LPS and Discovery customers should not be concerned about the log4j 1.2 vulnerability described in CVE-2021-4104.

## Composer Customers:

### 5/12/2022 9:00 AM EST: Composer and CVE-2021-44228

Composer uses a Log4j API via various 3d party dependencies, but never relies on the Log4j appender implementation or write path. All the logs are written using Logback logger implementation. Composer v6.9.20 and higher, and Composer v7.10 and higher releases going forward will not include a version of the Log4j implementation libraries.

### 12/24/2021 9:00 AM EST: Composer and CVE-2021-44228

Composer uses a Log4j API via various 3d party dependencies, but never relies on the Log4j appender implementation or write path. All the logs are written using Logback logger implementation.

Log4j implementation jars are bundled with the platform as the side effect and will be removed in an upcoming release.

Before the next update is available, you can remove Log4j *implementation* jar files (log4j-1.2.17.jar and log4j-core-2.12.1.jar) manually from the service jar bundle for safety (zoomdata.jar/BOOT-INF/lib).

There are also *API* jar files present (log4j-api-2.12.1.jar, log4j-over-slf4j-1.7.30.jar, log4j-to-slf4j-2.12.1.jar). These cannot be removed, as they provide a compatibility layer for the external dependencies relying on the Log4j API. They serve as a gateway to send actual log data to the Logback logger).

Logi Composer binaries 4.9.x, 5.9.x, 6.9.x and 7.x are not affected by this issue.

### 12/16/2021 4:00 AM EST: Composer and CVE-2021-45046 or CVE-2021-4104

Currently, we have no evidence that CVE-2021-45046 or CVE-2021-4104 affect Composer customers.

## Izenda Customers:

Currently, we have no evidence that CVE-2021-44228, CVE-2021-45046 or CVE-2021-4104 affect Izenda customers.

### 12/19/2021 10:00 PM EST Log4Net Vulnerability Update (CVE-2018-1285)

Impacts of this vulnerability have been assessed for Izenda and Exago, along with mitigation steps.

**Izenda 6 Series impact and mitigation:** Log4net is configurable via web.config, which should not be directly accessible remotely. But we are issuing the following workaround:

1. Download [Apache log4net v2.0.13](https://logging.apache.org/log4net/download_log4net.html).

2. Do the following change in web.config:

```
<runtime>  
<assemblyBinding>  
<dependentAssembly>  
        <assemblyIdentity name="log4net" publicKeyToken="669e0ddf0bb1aa2a" culture="neutral" />  
        <bindingRedirect oldVersion="0.0.0.0-2.0.13.0" newVersion="2.0.13.0" />  
 </dependentAssembly>  
</assemblyBinding>  
</runtime>
```

3. Restart your webserver in all required Izenda hosted nodes.

**Izenda 7 Series impacts and mitigation:** Only versions v3.x.x and Prior are affected.

* Izenda 7 (aspnet) - log4net 2.0.13.0-.NET 4.5
* Izenda 7 (aspnetcore) - log4net 2.0.13.0-.NET Standard 2.0

1. Download [Apache log4net v2.0.13](https://logging.apache.org/log4net/download_log4net.html).

2. For Izenda 7 (aspnet) - log4net 2.0.13.0-.NET 4.5 do below change in web.config:

```
<runtime>  
<assemblyBinding>  
<dependentAssembly>  
        <assemblyIdentity name="log4net" publicKeyToken="669e0ddf0bb1aa2a" culture="neutral" />  
        <bindingRedirect oldVersion="0.0.0.0-2.0.13.0" newVersion="2.0.13.0" />  
 </dependentAssembly>  
</assemblyBinding>  
</runtime>
```

3. Restart the webserver in all required izenda hosted nodes.

## Exago Customers

Currently, we have no evidence that CVE-2021-44228, CVE-2021-45046 or CVE-2021-4104 affect Exago customers.

### 12/19/2021 10:00 PM EST Log4Net Vulnerability Update (CVE-2018-1285)

**Exago impact and Mitigation:** The latest version of Exago is not impacted. Log4net is configurable via <WebApp>/Config/log4net.config as well as <Scheduler>/eWebReportsScheduler.exe.config.  Neither of these files should be directly accessible remotely.

Here is mitigation for versions v202.1 and lower.

1. Download log4net v2.0.12.

2. Add a dependent override to the <runtime><assemblyBinding> section of the <WebApp>/web.config, <Scheduler>/eWebReportsScheduler.exe.config, and Monitoring/Monitoring.exe.config (where applicable):

```
<runtime>  
<assemblyBinding>  
<dependentAssembly>  
        <assemblyIdentity name="log4net" publicKeyToken="669e0ddf0bb1aa2a" culture="neutral" />  
        <bindingRedirect oldVersion="0.0.0.0-2.0.12.0" newVersion="2.0.12.0" />  
 </dependentAssembly>  
</assemblyBinding>  
</runtime>
```

3. Restart the web app, web service, scheduler, and Monitoring service.

**\*\*PLEASE WATCH THIS PAGE!**

We are updating this article as new details are finalized.
